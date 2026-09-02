---
title: "Order Book Impact Model"
description: "Quantitative framework predicting how a given trade size will move prices by consuming depth at successive price levels in the limit order book."
keywords:
  - execution cost
  - market impact
  - order book
  - algorithmic trading
  - price elasticity
  - trading model
image: "/svg/trading.svg"
---

*An **order book impact model** is a quantitative estimate of the price movement that will result from executing a specific order size against the current limit order book. It answers the question: "If I buy 50,000 shares now, what average price will I pay?" by summing the cost of consuming liquidity level by level through the visible [order book](/order-book-impact-model/), plus a buffer for the market's likely adverse movement while the trade is happening.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Order Book Impact Model — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading execution." />

<div class="wiki-infobox-caption">Predicting how much your order will move the market.</div>

|   |   |
|---|---|
| **Core input** | Visible [bid-ask](/bid-ask-spread/) depths and order sizes at each price level |
| **Key output** | Expected average execution price; estimated realized impact in basis points |
| **Typical use** | Evaluating execution algorithms; routing decisions; [order book impact model](/order-book-impact-model/) |
| **Inputs needed** | Order size, direction (buy/sell), market state, historical volatility |
| **Limitations** | Doesn't account for hidden liquidity; assumes visible book is representative |
| **Related concept** | Market impact, [price discovery](/price-discovery/), [bid-ask spread](/bid-ask-spread/) |

</aside>

## Why the order book matters

When a trader wants to buy 50,000 shares, those shares must come from somewhere. The order book is a list of passive sell orders at various price levels: perhaps 10,000 shares offered at $99.50, another 15,000 at $99.51, another 20,000 at $99.52, and so on. To fill the entire 50,000, the buyer must consume shares at all these levels, paying an incrementally higher price as they go.

An order book impact model formalizes this calculation. It starts with the visible book—the quotes you can see—and asks: what is the cumulative cost of consuming this liquidity? But the actual execution cost is typically worse than the bare book suggests, because executing a visible trade moves dealers to revise their quotes. By the time the 40,000th share is bought, sellers have raised their ask from $99.50 towards $99.55 or higher.

The model bridges the gap between static book observation and dynamic execution reality.

## The mechanical calculation

The simplest form works level-by-level. Suppose the ask side of the book is:

- 10,000 shares at $99.50
- 15,000 shares at $99.51
- 25,000 shares at $99.52
- 20,000 shares at $99.53

A buyer wanting 50,000 shares will:

1. Buy 10,000 at $99.50 = $995,000
2. Buy 15,000 at $99.51 = $1,492,650
3. Buy 20,000 of the 25,000 at $99.52 = $1,990,400
4. Buy remaining 5,000 at $99.53 = $497,650

Total cost: $4,975,700 for 50,000 shares = $99.514 average.

But this assumes the order book stays static while the execution happens. In reality, as shares are bought, more sellers appear at the top of the book, or existing sellers pull their orders and re-quote higher. A more sophisticated model adds a **resilience factor**: a parameter that predicts how much the quoted prices will move as the order executes.

If resilience is low, the book recovers slowly and the market moves a lot. If resilience is high, the book heals quickly and impact is minimal. High-frequency market makers and algorithmic traders constantly assess and bet on resilience.

## Adverse movement and permanent impact

Order book models often distinguish between two kinds of impact:

**Temporary impact** is the immediate cost of consuming liquidity at worse price levels. This typically reverses quickly as the book restores itself.

**Permanent impact** is the market's longer-term reaction to the trade. If a large buyer steps in, the market interprets it as a positive signal and prices drift up even after the buyer is done. The buyer has, in effect, moved the market permanently. This permanent movement is often estimated using models of information asymmetry: what does the size of the order signal about future price direction?

A practical model might decompose total impact as:

**Total Execution Cost = Temporary Impact (spread + liquidity depletion) + Permanent Impact (market reassessment)**

For a small retail order, temporary impact dominates; for a multi-million-share institutional order, permanent impact can be larger.

## Parametric approaches

Rather than observing the specific order book each time, many institutions use parametric models fitted to historical data. A typical form is:

**Impact (bps) = α + β × (Order Size / Average Daily Volume)^γ**

This says: the cost (in basis points) of executing an order is proportional to the order size divided by the stock's typical daily volume, raised to some power. Larger orders relative to volume cause larger impact. Volatile stocks might have different α, β, or γ than stable ones.

The exponent γ (gamma) is crucial. If γ = 1, impact is linear in order size; if γ = 0.5, impact grows as the square root; if γ = 1.5, it grows superlinearly. Empirical studies suggest values near 0.5 to 1.0 across equities, though it varies by venue and market condition.

These parametric models are trained on historical trade data and let execution algorithms quickly estimate impact without parsing the real-time order book every microsecond. They're also portable across venues: a model trained on one exchange can be calibrated to another.

## Hidden liquidity and dark pools

A critical limitation of order book impact models is that they only see the lit (visible) liquidity. A stock might have 100,000 shares visible on the exchange order book, but another 500,000 shares tucked in dark pools, waiting. An impact model built on lit data alone will overestimate the cost of a large order, because there's actually much more liquidity available than the visible book suggests.

Sophisticated traders using dark pools or large block networks adjust their impact estimates downward, factoring in the probability that they can access hidden liquidity at a favourable price. The model becomes:

**Expected Cost = (Probability of lit fill × lit impact) + (Probability of dark fill × dark impact)**

This requires real-time or historical data on dark pool flow, which most retail traders don't have.

## Impact on execution strategy

Order book impact models directly inform execution decisions. A [schedule-driven execution](/schedule-driven-execution/) algorithm uses impact models to decide: "Should I execute 5,000 shares now, or is the book too thin and I should wait?" A [liquidity-seeking algorithm](/liquidity-seeking-algorithm/) uses them to route: "Impact is lower on venue B, so route this slice there." An [aggressive-in-the-money order](/aggressive-in-the-money-order/) placement is validated by asking: "Will pricing at this level still give me 100% fill, or will I move the market so much that I only get a partial fill?"

Models also feed into risk assessment. If a large position needs to be liquidated urgently, the impact model estimates the likely total cost, which feeds into decisions about timing, algorithm choice, or whether to accept a dealer's block trade offer instead.

## Calibration and decay

Impact models are only as good as their calibration. A model trained on a stock that was extremely liquid two years ago will overestimate available liquidity if the stock has since become thinner. Similarly, market structure changes—the rise of passive index funds, regulatory shifts, the entry or exit of major market makers—can shift impact parameters significantly.

Professional traders recalibrate their models frequently, often daily or in response to major market events. The parameters decay. A model trained in January that's still in use in June may be optimistic about summer liquidity, leading to aggressive execution decisions that backfire.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquidity-seeking algorithm](/liquidity-seeking-algorithm/) — uses impact models to route orders dynamically
- [Schedule-driven execution](/schedule-driven-execution/) — relies on impact models to choose execution pace
- [Aggressive-in-the-money order](/aggressive-in-the-money-order/) — impact models validate aggressive pricing
- [Bid-ask spread](/bid-ask-spread/) — the starting point of impact measurement
- [Algorithmic trading](/algorithmic-trading/) — the field that most heavily uses impact models
- [Market maker](/market-maker-trading/) — the counterparty whose response drives impact

### Wider context

- [Price discovery](/price-discovery/) — the mechanism through which orders move prices
- Market impact — the broader concept this model quantifies
- [Limit order book](/order-book-impact-model/) — the data structure the model analyzes
- [Over-the-counter market](/over-the-counter-market/) — alternative venue with different impact dynamics
- [Stock market](/stock-market/) — primary context for impact models in equities

</div>
