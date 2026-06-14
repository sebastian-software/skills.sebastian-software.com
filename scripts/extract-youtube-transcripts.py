#!/usr/bin/env python3
import json
import sys
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi


def compact(value: str) -> str:
    return " ".join(str(value or "").split())


def main() -> None:
    input_path = Path(sys.argv[1] if len(sys.argv) > 1 else "reports/things-skill-source-discovery-2026-06-14.json")
    output_path = Path(sys.argv[2] if len(sys.argv) > 2 else "reports/things-youtube-transcripts-frontend-2026-06-14.json")
    targets = set((sys.argv[3] if len(sys.argv) > 3 else "ui-design,react,web-performance,frontend-testing").split(","))

    discovery = json.loads(input_path.read_text())
    candidates = [
        candidate
        for candidate in discovery["candidates"]
        if candidate.get("kind") == "youtube" and candidate.get("youtubeId") and candidate.get("target") in targets
    ]

    api = YouTubeTranscriptApi()
    results = []
    for index, candidate in enumerate(candidates, start=1):
        try:
            fetched = api.fetch(candidate["youtubeId"], languages=["en", "de"])
            transcript = compact(" ".join(snippet.text for snippet in fetched))
            result = {
                **candidate,
                "ok": bool(transcript),
                "language": getattr(fetched, "language_code", ""),
                "isGenerated": getattr(fetched, "is_generated", None),
                "wordCount": len(transcript.split()) if transcript else 0,
                "transcript": transcript,
                "excerpt": transcript[:2500],
            }
        except Exception as error:
            result = {
                **candidate,
                "ok": False,
                "error": f"{type(error).__name__}: {str(error)[:500]}",
                "wordCount": 0,
                "transcript": "",
                "excerpt": "",
            }
        results.append(result)
        if index % 10 == 0 or index == len(candidates):
            print(f"{index}/{len(candidates)}", file=sys.stderr)

    payload = {
        "inputPath": str(input_path),
        "targets": sorted(targets),
        "candidates": len(candidates),
        "ok": sum(1 for result in results if result["ok"]),
        "results": results,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(json.dumps({"outputPath": str(output_path), "candidates": payload["candidates"], "ok": payload["ok"]}, indent=2))


if __name__ == "__main__":
    main()
