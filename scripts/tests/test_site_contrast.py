from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CSS = (ROOT / "site" / "styles.css").read_text(encoding="utf-8")


def color(name: str) -> tuple[float, float, float]:
    match = re.search(rf"--{re.escape(name)}:\s*(#[0-9a-fA-F]{{6}})", CSS)
    if match is None:
        raise AssertionError(f"Missing CSS color token: {name}")
    value = match.group(1)
    return tuple(int(value[index : index + 2], 16) / 255 for index in (1, 3, 5))


def luminance(value: tuple[float, float, float]) -> float:
    def channel(component: float) -> float:
        if component <= 0.04045:
            return component / 12.92
        return ((component + 0.055) / 1.055) ** 2.4

    return sum(weight * channel(component) for weight, component in zip((0.2126, 0.7152, 0.0722), value))


def contrast(
    foreground: tuple[float, float, float],
    background: tuple[float, float, float],
) -> float:
    lighter, darker = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def blend(
    foreground: tuple[float, float, float],
    background: tuple[float, float, float],
    alpha: float,
) -> tuple[float, float, float]:
    return tuple(
        alpha * foreground_component + (1 - alpha) * background_component
        for foreground_component, background_component in zip(foreground, background)
    )


def rule(selector: str) -> str:
    match = re.search(rf"{re.escape(selector)}\s*\{{(.*?)\}}", CSS, re.DOTALL)
    if match is None:
        raise AssertionError(f"Missing CSS rule: {selector}")
    return match.group(1)


def white_alpha(selector: str) -> float:
    match = re.search(r"color:\s*rgb\(255 255 255 / (\d+)%\)", rule(selector))
    if match is None:
        raise AssertionError(f"Missing white alpha color in {selector}")
    return int(match.group(1)) / 100


class SiteContrastTests(unittest.TestCase):
    def test_focus_indicator_has_a_contrasting_ring_on_every_surface(self) -> None:
        focus_rule = rule(":focus-visible")
        self.assertIn("outline: 3px solid var(--ink)", focus_rule)
        self.assertIn("outline-offset: 4px", focus_rule)
        self.assertIn("box-shadow: 0 0 0 7px var(--white)", focus_rule)

        ink = color("ink")
        white = color("white")
        self.assertGreaterEqual(contrast(ink, white), 3)
        for surface in ("paper", "signal", "sky", "blue", "coral-deep"):
            background = color(surface)
            self.assertGreaterEqual(max(contrast(ink, background), contrast(white, background)), 3)

    def test_flagship_copy_and_labels_meet_text_contrast(self) -> None:
        white = (1.0, 1.0, 1.0)
        blue = color("blue")
        for selector in (
            ".flagship-copy > p:not(.eyebrow)",
            ".flagship-stats span",
        ):
            foreground = blend(white, blue, white_alpha(selector))
            self.assertGreaterEqual(contrast(foreground, blue), 4.5)

    def test_flagship_accent_chip_meets_text_contrast(self) -> None:
        self.assertIn("background: var(--coral-deep)", rule(".route-accent"))
        self.assertGreaterEqual(contrast((1.0, 1.0, 1.0), color("coral-deep")), 4.5)


if __name__ == "__main__":
    unittest.main()
