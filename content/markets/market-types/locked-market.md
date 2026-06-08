---
title: "Locked Market"
description: "A market condition where the national best bid equals the national best offer, signalling crossed quotes or extreme quote compression."
keywords:
  - bid-ask spread
  - market anomaly
  - quote compression
  - market efficiency
  - trading frictions
image: "/svg/markets.svg"
---

*A **locked market** occurs when the best ask price exactly equals the best bid price across all trading venues for a security—the bid-ask spread compresses to zero. This anomaly signals either extremely tight competition, a data latency issue, or a crossed-quote condition that forces market participants to act quickly to correct the pricing imbalance.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Locked Market — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market structure and trading venues." />

<div class="wiki-infobox-caption">A visible symptom of market fragmentation and the speed-of-light arms race in modern equity trading.</div>

|   |   |
|---|---|
| **What it is** | National best bid equals national best ask (spread = 0) |
| **Also called** | Zero spread, crossed quote, inverted bid-ask |
| **Duration** | Milliseconds to seconds; rarely persists longer |
| **Cause** | Data latency, quote refresh delay, aggressive competition |
| **Trading implication** | Arbitrage opportunity; usually requires limit orders to capture |
| **Regulatory status** | Permissible but temporary; brokers must post quotes correctly |
| **Frequency** | Common in large-cap, liquid stocks; rare in small-cap |

</aside>

## The mechanics of bid-ask compression

Under normal conditions, a stock has a positive [bid-ask spread](/bid-ask-spread/). If Apple trades $150.00 bid / $150.05 ask, that $0.05 spread represents the cost of immediacy. A buyer willing to wait can place a limit order at $150.00; a seller willing to wait can bid $150.04 and wait for a fill. The spread is where [market makers](/market-maker-trading/) capture profit for providing liquidity.

A locked market occurs when this spread collapses to zero: the national best bid is $150.00 and the national best ask is also $150.00. At that price, no transaction can occur—a buyer and seller at the same price would have already traded. The moment the bid and ask are equal, the lock persists only until one of three things happens: a transaction occurs, a [market maker](/market-maker-trading/) posts a tighter quote, or a quote refresh occurs on another venue.

Locked markets are neither illegal nor inherently irrational. They reflect the extreme liquidity and quote-posting speed of modern U.S. equity markets. In the past, locks were rare because quotes updated slowly and manually. Now, with algorithmic trading and [market makers](/market-maker-trading/) refreshing quotes in milliseconds, locks happen dozens of times daily in large-cap stocks, often lasting only a few milliseconds before resolution.

## Why locks happen: fragmentation and data latency

The root cause of locked markets is market fragmentation combined with imperfect information. The National Best Bid and Offer (NBBO) is supposed to reflect the best available prices across all trading venues—the [New York Stock Exchange](/new-york-stock-exchange/), [NASDAQ](/nasdaq/), regional exchanges, and [alternative trading systems](/alternative-trading-system/). But "best" is only as good as the data that feeds it.

Market data moves at the speed of light, but not instantly. Different venues post quote information at different times and on different networks. A venue on the East Coast and one on the West Coast have a 15-millisecond latency gap just from the physical distance between them. During that window, a [market maker](/market-maker-trading/) on one venue might post a bid at $150.00 while one on another posts an ask at $150.00, both unaware of each other's quote. The consolidated data system that publishes the NBBO sees both and locks.

More commonly, locks occur because of aggressive competition. If one venue's market maker posts a bid at $150.00, another market maker wanting to attract buy orders might immediately post an ask at $150.00, hoping to undercut everyone else. For a microsecond, the market is locked. Then a trader hits that ask, it clears, and the market maker posts a new quote slightly higher, unlocking the market.

This is normal high-frequency trading behavior. The speed at which quotes are posted and cancelled—sometimes millions of quotes per second across all stocks—makes locks inevitable statistically. They are the friction that speed creates.

## The trader's dilemma in a locked market

A locked market presents a puzzle for traders. If the bid and ask are both $150.00, where is the next trade? There are three possibilities:

One: a transaction at $150.00 clears one side of the lock. Someone had a standing limit order at $150.00 to buy or sell, and it matches against the other side.

Two: a [market maker](/market-maker-trading/) posts a new quote that widens the spread. One venue's market maker posts a bid at $149.99, unlocking the market upward, or an ask at $150.01, unlocking downward. The trader who wants to buy now faces a choice: accept the new ask, or wait for another lock or movement.

Three: the lock resolves due to a quote refresh or cancellation. If a quote is withdrawn, the NBBO recalculates using the remaining venues' quotes, and the lock breaks.

Traders cannot directly profit from a lock because there is nowhere to trade at that price. But a lock often signals extreme demand on one side. If the market is locked at $150.00, it means both buyers and sellers are willing to transact at that price—a signal of price equilibrium. The next price move is uncertain; it depends on new information or the balance of supply and demand just above and below that price.

Some high-frequency traders try to detect locks as signals of extreme liquidity and position ahead of them, betting that a micro-movement will follow. But locks are so fast and numerous in large-cap stocks that consistent profit from lock-following is difficult without significant technological advantage.

## Locks in the context of market quality

Paradoxically, locked markets are often a sign of market efficiency and tight competition—not dysfunction. A zero spread means [market makers](/market-maker-trading/) are aggressive and price discovery is sharp. In thinly traded stocks, where [market makers](/market-maker-trading/) are rare and demand is asymmetric, spreads remain wide because there is less incentive to post tight quotes.

However, locks can also signal temporary problems. If a large-cap stock is locked for more than a second or two, it might indicate a data feed problem, a venue outage, or a circuit breaker event. The SEC has rules around locked markets; brokers are not supposed to post quotes that would lock the market, and when a lock is detected, traders must act quickly to resolve it or notify regulators.

The concern about locks is more subtle than dysfunction. Because locks are so common in modern markets, traders relying on the NBBO to make decisions might think prices are tighter than they actually are. A retail trader looking at a $150.00 / $150.00 quote might think they can buy and sell at the same price, but by the time they act, the quote has moved. This is not a problem with locks per se, but with the latency between quote publication and actual execution.

## The regulatory and practical fix

In practice, brokers and exchanges have adapted to locks by monitoring them closely. Rules require that if a broker posts a quote that would lock the market, it must be cancelled or adjusted within a short time. [Alternative trading systems](/alternative-trading-system/) have rules preventing locked quotes from persisting. The SEC's Regulation SHO also addresses locked and crossed markets by requiring market participants to execute orders promptly when the market locks.

Large institutional traders and algorithmic systems simply treat locks as noise and work around them. They break large orders into smaller pieces, use execution algorithms that react to locked markets, and trade directly with [market makers](/market-maker-trading/) off-venue when locks make public exchanges inefficient.

For most retail traders, locked markets are invisible. Their brokers aggregate quotes, hide the complexity, and execute orders at prices that reflect the aggregated liquidity. The lock is a millisecond-level phenomenon that the broker's routing engine handles automatically.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the pricing margin that compresses to zero in a locked market
- [Market maker](/market-maker-trading/) — the intermediaries who post quotes that cause locks
- [Market order](/market-order/) — immediate execution that must navigate locked or tight markets
- [Limit order](/limit-order/) — standing orders that trigger transactions during locks
- [Price discovery](/price-discovery/) — how locked markets reflect price equilibrium
- [Alternative trading system](/alternative-trading-system/) — venues where locked quotes are monitored and corrected

### Wider context

- [Stock exchange](/stock-exchange/) — the venues that post quotes contributing to the NBBO
- [Over-the-counter market](/over-the-counter-market/) — unlit market without the same NBBO synchronization
- [Internal market](/internal-market/) — broker-internal execution that avoids exchange locks
- [One-sided market](/one-sided-market/) — the opposite condition where only bids or asks exist

</div>
