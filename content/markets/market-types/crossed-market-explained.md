---
title: "Crossed Market Explained"
description: "A crossed market occurs when the best bid exceeds the best ask, violating normal pricing. Explains causes, risks, and how it signals fragmentation or data errors."
keywords:
  - crossed market explained
  - what is a crossed market
  - bid higher than ask
  - market fragmentation crossed
  - trading market conditions
  - locked market vs crossed
---

*A **crossed market** exists when the highest price someone is willing to pay (the best bid) exceeds the lowest price someone is willing to sell at (the best ask). In a properly functioning market, the bid is always lower than the ask. When they cross, it signals either a data error, extreme fragmentation across exchanges, or a temporary breakdown in market coordination.*

## The Normal Bid-Ask Spread

Under normal conditions, a stock or security has a [bid-ask spread](/bid-ask-spread/). The bid is the highest price a [market maker](/market-maker-trading/) or buyer will offer; the ask is the lowest price a seller will accept. A stock might trade with a $100 bid and a $100.05 ask. The 5-cent spread is the cost of immediate execution and the market maker's profit.

The spread exists because of [price discovery](/price-discovery/), inventory risk, and the cost of providing liquidity. A buyer who needs to execute immediately pays the ask; a seller who needs to exit immediately accepts the bid. Both pay a small friction to avoid waiting.

When bid is below ask, markets are orderly. No crossed wires, no paradoxes.

## How Crossovers Occur

Crossed markets arise in a few ways:

**Multiple Exchanges and Data Latency**: A security may trade on many venues—NYSE, Nasdaq, regional exchanges, alternative trading systems (ATS), even overseas. Each publishes its own bid and ask. A system consolidating these quotes into a "national best bid and offer" (NBBO) may lag. The NYSE publishes a $100 bid at time T, and Nasdaq publishes a $100.05 ask, but by time T+50 milliseconds, Nasdaq has updated to $100.02 and the NYSE to $100.04. If a data consumer's system is slightly out of sync, it may see the NYSE bid and old Nasdaq ask in the wrong order.

**Algorithmic Spikes**: A rogue algorithm might place an enormous buy order at a stale or incorrect price. If it gets partially filled before being canceled, it can momentarily create a crossed market on the aggregated feed.

**Circuit Breaker Delays**: When a stock halts for news, one exchange may resume trading before others. The resumed exchange's new quotes may cross older quotes still showing from the halted exchange.

**Fat Finger Errors**: A trader enters a vastly incorrect order (e.g., selling 1,000 shares at $1 instead of $100). If executed before cancellation, it can cascade into imbalances that create crossed markets momentarily.

**Manual Data Issues**: In some over-the-counter (OTC) markets or thinly traded securities, quotes are posted manually or via fragmented systems. A stale bid from one venue might exceed a fresh ask from another.

## Crossed vs. Locked

A **locked market** is when bid and ask are at the same price—a $100 bid and a $100 ask. This is unusual and signals a temporary supply-demand imbalance or a system glitch. Orders may queue or settle quickly once the imbalance resolves.

A **crossed market** is worse: bid is actually above ask. It's a clear violation of market logic and almost always a sign of a technical problem, not a fundamental mismatch.

Regulators and exchanges actively monitor for crossed markets. The SEC requires [brokers](/broker/) and market participants to avoid executing trades that would create or widen a crossed market, and execution quality rules penalize firms that execute at crossed prices when a better bid-ask existed on another venue.

## What It Signals

A crossed market indicates one of several breakdowns:

1. **Exchange or Data Fragmentation**: Multiple venues publishing conflicting information. Most common in volatile periods or after news, when exchanges struggle to synchronize.

2. **Liquidity Evaporation**: During fast market conditions, buy and sell orders may not be meeting at any price. The best bid and ask widen, potentially even crossing if sequencing is off.

3. **System Failures**: A quote feed is stale, a circuit breaker has paused one venue, or an algorithm has misfired.

4. **Regulatory Halt**: If a stock is halted for news, the last bid-ask from before the halt may still be quoted while the first quote after the halt is printed. The two might cross.

## Risks for Traders

If you rely on a crossed market quote to make a decision, you may:

- Place an order at an impossible price, mistakenly believing it reflects fair value.
- Miss the actual market price because your data is stale.
- Face execution issues if your broker or venue refuses to trade at crossed prices (as they should).

Most retail [brokers](/broker/) and [market makers](/market-maker-trading/) will not allow you to execute at a crossed price. Modern market data systems also flag and exclude crossed quotes in real time. However, in fragmented or illiquid markets, especially OTC or penny stocks, crossed quotes can persist briefly, creating confusion.

For algorithmic and high-frequency traders, crossed markets are noise to ignore. Their systems automatically detect and filter them. For active traders relying on manual quotes, a crossed market is a warning sign to pause and verify the data source.

## How Exchanges Prevent Them

Exchanges enforce rules like:

- **Automatic Execution**: If a buy order crosses a sell order on the same venue, they execute immediately at the cross price.
- **Inter-Market Sweep Orders (ISO)**: A rule allowing traders to buy at a higher ask on one venue if, simultaneously, they sweep (cancel or accept) lower bids on all other venues, ensuring the best bid-ask is always honored.
- **Quote Throttling**: Limiting stale quotes to prevent old data from crossing new data.
- **Circuit Breakers**: Pausing trading in a security to allow all venues to synchronize.

These rules have mostly eliminated persistent crossed markets. When they appear, exchanges and regulators investigate and often halt or suspend trading in the affected security until normalcy is restored.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — The normal gap between bid and ask, and what drives it
- [Fast Market Conditions in Stock Trading](/fast-market-conditions/) — When markets become volatile and quotes become less reliable
- [Market Maker (Trading)](/market-maker-trading/) — How market makers provide liquidity and maintain quotes
- [Alternative Trading System](/alternative-trading-system/) — Venues beyond the main exchanges where securities trade
- [Price Discovery](/price-discovery/) — How prices form and converge across markets

### Wider context

- [Stock Exchange](/stock-exchange/) — How exchanges operate and set rules
- [Market Order](/market-order/) — Executing at the market price (whatever it is)
- [Limit Order](/limit-order/) — Specifying a price and waiting for a match
- [Over-the-Counter Market](/over-the-counter-market/) — Decentralized trading outside formal exchanges
- [Market Risk](/market-risk/) — Broader risks in trading and investing

</div>
