---
title: "Forward Rate vs Spot Rate: Key Differences Explained"
description: "The forward rate vs spot rate difference: spot rates are today's yields for immediate delivery, while forward rates lock in yields for future periods."
keywords:
  - forward rate vs spot rate
  - spot rate bond
  - forward rate bond
  - yield curve
  - bond pricing
---

*The **forward rate vs spot rate difference** is fundamental to fixed-income pricing: the spot rate is the yield today for cash delivered now, while the forward rate is the yield implied by the market for a bond purchased at a future date. A forward rate is not a price the market announces—it's calculated from the difference between two spot rates, encoding what investors expect to earn in that future period.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Spot and Forward Rates — Key Facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two ways to measure bond yields across time.</div>

|   |   |
|---|---|
| **Spot rate** | Yield today for cash settlement now |
| **Forward rate** | Yield locked in today for a future period |
| **Relationship** | Forward rates are *implied* by two spot rates |
| **Use** | Forward rates show what the market prices in for future lending conditions |
| **Duration** | Spot rates apply to the full maturity; forward rates cover a single future interval |

</aside>

## Spot Rates: The Baseline

A spot rate is straightforward: it's the yield you earn by buying a [bond](/bond/) and holding it to maturity, starting today. If you buy a 2-year Treasury at 4.5%, that 4.5% is the spot rate for 2-year money. The settlement happens within a day or two—the bond is delivered, and the clock starts.

Every maturity has its own spot rate. The 3-year spot rate may be 4.2%, the 5-year spot rate 4.0%, and so on. These spot rates are observable prices in the market: they're the yields you can actually trade today. Plot them on a graph by maturity, and you get the [yield curve](/yield-curve/)—one of the most important charts in finance.

Spot rates are real; forward rates are inferred.

## How Forward Rates Are Derived

A forward rate emerges from the structure of two spot rates. Suppose the 2-year spot rate is 4.5% and the 3-year spot rate is 4.2%. What does the market imply for the yield on a 1-year bond *purchased 2 years from now*?

Use the no-arbitrage principle: an investor should earn the same total return whether they buy a 3-year bond today or buy a 2-year bond today and reinvest the proceeds into a 1-year bond in 2 years. 

Mathematically:
```
(1 + s₃)³ = (1 + s₂)² × (1 + f₂₋₃)
```

Where s₃ is the 3-year spot rate, s₂ is the 2-year spot rate, and f₂₋₃ is the 1-year forward rate starting in year 2. Solve for f₂₋₃, and you have the implied forward rate.

With our example:
- (1.042)³ = (1.045)² × (1 + f₂₋₃)
- 1.1317 = 1.0920 × (1 + f₂₋₃)
- 1 + f₂₋₃ = 1.0364
- f₂₋₃ ≈ 3.64%

The 1-year forward rate 2 years out is roughly 3.64%. This is lower than both the 2-year and 3-year spot rates, which tells us the market expects rates to fall.

## Why the Forward Rate Matters

Forward rates are not predictions. They are market prices embedded in yield curves—and they serve several roles:

**Pricing complex securities.** A [mortgage-backed security](/mortgage-backed-security/) or any [bond](/bond/) with embedded options requires discounting each cash flow by the appropriate forward rate, not a single spot rate. Forward rates let you value each period's cash flow at the rate the market has agreed upon.

**Spotting rate expectations.** If forward rates are much lower than current spot rates, the market is pricing in falling interest rates. If forward rates rise, the opposite is true. Traders watch forward rate curves as barometers of macro sentiment.

**Managing [reinvestment risk](/reinvestment-risk/).** An investor who buys a 5-year bond knows the yield to maturity assumes they can reinvest coupons at the implied forward rates baked into the bond price. If forward rates fall, that assumption becomes optimistic.

**Bond math and duration.** [Duration](/duration/) calculations lean on forward rates to measure how a bond's value responds to parallel shifts in the curve.

## Spot Rates and Forward Rates Across the Curve

A upward-sloping [yield curve](/yield-curve/) usually means forward rates are higher than current short-term spot rates. In other words, the market expects rates to rise as you move further out. A downward-sloping curve means forward rates are *lower* than short rates—a sign the market expects rate cuts.

Consider a simple curve:
- 1-year spot: 5.0%
- 2-year spot: 4.8%
- 3-year spot: 4.6%

The forward rates implicit in this curve are:
- 1-year forward rate starting in year 1 ≈ 4.6% (derived from the 1-year and 2-year spots)
- 1-year forward rate starting in year 2 ≈ 4.2% (derived from the 2-year and 3-year spots)

The curve slopes down, and so do the forward rates—the market is pricing in declining yields ahead.

## The Relationship to Spot Rates

Every spot rate is itself an average (technically, a geometric average) of forward rates. The 5-year spot rate is equivalent to locking in a series of 1-year forward rates—year 1 at the 1-year spot, then years 2–5 at the implied forward rates. This is why a single move in spot rates can reshape the entire forward curve, and why traders distinguish between parallel shifts (all rates up by the same amount) and [curve steepening](/yield-curve/) (the shape of forward rates changing).

Understanding the interplay between spot and forward rates is essential for anyone pricing bonds or managing interest-rate risk. Spot rates are the tangible prices you trade today; forward rates are the logical consequences of no-arbitrage pricing and a window into what the market expects next.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield curve](/yield-curve/) — How spot rates across maturities plot the market's term structure
- [Duration](/duration/) — How forward rates feed into measuring bond price sensitivity
- [Reinvestment risk](/reinvestment-risk/) — Why forward rates matter when bonds mature and coupons arrive
- [Bond](/bond/) — The instrument whose spot and forward yields we're analyzing
- [Discount rate](/discount-rate/) — The broader concept of discounting future cash flows

### Wider context

- [Interest rate](/interest-rate/) — The economic driver of spot and forward rate movements
- [Yield to maturity](/yield-to-maturity/) — Another key bond metric that embeds forward rate assumptions
- [Fixed-rate mortgage](/fixed-rate-mortgage-personal/) — A consumer application where forward rates affect pricing

</div>
