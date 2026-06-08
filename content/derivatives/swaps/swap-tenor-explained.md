---
title: "Swap Tenor Explained"
description: "What is swap tenor in derivatives? Learn how maturity dates affect swap pricing, duration, and hedge effectiveness across interest rate and currency swaps."
keywords:
  - swap tenor
  - tenor swap derivatives
  - swap maturity period
  - interest rate swap tenor
  - currency swap duration
  - swap duration and tenor
image: "/svg/derivatives.svg"
---

*In **swap** contracts, **tenor** refers to the time remaining until maturity—typically measured in months or years from trade date to final settlement. Tenor is the primary driver of [swap](/swap/) pricing, [duration](/duration/), and [hedge](/derivatives-hedging/) effectiveness, and it is standardized in the market to facilitate [liquidity](/liquidity-risk/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap Tenor — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The lifespan of a swap contract determines its economic value and how well it hedges long-term obligations.</div>

|   |   |
|---|---|
| **Definition** | Time from trade date to final cash settlement |
| **Common tenors** | 2, 3, 5, 7, 10, 20, 30 years |
| **Pricing dependency** | Longer tenors = higher [interest rate](/interest-rate/) risk premium |
| **Primary use** | Hedging long-term debt or currency exposure |
| **Liquidity** | Tightest spreads at 2, 5, and 10-year tenors |
| **Conversion to duration** | Approximate [duration](/duration/) is roughly ½ to ¾ of tenor |

</aside>

## Definition and timing

**Tenor** is the length of time a [swap](/swap/) contract lives from inception to final settlement. If you enter an [interest rate swap](/interest-rate-swap/) on January 1, 2026, with a 5-year tenor, the last cash exchange occurs on January 1, 2031.

Tenor is distinct from [expiration date](/expiration-date/), which refers to when an [option](/option/) or [futures contract](/futures-contract/) settles. For [swaps](/swap/), tenor is the native unit because [swaps](/swap/) are custom bilateral agreements settled through periodic cash flows—semiannual or quarterly—until maturity, not a single exercise or delivery event.

## Market-standard tenors

The most liquid and actively quoted tenors are:

- **Short end**: 1-year, 2-year, 3-year
- **Belly**: 5-year, 7-year
- **Long end**: 10-year, 20-year, 30-year

These maturities have the tightest [bid-ask spreads](/bid-ask-spread/) and deepest dealer order books. A bank quoting an [interest rate swap](/interest-rate-swap/) will price 2s, 5s, and 10s almost instantly; longer or odd-ball tenors (e.g., 4-year, 13-year) incur wider spreads and slower execution.

Tenor choice reflects hedging needs. A borrower with a 10-year fixed-rate [bond](/bond/) outstanding will typically hedge with a 10-year [interest rate swap](/interest-rate-swap/) to neutralize the duration mismatch.

## How tenor affects pricing

Tenor is the dominant factor in [swap](/swap/) [pricing](/price-discovery/). Longer tenors embed higher [interest rate](/interest-rate/) risk and require larger compensation.

Consider a 2-year [interest rate swap](/interest-rate-swap/) versus a 10-year [swap](/swap/). On the 2-year, rate movements of 25 basis points cause modest mark-to-market swings. On the 10-year, the same rate move can swing the [swap](/swap/) value by millions of dollars. To offset this risk, dealers quote wider [spreads](/bid-ask-spread/) and demand higher [fixed rates](/fixed-rate-mortgage-personal/) on longer tenors.

Mathematically, the present value of a [swap](/swap/) depends on discounting all future cash flows. A 10-year [swap](/swap/) has 40 quarterly cash flows; a 2-year [swap](/swap/) has 8. Longer time horizons mean greater sensitivity to [interest rate](/interest-rate/) assumptions and a larger risk premium embedded in the quoted rate.

## Tenor and duration

[Duration](/duration/) measures the price sensitivity of a bond or [swap](/swap/) to a 1% parallel shift in [interest rates](/interest-rate/). Tenor and [duration](/duration/) are related but not identical.

A bond or [swap](/swap/) with a duration of 7 years will fall roughly 7% in value if [interest rates](/interest-rate/) rise by 1%. For [swaps](/swap/), [duration](/duration/) approximates 40–75% of tenor, depending on the [swap](/swap/) type and [interest rate](/interest-rate/) level.

A 10-year [interest rate swap](/interest-rate-swap/) typically has a [duration](/duration/) near 7–8 years, not 10 years, because the cash flows are exchanged in small increments over time rather than as a lump sum at maturity. A 30-year [swap](/swap/) might have a [duration](/duration/) of 15–20 years.

This distinction matters for [hedging](/derivatives-hedging/). If you need to offset the [duration](/duration/) risk of a 10-year [bond](/bond/) portfolio, matching tenor (10-year [swap](/swap/)) is often correct, but confirming the actual [duration](/duration/) of the [swap](/swap/) avoids over- or under-hedging.

## Tenor in interest rate swaps

An [interest rate swap](/interest-rate-swap/) exchanges fixed [coupon payments](/coupon-payment/) for floating [payments](/coupon-payment/) (or vice versa) on a notional principal. The tenor determines how many cash flows are exchanged.

A 5-year swap, with semiannual payments, involves 10 fixed [coupon](/coupon-payment/) exchanges and 10 floating [rate](/interest-rate/) payments. The [fixed rate](/fixed-rate-mortgage-personal/) quoted at trade is locked in for all 5 years. A longer tenor implies more uncertainty about future [floating rates](/interest-rate/), so the [fixed rate](/fixed-rate-mortgage-personal/) must be higher to compensate the fixed-rate payer.

## Tenor in currency swaps

[Currency swaps](/swap/) involve exchanging principal and [interest](/interest-rate/) in one currency for principal and [interest](/interest-rate/) in another. Tenor again defines the settlement schedule and the [duration](/duration/) of the contract.

A 10-year [currency swap](/swap/) locks in a forward [exchange rate](/spot-exchange-rate/) for 10 years of [interest](/interest-rate/) payments. The longer the tenor, the greater the [currency risk](/currency-risk/) (wider expected [exchange rate](/spot-exchange-rate/) movements over the decade) and the higher the [swap](/swap/) [premium](/option-premium/).

[Currency swap](/swap/) tenors are often matched to [foreign exchange](/currency-volatility/) exposure. A U.S. company with a 7-year euro-denominated operating lease might use a 7-year [currency swap](/swap/) to hedge [exchange rate](/spot-exchange-rate/) moves.

## Term structure of swap rates

Just as [bonds](/bond/) have a [yield curve](/yield-curve/) (different yields at different maturities), [swap rates](/interest-rate/) vary by tenor. The **swap curve** plots [fixed rates](/fixed-rate-mortgage-personal/) for 2-year, 5-year, 10-year, and 30-year [interest rate swaps](/interest-rate-swap/) against tenor.

The swap curve is typically upward-sloping (longer tenors = higher rates) but can invert (recession signals). The shape of the swap curve influences relative value: a 5-year [swap](/swap/) might be expensive compared to the 10-year, creating opportunities for traders to buy the back end and sell the front end (a "curve trade").

## Why tenor matters for hedging

Suppose a company borrows $100 million on a floating-rate [basis](/basis/), repricing every 90 days, and plans to hold the debt for 7 years. To hedge, it enters a 7-year [interest rate swap](/interest-rate-swap/), paying fixed and receiving floating. The 7-year tenor matches the debt maturity, ensuring the [hedge](/derivatives-hedging/) lasts as long as the exposure.

If the company instead used a 3-year [swap](/swap/), it would be unhedged for the final 4 years. If it used a 10-year [swap](/swap/), it would overhang the exposure by 3 years. Matching tenor to the underlying risk ensures the [hedge](/derivatives-hedging/) is proportionate and avoids basis leakage.

## Non-standard and implied tenors

While 2s, 5s, and 10s dominate, tenors can be custom. A [swap](/swap/) might be 4 years 3 months, or 13 years. These **off-the-run** tenors trade with wider [spreads](/bid-ask-spread/) and lower [liquidity](/liquidity-risk/) because dealers must hedge them by trading more-liquid on-the-run tenors and managing the [curve](/yield-curve/) mismatch.

Some traders construct synthetic tenors by combining two standard [swaps](/swap/). For example, buying a 10-year [swap](/swap/) and selling a 5-year [swap](/swap/) creates a synthetic 5-to-10-year forward [swap](/swap/). This technique unlocks exposure at tenors where live dealer quotes are scarce.

## Tenor roll and portfolio management

As time passes, a [swap](/swap/)'s tenor shrinks. A 10-year [swap](/swap/) entered in 2026 becomes a 9-year [swap](/swap/) one year later. Portfolio managers occasionally choose to "roll" a [swap](/swap/)—close the existing position and enter a new one at the desired tenor to avoid unintended duration creep.

This rolling is most common when hedging an evergreen exposure. A company with a perpetual need for [interest rate](/interest-rate/) [hedging](/derivatives-hedging/) might maintain a rolling ladder of 2-, 5-, and 10-year [swaps](/swap/), allowing each to naturally expire while keeping the overall [hedge](/derivatives-hedging/) in place.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — the mechanics of bilateral derivatives contracts
- [Interest Rate Swap](/interest-rate-swap/) — most common tenor-dependent swap type
- [Currency Swap](/swap/) — cross-currency hedging and tenor selection
- [Duration](/duration/) — price sensitivity to rate changes, related to tenor
- [Derivatives Hedging](/derivatives-hedging/) — matching tenor to underlying exposure
- [Bid-Ask Spread](/bid-ask-spread/) — liquidity tightest at standard tenors
- [Yield Curve](/yield-curve/) — term structure of interest rates reflected in swap pricing

### Wider context

- [Interest Rate Risk](/interest-rate-risk/) — what tenor hedges protect against
- [Basis Risk](/basis/) — mismatches between hedge tenor and underlying exposure
- [Forward Contract](/forward-contract/) — fixed-price commitments over time
- [Counterparty Risk](/counterparty-risk/) — credit exposure in long-tenor swaps

</div>