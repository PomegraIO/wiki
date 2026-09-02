---
title: "Spread Trading (Futures)"
description: "A strategy betting on the relative change between two futures prices—buying one contract and shorting another—to profit from mean reversion or exploitable mispricing between related contracts."
---

*A speculator convinced oil will rise might buy crude futures. But an experienced trader who sees crude in [contango](/wiki/contango/) might instead buy nearby crude and short distant crude—a spread bet. The directional view is gone; the bet is purely on the shape of the curve.*

## Intra-commodity spreads

The most common spread trades occur within a single commodity. A trader might:

- **Buy nearby, short distant:** This is a [calendar spread](/wiki/expiration-contracts/) (or time spread). If the trader thinks the current [contango](/wiki/contango/) is excessive, they buy September crude (cheap relative to history) and short December crude (expensive relative to history), betting the spread will compress.
- **Exploit seasonality:** Crude oil futures often experience patterns: demand spikes in winter (heating), refining margins improve in summer. A trader might systematically short heating oil in summer and buy it in fall, betting on mean-reverting seasonal patterns.
- **Capture [basis](/wiki/basis/) plays:** If a refinery sees crude futures significantly out of line with spot crude, they can buy spot crude, store it, and simultaneously short futures. They profit if the [basis](/wiki/basis/) converges, locking in the storage spread without directional exposure.

Calendar spreads are less [volatile](/wiki/historical-volatility/) than outright positions. Instead of riding out a $5 move in crude (losing or gaining money on the entire position), a calendar spread participant earns or loses based on whether the spread changes by 50 cents. This lower volatility allows higher leverage, since margin requirements for spreads are lower than for outright directional bets.

## Commodity complex spreads

Commodity markets are interconnected. Spreads often exist between related commodities:

- **Crack spread:** Long crude oil, short [gasoline](/wiki/gasoline/) and [heating oil](/wiki/heating-oil/). This mimics a refinery's economics—buying crude and selling refined products. The spread widens when refining margins expand (demand for refined products is strong relative to crude) and narrows when margins compress (oversupply of refined products).
- **Crush spread:** Long [soybeans](/wiki/soybeans/), short [soybean oil](/wiki/soybean-oil/) and [soybean meal](/wiki/soybean-meal/). This mimics a crusher's economics (a processor who crushes soybeans into oil and meal). When the spread is attractive, crushers buy soybeans and sell oil and meal simultaneously.
- **Spark spread:** Long [natural gas](/wiki/natural-gas/), short [electricity](/wiki/electricity-as-commodity/). This mimics a power generator's economics. When spark spreads widen, generators buy natural gas and sell electricity contracts, locking in generation margins.

These spreads exist because the underlying businesses exist. Refiners actually do crack crude into products. Crushers actually crush soybeans. Power plants actually burn gas to make electricity. When spreads are attractive, real economic actors step in and transact, keeping spreads aligned with true operating margins.

For traders without physical operations, these spreads are pure bets on whether the economic relationship will hold. A trader might believe next year's refining margins will be stronger than the crack spread implies, so they buy the spread (long crude, short products), betting margins will expand and the spread will widen.

## Cross-commodity spreads

Spreads also exist between unrelated commodities:

- **Energy-Metals:** Traders might trade [crude oil](/wiki/crude-oil/) against [copper](/wiki/copper/), betting on relative risk-asset demand or global growth. When growth fears hit, both typically fall, but metals might fall harder because they are more correlated with industrial demand.
- **Agriculture Complex:** Spreads between different grains ([corn](/wiki/corn/) vs. [wheat](/wiki/wheat/)) or different animal feeds ([soybean meal](/wiki/soybean-meal/) vs. [corn](/wiki/corn/)) encode relative supply and demand for each.

These spreads are looser than commodity-complex spreads (crude, products, and the refining margin are mechanically linked). They exist because traders believe there are exploitable mispricings, and the spread can revert to historical norms or correlations.

## The mechanics of execution

A spread trade is typically executed as a single order: "Buy Dec crude, sell Mar crude at a fixed spread." The trader specifies the spread (e.g., "Buy Dec at -50 cents to Mar," meaning buy December at a price 50 cents below March). The order sits until matched with a counterparty willing to take the opposite side.

[Bid-ask spreads](/wiki/etf-bid-ask-spread/) on spread orders are often tighter than on outright positions. A Dec-Mar crude spread might trade at 3 cents wide, while an outright December contract might trade at 5 cents wide. This is because the spread is a lower-volatility product (you are hedging one leg with the other), so market makers can afford to offer tighter pricing.

## Risk in spread trading

Spreads are not risk-free, even though they isolate relative movement. A trader long the Dec-Mar spread (long Dec, short Mar) is betting the spread will narrow. But the spread is determined by [cost of carry](/wiki/cost-of-carry/): the March contract should be worth December plus the cost of carrying crude from December to March.

If interest rates rise unexpectedly, the cost of carry increases, the Mar contract becomes more expensive relative to Dec, and the spread widens against the trader. The trader faces "curve risk"—the risk that the term structure changes independent of spot prices.

Moreover, spreads can blow out unpredictably. During the March 2020 oil crash, spreads that had been stable for years suddenly widened dramatically as traders fled and liquidity dried up. A trader holding a tight spread with leverage faced forced liquidation.

## Margin efficiency

Regulatory and exchange-specific rules allow lower margin requirements for spread positions compared to outright positions. A trader might require 10% margin to hold a long crude oil position outright. That same trader might require only 3% margin to hold a 12-month calendar spread in crude (because the spread is lower-volatility).

This margin efficiency is why sophisticated traders prefer spreads to outright positions when appropriate: they can deploy capital more efficiently and concentrate on the specific bet they want to make (curve shape, relative supply and demand between two products) rather than spot price direction.

## When spreads work and when they don't

Spreads work best when:
- **Economic relationships are stable.** Refining margins have persisted for decades because the underlying chemistry and economics of refining do not change.
- **Liquidity exists in both legs.** If one leg of the spread is thinly traded, execution becomes costly and risky.
- **Mean reversion is likely.** Spreads that are extreme by historical standards (at the 95th percentile of width) are good candidates for reversal trades.

Spreads break when:
- **The underlying relationship shifts.** A structural change in refining economics (emissions regulations, switch to renewable fuels) can render historical spread relationships obsolete.
- **Market structure changes.** Liquidity can vanish suddenly; a formerly tight spread can widen to 50 cents or more in minutes if traders flee.
- **New information arrives that affects one leg more than the other.** A geopolitical event affecting oil supply will widen the crude-product spread because crude reacts more than already-priced refined products.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/contango/">Contango</a> — forward contracts more expensive than spot, the starting point for many calendar spreads.</li>
<li><a href="/wiki/basis/">Basis</a> — the spot-futures difference, which spread traders often exploit to lock in economic returns.</li>
<li><a href="/wiki/cost-of-carry/">Cost of carry</a> — storage and financing costs that determine fair value between contract months.</li>
<li><a href="/wiki/arbitrage-pricing-theory/">Arbitrage</a> — the mechanism that keeps spreads aligned with economic fundamentals.</li>
<li><a href="/wiki/pairs-trading/">Pairs trading</a> — the equity markets equivalent of commodity spread trading.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/futures-contract/">Futures contract</a> — the vehicle enabling spread trades through multiple standardized contracts on the same or related underlyings.</li>
<li>Derivatives — overview of the broader category that includes all leveraged and spread-trade opportunities.</li>
</ul>
</div>
