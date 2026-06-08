---
title: "Partial Fill in Order Execution"
description: "What is a partial fill in trading: when only part of your order executes, how brokers handle the remainder, and cost implications."
keywords:
  - partial fill trading
  - order execution partial
  - unfilled order remainder
  - limit order partial fill
  - market order slippage
---

*A **partial fill** occurs when only part of your [order](/limit-order/) executes and the rest remains in the [order book](/limit-order-book-priority-rules/) or is canceled. This is common with large limit orders, illiquid securities, or fast-moving markets. You pay [commissions](/broker/) on the filled portion, hold the unfilled amount at [limit price](/limit-order/) or cancel it, and may face slippage if you chase the execution.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Partial Fill — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Your 1,000-share order fills 600 shares; the other 400 wait or get canceled.</div>

|   |   |
|---|---|
| **Definition** | Portion of order executes; rest remains pending or is rejected |
| **Common in** | Large limit orders, thinly traded stocks, volatile markets |
| **Execution rule** | Exchange and broker determine fill algorithm, often "first in, first out" |
| **Unfilled amount** | Stays in order book at your limit price until filled or canceled |
| **Market orders** | Less likely to partial in liquid stocks; more likely in illiquid ones |
| **Broker handling** | Partial fills reported separately; unfilled remainder shown in order status |
| **Cost per fill** | Commission applied to each execution, sometimes per fill, sometimes per order |
| **Chasing price** | Canceling and resubmitting at worse price to speed execution increases costs |

</aside>

## Why Partial Fills Happen

Partial fills occur because there is not always enough liquidity at your limit price. If you place a limit buy for 10,000 shares at $50, but only 3,500 shares are currently offered at $50, you get a partial fill of 3,500 and 6,500 shares remain in the [order book](/limit-order-book-priority-rules/).

Market depth — the supply and demand stacked behind the best bid and ask — determines how much you can fill immediately. In highly liquid stocks like Apple or Tesla, a 10,000-share order might fill instantly. In a smaller-cap stock or after-hours trading, it might execute in chunks over minutes or hours.

**Limit orders** are prone to partials because they sit at a single price. A market order, by contrast, sweeps through multiple price levels and is less likely to partial (unless the entire market is illiquid). But even market orders can partially fill if the underlying security has very thin trading volume.

## Unfilled Remainder in the Order Book

Once your limit order is partially filled, the unfilled portion remains a **resting order** in the [order book](/limit-order-book-priority-rules/). It waits in queue, ranked by [price-time priority](/limit-order-book-priority-rules/). If you were the 5th buyer at $50 and 1,000 of your 2,000 shares just filled, your remaining 1,000 shares stay as the 5th order in the $50 queue.

You can monitor this in your broker's order management system. Many brokers show "Partial Fill" status and list the remaining quantity. You can leave it resting (hoping the price stays near $50), [cancel and resubmit](/limit-order/) at a different price, or close the position if you no longer want it.

Leaving an order resting ties up margin or capital depending on your broker's rules. A partial buy still reserves the cash for the unfilled remainder; a partial short still reserves [shares](/stock/) to borrow.

## Immediate and Delayed Fills

A single "order" can result in multiple fills across time. Example:

- 10:00 AM: you submit buy for 5,000 shares at $100
- 10:05 AM: 2,000 shares fill
- 10:12 AM: 1,500 shares fill
- 10:45 AM: 1,500 shares fill
- Order complete, 0 unfilled

Your broker reports three separate **fill events**, though they are all part of one order. Each fill is timestamped and priced separately for tax accounting (you may use [FIFO](/fifo/), [LIFO](/lifo/), or [specific identification](/specific-identification-basis/) to match fills to cost basis).

## Commission and Fee Treatment

Commission structures vary. Some brokers charge per order (flat fee for the entire quantity, filled or unfilled); others charge per execution. If your broker charges $10 per order, you pay $10 whether the order fills 100% at once or in five tranches. If they charge per fill (say, $2 per fill), a five-tranche partial fill costs $10 total.

Some brokers offer tiered commissions: lower rates for larger fills or order values. A partial fill might incur proportional commissions if the broker uses a "per-share" model. The net effect is that partial fills can be slightly more costly than single-price fills.

## Trading Costs and Slippage

A partial fill creates a choice: accept that the remainder might not fill at your target price, or chase the execution by canceling and resubmitting at a worse price.

If you want 5,000 shares at $100 and only 2,000 fill, you could:

1. **Wait**: leave the 3,000-share order resting and hope more shares come offered at $100. This costs nothing extra but delays your full position.
2. **Resubmit higher**: cancel the 3,000-share order and resubmit at $100.50 or $101 to attract sellers. This fills faster but costs you $0.50–1.00 per share on the incremental 3,000, or $1,500–3,000 total.

The decision hinges on urgency. A trader trying to enter a position before earnings can afford slight slippage; a passive index tracker willing to wait a few hours can save money by holding the order.

## Market Orders and Partials

A [market order](/market-order/) is designed to execute immediately, so partials are less common in liquid markets. A market buy for 5,000 shares in Apple executes almost instantly across multiple [asks](/bid-ask-spread/).

But in illiquid securities — micro-cap stocks, thinly traded international shares, or crypto on small exchanges — market orders can still partial if not enough liquidity exists at the market-clearing price. The broker might execute what is available and either (a) cancel the rest, or (b) leave a resting market order, which is rare.

## Reporting and Tax Implications

Each fill is reported separately on your broker statement. For tax purposes, each fill is its own purchase with its own cost basis. If you sell later, you must match those sales to buys using FIFO, LIFO, or [specific identification](/specific-identification-basis/).

Example: you bought 2,000 shares at $100, 1,500 at $100.20, and 1,500 at $99.80 (three partial fills). When you sell 3,000 shares, you owe [capital gains](/long-term-capital-gain-tax/) on the difference between the sale price and your cost basis, depending on which fills you identify as sold.

Many brokers default to FIFO (first in, first out), so the 2,000 oldest shares and 1,000 of the next 1,500 are matched to the sale. You can override this with specific identification in most brokers.

## Algorithmic and Iceberg Orders

Professional traders use algorithms to avoid partials or to exploit them. An "iceberg" order reveals only a small amount of volume (e.g., 500 of 5,000 shares) and automatically resubmits as each tranche fills, reducing [market impact](/market-risk/). This guarantees fills but spreads them over time.

Execution algorithms (e.g., VWAP, TWAP) also manage partials by working a large order into the market over a period, aiming for a better average price than a single market order.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — the order type most prone to partials
- [Market Order](/market-order/) — executes faster but accepts slippage
- [Order Book](/limit-order-book-priority-rules/) — where unfilled portions rest
- [Bid-Ask Spread](/bid-ask-spread/) — determines liquidity and partial-fill likelihood
- [Broker](/broker/) — executes orders and determines fill handling
- [FIFO](/fifo/) — tax lot matching rule for partial fills
- [Specific Identification](/specific-identification-basis/) — alternative matching method

### Wider context

- [Market Impact](/market-risk/) — how large orders move price and trigger partials
- [Algorithmic Trading](/algorithmic-trading/) — techniques to manage partial fills
- [Liquidity Risk](/liquidity-risk/) — core reason partials occur
- [Stock Exchange](/stock-exchange/) — where orders are matched

</div>
