---
title: "How High-Frequency Trading Earns Rebates"
description: "How high-frequency trading earns rebates by providing liquidity: the rebate structures exchanges use to attract market makers and how HFT firms scale across venues."
keywords:
  - high-frequency trading rebates
  - market-making rebates
  - maker-taker fee model
  - exchange liquidity incentives
  - latency arbitrage
  - venue rebates
---

*High-frequency trading firms earn rebates by acting as **market makers**—posting limit orders that attract other traders—and by exploiting the speed advantage to capture tiny price differences across venues. Exchanges pay these rebates to attract liquidity providers who keep bid-ask spreads tight and ready capital available.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">HFT Rebates — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Rebates are the exchange's payment to you for reducing spreads and improving price discovery.</div>

|   |   |
|---|---|
| **What triggers it** | Posting a limit order that executes against a market order (the taker) |
| **Typical rebate size** | $0.0001–$0.0005 per share (varies by venue and asset) |
| **Who earns them** | [Market makers](/market-maker-trading/) and HFT firms with high order volume |
| **The opposite cost** | Taker fees: what you pay to execute immediately at the posted price |
| **Revenue scale** | Earned on millions of shares daily across multiple venues |
| **Competition** | Rebates incentivize speed and venue fragmentation |

</aside>

## The maker-taker rebate model

Every time you submit a market order, you pay a fee to hit someone else's limit order. That someone—the market maker who posted first—gets rebated by the exchange. The exchange captures a small spread: the taker pays 0.0005 per share, the maker gets rebated 0.0004, and the exchange nets 0.0001. This simple mechanic invented in the 2000s transformed equity markets into a game of speed and scale.

High-frequency traders exploit this by running algorithms that post and cancel orders at machine speed, capturing maker rebates on fills while avoiding taker fees on canceled orders. The goal: fill enough limit orders at favorable prices to generate aggregate rebate income that exceeds their technology and facility costs.

## How HFT firms qualify for rebates

Most U.S. stock exchanges—NASDAQ, NYSE, ARCA, and others—publish tiered rebate schedules that scale with volume. A firm might earn 0.0001 per share on its first 10 million shares monthly, then 0.0002 on shares 10–50 million, and higher still at platinum volume tiers. This creates raw incentive: post more limit orders that execute, climb the tier, earn fatter rebates.

To maximize rebate earnings, HFT firms:

- **Post high volumes across multiple venues.** If the same stock trades on NASDAQ, NYSE, and ARCA, an HFT can post on all three, ensuring that when a macro trader moves, they hit one of the HFT's limit orders somewhere. Each fill is a rebate.
- **Hold inventory briefly.** Market makers buy slightly below mid-market and sell slightly above to capture the spread, plus the rebate on the buy-side fill. The position lasts milliseconds.
- **Optimize for rebate-positive orders.** Algorithms learn which order types, sizes, and venues trigger the largest rebates relative to adverse selection risk (the risk that prices move against them while holding inventory).

## Latency arbitrage as rebate amplification

Beyond raw market-making, HFT rebate revenue explodes when firms gain information faster than competitors. A classic example: a large institutional buyer places a buy order on NASDAQ. An HFT with faster data feeds and colocation sees the order microseconds before other traders, immediately posts sell limit orders on competing venues (ARCA, NYSE), and captures maker rebates as the institutional order sweeps across venues looking for liquidity.

This is not illegal, but it is controversial. The HFT earned rebates partly by seeing the order first—speed, not just tighter spreads. Critics argue that rebate-driven latency arbitrage extracts wealth from slower traders who pay taker fees to chase liquidity across venues.

## The volume and venue fragmentation spiral

Rebate schedules have accelerated market fragmentation. In the 1980s, most stocks traded on a single exchange (NYSE). Today, a single stock may trade on 13+ venues. Why? Exchanges compete by offering increasingly generous rebate schedules to attract market makers. Market makers respond by spreading volume across venues to hit rebate targets. Retail order flow attracts wholesale market makers, who then demand rebate improvements to stay competitive.

A typical large-cap HFT might earn:

| Venue | Daily shares | Rebate per share | Daily rebate |
|-------|--------------|------------------|--------------|
| NASDAQ | 2,000,000 | $0.00025 | $500 |
| NYSE | 1,500,000 | $0.00020 | $300 |
| ARCA | 1,000,000 | $0.00020 | $200 |
| **Total** | **4,500,000** | **avg. 0.00022** | **$1,000** |

Multiply that across thousands of stocks and you see why rebates fund the infrastructure arms race.

## Limits and trade-offs

Not all HFT strategies are rebate-positive. A firm that posts orders just to avoid taker fees (earning tiny rebates) while bearing inventory risk will lose money on adverse price moves. The skill lies in balancing:

- **Fill rate:** Post aggressively to capture rebates, but risk being left holding when prices gap.
- **Adverse selection:** Market makers lose on informed orders (someone buying because they know price will rise). Rebate income must exceed these losses.
- **Regulatory scrutiny:** The SEC and FINRA monitor order cancellation rates. Firms that post and cancel 99.9% of orders face sanctions, even if statistically profitable.

In 2024, after a wave of fines for spoofing and layering, HFT firms have become more cautious about posting volume purely to game rebate tiers. Many now focus on venues with looser volume thresholds and higher rebate percentages, or shift toward options and futures (where rebate models differ).

## The institutional impact

For retail and institutional traders, rebate-fueled fragmentation has a dual effect. Tight bid-ask spreads on each venue (a benefit of rebate-driven liquidity) are offset by the need to route orders across multiple venues to find the best prices. A passive index fund buying 100,000 shares might execute at a slightly better mid-price, but spreads are thinner because market makers earn rebates for posting.

The [price discovery](/price-discovery/) benefit is real: tight spreads mean bid-ask elastic, and prices more accurately reflect underlying value. The question is whether this efficiency gain offset the wealth extraction from informed traders chasing liquidity under speed disadvantage.

## See also

<div class="wiki-seealso">

### Closely related

- [Market maker trading](/market-maker-trading/) — how market makers profit from spreads and rebates
- [Bid-ask spread](/bid-ask-spread/) — the gap between buy and sell prices that rebates help tighten
- [Alternative trading system](/alternative-trading-system/) — dark pools and off-exchange venues with different rebate incentives
- [Latency arbitrage](/how-high-frequency-trading-earns-rebates/) — speed advantage in capturing cross-venue price differences
- [Stock exchange](/stock-exchange/) — the venues where rebate schedules attract liquidity

### Wider context

- [Algorithmic trading](/algorithmic-trading/) — automated strategies that exploit rebate opportunities
- Market microstructure — how order flow, spreads, and venues interact
- [Fragmented market](/fragmented-market/) — the proliferation of trading venues and liquidity pools
- [Execution risk](/execution-risk/) — the cost of routing orders across venues

</div>
