---
title: "Volume Price Trend"
description: "A cumulative indicator that weights trading volume by the percentage change in closing price to measure the intensity of price-driven accumulation and distribution."
keywords:
  - volume price trend
  - volume weighted momentum
  - vpt indicator
  - price weighted volume
  - accumulation distribution
image: "/svg/technical-analysis.svg"
---

*The **Volume Price Trend** (VPT) is a cumulative technical indicator that multiplies [volume](/volume-price-trend/) by the percentage change in closing price, creating a running total that rises steeply when small price moves occur on heavy volume, and rises gently when large price moves occur on light volume. This weighting reveals whether price momentum is backed by real participation or merely marking time. Traders use VPT divergences to spot weakening trends and potential reversals before price charts signal them.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volume Price Trend — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A volume-weighted cumulative measure of price momentum.</div>

|   |   |
|---|---|
| **What it is** | Cumulative indicator weighting volume by percentage price change |
| **Also called** | VPT, Price-Volume Trend |
| **Calculation** | VPT = Prior VPT + (Volume × Percentage Change in Close) |
| **Interpretation** | Rising VPT = broad participation supporting move; falling VPT = volume drying up despite price moves |
| **Key signal** | Divergences between price and VPT warn of trend exhaustion |
| **Time horizon** | Short-term to swing trading |

</aside>

## The logic of weighting by percentage change

Standard [volume](/volume-price-trend/) tells you only how many shares or contracts traded; it cannot distinguish between a stock rising 0.5% on a million shares versus rising 5% on a million shares. Both show the same volume bar, yet the first scenario—big volume, tiny price move—suggests the buying is shallow and the market is crowded. The second—big volume, big price move—suggests conviction.

Volume Price Trend fixes this by multiplying each bar's volume by that bar's *percentage change* in closing price. A 5% jump on one million shares generates a VPT contribution of 50,000; a 0.5% jump on one million shares generates only 5,000. The ratio reveals whether volume is concentrated in large moves (suggesting genuine momentum) or spread thinly across small moves (suggesting skepticism or consolidation).

## Building the cumulative line

VPT is cumulative—each day's contribution is added to the running total, creating a line that can only move upward (if price closes higher on volume), downward (if price closes lower on volume), or sideways (if volume dries up or price barely moves). A steeply rising VPT line means price gains are backed by heavy participation. A flat VPT line alongside a rising price means the rally is losing participation—fewer traders are convinced, a red flag for reversal.

The formula is simple:

VPT = Prior VPT + (Volume × (Close – Prior Close) / Prior Close)

This percentage-based approach is also why VPT works across different price levels. A stock trading at $50 and moving to $52.50 (5% gain) on volume V contributes the same to VPT as a stock trading at $100 and moving to $105 (5% gain) on the same volume V. The indicator is not biased toward higher-priced assets.

## Spotting distribution under rising prices

The real power of VPT emerges in divergences. Imagine a stock climbing from $40 to $50 over a month. The price chart shows a pristine uptrend. But the VPT line has flat spots—several days when price rose modestly on declining volume. Traders are stepping away even as price creeps higher. This divergence—rising price, weakening VPT—often precedes a sharp correction. Volume participation is eroding; the trend has no legs.

The reverse divergence is equally useful: price falling while VPT rises. Sellers are getting aggressive, but volume is light. Buyers are stepping in selectively. This pattern often marks a washout or capitulation low, the moment when panic selling has exhausted itself and astute traders are accumulating.

## Comparing VPT to price trends

In a healthy bull market, VPT and price rise together, showing that gains are broad-based and participated in. If price rises but VPT stagnates, the move is unsustainable—volume enthusiasm has faded while prices are being pushed by inertia or short-covering. This is the classic warning setup, and VPT makes it visible.

In downtrends, falling VPT alongside falling price confirms the move is genuine. But if price falls steeply while VPT rises (because the small percentage drops are occurring on heavy volume), it often signals a bottom forming—sellers have capitulated and volume is flooding into willing buyers.

## Sensitivity to recent price levels

VPT uses percentage change, not absolute point change, which means it is sensitive to the absolute price level of the security. A stock at $10 moving to $10.50 is a 5% move; a stock at $100 moving to $101 is a 1% move. Both on identical volume will produce different VPT contributions. This is appropriate—the $10 stock experienced larger price movement and presumably greater trader conviction—but it does mean comparing VPT across very different price regimes (e.g., a stock before and after a split) requires care.

## Practical trading applications

Short-term traders use VPT to time entries and exits within established trends. A divergence warning—price making a new high while VPT does not—is a sell signal. A divergence confirmation—price and VPT both making new highs—strengthens a buy setup. Swing traders often layer VPT with moving averages, selling when a rising price is accompanied by a falling or stalled VPT moving average.

Options traders use VPT to gauge whether a move has real conviction before committing to directional positions. A large implied move unaccompanied by rising VPT may be theoretical rather than real, increasing the chance the actual move will be smaller.

## Integration with other indicators

VPT is most useful when combined with price structure and other volume measures. Pair it with [Force Index](/force-index/) to see whether single-bar momentum (Force) aligns with cumulative, percentage-weighted momentum (VPT). Use [Klinger Oscillator](/klinger-oscillator/) to spot longer-term accumulation and distribution patterns. In markets lacking true volume data, [Tick Volume](/tick-volume/) can substitute for volume in the VPT formula, though with reduced reliability.

Many technical analysts also cross-reference VPT divergences with key price levels—support zones where buyers have historically stepped in, resistance zones where sellers have historically appeared—to increase the probability that a divergence warning will result in an actual reversal.

## Limitations and false signals

VPT can generate whipsaws in choppy, sideways markets. If price oscillates around a support level on modest volume, VPT will move sideways as well, creating no clear signal. It also relies entirely on closing price, ignoring intraday structure. A stock that gaps down on opening news may close only slightly lower, generating a small VPT contribution, even though intraday volume was dislocated and the market structure severely disrupted.

VPT can also lag when volume spikes unexpectedly. If a stock rallies 2% on triple-average volume, VPT will spike up sharply, but if the next day the stock gives back the gains on declining volume, VPT will stall while price falls further—a false buy signal. Always confirm VPT signals with price action, support and resistance, and overall trend context.

## Adjusting sensitivity

Some traders apply a moving average to the VPT line to smooth out daily noise and highlight the underlying direction. A 20-period simple moving average of VPT can reduce whipsaws while preserving genuine divergences. Others use VPT in oscillator form—subtracting a moving average of VPT from the raw VPT line—to see when VPT momentum is accelerating or decelerating, similar to how MACD works with moving average convergence.

## See also

<div class="wiki-seealso">

### Closely related

- [Force Index](/force-index/) — indicator combining price change and volume to measure momentum strength
- [Klinger Oscillator](/klinger-oscillator/) — long-term volume flow measure separating accumulation from distribution
- [Tick Volume](/tick-volume/) — trade count proxy for volume-unavailable markets
- [Momentum](/beta/) — rate of price acceleration in a direction

### Wider context

- [Stock Market](/stock-market/) — exchange where securities are traded by buyers and sellers
- [Price Discovery](/price-discovery/) — process by which supply and demand establish fair prices
- [Bull Market](/bull-market/) — extended period of rising prices and investor optimism
- [Bear Market](/bear-market/) — extended period of falling prices and risk aversion
- [Technical Analysis](/volume-price-trend/) — study of price and volume patterns to forecast future moves

</div>
