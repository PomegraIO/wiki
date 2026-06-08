---
title: "Interest Rate Ceiling and Floor"
description: "How caps and floors embedded in floating-rate bonds and loans limit upside and downside interest rate risk."
keywords:
  - interest rate cap
  - interest rate floor
  - collar
  - floating rate note
  - interest rate derivative
  - option-embedded bond
  - rate insurance
image: /svg/monetary.svg
---

*A borrower facing a [floating-rate loan](/interest-rate/) fears that rates will spike and his interest payments will become unaffordable. A lender on a floating-rate bond worries that rates will collapse and future coupons will shrivel. **Interest rate ceilings and floors** — sometimes bundled as a collar — are embedded optionality that protects against these asymmetric risks. A cap limits how high the coupon can go; a floor prevents it from falling below a minimum. Both shift risk between lender and borrower and carry an option cost.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Rate Ceiling and Floor — key facts</div>

<img src="/svg/monetary.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Embedded options that bind the range of floating-rate coupons.</div>

|   |   |
|---|---|
| **What it is** | A cap sets a maximum coupon; a floor sets a minimum. Both are option-like features embedded in floating-rate bonds or loans |
| **Also called** | Rate cap, rate floor, interest rate collar (cap + floor together) |
| **Typical usage** | Adjustable-rate mortgages, floating-rate corporate bonds, bank loans, variable-rate securities |
| **Cost** | Caps and floors have embedded value and typically reduce the coupon the issuer pays or charges |
| **Risk implication** | Cap protects borrower; floor protects lender. A collar limits both upside and downside |
| **Valuation** | Priced using [option](/option/) models; value increases with [volatility](/historical-volatility/) and time to maturity |

</aside>

## How caps and floors work in practice

A floating-rate bond or loan typically resets every three or six months to [SOFR](/sofr/) (or another benchmark) plus a fixed spread. Without caps or floors, the coupon fluctuates freely with the benchmark. A cap — say, at 7% — means the coupon can never exceed 7%, no matter how high SOFR climbs. A floor — say, at 2% — means the coupon cannot fall below 2%, even if SOFR turns negative or near-zero. When a cap binds (SOFR + spread would exceed 7%), the bondholder receives the cap rate instead and forgoes the excess. When a floor binds (SOFR + spread would fall below 2%), the borrower pays the floor rate instead of a lower amount. In extreme markets, both can bind simultaneously within a bond, creating a tight collar.

## Why borrowers buy caps and lenders buy floors

An adjustable-rate mortgage borrower fears a surge in rates; paying a cap through lower initial coupons (or an explicit premium) is insurance against payment shock. If SOFR doubles, a 6% cap saves the borrower tens of thousands of dollars over the loan life. Conversely, a [mortgage-backed security](/mortgage-backed-security/) investor worries that if rates fall, the borrower will refinance and the bondholder will receive par earlier than expected, forced to reinvest in a lower-rate environment. A floor ensures minimum coupons and guards against extreme negative yields. Corporate treasurers often buy caps on floating-rate debt; pension funds may buy floors on floating-rate holdings to lock in yield floors.

## The collar trade: both cap and floor

A collar combines a cap purchase (to protect against rate rises) with a floor sale (to fund that purchase by accepting lower yields if rates fall). For instance, a borrower might buy a cap at 6% and sell a floor at 3%, effectively bounding the coupon between 3% and 6%. The floor sale offsets the cap premium, making the hedge affordable or free. Collars are extremely common in corporate debt and mortgages. They are attractive to risk-averse borrowers and lenders who want to be financially nimble but not exposed to extreme rate shocks. But they also create cliff effects: if rates fall to the floor, the borrower gains no further benefit and may feel locked in.

## Pricing and the volatility link

Caps and floors are long and short [options](/option/), respectively. Their value depends on the [strike price](/strike-price/) (the cap or floor level), time to maturity, the [volatility](/historical-volatility/) of the underlying benchmark, and the curve level. High [implied volatility](/implied-volatility/) makes caps expensive and floors valuable; borrowers pay a wider spread or lower coupon to fund expensive caps. In low-volatility environments (e.g., when central banks have anchored expectations), caps trade cheaply, making floating-rate protection less costly. This creates procyclical dynamics: caps are most affordable when volatility is low and rates seem stable; they are most expensive and hard to obtain when markets are volatile and protection is most needed.

## Mechanics: in-the-money, at-the-money, out-of-the-money

A cap is in-the-money when SOFR + spread exceeds the cap rate; the cap binds and the bondholder forgoes excess returns. It is out-of-the-money when rates are far below the cap; the option has zero immediate value but retains time value. At-the-money caps (where SOFR + spread is near the cap) are the most expensive because they have the highest gamma (sensitivity to rate moves). A borrower buying a cap far in-the-money (e.g., a 5% cap when SOFR is already 5%) is paying for insurance on a loss that has already occurred — inefficient hedging. Best practice is to buy caps slightly out-of-the-money to reduce cost while preserving protection against further moves.

## Embedded caps and floors in mortgages and loans

[Adjustable-rate mortgages](/fixed-rate-mortgage-personal/) often include periodic caps (how much the rate can rise at each reset) and lifetime caps (the maximum the rate can ever reach). These are embedded options that reduce the lender's [interest rate risk](/interest-rate-risk/) but transfer some of it to the borrower — if rates spike, the borrower bears the brunt because the rate is capped. Bank loans to corporations often include floors, particularly when the [prime rate](/limit-order/) or SOFR is low; the bank compensates for negative yields by selling a floor, capping its coupon downside. These embedded options are not priced separately; they are baked into the coupon and spread.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — The foundational contract on which caps and floors are built
- [Interest Rate Risk](/interest-rate-risk/) — The risk that caps and floors manage
- [SOFR](/sofr/) — The modern benchmark rate to which floating-rate instruments and caps are tied
- [Implied Volatility](/implied-volatility/) — A key driver of cap and floor pricing
- [Strike Price](/strike-price/) — The cap or floor level, analogous to an option strike
- [Interest Rate Pass-Through](/interest-rate-pass-through/) — How policy rate changes transmit to floating-rate coupons

### Wider context

- [Floating Rate Note](/interest-rate/) — The instrument commonly embedding caps and floors
- [Bond](/bond/) — The broader fixed-income asset class
- [Duration](/duration/) — How caps and floors affect bond duration
- [Yield-to-Maturity](/yield-to-maturity/) — How effective caps and floors are depends on what rate path materializes

</div>
