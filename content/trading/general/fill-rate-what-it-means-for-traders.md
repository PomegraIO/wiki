---
title: "Fill Rate: What It Means for Limit-Order Traders"
description: "Fill rate for limit orders: percentage of order executed, how queue position and spreads affect it, venue differences."
keywords:
  - fill rate limit orders
  - what is fill rate for limit orders
  - limit order fill rate trading
  - order queue position fill rate
image: /svg/trading.svg
---

*Your **fill rate** is the percentage of a [limit-order](/limit-order/) that actually executes at your chosen price. If you place a 1,000-share limit buy at $50 and only 600 shares fill, your fill rate is 60%. It depends on queue position, [bid-ask-spread](/bid-ask-spread/) width, trading velocity, and venue. A limit order that sits on the order book unfilled has a 0% fill rate; a limit order that fills instantly has 100%. Understanding fill rate helps traders balance execution certainty with price discipline.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fill Rate — Key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for securities trading." />

<div class="wiki-infobox-caption">How much of your limit order actually executes; depends on queue position and market movement.</div>

|   |   |
|---|---|
| **Fill rate definition** | Percentage of order quantity that executes (0–100%) |
| **Main drivers** | Queue position, spread width, order flow, volatility |
| **Queue behavior** | Price-time priority: your position depends on arrival time at same price |
| **High-velocity venues** | Nasdaq, NYSE Arca; deep books, tight spreads, higher fill rates |
| **Thin-stock venues** | OTC, small-cap exchanges; wider spreads, lower fill rates |

</aside>

## What fill rate measures

**Fill rate** is straightforward: it's the fraction of your order size that gets executed. If you enter a 1,000-share limit buy at $50 per share and 750 shares trade, you have a 75% fill rate. If none trade, fill rate is 0%. If all 1,000 trade, fill rate is 100%.

A limit order gives you price certainty but not execution certainty. By contrast, a [market-order](/market-order/) fills immediately (near-100% fill rate on liquid stocks) but the price is uncertain—you might buy at $50.01 instead of your limit of $50.00. The tradeoff between price discipline (limit) and execution certainty (market) is the core of limit-order strategy.

Fill rate is especially important for traders working large positions or trading illiquid stocks. A day trader buying 100 shares of Apple at the limit is almost certain to fill. A trader trying to buy 50,000 shares of a micro-cap stock at limit may fill only a few thousand and watch the rest sit on the order book.

## Queue position and time priority

When you place a limit buy at $50, you join a queue of other buy orders at that price, ordered by arrival time. This is "price-time priority." The first buyer at $50 (earliest order) has first priority if and when sellers appear. Your order behind them waits. If a seller hits the bid at $50, the first buy order in the queue fills first, then the second, and so on.

Your position in the queue determines how much of your order fills when liquidity arrives. If you're 50th in the queue and only 100 shares are offered for sale at your price, you might fill zero shares. If you're 5th and 500 shares are sold, you might fill your entire 1,000-share order (catching the last 500 at your price), or you might fill only part of it depending on the orders ahead of you.

This is why many limit orders on liquid stocks fill only partially. A 1,000-share limit order might be 200th in queue; when a sell order arrives, it fills the first few hundred orders in line, and by the time your order's turn comes, the seller's shares are exhausted. You get 50 shares; fill rate is 5%.

On less-liquid stocks or off-hours trading, queues are much shorter, so if your order sits alone or has few orders ahead of it, fill rates are higher (assuming sellers arrive).

## Spread width and time to fill

A narrow [bid-ask-spread](/bid-ask-spread/) increases fill rate. If you buy at the bid (inside the spread), your order is likely to fill quickly because you're at the current best price. If you set your limit inside the spread—say, the bid is $50.00 but you offer $49.95—your order waits longer and may never fill if the stock doesn't drop.

Example: Apple [bid-ask](/bid-ask-spread/) is $150.00 (bid) to $150.01 (ask), a tight one-cent spread. If you place a limit buy at $150.00, you're matching the bid, and you queue behind other $150.00 bids. You fill quickly if shares are offered at $150.00. If you limit at $149.99, you're inside the spread, and you'll only fill if the price drops to $149.99—which might not happen.

Spread width varies by:
- **Liquidity**: Apple (highly liquid) has 1–2 cent spreads; a micro-cap might have 5–10 cent spreads.
- **Volatility**: Wide spreads widen in choppy markets; tight spreads widen during gaps.
- **Venue**: Large exchanges ([NYSE](/new-york-stock-exchange/), Nasdaq) have tighter spreads and deeper books than [OTC](/over-the-counter-market/) or regional markets.

Traders choosing tighter limit prices (closer to current bid/ask) get higher fill rates at the cost of potentially worse prices; traders choosing aggressive prices (inside the spread) get worse fill rates but might improve price if the market moves.

## Venue and fill-rate differences

Different trading venues have different fill-rate profiles. [Nasdaq](/nasdaq/) and [NYSE](/new-york-stock-exchange/), with the deepest order books and tightest spreads in large-cap stocks, offer high fill rates for competitive limit prices. An alternative trading system (ATS) or a regional exchange might have wider spreads and lower volume, making high fill rates harder to achieve.

OTC markets—informal dealer networks for stocks not listed on major exchanges—have even lower liquidity and wider spreads. A limit order in an OTC stock might sit for minutes or hours and never fill because few market makers are actively quoting at your price.

Cryptocurrency exchanges ([cryptocurrency-exchange](/cryptocurrency-exchange/)) vary: major venues like Coinbase or Kraken have tight spreads and high volume, supporting 80%+ fill rates on large orders; smaller exchanges have wider spreads and lower fill rates.

The practical implication: traders on liquid venues can pursue aggressive (inside-the-spread) limit prices and still achieve reasonable fill rates. Traders on illiquid venues must be less ambitious with price and accept either lower fill rates or wider spreads.

## Partial fill and slippage

A partial fill is both a feature and a drawback. A limit order that partially fills locks in your price for part of the position but leaves you chasing the remainder at a potentially worse price if you chase it with a market order.

Example: You limit-buy 1,000 shares at $50, intending to position size at 1,000. Only 400 fill immediately. You now have a decision: wait longer for the remaining 600 (risking price slippage if the stock moves up), or market-buy the remaining 600 (buying at the ask, likely $50.02 or worse). If you market-buy, your average fill price is ~$50.012 instead of $50.00—you've "given up" the benefit of the limit order through partial fill and chase.

High-frequency traders and algorithmic trading systems optimize for fill rates by slicing orders intelligently across time and venues, balancing price (limit precision) with execution certainty (fill rates).

## Monitoring and adjusting fill rates

Traders can improve fill rates by:
- **Choosing liquid venues and hours**: Place orders on Nasdaq or NYSE during market hours, not after-hours.
- **Adjusting limit prices moderately**: Set limit prices near (not far inside) the current bid/ask, accepting minor price slippage for higher fills.
- **Using iceberg orders**: Some venues allow hidden order sizes, releasing quantity gradually to avoid moving the market.
- **Splitting large orders**: Break a 10,000-share order into 1,000-share chunks to reduce queue position and improve fill rates.

Brokers and trading platforms report fill rates and execution-quality metrics. Retail traders should review these; they're a sign of whether your broker is giving you fair execution or routing orders to lower-liquidity venues to capture rebates (a conflict of interest).

## The tradeoff: fill rate vs. price

The core tension in limit-order trading is that higher fill rates come at the cost of worse prices, and vice versa. A market order gives you 100% fill rate but uncertain price. A limit order deep inside the spread gives you great price but 0% fill rate if the market doesn't reach you.

Smart traders set limit prices just inside the best bid or ask—accepting small slippage (a penny or two) in exchange for high fill rates and price certainty. Patients traders or those trading very liquid stocks can set limits further inside the spread and still achieve good fills over longer time horizons.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — How limit orders work and when to use them
- [Bid-Ask Spread](/bid-ask-spread/) — Why spreads exist and how they affect trading costs
- [Market Order](/market-order/) — The execution-certainty alternative
- [Price Discovery](/price-discovery/) — How order books reveal trading intention

### Wider context

- Order Queue and Latency — Why microseconds matter in trading
- [Market Maker Trading](/market-maker-trading/) — How professionals provide liquidity
- [Execution Risk](/execution-risk/) — Broader risks beyond fill rate
- [Stock Exchange](/stock-exchange/) — How venues differ in structure and rules

</div>
