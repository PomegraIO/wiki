---
title: "Flash Crash of 2010: Causes and Market Impact"
description: "What caused the flash crash of 2010: how a large S&P 500 futures order, high-frequency trading, and market fragmentation triggered a trillion-dollar drop."
keywords:
  - flash crash 2010
  - flash crash causes
  - May 6 2010 stock market crash
  - high frequency trading flash crash
  - circuit breakers stock market
  - flash crash 2010 what caused it
image: "/svg/history.svg"
---

*On May 6, 2010, U.S. equity markets experienced a **flash crash**: a near-instantaneous 9% plunge in broad indices followed by a rapid recovery, all within minutes. A single algorithmic sell order in S&P 500 [futures-contract], executed into a thin order book and amplified by high-frequency trading feedback loops, triggered a cascade that nearly wiped a trillion dollars of value before automatic circuit breakers halted the fall.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">May 6, 2010 Flash Crash — Key Facts</div>

<img src="/svg/history.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A breakdown in liquidity and speed exposed structural fragility in modern markets.</div>

|   |   |
|---|---|
| **Time duration** | ~36 minutes (2:30 p.m.–3:07 p.m. ET) |
| **Market decline** | S&P 500 fell from 1,190 to 1,056 (−9.2%) in 5–10 minutes |
| **Notional loss** | ~$1 trillion in market cap |
| **Recovery** | Most indices recovered 60% of losses by day's close |
| **Trigger order** | ~$4.1 billion sell of S&P 500 e-mini futures |
| **Execution speed** | 36-minute sell algorithm compressed into 20 minutes due to low liquidity |

</aside>

## The Setup: Fragmented Markets and Thin Liquidity

By 2010, U.S. equity trading had become fragmented across 13 exchanges and dozens of alternative trading venues. The [NASDAQ] and [New-York-Stock-Exchange] no longer dominated; a significant share of volume flowed through BATS, Direct Edge, and dark pools. This fragmentation meant that no single venue saw the full order book. Instead, traders relied on market data feeds and algorithms to stitch together a unified picture of price and volume.

High-frequency traders (HFTs) proliferated. These firms used proprietary algorithms and colocation (placing servers physically next to exchange data centers) to spot pricing discrepancies across venues and exploit them in microseconds. On many days, HFT firms accounted for 60% of volume. They were net buyers on up-ticks and net sellers on down-ticks, acting as quasi-liquidity providers—but only as long as volatility stayed low and profit margins were assured.

The S&P 500 had been rising into early May after a rebound from 2009's lows. On May 5, a bad employment report spooked the market. May 6 opened with sellers in control. European debt worries and U.S. economic data converged to create selling pressure. Volatility spiked. [Implied-Volatility] on the VIX index jumped 20%. Spreads widened.

## The Trigger: A Large Algorithmic Sell Order

At approximately 2:30 p.m., a major U.S. mutual fund or hedge fund—later identified as Waddell & Reed Financial—decided to exit a large $4.1 billion position in S&P 500 e-mini [futures-contract]. Instead of executing the order directly, the firm used an algorithm designed to minimize market impact: it would sell the notional amount gradually, matching a fixed percentage of market volume. The algorithm was not time-sensitive; it was designed to sell at a steady pace.

In normal conditions, this approach works well. The fund's shares blend into the ongoing volume, and price impact is minimal. But on May 6, two factors broke the algorithm:

1. Volumes spiked and fragmented. The algorithm's volume-matching routine couldn't find enough buyers on any single venue without significant price concessions.
2. The order was placed *during an unusually thin period*. Later analysis showed that the preceding 10 minutes had seen lower-than-typical volume. When the algorithm accelerated its selling to hit the volume-matching target, it dumped a mass of futures into a near-vacuum.

## The Cascade: Feedback Loops Unwind Liquidity

The sell pressure hit the e-mini futures contract hard. As the price dropped, two things happened:

**HFT algorithms panicked.** High-frequency traders' risk-management systems are programmed to scale back activity if losses exceed thresholds. When the e-mini futures fell 2–3%, HFT firms retreated from the market, turning off their liquidity-provision algorithms. Buy bids evaporated.

**Correlation broke down.** Normally, the S&P 500 e-mini futures and the underlying stocks track closely. When futures fall, arbitrageurs buy spot stocks and short futures to profit. But in the crush, data feeds lagged. Traders looking at real-time data couldn't see the full scope of the move. Many algorithms interpreted the futures fall as a fundamental shift and began selling stocks preemptively.

The selling spread across venues. Retail stocks, mega-cap names, and index trackers all fell together. Within five minutes, the S&P 500 was down 5%. Within ten minutes, down 9%. Some stocks fell so far so fast—hit with auto-execution from algorithmic fund liquidations—that circuit breakers on individual stocks tripped, pausing trading.

At 2:47 p.m., the SEC's Limit Up-Limit Down (LULD) rule did not yet exist (it was introduced after the crash). Without it, stocks that traded at $20 could suddenly show prints at $1 before rebounding. In this chaos, one large bank's algorithm, seeing extreme prices, began selling equities into the void. The selling snowballed.

## The Recovery and Circuit Breakers

At approximately 2:47 p.m., the e-mini futures—the leading instrument—hit a critical level and triggered a 15-minute trading halt under circuit breaker rules. This pause allowed:

1. **Market participants to step back.** Algorithms that had been running on panicked logic reset.
2. **Order books to refill.** Buyers who had pulled bids to avoid losses re-entered the market. Fundamental traders recognized the fall as excessive and began buying at discounts.
3. **Information to synchronize.** Data feeds caught up, and traders could see the true market picture again.

When trading resumed, sellers had exhausted themselves. Buy pressure returned, and indices rebounded sharply. By 3:00 p.m., most of the market was still down, but the free-fall had stopped. By the close, the S&P 500 was only about −3% for the day. Intraday gains of nearly 1,000 index points had been erased.

Volatility remained elevated for weeks, and the VIX spiked to 40. But the market had not crashed; it had been shocked and recovered.

## Root Causes Identified

The SEC's official investigation identified:

- **Inadequate circuit breakers.** The single-level circuit breaker halted the entire market, but intra-market trading halts on individual stocks were not automatic.
- **Fragmentation and tick sizes.** Small tick sizes (pennies) combined with fragmented venues made it easy for prices to fall 20–30% in seconds with no intermediate buyers.
- **Algorithmic feedback loops.** The absence of automatic safeguards meant algorithms could trigger other algorithms in a cascade.
- **Systemic liquidity illusion.** Markets appeared liquid, but that liquidity evaporated in a stress event. HFTs provided volume in calm conditions but withdrew in stress.

## Reforms: Limits Up-Limit Down and Curbs

After the flash crash, regulators implemented:

- **Limit Up-Limit Down (LULD)** trading halts on individual stocks, preventing extreme price moves.
- **Expanded circuit breakers** that halt trading if the S&P 500 falls 7%, 13%, or 20% intraday.
- **Larger minimum tick sizes** for stocks under $1.00 to increase liquidity and prevent wild swings.
- **Stress testing and firewall rules** requiring firms to test their algorithms and disconnect them if volatility exceeds thresholds.

These changes reduced the likelihood of a repeat, though they cannot eliminate the risk entirely. In 2015 and 2018, sharp intraday moves triggered circuit breakers, but trading halted and recovered calmly. The market now has more time to digest shocks.

## See also

<div class="wiki-seealso">

### Closely related

- [Algorithmic-Trading](/algorithmic-trading/) — The trading method that both triggered and amplified the crash
- [High-Frequency-Trading](/high-frequency-trading/) — The liquidity providers who withdrew in the crisis
- [Market-Risk](/market-risk/) — Systemic risk and market structure vulnerabilities
- [Circuit-Breakers](/circuit-breakers/) — The automatic halts introduced to prevent repeat crashes
- [Volatility-Smile](/volatility-smile/) — How option prices (implied volatility) reacted to the crash

### Wider context

- [Securities-and-Exchange-Commission](/securities-and-exchange-commission/) — The regulator that investigated and reformed markets afterward
- [Stock-Exchange](/stock-exchange/) — The fragmented venues where trading occurred
- [Systemic-Risk](/systemic-risk/) — The interconnection that nearly collapsed the market
- [Recession](/recession/) — The broader economic context of early 2010

</div>
