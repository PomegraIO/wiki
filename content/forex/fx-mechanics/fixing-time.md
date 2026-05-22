---
title: "Fixing Time"
description: "Benchmark reference time for daily FX settlement, determining spot rates for contracts and fund valuations."
keywords:
  - fx fixing
  - benchmark rates
  - settlement mechanics
  - london fixing
---

*A **fixing time** is a scheduled moment each business day when the [spot](/wiki/spot-exchange-rate/) exchange rate for a currency pair is formally set, usually for settlement purposes and fund valuations. The most widely used is the London 4 p.m. WMR (Wilmot Reuters) fixing, which serves as the reference for trillions in contracts, derivative settlements, and daily valuations. Fixing times matter because they determine who wins and loses on leveraged positions and derivative trades.*

<aside class="wiki-infobox">

| Fixing | Time (UTC) | Use |
|--------|---|---|
| **London WMR** | 16:00 (4 p.m.) | Most common for majors; derivatives settlement |
| **New York** | 21:00 (9 p.m.) | Alternative reference for USD/JPY and others |
| **Singapore** | 08:00 (8 a.m.) | Asian fixing benchmark |
| **Fixing period** | Usually 1 minute window | Prevents manipulation by averaging multiple spot rates |
| **Counterparty selection** | Major banks contribute; median used | Reduces outlier risk |

</aside>

## Why fixing times exist: settlement and valuation

In the [forex](/wiki/forex-leverage/) market, trades settle on [T+2 (two business days after trade date)](/wiki/settlement-cycles/). At settlement, one party sends currency A and the other sends currency B. But what rate applies? The fixing time establishes the official spot rate used for that day's settlements and contract adjustments.

For fund managers, fixing times are critical: a daily valuation of a fund holding foreign assets is computed using the fixing rate for that day. A fund owning 100 million euro must convert to USD at the fixing rate to report its net asset value (NAV). The fixing rate determines whether the fund appears to have gained or lost money in FX terms, even if the underlying assets were unchanged.

## The London 4 p.m. WMR as market standard

The London 4 p.m. fixing (now maintained by the Intercontinental Exchange, after moving from Reuters) is the **de facto global standard**. It is used for:
- Settling [FX forwards](/wiki/fx-forward/) and swaps
- Valuing bonds held in foreign currency
- Determining gains/losses on [carry trade](/wiki/carry-trade/) positions
- Striking [FX options](/wiki/fx-option/) exercise levels
- Daily mark-to-market in derivatives trading

Why London 4 p.m.? Because it is roughly the midpoint of the global trading day. North American markets are open (10 a.m. New York), European markets are about to close (early evening in London), and Asian markets will be just opening in a few hours. Trading volume and liquidity are high.

## Fixing methodology and manipulation risk

Fixing rates are not a single transaction; they are computed as the median (or mean) of spot rates contributed by major banks during a 1-minute window around the fixing time. The window (typically 30 seconds before to 30 seconds after the official time) avoids being distorted by a single block trade or outlier.

However, this methodology creates a vulnerability: if enough banks collude or if a large [position holder](/wiki/positioning-limit/) can move the spot rate in their favor during the fixing window, they can influence the fixing and profit. This actually happened: in 2013–2015, major banks (Deutsche Bank, Barclays, Citigroup, UBS, RBS) were found to have manipulated FX fixings by coordinating trades to move rates in their favor at fixing time. The scandal, known as the **FX fixing scandal**, resulted in billions in regulatory fines and criminal charges.

Post-scandal, fixing methodologies were tightened: more banks contribute, larger observation windows are used, outliers are excluded, and surveillance for coordination has increased.

## Fixing and derivative strikes

For [options](/wiki/option-greeks/), the fixing time determines whether an option is in-the-money, out-of-the-money, or at-the-money. An exporter with a [put option](/wiki/put-option/) protecting against euro weakness is keenly interested in what the fixing rate is at expiration. If the fixing is 1.10 USD/EUR, an option with strike 1.10 expires worthless. If it is 1.09, the put is in-the-money by 1 cent.

Large options positions create incentive for fixing manipulation: a trader with a billion-euro short position profits if the fixing falls 1 cent. This is why regulators now closely monitor fixings for suspicious activity—spikes in volume, orders entered moments before fixing time, or coordinated activity across multiple banks.

## Multiple fixings for different instruments

Not all trades use the London 4 p.m. fixing. Some use:
- **New York 9 p.m. fixing** for USD/JPY derivatives
- **Singapore 8 a.m. fixing** for Asian currency pairs
- **Mid-price fixings** computed from bid-ask spreads of multiple dealers
- **Transaction-based rates** (for money market instruments, settlements can use actual trade rates rather than official fixings)

The choice is typically specified in the contract. If a swap agreement says "London 4 p.m. WMR," that fixing is binding. If it does not specify, disputes can arise.

## Transition from LIBOR analogs to fixing governance

Like [LIBOR](/wiki/libor/), the FX fixing system was once loosely governed—banks submitted rates informally, and there was little transparency or regulation. Post-2015 scandal, governance tightened significantly. The International Organization of Securities Commissions (IOSCO) now oversees FX fixing standards. Submissions are authenticated, timestamped, and audited. Submitting banks face sanctions for manipulation.

## Practical implications for traders

For [position traders](/wiki/position-trading/) and funds, knowing the fixing time is critical. Carrying a foreign-currency position into the fixing window involves the risk that the fixing will move against you. Some traders deliberately position ahead of fixing times, hoping to influence flows; others actively avoid the volatility and exit positions before the window.

<div class="wiki-seealso">

### Closely related
- [Spot Exchange Rate](/wiki/spot-exchange-rate/) — The rate being fixed
- [FX Forward](/wiki/fx-forward/) — Instruments settled using fixing rates
- [FX Option](/wiki/fx-option/) — Derivatives whose payoffs depend on fixings
- [Settlement Cycles](/wiki/settlement-cycles/) — The T+2 window

### Wider context
- [LIBOR](/wiki/libor/) — Another benchmark plagued by manipulation
- [Benchmark Rate](/wiki/interbank-lending-rate/) — Fixing's role in financial architecture
- [Forex Mechanics](/wiki/carry-trade-pairs/) — Broader FX trading context
- [Central Bank Intervention](/wiki/currency-intervention/) — Sometimes occurs around fixings

</div>
