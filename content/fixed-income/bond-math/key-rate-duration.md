---
title: "Key Rate Duration"
description: "The sensitivity of a bond's price to a shift in yield at one specific maturity point on the yield curve."
keywords:
  - key rate duration
  - yield curve sensitivity
  - bond risk
  - duration
  - interest rate risk
image: "/svg/fixed-income.svg"
---

*The **key rate duration** measures how much a bond's price moves when the yield at a specific maturity point on the yield curve shifts by one basis point, holding other rates constant. It breaks down the full [duration](/duration/) into a granular map, showing which part of the yield curve poses the greatest price risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Key Rate Duration — at a glance</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark representing fixed-income instruments." />

<div class="wiki-infobox-caption">Bond price sensitivity to isolated yield moves at a particular point on the curve.</div>

|   |   |
|---|---|
| **What it is** | Price change (in dollars or percentage) per basis-point shift at one curve maturity |
| **Also called** | Partial duration, rate-curve sensitivity, yield-curve exposure |
| **Why it matters** | Tells you exactly where on the curve a bond's price risk lives |
| **Measured in** | Dollars (absolute) or percentage points (relative to bond price) |
| **Curve points tracked** | 2Y, 3Y, 5Y, 10Y, 30Y (or finer granularity) |

</aside>

## The curve is not flat

A bond's [duration](/duration/) tells you the average time-weighted risk exposure. But the [yield curve](/yield-curve/) is not flat. The 2-year point might move 20 basis points while the 10-year moves only 5. A 10-year bond's price will respond to 10-year yields more than to 2-year yields—yet standard duration treats all parallel shifts as equivalent.

Key rate duration disaggregates that risk. Instead of asking "how much will this bond fall if all yields rise 1 bp?", you ask: "how much will it fall if *only the 5-year point* rises 1 bp, with everything else frozen?" The answer is the **5-year key rate duration**.

A typical 10-year bond might have:
- 2Y key rate duration: 0.1
- 5Y key rate duration: 2.5
- 10Y key rate duration: 6.8
- 30Y key rate duration: 1.2

Sum those, and you approximate the bond's total [duration](/duration/). But now you see that its price is most sensitive to the 10-year point. The 30-year is almost irrelevant, and the 2-year barely registers.

## How it's calculated

Key rate durations are usually computed by "shocking" the yield curve at one node (maturity) and measuring the resulting price change. If you have a smooth yield curve from 2Y to 30Y, you might shock the 5Y point up by 1 basis point and interpolate neighbouring points using a spline or other smoothing method. The bond's repriced value minus its current value gives you the 5Y key rate duration.

Professional traders and portfolio managers use analytics software (Bloomberg, Refinitiv, internal systems) to compute these automatically. The maths relies on [discounted cash flow](/discounted-cash-flow-valuation/) mechanics: each coupon and principal repayment is discounted at the spot rates corresponding to its maturity. Tweak one spot rate, recalculate, and you have your sensitivity.

Different software vendors may use slightly different curve-construction methods (splines, bootstrapping, interpolation rules), so key rate durations can vary marginally between platforms. But the concept is invariant.

## Why traders care

In practice, the yield curve's movements are *not* parallel. The belly (5Y–10Y) might steepen while the long end flattens. Understanding key rate duration lets you:

1. **Target your hedge** — If you own a 10-year bond and only want to shed 5-year risk, you can [short-sell](/short-selling/) a 5-year [Treasury bill](/treasury-bill/) or use a [futures contract](/futures-contract/) on the 5Y. Key rate duration tells you exactly how much 5Y exposure you're carrying.

2. **Build a curve bet** — If you believe the 10-year will rally but the 2-year will sell off (steepening), you can buy a 10-year [corporate bond](/corporate-bond/) and short a 2-year Treasury. Key rate durations let you size each leg precisely.

3. **Assess [basis risk](/alternative-trading-system/)** — When you [hedge](/hedge-fund/) a bond with Treasury futures, the hedging contract and your bond don't perfectly track each other. Key rate durations help isolate the curve-specific risk that won't be hedged away.

4. **Compare bonds with different structures** — A 10-year [mortgage-backed security](/mortgage-backed-security/) and a 10-year corporate bond have the same [maturity](/expiration-date/), but their cash flows differ: mortgages prepay when rates fall. Their key rate duration profiles will diverge, revealing why they're not perfect substitutes.

## Key rate duration vs. effective duration

[Duration](/duration/) comes in flavours. Effective duration (the most common variant) assumes a parallel shift across all maturities. Key rate duration is its more surgical cousin.

For most bonds, adding up the key rate durations across the curve approximates the effective duration. But for bonds with optionality—callable bonds, mortgages, floating-rate instruments—the relationship breaks down. Those bonds' price responses to parallel moves differ from their response to isolated moves, and that difference is often where sophisticated pricing begins.

## The curve is dynamic

Key rate durations assume you can isolate a single point. In reality, yield curve moves are correlated. A shock to the 5-year usually ripples to the 3Y and 7Y as well. So while key rate durations are powerful diagnostic tools, they are idealisations. They shine when you're using them to compare bonds or to micro-hedge a specific maturity bucket. For broad market risk, you still want [duration](/duration/) and [convexity](/alternative-trading-system/).

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the average time-weighted price sensitivity of a bond to a parallel yield shift
- [DV01](/dv01/) — the dollar value of a one-basis-point move in any direction
- [Dollar Duration](/dollar-duration/) — the absolute dollar price change per basis point
- [Yield Curve](/yield-curve/) — the relationship between maturity and yield across the market
- [Effective Duration](/duration/) — duration computed from actual price changes, not analytical formulas
- [Convexity](/alternative-trading-system/) — how duration itself changes with yield moves

### Wider context

- [Bond](/bond/) — the fundamental fixed-income instrument
- [Treasury Bill](/treasury-bill/) — the short-maturity benchmark for curve anchoring
- [Mortgage-Backed Security](/mortgage-backed-security/) — a complex bond whose durations shift with rates
- [Futures Contract](/futures-contract/) — tools for hedging specific curve points
- [Interest Rate Risk](/interest-rate-risk/) — the broad category of price volatility from rate moves

</div>
