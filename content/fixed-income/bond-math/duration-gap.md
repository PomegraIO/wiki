---
title: "Duration Gap: Measuring Interest-Rate Exposure for Balance Sheets"
description: "Duration gap is the difference between the weighted average duration of assets and liabilities, revealing a balance sheet's net sensitivity to interest-rate changes."
keywords:
  - duration gap
  - assets liabilities interest rate
  - gap management
  - duration mismatch
  - interest rate sensitivity
  - balance sheet duration
  - liability-driven investing
image: "/svg/fixed-income.svg"
---

*A **duration gap** is the difference between the [duration](/duration-gap/) of a firm's assets and the duration of its liabilities. A positive gap means assets are longer-lived than liabilities; when rates rise, asset values fall more than liability values, squeezing equity. A negative gap exposes the balance sheet to the opposite risk. Banks, insurance companies, and pension funds all manage duration gaps to control interest-rate risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Duration Gap — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The maturity mismatch that determines how much equity swings when rates move.</div>

|   |   |
|---|---|
| **Definition** | Duration(Assets) − Duration(Liabilities) |
| **Positive gap** | Assets longer-dated; rate rise hurts equity value |
| **Negative gap** | Liabilities longer-dated; rate fall hurts equity value |
| **Zero gap** | Rates affect assets and liabilities equally; equity neutral |
| **Key users** | Banks, thrifts, insurance companies, pension funds |
| **Measurement unit** | Years (duration is in years) |
| **Related concept** | [Reinvestment risk](/reinvestment-risk-bonds/) (gap by maturity rather than sensitivity) |

</aside>

## What Duration Gap Measures

Duration is the weighted average time to receive a security's cash flows. For a bond paying coupons over time and a principal at maturity, duration is typically shorter than the maturity date. A 10-year bond might have a duration of 7 years, meaning price moves as if all cash arrives in 7 years.

When an institution borrows (creating liabilities) and lends or invests (creating assets), the durations of these two sides rarely match. If assets have a 7-year duration and liabilities have a 4-year duration, the duration gap is 7 − 4 = 3 years.

This gap matters because interest rates affect assets and liabilities differently. When rates rise:
- Bond values fall (inverse relationship)
- Longer-duration assets fall *more* in value than shorter-duration liabilities
- The gap widens, and equity value shrinks

A bank funded primarily by short-term deposits (low liability duration) and invested in long-term loans or bonds (high asset duration) runs a positive duration gap. Rising rates squeeze its equity. Conversely, a positive duration gap benefits when rates fall—asset values rise more than liability values.

## The Bank Example: Positive Duration Gap

A stylized bank balance sheet:

**Assets:**
- $100 million in 10-year loans, duration 8 years
- Asset duration: 8 years

**Liabilities:**
- $80 million in 3-year deposits, duration 2.8 years
- Liability duration: 2.8 years

**Equity:** $20 million (assets − liabilities)

**Duration Gap:** 8 − 2.8 = 5.2 years

Now suppose interest rates rise by 1% (100 basis points):

- Assets fall by 8% (duration 8 years × 1% rate move) = 8 million dollar loss
- Liabilities fall by 2.8% (duration 2.8 years × 1% rate move) = 2.24 million dollar loss
- Net loss to equity = 8 − 2.24 = 5.76 million

Equity shrinks from $20 million to $14.24 million, a 28.8% decline. The positive duration gap transformed a 1% rate move into nearly a 30% equity loss. This is [interest-rate risk](/interest-rate-risk/) made concrete.

## The Pension Fund Example: Negative Duration Gap

A pension fund has:

**Assets:**
- $500 million in equity ETFs and short-duration bonds, duration 3 years

**Liabilities:**
- $400 million in promised pension payouts, duration 12 years

**Equity:** $100 million (overfunded)

**Duration Gap:** 3 − 12 = −9 years (negative)

When rates rise:
- Assets fall by 3% = $15 million loss
- Liabilities (the present value of future pension payouts) fall by 12% = $48 million gain

The fund's equity actually *improves* because liabilities shrink faster than assets. A negative gap means rate increases help; rate decreases hurt.

## Why Institutions Care About Their Duration Gap

**Interest-rate risk management.** A positive gap exposes equity to rising rates. Managers hedge by shortening asset duration (sell long bonds, buy short bonds) or lengthening liability duration (refinance short-term debt into longer terms). A negative gap prompts the opposite moves.

**Earnings stability.** A large gap means earnings swing wildly with rate moves. Some institutions prefer gaps near zero, accepting lower average returns in exchange for less volatility.

**Regulatory capital requirements.** Bank regulators scrutinize duration gaps because they signal balance-sheet fragility. A bank with a large positive gap and rising rates may face pressure to hold more capital.

**Return optimization.** Some institutions deliberately run a gap—betting on the direction of rate moves. A mortgage lender with a positive gap profits if rates fall (asset prices rise more). But this is a bet, not a hedge, and many institutions prefer to be neutral.

## Calculating the Dollar Impact of a Rate Move

The **duration-gap formula** tells you how much equity changes for a given rate move:

**Change in Equity Value = −Duration Gap × Change in Rates × Market Value of Assets**

(The minus sign reflects that rising rates hurt a positive gap; falling rates hurt a negative gap.)

Using the bank example:
- Duration Gap = 5.2 years
- Rate move = +1%
- Asset value = $100 million
- Equity impact = −5.2 × 0.01 × $100M = −$5.2 million

This approximation assumes all assets and liabilities reprice at the same rate (a simplification; in reality, rate curve shapes matter).

## Beyond Simple Duration: Weighted Average and Ladders

Most institutions weight duration by the market value of assets (and liabilities) to avoid distortion. A bank with $1 million in 2-year duration assets and $99 million in 8-year duration assets has a weighted asset duration of approximately 7.9 years, not somewhere between 2 and 8.

Similarly, liabilities are weighted. If a bank funds itself 50% from 1-year deposits (duration ~1) and 50% from 5-year bonds (duration ~4.5), the weighted liability duration is 2.75 years.

## Gap Management Strategies

**Asset-liability matching (ALM).** Align asset and liability durations so the gap is near zero. This requires buying or selling securities, refinancing debt, and structuring new loans and deposits carefully. It is labor-intensive but minimizes equity volatility.

**Hedging with derivatives.** Use [interest-rate swaps](/duration-gap/) or [futures contracts](/futures-contract/) to synthetically change the effective duration of assets or liabilities without moving cash. A bank with a positive gap might enter a swap to convert fixed-rate assets into floating-rate, shortening effective duration.

**Laddering maturities.** Spread assets and liabilities across a range of maturities to avoid concentration. This reduces the impact of yield-curve twists and simplifies gap management.

**Accepting the gap and monitoring.** Some institutions choose not to hedge, accepting that equity will swing. They monitor the gap closely and adjust when exposure becomes uncomfortable.

## Duration Gap vs. Maturity Gap

Duration gap and maturity gap are related but distinct:

- **Maturity gap**: Weighted average maturity of assets minus weighted average maturity of liabilities. A crude measure; it ignores coupon timing.
- **Duration gap**: Accounts for all cash flows (coupons and principal), weighted by when they arrive. More accurate.

A zero maturity gap does not guarantee a zero duration gap. A 5-year bond with a 10% coupon has a shorter duration than a 5-year zero-coupon bond, so portfolios with the same maturity can have different durations.

## Practical Limits of Duration Gap Analysis

Duration gap assumes rates across the yield curve move by the same amount (a parallel shift). In reality, rates move differently at different maturities (a yield-curve twist). A bank with short-duration liabilities and long-duration assets is still exposed if short rates rise faster than long rates.

Duration also assumes linear price-yield relationships, which holds for small moves but breaks down for large moves. Very large rate swings expose issues like [convexity](/duration-gap/) (the curvature in the price-yield relationship).

Despite these limits, duration gap remains the standard tool for measuring interest-rate exposure in banking and fixed-income portfolio management.

## See also

<div class="wiki-seealso">

### Closely related

- [Reinvestment Risk in Bonds](/reinvestment-risk-bonds/) — Another dimension of rate risk; gap measures immediate price risk
- [Yield to Maturity vs Current Yield](/yield-to-maturity-vs-current-yield/) — Understanding yields helps interpret duration calculations
- [Interest-Rate Swap](/duration-gap/) — A tool for managing duration gaps
- [Bond Price Between Coupon Dates](/bond-price-between-coupon-dates/) — How accrued interest affects duration calculations
- [Futures Contract](/futures-contract/) — Another hedging tool for gap management

### Wider context

- [Bond](/bond/) — Foundation for understanding duration
- [Interest Rate Risk](/interest-rate-risk/) — The broader category of risks duration gap measures
- [Central Bank](/central-bank/) — How policy rate changes propagate to the yield curve
- [Balance Sheet](/balance-sheet/) — Where asset-liability management lives

</div>
