---
title: "Stock Exchange Co-Location Explained"
description: "Exchange co-location allows high-frequency traders to place servers inside exchange data centers, reducing message latency and improving execution speed—raising fairness concerns."
keywords:
  - stock exchange co-location
  - exchange co-location latency
  - hft co-location
  - high-frequency trading advantage
  - exchange data center proximity
image: /svg/institutions.svg
---

*Exchange **co-location** is the practice of renting rack space in an exchange's data center to house trading servers, dramatically cutting the time it takes to receive market data and send orders. High-frequency traders pay significant premiums—often $10,000–$50,000 per month or more—for proximity to matching engines, turning microseconds of latency advantage into profitable trading strategies. This arrangement has become a flashpoint in fairness debates, because it creates a tiered playing field where only well-capitalized [algorithmic trading](/algorithmic-trading/) firms can afford to sit at the exchange's door while others trade from remote locations.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Exchange Co-Location — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Proximity to market data and order routing confers measurable latency advantage.</div>

|   |   |
|---|---|
| **Purpose** | Reduce round-trip latency to matching engine |
| **Typical latency gain** | 1–100 microseconds vs. remote trading |
| **Monthly cost range** | $10,000–$100,000+ depending on rack size |
| **Who uses it** | High-frequency trading firms, large market makers |
| **Regulatory status** | Permitted but heavily scrutinized |
| **Fairness debate** | Creates two-tier market; may disadvantage retail traders |
| **Alternative** | Direct market access from remote locations (slower) |

</aside>

## How Co-Location Works

When a high-frequency trading (HFT) firm rents co-location space, it places physical servers in the same data center (or on the same floor) as the exchange's matching engine. The firm's trading algorithms run on these servers, receiving market data directly from the exchange's feed and sending orders to the matching engine through the shortest possible network path. Instead of routing market data and orders across the internet (typically 5–50 milliseconds of round-trip delay), co-located servers experience single-digit or even sub-millisecond latencies.

The exchange sells co-location as a premium service. It may offer tiered packages: basic co-location with a single 1-gigabit connection, premium co-location with redundant 10-gigabit connections, or custom buildouts for the largest trading operations. Some exchanges lease space not just for primary trading servers but for backup disaster-recovery systems, ensuring that HFTs never lose their proximity advantage.

## Latency Arbitrage and Profitability

The latency advantage is not academic. Consider a scenario: a security is trading on both the [NYSE](/new-york-stock-exchange/) and NASDAQ. A co-located trader at NYSE sees a price move one millisecond before a trader operating from a remote office. In that millisecond, the co-located firm can:

- See an order imbalance forming on NYSE
- Immediately post a contrary order on NASDAQ (or elsewhere) at a slightly better price
- Capture the tiny spread as the two prices converge

For strategies involving multiple venues, hundreds of securities, or statistical arbitrage across correlated instruments, this microsecond-level speed compounds into millions of dollars in annual profit. The co-location fee is trivial relative to the payoff.

Not all HFT strategies depend equally on latency. Some firms specialize in market making and benefit hugely from being first to update their quotes. Others focus on statistical arbitrage or pair trading and are less sensitive to sub-millisecond speed.

## Market Fairness and Regulatory Concerns

The core fairness critique is simple: a two-tier market has emerged. Retail traders and smaller institutional firms, executing from home offices or via a broker, face 10–100+ milliseconds of latency. They are, in effect, trading stale prices relative to co-located HFTs that have already reacted to fresh market data. This creates an informational disadvantage that large HFTs exploit systematically.

The SEC has acknowledged this concern. In 2010, it proposed rules to ensure that all market participants have "fair and equal" access to market data and order-entry systems. While some rules were adopted (e.g., ensuring that collocated firms do not receive data before public dissemination), the SEC stopped short of banning co-location itself or mandating uniform latency for all traders.

Some critics argue that co-location amounts to a subtle violation of market integrity: by paying for proximity, HFTs gain a front-running advantage that, while technically legal, undermines the fairness premise of a stock exchange. Others note that co-location is a direct reflection of market competition—if all firms had access to the same speed, competition would drive fees down and profitability would evaporate, eliminating HFT's incentive to invest in fast infrastructure. There is genuine disagreement among economists and policymakers on this question.

## Regulatory Framework and "Flash Crash" Aftermath

The 2010 flash crash and subsequent "Flash Boys" controversy (2014) put co-location in the political spotlight. Michael Lewis's book alleged that HFTs using co-location and advanced algorithms could prey on mutual funds and pension funds with slower execution. While later analysis showed that HFT was not the primary driver of the flash crash, the reputational damage stuck.

The SEC responded with circuit breakers, order-cancellation periods, and the short-sale rule to slow volatility. But co-location itself was not banned or significantly constrained. Instead, the SEC has focused on ensuring that co-location services are offered on a non-discriminatory, best-efforts basis and that collocated firms do not receive data in advance of the public.

## The Cost-Benefit Calculus for Exchanges

For exchanges, co-location is a significant revenue stream. NYSE, NASDAQ, and regional exchanges each operate data-center facilities and lease space to thousands of trading firms. This real-estate revenue is predictable and high-margin—once a rack is rented, the exchange collects monthly fees with minimal incremental cost. It is also a sticky business: once a HFT firm invests in co-location, moving to a competitor exchange is expensive and operationally complex.

However, exchanges face criticism for creating a conflict of interest: they profit from co-location while also operating the matching engine and owning market-data feed. This raises the question of whether exchanges have an incentive to subtly favor co-located firms—e.g., by prioritizing collocated orders, providing earlier data access, or structuring fee schedules to incentivize co-location.

## Alternatives and Competitive Pressure

Not all trading firms use co-location. Some retail brokers use batch-matching technology or offer fractional-second latency that is fast enough for most retail strategies. Decentralized exchanges, cryptocurrency venues, and alternative trading systems have experimented with latency-neutral designs, where all orders are subject to the same message delay, eliminating latency arbitrage.

The rise of passive investing and index funds has also reduced the relevance of co-location for some segments of the market. If an investor is simply buying an S&P 500 index fund, the microsecond-level latency at which their order is executed is irrelevant; what matters is execution quality and fees, not speed.

## See also

<div class="wiki-seealso">

### Closely related

- [Algorithmic Trading](/algorithmic-trading/) — the discipline that leverages co-location advantage
- [Market Maker Trading](/market-maker-trading/) — the primary use case for co-located systems
- [High-Frequency Trading](/high-frequency-trading/) — the player class that dominates co-location
- [Stock Exchange](/stock-exchange/) — the operator and beneficiary of co-location fees
- [Price Discovery](/price-discovery/) — mechanism potentially distorted by latency asymmetry
- [Execution Risk](/execution-risk/) — latency-related risk in order execution

### Wider context

- [Alternative Trading System](/alternative-trading-system/) — competitor venues with different latency models
- [Bid-Ask Spread](/bid-ask-spread/) — spread captured by latency-advantaged traders
- [Market Order](/market-order/) — execution method vulnerable to latency disadvantage
- [Nasdaq](/nasdaq/) — major exchange operating co-location facilities

</div>
