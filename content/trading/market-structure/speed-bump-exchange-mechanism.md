---
title: "Speed Bumps on Stock Exchanges: How They Work"
description: "Intentional order-processing delays on exchanges like IEX that neutralize latency arbitrage and level the playing field for retail and institutional traders."
keywords:
  - speed bump exchange mechanism
  - iex speed bump
  - latency arbitrage
  - stock market microstructure
  - exchange order processing
image: "/svg/trading.svg"
---

*A **speed bump** is a deliberate, millisecond-scale delay imposed on orders at certain stock exchanges—most famously the IEX—to neutralize latency arbitrage. By slowing every order by the same amount, speed bumps prevent high-frequency traders (HFTs) from profiting on the difference in how fast orders reach the exchange. The mechanism is a structural intervention meant to level the playing field between rapid algorithms and slower institutional traders.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Speed Bumps — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Intentional delays that neutralize latency trading arbitrage.</div>

|   |   |
|---|---|
| **Core function** | Impose fixed delay (typically 350 microseconds) on all incoming orders |
| **Primary target** | Eliminate latency arbitrage advantage for co-located, high-speed traders |
| **Exchange example** | IEX (Investors Exchange), launched 2013; now a [stock exchange](/stock-exchange/) |
| **Time scale** | Microseconds to low milliseconds; invisible to humans but crucial for algorithms |
| **Trade-off** | Slows all trading slightly; removes a (controversial) source of profits |
| **Regulatory stance** | Permitted; seen as market-design innovation, not manipulation |

</aside>

## The Problem: Latency Arbitrage and Predatory Algorithms

Before speed bumps, a critical advantage went to traders with the fastest connections to exchanges. If an HFT could see a large order hit the market 10 microseconds before other traders could, it could front-run the order by buying the same stock and immediately selling it back at a profit. This is *latency arbitrage*: exploiting the tiny time differences between when different traders observe the same event.

The mechanism is subtle but costly. Suppose a pension fund wants to buy 1 million shares of Stock X. The order reaches the exchange and is posted publicly, but by the time retail and distant institutional traders *see* the order and react, an HFT co-located in the exchange's data center has already bought 50,000 shares and is selling them to the pension fund at a profit. The pension fund has paid more; the HFT has extracted value without performing any real economic service.

This form of predatory trading is not illegal—it is pure market structure. But it is widely seen as unfair. A small investor or a geographically distant fund should not be disadvantaged simply because they cannot afford a microwave relay to the exchange. Speed bumps eliminate this advantage by ensuring all orders are treated equally in time.

## How Speed Bumps Work: IEX's 350-Microsecond Delay

The most prominent example is the IEX (Investors Exchange), which imposes a fixed 350-microsecond delay on all inbound orders. This means that every order—from the fastest algorithm to the slowest retail broker—sits in a queue for 350 millionths of a second before being processed.

The effect is dramatic: in that 350 microseconds, the latency advantage of being co-located vanishes. An order traveling 500 kilometers away and one traveling 10 meters away both experience the same delay at the exchange. An HFT's ability to use speed as a trading advantage is nullified.

IEX calls this delay the "Crumbling Quote Indicator" (CQI) reference. When a larger order appears that might trigger market-wide movement, the 350-microsecond pause gives smaller participants time to adjust their quotes before the wave hits—hence "crumbling quote." The delay is intentional and transparent; traders know it is there.

## Why It Works: Equalizing the Information Timeline

Latency arbitrage depends on information asymmetry in *time*. If all traders receive the same information at the same moment, the arbitrage disappears. Speed bumps enforce that moment.

Consider a simplified scenario:
- **Without speed bump:** Trader A (co-located) sees an order at t=0. Trader B (remote) sees it at t=10 microseconds. Trader A can act in that 10-microsecond gap and profit.
- **With 350-microsecond speed bump:** Both see the order, but both are delayed. Trader A's 10-microsecond advantage is absorbed into the larger 350-microsecond standardized delay. By the time orders execute, the gap is gone.

The psychological impact is equally important. Traders know they cannot outrace the system, so they stop trying. Capital that would have been spent on faster connections and co-location agreements—"technology arms race"—is freed up for actual research and value-add.

## Variations and Implementation

Not all speed bumps are identical. Some exchanges use:

- **Fixed delays:** IEX's 350-microsecond model.
- **Randomized delays:** Small, unpredictable variations (±50 microseconds) to prevent traders from synchronizing around the delay.
- **Order-type-dependent delays:** Different delays for market orders vs. limit orders, or for certain order sizes.

Each variant aims at the same goal: remove the ability to profit purely from being faster, not smarter.

## The Regulatory and Market Debate

Speed bumps have been controversially supported and opposed:

**Supporters** argue they:
- Eliminate predatory latency arbitrage, a form of unfair trading.
- Reduce incentives to spend billions on proprietary fiber optics and data-center real estate, resources better spent on fundamental research.
- Level the playing field for retail and distant institutional investors.
- Promote price discovery by slowing "quote stuffing" and other HFT spoofing tactics.

**Critics** argue they:
- Add latency to all trading, slightly slowing execution and reducing market speed overall.
- Prevent legitimate trading strategies (e.g., passive arbitrage between linked markets).
- Are a "tax" on all traders to benefit those slower or less sophisticated.
- May not eliminate latency arbitrage fully if traders adapt (e.g., by gaming the delay mechanism itself).

The [Securities and Exchange Commission](/securities-and-exchange-commission/) (SEC) has approved IEX as a national exchange despite the speed bump, implicitly blessing the mechanism as a valid design choice. The SEC sees speed bumps as a form of market-structure innovation rather than manipulation.

## Latency Arbitrage Beyond Speed Bumps

Speed bumps do not eliminate all forms of latency-based trading. Savvy traders can still profit from the time difference between markets (e.g., between NYSE and [NASDAQ](/nasdaq/), or between U.S. and European exchanges). They can trade on differences in tick times between sectors or security types. What they cannot do is extract pure value from being microseconds faster on a single exchange.

## Broader Context: Exchange Competition and Fairness

IEX's speed bump is part of a broader market-design philosophy: that exchanges should compete on fairness and order protection, not on who can afford the fastest pipes. Since IEX launched in 2013, other exchanges have experimented with similar features. The Investors Exchange model has shown that a well-designed, relatively slow exchange can still attract substantial order flow because large institutional investors value protection from predatory trading.

This represents a shift in how exchanges differentiate themselves. Rather than a race to zero latency, some platforms emphasize *controlled* latency, transparency, and anti-predatory design.

## See also

<div class="wiki-seealso">

### Closely related

- [Market maker trading](/market-maker-trading/) — closely related to HFT and latency arbitrage
- [Limit order](/limit-order/) — basic order type affected by speed bump delays
- [Market order](/market-order/) — immediate execution order that may face speed bump effects
- [Bid-ask spread](/bid-ask-spread/) — closely tied to latency and order-arrival time
- [Price discovery](/price-discovery/) — market function affected by order-processing speed

### Wider context

- [Stock exchange](/stock-exchange/) — infrastructure that implements speed bumps
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator approving IEX and speed-bump design
- [Algorithmic trading](/algorithmic-trading/) — the domain most affected by latency neutralization
- [Alternative trading system](/alternative-trading-system/) — competing market structure not subject to speed-bump rules
- [Over-the-counter market](/over-the-counter-market/) — alternative venue without exchange-level latency concerns

</div>