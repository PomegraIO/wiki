---
title: "Interest Rate Sensitivity of Bonds Explained"
description: "Interest rate sensitivity of bonds quantifies why bond prices fall when rates rise. Duration is the key metric: a 10-year bond with 8-year duration falls roughly 8% if rates rise 1%."
keywords:
  - interest rate sensitivity bonds
  - bond price interest rate relationship
  - bond duration
  - why bond prices fall
  - interest rate risk bonds
image: /svg/monetary.svg
---

*The **interest rate sensitivity of bonds** measures how much a bond's price changes when interest rates move. It is quantified by [duration](/duration/), which tells you that for every 1% rise in yields, a bond's price falls roughly (duration %) × 1%. A 5-year bond might fall 4.5% if rates rise 1%; a 20-year bond might fall 18% under the same move.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Rate Sensitivity — key facts</div>

<img src="/svg/monetary.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Longer bonds hurt more when rates rise; shorter bonds bounce back faster.</div>

|   |   |
|---|---|
| **Duration** | Average time to receive cash flows (in years); approximates percentage price drop per 1% rate rise |
| **Key insight** | A bond's price and yield move inversely; higher rates = lower prices |
| **2-year bond duration** | ~1.9 years; ~1.9% price change per 1% yield move |
| **10-year bond duration** | ~8–9 years; ~8–9% price change per 1% yield move |
| **30-year bond duration** | ~15–20 years; ~15–20% price change per 1% yield move |
| **Reinvestment risk** | Higher rates also benefit future cash flow reinvestment |

</aside>

## Why bond prices fall when rates rise

A bond is a fixed-income contract: you lend $1,000 to an issuer, they pay you a coupon each year (say, 3%), and return your principal at maturity (say, in 10 years).

If you hold the bond to maturity, the interest rate environment matters little. You get your 3% coupon and your $1,000 back, regardless of what happens to rates. But if you need to sell before maturity—whether to raise cash, rebalance a portfolio, or because a better opportunity appears—the bond's market price becomes crucial.

The price inversely tracks the yield. When new market interest rates climb above the coupon, the bond becomes less attractive. A newly issued 10-year bond offers 5%. Your bond, locked at 3%, is worth less. To sell it, you must discount the price so that the buyer's *yield to maturity* equals the market rate of 5%. This requires selling at a loss. Conversely, if market rates fall to 2%, your 3% bond is premium; you can sell above par because future buyers cannot get 3% elsewhere.

This inverse relationship is mechanical, not subjective. The bond still pays 3% annually and returns principal at maturity. The price change is simply what restores equilibrium: lower price → higher yield to the new buyer.

## Duration: the sensitivity metric

Not all bonds are equally sensitive. A short-term bond recovers faster: a 1-year bond that matures in a year is barely affected by a 1% rate rise, because the owner will receive par value in twelve months regardless. A long-term bond, with cash flows spread over decades, experiences large price swings.

**Duration** is the weighted average time until you receive the bond's cash flows, measured in years. It also serves as an elasticity rule: a bond's percentage price change ≈ (−Duration) × (change in yield, in decimal).

Example:
- A 5-year bond with a 3% coupon has a duration of roughly 4.4 years.
- If yields rise from 3% to 4% (a +1% move), the bond's price falls approximately 4.4%.
- If you bought at $1,000, it now trades near $956.

## Worked example: comparing maturities

Suppose three bonds, each yielding 4%, all issued by the same borrower:

| Bond | Maturity | Duration | Price if yields rise to 5% |
|---|---|---|---|
| 2-year | 2 years | 1.9 years | $980.20 (−1.98% change) |
| 10-year | 10 years | 8.7 years | $913 (−8.7% change) |
| 30-year | 30 years | 17.1 years | $745 (−17.1% change) |

All three were issued at par ($1,000) when the yield was 4%. When market yields jump to 5%, each bond's price adjusts so that new buyers earn the 5% yield to maturity.

The 2-year bond barely budges: even at a slight discount, it matures in just two years at par, so most of the cash flow is insensitive to the rate move. The 30-year bond plummets: most of its cash flows lie a decade or more in the future; a higher discount rate crushes their present value.

## The role of coupon

Bonds with higher coupons have *lower* duration, because you get more cash early. A 10-year bond paying 6% has a shorter duration than a 10-year bond paying 2%. The 6% bondholder receives more annual cash and can reinvest it sooner, shortening the weighted average life.

Zero-coupon bonds—which pay no coupons, only principal at maturity—have the longest duration for a given maturity: a 10-year zero has a duration of almost exactly 10 years.

## Rate environment and reinvestment risk

Rising interest rates do carry one silver lining for bondholders: reinvestment risk. When you receive a coupon payment, you must reinvest it. If rates fall, reinvestment income drops. If rates rise, reinvestment income rises. A bondholder with a 30-year bond receiving annual coupons actually benefits from higher rates if they reinvest those coupons at higher yields. This offsets some (but not all) of the price loss from longer duration.

A bond-fund investor does not enjoy this offset: the fund marks bonds to market constantly and does not hold most bonds to maturity. For traders and portfolio managers, interest rate sensitivity (as measured by duration) is the dominant risk.

## Duration vs. maturity

Maturity and duration are related but not identical. A 10-year bond has a maturity of 10 years but a duration shorter than 10 years (typically 7–9 years, depending on its coupon). Duration is the economically relevant measure for price sensitivity; maturity is simply the date of final payment.

This distinction matters for bond traders and [bond ETF](/bond-etf/) investors. Two bonds may have the same maturity but very different durations if one has a high coupon and the other a low coupon. A corporate bond and a Treasury note with the same maturity may also have different durations if their coupon rates differ.

## Modified duration and convexity

Practitioners often use **modified duration**, which adjusts duration for the yield level, to estimate price changes with greater precision. For large yield moves, **convexity**—a second-order sensitivity—becomes important. Most bonds exhibit positive convexity: when rates drop, their price rises *more* than duration would suggest (good news for buyers), and when rates rise, their price falls *less* than duration predicts (a small mercy for sellers).

Some callable bonds have negative convexity: if rates fall sharply, the issuer may call the bond back (prepay early), capping your upside. This is why [callable bonds](/callable-bond/) offer higher coupons than otherwise identical straight bonds.

## Practical implications

Interest rate sensitivity matters most in a rising-rate environment. If you are holding a [bond](/bond/) or a [bond ETF](/bond-etf/) and the central bank is tightening (raising policy rates), expect prices to fall in the near term. Duration tells you approximately how much. A high-duration [index fund](/index-fund/) of long-term Treasuries can fall 15–20% in a single year of rapid rate increases; a short-duration or [money market fund](/money-market-fund/) barely moves.

Conversely, in a falling-rate environment, long-duration bonds outperform. This is why portfolio managers often rotate between bonds of different durations depending on their outlook for interest rates and the [yield curve](/yield-curve/).

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — The precise mathematical measure of a bond's interest rate sensitivity.
- [Bond](/bond/) — What bonds are and how they are priced.
- [Bond ETF](/bond-etf/) — Funds of bonds and how their prices fluctuate with rates.
- [Policy Rate vs Market Interest Rate](/policy-rate-vs-market-interest-rate/) — How central bank rate moves feed into bond yields.
- [Interest Rate Lag in Monetary Policy](/interest-rate-lag-monetary-policy/) — Why rate changes take months to fully affect bond markets.
- [Callable Bond](/callable-bond/) — A bond type with altered interest rate sensitivity due to embedded options.

### Wider context

- [Interest Rate](/interest-rate/) — The foundation for all yield calculations.
- [Federal Funds Rate](/federal-funds-rate/) — The central bank policy rate that drives long-term bond yields.
- [Yield to Maturity](/yield-to-maturity/) — The return a bond investor receives if held to maturity.
- [Corporate Bond](/corporate-bond/) — Bonds issued by companies; higher duration and yield than Treasuries.
- [Treasury Bond](/treasury-bond/) — US government debt; the baseline for bond pricing.

</div>
