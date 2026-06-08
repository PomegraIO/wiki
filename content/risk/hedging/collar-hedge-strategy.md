---
title: "Collar Hedge Strategy: Capping Both Upside and Downside"
description: "A collar hedge combines a protective put with a covered call to cap losses while limiting gains—a zero or low-cost strategy for managing concentrated equity positions."
keywords:
  - collar hedge strategy
  - protective put covered call
  - capped hedge
  - zero-cost hedge
  - concentrated position
image: "/svg/risk.svg"
---

*A **collar hedge** is a defensive strategy in which an investor buys a [put option](/put-option/) to guard against sharp declines in a stock, then immediately sells a [call option](/call-option/) against that stock to offset (or nearly offset) the put premium. The result: you trade unlimited upside for defined protection—losses stop at the put strike, gains cap at the call strike.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Collar Strategy — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Own stock, buy a put floor, sell a call ceiling; net cost is minimal or zero.</div>

|   |   |
|---|---|
| **Structure** | Long stock + Long put + Short call |
| **Cost** | Often zero or near-zero (short call offsets put premium) |
| **Profit if stock rises** | Capped at the call strike price |
| **Loss if stock falls** | Limited to the put strike price |
| **Ideal use case** | Large concentrated position held pre-exit or event |
| **Upside sacrifice** | All gains above call strike are forfeited |
| **Time frame** | Usually 3–12 months; rarely used long-term |

</aside>

## How the Collar Works: The Mechanics

Suppose you own 100 shares of a stock trading at $100. A direct [protective put](/put-option-hedge-for-long-stock/) at a $90 strike costs $3 per share ($300 total). Rather than pay that premium, you simultaneously sell a call option at a $110 strike, collecting $3 per share ($300). The two offset exactly, and your net cost is zero.

Your payoff is now bounded:

- **If the stock falls to $70:** You exercise your put, sell at $90, and your loss is $10 per share (from $100 to $90) plus zero premium paid. Total loss: $1,000.
- **If the stock rises to $115:** The call owner exercises it, your shares are called away at $110. You keep a $10 gain per share ($1,000), but no more. The $5 additional move above $110 is not yours.
- **If the stock stays near $100:** You keep the stock and the benefit of any small moves, up to $110.

This is insurance with a hidden cost: you've forfeited the right to participate in a big rally. In exchange, you've paid little or nothing out of pocket.

## Why the Strategy Matters for Concentrated Holdings

Many large shareholders face a dilemma: they want or need to reduce risk in a concentrated position, but selling triggers an immediate [capital gains tax](/capital-gains-tax-investor/) bill. If you own $5 million of a single stock and sell half to diversify, you might owe $500,000 in taxes on the gain. A collar lets you cut risk without a sale. You cap your downside and upside for a defined window, then exit or roll the collar later.

This is particularly common with:

- **Founders and early employees:** Restricted shares vest over time; a collar locks in a price floor during the holding period.
- **Legacy positions:** An investor inherited or bought stock years ago and it has become too concentrated. A collar is a temporary shield while planning an orderly exit.
- **Pre-announcement scenarios:** If a company is exploring a sale or merger, insiders often use collars to lock in a floor while negotiations proceed.

The collar is not a permanent solution—it is a **time-buying mechanism**. Once the hedge expires, you face the same choice again: roll it, sell, or accept unhedged risk.

## Collar Structures: Tight vs. Wide

The width of the collar—the gap between the put strike and call strike—determines how much risk you retain and how much premium you save.

**Tight collar:** Put at $95, call at $105 (on a $100 stock)
- Tighter protection (you lose less in a crash)
- But the short call gives less credit, so you likely pay something out of pocket
- Good when downside risk feels acute and you don't mind sacrificing upside

**Medium collar:** Put at $90, call at $110
- Common structure; often zero or very low cost
- Leaves a $20 range for "normal" stock moves
- Short call premium largely offsets put cost

**Wide collar:** Put at $85, call at $120
- You absorb the first $15 per share of decline unhedged
- The short call generates a large credit, possibly more than the put cost (you *earn* money)
- Useful if you're not especially frightened of a decline, but you want to cap your upside and harvest some premium

The "right" structure depends on your fear level and your beliefs about future moves. If you expect a 15% move in either direction and the stock is at $100, a $85/$115 collar feels too wide; a $90/$110 collar feels reasonable.

## Net Cost and Cost-Effectiveness

When the short call premium exactly equals the put premium, the collar is **zero-cost**. This typically happens when:

1. The put strike is not too far out of the money (e.g., $90 on a $100 stock, a 10% cushion)
2. The call strike is high enough that the short call is well out of the money (e.g., $110, a 10% cap)
3. [Implied volatility](/implied-volatility/) is reasonably elevated, making calls valuable to sell

If volatility is very low, calls are cheap, and you might pay a small amount. If volatility is very high, calls are expensive, and you might net a small credit (you earn money on the trade).

Over time, as [theta](/time-decay-theta/) works in your favor (you're short the call, so time decay helps you), the collar may become profitable. This profit offsets some or all of the original put cost, making the true economic cost of protection even lower.

## The Upside Sacrifice: When It Matters and When It Doesn't

The biggest objection to a collar is the capped upside. If you are deeply bullish and believe the stock will double, a collar is the wrong strategy—you've locked in your ceiling and you'll regret it if the stock soars.

But if you've already made outsized gains on the position and you're using the collar as a transitional hedge (you plan to diversify into other assets in the next 6–12 months), the lost upside is acceptable insurance. Many investors find that the psychological comfort of a known downside floor is worth more than the small probability of missing a huge rally.

One way to think about it: if you would otherwise be checking the stock price every day and feeling stressed, a collar might improve your life enough to be worth the capped upside.

## Rolling and Exiting the Collar

A collar typically lasts 3 to 12 months. When it is nearing expiration, you can:

1. **Let it expire:** The put and call both expire. You own the stock unhedged.
2. **Roll it forward:** Sell the original collar and buy a new one at new strikes, locking in another period of protection.
3. **Exit and sell the stock:** Use the collar expiration as a forcing function to diversify or rebalance.

If you roll, the new collar will be priced based on the then-current stock price and market volatility. If the stock has risen, the new collar will likely be higher (further up the strike ladder), and you might face a modest cost to replace it.

## Tax Implications

A collar itself does not trigger [capital gains](/capital-gains-tax-investor/). The put is an option contract; the short call is an option contract. If the call is exercised and your shares are sold, you realize the gain at the call strike price. If the put is exercised and you sell at the put strike, you realize the loss (or smaller gain) at that price.

The wash-sale rule—a technical tax rule that disallows loss harvesting in certain cases—can interact with collars, especially if you're using them to define a specific realized loss. Consult a tax advisor before implementing a collar that you intend to exercise.

## Risks the Collar Leaves Unhedged

A collar hedges the price of the stock itself. It does not hedge other risks:

- **[Dividend](/dividend/) cuts:** If the company slashes or eliminates the dividend, the stock may fall, but your put still only protects to the strike.
- **Takeover at lower price:** If an acquirer announces a deal below your call strike, the collar caps your recovery.
- **Liquidity crises:** On a catastrophic trading halt or exchange closure, options may not trade, and you cannot exercise.
- **Single-stock idiosyncratic risk:** A collar does not diversify away company-specific problems. It only blunts the price impact.

A collar is not a replacement for reducing concentration; it is a tool to *manage* concentration while you execute a diversification plan.

## See also

<div class="wiki-seealso">

### Closely related

- [Put option hedge for long stock](/put-option-hedge-for-long-stock/) — protective puts on their own
- [Covered call](/covered-call/) — the mechanics of selling call options against a holding
- [Call option](/call-option/) — understanding the call side of the collar
- [Basis risk in hedging](/basis-risk-in-hedging/) — why hedges don't always move perfectly with the underlying
- [Strike price](/strike-price/) — how strike selection affects payoff
- [Option premium](/option-premium/) — what drives the cost of puts and calls
- [Theta](/time-decay-theta/) — how time decay favors the short-call side of a collar

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — general hedging approaches
- [Capital gains tax investor](/capital-gains-tax-investor/) — why locked-in gains matter for collar strategies
- Concentrated position management — broader approaches to large single-stock holdings
- [Volatility smile](/volatility-smile/) — why collar strikes trade at different implied volatilities

</div>
