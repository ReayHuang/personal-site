#!/usr/bin/env python3
"""Generate minimalist Open Graph previews for explosion protection notes (1200 x 630)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_EN = ROOT / "assets/images/maritime/explosion-protection-linkedin-preview.en-1200.jpg"
OUT_ZH = ROOT / "assets/images/maritime/explosion-protection-linkedin-preview-1200.jpg"

W, H = 1200, 630

COLORS = {
    "bg": (247, 249, 252),
    "paper": (255, 255, 255),
    "ink": (31, 41, 55),
    "muted": (100, 116, 139),
    "brand": (11, 58, 91),
    "brand_2": (21, 94, 147),
    "brand_soft": (232, 243, 251),
    "line": (216, 224, 234),
}

COPY = {
    "en": {
        "eyebrow": "Reay Huang Maritime Notes",
        "title": ("Hazardous Area", "Explosion Protection"),
        "subtitle": "Ex markings · Protection types · Gas groups · Temperature classes · Zones",
        "chips": ["Ex", "IEC 60079", "Zone 0–2", "Verification"],
        "footer": "reayhuang.com · Maritime Notes",
    },
    "zh": {
        "eyebrow": "Reay Huang Maritime Notes",
        "title": ("危險區域防爆設備分類",),
        "subtitle": "Ex 防爆等級、保護型式與實務",
        "chips": ["Ex", "標示", "保護型式", "氣體群組", "溫度等級", "Zone 分區"],
        "footer": "reayhuang.com · 海事筆記",
    },
}


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def load_cjk_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            try:
                index = 1 if bold and path.endswith(".ttc") else 0
                return ImageFont.truetype(path, size, index=index)
            except OSError:
                try:
                    return ImageFont.truetype(path, size)
                except OSError:
                    continue
    return load_font(size, bold)


def text_width(text: str, font: ImageFont.ImageFont) -> float:
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]


def wrap_lines(text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        trial = " ".join(current + [word])
        if text_width(trial, font) <= max_width or not current:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def wrap_lines_cjk(text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    segments = [part.strip() for part in text.split("·")]
    lines: list[str] = []
    current = ""
    for i, segment in enumerate(segments):
        piece = segment if i == 0 else f"· {segment}"
        for char in piece:
            trial = current + char
            if text_width(trial, font) <= max_width or not current:
                current = trial
            else:
                lines.append(current.strip())
                current = char
    if current.strip():
        lines.append(current.strip())
    return lines


def chip_labels(copy: dict) -> list[str]:
    chips = copy.get("chips") or []
    if chips:
        return chips
    description = copy.get("description", "")
    return description.split() if description else []


def layout_chip_rows(
    labels: list[str],
    *,
    start_x: int,
    max_x: int,
    font_chip: ImageFont.ImageFont,
) -> list[list[tuple[str, int, ImageFont.ImageFont]]]:
    pad_x = 16
    gap = 12
    rows: list[list[tuple[str, int, ImageFont.ImageFont]]] = []
    row: list[tuple[str, int, ImageFont.ImageFont]] = []
    row_width = 0

    for label in labels:
        chip_font = load_font(20, bold=True) if label.isascii() else font_chip
        cw = int(text_width(label, chip_font) + pad_x * 2)
        extra = gap if row else 0
        if row and row_width + extra + cw > max_x - start_x:
            rows.append(row)
            row = []
            row_width = 0
            extra = 0
        row.append((label, cw, chip_font))
        row_width += extra + cw

    if row:
        rows.append(row)
    return rows


def draw_chip_rows(
    draw: ImageDraw.ImageDraw,
    rows: list[list[tuple[str, int, ImageFont.ImageFont]]],
    *,
    start_x: int,
    start_y: int,
) -> None:
    pad_x, pad_y = 16, 10
    chip_h = 38
    row_gap = 10
    gap = 12
    y = start_y

    for row in rows:
        x = start_x
        for label, cw, chip_font in row:
            draw.rounded_rectangle(
                [x, y, x + cw, y + chip_h],
                radius=chip_h // 2,
                fill=COLORS["brand_soft"],
                outline=COLORS["line"],
                width=1,
            )
            draw.text((x + pad_x, y + pad_y - 2), label, font=chip_font, fill=COLORS["brand"])
            x += cw + gap
        y += chip_h + row_gap


def compose(locale: str, output: Path) -> None:
    copy = COPY[locale]
    use_cjk = locale == "zh"

    base = Image.new("RGBA", (W, H), (*COLORS["bg"], 255))
    wash = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(wash).ellipse([720, -80, 1280, 360], fill=(*COLORS["brand_2"], 28))
    img = Image.alpha_composite(base, wash).convert("RGB")
    draw = ImageDraw.Draw(img)

    card_margin = 72
    card = [card_margin, 88, W - card_margin, H - 88]
    draw.rounded_rectangle(card, radius=28, fill=COLORS["paper"], outline=COLORS["line"], width=2)

    accent_x = card[0] + 36
    draw.rounded_rectangle(
        [accent_x, card[1] + 44, accent_x + 6, card[3] - 44],
        radius=3,
        fill=COLORS["brand"],
    )

    x = accent_x + 32
    y = card[1] + 52

    font_eyebrow = load_font(20, bold=True)
    font_title = load_cjk_font(52, bold=True) if use_cjk else load_font(58, bold=True)
    font_sub = load_cjk_font(28, bold=True) if use_cjk else load_font(26, bold=False)
    font_chip = load_cjk_font(20, bold=True) if use_cjk else load_font(20, bold=True)
    font_footer = load_cjk_font(20, bold=False) if use_cjk else load_font(20, bold=False)

    eyebrow = copy["eyebrow"]
    pill_pad_x, pill_pad_y = 18, 10
    pill_w = text_width(eyebrow, font_eyebrow) + pill_pad_x * 2
    pill_h = 40
    draw.rounded_rectangle(
        [x, y, x + pill_w, y + pill_h],
        radius=pill_h // 2,
        fill=COLORS["brand_soft"],
    )
    draw.text((x + pill_pad_x, y + pill_pad_y - 2), eyebrow, font=font_eyebrow, fill=COLORS["brand_2"])
    y += pill_h + 28

    title_line_h = 68 if use_cjk else 68
    for line in copy["title"]:
        draw.text((x, y), line, font=font_title, fill=COLORS["brand"])
        y += title_line_h

    y += 10
    max_sub_w = card[2] - x - 48
    subtitle_color = COLORS["brand_2"] if use_cjk else COLORS["muted"]
    subtitle_wrap = wrap_lines if copy.get("description") else (wrap_lines_cjk if use_cjk else wrap_lines)
    for line in subtitle_wrap(copy["subtitle"], font_sub, max_width=max_sub_w):
        draw.text((x, y), line, font=font_sub, fill=subtitle_color)
        y += 36

    labels = chip_labels(copy)
    if labels:
        chip_rows = layout_chip_rows(labels, start_x=x, max_x=card[2] - 48, font_chip=font_chip)
        chip_h = 38
        row_gap = 10
        chip_block_h = len(chip_rows) * chip_h + max(0, len(chip_rows) - 1) * row_gap
        footer_y = card[3] - 52
        chip_y = footer_y - 16 - chip_block_h
        draw_chip_rows(draw, chip_rows, start_x=x, start_y=chip_y)

    footer = copy["footer"]
    footer_font = load_font(20, bold=False) if footer.isascii() else font_footer
    if " · " in footer:
        prefix, suffix = footer.split(" · ", 1)
        suffix_font = font_footer if use_cjk else footer_font
        footer_w = text_width(prefix, footer_font) + text_width(" · ", footer_font) + text_width(suffix, suffix_font)
        footer_x = card[2] - 48 - footer_w
        footer_y = card[3] - 52
        draw.text((footer_x, footer_y), prefix, font=footer_font, fill=COLORS["muted"])
        sep_x = footer_x + text_width(prefix, footer_font)
        draw.text((sep_x, footer_y), " · ", font=footer_font, fill=COLORS["muted"])
        draw.text((sep_x + text_width(" · ", footer_font), footer_y), suffix, font=suffix_font, fill=COLORS["muted"])
    else:
        draw.text(
            (card[2] - 48 - text_width(footer, footer_font), card[3] - 52),
            footer,
            font=footer_font,
            fill=COLORS["muted"],
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, "JPEG", quality=92, optimize=True, subsampling=0)
    print(f"Wrote {output} ({W}x{H})")


def main() -> None:
    compose("en", OUT_EN)
    compose("zh", OUT_ZH)


if __name__ == "__main__":
    main()
