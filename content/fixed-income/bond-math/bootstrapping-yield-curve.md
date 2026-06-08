---
title: "Bootstrapping the Yield Curve"
description: "Deriving zero-coupon spot rates sequentially from coupon-bond prices using no-arbitrage logic."
keywords:
  - bootstrapping yield curve
  - spot rate extraction
  - yield curve construction
  - zero-coupon rates
  - no-arbitrage
image: /svg/fixed-income.svg
---

*Bootstrapping is the process of systematically extracting zero-coupon [spot rates](/spot-rate/) from the observed prices of coupon-bearing [bonds](/bond/). By using a no-arbitrage framework and solving sequentially from short to long maturity, analysts derive the true discount curve—the set of [spot rates](/spot-rate/) that accurately prices every cash flow in the fixed-income market.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bootstrapping the Yield Curve — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income markets." />

<div class="wiki-infobox-caption">Stripping coupon bonds down to their zero-coupon building blocks.</div>

|   |   |
|---|---|
| **What it is** | Sequential extraction of [spot rates](/spot-rate/) from coupon bond market prices |
| **Also called** | Stripping, spot curve construction, zero-coupon curve derivation |
| **Core principle** | No-arbitrage: one bond's price must equal the sum of its discounted cash flows |
| **Starting point** | Short-maturity bonds with known or near-known [spot rates](/spot-rate/) |
| **Method** | Solve backwards through the bond price equation, removing one known rate per step |
| **Output** | Complete [spot rate](/spot-rate/) curve (one rate per maturity) |
| **Frequency** | Updated daily as bond prices change; can shift basis points per session |

</aside>

## Why bootstrapping is necessary

[Bonds](/bond/) with coupons do not directly reveal their zero-coupon discount rates. A 5-year [bond](/bond/) paying semi-annual coupons has its price determined by five distinct cash flows (four coupon payments plus principal), each of which should be discounted at the rate appropriate to its maturity. But market conventions quote a single [yield-to-maturity](/yield-to-maturity/) that hides this underlying structure.

Bootstrapping reverses this opacity. It recovers the individual [spot rates](/spot-rate/) that, when applied to each cash flow, exactly reproduce the bond's market price. These [spot rates](/spot-rate/) can then be used to price other securities, hedge portfolios, and measure interest-rate risk.

## The sequential logic

Bootstrapping works because short-maturity bonds are relatively simple. A 1-year [bond](/bond/) with semi-annual coupons has only two cash flows: a coupon in 6 months and a coupon plus principal in 1 year. If we assume the 6-month [spot rate](/spot-rate/) is known or can be approximated from 6-month instrument prices, we can solve for the 1-year [spot rate](/spot-rate/) directly.

Once the 1-year [spot rate](/spot-rate/) is locked in, a 1.5-year or 2-year [bond](/bond/) has one fewer unknown: we can discount its 6-month and 1-year cash flows using known rates, then solve for the next [spot rate](/spot-rate/). This process repeats up the curve.

**The key principle:** At each step, only one [spot rate](/spot-rate/) is unknown. Solving the bond-pricing equation yields that unknown rate; then you move to the next maturity.

## A worked example

Suppose we have a 2-year [bond](/bond/) with 4% annual coupons (paid once per year), a face value of 100, and a market price of 101.92. We already know the 1-year [spot rate](/spot-rate/) is 2%.

The cash flows are:
- Year 1: $4 coupon
- Year 2: $4 coupon + $100 principal = $104

The bond price equation is:

```
Price = 4 / (1 + s₁) + 104 / (1 + s₂)²
101.92 = 4 / 1.02 + 104 / (1 + s₂)²
101.92 = 3.92 + 104 / (1 + s₂)²
98 = 104 / (1 + s₂)²
(1 + s₂)² = 104 / 98 = 1.0612
1 + s₂ = 1.0304
s₂ ≈ 3.04%
```

The 2-year [spot rate](/spot-rate/) is 3.04%. This rate, when applied to the year-2 cash flow, combines with the 2% rate on the year-1 coupon to price the [bond](/bond/) correctly.

## Handling coupons and market complications

Most [bonds](/bond/) pay semi-annual coupons, not annual ones, so bootstrap curves often proceed in 6-month intervals. The principle remains identical: discount known cash flows at known rates, solve for the unknown [spot rate](/spot-rate/), then advance.

Market frictions complicate real-world bootstrapping. Treasury [bonds](/bond/) of a given maturity may not have perfectly clean prices—some may be special repo [collateral](/bond/), others may carry accrued interest or have fallen temporarily out of favour. Professional traders and risk systems build multiple bootstrap curves (one from yields, another from bid-ask midpoints, another from traded volumes) and average or weight them.

Off-the-run [bonds](/bond/) (older issues) may trade less frequently, introducing gaps. Analysts fill these gaps using [interpolation](/interpolated-yield/) or by selecting the most liquid set of [bonds](/bond/) for bootstrapping.

## From bonds to [spot rates](/spot-rate/) to any price

Once a bootstrap curve is complete, it becomes the standard discounting tool. A corporate [bond](/bond/) with cash flows in year 2 and year 5 is priced using the 2-year and 5-year [spot rates](/spot-rate/) extracted from Treasuries. A mortgage-backed security with complex prepayment cash flows is discounted using the full spot curve. A swap's value is calculated by discounting each leg at the appropriate spot rate.

This is why bootstrap curves are constantly refreshed (often multiple times per day in high-speed trading). Each basis-point move in a Treasury's price shifts the extracted [spot rates](/spot-rate/) slightly, which in turn reprices the entire market's worth of bonds and derivatives.

## Bootstrapping versus [interpolation](/interpolated-yield/) versus [forward rates](/forward-rate/)

**Bootstrapping** extracts the true zero-coupon rate at each maturity by solving through coupon-bond prices. It is precise but data-intensive and requires an assumption about the curve shape between data points.

[**Interpolation**](/interpolated-yield/) simply connects two observed [spot rates](/spot-rate/) with a straight line (or smooth curve) to estimate rates at intermediate maturities. It is quick and useful for benchmarking but does not generate new information.

[**Forward rates**](/forward-rate/) are implied future short rates, calculated from pairs of [spot rates](/spot-rate/) using no-arbitrage. They embed market expectations and risk premia but are not directly observed.

All three are complementary: bootstrapping builds the [spot curve](/spot-rate/), [interpolation](/interpolated-yield/) fills in between, and [forward rates](/forward-rate/) reveal what future rates are locked in.

## Limitations and assumptions

Bootstrapping assumes no-arbitrage and perfect markets—that is, no transaction costs, no bid-ask spreads, and perfect divisibility of [bonds](/bond/). Real markets have all of these frictions.

Bootstrapping also assumes the [bond](/bond/) prices used are clean and representative. If a particular [bond](/bond/) is distressed, illiquid, or special in repo, its price may not reflect the true [spot rate](/spot-rate/), polluting the entire curve downstream.

For these reasons, professional risk systems typically build a bootstrap curve and then smooth it—fitting a parametric curve to the extracted [spot rates](/spot-rate/) and re-deriving a fitted curve that is more stable and less prone to individual [bond](/bond/) pricing anomalies.

## See also

<div class="wiki-seealso">

### Closely related

- [Spot Rate](/spot-rate/) — the zero-coupon yield at each maturity, the output of bootstrapping
- [Forward Rate](/forward-rate/) — implied future rates derived from [spot rates](/spot-rate/)
- [Interpolated Yield](/interpolated-yield/) — estimating a rate between two [spot rates](/spot-rate/)
- [Yield Curve](/yield-curve/) — the complete map of yields; bootstrapping builds this
- [Yield-to-Maturity](/yield-to-maturity/) — a [bond](/bond/)'s single internal rate; bootstrapping breaks it into components
- [Bond](/bond/) — the coupon-bearing instrument used as bootstrap input
- [Coupon Payment](/coupon-payment/) — the cash flows being discounted

### Wider context

- [Treasury Bond](/treasury-bond/) — the benchmark [bonds](/bond/) typically used for bootstrapping
- [Discount Rate](/discount-rate/) — the fundamental concept behind spot rates
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the broader principle of valuing future cash
- [Duration](/duration/) — interest-rate sensitivity, derived using the spot curve
- [Interest Rate Risk](/interest-rate-risk/) — the risk that spot rates will change

</div>
