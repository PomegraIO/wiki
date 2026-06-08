---
title: "Cliquet Option"
description: "A series of reset options that lock in gains periodically while maintaining upside exposure throughout the contract's life."
keywords:
  - cliquet option
  - reset option
  - exotic option
  - derivatives
image: "/svg/derivatives.svg"
---

*A **cliquet option** is a series of nested [at-the-money options](/option/) that reset periodically, locking in accumulated gains and starting fresh with a new [strike price](/strike-price/) at each reset date. Also called a reset option or ratchet option, it's designed to capture upside movement while protecting earlier profits from later reversals.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cliquet Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and structured contracts." />

<div class="wiki-infobox-caption">A long-lived derivative that locks in gains periodically and resets exposure.</div>

|   |   |
|---|---|
| **What it is** | A series of overlapping at-the-money options that reset on preset dates |
| **Also called** | Reset option, ratchet option, rachet option |
| **Payoff structure** | Sum of gains in each reset period; earlier gains cannot be lost |
| **Common underlyings** | Equities, [forex](/us-dollar/), [commodities](/crude-oil/), indices |
| **Buyer motivation** | Harvest gains from rallies without risk of giving back earlier profits |
| **Seller motivation** | Collect premium upfront; cap maximum loss on any reset leg |
| **Key difference from vanilla** | No single [strike price](/strike-price/); multiple strikes reset automatically |

</aside>

## How the reset mechanics work

A cliquet option's life is divided into discrete reset periods—typically quarterly or annually. At the start of the first period, the option's [strike price](/strike-price/) equals the current asset price; it's at-the-money. If the asset rises by 8%, the holder locks in that 8% gain. On the reset date, a new at-the-money option begins with a fresh strike price set to the asset price on that date, regardless of whether it's higher or lower than where the last period ended.

The holder's total payoff is the sum of all gains realized in each reset period. A crucial asymmetry emerges: gains are cumulatively earned, but losses in any single period are capped—the holder walks away from that reset leg, and the next one starts afresh. This ratcheting behavior is the namesake draw for investors and hedgers who want to participate in rallies without the risk of a single violent drawdown wiping out a year's worth of accumulated profits.

## Why cliquet options appeal to conservative investors

Traditional [call options](/call-option/) force a painful trade-off: buy protection with a high [strike price](/strike-price/) and forfeit upside, or buy a low strike and face catastrophic loss if the underlying drops sharply. A cliquet lets a holder have it both ways over a longer period. If an equity index rallies steadily over two years, the investor locks in monthly or quarterly wins. If a sudden crash happens in month 18, the holder has already banked the first 17 months' gains.

This structure appeals especially to pension funds and insurance companies with long investment horizons who care more about steady accumulation than maximum short-term payoff. The drawback is cost: the upfront [premium](/option-premium/) is higher than a single vanilla option because the seller is effectively selling multiple embedded options. The pricing also reflects [volatility](/historical-volatility/) over the entire life of the contract, not just a single maturity date.

## Valuation and the role of volatility

Cliquet pricing depends critically on [implied volatility](/implied-volatility/) within each reset period, not the realized path of the underlying asset. A stock that jumps 20% in month 1 and then drifts sideways is worth more to the cliquet holder than one that meanders up 5% per month. The reason: the reset mechanism locks in the full jump immediately, then the next period starts fresh from the new, higher level.

Conversely, high volatility between reset dates (with no trend) hurts the buyer. The seller's risk is also multifaceted: if early resets go deeply in-the-money, the seller's cumulative liability grows rapidly. Most dealers hedge cliquet exposure by replicating the embedded options and rebalancing as spot prices move.

## Variations and real-world use

Banks offer many cliquet flavors. A **leveraged cliquet** amplifies gains in each reset period (e.g., 150% of the measured move) in exchange for a higher premium. A **capped cliquet** places a ceiling on gain per period, lowering cost. Some structures include a **floor**—a minimum payoff if the asset falls, paid for by capping upside.

[Currency traders](/currency-risk/) use cliquets to lock in forex gains over trading cycles. A Japanese importer worried about yen appreciation might buy a cliquet on USD/JPY that captures monthly rallies in the dollar without exposure to reversals. [Commodity traders](/crude-oil/) employ them to harvest seasonal trends: oil often rallies in winter and weakens in summer, so a series of reset periods can capture each cycle's distinct move.

## The cost of locking in gains

Cliquet premiums are rarely cheap. Because each reset period is, in effect, a separate at-the-money option, the total premium is roughly the sum of all those individual premiums. An investor comparing a three-year cliquet to a single three-year vanilla option will pay a significant premium for the reset benefit. This structure only pays off if the underlying asset exhibits the kind of trendy, rally-then-consolidate pattern that resets can exploit. In a sideways or slowly drifting market, the early resets may trigger small gains that don't compound enough to justify the upfront cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — foundational contract giving the holder the right, not obligation, to buy or sell
- [Strike Price](/strike-price/) — the agreed price at which an option may be exercised
- [Call Option](/call-option/) — the right to buy an asset at a fixed price
- [Implied Volatility](/implied-volatility/) — expected price swings priced into the option
- [Option Premium](/option-premium/) — upfront cost paid by the option buyer
- [At-the-Money](/option/) — an option whose strike equals the current asset price
- [Shout Option](/shout-option/) — similar exotic option with a single lock-in date chosen by the holder
- [Power Option](/power-option/) — exotic option with a nonlinear payoff function

### Wider context

- [Exotic Option](/option/) — family of complex derivatives beyond vanilla calls and puts
- [Derivatives](/option/) — financial contracts whose value derives from an underlying asset
- [Volatility Smile](/volatility-smile/) — observed pattern in implied volatility across strike prices
- [Hedging](/option/) — using derivatives to reduce exposure to adverse price moves
- [Forex](/currency-risk/) — trading in foreign exchange markets

</div>
