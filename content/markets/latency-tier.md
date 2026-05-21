---
title: "Latency Tier"
description: "A latency tier is a measurement of the time delay between a market event and when information about that event reaches a trader. Latency tiers range from microseconds (high-frequency trading) to seconds (retail). Lower latency provides trading advantages but requires expensive infrastructure."
keywords:
  - latency
  - trading speed
  - microsecond
  - millisecond
  - high-frequency trading
  - execution speed
image: "https://picsum.photos/seed/latency-tier/900/600"
---

*The **latency tier** of a trader refers to the speed at which market information reaches them and orders are executed. Latency is measured in microseconds (μs), milliseconds (ms), and seconds. High-frequency traders operate in the 10–1,000 microsecond range; institutions typically experience 1–100 millisecond latencies; retail investors may see second-level delays. Reducing latency by even microseconds can mean the difference between profit and loss.*

<div class="wiki-hatnote">

This entry is about speed tiers in trading. For the infrastructure enabling it, see [colocation](/colocation-detail); for the data feeds supporting it, see [direct market data feed](/market-data-feed-direct).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Latency Tier — key facts</div>

<img src="https://picsum.photos/seed/latency-tier/900/600" alt="A latency timeline showing microseconds to seconds on a logarithmic scale" />

<div class="wiki-infobox-caption">Latency determines trading advantage in modern markets.</div>

|   |   |
|---|---|
| **Ultra-low (HFT)** | 10–100 microseconds |
| **Low (institutional)** | 100–1,000 microseconds |
| **Medium (active trader)** | 1–10 milliseconds |
| **High (retail)** | 10–1,000 milliseconds |
| **Very high (delayed data)** | 1–15 seconds or more |
| **Cost of infrastructure** | Higher speed = higher cost |
| **Advantage magnitude** | Microseconds can mean thousands/millions in profit |

</aside>

## Latency components

Total latency has multiple components:

1. **Market latency:** Time for the exchange to execute an order (typically 1–10 microseconds for orders that can be matched immediately).
2. **Network latency:** Time for data to travel from the exchange to the trader's system (typically 0.1–10 milliseconds).
3. **Processing latency:** Time for the trader's algorithm to process data and generate an order (typically 0.1–10 milliseconds).
4. **Transmission latency:** Time to send the order from the trader's system back to the exchange (typically 0.1–10 milliseconds).

Total end-to-end latency might be 1–100 milliseconds or more for most traders.

## Latency tiers and trading styles

**Ultra-low latency (10–100 microseconds):** High-frequency traders. Infrastructure at this level is expensive (servers co-located at exchanges, specialized networking, custom code). Profits come from microsecond-level advantages.

**Low latency (100–1,000 microseconds = 0.1–1 millisecond):** Sophisticated institutions and algorithmic traders. Achievable with quality infrastructure and direct exchange connections.

**Medium latency (1–10 milliseconds):** Active traders and institutions without ultra-low-latency infrastructure. This is typical for most institutional traders.

**High latency (10–1,000 milliseconds = 0.01–1 second):** Retail traders using standard brokers. Brokers themselves may route orders quickly, but the retail client's connection may add delays.

**Very high latency (1–15+ seconds):** Delayed data users. Free market data often has a 15-minute delay; some reports are even older.

## Latency arbitrage

Latency differences create trading opportunities:

**Example:** A stock trades at $100 on the NYSE and $100.05 on NASDAQ. A high-frequency trader with direct feeds from both venues might:

1. See the price discrepancy (1 millisecond).
2. Buy on NYSE at $100.00 (2 microseconds).
3. Sell on NASDAQ at $100.05 (2 microseconds).
4. Profit $0.05 per share (say, 1,000 shares = $50).

A retail investor with 1-second latency cannot execute this arbitrage; by the time they see the prices, they have moved.

## Controversy and fairness

Latency advantages are controversial:

**Arguments in favor:**
- Speed encourages market-making and liquidity.
- Technology investment is rewarded.
- Information is still ultimately available to all.

**Arguments against:**
- Creates information asymmetry; fast traders see prices before slow ones.
- Enables predatory strategies (front-running, spoofing).
- Disadvantages retail investors who cannot afford low-latency infrastructure.
- Contributes to flash crashes and volatility.

## Infrastructure costs

Achieving lower latency requires expensive infrastructure:

- **Servers and software:** Custom-built systems optimized for speed. Cost: $100,000–$1,000,000+.
- **Co-location:** Placing servers at exchange data centers to minimize network latency. Cost: $10,000–$100,000+ per year.
- **Direct feeds:** Subscribing to exchange market data feeds. Cost: $1,000–$10,000+ per month.
- **Network:** High-quality, dedicated network connections. Cost: $10,000–$100,000+ per year.
- **Total system cost:** A full high-frequency trading setup: $1–$10 million or more.

This cost structure means that ultra-low-latency trading is accessible only to well-capitalized firms.

## Measures of latency

**Absolute latency:** Total time from market event to trader decision (e.g., 5 milliseconds).

**Relative latency:** Latency difference between two traders or systems (e.g., "Firm A has 2ms advantage over Firm B").

**Latency distribution:** Typical latencies vary; traders care about the *worst-case* (tail) latencies as much as average.

## Regulation and latency

Regulators have discussed whether to mandate uniform latency or slow down fast traders:

- **No direct regulation.** The SEC has not mandated specific latency targets.
- **Indirect regulation.** [SIP](/sip-securities-information-processor) data is slower than direct feeds, but this is not a formal constraint.
- **Proposed solutions.** Some propose speed bumps (artificial delays to eliminate sub-microsecond advantages) or faster SIPs.

However, no major regulatory changes have materialized.

## Latency and market stability

During flash crashes and volatile episodes, latency differences can exacerbate volatility:

- Fast traders see cascading bids disappearing and hit bids aggressively.
- Slow traders are still seeing outdated prices.
- By the time slow traders' orders execute, prices have moved sharply.

This can lead to disorderly markets and execution at irrational prices.

## See also

<div class="wiki-seealso">

### Closely related

- [Colocation](/colocation-detail) — enables low latency
- [Direct market data feed](/market-data-feed-direct) — low-latency data source
- [High-frequency trading](/stock-market) — depends on low latency
- [SIP](/sip-securities-information-processor) — slower than direct feeds
- [Order routing](/stock-market) — affected by latency

### Wider context

- [Market microstructure](/stock-market) — latency shapes this
- [Price discovery](/stock-market) — affected by latency differences
- [Liquidity](/secondary-market) — provided by low-latency traders
- [Volatility](/bull-market) — exacerbated by latency disparities
- [Fair execution](/broker) — latency creates fairness concerns

</div>
