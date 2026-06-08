---
title: "Convexity Adjustment in Swap Pricing"
description: "Why in-arrears and CMS swaps need convexity adjustment to their forward rates, and how the correction direction depends on payoff structure."
keywords:
  - convexity adjustment
  - swap pricing
  - in-arrears swap
  - cms swap
  - forward rate
  - derivatives pricing
  - interest rate swaps
image: /svg/derivatives.svg
---

*A **convexity adjustment** in swap pricing corrects the forward rate used to value floating-rate payments when the reset and settlement dates do not align, or when the coupon itself depends on forward-rate derivatives. The adjustment direction depends on whether you are long or short the convexity risk—rewarding one counterparty for bearing the interest-rate volatility embedded in the payoff.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Convexity Adjustment — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A small but material correction to [forward rates](/spot-rate/) in non-standard swap structures.</div>

|   |   |
|---|---|
| **Definition** | Additive or subtractive correction to the rate used in swap valuation when reset and settlement do not coincide, or when the coupon embeds a [derivative](/option/) |
| **When it appears** | In-arrears swaps, [CMS swaps](/interest-rate-swap/), constant-maturity swaps, any structure linking payment to a forward-rate derivative |
| **Why it matters** | Ignoring it biases pricing by 0.5–5 bps or more; the size grows with [volatility](/implied-volatility/) and time to reset |
| **Who pays whom** | The party holding the "short convexity" position (owes the adjustment) to the "long convexity" party |
| **Common approximation** | For small [volatility](/historical-volatility/), adjustment ≈ (volatility²) × (time-to-reset) × (derivative of rate w.r.t. forward) |

</aside>

## The basic mismatch: in-arrears timing

In a vanilla interest-rate [swap](/interest-rate-swap/), the floating rate is set at the start of the period and paid at the end. A borrower locks in a rate for the next three months on day 0, and pays interest on day 90. The forward rate on day 0 is a good estimate of what that three-month rate will actually be on day 90, especially over short horizons.

But in an **in-arrears swap** (also called a delayed-setting swap), the rate is determined at the *end* of the period and paid immediately. On day 90, the floating rate for the period just finished is observed, and you pay that rate the same day. Now the "forward rate" used to price the swap is not the rate locked in at the swap start—it is the rate that will actually exist at day 90. These are different expectations, and the mismatch creates convexity.

The practical effect: if interest-rate volatility is positive (rates move), the observed rate at day 90 will not equal the day-0 forward expectation for that same rate. The convexity adjustment compensates the counterparty absorbing this extra risk.

## Why CMS and other structured coupons need adjustment

A constant-maturity swap (CMS) pays a coupon equal to a long-dated swap rate—say, the 10-year swap rate observed every six months. A borrower receives the 10-year rate, which is itself a derivative of the [yield curve](/yield-curve/). The 10-year rate does not move linearly with the short end of the curve; it depends on [convexity](/duration/) of the longer-duration bonds underlying it.

Pricing a CMS swap naively—using the expected future 10-year rate from the current yield curve—understates the risk. The convexity adjustment accounts for the fact that if yields rise steeply, the 10-year rate falls in a non-linear way, and vice versa. The counterparty short the CMS coupon is bearing this non-linearity and deserves compensation.

This adjustment applies broadly: any time a swap coupon depends on a [forward-looking rate derivative](/derivatives-hedging/) (not just historical rates), convexity matters.

## The direction of the adjustment: who wins?

Whether the convexity adjustment is added to or subtracted from the fair-value rate depends on the payoff structure and who is bearing the risk.

**In-arrears swaps**: The party that is effectively short interest-rate convexity—typically the floating-rate payer—receives an adjustment. If rates rise sharply and then fall, the observed in-arrears rate is higher than the forward expectation, and the floating payer loses. The lender (fixed payer) compensates by adding a few basis points to the coupon.

**CMS swaps**: The receiver of the 10-year rate (the long-dated coupon) benefits when long rates are volatile, because occasional large spikes in the swap rate yield outsized coupons. The CMS payer (short the long-dated coupon) bears this risk and demands a negative adjustment—a reduction in the CMS coupon or a cash payment up front.

The direction always flows from the volatility absorber to the risk holder. High volatility makes the adjustment larger; low volatility makes it negligible.

## Calculating and approximating the adjustment

Full convexity adjustment calculations require numerical methods or closed-form solutions for specific curve models. The [Black-Derman-Toy](/black-scholes-model/) model and its extensions are standard in derivatives trading.

For a quick approximation (especially useful for gauging whether an adjustment is material), the Taylor-expansion rule of thumb is:

**Convexity adjustment ≈ σ² × T × γ**

where:
- **σ** is the implied volatility of the reset rate (e.g., 3-month or 10-year rate)
- **T** is the time to reset
- **γ** (gamma) is the second derivative of the swap value with respect to the reset rate

For example, if implied volatility is 80 basis points, time to reset is 6 months, and gamma is –0.5 per basis point, the adjustment is roughly 0.0064 × 0.5 × 0.5 = 1.6 bps. This is small but noticeable in a tight-margin swap.

## Why traders care

In liquid markets (vanilla interest-rate swaps), convexity adjustments are often priced implicitly and are already embedded in quoted swap rates. But in structured or bespoke swaps—CMS products, bermudan swaptions, mortgage-backed [securities](/securities-and-exchange-commission/)—the adjustment can swing a deal's internal rate of return by 10–50 basis points.

Traders who ignore convexity are either mispricing the risk or relying on the market quote to absorb it. In client-facing negotiations, knowing the direction and magnitude of the adjustment can shift how a deal is framed: is the structure beneficial because rates are expected to rise, or because embedded convexity is expensive and you are capturing that premium?

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate Swap](/interest-rate-swap/) — foundational swap structure and pricing mechanics
- [Duration](/duration/) — measure of curve convexity and rate sensitivity
- [Implied Volatility](/implied-volatility/) — the input driving convexity adjustment size
- [Forward Contract](/forward-contract/) — underlying expectation that convexity adjusts
- [Gamma](/gamma/) — the second-order sensitivity that quantifies convexity in options
- [Yield Curve](/yield-curve/) — the term structure underlying CMS and longer-dated coupons
- [Derivatives Hedging](/derivatives-hedging/) — why convexity risk matters in real portfolios

### Wider context

- [Swap](/interest-rate-swap/) — broader swap market and instrument types
- [Bond](/bond/) — fixed-income instruments affected by the same convexity principles
- [Mortgage-Backed Security](/mortgage-backed-security/) — structured products with embedded convexity
- [Risk-Weighted Assets](/risk-weighted-assets/) — regulatory framework for derivatives valuation
- [Sensitivity Analysis (Valuation)](/sensitivity-analysis-valuation/) — frameworks for measuring rate and volatility impacts

</div>
