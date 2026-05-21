---
title: "High-frequency trading"
description: "High-frequency trading (HFT) is algorithmic trading by firms using powerful computers and advanced algorithms to execute thousands of trades per second. They profit on tiny price differences and arbitrage opportunities, relying on speed and scale."
keywords:
  - HFT
  - high-frequency trading
  - algorithmic trading
  - latency arbitrage
image: "/svg/trading.svg"
---

*High-frequency trading (HFT) is [algorithmic trading](/algorithmic-trading) at extreme speed. HFT firms use custom-built computers and fiber-optic cables to execute thousands of trades per second, exploiting tiny price discrepancies that last only milliseconds. HFT accounts for roughly 50% of U.S. equity trading volume and is controversial: proponents credit it with tighter spreads and greater liquidity; critics worry it causes flash crashes and harms retail traders.*

<div class="wiki-hatnote">

For slow algorithmic trading, see [algorithmic trading](/algorithmic-trading). For market making, see [market maker](/market-maker-trading). For the broader trading landscape, see [stock exchange](/stock-exchange).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">High-frequency trading — key facts</div>

<img src="/svg/trading.svg" alt="A server farm representing the infrastructure behind HFT" />

<div class="wiki-infobox-caption">HFT firms use specialized hardware and software to trade at millisecond speeds.</div>

|   |   |
|---|---|
| **What it is** | Algorithmic trading at speeds of microseconds to milliseconds |
| **Typical holding time** | Seconds to microseconds |
| **Profit source** | Tiny spreads, arbitrage, liquidity rebates |
| **Market share** | ~50% of U.S. equity trading volume |
| **Infrastructure cost** | Millions in hardware and colocation |
| **Best for** | Firms with capital and tech expertise |

</aside>

## How HFT works

An HFT algorithm:
1. **Watches prices** on multiple exchanges simultaneously (or microseconds apart).
2. **Detects arbitrage:** Spot Apple trading at $150.00 on NYSE and $150.01 on NASDAQ. This 1-cent difference is a potential profit.
3. **Executes instantly:** Buy on NYSE at $150.00, sell on NASDAQ at $150.01. Pocket the 1-cent difference × 10,000 shares = $100 profit, in microseconds.
4. **Repeats:** Do this thousands of times a day.

The strategy is simple; the execution requires extreme speed and massive scale.

## Competitive advantages of HFT

**Speed:** Microsecond advantages matter. A firm that is 1 millisecond faster can see price movements before slower competitors and trade first.

**Infrastructure:** Custom servers, fiber-optic cables, and colocation (housing servers inside exchange data centers) cost millions. Smaller firms cannot compete.

**Data and algorithms:** Sophisticated algorithms detect patterns and opportunities that human traders miss.

**Capital:** HFT requires millions in operating capital to sustain positions and absorb losses.

## Common HFT strategies

**Arbitrage:** Buy low on one exchange, sell high on another. Risk-free profit (if execution is fast enough).

**Market making:** Quote continuously and profit on the spread. HFT firms account for a large portion of market-making supply.

**Latency arbitrage:** Use proprietary speed advantages to trade ahead of slower competitors.

**Statistical arbitrage:** Complex algorithms spot correlations between securities and exploit them (e.g., if Stock A usually leads Stock B by 100 milliseconds, trade that pattern).

**Momentum ignition:** Allegedly, some HFT strategies trigger cascades (orders moving the market) that benefit the HFT firm's position. This is controversial and potentially illegal.

## HFT and market structure

**Tighter spreads:** HFT market makers compete aggressively, keeping bid-ask spreads tight (1 cent or less for large-cap stocks).

**Continuous liquidity:** HFT provides continuous depth of liquidity, so retail traders can execute large orders without wide slippage.

**Volume:** HFT accounts for roughly 50% of U.S. equity trading volume, making markets more active.

## Criticisms of HFT

**Flash crashes:** On May 6, 2010, U.S. equity markets crashed and recovered in minutes, partly due to HFT systems unwinding positions. Concerns that HFT could trigger similar crashes remain.

**Fairness:** HFT's speed advantage is a form of informational edge. Retail traders cannot compete. Some see this as market manipulation; others see it as competition.

**Systemic risk:** If HFT firms face large losses simultaneously (e.g., a "crowded trade"), they could simultaneously unwind, causing a market disruption.

**Front-running concerns:** HFT's speed advantage could enable them to detect slow traders' intent and trade ahead, similar to traditional front-running.

## Regulation of HFT

U.S. regulators have implemented several HFT safeguards:

**Circuit breakers:** If a stock's price falls too fast, trading is halted automatically to allow human intervention.

**Position limits:** Some regulators impose limits on how much a single firm can control.

**Reporting requirements:** Brokers must report order flow and execution quality; regulators monitor for suspicious patterns.

**Technology rules:** Exchanges mandate software controls and risk management ("kill switches").

Despite these rules, major HFT incidents have occurred (e.g., the 2012 Knight Capital flash crash).

## HFT and retail investors

**Pros:**
- Tighter spreads benefit all traders, including retail.
- Continuous liquidity means retail orders execute quickly.

**Cons:**
- Some HFT strategies may front-run or exploit slow traders.
- Payment-for-order-flow arrangements let brokers sell retail order flow to HFT firms, creating potential conflicts.

## Geographic arbitrage and colocation

HFT firms invest heavily in colocation: placing their servers physically in exchange data centers to minimize latency. A 1-millisecond advantage is worth millions if you trade millions of shares daily.

This has led to an "arms race" in latency, with some firms investing in microwave towers to transmit data at near-light-speed between exchanges.

## The debate: good or bad?

**Pro-HFT view:** HFT increases liquidity, tightens spreads, improves price discovery, and makes markets more efficient. The competitive pressure keeps everyone honest.

**Anti-HFT view:** HFT creates unfair informational advantages, increases systemic risk, and profits at the expense of slower traders (especially retail). The flash crashes and market instability are evidence.

The truth likely lies in the middle: HFT has benefits (liquidity) and risks (systemic, fairness), and the right level of regulation remains contested.

## See also

<div class="wiki-seealso">

### Closely related

- [Algorithmic trading](/algorithmic-trading) — slower cousin of HFT
- [Market maker](/market-maker-trading) — HFT firms often act as these
- Latency arbitrage — HFT's core advantage
- Arbitrage — risk-free profits HFT pursues

### Trading strategies and execution

- [VWAP order](/vwap-order) — algorithmic execution (slower than HFT)
- [TWAP order](/twap-order) — time-based execution
- [Smart order router](/smart-order-router) — routes to best prices
- [Dark pool](/dark-pool) — HFT firms also trade here

### Market structure and regulation

- [Lit venue](/lit-venue) — where HFT operates
- [Circuit breaker](/circuit-breaker) — regulatory safeguard against HFT crashes
- Flash crash — 2010 event partly due to HFT
- [Best execution](/best-execution) — ensures HFT does not harm retail

### Risk and concerns

- [Systemic risk](/systemic-risk) — HFT could trigger broader crashes
- Front-running — concern about HFT strategy
- [Payment for order flow](/payment-for-order-flow) — retail order routing to HFT
- Order toxicity — HFT avoids informed traders

</div>
