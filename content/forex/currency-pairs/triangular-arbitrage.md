---
title: "Triangular Arbitrage"
description: "A strategy exploiting price discrepancies across three currency pairs, buying and selling to lock in a risk-free profit when the cross-rates are misaligned."
---

*Triangular arbitrage is a rare but elegant exploit in currency markets. A trader observes three [currency pairs](/wiki/currency-pair/)—say EUR/USD, GBP/USD, and EUR/GBP—and notices they are momentarily mispriced relative to each other. By executing a series of trades (buying EUR/USD, selling GBP/USD, and trading EUR/GBP in the opposite direction), the trader locks in a tiny but certain profit. The opportunity exists only for microseconds before algorithmic traders exploit and eliminate it. For retail traders, triangular arbitrage is almost impossible to execute profitably, but the concept illustrates how forex markets are linked.*

## The mechanics: a concrete example

Suppose these quotes appear simultaneously:

- EUR/USD: 1.0850 / 1.0852 (bid 1.0850, ask 1.0852)
- GBP/USD: 1.2750 / 1.2752
- EUR/GBP: 0.8500 / 0.8502

A trader buys 1 million euros at 1.0852 (USD), paying 1,085,200 dollars. They convert those euros to sterling at 0.8500 (selling EUR/GBP at the bid), receiving 850,000 pounds. They then sell those pounds at 1.2750 (USD), receiving 1,083,750 dollars. The round trip cost 1,085,200 and returned 1,083,750—a loss of 1,450 dollars. This specific trade loses money.

But if prices were slightly different (perhaps the EUR/GBP quote was a fraction tighter), the round trip could profit. The dealer-made spread is typically so tight that only microsecond-scale algorithmic traders can profitably execute. Any human delay means the opportunity vanishes.

## Cross-rate consistency and no-arbitrage

The three pairs must be internally consistent: EUR/GBP should equal EUR/USD divided by GBP/USD. If EUR/USD is 1.0850 and GBP/USD is 1.2750, the implied EUR/GBP is 1.0850 / 1.2750 = 0.8510. If the market is quoting EUR/GBP at 0.8510, the rates are consistent; if it is quoting 0.8500, there is a 100-pip discrepancy in a small pair—a big arbitrage. Banks and ECNs ensure consistency by quoting the three pairs such that a round-trip conversion breaks even (or nearly so). This internal consistency is a sign of efficient markets.

## Why triangular arbitrage rarely persists

Forex is a highly liquid, decentralized market with thousands of participants and ultra-fast algorithms watching for mispricings. The moment a discrepancy appears—even a 0.1-pip triangular opportunity—algorithms buy the cheap leg and sell the expensive leg, instantly closing the gap. By the time a human trader sees the opportunity, it has likely evaporated. The spreads are so tight that the bid-ask span alone (usually 1–2 pips on major pairs) eats up any tiny profit.

## Execution in practice

If a retail trader wanted to attempt triangular arbitrage, they would:

1. Monitor three pairs simultaneously.
2. Calculate the implied cross-rate and compare it to the market cross-rate.
3. If a discrepancy is detected, execute the round-trip trades as fast as their broker allows.
4. Lock in the profit (if any).

The entire execution must happen in seconds; any delay allows the market to move and the opportunity to vanish. Retail brokers have order-entry latency (the time between your click and the trade execution) of 100+ milliseconds; professional algorithms have latency in single-digit milliseconds. This speed advantage is why institutional traders and exchanges detect these opportunities before retail traders can.

## Slippage and real-world constraints

Even if you spot a triangular opportunity, you face slippage: the price moves between your order entry and execution. If the best bid-ask spread on EUR/GBP is 0.8500/0.8502, and you want to sell at 0.8500 to complete your round trip, you might hit the bid a moment after it moves to 0.8499. This 1-pip slippage wipes out a 2-pip profit. Retail brokers' execution is less instantaneous than professional venues, widening the slippage.

## Implications for market efficiency

The rarity and fleeting nature of triangular arbitrage opportunities is actually a sign of market efficiency. If these opportunities persisted for hours or days, we would say the market is inefficient. The fact that they are exploited in microseconds shows that prices adjust instantly to new information and that traders with speed and capital are constantly hunting for them. This efficiency is good for traders looking for fair prices and bad for those seeking easy arbitrages.

## Generalizations to non-currency assets

Triangular arbitrage applies to any three linked markets. Equity traders exploit pricing inconsistencies among stocks and index futures; commodity traders exploit gaps between crude oil and refined products; bond traders exploit discrepancies between bonds and bond futures. The principle is the same: find a mispricing across related assets, execute the round-trip trades, and lock in profit. The difficulty is also the same: speeds must be fast and capital must be deployed efficiently.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/cross-rate/">Cross Rate</a> — the implied rate used in triangular arbitrage.</li>
<li><a href="/wiki/arbitrage-pricing-theory/">Arbitrage Pricing Theory</a> — the principle that arbitrage enforces fair pricing.</li>
<li><a href="/wiki/statistical-arbitrage/">Statistical Arbitrage</a> — more complex, multi-asset arbitrage.</li>
<li><a href="/wiki/currency-pair/">Currency Pair</a> — the instruments linked by triangular relationships.</li>
<li><a href="/wiki/spot-exchange-rate/">Spot Exchange Rate</a> — the rates used in triangular trades.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/high-frequency-trading/">High Frequency Trading</a> — the domain of profitable triangular arbitrage.</li>
<li><a href="/wiki/market-efficiency/">Market Efficiency</a> — triangular arbitrage is evidence of efficiency.</li>
<li><a href="/wiki/algorithmic-trading/">Algorithmic Trading</a> — the method used to exploit these opportunities.</li>
</ul>
</div>
