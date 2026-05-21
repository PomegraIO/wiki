---
title: "Commodity Swap"
description: "A swap that exchanges fixed or floating payments based on commodity prices, used to hedge price volatility or lock in costs."
---

*A commodity swap is a contract where two parties exchange cash flows tied to the price of a physical commodity—oil, gold, wheat, copper, or others. One party typically pays a fixed average price; the other pays the floating market price. The swap settles in cash at intervals, with no physical commodity changing hands.*

<aside class="wiki-infobox">
<div class="wiki-infobox-title">Commodity Swap — key facts</div>
<table>
<tr><th>Underlying</th><td>Any commodity (energy, metals, agricultural).</td></tr>
<tr><th>Typical notional</th><td>Measured in physical units (barrels, tons, bushels); cash settlement in currency.</td></tr>
<tr><th>Typical use</th><td>Hedging commodity price exposure for producers and consumers.</td></tr>
<tr><th>Settlement</th><td>Cash, based on the difference between fixed and floating price.</td></tr>
</table>
</aside>

## Why commodity swaps matter

Commodity producers (oil drillers, miners, farmers) and consumers (refineries, utilities, food makers) face severe price risk. Crude oil might surge from $80 to $120 per barrel in months, obliterating profit margins or consuming a year's budget in fuel costs. A commodity swap lets both sides lock in a known price, even as the market swings wildly.

Unlike a [futures contract](/wiki/futures-contract/), which is exchange-traded and standardized, a commodity swap is over-the-counter (OTC). It can be tailored to a producer's or consumer's exact schedule and volume needs. A refinery that runs 50,000 barrels per day can swap all 50,000, and the swap can match the refinery's seasonal ramp-up and ramp-down rather than forcing it into rigid 1,000-barrel lot sizes.

## Structure

A typical commodity swap has two legs:

- **Fixed leg**: One party pays a fixed price per unit (e.g., $75 per barrel of oil) on a notional quantity.
- **Floating leg**: The other party pays the market price of the commodity, usually the price on a reference exchange (e.g., crude oil traded on NYMEX or ICE) or a pricing service.

Settlement is typically monthly or quarterly. The difference between the two prices is multiplied by the notional quantity and settled in cash. If the fixed price is $75 and the market price settles at $80, the fixed-price payer owes the floating-price payer $5 per barrel times the notional quantity.

## Why the swap structure beats futures

For a mining company hedging gold output, a commodity swap offers advantages over [futures contracts](/wiki/futures-contract/):

1. **Custom quantities**: A mine might produce 1,500 ounces per month of gold. Futures contracts trade in standard 100-ounce lots. A swap can lock in 1,500 ounces directly.

2. **Matching cash flow timing**: A swap settles when the company prefers (monthly, quarterly, at shipment), while futures require active rolling and margin management.

3. **Customized baselines**: A swap can reference the exact grade or location of the commodity. Crude oil, for instance, trades in many varieties (West Texas Intermediate, Brent, Dubai). A refinery that processes a blend of oils can swap to reflect its actual feedstock mix rather than a single NYMEX contract.

4. **Operational simplicity**: No [margin calls](/wiki/initial-margin/) or daily mark-to-market settlement; a single monthly or quarterly cash flow occurs.

## Common structures

**Simple fixed-float**: One party pays a fixed price; the other pays market. Straightforward and common.

**Commodity index swap**: The floating leg is tied to an index of commodity prices rather than a single commodity. A food company might swap to an index that captures grain, oil, and other ingredients it uses.

**Basis swap on commodities**: Two parties exchange floating payments tied to different price indices (e.g., WTI crude vs. Brent, or crude vs. products). A refinery that runs both types of crude might use this to neutralize basis risk.

**Staged commodity swap**: The fixed price or notional changes over time. For example, a contract for 10 years where the notional declines 5% per year as production is expected to fall.

## Valuation and pricing

Dealers price commodity swaps by:

1. Projecting forward prices of the commodity using [futures curves](/wiki/contango/) and [forward contracts](/wiki/forward-contract/).
2. Discounting expected cash flows back to present value.
3. Solving for the fixed price that equates the two legs in value.

The fixed swap price is typically the average of forward prices for the swap's life, adjusted for convenience yield (the benefit of holding physical commodity instead of a futures contract) and credit spreads.

For commodities with [contango](/wiki/contango/) (forward prices are higher than spot), the swap price is usually above the current spot price. For [backwardation](/wiki/backwardation/) (forward prices below spot), the swap price is below spot. This is economically rational: if you lock in a price below the expected future price, you are getting a deal.

## Users

**Commodity producers** (oil companies, mining firms, agricultural processors) use swaps to lock in revenue at a price that covers their costs and returns a profit, regardless of market moves.

**Commodity consumers** (utilities, refineries, food manufacturers, chemical plants) use swaps to lock in their input costs, making margins predictable.

**Utilities** use [electricity](/wiki/electricity-as-commodity/) and natural gas swaps to stabilize operating costs.

**Traders and hedge funds** sometimes use commodity swaps to take positions on prices. If a trader believes [crude oil](/wiki/crude-oil/) is underpriced, they might go long a commodity swap, benefiting if the market price rises above the fixed rate they locked in.

## Risks

**Counterparty risk**: The other party might default. A commodity producer that enters a swap to lock in revenue is at risk if the swap dealer or counterparty fails.

**Price basis risk**: The swap price is tied to a reference index, but the producer or consumer may face a different price. A small refinery may not get NYMEX prices; it might pay a local premium. The swap doesn't fully cover that risk.

**Liquidity risk**: If you need to exit a commodity swap early, dealers may quote a wide spread or be unwilling to trade at all. Liquidity varies by commodity.

**Model risk**: Valuation depends on forward curves and convenience yield, which are estimated. Disagreements on these inputs can lead to wide bid-ask spreads.

**Operational risk**: If the commodity is not delivered or the market price cannot be fixed reliably (e.g., during a supply shock or exchange closure), settlement disputes may arise.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the parent swap structure.</li>
<li><a href="/wiki/futures-contract/">Futures contract</a> — the exchange-traded alternative to commodity swaps.</li>
<li><a href="/wiki/forward-contract/">Forward contract</a> — another OTC alternative to swaps.</li>
<li><a href="/wiki/commodity-etf/">Commodity ETF</a> — a simpler way for retail investors to gain commodity exposure.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/contango/">Contango</a> — forward prices above spot, affects commodity swap pricing.</li>
<li><a href="/wiki/backwardation/">Backwardation</a> — forward prices below spot.</li>
<li><a href="/wiki/crude-oil/">Crude oil</a> — the most actively swapped commodity.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the main risk in OTC swaps.</li>
</ul>
</div>
