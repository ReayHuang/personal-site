#!/usr/bin/env python3
"""Build Open Graph previews for explosion protection notes (1200 x 630 JPEG)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC_EN = ROOT / "assets/images/maritime/explosion-protection-preview-source.en.png"
SRC_ZH = ROOT / "assets/images/maritime/explosion-protection-preview-source.zh-Hant.png"
OUT_EN = ROOT / "assets/images/maritime/explosion-protection-linkedin-preview.en-1200.jpg"
OUT_ZH = ROOT / "assets/images/maritime/explosion-protection-linkedin-preview-1200.jpg"

W, H = 1200, 630


def export_og(source: Path, output: Path) -> None:
    if not source.exists():
        raise FileNotFoundError(f"Missing source image: {source}")

    img = Image.open(source).convert("RGB")
    img = img.resize((W, H), Image.Resampling.LANCZOS)
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, "JPEG", quality=92, optimize=True)
    print(f"Wrote {output} ({W}x{H}) from {source.name}")


def main() -> None:
    export_og(SRC_EN, OUT_EN)
    export_og(SRC_ZH, OUT_ZH)


if __name__ == "__main__":
    main()
