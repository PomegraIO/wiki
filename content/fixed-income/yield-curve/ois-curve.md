---
title: "OIS Curve"
description: "The overnight-indexed swap curve, which reflects near-risk-free rate expectations and is the foundation of modern fixed-income valuation."
keywords:
  - overnight-indexed swaps
  - OIS rates
  - risk-free curve
  - SOFR curve
  - yield curve construction
  - interest rate swaps
image: "/svg/fixed-income.svg"
---

*The OIS (overnight-indexed swap) curve reflects the expected path of the [central bank](/central-bank/) policy rate across maturities and has replaced older rate benchmarks as the standard risk-free curve. It is built from the prices of swaps that exchange a fixed rate for compounded daily overnight rates, and it dominates fixed-income valuation today.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">OIS Curve — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">The modern risk-free benchmark: what markets believe the overnight rate will be, every day for years ahead.</div>

|   |   |
|---|---|
| **What it is** | Yield curve built from overnight-indexed swap rates |
| **Also called** | Risk-free curve, SOFR curve (U.S.), EONIA curve (EUR) |
| **Current benchmark** | [SOFR](/sofr/) in the U.S.; SONIA in the UK; ESTR in the eurozone |
| **What it prices** | Daily compounded overnight borrowing costs |
| **Key users** | Banks, derivatives dealers, central banks |
| **Replaces** | LIBOR curve (phased out by 2023) |
| **Why it matters** | The foundation for [discounting](/discount-rate/) all fixed-income cash flows |

</aside>

## The shift from LIBOR to risk-free rates

For decades, the [LIBOR](/libor/) curve was the universal discount curve. Banks published [LIBOR](/libor/) rates at which they claimed to lend to each other, and traders used these rates to value [bonds](/bond/), [swaps](/interest-rate/), and [derivatives](/option/). But LIBOR was not truly risk-free—it embedded bank credit risk, and after the 2008 financial crisis, the rate became unreliable as lending froze.

Starting around 2012, regulators and markets moved toward risk-free rates (RFRs): the actual rates at which banks transact overnight. In the U.S., the alternative was [SOFR](/sofr/) (Secured Overnight Financing Rate), backed by actual repurchase agreement trades. In sterling, SONIA (Sterling Overnight Index Average). In euros, ESTR (Euro Short-Term Rate). These rates are backward-looking averages of real transactions, not surveys or estimates.

The OIS curve is built by stripping these overnight rates forward. It answers the question: what overnight rate does the market expect over the next 2 years? 5 years? 10 years?

## How overnight-indexed swaps work

An overnight-indexed swap (OIS) is an [interest rate swap](/interest-rate/) with a special structure. One counterparty pays a *fixed* rate. The other pays the overnight reference rate, compounded daily. At the end (say, one year), they settle:

Fixed payment = Fixed rate × Notional

Floating payment = Notional × [(1 + r₁) × (1 + r₂) × ... × (1 + r₃₆₅) − 1]

where r₁, r₂, etc. are the daily overnight rates.

The overnight rate adjusts every day, but the fixed rate is locked in at the swap's inception. If the OIS rate quoted in the market is 3.5%, both parties agree that the fixed side is worth 3.5% and the floating side (expected average overnight rate) is also worth 3.5%.

The brilliance is that overnight rates have almost no counterparty or term risk. A bank can borrow unsecured overnight at nearly the central bank rate. So the OIS rate is a proxy for what the [central bank](/central-bank/) policy rate will average over the life of the swap.

## Building the curve via bootstrapping

An OIS curve is [bootstrapped](/bootstrap-yield-curve/) like any other. The shortest instruments (overnight, 1-week, 1-month OIS swaps) are observable. Longer maturities (1-year, 5-year, 10-year OIS) are quoted in dealer markets.

From these, traders extract the [spot rate](/discount-rate/) (zero-coupon discount factor) at each maturity using [bootstrapping](/bootstrap-yield-curve/). The mathematics is identical to a Treasury [bootstrap](/bootstrap-yield-curve/), except the cash flows are the daily compounded overnight rate instead of regular coupon payments.

Once you have the spot curve, you can infer forward rates. If 1-year OIS is 3% and 2-year OIS is 3.5%, the market is pricing in a roughly 4% overnight rate in year 2. Traders use these forward rates to bet on [monetary policy](/monetary-policy/) and [Federal Reserve](/federal-reserve/) action.

## Why OIS has replaced LIBOR

The OIS curve dominates because it has three advantages over LIBOR:

First, it is risk-free. LIBOR embedded bank credit risk, so in stress (like 2008), the LIBOR curve became distorted. OIS is backed by actual overnight lending rates, often collateralized, so it stays anchored to the central bank's policy rate.

Second, it is verifiable. LIBOR was a daily poll of banks; traders could manipulate their submissions. OIS rates are computed from millions of real trades in the repo market, so they cannot be faked.

Third, it aligns incentives. Since 2012, over-the-counter derivatives (swaps, options, forwards) have been discounted at OIS, not LIBOR. This is the industry standard, set by ISDA (International Swaps and Derivatives Association) conventions. So the OIS curve is the curve that actually clears the market.

## The flatten spread: OIS-to-SOFR basis

After SOFR replaced LIBOR in 2023, a new basis emerged: the spread between OIS (overnight-indexed swaps) and SOFR cash rates. In normal conditions, this spread is tight (a few basis points), reflecting the cost of funding a SOFR position. In stress, the spread widens.

Some traders use a hybrid: OIS discounting for near-term cash flows (where OIS is tight) and SOFR fixing rates further out. The choice is a technical detail, but it shows that even within the "risk-free" framework, multiple curves coexist.

## Forward rates from OIS: reading policy expectations

The OIS curve is read like a crystal ball for monetary policy. If the 1-year OIS rate is 3.5% and the 2-year OIS is 3.2%, the market is pricing in lower rates in the second year. If both are flat at 3%, the market sees no change coming.

Central banks publish their own forecasts; OIS forwards reflect what the market believes those forecasts will become. During policy shifts—a rate cut cycle, a surprise inflation spike—OIS forwards move sharply. Traders watching real-time OIS moves often know about monetary policy shifts before the central bank announces them.

## Practical use: discounting derivatives and bonds

Every [bond](/bond/) or [derivative](/option/) trader discounts cash flows using the OIS curve. A [corporate bond](/corporate-bond/) issued at 5% is valued as:

Bond Price = ∑ [Coupon / (1 + OIS_t)] + [Par / (1 + OIS_T)]

where OIS_t is the spot rate from the OIS curve at maturity t. The company's own credit risk is captured in a separate [credit spread](/credit-spread/), not in the discount rate. This clean separation—risk-free curves separate from credit—is modern best practice.

The OIS curve is so central to fixed-income that when it shifts abruptly (e.g., a [Federal Reserve](/federal-reserve/) surprise announcement), the entire market reprices in minutes.

## See also

<div class="wiki-seealso">

### Closely related

- [SOFR](/sofr/) — the overnight rate underlying U.S. OIS curves
- [Yield curve](/yield-curve/) — the general structure that OIS represents for risk-free rates
- [Bootstrap yield curve](/bootstrap-yield-curve/) — the method used to construct OIS curves
- [Interest rate swap](/interest-rate/) — the instrument whose prices build the OIS curve
- [Discount rate](/discount-rate/) — how OIS rates are applied in valuation
- [Bond pricing](/bond/) — practical application of the OIS curve

### Wider context

- [Federal Reserve](/federal-reserve/) — sets the policy rate that OIS forwards embed
- [Monetary policy](/monetary-policy/) — the force driving OIS curve shifts
- [Central bank](/central-bank/) — the issuer of overnight rates that OIS aggregates
- [Credit spread](/credit-spread/) — the extra yield above OIS for risky borrowers
- [Derivatives](/option/) — major users of OIS discounting in valuation
- [Volatility smile](/volatility-smile/) — interest rate volatility structure, visible in OIS moves

</div>
