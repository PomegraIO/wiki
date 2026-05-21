#!/usr/bin/env python3
"""Generate one static SVG file per content category, in static/svg/.

Each SVG is editorial in style (cream paper, Pomegra accent red, geometric)
and represents the category visually: equity gets a bar chart, fixed-income
a yield curve, derivatives an option-payoff hockey stick, etc.

These files replace the Picsum random-photo URLs in every article's
infobox. Run after editing this file or after adding a new category.
"""
from __future__ import annotations
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT  = ROOT / 'static' / 'svg'
OUT.mkdir(parents=True, exist_ok=True)

CREAM   = '#f4ede2'
PAPER   = '#faf7f2'
INK     = '#0f0f10'
GRAPH   = '#5b5b63'
RULE    = '#d4cdbd'
ACCENT  = '#c0392b'

LABELS = {
    'equity':            ('Equity',            'SHARES — OWNERSHIP STAKES'),
    'fixed-income':      ('Fixed income',      'BONDS — IOUS WITH A COUPON'),
    'derivatives':       ('Derivatives',       'OPTIONS, FUTURES & SWAPS'),
    'funds':             ('Funds',             'POOLED INVESTMENT VEHICLES'),
    'forex':             ('Forex',             'CURRENCIES — THE FX MARKET'),
    'commodities':       ('Commodities',       'METALS, ENERGY, AGRICULTURE'),
    'macro':             ('Macro',             'THE WIDER ECONOMY'),
    'monetary':          ('Monetary',          'CENTRAL BANKS & MONEY'),
    'fiscal':            ('Fiscal',            'GOVERNMENT FINANCE'),
    'ratios':            ('Ratios',            'VALUATION & PROFITABILITY'),
    'accounting':        ('Accounting',        'THE THREE STATEMENTS'),
    'strategies':        ('Strategies',        'HOW INVESTORS DECIDE'),
    'risk':              ('Risk',              'WHAT CAN GO WRONG'),
    'behavioral':        ('Behavioural',       'PSYCHOLOGY & BIASES'),
    'history':           ('History',           'CRISES, BUBBLES, CYCLES'),
    'people':            ('People',            'INVESTORS & THINKERS'),
    'regulation':        ('Regulation',        'RULES & REGULATORS'),
    'corporate':         ('Corporate',         'M&A, GOVERNANCE'),
    'personal-finance':  ('Personal finance',  'HOUSEHOLD MONEY'),
    'taxes':             ('Taxes',             'WHAT INVESTORS OWE'),
    'real-estate':       ('Real estate',       'PROPERTY & MORTGAGES'),
    'trading':           ('Trading',           'ORDERS & EXECUTION'),
    'crypto':            ('Crypto',            'CRYPTOCURRENCIES & DEFI'),
    'technical-analysis':('Technical analysis','CHARTS & INDICATORS'),
    'institutions':      ('Institutions',      'EXCHANGES & FIRMS'),
    'valuation':         ('Valuation',         'WHAT IS IT WORTH'),
    'markets':           ('Markets',           'WHERE TRADES HAPPEN'),
    'default':           ('Pomegra Wiki',      'FINANCIAL ENCYCLOPEDIA'),
}


def _esc(s: str) -> str:
    # SVG served as image/svg+xml is parsed as strict XML; a literal & breaks
    # the whole document and browsers refuse to render. Escape entities in all
    # text content, not just labels (titles can contain & too).
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def header(title: str, label: str) -> str:
    t = _esc(title)
    l = _esc(label)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{t}">
<rect width="900" height="600" fill="{CREAM}"/>
<line x1="60" y1="60" x2="60" y2="540" stroke="{RULE}" stroke-width="1"/>
<text x="80" y="100" font-family="'Source Serif 4','Source Serif Pro',Georgia,serif" font-size="36" fill="{INK}" font-weight="600">{t}</text>
<text x="80" y="128" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="11" fill="{ACCENT}" letter-spacing="3" font-weight="700">{l}</text>'''

FOOTER = f'<text x="840" y="570" font-family="ui-monospace,monospace" font-size="10" fill="{GRAPH}" letter-spacing="2" text-anchor="end" opacity="0.7">POMEGRA WIKI</text></svg>'


# ── per-category iconography ────────────────────────────────────────────

def _equity() -> str:
    bars = [80, 120, 160, 140, 200, 240, 180, 260, 220]
    out = ['<g transform="translate(120,200)">', f'<line x1="0" y1="300" x2="700" y2="300" stroke="{RULE}" stroke-width="1"/>']
    for i, h in enumerate(bars):
        x = 20 + i * 70
        fill = ACCENT if i == 7 else INK
        op = 1 if i == 7 else 0.85
        out.append(f'<rect x="{x}" y="{300-h}" width="50" height="{h}" fill="{fill}" opacity="{op}"/>')
    pts = ' '.join(f'{20+i*70+25},{300-h-20}' for i, h in enumerate(bars))
    out.append(f'<polyline points="{pts}" fill="none" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    out.append('</g>')
    return '\n'.join(out)


def _fixed_income() -> str:
    return f'''<g transform="translate(120,200)">
<line x1="0" y1="0" x2="0" y2="300" stroke="{RULE}" stroke-width="1"/>
<line x1="0" y1="300" x2="700" y2="300" stroke="{RULE}" stroke-width="1"/>
<path d="M 0 260 Q 200 230, 350 160 T 700 60" fill="none" stroke="{ACCENT}" stroke-width="4" stroke-linecap="round"/>
<circle cx="0" cy="260" r="5" fill="{ACCENT}"/>
<circle cx="200" cy="200" r="5" fill="{ACCENT}"/>
<circle cx="350" cy="160" r="5" fill="{ACCENT}"/>
<circle cx="500" cy="110" r="5" fill="{ACCENT}"/>
<circle cx="700" cy="60" r="5" fill="{ACCENT}"/>
<text x="0" y="330" font-family="ui-monospace,monospace" font-size="11" fill="{GRAPH}" text-anchor="middle">3M</text>
<text x="200" y="330" font-family="ui-monospace,monospace" font-size="11" fill="{GRAPH}" text-anchor="middle">2Y</text>
<text x="350" y="330" font-family="ui-monospace,monospace" font-size="11" fill="{GRAPH}" text-anchor="middle">5Y</text>
<text x="500" y="330" font-family="ui-monospace,monospace" font-size="11" fill="{GRAPH}" text-anchor="middle">10Y</text>
<text x="700" y="330" font-family="ui-monospace,monospace" font-size="11" fill="{GRAPH}" text-anchor="middle">30Y</text>
</g>'''


def _derivatives() -> str:
    return f'''<g transform="translate(120,200)">
<line x1="0" y1="300" x2="700" y2="300" stroke="{RULE}" stroke-width="1"/>
<line x1="350" y1="0" x2="350" y2="320" stroke="{RULE}" stroke-width="1" stroke-dasharray="4 4"/>
<polyline points="0,180 350,180 700,40" fill="none" stroke="{ACCENT}" stroke-width="4"/>
<polyline points="0,40 350,180 700,180" fill="none" stroke="{INK}" stroke-width="2" opacity="0.6"/>
<circle cx="350" cy="180" r="6" fill="{ACCENT}"/>
<text x="350" y="350" font-family="ui-monospace,monospace" font-size="11" fill="{GRAPH}" text-anchor="middle">STRIKE</text>
<text x="700" y="35" font-family="ui-monospace,monospace" font-size="11" fill="{ACCENT}" text-anchor="end" font-weight="700">CALL</text>
<text x="0" y="35" font-family="ui-monospace,monospace" font-size="11" fill="{INK}" opacity="0.6" font-weight="700">PUT</text>
</g>'''


def _funds() -> str:
    cols = [(0, 0, 300, 120, 80), (160, 60, 240, 90, 60), (320, 30, 270, 100, 70), (480, 100, 200, 70, 50)]
    out = ['<g transform="translate(140,200)">']
    for x, y, h, red, gr in cols:
        out.append(f'<rect x="{x}" y="{y}" width="120" height="{h}" fill="{INK}" opacity="0.85"/>')
        out.append(f'<rect x="{x}" y="{y}" width="120" height="{red}" fill="{ACCENT}"/>')
        out.append(f'<rect x="{x}" y="{y+red}" width="120" height="{gr}" fill="{GRAPH}"/>')
    out.append(f'<line x1="-10" y1="300" x2="610" y2="300" stroke="{RULE}" stroke-width="1"/>')
    out.append('</g>')
    return '\n'.join(out)


def _forex() -> str:
    heights = [80, 120, 100, 150, 90, 140, 110, 170, 130, 100, 80, 140, 95, 130, 90]
    out = ['<g transform="translate(120,220)">', f'<line x1="0" y1="160" x2="700" y2="160" stroke="{RULE}" stroke-width="1"/>']
    for i, h in enumerate(heights):
        x = i * 45
        col = ACCENT if i % 3 == 0 else INK
        out.append(f'<line x1="{x+10}" y1="{160-h}" x2="{x+10}" y2="{160+h//2}" stroke="{GRAPH}" stroke-width="1"/>')
        out.append(f'<rect x="{x}" y="{160-h//2}" width="20" height="{h//2}" fill="{col}"/>')
    out.append('</g>')
    return '\n'.join(out)


def _commodities() -> str:
    items = [(0, 120, 180, INK, 0.85), (120, 60, 240, ACCENT, 1), (240, 160, 140, GRAPH, 1), (360, 100, 200, INK, 0.85), (480, 30, 270, ACCENT, 0.85)]
    labels = ['CRUDE', 'GOLD', 'COPPER', 'WHEAT', 'NAT GAS']
    out = ['<g transform="translate(180,220)">']
    for (x, y, h, c, op), lab in zip(items, labels):
        out.append(f'<rect x="{x}" y="{y}" width="100" height="{h}" fill="{c}" opacity="{op}"/>')
        out.append(f'<text x="{x+50}" y="325" font-family="ui-monospace,monospace" font-size="10" fill="{GRAPH}" text-anchor="middle">{lab}</text>')
    out.append(f'<line x1="-10" y1="300" x2="590" y2="300" stroke="{RULE}" stroke-width="1"/>')
    out.append('</g>')
    return '\n'.join(out)


def _macro() -> str:
    return f'''<g transform="translate(80,230)">
<line x1="0" y1="150" x2="760" y2="150" stroke="{RULE}" stroke-width="1"/>
<path d="M 0 150 Q 95 30, 190 150 T 380 150 T 570 150 T 760 150" fill="none" stroke="{ACCENT}" stroke-width="4" stroke-linecap="round"/>
<circle cx="95" cy="30" r="6" fill="{ACCENT}"/>
<circle cx="285" cy="270" r="6" fill="{INK}"/>
<circle cx="475" cy="30" r="6" fill="{ACCENT}"/>
<circle cx="665" cy="270" r="6" fill="{INK}"/>
<text x="95" y="20" font-family="ui-monospace,monospace" font-size="10" fill="{GRAPH}" text-anchor="middle">PEAK</text>
<text x="285" y="295" font-family="ui-monospace,monospace" font-size="10" fill="{GRAPH}" text-anchor="middle">TROUGH</text>
</g>'''


def _monetary() -> str:
    return f'''<g transform="translate(450,330)">
<circle r="180" fill="none" stroke="{RULE}" stroke-width="1.5"/>
<circle r="140" fill="none" stroke="{GRAPH}" stroke-width="1.5"/>
<circle r="95" fill="none" stroke="{INK}" stroke-width="2"/>
<circle r="50" fill="{ACCENT}"/>
<text x="0" y="6" font-family="ui-monospace,monospace" font-size="16" fill="{CREAM}" text-anchor="middle" font-weight="700">M0</text>
<text x="0" y="-72" font-family="ui-monospace,monospace" font-size="12" fill="{INK}" text-anchor="middle" font-weight="600">M1</text>
<text x="0" y="-118" font-family="ui-monospace,monospace" font-size="12" fill="{GRAPH}" text-anchor="middle">M2</text>
<text x="0" y="-160" font-family="ui-monospace,monospace" font-size="12" fill="{GRAPH}" text-anchor="middle">M3</text>
</g>'''


def _fiscal() -> str:
    heights = [140, 160, 130, 180, 210, 170, 220, 200, 240, 230, 250]
    out = ['<g transform="translate(140,210)">']
    for i, h in enumerate(heights):
        x = i * 55
        out.append(f'<rect x="{x}" y="{280-h}" width="40" height="{h}" fill="{INK}" opacity="0.85"/>')
        out.append(f'<rect x="{x}" y="280" width="40" height="{i*5}" fill="{ACCENT}"/>')
    out.append(f'<line x1="-10" y1="280" x2="640" y2="280" stroke="{INK}" stroke-width="2"/>')
    out.append(f'<text x="-10" y="298" font-family="ui-monospace,monospace" font-size="10" fill="{ACCENT}" font-weight="700">DEFICIT</text>')
    out.append('</g>')
    return '\n'.join(out)


def _ratios() -> str:
    return f'''<g transform="translate(150,220)">
<rect x="0" y="0" width="600" height="60" fill="{ACCENT}"/>
<rect x="0" y="120" width="380" height="60" fill="{INK}"/>
<line x1="0" y1="100" x2="600" y2="100" stroke="{GRAPH}" stroke-width="2"/>
<text x="610" y="40" font-family="ui-monospace,monospace" font-size="13" fill="{ACCENT}" font-weight="700">PRICE</text>
<text x="610" y="160" font-family="ui-monospace,monospace" font-size="13" fill="{INK}" font-weight="700">EARNINGS</text>
<text x="0" y="240" font-family="'Fraunces',Georgia,serif" font-size="44" fill="{INK}" font-style="italic" font-weight="600">= 18.4×</text>
</g>'''


def _accounting() -> str:
    out = ['<g transform="translate(150,200)">']
    cols = [(0, INK), (220, INK), (440, ACCENT)]
    titles = ['P&amp;L', 'BALANCE', 'CASH FLOW']
    for (x, color), title in zip(cols, titles):
        out.append(f'<rect x="{x}" y="0" width="180" height="320" fill="none" stroke="{color}" stroke-width="2"/>')
        out.append(f'<text x="{x+90}" y="25" font-family="ui-monospace,monospace" font-size="11" fill="{color}" text-anchor="middle" font-weight="700">{title}</text>')
        for j in range(7):
            y = 50 + j * 35
            out.append(f'<line x1="{x+20}" y1="{y}" x2="{x+160}" y2="{y}" stroke="{GRAPH}" stroke-width="1" opacity="0.5"/>')
    out.append('</g>')
    return '\n'.join(out)


def _strategies() -> str:
    return f'''<g transform="translate(130,210)" stroke="{GRAPH}" stroke-width="2" fill="none">
<line x1="0" y1="160" x2="200" y2="160"/>
<line x1="200" y1="160" x2="350" y2="60"/>
<line x1="200" y1="160" x2="350" y2="260"/>
<line x1="350" y1="60" x2="520" y2="20"/>
<line x1="350" y1="60" x2="520" y2="100"/>
<line x1="350" y1="260" x2="520" y2="220"/>
<line x1="350" y1="260" x2="520" y2="300"/>
<circle cx="0" cy="160" r="11" fill="{ACCENT}" stroke="none"/>
<circle cx="200" cy="160" r="8" fill="{INK}" stroke="none"/>
<circle cx="350" cy="60" r="8" fill="{INK}" stroke="none"/>
<circle cx="350" cy="260" r="8" fill="{INK}" stroke="none"/>
<circle cx="520" cy="20" r="6" fill="{GRAPH}" stroke="none"/>
<circle cx="520" cy="100" r="6" fill="{GRAPH}" stroke="none"/>
<circle cx="520" cy="220" r="6" fill="{GRAPH}" stroke="none"/>
<circle cx="520" cy="300" r="6" fill="{ACCENT}" stroke="none"/>
</g>'''


def _risk() -> str:
    return f'''<g transform="translate(80,220)">
<line x1="0" y1="220" x2="760" y2="220" stroke="{RULE}" stroke-width="1"/>
<path d="M 0 220 C 200 220, 280 30, 380 30 C 480 30, 560 220, 760 220 Z" fill="{INK}" opacity="0.10"/>
<path d="M 0 220 C 200 220, 280 30, 380 30 C 480 30, 560 220, 760 220" fill="none" stroke="{INK}" stroke-width="2"/>
<path d="M 600 220 C 640 220, 670 100, 700 100 C 720 100, 740 220, 760 220 Z" fill="{ACCENT}" opacity="0.75"/>
<line x1="380" y1="30" x2="380" y2="220" stroke="{GRAPH}" stroke-width="1" stroke-dasharray="3 3"/>
<text x="680" y="265" font-family="ui-monospace,monospace" font-size="11" fill="{ACCENT}" font-weight="700" text-anchor="middle">TAIL</text>
</g>'''


def _behavioral() -> str:
    return f'''<g transform="translate(140,210)">
<circle cx="50" cy="160" r="14" fill="{ACCENT}"/>
<line x1="65" y1="155" x2="500" y2="50" stroke="{INK}" stroke-width="2.5"/>
<line x1="65" y1="165" x2="500" y2="270" stroke="{INK}" stroke-width="2.5"/>
<polygon points="500,50 480,42 480,58" fill="{INK}"/>
<polygon points="500,270 480,262 480,278" fill="{INK}"/>
<text x="520" y="55" font-family="'Fraunces',Georgia,serif" font-style="italic" font-size="22" fill="{INK}">rational</text>
<text x="520" y="275" font-family="'Fraunces',Georgia,serif" font-style="italic" font-size="22" fill="{ACCENT}">biased</text>
</g>'''


def _history() -> str:
    years = ['1929', '1973', '1987', '2000', '2008', '2020']
    out = ['<g transform="translate(80,300)">', f'<line x1="0" y1="0" x2="760" y2="0" stroke="{INK}" stroke-width="2"/>']
    for i, y in enumerate(years):
        x = 40 + i * 140
        col = ACCENT if i % 2 == 0 else INK
        out.append(f'<line x1="{x}" y1="-12" x2="{x}" y2="12" stroke="{INK}" stroke-width="2"/>')
        out.append(f'<circle cx="{x}" cy="0" r="7" fill="{col}"/>')
        out.append(f'<text x="{x}" y="-28" font-family="ui-monospace,monospace" font-size="12" fill="{GRAPH}" text-anchor="middle">{y}</text>')
    out.append('</g>')
    return '\n'.join(out)


def _people() -> str:
    return f'''<g transform="translate(360,200)">
<circle cx="100" cy="80" r="58" fill="{INK}"/>
<path d="M 30 250 C 30 170, 170 170, 170 250 Z" fill="{INK}"/>
<line x1="100" y1="240" x2="100" y2="320" stroke="{ACCENT}" stroke-width="3"/>
<circle cx="100" cy="80" r="58" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="5 4"/>
</g>'''


def _regulation() -> str:
    out = ['<g transform="translate(180,200)">']
    out.append(f'<rect x="0" y="0" width="540" height="50" fill="{INK}"/>')
    for k in range(1, 4):
        out.append(f'<rect x="0" y="{k*60}" width="540" height="50" fill="none" stroke="{GRAPH}" stroke-width="1"/>')
        out.append(f'<line x1="20" y1="{k*60+20}" x2="500" y2="{k*60+20}" stroke="{RULE}" stroke-width="1"/>')
        out.append(f'<line x1="20" y1="{k*60+35}" x2="380" y2="{k*60+35}" stroke="{RULE}" stroke-width="1"/>')
    out.append(f'<rect x="0" y="240" width="540" height="50" fill="{ACCENT}"/>')
    out.append(f'<text x="20" y="33" font-family="ui-monospace,monospace" font-size="14" fill="{CREAM}" font-weight="700">§ STATUTE</text>')
    out.append(f'<text x="20" y="273" font-family="ui-monospace,monospace" font-size="14" fill="{CREAM}" font-weight="700">§ AMENDMENT</text>')
    out.append('</g>')
    return '\n'.join(out)


def _corporate() -> str:
    return f'''<g transform="translate(120,200)">
<rect x="0" y="40" width="180" height="240" fill="{INK}" opacity="0.85"/>
<rect x="520" y="40" width="180" height="240" fill="{INK}" opacity="0.85"/>
<path d="M 180 100 L 350 160 L 180 220 Z" fill="{GRAPH}"/>
<path d="M 700 100 L 530 160 L 700 220 Z" fill="{GRAPH}"/>
<circle cx="350" cy="160" r="42" fill="{ACCENT}"/>
<circle cx="350" cy="160" r="42" fill="none" stroke="{INK}" stroke-width="2"/>
<text x="350" y="167" font-family="ui-monospace,monospace" font-size="16" fill="{CREAM}" text-anchor="middle" font-weight="700">M&amp;A</text>
</g>'''


def _personal_finance() -> str:
    heights = [60, 100, 145, 180, 220, 260]
    out = ['<g transform="translate(160,210)">', f'<line x1="0" y1="280" x2="600" y2="280" stroke="{RULE}" stroke-width="1"/>']
    for i, h in enumerate(heights):
        x = i * 95
        col = ACCENT if i == 5 else INK
        op = 1 if i == 5 else 0.85
        out.append(f'<rect x="{x}" y="{280-h}" width="60" height="{h}" fill="{col}" opacity="{op}"/>')
    pts = ' '.join(f'{i*95+30},{280-h-15}' for i, h in enumerate(heights))
    out.append(f'<polyline points="{pts}" fill="none" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>')
    out.append(f'<text x="0" y="305" font-family="ui-monospace,monospace" font-size="10" fill="{GRAPH}">YR 1</text>')
    out.append(f'<text x="475" y="305" font-family="ui-monospace,monospace" font-size="10" fill="{ACCENT}" font-weight="700">YR 30</text>')
    out.append('</g>')
    return '\n'.join(out)


def _taxes() -> str:
    rates = [10, 12, 22, 24, 32, 35, 37]
    out = ['<g transform="translate(140,220)">', f'<line x1="0" y1="260" x2="640" y2="260" stroke="{RULE}" stroke-width="1"/>']
    for i, r in enumerate(rates):
        x = i * 90
        h = r * 6
        col = ACCENT if i >= 4 else INK
        op = 1 if i >= 4 else 0.85
        out.append(f'<rect x="{x}" y="{260-h}" width="70" height="{h}" fill="{col}" opacity="{op}"/>')
        out.append(f'<text x="{x+35}" y="{255-h}" font-family="ui-monospace,monospace" font-size="11" fill="{GRAPH}" text-anchor="middle">{r}%</text>')
    out.append('</g>')
    return '\n'.join(out)


def _real_estate() -> str:
    heights = [180, 240, 200, 290, 220, 260, 180, 320, 230, 200, 280, 210, 250, 200]
    out = ['<g transform="translate(80,200)">']
    for i, h in enumerate(heights):
        x = i * 55
        col = ACCENT if i % 4 == 0 else INK
        op = 1 if i % 4 == 0 else 0.85
        out.append(f'<rect x="{x}" y="{360-h}" width="50" height="{h}" fill="{col}" opacity="{op}"/>')
        rows = max(1, h // 35 - 1)
        for j in range(rows):
            yw = 360 - h + j * 30 + 8
            out.append(f'<rect x="{x+10}" y="{yw}" width="6" height="6" fill="{CREAM}" opacity="0.42"/>')
            out.append(f'<rect x="{x+25}" y="{yw}" width="6" height="6" fill="{CREAM}" opacity="0.42"/>')
    out.append(f'<line x1="-10" y1="360" x2="780" y2="360" stroke="{INK}" stroke-width="2"/>')
    out.append('</g>')
    return '\n'.join(out)


def _trading() -> str:
    out = ['<g transform="translate(140,200)">', f'<line x1="300" y1="-10" x2="300" y2="330" stroke="{GRAPH}" stroke-width="1"/>']
    for i in range(8):
        w = (8 - i) * 30
        out.append(f'<rect x="{300-w}" y="{10+i*38}" width="{w}" height="28" fill="{INK}" opacity="0.65"/>')
        out.append(f'<rect x="300" y="{10+i*38}" width="{w}" height="28" fill="{ACCENT}" opacity="0.65"/>')
    out.append(f'<text x="0" y="-15" font-family="ui-monospace,monospace" font-size="11" fill="{INK}" font-weight="700">BIDS</text>')
    out.append(f'<text x="595" y="-15" font-family="ui-monospace,monospace" font-size="11" fill="{ACCENT}" font-weight="700" text-anchor="end">ASKS</text>')
    out.append('</g>')
    return '\n'.join(out)


def _crypto() -> str:
    out = ['<g transform="translate(80,260)">']
    for i in range(5):
        x = i * 155
        col = ACCENT if i == 4 else INK
        op = 1 if i == 4 else 0.85
        out.append(f'<rect x="{x}" y="0" width="120" height="100" fill="{col}" opacity="{op}" rx="4"/>')
        out.append(f'<text x="{x+60}" y="40" font-family="ui-monospace,monospace" font-size="10" fill="{CREAM}" text-anchor="middle">BLOCK</text>')
        out.append(f'<text x="{x+60}" y="62" font-family="ui-monospace,monospace" font-size="14" fill="{CREAM}" text-anchor="middle" font-weight="700">#{781200+i}</text>')
        out.append(f'<text x="{x+60}" y="80" font-family="ui-monospace,monospace" font-size="8" fill="{CREAM}" text-anchor="middle" opacity="0.7">0x4a7e…</text>')
        if i < 4:
            out.append(f'<line x1="{x+120}" y1="50" x2="{x+155}" y2="50" stroke="{GRAPH}" stroke-width="2"/>')
    out.append('</g>')
    return '\n'.join(out)


def _technical_analysis() -> str:
    tops = [100, 130, 80, 110, 140, 60, 90, 130, 80, 50, 90, 70, 110, 80, 50, 110, 40, 60]
    bodies = [1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1]
    out = ['<g transform="translate(100,200)">', f'<line x1="0" y1="280" x2="720" y2="280" stroke="{RULE}" stroke-width="1"/>']
    for i, (top, body) in enumerate(zip(tops, bodies)):
        x = i * 38
        h = 60 + (i % 5) * 12
        col = ACCENT if body == 1 else INK
        out.append(f'<line x1="{x+10}" y1="{top}" x2="{x+10}" y2="{top+h+30}" stroke="{GRAPH}" stroke-width="1"/>')
        out.append(f'<rect x="{x}" y="{top+10}" width="20" height="{h}" fill="{col}"/>')
    out.append('</g>')
    return '\n'.join(out)


def _institutions() -> str:
    out = ['<g transform="translate(150,200)">']
    out.append(f'<polygon points="0,80 600,80 540,30 60,30" fill="{INK}"/>')
    for i in range(6):
        x = 50 + i * 100
        col = ACCENT if i == 2 else INK
        op = 1 if i == 2 else 0.85
        out.append(f'<rect x="{x}" y="80" width="40" height="200" fill="{col}" opacity="{op}"/>')
    out.append(f'<rect x="0" y="280" width="600" height="40" fill="{INK}"/>')
    out.append(f'<text x="300" y="60" font-family="\'Fraunces\',Georgia,serif" font-size="17" fill="{CREAM}" text-anchor="middle" font-style="italic">EXCHANGE</text>')
    out.append('</g>')
    return '\n'.join(out)


def _valuation() -> str:
    out = ['<g transform="translate(100,210)">', f'<line x1="0" y1="200" x2="720" y2="200" stroke="{INK}" stroke-width="2"/>']
    for i in range(7):
        x = 40 + i * 110
        h = 50 + i * 18
        col = ACCENT if i == 6 else INK
        out.append(f'<line x1="{x}" y1="200" x2="{x}" y2="{200-h}" stroke="{col}" stroke-width="3"/>')
        out.append(f'<polygon points="{x-6},{200-h} {x},{200-h-14} {x+6},{200-h}" fill="{col}"/>')
        out.append(f'<text x="{x}" y="225" font-family="ui-monospace,monospace" font-size="10" fill="{GRAPH}" text-anchor="middle">Y{i}</text>')
    out.append(f'<text x="720" y="195" font-family="\'Fraunces\',Georgia,serif" font-size="20" fill="{ACCENT}" font-style="italic" font-weight="600">TV</text>')
    out.append('</g>')
    return '\n'.join(out)


def _markets() -> str:
    return f'''<g transform="translate(80,210)">
<line x1="0" y1="260" x2="760" y2="260" stroke="{RULE}" stroke-width="1"/>
<polygon points="0,260 50,200 110,150 180,110 250,80 320,50 380,50" fill="{INK}" opacity="0.20"/>
<polyline points="0,260 50,200 110,150 180,110 250,80 320,50 380,50" fill="none" stroke="{INK}" stroke-width="3"/>
<polygon points="380,50 440,80 510,110 580,150 650,200 700,250 760,260" fill="{ACCENT}" opacity="0.25"/>
<polyline points="380,50 440,80 510,110 580,150 650,200 700,250 760,260" fill="none" stroke="{ACCENT}" stroke-width="3"/>
<line x1="380" y1="30" x2="380" y2="280" stroke="{GRAPH}" stroke-width="1" stroke-dasharray="4 4"/>
<text x="380" y="20" font-family="ui-monospace,monospace" font-size="11" fill="{GRAPH}" text-anchor="middle">MID</text>
</g>'''


def _default() -> str:
    return f'''<g transform="translate(150,180)">
<line x1="0" y1="180" x2="600" y2="0" stroke="{INK}" stroke-width="3"/>
<line x1="0" y1="260" x2="600" y2="80" stroke="{GRAPH}" stroke-width="2"/>
<line x1="0" y1="340" x2="600" y2="160" stroke="{ACCENT}" stroke-width="4"/>
</g>'''


RENDERERS = {
    'equity':            _equity,
    'fixed-income':      _fixed_income,
    'derivatives':       _derivatives,
    'funds':             _funds,
    'forex':             _forex,
    'commodities':       _commodities,
    'macro':             _macro,
    'monetary':          _monetary,
    'fiscal':            _fiscal,
    'ratios':            _ratios,
    'accounting':        _accounting,
    'strategies':        _strategies,
    'risk':              _risk,
    'behavioral':        _behavioral,
    'history':           _history,
    'people':            _people,
    'regulation':        _regulation,
    'corporate':         _corporate,
    'personal-finance':  _personal_finance,
    'taxes':             _taxes,
    'real-estate':       _real_estate,
    'trading':           _trading,
    'crypto':            _crypto,
    'technical-analysis':_technical_analysis,
    'institutions':      _institutions,
    'valuation':         _valuation,
    'markets':           _markets,
    'default':           _default,
}


def main() -> None:
    for cat, fn in RENDERERS.items():
        title, label = LABELS[cat]
        svg = '\n'.join([header(title, label), fn(), FOOTER])
        path = OUT / f'{cat}.svg'
        path.write_text(svg, encoding='utf-8')
        print(f'  {path.name}')
    print(f'Done. {len(RENDERERS)} SVG files written to {OUT}')


if __name__ == '__main__':
    main()
