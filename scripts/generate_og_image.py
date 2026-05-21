#!/usr/bin/env python3
"""Generate the default Pomegra Wiki Open-Graph card as a 1200x630 PNG.

Run after editing this script (or after a brand change):
    python scripts/generate_og_image.py

The output lives at static/img/og-default.png and is referenced from
hugo.toml's [params].ogImage. Also generates 192x192 + 512x512 PWA icons
and a 180x180 apple-touch-icon.
"""
from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sys

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'static' / 'img'
OUT.mkdir(parents=True, exist_ok=True)

CREAM   = (244, 237, 226)
PAPER   = (250, 247, 242)
INK     = (15, 15, 16)
GRAPHITE = (58, 58, 68)
RULE    = (212, 205, 189)
ACCENT  = (192, 57, 43)


def load_font(weights: list[str], size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        # Windows
        r'C:\Windows\Fonts\georgia.ttf',
        r'C:\Windows\Fonts\georgiab.ttf',
        r'C:\Windows\Fonts\seguibl.ttf',
        r'C:\Windows\Fonts\arialbd.ttf',
        r'C:\Windows\Fonts\arial.ttf',
        # Mac/Linux fallbacks
        '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',
        '/System/Library/Fonts/Georgia.ttf',
    ]
    chosen = None
    for c in candidates:
        if any(w.lower() in c.lower() for w in weights) and Path(c).exists():
            chosen = c
            break
    if not chosen:
        for c in candidates:
            if Path(c).exists():
                chosen = c
                break
    if not chosen:
        return ImageFont.load_default()
    return ImageFont.truetype(chosen, size)


def render_og() -> None:
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # Left vertical rule (editorial)
    d.line([(80, 80), (80, H - 80)], fill=RULE, width=2)

    # Wordmark + kicker
    title_font = load_font(['georgiab', 'bold'], 96)
    kicker_font = load_font(['arialbd', 'bold'], 22)
    body_font   = load_font(['georgia', 'serif'], 34)
    chip_font   = load_font(['arialbd', 'bold'], 18)

    d.text((120, 130), 'Pomegra Wiki', fill=INK, font=title_font)
    d.text((120, 240), 'THE READER-FRIENDLY ENCYCLOPEDIA', fill=ACCENT, font=kicker_font)
    d.text((120, 280), 'OF THE FINANCIAL WORLD', fill=ACCENT, font=kicker_font)

    d.text((120, 360), 'Plain-language entries on markets, instruments,', fill=GRAPHITE, font=body_font)
    d.text((120, 408), 'institutions, and the ideas that move them.', fill=GRAPHITE, font=body_font)

    # Chip row at bottom
    chips = [
        ('1,000+ ENTRIES', 120),
        ('27 CATEGORIES', 380),
        ('10K+ CROSS-LINKS', 640),
    ]
    y = 520
    for text, x in chips:
        d.text((x, y), text, fill=INK, font=chip_font)
    # vertical separators
    d.line([(348, y - 4), (348, y + 22)], fill=RULE, width=2)
    d.line([(608, y - 4), (608, y + 22)], fill=RULE, width=2)

    # Footer attribution
    foot_font = load_font(['arialbd', 'bold'], 16)
    txt = 'POMEGRA.IO/WIKI'
    bbox = d.textbbox((0, 0), txt, font=foot_font)
    tw = bbox[2] - bbox[0]
    d.text((W - 80 - tw, H - 70), txt, fill=GRAPHITE, font=foot_font)

    out = OUT / 'og-default.png'
    img.save(out, 'PNG', optimize=True)
    print(f'  Wrote {out.name} ({out.stat().st_size // 1024} KB)')


def render_icon(size: int, name: str) -> None:
    img = Image.new('RGB', (size, size), CREAM)
    d = ImageDraw.Draw(img)
    # rounded background hint (square is fine for icons)
    f = load_font(['georgiab', 'bold'], int(size * 0.72))
    bbox = d.textbbox((0, 0), 'P', font=f)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    d.text(((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1] - size * 0.04), 'P', fill=ACCENT, font=f)
    # small WIKI kicker beneath
    kf = load_font(['arialbd', 'bold'], max(8, int(size * 0.08)))
    kicker = 'WIKI'
    kbox = d.textbbox((0, 0), kicker, font=kf)
    kw = kbox[2] - kbox[0]
    d.text(((size - kw) / 2, size * 0.78), kicker, fill=INK, font=kf)
    out = OUT / name
    img.save(out, 'PNG', optimize=True)
    print(f'  Wrote {out.name} ({out.stat().st_size // 1024} KB)')


def main() -> int:
    render_og()
    render_icon(180, 'apple-touch-icon.png')
    render_icon(192, 'icon-192.png')
    render_icon(512, 'icon-512.png')
    print('Done.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
