---
title: "Total Value Locked"
description: "A metric measuring the aggregate dollar value of cryptocurrency assets deposited in DeFi protocols, widely cited but subject to double-counting and methodological ambiguity."
keywords:
  - total value locked
  - tvl
  - defi metrics
  - asset under management
  - double counting
image: "/svg/crypto.svg"
---

*The **total value locked** (TVL) is the aggregate dollar value of all cryptocurrency assets deposited into a DeFi protocol or across the entire ecosystem. It is the industry's primary yardstick for protocol size and liquidity, yet the metric conflates distinct categories of risk and often double-counts assets moved between protocols.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Total Value Locked — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and decentralized finance." />

<div class="wiki-infobox-caption">A headline number—useful but misleading if misread.</div>

|   |   |
|---|---|
| **What it is** | Sum of USD-denominated value of assets in a DeFi protocol at a point in time |
| **Calculation** | Asset quantity × price per unit, summed across all deposits |
| **Typical sources** | DeFi Pulse, DefiLlama, Dune Analytics |
| **Advantages** | Simple, comparable across protocols, correlates roughly with liquidity |
| **Drawbacks** | Double-counts nested positions, ignores leverage, conflates safety profiles |
| **Common unit** | Billions of USD ($B) |

</aside>

## Why TVL matters and why it misleads

TVL is ubiquitous because it answers a simple question: how much money is using this protocol? A protocol with $10 billion TVL is, prima facie, larger and more liquid than one with $1 billion. Assets in a pool mean transactions can execute, borrowers have capital to access, and the protocol can absorb price shocks without cascading liquidations.

Yet TVL is not a proxy for safety, profitability, or risk-adjustment. Two protocols with identical TVL may have vastly different risk profiles: one might hold mostly stablecoins in a [money market protocol](/money-market-protocol/), the other volatile altcoins in a leverage-trading venue. A protocol with high TVL may generate minimal fees if capital is idle; another with low TVL but high transaction velocity might yield greater returns to users. TVL says only: *this much notional value has flowed in and not yet left*.

## The double-counting trap

The most insidious flaw of TVL is recursive counting. Suppose a user deposits 1,000 USDC into Aave (a [money market protocol](/money-market-protocol/)) and borrows ETH. That USDC is counted in Aave's TVL. The user then deposits the borrowed ETH into Curve (a decentralized exchange) for yield, and that same ETH is counted in Curve's TVL. Finally, the user uses Curve's LP token as collateral in another Aave position. Now that LP token is counted again in Aave's TVL.

One unit of capital can thus be counted three, four, or more times across protocols. When headline figures tout "DeFi TVL hit $100 billion," much of that number is the same dollar counted repeatedly. During booms, recursive leverage inflates TVL figures; during busts, margin calls and liquidations deflate them rapidly—not because capital left the ecosystem entirely, but because leverage unwind reduced the count.

Most professional analysts now track *unique value locked*—assets that belong to non-smart-contract accounts, or adjusted figures that penalize nested deposits. But the raw TVL figures published by popular trackers (DefiLlama, DeFi Pulse) remain unadjusted, making them useful as sentiment indicators but dangerous as measures of true ecosystem size.

## Measurement inconsistencies across protocols

TVL also disguises differences in what "locked" means. In a [money market protocol](/money-market-protocol/), a deposit of 100 USDC is immediately available for withdrawal (subject to utilization constraints) and is counted as TVL. In a liquidity pool on a decentralized exchange, capital is locked for the duration of the liquidity provider's commitment, often with unbounded price exposure. In a derivative perpetual-futures venue, "value locked" refers to collateral, much of which is leveraged and represents notional exposure many times its notional value. All three are lumped into one TVL figure.

A more nuanced metric would distinguish between passive deposited collateral, active trading collateral, and LP capital exposed to impermanent loss. Instead, TVL collapses these into a single number.

## TVL by protocol category

Practitioners often segment TVL by protocol type: lending (money markets), decentralized exchanges, derivatives, and cross-chain bridges. Lending protocols have historically commanded the largest TVL share because deposits are persistent; users earn yield on long-term positions. Decentralized exchanges attract TVL proportional to traded volume—high volume can justify capital in liquidity pools. Derivative protocols see TVL spike during volatility and liquidation cascades; calm markets see TVL drain as traders close leveraged positions.

TVL concentration is also notable. The largest three protocols often command 40–50% of total DeFi TVL, creating systemic risk: a failure or exploit in a major protocol cascades. Conversely, fragmentation of TVL across many smaller protocols can signal ecosystem maturity (capital flowing to best-performing venues) or dysfunction (users abandoning large protocols for reasons).

## TVL and actual user returns

A final caution: TVL does not determine user returns. A protocol with massive TVL and low fee revenue can offer poor yields; one with modest TVL and high activity can offer excellent ones. TVL is a snapshot of capital quantity, not capital productivity. Yield farmers track yield—expressed as annual percentage rate or APR—not TVL. A savvy user compares TVL to fees earned and protocol risk before committing capital.

## See also

<div class="wiki-seealso">

### Closely related

- [Money Market Protocol](/money-market-protocol/) — primary TVL category, lending platforms
- [Decentralized Exchange](/decentralized-exchange/) — liquidity pools and their TVL composition
- [Yield Farming](/yield-farming/) — strategies capturing returns within DeFi
- [Impermanent Loss](/impermanent-loss/) — risk to liquidity providers in volatile pairs
- [Liquidation](/liquidation/) — TVL-collapsing mechanism during downturns

### Wider context

- Decentralized Finance — ecosystem TVL rollup and governance
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — centralized alternatives with different metrics
- Asset Under Management — traditional finance analogue
- [Market Capitalization](/market-capitalization/) — crypto asset valuation metric

</div>
