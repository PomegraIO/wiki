---
title: "How Limit Up–Limit Down Circuit Breakers Work for Individual Stocks"
description: "Walks through the price-band calculation and trading pause mechanics that trigger when individual securities move sharply under the Limit Up–Limit Down plan."
keywords:
  - circuit breakers individual stocks
  - limit up limit down
  - luld plan
  - trading halts mechanics
  - price circuit breaker
image: /svg/regulation.svg
---

*The **Limit Up–Limit Down (LULD) plan** establishes automatic price bands around individual stocks and other securities; when a trade tries to occur outside those bands, the trade is rejected and trading pauses for a short window. This circuit breaker prevents the kind of flash crashes or erratic price spikes that can occur in fast, electronic markets. Unlike market-wide circuit breakers that halt all trading during extreme moves, **LULD circuit breakers work on a per-stock basis**, with bands calculated dynamically based on the stock's recent price and volatility.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">LULD Circuit Breakers — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for market regulation." />

<div class="wiki-infobox-caption">Per-stock price bands that reject trades and pause trading during sharp moves.</div>

|   |   |
|---|---|
| **What it is** | Automated trading pause triggered by price moves outside dynamic bands |
| **Bands set at** | 5% and 20% of the average reference price (different bands for different tiers) |
| **Pause duration** | 15 seconds during regular hours; 5 minutes at market open |
| **Scope** | Individual stocks, ETFs, and certain other securities (not bonds) |
| **Triggered by** | Single trade or order at or beyond the band limit |
| **Rule basis** | SEC Regulation SHO and FINRA rules (effective since April 2013) |
| **Wide acceptance** | Adopted also by TSX and other major exchanges |

</aside>

## The Problem LULD Solves

Before Limit Up–Limit Down, individual stocks could move wildly in microseconds due to errant orders, algorithm mistakes, or sudden loss of liquidity. In 2010, the so-called "Flash Crash" sent the S&P 500 down nearly 10% in minutes before recovering. Regulators found that some individual stocks fell 50%, 60%, or more in seconds due to a single large order meeting no bids. Electronic trading systems can execute millions of shares per second; a fat-finger trade or a malfunctioning algorithm can create mayhem before a human operator reacts.

Circuit breakers for individual stocks address this. They create a floor and ceiling around a stock's fair price. If a buy order tries to execute above the ceiling or a sell order below the floor, the order is rejected and trading pauses. This gives market makers, traders, and algorithms a moment to reassess and re-quote, preventing a cascade of panic sales or a runaway spike on bad information.

## How the Bands Are Calculated

The LULD plan divides stocks into three tiers based on price and liquidity. Each tier has different band widths.

**Tier 1** covers highly liquid, high-priced stocks (broadly, stocks in the S&P 500 and certain large-cap ETFs). The bands are set at 5% above and 5% below the *average reference price*, calculated from the previous five minutes of trading. If a Tier 1 stock has a reference price of $100, the limit up level is $105 and the limit down level is $95. Any order to buy at $105.01 or sell at $94.99 is rejected.

**Tier 2** covers other stocks and smaller-cap stocks. Bands are wider: 10% above and 10% below the reference price.

**Tier 3** covers stocks below $1.00 and certain other illiquid securities. Bands are the widest: 20% above and 20% below.

The reference price itself updates every five seconds during trading, reflecting the average price of trades (or quotes, if no trades have occurred) in that window. This means the bands move continuously as the market reprices the security. If a stock rallies, its reference price rises and the limit up and limit down levels move up with it.

## When a Band Is Hit: The Pause

When an order or quote tries to execute at or beyond a band limit, the exchange or market center rejects the order. Trading in that security pauses for 15 seconds during regular trading hours (9:30 a.m. to 4:00 p.m. Eastern) or 5 minutes during the opening (9:28 a.m. to 9:33 a.m.) and closing periods (3:55 p.m. to 4:00 p.m.).

During the pause, no trades execute at any price, but new orders and quotes can be submitted. Traders and market makers use the pause to re-quote at new levels, re-examine risk, and reset algorithms. When the pause ends (after 15 or 5 seconds), trading resumes and orders are matched at the best available price. If the stock has moved sharply in trader estimates, the reference price recalculates and new bands are set. This prevents a single pause from capping a legitimate rally or decline.

After a pause, if another order immediately hits a band, another pause is triggered. A stock can pause multiple times in succession if the underlying price is moving rapidly. However, there is no broader "trading halt"—other stocks continue trading unaffected.

## The Reference Price and Quotation Halt Interaction

The reference price is not just an arbitrary midpoint; it is the actual average price at which the security has traded (or been quoted) in the prior five-minute window. This means LULD bands move with the market. If a stock is in an uptrend, the reference price drifts up and the bands move up, allowing the stock to continue rising. The circuit breaker is not a price cap; it is a speed governor, preventing single transactions from moving price more than 5%, 10%, or 20% in one go.

In the first 15 minutes of the trading day (the opening window), the band widths are relaxed. Stocks often have a wider band of 10% or 20% during the open because reference prices may not yet be reliable after a night without trading. This prevents overnight news from triggering repeated LULD pauses at the opening bell.

## Market-Wide Circuit Breakers vs. LULD

LULD is distinct from market-wide circuit breakers, which halt all trading on the S&P 500 when the index falls 7%, 13%, or 20% in a single day. Those halts last 15 minutes (at 7% and 13%) or close the market (at 20%). LULD is stock-by-stock and subsecond, designed to catch individual stock anomalies. Market-wide breakers catch systemic shocks.

A stock can trigger LULD many times in a day due to volatile sentiment or news; the overall market can still be trading normally. Conversely, if the whole market is crashing, individual LULD pauses do not prevent that decline—they just slow individual stocks as they fall.

## Trade-Offs and Criticisms

LULD has reduced flash-crash-like moves and is widely credited with improving market stability. However, it has also created frictions. During volatile periods, active stocks can pause repeatedly, making them harder to exit quickly. Some argue that wider bands for Tier 2 and Tier 3 stocks leave them more vulnerable to erratic moves. Others contend that the five-minute reference-price window is too short, allowing bands to lag genuine price shifts. And some traders argue that knowing where the bands are creates opportunities for manipulation: a trader can place orders near a band to trigger a pause and profit from the disruption.

Regulators monitor LULD data to refine the plan. There have been periodic proposals to tighten bands for lower-tier stocks or to adjust the reference-price methodology, but consensus on improvements is hard to reach.

## International Adoption

The LULD concept has been adopted by other major exchanges. The Toronto Stock Exchange, exchanges in Australia, and many European markets have circuit breaker rules for individual stocks, though the band widths and reference-price calculations may differ. This global adoption reflects a consensus that per-stock circuit breakers are a basic safeguard in fast electronic markets.

## See also

<div class="wiki-seealso">

### Closely related

- [Circuit Breaker Market-Wide](/circuit-breaker-market-wide/) — Halts of all trading on sharp index moves
- Trading Halts — Voluntary or regulatory suspension of trade in a security
- [Market Maker Trading](/market-maker-trading/) — Role of market makers in absorbing order imbalances during pauses
- Flash Crash — 2010 event that prompted LULD adoption
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulator that oversees LULD
- [Algorithmic Trading](/algorithmic-trading/) — Automated systems that LULD protects against

### Wider context

- [Stock Exchange](/stock-exchange/) — Trading venue where LULD operates
- [Market Risk](/market-risk/) — Broader category of trading risks
- [Volatility Smile](/volatility-smile/) — Pricing of options during volatile moves
- [Execution Risk](/execution-risk/) — Risk of adverse price movement during order execution

</div>
