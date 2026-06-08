---
title: "Dividend Discount Model With Negative or Declining Growth"
description: "How the DDM formula applies when dividends are expected to shrink over time, with examples from declining industries and mature firms returning cash."
keywords:
  - dividend discount model negative growth
  - declining dividend valuation
  - negative growth rate ddm
  - mature company valuation
image: /svg/valuation.svg
---

*A **dividend discount model with negative growth** is a straightforward extension of the standard DDM: it values stocks whose dividends are expected to fall over time. The formula still works, but the interpretation flips—you're valuing a cash stream that shrinks, not grows, and the stock's value is what the shrinking dividend warrants.*

## When Dividends Decline

Not all dividend stocks are growth stories. Many face structural headwinds: demand erosion, technological disruption, or a deliberate shift to returning cash faster than reinvestment builds earnings. Common examples include:

- **Declining industries.** Coal, print media, and traditional retail companies saw dividends shrink as the market contracted.
- **Mature firms harvesting cash.** A utility or manufacturer might explicitly return more cash than it earns, milking decades of accumulated assets with no intention to reinvest or grow. Think of a private equity-owned portfolio company or an activist-target firm.
- **Cyclical downturns.** A bank or oil company in a deep cycle may sustain dividends while earnings collapse, reducing the payout ratio and setting up lower dividends when the cycle turns.
- **Strategic retreat.** A pharmaceutical firm losing patent exclusivity and facing generic competition might preserve dividends longer than earnings warrant, depleting cash reserves, then cut dividends sharply.

## The Formula Still Works

The perpetual DDM formula is:

> Stock Value = D₁ / (r – g)

where g is the dividend growth rate. If g is negative—say, dividends are expected to decline 3% annually—you simply plug in g = –0.03.

**Example:**
- Current dividend: $5 per share
- Expected next year's dividend: $5 × (1 – 0.03) = $4.85
- Required return: 10%
- Stock value = 4.85 / (0.10 – (–0.03)) = 4.85 / 0.13 = $37.31

The denominator grows because you're subtracting a negative number, which is equivalent to adding. The stock's value declines as the dividend shrinks, but the shrinkage is slow (3% per year), so the value isn't zero—it's finite.

## Why Negative Growth Happens

**Business decline.** A firm's addressable market is shrinking faster than it can pivot. Newspapers faced this starkly: advertising revenue eroded 50%+ over 15 years. Dividends had to follow earnings down. The stock becomes a "value trap"—it looks cheap on yield (say, 8%), but the dividend is unsustainable, and yields keep rising as prices fall.

**No growth, no reinvestment needed.** A water utility or toll road in a mature market generates steady cash with minimal capex. It can safely return 80–90% of earnings. If inflation is modest, real dividend growth is near zero. The effective growth rate might be 1–2% nominal (inflation plus a small volume increase), or zero, or even negative if real demand is flat.

**Private equity playbook.** PE firms often acquire mature businesses with stable cash flows, refinance them with debt, and pay out maximum cash to investors while reducing the equity base. Dividends (or equivalently, special distributions) can exceed annual earnings, causing equity to shrink. From a shareholder's perspective, the dividend growth is negative because the retained earnings pool is being depleted.

## Distinguishing True Decline From Temporary Payout Shifts

A critical first step is determining whether negative dividend growth reflects fundamental business decline or a deliberate payout decision.

A firm that cuts dividends to fund acquisitions or debt paydown might have fundamentally stable or growing earnings, but consciously lower payout ratios. Conversely, a firm cutting dividends because earnings are falling faces an uphill battle to restore them.

Analyzing why growth is negative is essential:
- **Falling earnings and rising payout ratio?** The business is contracting. Negative growth may persist indefinitely.
- **Stable earnings but falling payout ratio?** The firm is retaining cash for strategic reasons. Dividends might recover if the strategy succeeds.
- **Earnings rising but dividends falling faster (as a policy)?** The firm is hoarding cash or deleveraging. Dividends might resume growth in a few years once the balance sheet is rebuilt.

Only the first scenario justifies a negative growth assumption in perpetuity. The other two are temporary and warrant a multi-stage model: a phase of negative growth, followed by a transition back to positive growth or stability.

## A Multi-Stage Approach for Transitions

In practice, few dividends decline at a constant rate forever. A more realistic model breaks the forecast into phases.

**Phase 1: Decline.** For the next 5–7 years, dividends shrink at 3% annually due to market contraction or strategic cash return.

**Phase 2: Stabilization.** Dividends flatten or return to low single-digit growth as the firm reaches a steady state.

You then calculate the present value of Phase 1 (a declining annuity) and the present value of Phase 2 (a stable perpetuity starting from Year 8's dividend, discounted back).

**Example:**
- Current annual dividend: $5
- Phase 1 (Years 1–7): Dividend declines 3% per year
- Phase 2 (Year 8 onward): Dividend stable at $4.09 (Year 7 value), 0% growth
- Required return: 10%

Phase 1 present value of declining annuity = 5 × [(1 – ((1.03 / 1.10)^7)) / (0.10 – (–0.03))] ≈ $30.20

Phase 2 terminal value = 4.09 / 0.10 = $40.90, discounted back 7 years = 40.90 / 1.10^7 ≈ $21.05

Total value ≈ $30.20 + $21.05 = $51.25

This is more realistic than a perpetual 3% decline, which would eventually approach zero.

## The "Value Trap" Risk

A stock with negative dividend growth is a classic value trap: it looks "cheap" in yield terms, but the low price has already priced in the decline. New investors buying for the current yield often underestimate how far the dividend can fall.

Consider a stock yielding 8% (price $50, dividend $4). If the dividend declines 5% per year, in 10 years the annual dividend will be $2.46, and the firm may have cut the payout entirely if losses accelerate. An investor buying for the 8% yield is setting themselves up for both capital loss and dividend disappointment.

This is why negative-growth valuations must be paired with a conviction about when (or if) the decline stops. If you're valuing a declining newspaper at $20 per share with a 7% dividend, you're implicitly betting that in 10 years, the dividend isn't zero and the business hasn't collapsed. That's a speculative view, not a safe-yield bet.

## When Negative Growth is Actually Zero Growth

Many mature, stable firms have no real growth. A regulated utility earning a 10% return on capital, with 0% real growth (just keeping pace with inflation), has g ≈ 0. If you model this as g = 0.02 (inflation) or g = –0.01 (slight real decline), the valuation is nearly identical.

The difference becomes material only when you're confident growth is substantially negative (below inflation). Most mature, established dividend payers—utilities, blue-chips, REITs—are better modeled with g = 0 to 2%, not with negative growth.

Negative growth is reserved for firms with genuine headwinds: industry contraction, technological obsolescence, or a deliberate policy of harvesting cash faster than business growth permits.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Discount Model](/dividend-discount-model/) — the foundational formula and stable-growth assumption
- [Dividend Payout Ratio](/dividend-payout-ratio/) — how much of earnings are returned
- [Required Rate of Return in Dividend Discount Models](/required-rate-of-return-dividend-model/) — choosing r for declining firms
- Declining Annuity — the math behind shrinking cash flows
- Growth Rate in Valuation — estimating perpetual growth assumptions

### Wider context

- [DDM vs DCF: Key Differences in Equity Valuation](/ddm-vs-dcf-valuation-differences/) — when to use dividend models versus cash flow approaches
- Value Trap — why cheap yields can signal danger, not opportunity
- [Dividend Discount Model for Bank Valuation](/dividend-discount-model-bank-valuation/) — DDM applied to mature financial firms
- [Real Estate Investment Trust](/real-estate-investment-trust/) — REITs often have mature, stable dividend growth
- [Relative Valuation](/relative-valuation/) — comparing yield to peers to identify false bargains

</div>
