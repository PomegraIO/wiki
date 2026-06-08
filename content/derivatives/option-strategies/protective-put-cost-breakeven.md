---
title: "Protective Put Cost and Breakeven Calculation"
description: "A protective put adds cost to a stock position; the breakeven shows how high the stock must rise to overcome the premium paid for downside protection."
keywords:
  - protective put breakeven calculation
  - protective put cost analysis
  - protective put premium
  - put option cost recovery
image: /svg/derivatives.svg
---

*The **protective put breakeven** is the stock price at which gains from holding the underlying stock position equal the [premium](/option-premium/) cost of the put hedge—the threshold a position must reach for the insurance to justify its cost.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Protective Put Breakeven — calculation and tradeoff</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Protection costs; the math shows what gains must be earned to recover that cost.</div>

|   |   |
|---|---|
| **Premium paid** | Cost of the [put option](/put-option/) for downside protection |
| **Stock purchase price** | Original entry price for the long stock |
| **Breakeven formula** | Stock purchase price + total premium paid ÷ shares |
| **Max loss** | Strike price of put minus stock purchase price (if held to expiration) |
| **Unhedged loss** | Unlimited below the stock purchase price |

</aside>

## The Core Tradeoff: Cost Versus Protection

A [protective put](/protective-put-cost-breakeven/) combines a long stock position with a long [put option](/put-option/). The put grants the right to sell the stock at a fixed strike price, capping losses if the stock falls sharply. This insurance is not free—the put carries a premium that reduces overall gains.

The breakeven calculation answers a direct question: if I pay this premium for this insurance, how far must the stock rise before I recover that cost and begin earning profit?

## Step-by-Step Breakeven Calculation

Suppose an investor buys 100 shares of a stock at $50 per share and purchases a 3-month put option with a $50 strike for $2 per share ($200 total).

**Step 1:** Calculate total premium cost.
- Put premium = $2 per share × 100 shares = $200

**Step 2:** Identify the stock's current price.
- Stock purchase price = $50 per share

**Step 3:** Add premium to stock price.
- Breakeven = $50 + $2 = $52 per share

At $52, the investor has broken even:
- Stock unrealized gain: ($52 − $50) × 100 = $200
- Premium cost: −$200
- Net P&L: $0

Below $50, the put protects losses. At $40, the position is protected:
- Stock loss: ($40 − $50) × 100 = −$1,000
- Put intrinsic value: ($50 − $40) × 100 = $1,000
- Net loss: −$200 (the premium paid)

Above $52, the put is an increasingly expensive insurance policy as the stock appreciates and the put expires worthless.

## Premium Factors: Time, Volatility, Strike Selection

The premium paid depends on three variables:

**Strike price selection** affects the cost. A put struck at-the-money ($50) costs more than a put struck out-of-the-money ($45). Choosing a lower strike reduces premium but leaves a larger unprotected downside. A $45 put might cost $0.50, raising breakeven to only $50.50 instead of $52, but losses between $45 and $50 are unprotected.

**Time to expiration** drives premium via [theta](/theta/). A 6-month put is more expensive than a 3-month put because there is more time for the stock to fall. The longer the hedge duration, the higher the cost—and thus the higher the breakeven.

**Implied volatility** shifts the premium. A stock expected to swing wildly (high implied vol) raises put prices; a calm stock lowers them. In volatile periods, protective puts become expensive, pushing breakeven higher.

## Comparing Protective Put Strategies

A trader holding $50,000 in a stock position has multiple hedge options:

| Strategy | Strike | Premium | Breakeven | Unhedged Loss at $40 |
|----------|--------|---------|-----------|----------------------|
| **Unhedged** | — | $0 | $50 | −$10,000 |
| **Put at $50** | $50 | $2,000 | $52 | −$2,000 (capped) |
| **Put at $45** | $45 | $500 | $50.50 | −$5,000 |
| **Put at $40** | $40 | $150 | $50.15 | −$10,000 |

The in-the-money put ($50 strike) is the most expensive but offers the most protection. The out-of-the-money puts cost less upfront but leave gaps. The choice depends on the investor's fear threshold and expected holding period.

## Breakeven in Multi-Period Scenarios

If the investor rolls the put forward—selling the near-term put at expiration and buying another—the calculation becomes layered. Each roll adds a new premium cost and shifts the overall breakeven.

Assume the $50 put expires in 3 months at $52 (worthless), then is rolled into a new $50 put costing $1.50:
- First period breakeven: $52
- New premium: $150
- Second period breakeven: $52 + $1.50 = $53.50

Over a full year of quarterly rolls, total premium paid accumulates, pushing breakeven higher. Rolling hedges is a perpetual drain on returns in a rising market—the insurance stays in place but premium keeps eroding gains.

## When Protective Puts Make Sense

The breakeven calculation is the first filter. If a stock must rally 10% just to recover put premium in a 3-month period, the expected return on the stock should justify that drag. A stock with 20% upside expected return and 4% downside protection cost is attractive; a stock with 5% expected return and 2% protection cost is not.

Protective puts are most economical when:
- Volatility is low (premiums are cheap)
- The holding period is short (less time decay)
- The investor fears a specific catalyst (earnings, acquisition uncertainty)
- The underlying position is large and concentrated (insurance adds significant value)

## Breakeven Versus Maximum Loss

It is important not to confuse breakeven with maximum loss. The protective put's **maximum loss** occurs if the stock falls to zero and the put's strike becomes the floor.

Using the $50 stock and $50 put:
- Maximum loss = Stock price − Strike = $50 − $50 = $0 (plus premium paid: −$200, or −$200 per 100 shares)

A protective put turns what would be a potential 100% loss into a capped, known loss. The breakeven tells you the cost of that cap; the maximum loss tells you what you paid protects.

## Practical Example: Calculating Full Position Economics

A trader owns 200 shares of a $100 stock and buys 2 put contracts (100 shares each) at the $95 strike for $3 per share.

- Total premium: $3 × 200 shares = $600
- Breakeven: $100 + $3 = **$103 per share**
- Maximum loss if stock falls to $0: $95 − $100 + $3 = **−$2 per share, or −$400 total**
- Unprotected loss if stock falls to $0 (no put): −$100 × 200 = −$20,000

At $103, the position breaks even. Below $95, the put caps losses. The investor traded $600 of certain cost for protection worth up to $10,000 in downside.

## See also

<div class="wiki-seealso">

### Closely related

- [Put option](/put-option/) — the insurance contract used in protective strategies
- [Option premium](/option-premium/) — what buyers pay and sellers collect
- [Protective put](/protective-put-cost-breakeven/) — the core structure explained here
- [Intrinsic value](/intrinsic-value/) — how much protection the put provides
- [Strike price](/strike-price/) — the level at which the put protects
- [Call option](/call-option/) — understanding calls helps clarify puts

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — broader risk management with options
- [Cost basis](/cost-basis/) — how premium affects tax accounting
- [Value at risk](/value-at-risk/) — quantifying position downside in risk terms
- [Covered call](/covered-call/) — selling calls; counterpoint to buying puts
- [Counterparty risk](/counterparty-risk/) — options settlement and clearing mechanics

</div>
