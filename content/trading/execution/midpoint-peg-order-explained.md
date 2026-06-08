---
title: "Midpoint Peg Order Explained"
description: "How midpoint peg orders track the NBBO midpoint to minimize market impact and execution costs, and why traders choose them over limit or market orders."
keywords:
  - midpoint peg order
  - midpoint peg order how it works
  - peg to midpoint trading
  - minimize market impact order
  - execution algorithm trading
  - national best bid offer
image: "/svg/trading.svg"
---

*A **midpoint peg order** is a type of order that automatically reprices itself to match the midpoint of the National Best Bid and Offer (NBBO) on each trade, offering a trader a better fill price than a traditional limit order in fast-moving markets while reducing the risk of not being filled. It sits between passive limit orders and aggressive market orders, appealing to traders who want to trade closer to fair value without taking on the worst execution of an outright market order.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Midpoint Peg Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Continuously reprices to track the NBBO midpoint in real time.</div>

|   |   |
|---|---|
| **How it works** | Automatically adjusts order price to the midpoint between best bid and ask |
| **Reprice frequency** | Continuously, on each NBBO update across all exchanges |
| **Typical use** | Mid-sized institutional orders seeking fair execution without market impact |
| **Execution guarantee** | No guarantee; loses priority to orders pegged at the bid or ask |
| **Market impact** | Reduces impact vs. market orders; higher than limit orders at best bid/ask |
| **Broker support** | Most major brokers offer midpoint peg algorithms; [alternative trading systems](/alternative-trading-system/) also support them |
| **Best for** | Liquid stocks where NBBO changes frequently |

</aside>

## The NBBO and Why the Midpoint Matters

To understand midpoint peg orders, you must first understand the National Best Bid and Offer. Every second, the [bid-ask spread](/bid-ask-spread/)—the difference between the highest price a buyer will pay (the bid) and the lowest price a seller will accept (the ask)—changes as orders flow in across all U.S. stock exchanges and trading venues. The NBBO is the aggregation of the single best bid and single best ask across all these venues.

For example, if the NBBO is a bid of $50.00 and an ask of $50.10, the midpoint is $50.05. This midpoint represents a notional "fair value"—exactly halfway between the sides of the market. It is where a neutral counterparty with no informational edge might reasonably transact.

For decades, traders had a simple choice: place a limit order at the bid (if selling) or the ask (if buying), or send a market order that crossed the spread. A limit order near the NBBO was safe—you could not be picked off at a worse price—but might not fill in a fast market. A market order would fill immediately but could execute at a terrible price if the market gapped or if you were filling a large block.

The midpoint peg order offers a third way. Instead of sitting at a fixed price, your order automatically climbs or falls with the midpoint, giving you a continuously updated "fair" price without the aggressive footprint of a market order.

## How Midpoint Peg Orders Reprice

When you submit a midpoint peg order to buy 10,000 shares of a liquid stock, your broker's system does the following in real time:

1. Receives every NBBO tick (bid and ask prices) from the consolidated feed.
2. Calculates the midpoint: (best bid + best ask) ÷ 2.
3. Reprices your buy order to that midpoint.
4. Waits for a fill as the market trades, or reprices again when the next NBBO tick arrives.

This happens dozens of times per second in active stocks. Your order price is not static; it floats. If the bid tightens toward your price, the midpoint rises, and your order rises with it. If the market widens, your order falls. You are always pegged to the center.

Fills occur when the stock trades at or through your peg price. If you are buying at the midpoint and the stock trades at the ask, you will not fill. But if it trades at the bid and that bid price is below your peg price, you will not fill either. You only fill when real trades occur at or through your peg price—which happens frequently in liquid stocks but less so in thinly traded ones.

## Midpoint Peg vs. Limit and Market Orders

A [limit order](/limit-order/) placed at a fixed price (say, $50.00) does not reprice. It has a fixed "time priority"—the longer it sits, the higher in the queue it is. But in a fast market, your price can quickly become stale. You might have wanted to buy at $50.00, but by the time the stock reaches that price again, a hundred other limit orders are ahead of you.

A [market order](/market-order/) guarantees a fill almost immediately, but you have no control over price. In a wide market or during a liquidity crunch, you could pay significantly more than you intended.

A midpoint peg order resets your priority on every NBBO tick. It does not sit at the back of a queue. But because you are trading at the midpoint—technically at neither the bid nor the ask—you are not on the exchanges' official order books that get queued by time. Instead, you rely on your broker's venue to execute you when the stock trades near your peg price. This can mean faster execution in active names, but no time priority in quiet ones.

The trade-off: your fill price is better than a market order and fairer than a limit order at worst bid/ask, but you risk not filling at all if the market moves away from your price or if volume dries up.

## When Traders Use Midpoint Peg Orders

Midpoint pegs are popular for several scenarios:

**Large institutional orders.** A pension fund or mutual fund buying 100,000 shares does not want to show a market order on the tape, which would signal aggressive demand and cause the market to run up. A midpoint peg order gives a reasonable execution without broadcasting intent.

**Volatile or fast-moving markets.** If a stock is gapping up or down, a fixed limit order becomes irrelevant in seconds. A peg order automatically adjusts to the new market.

**Liquid equities.** Midpoint pegs work best in names with tight spreads and frequent NBBO changes. In illiquid micro-cap stocks, the NBBO may change rarely, and your peg price may not move often enough.

**Algorithms and passive execution.** Many execution algorithms (used by brokers to slice large orders) include a midpoint peg component. A broker might execute your order through a combination of midpoint pegs, limit orders, and small market orders.

**Tighter spreads in times of stress.** Counterintuitively, midpoint pegs sometimes execute better in market stress. Bid-ask spreads widen, so the midpoint is now further away from both sides—a potentially attractive compromise when liquidity is tight.

## How Execution Venues Handle Midpoint Orders

Regulation SHO and Rule 10b-5 require that orders be executable at their displayed price, but midpoint peg orders are not displayed on the standard market data feed the way a conventional limit order is. Instead, they are held on a broker's or alternative trading system's own matching engine.

Many **alternative trading systems** ([ATS](/alternative-trading-system/)) have built-in midpoint crossing functionality. Brokers like Goldman Sachs, JPMorgan, and Morgan Stanley run internal crossing networks where customer orders can be matched at the midpoint during each second. If your broker sends your midpoint peg order to an ATS midpoint crossing service, you might fill against another customer's order at the NBBO midpoint with zero spread.

For orders not matched at an ATS, your broker's algorithm will attempt to route your order to the lit (public) markets when the stock trades near your peg price, or hold it for crossing with other customers.

## Risks and Limitations

**No guarantee of execution.** Unlike a market order, a midpoint peg can sit unfilled if the stock does not trade at your price. If the market jumps from $50.00 ask to $50.20 ask without trading in between, your buy order pegged at the midpoint will also jump, and you might never fill.

**Information leakage.** If your broker's routing is visible to other market participants, aggressive traders can front-run or predict your order. This is less of a concern with large brokers running internal crossing networks, but is a real risk with smaller venues.

**Execution quality in low-volume stocks.** In thinly traded names, the NBBO might be stale or the spread might be so wide that the midpoint is still not a great price. Midpoint pegs are not a cure-all for illiquidity.

**Regulatory complexity.** Different venues have different rules about how midpoint orders are handled. Some venues peg to the bid or ask instead of the midpoint, or peg to one side but step in front of the other side. Understanding the nuances of each execution venue is important.

## Midpoint Pegs in Modern Markets

The rise of high-frequency trading has made NBBO updates faster and spreads tighter, making midpoint pegs more attractive. In the early 2000s, before high-speed connectivity became standard, a midpoint peg could sit for seconds without a fill. Today, in large-cap liquid stocks, a midpoint peg can execute within milliseconds.

Some critics argue that midpoint pegs can be used to circumvent market data priorities—by pegging rather than displaying on an exchange, an order avoids the strict time priority rules of the lit markets. Regulators have scrutinized ATS midpoint crossing services to ensure they are not unfairly advantaging certain participants. But the practice remains legal and widely used.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit order](/limit-order/) — fixed-price order with time priority
- [Market order](/market-order/) — immediate execution at market price
- [Bid-ask spread](/bid-ask-spread/) — the spread within which the midpoint falls
- [Alternative trading system](/alternative-trading-system/) — venue for midpoint crossing
- [Execution algorithm trading](/algorithmic-trading/) — often includes midpoint peg components
- [Price discovery](/price-discovery/) — role of NBBO and midpoint in fair valuation
- [Market maker trading](/market-maker-trading/) — counterparty to pegged orders

### Wider context

- [Stock market](/stock-market/) — broader context for order types
- [Over-the-counter market](/over-the-counter-market/) — alternative to exchange execution
- [Regulation SHO](/securities-and-exchange-commission/) — regulatory framework for order handling
- [Liquidity risk](/liquidity-risk/) — risk that a peg order will not fill

</div>
