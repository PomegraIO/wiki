---
title: "Crossed Market vs Locked Market"
description: "Locked markets have identical bid and ask prices; crossed markets have the bid above the ask. Both are anomalies that Reg NMS requires exchanges to resolve quickly."
keywords:
  - crossed market vs locked market
  - locked market trading
  - crossed market definition
  - bid ask anomaly
image: /svg/trading.svg
---

*A **locked market** occurs when the best bid and best ask are at the same price—the [bid-ask spread](/bid-ask-spread/) is zero. A **crossed market** is worse: the highest bid is above the lowest ask, inverting the normal relationship. Both are rare but fleeting anomalies in modern markets. Regulation NMS requires exchanges to correct them within seconds or risk fines.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Locked vs Crossed Markets — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two price-inversion anomalies that trigger automatic intervention.</div>

|   |   |
|---|---|
| **Locked market** | Bid = Ask (zero spread) |
| **Crossed market** | Bid > Ask (inverted spread) |
| **Normal state** | Bid < Ask (positive spread) |
| **Cause** | Latency, order routing delays, multiple exchanges |
| **Reg NMS requirement** | Must be corrected or deferred within 1 second |

</aside>

## Normal Markets: Bid Below Ask

In a functioning market, the highest price a buyer will pay (the [bid](/bid-ask-spread/)) is always lower than the lowest price a seller will accept (the ask). An Apple stock might have a bid of $222.50 and an ask of $222.51. The spread of $0.01 is the profit a [market maker](/market-maker-trading/) earns for standing ready to trade.

This spread exists because:

- Buyers want the lowest price.
- Sellers want the highest price.
- Market makers bridge them, buying at the bid and selling at the ask.
- The spread compensates makers for inventory risk and execution costs.

In most trades, the market is in this healthy state. Bid is below ask.

## Locked Market: When Bid Equals Ask

A **locked market** occurs when the highest bid equals the lowest ask. Apple stock: bid $222.50, ask $222.50. The spread is zero.

This is unusual but not necessarily an error. It can happen when:

1. **Heavy buying interest**: Many buyers willing to pay $222.50, but few sellers willing to accept less than $222.50. The best bid rises to meet the ask.
2. **Multiple exchanges asynchronous**: A buyer on Nasdaq executes at the ask, raising the bid to that price; meanwhile, a seller on a regional exchange hasn't updated yet.
3. **Fast-moving markets**: During price spikes (earnings announcements, geopolitical events), liquidity can momentarily dry up and orders can lock.

In a locked market, there's no spread profit available. A buyer and seller would both accept the same price, but they're not immediately matched. The order book shows equal bids and asks, awaiting the next quote update or trade execution.

A locked market can persist for seconds if:
- No one trades to clear the overlap.
- Market makers are quoting the same price on different venues and haven't synchronized.
- An exchange has a latency issue and is slow to cancel stale orders.

## Crossed Market: Bid Above Ask

A **crossed market** is more severe: the highest bid is above the lowest ask. Apple stock: bid $222.52, ask $222.50. The bid is $0.02 above the ask.

This is theoretically an arbitrage opportunity. A trader could buy at the ask ($222.50) and immediately sell at the bid ($222.52), pocketing $0.02 with zero risk. Yet the trade doesn't happen because the bid and ask are on different exchanges or with different market makers who aren't in direct contact.

Crossed markets arise from:

1. **Exchange latency**: An order executes on the NYSE at $222.50, raising the NYSE bid to $222.51. Simultaneously, a new sell order hits Nasdaq at $222.52 (the old ask). Before the exchanges sync quotes via the consolidated feed, the bid and ask are inverted.
2. **Order routing delays**: A broker receives a sell order, routes it to Nasdaq, but hasn't yet cancelled an old buy order on the NYSE. In between, quotes cross.
3. **Fragmented markets**: With U.S. stocks trading on 13+ venues (NYSE, Nasdaq, regional exchanges, and dark pools), timing mismatches are inevitable.

Crossed markets represent an inefficiency and a regulatory violation. They imply that efficient trading is not occurring, and they create opportunities for informed traders to exploit stale quotes.

## Why Regulation NMS Requires Correction

The SEC's Regulation National Market System (Reg NMS), adopted in 2007, mandated that exchanges and market makers eliminate locked and crossed markets. The rule, called the "Order Protection Rule" or "Trade-Through Rule," requires:

- **Locked or crossed quotes must be corrected or deferred within 1 second**.
- **Exchanges must route orders to respect the best quote** across all venues, even if it means splitting the order.
- **Exceptions**: Exchanges can briefly defer correcting a cross if they're actively working to fix a technical glitch.

If an exchange fails to fix a cross within the tolerance, it can face fines. The SEC has issued fines to major exchanges (including Nasdaq and the NYSE) for repeatedly violating the rule.

The 1-second window is short because systems today operate at microsecond speeds. But the SEC recognized that occasional, momentary crosses are inevitable in a fragmented market and allowed a small grace period before enforcement.

## How Exchanges Fix Crosses and Locks

When an exchange detects a locked or crossed market, it has several options:

1. **Trade execution**: If a trade can occur at the locking/crossing price, both the bid and ask orders are executed, eliminating the imbalance.
2. **Quote cancellation or adjustment**: The exchange cancels or reprices the stale quote (usually the one on the slower venue) to restore normalcy.
3. **Halt**: In rare cases, the exchange halts trading for a few seconds to allow all venues to synchronize.
4. **Defer**: Under Reg NMS, if the exchange can demonstrate it's working to fix a technical issue, it can defer the correction window.

Modern market data systems feed all exchanges' quotes in near-real-time, so the quoted spread (the National Best Bid and Offer, or NBBO) reflects the best prices across all venues. But there's still a small window where latency can cause a cross.

## Practical Impact for Traders

For retail traders using [market orders](/market-order/) or executing through a broker, crosses and locks are largely invisible. Your broker routes your order to the exchange with the best price, and the order executes at a single price.

For [algorithmic traders](/algorithmic-trading/) and market makers, a momentary cross can be an opportunity or a trap:

- **Opportunity**: An algorithm can detect a cross and instantly buy at the crossed ask and sell at the crossed bid, arbitraging the misquote.
- **Trap**: If the cross corrects immediately (which it usually does), the arbitrageur's buy might execute but the sell might not, leaving them holding inventory.

High-frequency traders have invested heavily in systems to detect and exploit temporary crosses and locks, but the payoff is usually tiny (a fraction of a cent) and the window is extremely narrow.

## The Broader Market Structure Issue

Crossed and locked markets are symptomatic of a fundamental challenge: U.S. equity markets are fragmented across many venues, and perfect synchronization is impossible. Each exchange operates independently and quotes its own prices. The consolidated quote feed (NBBO) does its best to aggregate the best prices, but latency means that the public-facing quote is always slightly stale relative to what's happening on individual exchanges.

Some observers argue that a single, centralized exchange would eliminate crosses and locks. Others counter that competition among exchanges is more important than perfect synchronization, and that brief, rare crosses are an acceptable cost of market fragmentation.

Reg NMS strikes a balance: it allows multiple exchanges to operate but requires them to behave as if they're synchronized. Crosses and locks that persist longer than 1 second are fined heavily, incentivizing exchanges to invest in low-latency systems.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid Ask Spread](/bid-ask-spread/) — the normal price gap between bid and ask
- [Market Order](/market-order/) — orders that execute at the ask (for buys) or bid (for sells)
- [Limit Order](/limit-order/) — orders that specify a price and are subject to locking/crossing
- [Market Maker Trading](/market-maker-trading/) — the activity that typically restores normal spreads
- [T+1 Settlement Explained](/t-plus-one-settlement-explained/) — settlement mechanics unaffected by crossing

### Wider context

- [Stock Exchange](/stock-exchange/) — the venues where locking and crossing occur
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — author of Regulation NMS
- [Algorithmic Trading](/algorithmic-trading/) — systems that try to exploit temporary crosses
- [Price Discovery](/price-discovery/) — the broader function of markets that crosses temporarily disrupt

</div>
