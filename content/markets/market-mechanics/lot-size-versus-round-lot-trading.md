---
title: "Lot Size vs Round Lot in Stock Trading"
description: "A round lot is 100 shares; odd lots are smaller. Though exchanges now allow fractional trading, lot size still affects institutional order routing, commissions, and execution."
keywords:
  - round lot trading
  - odd lot definition
  - lot size stocks
  - share trading units
  - institutional order routing
  - trading commission structure
image: /svg/markets.svg
---

*A **round lot** is a standard unit of 100 shares per trade. An **odd lot** is any quantity that does not fill a round lot (e.g., 1–99 shares, or 350 shares). Though modern brokers permit fractional-share purchase and eliminating literal odd-lot penalties, **lot size** remains operationally relevant for institutional trading, [broker](/broker/) order routing, and exchange pricing rules.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Lot Sizes in Equity Markets — units and mechanics</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for markets." />

<div class="wiki-infobox-caption">100 shares remains the standard trading unit despite retail fractional trading.</div>

|   |   |
|---|---|
| **Round lot** | Exactly 100 shares; standard unit on major exchanges |
| **Odd lot** | 1–99 shares, or any remainder not filling a round lot |
| **Mixed lot order** | Order containing both round and odd components (e.g., 250 shares = two round lots + one odd lot) |
| **Historical odd-lot fee** | Brokers charged 1/8 point per share on odd lots; now mostly obsolete |
| **Modern fractional trading** | Retail brokers now allow 0.01-share purchases; lot size less visible but still operative |
| **Institutional routing** | Tier-1 traders still prefer round-lot block trades for speed and anonymity |

</aside>

## The 100-share standard

Lot size in equities has roots in the physical stock certificate era. When shares were pieces of paper, trading in bundles of 100 simplified record-keeping and settlement. That convention persisted when trading moved to electronic screens, and it remains embedded in market structure today.

A **round lot** is precisely 100 shares. A purchase of 100, 200, 500, or any multiple of 100 is a round-lot order. An **odd lot** is anything else: 50 shares, 75 shares, 123 shares, or 5 shares. For decades, odd-lot orders were operationally cumbersome. They were routed separately, processed by specialists or dealers who charged markups to compensate for administrative hassle, and often filled at slightly worse prices than round-lot orders.

## Historical pricing and execution penalties

Before electronic markets, odd-lot buyers and sellers faced real cost disadvantages.

A dealer handling a 100-share round-lot trade on a [stock-exchange](/stock-exchange/) could match it against a customer on the other side with minimal friction. A dealer handling 50 shares faced a choice: combine it with other odd-lot orders to form a round lot, hold it in inventory at risk, or charge the customer a premium (perhaps 1/8 of a point per share, or 12.5 cents per share).

This created a two-tier pricing system. Large traders (institutions, rich individuals) bought in round lots and got the best prices. Small traders buying odd lots paid slightly more on the bid-ask spread. The difference was small per share but cumulative over many trades.

## Modern markets and fractional shares

Electronic trading and retail brokers have softened—though not eliminated—odd-lot friction.

Large retail brokers like Charles Schwab, Fidelity, and Robinhood now permit customers to buy 0.01-share increments (even fractional shares), eliminating the odd-lot category entirely from a customer perspective. A retail investor can buy "$1,000 worth" of a stock priced at $150 and receive 6.67 shares, not constrained by the 100-share round lot.

Behind the scenes, the broker aggregates customer fractional orders and routes the combined order to a [market-maker](/market-maker-trading/) or exchange in a form the market understands. The technical infrastructure of round lots still exists; it is simply hidden from the retail customer.

For retail investors, this means odd-lot pricing penalties are extinct. You pay the published [bid-ask-spread](/bid-ask-spread/), regardless of whether you buy 1 share or 1,000.

## Institutional trading and lot-size mechanics

For institutional investors and professional traders, lot size remains operationally critical.

A large mutual fund or pension fund managing billions of dollars does not route small 50-share orders. It accumulates demand and executes in blocks of 1,000, 10,000, or 100,000 shares. These block trades are negotiated over-the-counter with [broker](/broker/)-dealers who have the capital and market-making capability to absorb large positions.

When a [broker](/broker/) receives a large institutional order—say, "sell 50,000 shares of XYZ"—the execution algorithm splits it into manageable pieces, often round-lot blocks, to minimize market-impact. A 50,000-share order might be routed as:

- 500 round-lot orders of 100 shares each (executed across venues and time)
- Or as a single block trade negotiated bilaterally with a [market-maker](/market-maker-trading/)

The decomposition into round lots is not visible to the customer but affects execution speed, anonymity, and slippage. Round-lot blocks execute faster because market-makers hold inventory at those sizes. Odd-lot remainders (say, 30 shares left over in a 50,030-share order) are routed separately and filled on less favorable terms or held until they can be batched with other orders.

## Exchange pricing rules and lot definitions

Stock exchanges define lot size in their rulebooks, and those definitions affect order priority and execution.

The [New York Stock Exchange](/new-york-stock-exchange/) and [NASDAQ](/nasdaq/) designate 100 shares as the "normal unit of trading" (NUT). Orders for exactly 100 shares or multiples thereof receive priority in certain matching algorithms over orders for odd-lot quantities.

For example, on an automated limit-order book, if there are:
- A 200-share bid at $50.00 (two round lots)
- A 75-share bid at $50.00 (an odd lot)
- A 100-share sell order at $50.00 (one round lot)

The 100-share order matches the 100 shares from the first bid (the round-lot portion), not the entire first bid. The second bid (the odd lot) waits in queue. This matching rule prioritizes round-lot fulfillment.

In practice, this creates minute execution advantages for orders in round-lot sizes. It is not a penalty for odd-lot orders—they still execute—but they wait slightly longer or face marginally less favorable pricing in thick books.

## Order routing and [Alternative Trading System](/alternative-trading-system/)

Lot size also affects how [broker](/broker/) order-routing systems decide where to send an order.

A 500-share order (five round lots) might be routed to a primary exchange (NYSE, NASDAQ) because the round-lot size attracts [market maker](/market-maker-trading/) interest and liquidity. A 75-share order (odd lot with remainder) might be routed to a [broker](/broker/)-dealer's internal inventory or an [Alternative Trading System](/alternative-trading-system/) (ATS) where odd-lot aggregation happens.

Some ATS venues specialize in odd-lot accumulation and block execution. They provide price improvement relative to public spreads by netting customer orders internally. When 15 customers each submit 50-share limit orders, the ATS might net them into a single 750-share order, execute it once, and allocate the fill proportionally to customers.

For individual investors, this is invisible and beneficial—they get a price better than the public book. For institution tracking execution quality and market impact, lot size is part of the calculation.

## Cost basis tracking and tax implications

Lot size affects tax planning for investors holding multiple purchase batches.

When a shareholder sells stock, they must designate which lot (which prior purchase) is being sold to establish the [cost-basis](/cost-basis/) for [capital-gains-tax-investor](/capital-gains-tax-investor/) purposes. If you bought 100 shares in January (cost basis $50), another 100 in March (cost basis $55), and another 100 in June (cost basis $60), and you now sell 150 shares at $65, your [cost-basis](/cost-basis/) depends on lot designation.

Selling the June lot (100 shares at $60) plus 50 shares from the March lot (at $55) yields a lower gain than selling the January lot first (at $50). The ability to specify cost basis via [Form 8949](/form-8949/) and [Schedule D](/schedule-d/) allows sophisticated investors to optimize [tax-loss-harvesting](/tax-loss-harvesting/).

Lot sizes and their composition matter for this calculation. If all purchases were odd lots (e.g., 75 shares each), cost-basis tracking becomes messier; brokers must subdivide lots carefully when you sell a partial quantity.

## Modern practical relevance

The operational importance of lot size has diminished but not disappeared.

For **retail investors**, lot size is nearly irrelevant. Fractional trading and low commissions mean you can buy $1,000 worth of any stock without penalty.

For **day traders** using electronic market-making platforms (e.g., Interactive Brokers, TD Ameritrade's thinkorswim), lot size still shapes order routing and execution latency. Submitting round-lot orders gets faster fills from market-makers than odd-lot orders.

For **institutional traders**, lot size remains fundamental. Block trades, dark pools, and negotiated executions all operate at round-lot granularity. A pension fund accumulating a $5 million position in a $50 stock (100,000 shares = 1,000 round lots) considers lot size when calculating market impact and execution cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Stock-exchange](/stock-exchange/) — primary venues where round-lot rules apply
- [Broker](/broker/) — execution and routing of lot-sized orders
- [Market-maker-trading](/market-maker-trading/) — how round lots affect inventory and pricing
- [Bid-ask-spread](/bid-ask-spread/) — odd lots and round lots in spread structure
- [Alternative-trading-system](/alternative-trading-system/) — venues for odd-lot aggregation
- [Cost-basis](/cost-basis/) — lot identification for tax accounting

### Wider context

- Market-mechanics — structural rules of equity trading
- Order — limit, market, and block order types
- Execution-quality — measuring fills relative to lot size
- [Capital-gains-tax-investor](/capital-gains-tax-investor/) — tax treatment of stock sales

</div>
