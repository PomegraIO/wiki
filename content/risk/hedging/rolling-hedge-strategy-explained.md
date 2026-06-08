---
title: "Rolling Hedge Strategy Explained"
description: "How firms use rolling hedge strategies with futures to maintain long-term commodity and interest-rate exposure without holding distant contracts."
keywords:
  - rolling hedge strategy futures
  - futures roll hedge
  - continuous hedging strategy
  - commodity hedge rolling
  - interest rate hedge futures
  - contract rollover hedging
image: "/svg/risk.svg"
---

*A **rolling hedge strategy** involves continuously replacing short-dated futures contracts with new ones at longer maturities, maintaining steady exposure to a commodity or interest rate without ever holding a contract through expiration or deep into its life.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rolling Hedge Strategy — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The method keeps derivative exposure fresh and liquid while avoiding operational friction of physical delivery or contract expiry.</div>

|   |   |
|---|---|
| **Core idea** | Replace maturing short-dated futures with new contracts at longer dates |
| **Primary use** | Commodity producers, refiners, airlines, importers, treasurers maintaining long-term exposure |
| **Timing** | Roll typically weeks or months before contract expiration |
| **Cost source** | [Basis risk](/basis-risk/), [contango](/contango/) or [backwardation](/backwardation/) between contracts, execution slippage |
| **Key advantage** | Avoids physical delivery; maintains liquid contracts; predictable execution |
| **Key risk** | Roll date price movement; cumulative slippage on repeated rolls; mismatch between hedged and rolling tenor |

</aside>

## How Rolling Maintains Continuous Hedge Exposure

A company that needs commodity or rate protection for years—say, an airline locking in jet fuel costs, or a utility hedging natural gas through winter—faces a structural problem: futures contracts expire. The nearest contract loses liquidity as expiration nears, and buying a contract two or three years out carries less liquidity and wider spreads than the front contract.

Rolling hedge strategy solves this by staying in the front part of the curve. As the near-term futures contract approaches expiration (typically 2–8 weeks before), the hedger closes that position and opens an identical notional position in the next contract month. The process repeats continuously, creating an unbroken chain of hedge coverage.

A jet fuel hedger, for instance, might sell June crude oil futures in March, then roll that position into July or August contracts in May. When July approaches, those roll into September or October. Over five years, the hedger might execute 20–30 rolls, always staying in relatively liquid, nearby contracts.

## Basis Risk and Slippage at Each Roll

The real cost of rolling emerges from the mismatch between the price at which the near contract closes and the price at which the next contract opens.

When the hedger exits the June contract and enters July on the same day, the spread between June and July is locked in at roll time. This spread depends on [contango](/contango/) (July futures trading above June) or [backwardation](/backwardation/) (July trading below June). In a steep contango market—typical for storable commodities like crude oil or natural gas—the roll loss is visible and immediate: the hedger sells June at $80 and buys July at $83, locking in a $3/barrel cost that flows through the economics.

Over multiple rolls across a year or decade, these slippages accumulate. A [basis-risk](/basis/) calculation reveals whether the cumulative drag is worth the benefit of avoiding delivery mechanics and near-term contract illiquidity.

The timing of the roll also matters. Rolling too early (more than a month ahead of expiration) means transacting in less liquid back contracts. Rolling too late risks forced execution when the front contract is in its final, volatile days. Professional hedgers typically establish roll calendars weeks in advance and execute during windows of normal market conditions.

## Working Example: Agricultural Commodity Hedger

Consider a corn producer with a harvest expected in September who wants to lock in revenue at planting time (March). March corn futures are liquid, and the producer sells 100 contracts at $4.80/bushel to hedge the expected crop.

In June—about 3 months before harvest—the July contract (the next delivery month after June) is now the liquid nearby contract. The producer closes the July position at $4.65 and buys September at $4.70. The roll cost is $0.05/bushel ($0.65 loss on closing July minus $0.70 gain if July had stayed flat).

By late August, the September contract approaches expiration. The producer rolls into December (the next tradeable month) at a cost reflecting the seasonal premium for post-harvest delivery. The pattern repeats: each roll locks in incremental slippage, but the producer never faces the delivery logistics or the extreme volatility of a contract in its final week.

## Rolling vs. Long-Dated Contracts

A natural alternative is to simply buy or sell the contract at the target maturity upfront—say, the December contract in March, holding it through September. Why roll instead?

**Liquidity**: Nearby contracts (the front contract and the one or two months after) trade with the tightest spreads and highest volume. A contract twelve months out has wider spreads and lower depth. Rolling in liquid contracts often produces better execution prices than a single transaction in a distant contract.

**Volatility**: The last week or two of a contract's life often sees erratic trading as holders adjust or close positions. Exiting just before that window avoids that noise.

**Operational simplicity**: For ongoing operations (airlines, refiners, utilities), rolling creates a mechanical, repeatable process that compliance and treasury staff can monitor and execute on schedule.

**Basis stability**: The basis (the gap between spot and futures) is more stable and better-understood for nearby contracts. A distant contract's basis can be highly uncertain.

The tradeoff is that rolling requires repeated execution and accumulates transaction costs. In calm, flat markets, rolling and holding a distant contract produce similar outcomes. In volatile markets with steep contango, the cost of rolling can be substantial—which is precisely when hedgers most need to evaluate whether the hedge is worth its expense.

## Timing Considerations and Roll Windows

Professional hedgers establish formal roll schedules. For a weekly-rolling program (common in energy markets), the hedger might close the Monday contract on Friday and open Tuesday on Monday, minimizing weekend gap risk. For monthly rollers, a typical calendar rolls on the 10th business day of each month into the next contract month.

The roll window—the period when execution can occur without undue slippage—typically spans two to four weeks before expiration. Outside that window, the spread between contracts may be distorted or unstable. Rolling during trending or event-driven days (FOMC announcements, crop reports, geopolitical shocks) can widen spreads significantly.

Automated or algorithmic execution during the roll window helps large hedgers minimize the price impact of their trades, especially critical for positions large enough to move the market.

## When Rolling Strategies Break Down

Rolling hedge strategies assume the near-term and deferred contracts remain correlated (move together proportionally). When they decouple—for instance, during a supply shock that affects the prompt month but not deferred delivery, or a credit event that disrupts the [contango](/contango/) structure—the effectiveness of the hedge can suffer. A hedge designed to protect against spot price moves may instead accumulate unexpected losses from roll slippage that doesn't correlate with the underlying exposure.

Additionally, if the underlying risk (the exposure being hedged) changes character or disappears earlier than expected—say, a company completes an acquisition that removes the need for some hedges—terminating the rolling program mid-stream can lock in realized losses.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — How deferred contracts trade above spot, creating roll costs
- [Backwardation](/backwardation/) — When deferred contracts trade below spot, favoring roll economics
- [Basis risk](/basis-risk/) — The gap between the hedge instrument and the actual exposure
- [Futures contract](/futures-contract/) — The mechanics of standardised derivative contracts
- [Derivatives hedging](/derivatives-hedging/) — Broader framework of using derivatives to reduce risk
- [Cost of debt](/cost-of-debt/) — How interest-rate rolling protects financing costs

### Wider context

- Commodity curves — Structure of multi-month futures prices
- [Interest rate swap](/interest-rate-swap/) — Alternative derivative tool for long-term rate exposure
- [Counterparty risk](/counterparty-risk/) — Operational risk in repeated derivative trading
- [Market maker trading](/market-maker-trading/) — How liquidity exists in nearby contracts

</div>
