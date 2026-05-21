---
title: "Rollover Management"
description: "How traders and funds maintain long-term futures positions by systematically closing expiring contracts and opening equivalent new ones—managing the cost and mechanics of staying invested."
---

*A [futures contract](/wiki/futures-contract/) has an [expiration date](/wiki/expiration-contracts/). If you want a position that extends beyond that date, you must roll it forward—close the old contract and open the new one. The cost and mechanics of this process are invisible to the end investor but determinative for long-term returns.*

## The mechanical roll

When September crude oil futures are set to expire, a trader holding an equivalent position in October crude must execute a roll. On the designated roll date (typically a week or two before expiration, depending on the exchange and contract), the trader:

1. Sells all September contracts (closing the long or short position).
2. Simultaneously (or immediately after) buys equivalent October contracts.

From the trader's perspective, nothing changes: they remain exposed to crude oil price risk. But technically, they have exited one contract and entered another.

Most professional funds automate this. A [commodity fund](/wiki/commodity-etf/) that holds a static allocation to crude oil futures will execute thousands of rolls per year, each one choreographed according to a calendar the fund publishes. Retail traders using futures must remember to roll or face [delivery](/wiki/delivery-mechanisms/) of the physical commodity (or cash settlement if the contract is cash-settled).

## The cost of rolling: the curve

The critical detail is this: the September contract and the October contract almost never trade at the same price. If October crude trades at $85 and September trades at $86, the roll costs you $1 per barrel. Multiply by your position size, and the cost becomes real.

The shape of this curve determines the entire economics of long-term futures holding. If the market is in [contango](/wiki/contango/) (later months more expensive), rolling forward—selling near and buying far—is costly. If the market is in [backwardation](/wiki/backwardation/) (later months cheaper), rolling is profitable.

A [commodity fund](/wiki/commodity-etf/) that holds crude oil rolling the contract once per month will lose or gain depending on the curve shape over that period. In periods of steep [contango](/wiki/contango/), a fund's returns are dragged down by persistent roll losses. This is not a market timing loss; it is a structural cost that shows up in the fund's [expense ratio](/wiki/expense-ratio/) or, more honestly, in the fund's performance relative to spot prices.

## Who rolls and why

**Long-term hedgers** (companies needing to lock in future prices, insurance companies protecting portfolios) roll continuously to maintain their exposure. A farmer hedging next year's corn crop will roll every three months as the expiring month approaches, always maintaining exposure to the upcoming harvest season.

**Commodity funds and indices** roll according to fixed schedules. Some roll evenly across many months (a calendar spread). Others roll concentrated in the front month, minimizing exposure to [basis](/wiki/basis/) risk. The choice affects performance: a fund rolling concentrated in the front month bears more curve risk (the front month might be more expensive relative to later months) but less complexity.

**Speculators** may roll or may simply close positions and re-enter if they wish to extend a bet. A trader who buys crude oil futures expecting a price spike does not have to hold the position all the way to expiration; they can close it weeks or months before expiration and re-enter if sentiment shifts.

## Timing and execution

The choice of *when* to roll can matter. The standard practice is to roll early (5-10 days before expiration) when both the near and far months are liquid. Rolling too late risks illiquidity: the expiring contract thins dramatically as traders flee; bid-ask spreads widen; slippage increases.

But rolling early means holding the new contract for longer, which can be expensive or profitable depending on the curve. A fund that rolls five days before expiration of September crude will be long October crude for a full month before September expires. If the October-September spread widens during that month, the fund loses.

Professional traders and funds have sophisticated rolling strategies:

- **Calendar spreads:** Simultaneously selling the near month and buying the far month, locking in the curve spread explicitly rather than doing separate trades.
- **Staggered rolls:** Rolling a portion of the position every day or every few days, averaging execution across time.
- **Dynamic rolls:** Waiting for favorable curve conditions (backwardation periods) before rolling, accepting the risk of illiquidity near final expiration.

## The roll yield

From the investor's perspective, roll yield is the return earned (or lost) purely from the rolling process, independent of price moves. If crude oil price stays flat but the fund rolls from $85 September to $84 October, the roll costs money—negative roll yield. If the fund rolls from $86 September to $85 October, it costs money but less than the price decline that happened earlier.

Over long periods, roll yield can dominate returns. A fund that buys crude oil in 2020 and holds it rolling forward through 2024 will have experienced steep [contango](/wiki/contango/) in 2020-2021 (costly rolls) and periods of [backwardation](/wiki/backwardation/) in 2021-2022 (profitable rolls). The cumulative impact of these rolls, independent of price changes, is visible in the fund's total return vs. spot crude prices.

This is why [commodity funds](/wiki/commodity-etf/) often underperform spot commodity prices over multi-year periods: the cost of rolling is real, and [contango](/wiki/contango/) can be steep.

## The mechanics of settlement

When a contract expires, the roll must be complete. On the final day of September crude, all remaining September positions are settled (cash or [delivery](/wiki/delivery-mechanisms/)). If you failed to roll, you are settled whether you like it or not.

For [physically deliverable contracts](/wiki/delivery-mechanisms/), failure to roll means accepting or making delivery of the physical commodity. A farmer can take delivery of soybean futures if they want the soybeans; most traders cannot, so they must roll. For [cash-settled contracts](/wiki/cash-settlement/) like index futures, failure to roll means your position is liquidated at the settlement price.

This mandatory settlement is why roll discipline is essential. Miss a roll, and the clearing house makes decisions for you.

## Automated rolling and ETF tracking

Modern [commodity ETFs](/wiki/commodity-etf/) and [leveraged ETFs](/wiki/leveraged-etf/) automate rolling using rules known to the market. Some publish their roll schedules in advance. This transparency creates opportunities for arbitrage but also means the market can front-run the rolls: if everyone knows the fund will roll 100,000 contracts of crude oil on Thursday, traders may position ahead of that event.

The impact of automated rolling on commodity prices is debated. Some research suggests that heavy rolling by indices and funds amplifies the impact of [contango](/wiki/contango/) or [backwardation](/wiki/backwardation/), potentially pushing near-month contracts to expensive or cheap levels relative to fundamentals. But the evidence is mixed, and the debate is live.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/expiration-contracts/">Expiration dates</a> — the scheduling framework that makes rolling necessary and predictable.</li>
<li><a href="/wiki/contango/">Contango</a> — forward months more expensive than spot, making rolls costly for long-term holders.</li>
<li><a href="/wiki/backwardation/">Backwardation</a> — forward months cheaper than spot, making rolls profitable for long-term holders.</li>
<li><a href="/wiki/basis/">Basis</a> — the spot-futures spread, which is another way to understand roll costs.</li>
<li><a href="/wiki/cost-of-carry/">Cost of carry</a> — storage, interest, and other economic forces driving the term structure of futures prices.</li>
<li><a href="/wiki/commodity-etf/">Commodity ETF</a> — funds that roll futures mechanically to track commodity prices for retail investors.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/futures-contract/">Futures contract</a> — the standardized vehicles on which rolling is performed.</li>
<li><a href="/wiki/derivatives/">Derivatives</a> — the broader category encompassing all leveraged and risk-transfer instruments.</li>
</ul>
</div>
