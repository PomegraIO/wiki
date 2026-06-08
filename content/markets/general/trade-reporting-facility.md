---
title: "Trade Reporting Facility"
description: "Systems operated by FINRA where brokers must report equity trades executed off the lit exchanges."
keywords:
  - trf
  - trade reporting
  - otc equities
  - finra
image: "/svg/markets.svg"
---

*A **Trade Reporting Facility** (TRF) is a system administered by the Financial Industry Regulatory Authority (FINRA) that collects and publishes information about equity trades executed away from lit exchanges—typically in over-the-counter venues or [alternative trading systems](/alternative-trading-system/). Brokers must report completed trades to the TRF within strict timeframes, ensuring that the public gains visibility into price discovery across the entire market, not just exchange-listed transactions.*

## Why OTC trades need reporting

Before the TRF system, equity trades executed in OTC or "fourth market" channels went largely unrecorded. A broker might execute a 50,000-share block off-exchange with no public record of the trade price, size, or timing. This opacity meant that investors relying on public price quotes saw only exchange transactions, missing a substantial portion of actual market activity.

For popular stocks, this mattered enormously. A significant fraction of trading volume occurred off-exchange, in brokers' internal crossing networks, or between institutions. Market makers and algorithmic traders could exploit this information: they knew OTC trades that the public did not, and could adjust their exchange quotes accordingly. The [bid-ask spread](/bid-ask-spread/) on the exchange might not reflect the true market price if dark liquidity pools were consistently executing at better prices.

## The structure and timeline

FINRA operates three TRFs: two for equities (the ADF and the ORF, merged into a single entity) and the OTCBB for small-cap securities. When a trade completes off-exchange, the executing broker must report details within seconds (typically within 30 seconds of execution for equities, sooner for some venues). The report includes:

- Security identifier (ticker or ISIN)
- Price and share count
- Timestamp of execution
- Whether the trade was a buy or sell for the reporting firm (buy/sell indicator)

The TRF aggregates these reports and publishes them in real time to the public. A trader monitoring the feed can see when large blocks trade off-exchange, at what prices, and in what sequence—reconstructing a more complete picture of market flow than exchange data alone provides.

## Impact on price discovery

The TRF increased transparency and narrowed information asymmetry. Institutions and market makers could no longer exploit off-exchange price information without risk that the trades would be reported within seconds. As a result, off-exchange prices and exchange prices converged. An [alternative trading system](/alternative-trading-system/) that consistently executed at worse prices than the reported TRF midpoint would lose order flow to venues offering better execution.

However, TRF data also created new complexities. The timestamp of execution and the timestamp of reporting differ by up to 30 seconds—enough for a high-frequency trader to observe TRF data and act on it before older exchange data reaches their systems. This latency asymmetry can create arbitrage opportunities. A trade reported to the TRF today may have occurred minutes ago; an algorithmic trader seeing the report might assume the TRF price is fresher than it is.

## Block trades and conditional reporting

The SEC permits certain conditional exemptions to immediate TRF reporting. A block trade—typically defined as substantially larger than average volume—can be reported with delayed disclosure of size under "alternative reporting." For example, a 1 million-share block might be reported as executed in tranches over time, masking the full size from immediate public view. This allows institutions to execute large positions without signalling the full scope of their trading intent.

The rationale is to prevent market impact: if everyone instantly saw a 1 million-share seller, prices could move sharply before the entire block was cleared. The delay (often 24 hours) allows the seller to exit with less slippage. Critics argue this transparency delay perpetuates off-exchange trading advantages for large players, whilst retail traders see only consolidated quotes and smaller-sized on-exchange activity.

## TRF and dark pools

[Alternative trading systems](/alternative-trading-system/) that accept equity orders must report trades through the TRF. A dark pool (an ATS that does not display order books) executes trades and reports them. In this sense, the TRF is the only public visibility into dark pool activity: after execution, the trades flow through the TRF and become part of the published record.

This creates an odd dynamic. A dark pool's competitive advantage rests on the inability to see its order book in real time. But once a trade executes, it becomes public within 30 seconds. A trader can observe TRF data, infer that a dark pool executed a large sell, and anticipate the direction of [market fragmentation](/market-fragmentation/) across venues. The reported trades become a footprint the market reads.

## Regulatory oversight and compliance

FINRA audits brokers' TRF submissions for accuracy and timeliness. Incorrect reporting—wrong price, wrong timestamp, missing trades—triggers compliance actions. Systematic under-reporting or intentional delays are serious violations. Fines have reached millions of dollars for large firms that failed to report trades promptly or accurately.

The SEC also applies additional rules on top of TRF reporting. Regulation SHO and the broader Dodd-Frank Act mandate specific transparency standards. [Alternative trading systems](/alternative-trading-system/) filing with the SEC must agree to TRF reporting as a condition of operation. The TRF thus sits at the intersection of FINRA self-regulatory oversight and SEC market structure authority.

## Evolution and data challenges

The TRF system evolved in phases, starting with manual reporting in the 1990s and automating over the 2000s. Modern TRF feeds handle millions of trades daily and serve market data vendors, retail brokers, and retail platforms. The data is freely available after a brief dissemination delay, ensuring that a retail trader using a data feed can see the same reported trades as an institutional firm.

That said, reconstructing a complete market picture from TRF data alone remains difficult. Timestamps may show a trade executed at 10:00:05, but the order that filled it may have been sitting in a dark pool for ten minutes beforehand. Trades reported to the TRF represent only a final match point; the microstructure of how that order arrived at the venue is invisible.

## See also

<div class="wiki-seealso">

### Closely related

- [Alternative Trading System](/alternative-trading-system/) — venues subject to TRF reporting requirements
- [Electronic Communication Network](/electronic-communication-network/) — off-exchange systems whose trades flow through TRF
- [Over-the-Counter Market](/over-the-counter-market/) — the broader OTC space that TRF monitors
- [National Best Bid and Offer](/national-best-bid-offer/) — the consolidated best prices across lit venues
- [Market Fragmentation](/market-fragmentation/) — the fragmented landscape the TRF helps traders navigate
- [Price Discovery](/price-discovery/) — improved by TRF transparency
- [Broker](/broker/) — responsible for accurate TRF reporting

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — oversees TRF through ATS rules
- [Stock Exchange](/stock-exchange/) — the primary lit venues whose trades feed into broader market records
- [Bid-Ask Spread](/bid-ask-spread/) — tightened by TRF visibility

</div>
