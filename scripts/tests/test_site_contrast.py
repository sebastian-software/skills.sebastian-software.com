from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CSS = (ROOT / "site" / "styles.css").read_text(encoding="utf-8")


def palette_block(palette: str) -> str:
    if palette == "light":
        match = re.search(r":root\s*\{(.*?)\}", CSS, re.DOTALL)
    else:
        match = re.search(
            r"@media \(prefers-color-scheme: dark\)\s*\{\s*:root\s*\{(.*?)\}",
            CSS,
            re.DOTALL,
        )
    if match is None:
        raise AssertionError(f"Missing {palette} palette token block")
    return match.group(1)


PALETTES = ("light", "dark")


def color(name: str, palette: str = "light") -> tuple[float, float, float]:
    match = re.search(
        rf"--{re.escape(name)}:\s*(#[0-9a-fA-F]{{6}})", palette_block(palette)
    )
    if match is None:
        raise AssertionError(f"Missing CSS color token in {palette} palette: {name}")
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


def token_pair(selector: str) -> tuple[str, str]:
    """Return the (background, color) design tokens declared by a badge rule."""
    body = rule(selector)
    background = re.search(r"background:\s*var\(--([\w-]+)\)", body)
    foreground = re.search(r"color:\s*var\(--([\w-]+)\)", body)
    if background is None or foreground is None:
        raise AssertionError(f"Missing background/color token pair in {selector}")
    return background.group(1), foreground.group(1)


class SiteContrastTests(unittest.TestCase):
    def test_dark_palette_overrides_every_color_token(self) -> None:
        light_tokens = re.findall(r"--([\w-]+):\s*#[0-9a-fA-F]{6}", palette_block("light"))
        dark_tokens = re.findall(r"--([\w-]+):\s*#[0-9a-fA-F]{6}", palette_block("dark"))
        self.assertTrue(light_tokens)
        self.assertEqual(sorted(light_tokens), sorted(dark_tokens))

    def test_focus_indicator_has_a_contrasting_ring_on_every_surface(self) -> None:
        focus_rule = rule(":focus-visible")
        self.assertIn("outline: 3px solid var(--ink)", focus_rule)
        self.assertIn("outline-offset: 4px", focus_rule)
        self.assertIn("box-shadow: 0 0 0 7px var(--white)", focus_rule)

        for palette in PALETTES:
            with self.subTest(palette=palette):
                ink = color("ink", palette)
                white = color("white", palette)
                self.assertGreaterEqual(contrast(ink, white), 3)
                for surface in ("paper", "signal", "sky", "blue-surface", "coral-deep"):
                    background = color(surface, palette)
                    self.assertGreaterEqual(
                        max(contrast(ink, background), contrast(white, background)), 3
                    )

    def test_body_and_muted_text_meet_contrast_on_light_surfaces(self) -> None:
        for palette in PALETTES:
            with self.subTest(palette=palette):
                ink = color("ink", palette)
                muted = color("muted", palette)
                for surface in ("paper", "paper-soft", "white"):
                    background = color(surface, palette)
                    self.assertGreaterEqual(contrast(ink, background), 4.5)
                    self.assertGreaterEqual(contrast(muted, background), 4.5)

    def test_accent_text_tokens_meet_contrast(self) -> None:
        for palette in PALETTES:
            with self.subTest(palette=palette):
                blue = color("blue", palette)
                for surface in ("paper", "paper-soft", "white"):
                    self.assertGreaterEqual(contrast(blue, color(surface, palette)), 4.5)
                self.assertGreaterEqual(
                    contrast(color("accent-ink", palette), color("signal", palette)), 4.5
                )
                self.assertGreaterEqual(
                    contrast(color("signal", palette), color("blue-surface", palette)), 4.5
                )
                self.assertGreaterEqual(
                    contrast(color("ink", palette), color("sky", palette)), 4.5
                )

    def test_panel_surfaces_keep_readable_white_text(self) -> None:
        white = (1.0, 1.0, 1.0)
        for palette in PALETTES:
            with self.subTest(palette=palette):
                panel = color("panel", palette)
                self.assertGreaterEqual(contrast(white, panel), 4.5)
                copyright_text = blend(white, panel, white_alpha(".copyright"))
                self.assertGreaterEqual(contrast(copyright_text, panel), 4.5)

    def test_flagship_copy_and_labels_meet_text_contrast(self) -> None:
        white = (1.0, 1.0, 1.0)
        for palette in PALETTES:
            with self.subTest(palette=palette):
                blue_surface = color("blue-surface", palette)
                for selector in (
                    ".flagship-copy > p:not(.eyebrow)",
                    ".flagship-stats span",
                ):
                    foreground = blend(white, blue_surface, white_alpha(selector))
                    self.assertGreaterEqual(contrast(foreground, blue_surface), 4.5)

    def test_fit_badges_meet_text_contrast_in_both_palettes(self) -> None:
        for selector in (".fit-companion", ".fit-selective", ".fit-covered"):
            background_token, foreground_token = token_pair(selector)
            for palette in PALETTES:
                with self.subTest(selector=selector, palette=palette):
                    self.assertGreaterEqual(
                        contrast(
                            color(foreground_token, palette),
                            color(background_token, palette),
                        ),
                        4.5,
                    )

    def test_flagship_accent_chip_meets_text_contrast(self) -> None:
        self.assertIn("background: var(--coral-deep)", rule(".route-accent"))
        for palette in PALETTES:
            with self.subTest(palette=palette):
                self.assertGreaterEqual(
                    contrast((1.0, 1.0, 1.0), color("coral-deep", palette)), 4.5
                )


if __name__ == "__main__":
    unittest.main()
