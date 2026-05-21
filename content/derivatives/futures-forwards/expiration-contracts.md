---
title: "Expiration Dates"
description: "How futures and forwards specify their maturity dates—contract calendars, notice periods, and the mechanics of what happens when a contract expires."
---

*Derivatives are born with an expiration date baked into their DNA. Unlike a stock, which exists indefinitely, a futures contract is an obligation that terminates on a precise calendar day. That day drives both the contract's pricing and the behavior of its traders.*

## Contract cycles and the calendar

[Futures contracts](/wiki/futures-contract/) trade on fixed calendars. Most actively-traded [commodity futures](/wiki/commodity-contract-specifications/) have contracts for the next 10 to 20 expiration dates, stretching months or even years into the future. The front-month (nearest expiration) is where the most volume trades. Back months are thinner.

For example, WTI crude oil futures expire on the third business day before the 25th calendar day of the contract month. December WTI expires in early November. January WTI expires in late December. Traders always know the expiration date; it is written in the contract specification. This predictability allows hedgers to plan: if you know oil is expiring the third Wednesday of November, you can time your [hedging](/wiki/hedging-with-futures/) to that calendar.

## The notice period and delivery window

Physical delivery contracts introduce complexity that financial contracts avoid. If a contract matures, someone must deliver. But the short side (the seller of the futures) cannot show up with a truck on the last day and expect to off-load a shipment. Instead, exchanges define **notice periods**—a window during which a seller can notify the exchange and the clearing house of intent to deliver.

For metals futures, this window opens weeks before final expiration. For agricultural commodities, it may open at the start of the delivery month and extend for weeks. The notice period accomplishes two things:

- **It gives the buyer time to arrange logistics.** If you are long 100 contracts of soybeans and the short side announces delivery intent, you need time to arrange warehouse space, arrange financing, and plan transportation.
- **It prevents surprises.** Without a notice period, the short side could hold the long side hostage, using the threat of physical delivery as leverage to negotiate an off-market price.

During the notice period, the risk of physical delivery becomes real, and prices adjust accordingly. Many long traders close their positions before this window opens rather than take on delivery responsibility.

## Last trading day

Most contracts specify a **last trading day**—the final day on which a position can be opened or closed. This date is earlier than the expiration date itself. On the last trading day of September soybeans, new trades can still be struck. After the close on that day, no new longs or shorts can be created; only existing positions remain active.

For [cash-settled contracts](/wiki/cash-settlement/), the last trading day and expiration date are often identical or very close. The index is fixed at the close; positions are settled in cash immediately. For physical delivery contracts, the last trading day comes weeks before final expiration, giving traders time to execute their intentions (take delivery, make delivery, or offset positions entirely).

## The roll forward

Because most trading happens in the front-month contract, a systematic ritual unfolds as expiration approaches: the **roll forward**. Traders and funds that want to maintain a position must close the front month and open the next month's contract. This creates a spike in volume; both the expiring month and the next month trade at elevated volumes on the final days.

The roll can be a profitable trade or a losing one. If [contango](/wiki/contango/) is steep (the far-month contract is much more expensive), rolling becomes expensive. If [backwardation](/wiki/backwardation/) prevails (the front month is expensive relative to later months), rolling is profitable. [Commodity index funds](/wiki/commodity-etf/), which hold a static portfolio of rolling futures positions, suffer or benefit depending on the curve shape during their rolls.

## The final settlement

Once expiration arrives, all remaining positions are closed or delivered. For cash-settled contracts, a reference price is published (often the opening print of the expiration day, the closing price, or a special settlement auction). All longs and shorts are marked to this price; money changes hands, and the contract is dead.

For physical delivery contracts, long and short positions that were not voluntarily closed are settled through delivery. The short side makes physical delivery (or tenders it, or arranges it via warehouse receipt) to the exchange's approved locations. The long side accepts delivery and pays the contract price. This is where the contract's true purpose—serving the real economy—becomes visible.

## Why expiration dates matter

Expiration dates structure the entire futures market. They determine:

- **Liquidity patterns.** The front-month contract is most liquid; traders migrate to the next month as each expiration approaches, creating predictable volume flows.
- **[Basis](/wiki/basis/) behavior.** As expiration nears, futures prices converge to spot prices. The [basis](/wiki/basis/) (spot minus futures) shrinks toward zero. This convergence is deterministic and is the engine of [hedging](/wiki/hedging-with-futures/).
- **Pricing of [cost of carry](/wiki/cost-of-carry/).** The gap between contract months reflects storage costs, interest rates, and convenience yields—the entire economic structure that [contango](/wiki/contango/) and [backwardation](/wiki/backwardation/) embody.
- **Hedging strategy.** A farmer hedging next year's harvest must choose which futures months to short. Picking the month that expires just after harvest is the most efficient [hedge](/wiki/hedging-with-futures/).

Without expiration dates, futures would be indistinguishable from forward contracts. With them, futures become a machine for price discovery and risk transfer across time.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/futures-contract/">Futures contract</a> — standardized derivatives with fixed expiration dates and daily [mark-to-market](/wiki/mark-to-market/).</li>
<li><a href="/wiki/forward-contract/">Forward contract</a> — customized, usually with a single expiration date chosen by the counterparties.</li>
<li><a href="/wiki/basis/">Basis</a> — the spread between spot and futures prices, which converges as expiration approaches.</li>
<li><a href="/wiki/contango/">Contango</a> — forward months trading higher than spot, common when [cost of carry](/wiki/cost-of-carry/) is positive.</li>
<li><a href="/wiki/backwardation/">Backwardation</a> — forward months trading lower than spot, often reflecting scarcity or convenience yield.</li>
<li><a href="/wiki/cost-of-carry/">Cost of carry</a> — the economic forces (storage, interest, dividends) that drive the spread between spot and futures.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/derivatives/">Derivatives</a> — the broad category encompassing futures, forwards, and options.</li>
</ul>
</div>
