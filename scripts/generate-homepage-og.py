#!/usr/bin/env python3
"""Generate homepage Open Graph preview images (1200 x 630)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
PORTRAIT = ROOT / "assets/images/reay-huang.png"
SHIP_SOURCE = ROOT / "assets/images/source/container-ship-bow.png"
OUT_EN = ROOT / "assets/images/homepage-linkedin-preview-reay-huang.en-1200.jpg"
OUT_ZH = ROOT / "assets/images/homepage-linkedin-preview-reay-huang-1200.jpg"

W, H = 1200, 630

# Layout columns (px): portrait | gap | text | ship backdrop
PORTRAIT_X = 48
PORTRAIT_W = 326
TEXT_X = 420
TEXT_MAX_W = 380
DIVIDER_X = 396

COLORS = {
    "navy": (7, 13, 25),
    "hero": (13, 70, 101),
    "teal": (0, 197, 183),
    "teal_dark": (0, 168, 156),
    "white": (255, 255, 255),
    "muted": (114, 123, 157),
    "light": (238, 245, 251),
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


def make_gradient() -> Image.Image:
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        for x in range(W):
            t_x = x / (W - 1)
            t_y = y / (H - 1)
            r = int(COLORS["navy"][0] * (1 - t_x) * 0.55 + COLORS["hero"][0] * t_x * 0.85 + COLORS["teal"][0] * t_x * t_y * 0.12)
            g = int(COLORS["navy"][1] * (1 - t_x) * 0.55 + COLORS["hero"][1] * t_x * 0.85 + COLORS["teal"][1] * t_x * t_y * 0.12)
            b = int(COLORS["navy"][2] * (1 - t_x) * 0.55 + COLORS["hero"][2] * t_x * 0.85 + COLORS["teal"][2] * t_x * t_y * 0.12)
            px[x, y] = (min(255, r), min(255, g), min(255, b))
    return img


def make_ship_lineart(target_w: int) -> Image.Image:
    """Convert the bow-view container ship photo into a stylized line drawing.

    Uses a difference-of-Gaussians approach for clean, expressive edges,
    then tints them so they sit naturally on the dark navy background.
    """
    src = Image.open(SHIP_SOURCE).convert("RGB")
    ratio = target_w / src.width
    target_h = int(src.height * ratio)
    src = src.resize((target_w, target_h), Image.Resampling.LANCZOS)

    gray = ImageOps.grayscale(src)
    gray = ImageOps.autocontrast(gray, cutoff=2)

    # Difference of Gaussians gives finer, more drawing-like edges than FIND_EDGES.
    blur_a = gray.filter(ImageFilter.GaussianBlur(radius=1.0))
    blur_b = gray.filter(ImageFilter.GaussianBlur(radius=3.5))
    dog = ImageChops.subtract(blur_a, blur_b, scale=1.0, offset=0)
    dog = ImageOps.autocontrast(dog, cutoff=1)
    dog = ImageEnhance.Brightness(dog).enhance(2.4)
    dog = ImageEnhance.Contrast(dog).enhance(1.8)

    # Soften jaggies slightly so lines feel hand-drawn rather than noisy.
    dog = dog.filter(ImageFilter.SMOOTH)

    # Crop the 1-pixel artefact ring left by the filters.
    dog = ImageOps.crop(dog, border=3)

    # Build an RGBA layer: white-teal ink, alpha driven by edge strength.
    ink_color = (180, 230, 230)
    alpha_map = dog.point(lambda p: min(255, int(p * 1.05)))
    rgba = Image.new("RGBA", dog.size, (*ink_color, 0))
    rgba.putalpha(alpha_map)
    return rgba


def prepare_portrait() -> Image.Image:
    """Portrait-shaped crop showing full face plus suit, tie, and LR pin."""
    portrait = Image.open(PORTRAIT).convert("RGBA")
    w, h = portrait.size
    # Trim sides moderately and keep nearly the full vertical range so the
    # face has headroom and the suit (lapel, tie, LR pin) stays visible.
    crop_w = int(w * 0.78)
    crop_h = int(h * 0.96)
    left = (w - crop_w) // 2
    top = int(h * 0.02)
    portrait = portrait.crop((left, top, left + crop_w, top + crop_h))

    scale = PORTRAIT_W / portrait.width
    target_w = PORTRAIT_W
    target_h = int(portrait.height * scale)
    portrait = portrait.resize((target_w, target_h), Image.Resampling.LANCZOS)

    mask = Image.new("L", portrait.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    inset = 6
    mask_draw.rounded_rectangle(
        [inset, inset, portrait.width - inset, portrait.height - inset],
        radius=18,
        fill=255,
    )
    portrait.putalpha(mask)
    return portrait


def draw_text_block(base: Image.Image, *, locale: str) -> None:
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Column divider — keeps portrait and text visually separate
    draw.rounded_rectangle(
        [DIVIDER_X, 88, DIVIDER_X + 4, H - 88],
        radius=2,
        fill=(*COLORS["teal"], 150),
    )

    font_brand = load_font(20, bold=True)
    font_name = load_font(50, bold=True)
    font_alias = load_font(28, bold=False)
    font_role = load_font(28, bold=True)
    font_tag = load_font(22, bold=False) if locale == "en" else load_cjk_font(22, bold=False)

    y = 96

    pill_text = "reayhuang.com"
    pill_w = draw.textlength(pill_text, font=font_brand) + 32
    draw.rounded_rectangle(
        [TEXT_X, y, TEXT_X + pill_w, y + 36],
        radius=16,
        outline=(*COLORS["teal"], 180),
        width=2,
        fill=(255, 255, 255, 18),
    )
    draw.text((TEXT_X + 16, y + 6), pill_text, font=font_brand, fill=COLORS["teal"])
    y += 56

    draw.text((TEXT_X, y), "Reay Huang", font=font_name, fill=COLORS["white"])
    y += 58
    draw.text((TEXT_X, y), "Marine Surveyor · PMP®", font=font_role, fill=COLORS["teal"])
    y += 48

    if locale == "en":
        tagline = "International survey, compliance,\nand professional maritime insights."
    else:
        tagline = "國際驗船、合規實務與\n海事專業知識分享"
    draw.multiline_text((TEXT_X, y), tagline, font=font_tag, fill=(*COLORS["light"], 230), spacing=6)

    base.alpha_composite(overlay)


def compose(locale: str, output: Path) -> None:
    base = make_gradient().convert("RGBA")
    portrait = prepare_portrait()

    # Ship line art in bottom-right (drawn before text so any text overlay sits on top)
    ship_lineart = make_ship_lineart(target_w=380)
    # Soften so the footer line stays legible on top of it
    fade = ship_lineart.split()[-1].point(lambda p: int(p * 0.78))
    ship_lineart.putalpha(fade)
    ship_x = W - ship_lineart.width - 28
    ship_y = H - ship_lineart.height - 14
    base.alpha_composite(ship_lineart, (ship_x, ship_y))

    portrait_y = (H - portrait.height) // 2
    frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    frame_draw = ImageDraw.Draw(frame)
    frame_draw.rounded_rectangle(
        [
            PORTRAIT_X - 8,
            portrait_y - 8,
            PORTRAIT_X + portrait.width + 8,
            portrait_y + portrait.height + 8,
        ],
        radius=18,
        fill=(255, 255, 255, 24),
        outline=(*COLORS["teal"], 130),
        width=2,
    )
    base.alpha_composite(frame)
    base.alpha_composite(portrait, (PORTRAIT_X, portrait_y))

    draw_text_block(base, locale=locale)

    vignette = Image.new("L", (W, H), 0)
    vdraw = ImageDraw.Draw(vignette)
    vdraw.ellipse([-120, -80, W + 120, H + 120], fill=180)
    vignette = vignette.filter(ImageFilter.GaussianBlur(80))
    dark = Image.new("RGBA", (W, H), (7, 13, 25, 0))
    dark.putalpha(Image.eval(vignette, lambda p: max(0, 100 - p // 3)))
    base.alpha_composite(dark)

    final = base.convert("RGB")
    final.save(output, "JPEG", quality=92, optimize=True, subsampling=0)
    print(f"Wrote {output} ({final.size[0]}x{final.size[1]})")


def main() -> None:
    compose("en", OUT_EN)
    compose("zh", OUT_ZH)


if __name__ == "__main__":
    main()
