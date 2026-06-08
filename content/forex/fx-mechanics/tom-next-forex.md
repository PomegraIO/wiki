---
title: "Tom-Next in FX"
description: "A one-day forex swap rolling a position from tomorrow to the next spot date, commonly used to bridge or extend FX exposures without locking in a long-term forward rate."
keywords:
  - tom-next
  - FX swap
  - currency rollover
  - forex mechanics
  - spot date
image: "/svg/forex.svg"
---

*A **tom-next** (or **tomorrow-next**) is a one-day currency swap that simultaneously sells a currency for settlement tomorrow and buys it back for settlement at the next [spot value date](/spot-value-date/). It effectively rolls an FX position forward by one day, without committing to a longer-term forward rate.*

## The structure: two trades, one settlement spread

Tom-next is shorthand for two transactions that happen at the same time but settle on different dates:

1. **Tomorrow leg**: Sell (or buy) a currency for settlement in one business day.
2. **Spot leg**: Buy (or sell) the same currency for settlement at [spot](/spot-value-date/) (two business days later).

The net result: your position moves from settling tomorrow to settling at spot. You have rolled it forward one day.

The price of a tom-next is the difference between the two rates, often quoted as a small number (a few pips). This spread compensates the counterparty for the interest-rate differential between the overnight and two-day funding periods.

## Why traders use tom-next

Tom-next serves three main purposes:

**Avoiding forced cash flows**: A trader who has a position settling tomorrow but wants to keep the exposure decides, "I'll just roll it." Rather than deliver currency today, they enter a tom-next. The cash-flow due tomorrow is offset by the cash-flow they're due to receive tomorrow (from the spot leg selling it back). Net result: they deliver at spot instead.

**Funding flexibility**: A bank may have a large USD/EUR position with settlement tomorrow. The bank's treasury team might not have USD ready yet, but expects it by spot date. Tom-next buys them two extra business days without the cost of a two-week or one-month forward.

**Carry arbitrage**: If overnight interbank lending rates in one currency are cheaper than the tom-next swap rate quoted by dealers, a sophisticated trader can borrow at the cheaper rate and lend via the tom-next, pocketing the spread. This is low-margin but happens in high volume.

**Bridge financing**: A borrower awaiting an overnight loan or a custodian expecting an asset transfer can use tom-next to manage timing mismatches without running afoul of credit lines.

## Pricing and the carry cost

A tom-next rate depends almost entirely on the interest-rate gap between the two currencies over the one-day period. If USD rates are higher than EUR rates, a trader selling USD tomorrow and buying it back at spot must *pay* a rate to the counterparty (because they are financing USD for two days instead of one). This cost, expressed as pips or basis points, is the tom-next spread.

The formula is roughly:
> Tom-next spread ≈ (Overnight rate difference) × (Number of days/360)

For example, if USD overnight rates are 5% and EUR rates are 2%, the tom-next spread for USD/EUR will reflect that 3% annual differential compressed into one day, reducing to about 0.83 basis points.

In illiquid currency pairs or during market stress, the spread widens. The counterparty demands extra compensation for tying up capital or accepting rollover risk.

## Tom-next versus longer-dated forwards

A tom-next is not the same as a one-day [forward contract](/forward-contract/). A forward is a single trade for delivery at a future date, locked in at the outset. Tom-next is a pair of simultaneous spot-type trades in opposite directions.

The key practical difference: tom-next is usually cheaper and tighter than a one-day forward, because it's quoted off [overnight interest rates](/interest-rate/), which are more liquid. A dealer might quote a one-day forward at 10 pips, but the tom-next at only 4 pips. Traders use tom-next for short-term rolling; they use forwards for fixed, longer-term commitments.

## Rolling and chain-rolling

In practice, dealers and corporate treasuries constantly use tom-next to roll maturing FX positions. On a settlement day, rather than settle the trade, the trader enters a fresh tom-next. Day after day, the position rolls forward.

This is called **chain-rolling**. A trader can effectively maintain a constant USD/JPY exposure by rolling daily, paying (or receiving) the daily carry cost each time. Over weeks or months, the cumulative carry cost can be significant, so treasurers carefully model it.

However, chain-rolling introduces **rollover risk**: the dealer's bid-ask spread on tom-next can widen if market liquidity dries up or if there's a sudden event (an unscheduled holiday, a central-bank move). A trader who *needs* to roll because they have no other choice is at the mercy of whatever spread the dealer offers that morning.

## Operational mechanics

Tom-next trades are booked as two separate contracts with two different settlement dates. In the bank's back office, they appear as:

- **TN/TOM** (tomorrow): Sell EUR/Buy USD, settle T+1
- **TN/SN** (spot/next): Buy EUR/Sell USD, settle T+2

Both trades carry the same amount (e.g., EUR 10 million) and reference rate for the pair. The net cash flows at maturity are:

- T+1: Deliver USD, receive EUR (from the first leg)
- T+2: Receive USD, deliver EUR (from the second leg)

This cross-settlement design is one reason tom-next must be carefully documented; misalignment between the two legs on settlement dates or amounts creates [settlement risk](/counterparty-risk/).

## Regulatory and clearing implications

Most major banks clear tom-next swaps through central counterparties (LCH, CME). The clearing process simplifies counterparty risk but adds initial margin and variation margin mechanics. A trader entering a tom-next that moves against them will have to post additional margin within hours, whereas in a bilateral trade, margin might be due at period-end.

In stress events (like March 2020), dealers tightened tom-next spreads and some stopped accepting very large amounts, creating bottlenecks for treasurers trying to roll expiring positions. Central clearing helped but did not eliminate the problem entirely.

## Cost-benefit for non-dealers

For a corporate treasurer, using tom-next is cheaper than setting up a multi-week forward, especially if the need is temporary. But daily rolling means daily monitoring. If the treasurer thinks the position will mature naturally (a foreign-currency invoice is expected to be paid in two days anyway), they might skip the tom-next and just wait.

If they *know* they need the position to extend beyond tomorrow, tom-next is efficient. If they are unsure, the rollover logistics can become tedious.

## See also

<div class="wiki-seealso">

### Closely related

- [Spot value date](/spot-value-date/) — the two-business-day settlement point for FX spot trades
- [Forward contract](/forward-contract/) — fixed-date settlement for currencies and commodities
- [Interest rate](/interest-rate/) — driver of carry cost in tom-next pricing
- [Counterparty risk](/counterparty-risk/) — credit exposure between settlement dates
- [Over-the-counter market](/over-the-counter-market/) — decentralised market where tom-next swaps are quoted

### Wider context

- [Currency volatility](/currency-volatility/) — price swings that interact with rollover decisions
- [Currency risk](/currency-risk/) — exposures that traders manage via tom-next rolls
- [Leverage ratio forex](/leverage-ratio-forex/) — how margin requirements affect rollover capacity

</div>
