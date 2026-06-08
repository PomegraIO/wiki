---
title: "Price Improvement in Order Execution"
description: "What price improvement is, how brokers execute orders better than the NBBO, and how to evaluate whether your broker delivers it."
keywords:
  - price improvement
  - price improvement order execution
  - what is price improvement
  - nbbo
  - order execution quality
image: "/svg/trading.svg"
---

*In trading, **price improvement** occurs when your order is filled at a price better (lower for a buy, higher for a sell) than the national best bid and offer (NBBO)—the best publicly available price. Brokers and market makers can deliver price improvement by internalizing orders, negotiating block trades, or routing to venues with deeper liquidity.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Price Improvement — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Price improvement is a real rebate—you pay less or receive more than the market's posted spread allows.</div>

|   |   |
|---|---|
| **Definition** | Filling at a price better than the current NBBO |
| **For a buy order** | Filling below the national best offer |
| **For a sell order** | Filling above the national best bid |
| **Typical range** | 0.01 to 0.10 per share, more on large blocks |
| **Who delivers it** | [Brokers](/broker/), [market makers](/market-maker-trading/), [alternative trading systems](/alternative-trading-system/) |
| **How to verify** | Compare actual fill price to NBBO at time of submission (your [broker](/broker/) reports this data) |

</aside>

## How price improvement happens

Price improvement exists because the NBBO is a snapshot of public liquidity on major exchanges. Below that surface, vast pools of liquidity exist in dark pools, between market makers, and inside broker order books.

When a broker receives your order, they have several choices. They can route it to a public [stock exchange](/stock-exchange/) and accept the NBBO. Or they can look internally: do they have a buyer or seller on the other side in their own order queue? If so, they can execute you at a price better than the NBBO, pocketing a small profit from the difference. This is called order internalization.

Alternatively, a broker can negotiate a block trade directly with a [market maker](/market-maker-trading/) or block desk. A market maker might agree to sell you 50,000 shares at \$50.02 when the public [ask price](/bid-ask-spread-explained/) is \$50.05. The market maker accepts a lower spread to move size, and you get price improvement.

A broker might also route to an alternative venue—a [dark pool](/alternative-trading-system/) or a regional exchange—where the order book offers better liquidity than the national best offer.

## The broker's incentive and risk

Brokers profit from price improvement by capturing the spread they save you. If you wanted to buy at the national best offer of \$50.05 and the broker sells you \$50.02 shares from their inventory, they keep the \$0.03. The question is: are they taking that spread from their own pocket, or are they passing it through from a better-posted bid or offer they found elsewhere?

Many brokers claim they "pass through" price improvement from real liquidity sources. Others are intentionally buying or selling against their clients' orders, effectively acting as a principal (a mini-market maker). Both are legal under Securities and Exchange Commission (SEC) rules, provided the broker discloses the practice and is not painting the tape or manipulating quotes.

For your purposes, price improvement is free money. You should always prefer a broker that executes with better prices than the NBBO, all else equal.

## Positive versus negative slippage

Price improvement is the opposite of [slippage](/slippage-in-trading/). Slippage is when you expected to fill at the NBBO but end up with a worse price. Price improvement is when you expected to fill at the NBBO but end up with a better price.

For example, you submit a limit order to buy 1,000 shares at \$50.00. The NBBO is \$50.02 ask / \$50.00 bid. Normally, you would expect to wait for a seller at \$50.00, or accept \$50.02 if you use a [market order](/market-order/). But a market maker fills you at \$49.99—price improvement of \$0.01 per share, or \$10 total. That is positive slippage or price improvement, depending on your terminology.

## How to measure and evaluate price improvement

The SEC requires brokers to report execution quality metrics, including the frequency and magnitude of price improvement. You can access this data through:

**Rule 10b-1 reports.** Brokers publish quarterly execution quality reports to the SEC. These show, for each security, how many shares were executed with price improvement, at NBBO, and with worse prices. Public data is available on the SEC's website.

**Your broker's execution quality dashboard.** Many brokers offer clients their own execution statistics—what percentage of orders filled at NBBO, with improvement, or with worse prices. If your broker does not offer this, ask for it.

**Comparing actual fills to the NBBO.** On each trade, note the NBBO at the moment you submitted your order and compare it to your fill price. Over dozens of trades, a pattern emerges. If your average fill is consistently better than the NBBO, your broker is delivering price improvement.

Pay special attention to:
- **Frequency.** Do you get price improvement on 5% of trades or 50%?
- **Magnitude.** Is it a penny (\$0.01) or a dime (\$0.10)?
- **Size dependency.** Do larger orders get more improvement, or does it vanish once you exceed a certain size?

## When price improvement is not available

Price improvement is rarest when spreads are widest:

- **Volatile or illiquid stocks.** In a stock with a \$1.00 [bid-ask spread](/bid-ask-spread-explained/), there is little room for a broker to offer price improvement and still profit.
- **Earnings announcements or economic data.** When prices are moving fast, brokers become risk-averse and pull quotes, shrinking the pool of internalized liquidity.
- **After-hours trading.** With fewer market participants, price improvement opportunities shrink.
- **Small orders.** Brokers are less likely to dedicate resources to improving execution on 100-share orders; the profit margin is tiny.

Large institutional traders, conversely, almost always negotiate price improvement on block trades. A pension fund buying 1 million shares can negotiate pricing directly with a [market maker](/market-maker-trading/) or broker, often beating the NBBO by meaningful amounts.

## Dark pools and price improvement

Some of the most aggressive price improvement in U.S. equity markets occurs in dark pools—private trading venues operated by brokers and banks. A dark pool does not publish quotes; instead, liquidity is hidden until orders are matched.

This creates both opportunity and risk. The opportunity is that a [market maker](/market-maker-trading/) in a dark pool might offer you a price inside the NBBO to attract your order. The risk is opacity—you cannot see the full liquidity picture, and you may not realize that a better price existed in a public venue you were not shown.

Regulators have increased scrutiny of dark pool execution quality over the past decade, pushing venues to prove they are delivering price improvement to clients, not just to themselves.

## How to optimize for price improvement

**Choose a broker transparent about execution.** Look for brokers that publish their price improvement statistics and break them down by security and order size.

**Use limit orders.** A limit order gives a broker more flexibility to source better liquidity without the risk of market impact.

**Trade liquid stocks.** Mega-cap stocks have enough depth that multiple brokers can compete on price improvement.

**Ask your broker about their best practices.** Some brokers offer guaranteed price improvement on certain order types or securities.

**Monitor your fills regularly.** Compare your actual prices to the NBBO over a month. If you are consistently filling worse than the NBBO, switch brokers.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread Explained](/bid-ask-spread-explained/) — the baseline price you are trying to improve on
- [Slippage in Trading](/slippage-in-trading/) — the opposite of price improvement; worse-than-expected fills
- [Market Maker Trading](/market-maker-trading/) — how market makers source and offer price improvement
- [Limit Order](/limit-order/) — the order type most conducive to price improvement
- [Market Order](/market-order/) — instant fill, often without price improvement

### Wider context

- [Alternative Trading System](/alternative-trading-system/) — dark pools and other venues offering price improvement
- [Stock Exchange](/stock-exchange/) — public venues where NBBO is set
- [Broker](/broker/) — the intermediary responsible for execution quality
- [Fill-or-Kill Order](/fill-or-kill-order/) — all-or-nothing orders that may forfeit price improvement for certainty
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator overseeing execution quality rules

</div>
