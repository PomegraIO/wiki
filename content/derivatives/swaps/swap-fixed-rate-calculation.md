---
title: "How the Fixed Rate on a Swap Is Calculated"
description: "How swap dealers derive the at-market fixed rate using discount factors and forward rates, ensuring zero initial value."
keywords:
  - how is the fixed rate on a swap calculated
  - swap rate calculation discount factors
  - par swap rate formula
  - fixed leg swap pricing
image: /svg/derivatives.svg
---

*The fixed rate on a **swap**—the rate that a dealer quotes and both sides lock in at inception—is calculated so that the swap has zero initial value. The dealer computes it by discounting each floating cash flow to its present value using the current yield curve, then solves for the single fixed rate that makes the present value of all fixed payments equal to the present value of all floating payments. The result is fair value, requiring no upfront payment from either party.*

<div class="wiki-hatnote">

This article explains the mechanics of fixed-rate pricing in a standard interest-rate [swap](/swap/). For an overview of how swaps work, see [Swap](/swap/); for valuation after inception, see [Interest Rate Swap](/interest-rate-swap/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap Rate Calculation — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">The fixed rate is the discount-weighted average of forward rates, solved so net present value is zero.</div>

|   |   |
|---|---|
| **Purpose** | Lock in a fair fixed rate that requires no upfront cash exchange |
| **Key input** | Current [yield curve](/yield-curve/) and implied forward rates |
| **Calculation method** | Solve for the rate that equates PV of fixed and floating legs |
| **Why zero NPV** | Swap is a derivative; dealer passes through no profit at inception |
| **Who calculates it** | Swap dealer (bank) using real-time pricing models |
| **Adjusted for** | [Counterparty risk](/counterparty-risk/), collateral agreements, dealer spread |

</aside>

## The Core Principle: Zero Net Present Value

A **swap** is an [exchange of cash flows](/cash-conversion-cycle/) between two parties. In a vanilla interest-rate swap, one side (the *fixed payer*) pays a constant rate; the other (the *floating payer*) pays a rate that resets periodically (typically [SOFR](/sofr/) or another [benchmark](/interest-rate/) plus a spread).

At *inception*—the moment the swap is entered—neither party should be giving away money for free. The dealer's job is to quote a fixed rate such that the swap starts at zero value. No present value is owed up front.

Mathematically:

**PV(Fixed Leg) = PV(Floating Leg)**

The fixed rate that satisfies this equation is the **par swap rate**—the rate agreed upon.

## Discounting and Forward Rates

To calculate the PV of each leg, the dealer must discount future payments. The **[discount factor](/discount-rate/)** for a payment arriving *n* periods ahead is derived from the current [yield curve](/yield-curve/).

Suppose the yield curve shows that the one-year rate is 2%, the two-year rate is 2.5%, and the three-year rate is 3%. Each of these points on the curve contains implicit **forward rates**—the expected rate between, say, year 1 and year 2, or year 2 and year 3.

**Discount factor for year 1** = 1 / (1 + 2%) ≈ 0.9804
**Discount factor for year 2** = 1 / (1 + 2.5%)^2 ≈ 0.9518
**Discount factor for year 3** = 1 / (1 + 3%)^3 ≈ 0.9151

The floating leg's value is the sum of each expected floating payment (based on the forward curve) discounted back at these factors. The fixed leg's value is the sum of fixed payments at the *unknown* fixed rate, also discounted.

## Solving for the Par Swap Rate

Let's walk through a simplified 3-year swap paying annually.

**Assume:**
- Discount factors: 0.9804, 0.9518, 0.9151 (as above)
- Forward rates embedded in the yield curve: 2%, 2.5%, 3%
- Notional principal: $1 million

**Floating leg PV:**
- Year 1 payment: 2% × $1M = $20,000 → PV = $20,000 × 0.9804 = $19,608
- Year 2 payment: 2.5% × $1M = $25,000 → PV = $25,000 × 0.9518 = $23,795
- Year 3 payment: 3% × $1M = $30,000 → PV = $30,000 × 0.9151 = $27,453

**Total Floating Leg PV = $70,856**

**Fixed leg PV:** (where *R* is the unknown fixed rate)
- Year 1: *R* × $1M × 0.9804
- Year 2: *R* × $1M × 0.9518
- Year 3: *R* × $1M × 0.9151

**Total Fixed Leg PV = R × $1M × (0.9804 + 0.9518 + 0.9151) = R × $1M × 2.8473**

**Setting them equal:**
R × $1M × 2.8473 = $70,856

**R = $70,856 / (1,000,000 × 2.8473) = 0.0249 = 2.49%**

So the fair fixed rate is **2.49%** on an annual [coupon-payment](/coupon-payment/) basis.

## Why This Rate Needs Adjustment

The above calculation gives the *pure* par rate in a frictionless market. In reality, dealers adjust for several factors:

**[Counterparty risk](/counterparty-risk/).** If the swap partner is riskier, the dealer may demand a higher fixed rate to compensate for default exposure.

**Collateral agreements.** Many swaps are cleared through central counterparties or are [OTC](/over-the-counter-market/) with collateral posted. The rate paid on posted collateral (often the [federal funds rate](/federal-funds-rate/) or a low overnight rate) affects pricing.

**Dealer spread.** The bank quoting the rate retains a small [bid-ask spread](/bid-ask-spread/). The fixed rate quoted to a customer may be slightly higher or lower than the true par rate, depending on which side of the swap the customer takes and how much flow the dealer sees.

**[Accrued interest](/accrual-accounting/) and settlement conventions.** Day-count conventions and the actual settlement date can shift the PV slightly.

## Post-Inception Valuation

Once the swap is in place and time passes, the floating rate resets, yields shift, and the swap's value changes. The floating payer now holds a valuable position if rates have fallen (fixed payments are now better than floating), or an underwater position if rates have risen.

This post-inception valuation uses the same discounting framework: recompute the PV of remaining fixed and floating payments at the *new* yield curve. The difference between the two legs is the [mark-to-market](/market-maker-trading/) gain or loss.

## The Role of the Yield Curve

The entire calculation rests on the current [yield curve](/yield-curve/). If the curve is steep—long-term rates much higher than short-term—the par swap rate will be correspondingly higher, because long-dated floating payments are discounted at higher rates. If the curve is flat or inverted, the par rate will be lower.

When the yield curve shifts—say, the Federal Reserve raises the [federal funds rate](/federal-funds-rate/)—the entire curve typically reprices upward. The next swap quoted will have a higher fixed rate than the previous one, because discount factors shrink (future cash is worth less in today's dollars).

This is why swap dealers are sensitive to [interest-rate risk](/interest-rate-risk/). A dealer who is long a 10-year swap (receiving fixed) loses money if the curve rises after inception, because the fair value of that fixed receipt falls as discount factors compress.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — Overview of swap mechanics and types
- [Interest Rate Swap](/interest-rate-swap/) — Detailed structure and uses
- [Discount Rate](/discount-rate/) — The foundation of present-value calculations
- [Yield Curve](/yield-curve/) — The input to all swap pricing
- [Forward Guidance](/forward-guidance/) — How forward rates are implied from spot curves

### Wider context

- [Counterparty Risk](/counterparty-risk/) — Why creditworthiness affects swap pricing
- [Derivatives Hedging](/derivatives-hedging/) — Why firms use swaps
- [Interest Rate Risk](/interest-rate-risk/) — How rate moves affect swap value
- [SOFR](/sofr/) — The modern floating benchmark
- [Spread](/bid-ask-spread/) — Dealer costs baked into quoted rates

</div>
