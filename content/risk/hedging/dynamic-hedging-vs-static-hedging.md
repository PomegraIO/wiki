---
title: "Dynamic Hedging vs Static Hedging"
description: "Dynamic hedges are continuously rebalanced to adjust to changing prices; static hedges are set once and held. Each approach has different costs, risks, and optimal use cases."
keywords:
  - dynamic hedging static hedging
  - rebalanced hedge
  - static hedge
  - hedge rebalancing cost
  - hedge management
image: "/svg/risk.svg"
---

*A **static hedge** is set up once and left alone; you sell a [futures contract](/futures-contract/) or buy an [option](/option/) and hold it to expiration. A **dynamic hedge** is adjusted repeatedly as market prices move, rebalancing the hedge position to maintain a consistent level of protection. The difference matters: dynamic hedges reduce some risks but incur repeated transaction costs, while static hedges are cheaper to implement but may drift away from your target protection level.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dynamic vs. Static — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Rebalance often = more control, higher costs. Set and hold = simpler, but it drifts.</div>

|   |   |
|---|---|
| **Static hedge** | One entry; held to expiration or maturity |
| **Dynamic hedge** | Continuously rebalanced as price/delta changes |
| **Cost advantage** | Static: lower transaction costs; dynamic: reduced [basis risk](/basis-risk-in-hedging/) |
| **Operational burden** | Static: minimal monitoring; dynamic: frequent adjustments |
| **Best for** | Static: short-term or well-defined events; dynamic: long-dated exposures |
| **Key metric** | [Delta](/delta/) — sensitivity to underlying price |
| **Ideal frequency** | Dynamic: daily or when [delta](/delta/) threshold is breached |

</aside>

## Static Hedging: The Simple Buy-and-Hold Approach

A static hedge is the simplest form. You identify an exposure, put on a hedge using a derivative or cash instrument, and then do nothing—you hold until expiration or maturity, at which point the hedge naturally unwinds.

**Example: A wheat farmer's static hedge**

In March, a farmer plants 50,000 bushels of wheat for autumn harvest. He fears falling prices, so he sells 100 futures contracts (each 5,000 bushels) at $6.50 per bushel, locking in a sale price. The futures expire in September. From March through September, he does nothing. At harvest, he sells his physical wheat at the spot price and simultaneously closes his short futures position. The combination of physical sale and futures close determines his net realized price.

If wheat falls to $5.50, his physical loss is $0.50/bu × 50,000 bu = $25,000. But his short futures position gains $0.50/bu × 50,000 bu = $25,000. The two offsets, and he realizes his locked-in $6.50 price.

**Why static hedges are used:**

1. **Cost:** One entry transaction, one exit. Commissions and bid-ask spreads are paid once.
2. **Simplicity:** No monitoring, no decisions between now and expiration.
3. **Known maturity:** The underlying exposure is naturally resolved at a known time (harvest, loan maturity, delivery date).
4. **Regulatory or operational constraints:** Some portfolios or mandates don't allow frequent rebalancing.

## Dynamic Hedging: Continuous Adjustment

A dynamic hedge is rebalanced periodically (daily, weekly, or whenever a trigger is hit) to maintain a target exposure level. The rebalancing is necessary because the sensitivity of the hedge changes as the underlying price moves.

**The [delta](/delta/) problem:**

Consider a [call option](/call-option/). Its [delta](/delta/) (the rate at which its value changes with the underlying) starts out relatively low when the option is far out of the money, and rises as the underlying price approaches the strike. An option trader who has sold calls (a short position) is exposed to rising prices. To hedge that, they might buy some of the underlying stock. But as the price rises, [delta](/delta/) rises, and they need to buy more stock to stay hedged. As the price falls, [delta](/delta/) falls, and they need to sell some stock.

This is dynamic hedging in action: constantly buying high and selling low to maintain a neutral [delta](/delta/) position.

**Example: A bank using dynamic hedging for a convertible bond**

A bank purchases a [convertible bond](/convertible-bond/)—a bond that can be converted into stock by the holder. The bond is long credit risk and long an embedded call option on the company's stock. To hedge the stock price sensitivity, the bank shorts stock dynamically. Each day:

1. Compute [delta](/delta/): how much the convertible's value changes if the stock rises 1%.
2. If [delta](/delta/) is 0.60, short 60% of the notional position in stock.
3. If the stock rises and [delta](/delta/) rises to 0.75, short more stock.
4. If the stock falls and [delta](/delta/) drops to 0.40, buy back some stock.

The bank incurs transaction costs with each trade, but it keeps the hedge tightly aligned with the exposure.

## Transaction Costs and the Rebalancing Trade-Off

The key trade-off is transaction costs vs. protection quality:

**Static hedges win on cost.** If you hedge once at a cost of 0.05% (bid-ask spread + commissions), that cost is sunk. Done.

**Dynamic hedges incur repeated costs.** If you rebalance monthly and each rebalance costs 0.05%, the annual cost is roughly 0.60% (12 × 0.05%), plus adjustments for higher-cost rebalancing near the strike or when volatility is elevated. For a year-long hedge, that adds up.

**But dynamic hedges reduce other risks:**

1. **[Basis risk](/basis-risk-in-hedging/):** A static hedge with a coarse instrument (e.g., hedging a specific company's stock with a broad index futures contract) might drift. Dynamic hedging can tighten the fit.
2. **[Delta risk](/delta/):** For options positions, a static hedge leaves your [delta](/delta/) exposure shifting as prices move. Dynamic hedging restores neutrality.
3. **Event risk:** If an unexpected announcement changes the underlying's volatility, a static hedge's effectiveness is frozen. A dynamic hedge can adapt.

## When to Use Each Approach

**Static hedging is appropriate for:**

- **Short-dated exposures:** A 3-month loan, a seasonal commodity position, an announced event-driven transaction. The exposure is well-defined and resolves in a known timeframe.
- **Cost-sensitive hedgers:** Farmers, small businesses, and fund managers with tight operational budgets often use static hedges.
- **Commodity producers:** A farmer hedges the harvest; a mine hedges annual production. The physical harvest date is fixed, and the static hedge mirrors it.
- **Regulatory or mandated hedging:** Some institutional mandates require hedging a known liability (a pension fund's long-term benefit obligation, for instance) using a specific static instrument.

**Dynamic hedging is appropriate for:**

- **Long-dated or uncertain exposures:** If you're hedging a position that might take 2–3 years to unwind, or one with uncertain timing, static hedging might drift too far. Dynamic rebalancing keeps you on target.
- **Options positions:** An options desk must rebalance [delta](/delta/) regularly or accept directional risk. This is non-negotiable.
- **Volatile markets:** When markets are turbulent and price-sensitivity shifts sharply, static hedges can become poorly matched to the underlying. Dynamic adjustment restores fit.
- **Large institutional portfolios:** With many offsetting positions and frequent cash flows, dynamic rebalancing is often built into the operations already (e.g., a pension fund rebalancing asset allocation quarterly).

## The Hidden Complexity: Optimal Rebalancing Frequency

If you decide to hedge dynamically, how often should you rebalance? Too often and you incur excessive transaction costs. Too infrequently and your hedge drifts.

Academic research on option hedging suggests rebalancing **when [delta](/delta/) has moved a fixed amount** (e.g., by 0.10 or 0.20) rather than on a fixed time schedule. This is called **threshold rebalancing**. If the price moves slowly, you rebalance infrequently; if it moves sharply, you rebalance more often. The threshold is calibrated to balance transaction costs against [gamma](/gamma/) risk (the risk that [delta](/delta/) itself moves unfavorably between rebalances).

For a farmer or commodity producer, rebalancing might be triggered by a big move in the underlying price (e.g., wheat jumps 5%)—a signal to adjust the futures position—rather than a calendar schedule.

## Costs and Risks Each Approach Leaves Unmanaged

**Static hedges are exposed to:**

- **Slippage as circumstances change:** If the underlying exposure changes (you harvest more corn than expected, or the loan grows larger), the hedge is now mismatched.
- [**Basis risk**](/basis-risk-in-hedging/): If the hedge instrument is not a perfect match, a static hedge leaves basis divergence unhedged.
- **Volatility changes:** If [implied volatility](/implied-volatility/) spikes, an option hedge's value may diverge sharply from the underlying, especially at far-OTM strikes.

**Dynamic hedges are exposed to:**

- **Transaction costs and market impact:** Especially in illiquid markets, frequent rebalancing can accumulate into a hidden tax.
- **Timing risk:** When you rebalance, you buy or sell at the market price of the moment. If you're forced to rebalance during a liquidity crunch, you might face wide bid-ask spreads.
- **Operational risk:** More moving parts (pricing models, rebalancing rules, execution systems) mean more room for error.

## Hybrid Approaches

In practice, most sophisticated hedgers use **hybrid strategies**:

- Start with a static hedge for the "base" exposure, then use dynamic hedging only for the most volatile or uncertain portion.
- Use a static hedge, but rebalance only if the underlying exposure changes significantly.
- Use threshold rebalancing: no action unless [delta](/delta/) has drifted more than X% from the target.

These approaches balance the simplicity of static hedging with the precision of dynamic hedging.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — how much an option's value changes with the underlying price
- [Gamma](/gamma/) — how much delta itself changes, and why it matters for rebalancing
- [Derivatives hedging](/derivatives-hedging/) — the general framework for hedging
- [Basis risk in hedging](/basis-risk-in-hedging/) — why even hedged positions can lose money
- [Call option](/call-option/) — the instrument often dynamically hedged
- [Put option hedge for long stock](/put-option-hedge-for-long-stock/) — a static hedge example
- [Implied volatility](/implied-volatility/) — affects rebalancing frequency and costs
- Transaction cost — the hidden drag on frequent rebalancing

### Wider context

- [Futures contract](/futures-contract/) — the instrument of choice for static commodity hedges
- Options — the driver of dynamic hedging complexity
- Portfolio rebalancing — a related concept in asset allocation
- [Counterparty risk](/counterparty-risk/) — another risk to manage alongside hedging

</div>
