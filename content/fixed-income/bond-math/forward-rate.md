---
title: "Forward Rate"
description: "The implied future interest rate embedded between two spot rates on the yield curve."
keywords:
  - forward rate
  - implied forward rate
  - yield curve
  - future interest rates
  - spot rate relationship
image: /svg/fixed-income.svg
---

*A **forward rate** is the expected or implied [interest rate](/interest-rate/) for borrowing or lending during a future period, calculated from today's [spot rates](/spot-rate/) for different maturities. If the 1-year [spot rate](/spot-rate/) is 2% and the 2-year [spot rate](/spot-rate/) is 3%, the 1-year rate starting one year from now (the "1×2 forward rate") must be approximately 4% for the rates to be consistent with no-arbitrage principles.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forward Rate — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income markets." />

<div class="wiki-infobox-caption">The hidden future rate locked in by the gap between two spot rates today.</div>

|   |   |
|---|---|
| **What it is** | The implied future short rate between two [spot rates](/spot-rate/) on the curve |
| **Also called** | Implied forward rate, forward yield |
| **Notation** | ₁f₂ (1-year forward 1-year from now); f(1,3) (rate from year 1 to 3) |
| **Derivation** | Backed out from spot rates using no-arbitrage logic |
| **Primary use** | Assessing market expectations; hedging future borrowing or lending |
| **Sign** | Higher spot rates in the future imply higher forward rates embedded today |

</aside>

## The no-arbitrage logic

The forward rate is not an independent market quote—it is a derived number that ensures consistency between spot rates at different maturities. The principle is simple: two strategies for investing money over two years should give identical returns if there is no arbitrage.

**Strategy A:** Invest for 2 years at the 2-year [spot rate](/spot-rate/).

**Strategy B:** Invest for 1 year at the 1-year [spot rate](/spot-rate/), then reinvest the proceeds for another year at the 1-year rate starting in one year (the "1×2 forward rate").

If both strategies offer the same total return, there is no opportunity for a risk-free profit. This constraint uniquely determines the forward rate.

## Calculating the 1×2 forward rate

Suppose:
- 1-year [spot rate](/spot-rate/): 2.0%
- 2-year [spot rate](/spot-rate/): 3.0%

To find the forward rate for year 2 (the 1×2 rate), set the returns equal:

```
(1 + s₁) × (1 + ₁f₂) = (1 + s₂)²
(1 + 0.02) × (1 + ₁f₂) = (1 + 0.03)²
1.02 × (1 + ₁f₂) = 1.0609
1 + ₁f₂ = 1.0609 / 1.02 = 1.04009
₁f₂ ≈ 4.0%
```

The forward rate for year 2 is approximately 4.0%. This is the rate that, when combined with the 2% first-year return, produces the same overall 2-year yield as investing at 3% annually.

## The forward rate curve

Just as [spot rates](/spot-rate/) at many maturities form the [yield curve](/yield-curve/), forward rates at many periods form the **forward curve**. A portfolio manager or trader can ask: What is the 3-year rate starting 5 years from now? The answer comes from the forward curve, calculated from spots.

On an upward-sloping [yield curve](/yield-curve/), forward rates typically exceed the spot rates at the beginning of each period. If a curve is flat or inverted, forward rates may be lower. This is because a rising curve embeds the market's expectation (or risk premium) that short rates will be higher in the future.

## Forward rates and market expectations

Forward rates are sometimes interpreted as the market's forecast of future short rates. If the 1×2 forward rate is 4%, one argument goes, the market expects the 1-year rate to be 4% one year from now.

This interpretation is popular but incomplete. Forward rates reflect two things: expected future short rates *and* a risk premium for being locked into a future rate. Because longer-maturity bonds carry more [interest-rate risk](/interest-rate-risk/), investors demand additional yield to compensate, driving forward rates higher than expectations alone would suggest.

Thus, forward rates are best thought of as **market-implied rates**, not pure forecasts. A steep forward curve could signal either high growth expectations or a large risk premium—or both. Professional analysts distinguish between them using other tools like survey data on interest-rate expectations.

## Forward rates in hedging and contract pricing

Forward rates are critical in structuring financial contracts. A company needing to borrow money in one year can **lock in the rate today** using a forward-rate agreement (FRA) or by buying and selling bonds in a matched way. The rate in that contract is derived from the forward curve.

Similarly, traders use forward rates to price longer-dated securities and to hedge. If a fund holds a 5-year bond and wants to protect itself against falling prices, it may lock in a forward rate at which it will reinvest coupons—this protects its overall 5-year return.

## Comparing spot, forward, and interpolated yields

[Spot rates](/spot-rate/) are the zero-coupon yields at each maturity—the foundation of the curve. [Forward rates](/forward-rate/) are derived future short rates, calculated from pairs of spot rates using no-arbitrage. [Interpolated yields](/interpolated-yield/) are synthetic points *between* two observed spot rates, created by assuming a smooth curve shape.

All three are tools: analysts use [interpolated yields](/interpolated-yield/) for quick benchmarking, [spot rates](/spot-rate/) for precise discounting, and forward rates to understand what future rates are embedded in today's prices and to price forward contracts.

## See also

<div class="wiki-seealso">

### Closely related

- [Spot Rate](/spot-rate/) — the zero-coupon yield at a specific maturity
- [Interpolated Yield](/interpolated-yield/) — a synthetic yield for an odd maturity
- [Bootstrapping the Yield Curve](/bootstrapping-yield-curve/) — extracting spot rates from coupon bonds
- [Yield Curve](/yield-curve/) — the complete map of yields across all maturities
- [Interest Rate](/interest-rate/) — the fundamental economic variable
- [Yield-to-Maturity](/yield-to-maturity/) — a bond's single internal rate of return

### Wider context

- [Bond](/bond/) — the instrument whose rates embed forward expectations
- [Treasury Bond](/treasury-bond/) — the benchmark for deriving forward curves
- [Duration](/duration/) — a bond's sensitivity to moves in spot and forward rates
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — using rates to value future cash
- [Interest Rate Risk](/interest-rate-risk/) — why forward rates carry a risk premium

</div>
