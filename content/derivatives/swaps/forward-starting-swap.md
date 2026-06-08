---
title: "Forward-Starting Swap"
description: "An interest-rate swap whose effective date begins in the future, allowing counterparties to lock in rates ahead of a known financing need."
keywords:
  - forward starting swap
  - deferred swap
  - interest rate swap
  - rate lock
  - swap pricing
  - financing hedge
image: "/svg/derivatives.svg"
---

*A **forward-starting swap** (or deferred swap) is an interest-rate [swap](/bond/) whose accrual period commences at a future date rather than immediately. Instead of exchanging fixed and floating [interest](/interest-rate/) payments today, the counterparties agree now on the fixed rate and floating index they will use starting six months, one year, or two years from now. This lets a company lock in a borrowing rate well before it actually needs to access funds.*

## Why wait? The financing hedge use case

Consider a construction company that will issue a bond in nine months to finance a new project. The company wants to fix its borrowing cost now, rather than gamble that [interest rates](/interest-rate/) will be lower when it eventually borrows. Yet issuing the bond today, nine months early, makes no sense—it would have to hold the cash and invest it, earning a much lower rate than it would pay on the bond, creating a drag.

The solution is a nine-month forward-starting, five-year swap. The company and its [counterparty](/counterparty-risk/) (usually a [bank](/jpmorgan-chase/)) agree now that in nine months, they will begin a five-year swap with the company paying a fixed 4.50% and receiving [SOFR](/sofr/) (or another floating index). No cash changes hands today. In nine months, when the company actually issues its bond at a floating rate, it enters the swap and effectively converts the floating bond to fixed at 4.50%. The [hedge](/covered-call/) is in place; the company has achieved its goal of rate certainty without borrowing early.

## Pricing: spot rates and forward rates

A forward-starting swap's fixed rate is determined by a combination of today's spot [yield curve](/yield-curve/) and the [forward-rate](/forward-contract/) curve. If a five-year [swap](/bond/) today is priced at 4.00% and a 1-year forward-starting five-year swap is priced at 4.25%, the 25 basis-point difference reflects the market's expectation that [interest rates](/interest-rate/) will be higher in one year. Traders pricing swaps use mathematical models grounded in no-arbitrage conditions to ensure consistency between spot swaps, forward-starting swaps, and [bond](/treasury-bond/) yields.

The math is elegant. The present value of a forward-starting swap should be equivalent to selling a spot swap, entering a short-term [interest rate](/interest-rate/) [futures contract](/futures-contract/) (or forward rate agreement), and simultaneously buying another swap that begins when the first ends. If the markets are linked correctly, these combinations yield the same economic outcome.

In practice, market participants—especially [banks](/bank-of-america/) and [hedge funds](/hedge-fund/)—continuously compare spot swaps, forward-starting swaps, and bond [yields](/yield-to-maturity/) to arbitrage away mispricings. A mispriced forward-starting swap creates an opportunity to lock in a risk-free gain, and sophisticated traders will execute the trade until the price corrects.

## Market structure and liquidity

Forward-starting swaps are liquid, but less so than spot (today-starting) [swaps](/bond/). The most-traded forward-starting swaps have a delay of three to twelve months before accrual begins and a total [duration](/duration/) of five to ten years. Shorter delays and shorter tenors trade less frequently.

Major banks quote forward-starting swaps electronically on [trading platforms](/stock-exchange/) and dealer networks. A large institutional borrower—a corporation, government agency, or [mortgage REIT](/mortgage-reit/)—can call a bank and get a live two-way quote for a forward-starting swap with custom dates, sizes, and [underlying floating rates](/interest-rate/). Smaller borrowers or those without direct bank relationships access forward-starting swaps through [brokers](/broker/) or derivatives dealers.

The bid-ask [spread](/bid-ask-spread/) on a forward-starting swap widens as the delay lengthens or as the [underlying floating rate](/sofr/) becomes less standard. A 6-month forward five-year swap on [SOFR](/sofr/) might trade with a 1–2 basis-point spread; a 24-month forward swap on a less common index might trade with a 3–5 basis-point spread.

## Use by treasurers and debt managers

Treasury departments of large corporations, municipalities, and financial institutions use forward-starting swaps constantly. When a government agency knows it will issue debt in six months but wants to hedge today, it enters a forward-starting swap. When a bank plans a retail deposit campaign and expects to fund growth through customer inflows three months out, it locks in asset rates using forward-starting swaps.

Central banks also use forward-starting swaps indirectly. When [monetary policy](/monetary-policy/) expectations change—for instance, if the market reprices expectations for [interest rate](/interest-rate/) cuts—the forward-starting [swap curve](/yield-curve/) shifts. A trader betting on future policy can structure a position across spot and forward-starting swaps to profit from curve reshaping.

## Accrual versus notional reset mechanics

Most forward-starting swaps are "standard," meaning the notional principal stays constant throughout, but accrual (the calculation of interest owed) begins at the future start date. Some bespoke forward-starting swaps, however, embed accrual that begins immediately—the floating-rate payer accrues [SOFR](/sofr/) from today—but the exchange of payments is deferred. These structures are rarer and typically used for special hedging situations.

The economic difference is subtle. In a standard forward-starting swap, there is no exposure to rate moves until the forward date. In an accrual-deferred swap, there is exposure to the floating index immediately, but no obligation to pay or receive until later. Treasurers must understand which structure they are entering, as it affects the precise hedge outcome.

## Tenor combinations and the forward curve

The forward-starting swap market is most liquid when combining intuitive dates: a one-year delay with a five-year tenor (1y5y), a two-year delay with a five-year tenor (2y5y), or a six-month delay with a ten-year tenor (6m10y). These combinations are heavily traded by [banks](/bank-of-america/) and funds and reflect common corporate financing cycles.

A trader observing the entire curve of forward-starting swaps—from spot (0y5y) out through 5y5y and 10y5y—can infer the market's expectations for [interest rate](/interest-rate/) changes. If the 1y5y swap rate is much higher than the 0y5y, the market is pricing in rising rates. If it's lower, the market expects rates to fall.

## Risks and complications

Forward-starting swaps carry [interest rate risk](/interest-rate-risk/). If rates fall after the swap is entered but before it accrues, the swap moves in-the-money for the fixed-rate receiver (and out-of-the-money for the payer). The [market value](/fair-value/) of the swap—the amount it would cost to unwind early—grows. Conversely, if rates rise, the value falls.

[Credit risk](/credit-risk/) also exists. If the [counterparty](/counterparty-risk/) defaults between now and the accrual date, the other party loses the benefit of the locked-in rate and must re-hedge in a possibly worse rate environment.

Funding and collateral management adds complexity. Many forward-starting swaps are cleared through central clearinghouses, requiring daily margin posting. A treasurer must budget for potential collateral needs if rates move adversely, especially as the accrual date approaches and the position becomes more sensitive to near-term rate moves.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate Swap](/bond/) — the foundational instrument whose start date is being deferred
- [Swap Spread](/swap-spread/) — forward-starting swaps have their own spread dynamics relative to Treasuries
- [SOFR](/sofr/) — the standard floating index in modern forward-starting USD swaps
- [Counterparty Risk](/counterparty-risk/) — credit risk that the counterparty defaults before accrual begins
- [Forward Contract](/forward-contract/) — structurally similar; both lock in future rates
- [Futures Contract](/futures-contract/) — often used alongside forward-starting swaps in arbitrage and hedge construction

### Wider context

- [Interest Rate Risk](/interest-rate-risk/) — forward-starting swaps accumulate market-value sensitivity as the accrual date nears
- [Yield Curve](/yield-curve/) — forward-starting swap rates trace out the forward-rate expectations embedded in the curve
- [Duration](/duration/) — the duration of a forward-starting swap begins to impact portfolio [risk](/market-risk/) once accrual commences
- [Quantitative Easing](/quantitative-easing/) — central bank actions change [interest rate](/interest-rate/) expectations and shift forward-starting swap valuations
- [Treasury Bond](/treasury-bond/) — benchmarks for [swap spread](/swap-spread/) measurement on forward-starting swaps

</div>
