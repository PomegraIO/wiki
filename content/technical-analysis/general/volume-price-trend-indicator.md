---
title: "Volume Price Trend Indicator Explained"
description: "The VPT indicator combines price change percentage with volume to measure trend strength and confirm directional momentum."
keywords:
  - volume price trend indicator explained
  - vpt indicator
  - volume price trend
  - price volume trend
  - technical analysis momentum
  - volume confirmation indicator
---

*The Volume Price Trend (VPT) indicator blends percentage price changes with trading volume, then cumulates the result into a running total. The logic is simple: big volume on large price moves signals genuine conviction, while small volume on big moves suggests weakness. Unlike on-balance volume, which treats every transaction equally regardless of magnitude, VPT scales volume by the percentage move, so a 5% rally on high volume carries more weight than a 0.5% rally on the same volume.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volume Price Trend — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">VPT accumulates volume weighted by percentage price change; confirms trend strength and divergences.</div>

|   |   |
|---|---|
| **Formula** | VPT = Prior VPT + (Volume × Price Change %)) |
| **Time frame** | Works on any—minutes, hours, days, weeks |
| **Use case** | Identify trend strength and spot divergences |
| **Signal** | Rising VPT on price rallies = strong trend; flat VPT on price gains = warning |
| **Difference from OBV** | VPT scales volume by price move magnitude; OBV counts all volume equally |
| **Strength** | Captures conviction (big move + big volume is real) |
| **Weakness** | Lagging indicator; doesn't predict turns, only confirms established moves |

</aside>

## The formula and mechanics

VPT is calculated period by period, building a cumulative total:

**VPT = Prior VPT + (Current Volume × Daily Price Change %)**

Where "Daily Price Change %" is the percentage move from close to close (or open to close).

**Example:**
- Day 1: Stock price closes at $100 on 1 million shares. VPT starts at zero.
- Day 2: Price closes at $105 (5% gain) on 2 million shares. VPT = 0 + (2,000,000 × 0.05) = 100,000.
- Day 3: Price falls to $103 (−1.9% loss) on 1.5 million shares. VPT = 100,000 + (1,500,000 × −0.019) = 100,000 − 28,500 = 71,500.
- Day 4: Price rises to $107 (3.9% gain) on 3 million shares. VPT = 71,500 + (3,000,000 × 0.039) = 71,500 + 117,000 = 188,500.

The VPT line rises when big volume arrives on up days and falls when big volume hits on down days. Sideways movement in VPT signals weak conviction behind price moves.

## VPT vs. On-Balance Volume

The most common alternative is on-balance volume (OBV), which simply adds volume on up days and subtracts it on down days, ignoring how big the move was.

**OBV with the same example:**
- Day 1: Price up or down? Neutral. OBV = 0.
- Day 2: Price up 5%. OBV = 0 + 2,000,000 = 2,000,000.
- Day 3: Price down 1.9%. OBV = 2,000,000 − 1,500,000 = 500,000.
- Day 4: Price up 3.9%. OBV = 500,000 + 3,000,000 = 3,500,000.

Notice: OBV treats the 5% rally the same as the 3.9% rally (both get full volume credit). VPT gives the 5% rally more weight because it was a bigger move.

**Practical difference:** If a stock rallies 0.1% on 50 million shares, OBV adds the full 50M. VPT adds only 50M × 0.001 = 50,000. The VPT philosophy is that a trivial price move on massive volume is suspicious—it suggests the market is uncertain or that large players are positioning without moving price. Conviction moves price significantly relative to volume.

## Interpreting VPT: trend confirmation

**Rising VPT + rising price** = Strong uptrend. Big rallies are accompanied by climbing volume, signaling real buyer conviction.

**Rising VPT but flat price** = Accumulation. Smart money is buying, but the crowd hasn't noticed yet. This can precede a breakout.

**Flat or falling VPT + rising price** = Weakness. The price is climbing on low or declining volume, suggesting the move is fragile. Sellers are absent, but so are committed buyers.

**Falling VPT + falling price** = Strong downtrend. Large-volume selling on big drops signals genuine selling pressure.

**Flat VPT + falling price** = Distribution. Sellers are stepping in, but without conviction; this can precede a bounce.

## Divergences: the main signal

The classic VPT signal is a **divergence** between price and the indicator.

**Bearish divergence:** Price makes a new high, but VPT doesn't. This suggests the rally is losing momentum. Fewer shares are moving into smart money's hands. Traders watch for a selloff to follow.

**Bullish divergence:** Price makes a new low, but VPT doesn't fall as sharply. Buying interest is stabilizing even as prices fall. This can signal a bottom and reversal.

Divergences are not infallible—they're statistical tendencies, not guarantees—but they're useful flags to prompt closer attention.

## Worked example: technology stock rally

Imagine a tech stock trading at $50:

**Week 1:** Stock closes at $55 (10% gain) on 50 million shares daily average. VPT climbs sharply (big move + big volume).

**Week 2:** Stock closes at $57 (3.6% gain) on 30 million shares daily average. VPT continues rising, but more slowly (smaller move, less volume).

**Week 3:** Stock shoots to $62 (8.8% gain) on only 15 million shares daily average. Price at new high, but VPT climbs slowly (big move, but volume dried up).

**Week 4:** Stock rallies to $63 (1.6% gain) on 60 million shares. VPT explodes higher (massive volume, but tiny move). This is a divergence: heavy volume hitting a stock that barely budged.

The pattern is typical of a local top. In Week 3, the rally to $62 looks impressive, but the light volume suggests it's exhausted. In Week 4, the huge volume on a 1% gain signals distribution—insiders or smart money unloading. Technicians would expect a pullback.

A trader would watch the next few days closely. If the stock breaks below $60, and VPT turns negative, it confirms the rally is over.

## Limitations and best practices

VPT is a **confirmation indicator**, not a predictor. It tells you if recent price moves have conviction, but it doesn't tell you when a move will end. Plenty of stocks continue rising despite VPT divergences, especially in strong bull markets. Conversely, prices can crash without a warning divergence.

The indicator is also **lagging**. VPT only reflects what has already happened. It doesn't see the future. For day traders and short-term chartists, this lag can mean missing quick reversals.

VPT is most useful when combined with other technical analysis tools—support and resistance levels, [moving averages](/moving-average/), momentum indicators—to build a convergent signal. A VPT divergence at a major price level (e.g., a prior support or resistance zone) is more meaningful than one in empty space.

Finally, volume data quality matters. Stocks with thin trading or low liquidity produce noisy VPT lines. Blue-chip or highly liquid assets generate cleaner signals.

## See also

<div class="wiki-seealso">

### Closely related

- Technical Analysis — overview of chart and indicator methods
- On-Balance Volume — alternative volume indicator
- [Moving Average](/moving-average/) — trend confirmation tool
- [Momentum Investing](/momentum-investing/) — strategy based on price/volume signals

### Wider context

- [Bid-Ask Spread](/bid-ask-spread/) — volume and liquidity relationship
- [Market Maker Trading](/market-maker-trading/) — institutional volume drivers
- [Price Discovery](/price-discovery/) — how volume reveals true value

</div>
