---
title: "Protective Put vs Collar: Choosing the Right Hedge"
description: "Compare buying a standalone put versus funding it with a short call. Understand cost structure, upside tradeoffs, and when each hedge strategy fits your goal."
keywords:
  - protective put vs collar strategy
  - collar vs protective put
  - collar hedge vs long put
  - collared stock strategy
image: /svg/derivatives.svg
---

*Choosing between a **protective put** and a **collar** comes down to cost: a protective put offers unlimited upside but you pay full [option premium](/option-premium/); a collar funds the put by selling a call, capping upside but costing little or nothing. Both hedge a stock or portfolio against downside.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Protective Put vs Collar — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Two ways to hedge: pay cash for unlimited upside, or trade some upside for free downside protection.</div>

|   |   |
|---|---|
| **Protective put** | Buy a put; keep all upside |
| **Collar** | Buy a put + sell a call; cap upside |
| **Cost** | Put premium (e.g., 2–4% annual) | Minimal; call sale offsets put cost |
| **Max loss** | Limited to put strike | Limited to put strike |
| **Max profit** | Unlimited above call strike (put only) | Capped at short call strike |
| **Tax treatment** | Assignment triggers [long-term capital gains](/long-term-capital-gain-tax/) | Assignment triggers [capital gains](/long-term-capital-gain-tax/) |
| **Assignment risk** | Only on the put (rare) | Both put and call can assign |

</aside>

## The Two Hedging Approaches

**Protective put.** You own stock and buy a [put option](/put-option/). If the stock crashes below the put strike, you exercise it and sell the shares at the strike price, locking in your floor. Above the strike, you own the shares outright and keep all gains. The cost is the put premium, paid upfront. For example, if you own a $100 stock and buy a $95 put for $2, you've paid $200 per share ($2 × 100) to ensure you can't lose more than $5 per share (plus the $2 premium). Your cost: $7 per share, or 7% of stock price.

**Collar.** You own stock, buy a put at the same strike, but immediately sell a call at a higher strike. The call premium offsets (or entirely covers) the put premium, making the total cost near zero or negative. The tradeoff: if the stock rises above the call strike, you are obligated to deliver shares at that strike. Above the call strike, your profit is capped. For the same $100 stock, you might buy a $95 put for $2 and sell a $105 call for $2.50. Net cost: –$0.50 (you receive cash). Your downside is protected below $95, but your upside is capped at $105.

## Cost Structure

The core comparison is cost.

A **protective put** requires you to spend real premium. The amount depends on [implied volatility](/implied-volatility/), [time to expiry](/expiration-date/), and how far out-of-the-money the put is. A put that is closer to the current stock price (more downside protection) is more expensive. A put that is further out (less protection) is cheaper. For a volatile stock with 30 days to expiry, an at-the-money put might cost 1.5–2.5% of stock price; a 5–10% out-of-the-money put might cost 0.5–1.5%.

A **collar** typically costs much less because the short call premium offsets the put. In many cases, the call sale exactly funds the put, yielding a zero-cost or even a positive-credit collar. This is especially true for:
- High-volatility stocks (calls sell for more premium).
- Wide collar bands (a far-out-of-the-money call offsets a less-far-out put).
- Stocks with high [dividend yield](/dividend-yield/) (affects [option pricing](/option-premium/)).

The zero-cost collar is popular for this reason: you get downside protection without writing a check, but you have capped the upside in exchange.

## Upside Scenarios and Tradeoffs

Suppose you own 100 shares of a stock trading at $100. You want to hedge for the next six months.

**Scenario 1: Stock rises to $120.**
- **Protective put:** Your put expires worthless. You own the stock at $120, a $2,000 gain, minus the $200–$400 put premium you paid. Net gain: $1,600–$1,800.
- **Collar:** Your short $105 call is exercised. You deliver shares at $105, a $500 gain above the original $100, minus any net cost (likely near zero). Net gain: ~$500.

The protective put winner here, but you paid for the privilege.

**Scenario 2: Stock rises to $102.**
- **Protective put:** Net gain $100 (stock gain of $200 minus put premium).
- **Collar:** Net gain ~$200 (stock gain of $200, no call exercise, no net cost).

In small-move scenarios, the collar cost advantage shows.

**Scenario 3: Stock falls to $90.**
- **Protective put:** Both strategies work identically. You exercise the $95 put and sell at $95, limiting loss to $500 (plus original premium). Net loss: $500–$700 (depending on upfront put cost).
- **Collar:** You exercise the $95 put. Net loss: ~$500 (call expires, no benefit).

On the downside, both protect equally. The difference is how much you paid for that protection.

## When to Use Each

**Choose a protective put if:**
- You expect significant upside and want to keep all of it.
- You cannot afford to cap upside (e.g., a catalyst event you believe in strongly).
- You have a short-term hedge horizon and [volatility](/implied-volatility/) is low (cheap puts).
- Your position is small relative to your portfolio, so the premium cost is tolerable.
- You want to test your conviction without pressure to sell into a rise.

**Choose a collar if:**
- You want downside protection at minimal cost.
- You are comfortable with a capped upside (or see the call strike as realistic profit target).
- You have a longer hedge horizon and volatility is moderate to high (call premium is rich).
- You want to reduce or eliminate capital outlay for the hedge.
- You are hedging a large, concentrated position where the cost of a full put would be prohibitive.

## Assignment and Exercise

**Protective put assignment** is rare. If the stock falls below the strike, you *choose* to exercise the put and sell. There's no forced assignment.

**Collar assignment** can happen on either leg. If the stock drops below the put strike and you exercise, you sell at the put strike (good). If the stock rises above the call strike at or before expiry, the call is likely assigned, and you must deliver shares (the cost of the hedge). If you hold the stock after assignment, you've effectively sold at a fixed price; if you wanted the stock, you must repurchase.

For [tax-loss harvesting](/tax-loss-harvesting/) purposes, be aware of the [wash-sale](/wash-sale/) rule if you close a collar and repurchase similar stock within 30 days.

## Choosing the Strikes

In a protective put, you choose the strike based on your loss tolerance. A put at 95 (5% out-of-the-money) protects against losses beyond that point and costs less than one at 100 (at-the-money). A put at 90 (10% out-of-the-money) is cheaper but offers less protection.

In a collar, you choose both strikes to balance cost and upside cap. A wide collar (e.g., buy $95 put, sell $110 call) often comes close to zero cost but caps upside further out. A tight collar (e.g., buy $97 put, sell $103 call) keeps you in a narrow band and may still cost net premium.

The optimal collar adjusts over time. Stocks with rising prices allow you to sell calls further out; stocks that stall may require you to roll the call lower to keep the net cost near zero.

## Tax Implications

Both strategies have [capital gains](/long-term-capital-gain-tax/) implications. If you hold a protective put and the underlying stock is assigned (exercised) while you still own shares, the assignment resets your holding period, potentially affecting whether the gain qualifies as long-term.

In a collar, if you allow both legs to be assigned, the short call assignment is treated as a sale, and the purchase price of the original shares is your [cost basis](/cost-basis/). If you repurchase stock after assignment, that's a new purchase with a new holding period.

## Comparing Across Market Regimes

| Regime | Protective Put | Collar |
|--------|---|---|
| **High volatility** | Expensive puts | Call premiums offset, lower net cost |
| **Low volatility** | Cheap puts; affordable | Wide collars needed to zero cost |
| **Rising market** | Protects gains while capturing upside | Capped at call strike |
| **Sideways market** | Hedge underutilized; premium lost | Net cost is minimal, small upside capped |
| **Falling market** | Both perform identically; put cost matters | Both perform identically; low cost wins |

## Common Missteps

**Forgetting roll management.** Collars expire; if you do nothing, the call assignment delivers stock. Plan ahead whether you want to roll the collar further out, close it, or accept assignment.

**Choosing strikes in isolation.** A collar's strikes should be chosen together, balancing the cost against your upside target. Picking a 95 put without considering what short call premium offsets it will likely result in a net cost.

**Comparing a cheap out-of-the-money put to a zero-cost collar.** A protective put at 95 (far out) looks cheap but offers minimal protection. The collar at 95/105 (zero cost) offers more symmetry and certainty.

**Ignoring dividends.** If the underlying stock pays a dividend, the call owner has no right to it; this affects option pricing and the cost of the collar.

## See also

<div class="wiki-seealso">

### Closely related

- [Put Option](/put-option/) — downside protection fundamentals
- [Call Option](/call-option/) — upside capping
- [Collar](/collar/) — the combined strategy in depth
- [Covered Call on LEAPS](/covered-call-on-leaps/) — alternative upside-capping trade
- [Option Wheel Strategy Explained](/options-wheel-strategy-explained/) — repeating hedge cycle

### Wider context

- Options Strategies — survey of risk management tools
- [Implied Volatility](/implied-volatility/) — drives option premium
- [Assignment](/assignment/) — when exercise happens
- [Tax-Loss Harvesting](/tax-loss-harvesting/) — coordinating hedges with taxes
- [Capital Gains](/long-term-capital-gain-tax/) — tax treatment of sales

</div>
