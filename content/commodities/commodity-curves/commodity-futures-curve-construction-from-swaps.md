---
title: "Building a Commodity Forward Curve from OTC Swap Quotes"
description: "Step-by-step guide to constructing a continuous commodity forward curve from sparse exchange futures and dense OTC swap data."
keywords:
  - commodity forward curve construction swaps
  - forward curve interpolation
  - OTC commodity swaps
  - futures curve gaps filling
image: /svg/commodities.svg
---

*Constructing a **commodity forward curve from swaps** requires blending sparse exchange [futures](/futures-contract/) with liquid OTC [swap](/swap/) quotes to create a continuous, smooth curve across all relevant tenors. Exchange futures may exist only at quarterly or monthly intervals, while OTC swaps often trade daily. Traders use interpolation and curve-fitting techniques to fill the gaps, then use the complete curve for valuation, risk management, and hedging decisions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Curve Construction Toolkit — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">A practical curve pulls data from multiple sources to cover all maturities traders need.</div>

|   |   |
|---|---|
| **Exchange futures** | Quarterly or monthly contracts; liquid near-term; wide bid-ask far out. |
| **OTC swaps** | Daily settlement; often 1Y, 2Y, 5Y, 10Y standard tenors; bespoke possible. |
| **[Spot rate](/spot-rate/)** | Today's physical price; anchor point for the curve. |
| **Interpolation** | Linear or spline methods to fill single-month gaps. |
| **Extrapolation** | Methods for years beyond swap liquidity. |
| **Calibration** | Ensuring fit is smooth and economically sensible. |

</aside>

## Why splicing is necessary

A commodity trader or risk manager needs prices for every maturity: 1 month, 2 months, 3 months, 6 months, 1 year, 18 months, 2 years, 5 years. But the market does not always provide prices at all tenors.

Exchange-traded [futures contracts](/futures-contract/) in crude oil, natural gas, and metals trade quarterly or monthly, so you get:

- Jan 2026, Feb 2026, Mar 2026, Apr 2026 … Dec 2026 (monthly).
- Q1 2027, Q2 2027, Q3 2027 … (quarterly).

OTC [swaps](/swap/) in the same commodities trade on standard tenors:

- 1 Year, 2 Year, 3 Year, 5 Year, 10 Year.

A trader holding a position or running a valuation model needs intermediate tenors: What is the 18-month forward price? What is the 3.5-year price? The market doesn't quote those; you must construct them.

This is where interpolation and curve fitting come in.

## Step 1: Collect quotes and identify anchor points

Start by gathering all available quotes for the commodity across the curve:

1. **Spot price** (current physical delivery today).
2. **Liquid exchange futures** (the front few months, where bid-ask spreads are tight).
3. **All standard OTC swap tenors** (typically 1Y through 10Y, sometimes 20Y or longer).
4. **Any additional OTC quotes** (if your counterparties have provided 6M, 18M, or 7Y swaps).

For crude oil, a typical curve set might look like:

| Tenor | Source | Quote ($/bbl) |
|---|---|---|
| Spot | Physical market | 75.00 |
| 1M | WTI futures | 75.45 |
| 2M | WTI futures | 75.80 |
| 3M | WTI futures | 76.10 |
| 6M | Swap dealer | 76.50 |
| 1Y | Swap dealer | 76.80 |
| 2Y | Swap dealer | 77.20 |
| 5Y | Swap dealer | 77.50 |
| 10Y | Swap dealer | 77.60 |

Gaps exist: you have 1M, 2M, 3M, then a jump to 6M, then to 1Y, etc.

## Step 2: Interpolate near-term gaps (monthly and quarterly)

Between spot and 1Y, you often need monthly or quarterly precision. If you have quarterly futures (Jan, Apr, Jul, Oct), you can interpolate the intervening months.

**Linear interpolation** is the simplest: assume the forward price moves in a straight line between two known points.

Example: You have March futures at $76.10 and June futures at $76.50 (a gap of $0.40 over 3 months, or 13.3 basis points per month). For April, interpolate:

April price ≈ 76.10 + (1/3) × 0.40 = 76.23

For May:

May price ≈ 76.10 + (2/3) × 0.40 = 76.37

This assumes a constant slope, which is often reasonable over 2–3 months. But it can create visible kinks if futures prices jump abruptly.

**Spline interpolation** (cubic or smoothing splines) is more sophisticated. Rather than a straight line, it fits a smooth curve through the known points, minimizing kinks and ensuring the curve is continuous in both level and slope.

Spline methods are preferred by risk managers because they:

- Avoid sharp angles (which are unrealistic for commodity prices).
- Ensure the second derivative is continuous (smooth curvature).
- Reduce arbitrage opportunities from interpolation artifacts.

## Step 3: Splice the futures curve into the swap curve

Once you have a smooth curve from spot to 1Y (using futures and spline), you need to connect it to the 1Y swap quote and beyond.

Futures and swaps may not quote at exactly the same price even for the same maturity (say, the December futures and a 1Y swap starting December 1). The differences reflect:

- **Timing**: Futures are daily mark-to-market; swaps settle on agreed dates.
- **Optionality**: Some futures embed delivery options (choose month, location); swaps are cash-settled.
- **Bid-ask**: Futures are tightly bid-ask; swaps wider.

A trader typically uses the swap curve for long-dated forward prices (1Y and beyond) because swaps are the more liquid, standard instrument for multi-year commodities bets. The futures curve provides precision near-term.

The splice point is usually at 1 year. You fit:

- **Futures curve** from spot to 1Y (monthly granularity).
- **Swap curve** from 1Y onward (annually or semi-annually, interpolated as needed).

If there is a discontinuity at 1Y (futures quote at 76.80, swap quote at 76.85), you must choose: use the futures price (if nearer-term is more reliable) or use the swap (if you believe the swap is the truer market rate). Often, traders take a weighted blend based on confidence in each source.

## Step 4: Interpolate swap tenors and extrapolate beyond 10Y

Between standard swap tenors (1Y, 2Y, 3Y, 5Y, 10Y), interpolate missing maturities. If you need the 18-month price:

18M is 50% of the way from 1Y to 2Y (since 18M = 1.5Y). Linear or spline interpolation gives:

18M price ≈ 76.80 + 0.50 × (77.20 - 76.80) = 77.00

For tenors beyond 10Y (say, 15Y or 20Y), most markets lack liquid swaps. Traders extrapolate by assuming:

1. **Flat**: The 10Y price is assumed to hold for all longer tenors (conservative, common for long-term planning).
2. **Linear extension**: Extend the slope of the 5Y–10Y segment beyond 10Y.
3. **Theoretical assumption**: If there is no new information, assume the forward price converges to an expected long-term average or to the long-dated swap rate (if available).

Many risk frameworks use flat extrapolation (30-year equals 10-year) because there is little market information to support a different view.

## Step 5: Validate and smooth the final curve

The constructed curve must pass sanity checks:

- **Monotonicity**: Does the curve go consistently up, down, or sideways, or are there unexplained reversals? A reversal may reflect real market dislocations (like a [curve kink](/commodity-curve-kink-storage-constraint/) from storage constraints) or interpolation artifacts.
- **Smoothness**: Are there visible kinks where you spliced futures and swaps? Adjust the splice point or use spline smoothing to reduce them.
- **[Contango](/contango/) / [Backwardation](/backwardation/) structure**: Is the curve shape consistent with known supply-demand dynamics? If crude oil is suddenly backwardated at a 5-year tenor (futures > swaps), investigate why; it is unusual.
- **Volatility**: Compare the curve to yesterday's curve. Large shifts in the 5Y–10Y segment without news may indicate a data error.

A trader who constructs a curve should plot it visually and eyeball it for anomalies. Obvious kinks or reversals are red flags.

## Step 6: Update and rebalance regularly

Commodity swap markets move daily. Quotes that were tight yesterday are stale today. A production hedge portfolio, a risk model, or a valuation framework must be updated frequently—often daily or weekly for actively managed books.

When you rebalance:

1. Pull fresh swap quotes from dealers.
2. Update the futures curve (most liquid near-term contracts).
3. Re-interpolate and re-splice.
4. Recalculate all positions, valuations, and risks.

Markets can shift structure quickly. A curve that was flat at 1–2 years can steepen if demand shocks hit; a smooth contango can develop a [kink](/commodity-curve-kink-storage-constraint/) if storage fills. Regular updates ensure your curve reflects the current market regime.

## Challenges in curve construction

**Liquidity cliffs**: OTC swaps in some commodities (e.g., industrial metals) are much less liquid than crude or natural gas. Bid-ask spreads widen sharply at 5Y and longer, and dealer quotes may be stale.

**Market disruptions**: During stress (2020 oil crash, 2022 energy crisis), normal correlations and spreads break down. Futures and swaps may diverge significantly. Interpolation that assumes smooth transitions fails.

**Commodity-specific issues**: Agricultural commodities have seasonal curves with sharp [kinks](/commodity-curve-kink-storage-constraint/) at harvest. Metals have regional and storage-driven dislocations. A generic spline may not capture these patterns.

**Data quality**: Errant quotes (a dealer fat-fingers a swap price) or staleness (a dealer hasn't updated prices since yesterday) can pollute the curve. Traders must filter for outliers and reconcile sources.

## Practical curve tools

Most commodity trading systems (Bloomberg, Refinitiv, FactSet) provide pre-constructed curves, but traders often build custom curves for risk models, hedging programs, or internal valuations. Common tools include:

- **Pandas / NumPy** (Python): Interpolation, splicing, and plotting.
- **Excel with add-ins**: Simpler for small curves; limited for large, real-time books.
- **QuantLib** (open-source): Full curve construction, discounting, and risk calculations.
- **Proprietary systems**: Large desks build custom curve engines tied to their booking and risk systems.

A trader new to curve construction should start with linear interpolation and simple splicing, then graduate to spline methods and more sophisticated fitting as sophistication grows.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — OTC instruments that form the backbone of long-dated commodity curves.
- [Futures Contract](/futures-contract/) — Standardized contracts that anchor near-term curves.
- [Forward Contract](/forward-contract/) — Custom OTC agreements for non-standard tenors.
- [Contango](/contango/) — Normal upward-sloping curve structure and carry economics.
- [Backwardation](/backwardation/) — Inverted curves signaling scarcity or demand spikes.
- [Commodity Curve Kinks Caused by Storage Constraints](/commodity-curve-kink-storage-constraint/) — Dislocations that challenge smooth curve fitting.

### Wider context

- [Spot Rate](/spot-rate/) — Today's price; anchor for all forward curves.
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Using commodity curves to value future cash flows.
- [Basis Risk](/basis-risk/) — Mismatch between hedging instrument and physical position.
- [Price Discovery](/price-discovery/) — How markets aggregate supply and demand information.
- [Sensitivity Analysis Valuation](/sensitivity-analysis-valuation/) — Testing valuations across curve scenarios.

</div>
