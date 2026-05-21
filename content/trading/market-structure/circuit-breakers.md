---
title: "Circuit Breakers"
description: "Automatic trading halts triggered when market prices move too far, too fast. Designed to prevent panic selling and allow time for repricing."
---

*A circuit breaker is an automatic brake built into stock exchanges. When the [S&P 500](/wiki/sp-500-index/) drops more than a certain percentage in a single day—typically 7%, 13%, or 20%—trading halts for 15 minutes. The circuit breaker pauses the market long enough for traders to digest the news and update their valuations, reducing the risk of a cascade of forced selling and a market crash.*

## Why circuit breakers exist

Before circuit breakers, markets experienced occasional events where panic selling fed on itself. The most famous example is [Black Monday, 1987](/wiki/black-monday-1987/), when the Dow Jones fell 22% in a single day. Computerized [trading programs](/wiki/algorithmic-trading/) sold automatically as prices fell, triggering more sales, which triggered more [algorithmic selling](/wiki/algorithmic-trading/). No single mechanism forced traders to pause and reconsider.

Circuit breakers were designed to interrupt this feedback loop. If prices are falling at an unsustainable pace, halt the market. Force traders to reevaluate. When trading resumes, the next wave of selling (or buying) is made consciously, not automatically.

## How they work

On U.S. stock exchanges, circuit breakers are tied to the level of the S&P 500 index. There are three levels:

**Level 1:** 7% decline from the prior day's close. The entire U.S. stock market halts for 15 minutes. This happens once every few years on average.

**Level 2:** 13% decline. Another 15-minute halt.

**Level 3:** 20% decline. The market closes for the rest of the day (or until the next day if the decline occurs after 3:25 p.m. Eastern).

The exact percentages and timing can vary by exchange and are adjusted periodically. Individual stocks may also have their own [trading halts](/wiki/trading-halts/) on news, but those are distinct from systemwide circuit breakers.

## Circuit breakers in action

The 2020 COVID-19 market sell-off triggered circuit breakers multiple times. On March 9, 2020, the market fell 7% at the open, triggering Level 1. On March 12, it fell 9.99% (triggering Level 1 again). On March 16, it fell 12.93% (triggering Level 2). In all three cases, the 15-minute halt allowed [market makers](/wiki/market-makers/) to rebalance and valuations to stabilize, and when trading resumed, the declines slowed. Without the halts, many analysts believed the panic selling could have been far worse.

## Criticisms and limitations

Some argue that circuit breakers delay the inevitable. If a security is worth 30% less, a 15-minute pause doesn't change that. Markets are designed to discover prices, and artificially freezing the market just defers the repricing and potentially frustrates traders who want to exit positions.

Others note that modern [high-frequency trading](/wiki/high-frequency-trading/) systems can cause mini-crashes at the individual-stock level that never trigger systemwide halts. A stock can fall 30% in milliseconds and then recover, all without the market realizing what happened. Individual [trading halts](/wiki/trading-halts/) at the single-stock level address this, but they can be delayed by a few seconds of processing time.

## International variations

Not all exchanges use the same circuit breaker rules. Some European and Asian exchanges use percentage declines tied to individual stock prices rather than a broad index. Others use time-based circuit breakers: if the market has been down for an hour without recovering, close trading and reassess. The goal is universal—avoid panic cascades—but the mechanics vary.

## Technical implementation

Circuit breakers rely on real-time monitoring of the [S&P 500](/wiki/sp-500-index/) price. The major U.S. exchanges (NYSE, NASDAQ) feed their data to the [consolidated tape](/wiki/consolidated-tape/), which publishes the official index price every second. When that price crosses a circuit-breaker threshold, the exchanges immediately halt all trading. Traders cannot execute new orders; existing [limit orders](/wiki/limit-order/) remain in the order book but do not execute.

The 15-minute halt gives [market makers](/wiki/market-makers/), portfolio managers, and news agencies time to process information and adjust their valuations. When trading resumes, a new [opening auction](/wiki/opening-auction/) is held to match orders at a fair price. This repricing often results in a smaller next decline as traders decide collectively that the move was overdone.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/trading-halts/">Trading halts</a> — temporary suspension of trading in individual securities.</li>
  <li><a href="/wiki/opening-auction/">Opening auction</a> — price discovery after a circuit-breaker halt.</li>
  <li><a href="/wiki/black-monday-1987/">Black Monday, 1987</a> — the event that prompted circuit breakers.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/stock-exchange/">Stock exchange</a> — where circuit breakers are enforced.</li>
  <li><a href="/wiki/high-frequency-trading/">High-frequency trading</a> — systems that can trigger individual-stock halts.</li>
  <li><a href="/wiki/market-makers/">Market makers</a> — who adjust prices during halts.</li>
</ul>
</div>
