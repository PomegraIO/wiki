---
title: "Variance Ratio Test"
description: "A statistical test comparing return variance across different holding periods to detect deviations from random walk behavior, exposing momentum and mean reversion."
keywords:
  - variance ratio test
  - random walk
  - market efficiency
  - momentum detection
  - mean reversion
image: "/svg/ratios.svg"
---

*If stock prices follow a random walk—moving up or down each period with no pattern—then variance should grow linearly with time. A four-day variance should be roughly four times a one-day variance. The **Variance Ratio Test** compares actual variances across timeframes to see if this holds. When it doesn't, markets reveal memory: momentum that makes recent winners keep winning, or mean reversion that brings extreme moves back to centre.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Variance Ratio Test — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for risk metrics." />

<div class="wiki-infobox-caption">Comparing return variance at different horizons to test for random-walk departures.</div>

|   |   |
|---|---|
| **What it is** | Ratio of k-period return variance to k times the 1-period variance. |
| **Formula** | VR(k) = Var(Rk) / (k × Var(R1)) |
| **Expected under random walk** | VR(k) = 1.0 for all k. |
| **VR > 1** | Variance is higher than random walk predicts; momentum or persistence. |
| **VR < 1** | Variance is lower than random walk predicts; mean reversion or negative autocorrelation. |
| **Range** | 0 to unbounded; 1.0 is the neutral hypothesis. |

</aside>

## The logic: why random walk variance scales linearly

Assume a stock's returns follow pure randomness. Each day, it's equally likely to jump +1% or –1% (simplistically). Over one day, variance is 1%.

Over four days, the returns compound: (1 ± 1%) × (1 ± 1%) × (1 ± 1%) × (1 ± 1%). If the changes are truly independent, the four-day return variance should be 1% × 4 = 4% (variance adds linearly under independence). The variance ratio VR(4) = 4% / (4 × 1%) = 1.0.

Now suppose day-to-day returns are *not* independent. If a 1% jump on Day 1 makes a 1% jump on Day 2 more likely (momentum), then the four-day return is amplified; variance inflates beyond 4%, and VR(4) > 1.0. If a 1% jump makes a –0.8% correction on Day 2 more likely (mean reversion), variance shrinks below 4%, and VR(4) < 1.0.

By testing whether VR(k) = 1 across multiple k values (2, 4, 8, 16 periods), you uncover *temporal structure* in prices. Markets are not random walks—they reveal preferences for mean reversion or momentum at different timescales.

## Calculating the variance ratio

Take daily returns for 500 trading days (approximately two years). Denote them r₁, r₂, …, r₅₀₀.

**One-day variance:** Var(R₁) = variance of {r₁, r₂, …, r₅₀₀}.

**Four-day variance:** Construct four-day returns: {r₁ + r₂ + r₃ + r₄, r₅ + r₆ + r₇ + r₈, …}. Then Var(R₄) = variance of these cumulative returns.

**Variance Ratio:** VR(4) = Var(R₄) / (4 × Var(R₁)).

If VR(4) = 1.2, four-day returns are 20% more variable than random walk predicts. This hints that a move on day 1 is likely to persist into days 2–4 (momentum).

## What the test reveals at different horizons

For most stocks and indices, the variance ratio *varies* across k:

- **VR(2) to VR(4):** Often slightly below 1.0 (mean reversion on very short timescales).
- **VR(8) to VR(20):** Often above 1.0 (momentum dominates medium-term; winners keep winning).
- **VR(60+):** Often drifts back toward 1.0 or slightly below (long-term reversion to fundamentals).

This pattern suggests markets are *not* random walks at any single timescale, but different timescales have different biases. A trader exploiting VR(8) > 1.2 might ride momentum, while a rebalancer exploiting VR(4) < 0.95 might bet on reversal.

## Statistical significance: beyond the ratio

Computing VR(k) is half the battle; testing whether it's statistically different from 1.0 requires a test statistic. Lo and MacKinlay (1988) showed that under the random walk null, VR(k) is asymptotically normal. A z-score test tells you if the deviation is real or sampling noise:

z = (VR(k) – 1) / SE(VR(k))

If |z| > 1.96 (at the 5% level), you can reject the random walk hypothesis. A VR(8) = 1.05 with small sample size might not be significant; a VR(8) = 1.15 over 20 years likely is.

## Market implications and practical limits

Evidence from the variance ratio test suggests:

1. **Equities show mild momentum.** Over weeks and months, VR often exceeds 1.0, meaning winners keep winning. This supports [momentum](/momentum-investing/) strategies and explains why [trend-following](/trend-following/) funds exist.

2. **Very long horizons (years) revert.** VR(250) or VR(500) sometimes drops below 1.0, suggesting mean reversion dominates multiyear moves. Extreme valuations do eventually correct.

3. **Differences by asset class.** [Currencies](/currency-risk/) and commodities show different patterns; [forex](/leverage-ratio-forex/) pairs often exhibit stronger mean reversion than equities.

4. **Time-varying results.** A market in boom phase has different VR(k) patterns than one in crisis. The test is static; it doesn't adapt to regime change.

The test's practical limits: VR(k) is noisy with real-world data (transaction costs, bid-ask spreads, non-synchronous trading). A significant variance ratio doesn't guarantee a profitable trade—you still face implementation costs and the risk that the pattern breaks.

## Relation to efficient markets and predictability

The random walk hypothesis is a building block of the efficient market hypothesis. If VR(k) ≠ 1 significantly, prices contain predictable patterns, and markets are not efficient at that horizon. Many academics interpret significant variance ratios as evidence that:

- Arbitrage hasn't fully exploited the pattern, or
- The pattern is real but too small (after costs) to trade profitably, or
- The market is inefficient at that timescale.

Most economists accept that variance ratios deviate meaningfully from 1 in real data—rejecting the strict random walk—yet debate whether this creates genuine profit opportunities or is noise.

## See also

<div class="wiki-seealso">

### Closely related

- [Beta](/beta/) — a measure of systematic sensitivity; independent of variance ratio patterns.
- Market Efficiency — the hypothesis that variance ratios test; random walk is one component.
- [Momentum](/momentum-investing/) — variance ratios above 1 support momentum strategies.
- Mean Reversion — variance ratios below 1 suggest reversal trading.
- Autocorrelation — the statistical root of non-unity variance ratios.
- [Volatility Smile](/volatility-smile/) — option prices embed expectations about return distribution; complements variance ratio tests.

### Wider context

- [Trend Following](/trend-following/) — strategy exploiting positive variance ratios.
- [Algorithmic Trading](/algorithmic-trading/) — uses variance ratio and similar tests to detect tradeable patterns.
- [Price Discovery](/price-discovery/) — how information is incorporated; variance ratios reveal speed and overshoot.
- [Factor Investing](/factor-investing/) — momentum and value factors have different variance ratio signatures.

</div>
