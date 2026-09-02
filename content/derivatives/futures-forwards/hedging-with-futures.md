---
title: "Hedging with Futures"
description: "Using futures contracts to transfer price risk to speculators—locking in costs or revenues and allowing businesses to focus on operations rather than market moves."
---

*A farmer will harvest wheat in three months. The price of wheat could fall 30% or rise 30%. This uncertainty is dangerous. By shorting [futures](/wiki/futures-contract/), the farmer locks in today's price and removes the guessing game.*

## The hedging principle

Hedging is the transfer of risk from someone who does not want it to someone who does. In [futures](/wiki/futures-contract/) markets:

- **The hedger** has real exposure (a farmer will harvest wheat, an airline will buy fuel, a manufacturer will buy copper). They use [futures](/wiki/futures-contract/) to lock in prices.
- **The speculator** has no real exposure but believes they can predict future prices. They take the other side of the hedger's trade.

Both sides benefit: the hedger gets certainty; the speculator gets a chance to profit.

## Agricultural hedging: the classic example

A farmer plants 5,000 bushels of corn. At planting time (April), corn [futures](/wiki/futures-contract/) are $6.00 per bushel. The farmer does not know if corn will be $5.00 or $7.00 at harvest (September).

**Unhedged:** The farmer hopes corn rises but faces full downside if it falls to $4.00. A $2 move is a $10,000 loss—catastrophic for a typical farm.

**Hedged:** The farmer shorts 5,000 bushels of September [futures](/wiki/futures-contract/) at $6.00.

At harvest (September), suppose corn has fallen to $4.50:
- Spot corn: $4.50 per bushel. Farmer can sell 5,000 bushels for $22,500.
- [Futures](/wiki/futures-contract/) position: Farmer bought back (closed) the short at $4.50. Profit on the [futures](/wiki/futures-contract/): 5,000 × ($6.00 - $4.50) = $7,500.
- Total revenue: $22,500 + $7,500 = $30,000 (equivalent to $6.00/bushel).

The farmer locked in $6.00 per bushel despite the price fall. The [futures](/wiki/futures-contract/) short offset the spot price decline.

If corn had risen to $7.50:
- Spot corn: $7.50 per bushel. Farmer sells for $37,500.
- [Futures](/wiki/futures-contract/) loss: 5,000 × ($7.50 - $6.00) = -$7,500.
- Total revenue: $37,500 - $7,500 = $30,000 (equivalent to $6.00/bushel).

Again, the farmer locked in $6.00, sacrificing upside in exchange for eliminating downside. This is the hedging trade: certainty over speculation.

## Duration-based hedging in borrowing

A company planning to borrow $10 million in three months faces [interest rate](/wiki/interest-rate/) risk. If rates rise, their [cost of debt](/wiki/cost-of-debt/) increases.

**Unhedged:** Rates could jump from 5% to 6%, adding $100,000 per year to financing costs.

**Hedged:** The company sells [Treasury](/wiki/treasury-bond/) [futures](/wiki/futures-contract/) (or uses [interest rate swaps](/wiki/interest-rate-swap/)) locking in a rate. If rates rise to 6%, the [futures](/wiki/futures-contract/) position gains, offsetting higher borrowing costs.

The company locks in an all-in [cost of debt](/wiki/cost-of-debt/), enabling board-level budget certainty.

## Foreign exchange hedging

A US exporter selling goods to Japan in six months is owed 100 million yen. At today's rate (140 yen/dollar), that is $714,000.

If the yen weakens to 150 per dollar, the exporter receives only $667,000—a $47,000 loss.

**Hedged:** The exporter sells yen [futures](/wiki/futures-contract/) (contracts to deliver yen and receive dollars) locking in 140. At settlement, regardless of the spot rate, the exporter converts at 140, netting $714,000.

This is critical for companies with long supply chains spanning multiple countries. A German manufacturer importing parts from Asia and selling in North America faces multiple [currency risks](/wiki/currency-risk/). [Futures](/wiki/futures-contract/) and [forwards](/wiki/forward-contract/) allow them to lock in all pieces, making the economics predictable.

## Commodity hedging for manufacturers

A food company processes cocoa into chocolate. They need to buy cocoa beans and sell chocolate. Their profit depends on the margin between cocoa prices and chocolate selling prices.

When cocoa prices rise, input costs rise. The company can hedge cocoa [futures](/wiki/futures-contract/) (going long, to offset the risk of rising spot cocoa costs) or equivalently, lock in a cocoa input price. Alternatively, they might hedge the spread: lock in the margin between buying cocoa [futures](/wiki/futures-contract/) and selling chocolate (if chocolate futures exist) or selling finished goods forward.

Airlines hedge jet fuel, refineries hedge crude and products (via [crack spreads](/wiki/spread-trading-futures/)), and mining companies hedge metals. In each case, the goal is the same: isolate the business risk (the skill of the operator) from market-price risk (which is uncontrollable).

## Basis risk and imperfect hedges

A perfect hedge leaves zero risk. But in practice, perfect hedges often do not exist:

- **Grade mismatch:** A farmer with slightly off-spec corn cannot deliver into [futures](/wiki/futures-contract/), so the [futures](/wiki/futures-contract/) hedge does not fully offset spot-price moves.
- **Location mismatch:** A farmer 200 miles from the approved delivery point faces logistics costs that are not perfectly correlated with the spot-futures spread.
- **Duration mismatch:** A hedger needing to lock in a price in October but holding December [futures](/wiki/futures-contract/) faces the risk that the [basis](/wiki/basis/) changes between October and December.
- **Cross-hedges:** A company hedging aluminum with copper [futures](/wiki/futures-contract/) (if aluminum [futures](/wiki/futures-contract/) do not exist) faces the risk that aluminum and copper move differently.

These imperfect hedges leave [basis risk](/wiki/basis-risk/), but that is acceptable: [basis](/wiki/basis/) risk is usually much smaller than directional price risk.

## The hedge ratio

A sophisticated hedger calculates the optimal hedge ratio: how much [futures](/wiki/futures-contract/) to short per unit of spot exposure.

If a company expects to buy 100,000 barrels of oil but wants to hedge 70% of the downside (accepting 30% unhedged), they short 70,000 barrels of crude [futures](/wiki/futures-contract/).

Or if the company has cross-hedge risk (hedging oil purchases with natural gas [futures](/futures-contract/), they estimate correlation: if oil and gas correlate 0.8, they short 80,000 barrels of gas [futures](/wiki/futures-contract/) for every 100,000 barrels of oil exposure.

These calculations are statistical, not prophetic. But they guide better decisions than unhedged guesses.

## When hedging fails

Hedges break down when:

1. **Correlations shift:** A cross-hedge (e.g., oil vs. natural gas) assumes a stable correlation. During crises, correlations often spike to 1.0 or even shift. A hedge that worked for 20 years can fail overnight.

2. **Liquidity disappears:** A hedger might short 10,000 [futures](/futures-contract/) contracts, but if the market freezes and no one is buying, the hedger cannot close the position without moving the price drastically. They are stuck with the [futures](/wiki/futures-contract/) exposure while spot positions shift.

3. **Funding risk:** A leveraged hedger must post [variation margin](/wiki/variation-margin/) daily. A sharp adverse move in the hedged asset can force variation margin calls, depleting cash and forcing early liquidation even though the long-term hedge is sound.

4. **Basis risk becomes too large:** If the [basis](/wiki/basis/) widens unexpectedly, the hedge backfires. A farmer locking in $5.00 per bushel via [futures](/futures-contract/) at spot $4.80 expects the [basis](/wiki/basis/) to be -$0.20 at harvest. If the [basis](/wiki/basis/) widens to -$0.50 at harvest, the effective locked-in price is $4.50, worse than the original spot.

The 2008 financial crisis saw multiple hedge failures as correlations shifted and liquidity dried up simultaneously. Companies that were "hedged" found themselves underwater as hedges stopped working.

## Hedging vs. speculation

The line between hedging and speculation blurs in practice:

- A farmer hedging a future harvest is hedging.
- A farmer speculating on future wheat prices by holding unhedged short positions is speculating.
- A company hedging its cost of debt by selling Treasury [futures](/futures-contract/) is hedging.
- A fund buying Treasury [futures](/futures-contract/) betting on falling rates is speculating.

The CFTC and exchanges track hedging positions separately from speculative ones, enforcing position limits more leniently on hedgers (who have real exposure) than speculators (who do not). But this distinction depends on honest reporting and is not always waterproof.

## The economics of successful hedging

When a hedge works well, the hedger typically:
- Locks in a known cost or revenue within 1-2% of the contract price.
- Avoids extreme outcomes (bankruptcy, forced production shutdowns) while sacrificing some upside.
- Can borrow more cheaply (lenders see lower risk) and invest in growth rather than fighting market volatility.

The benefit is not a profit but a **reduction in uncertainty**, which translates to lower risk premiums, better access to capital, and focus on core business.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/futures-contract/">Futures contract</a> — the standardized instrument enabling hedging.</li>
<li><a href="/wiki/basis/">Basis</a> — the spot-futures spread that determines hedging efficiency.</li>
<li><a href="/wiki/basis-risk/">Basis risk</a> — the residual risk remaining after an imperfect hedge.</li>
<li><a href="/wiki/cost-of-carry/">Cost of carry</a> — storage and financing costs embedded in hedging prices.</li>
<li><a href="/wiki/spread-trading-futures/">Spread trading</a> — hedging margins by betting on relative prices rather than absolute moves.</li>
<li><a href="/wiki/variation-margin/">Variation margin</a> — daily cash settlements that create funding challenges for hedgers.</li>
<li><a href="/wiki/forward-contract/">Forward contract</a> — the OTC alternative to [futures](/wiki/futures-contract/) for hedging custom exposures.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li>Derivatives — the broader category of risk-transfer instruments.</li>
<li>Risk management — the strategic practice of hedging specific exposures.</li>
</ul>
</div>
