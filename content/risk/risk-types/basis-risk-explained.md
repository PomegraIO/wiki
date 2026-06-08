---
title: "Basis Risk Explained"
description: "Basis risk is the residual exposure that remains when a hedge uses a related but imperfect substitute, leaving the spread between asset and hedge free to move."
keywords:
  - basis risk hedging
  - what is basis risk
  - hedge imperfect substitute
  - basis spread
  - hedging residual risk
---

*A **basis risk** is the risk that a [hedge](/derivatives-hedging/) using a related but non-identical instrument will fail to offset losses dollar-for-dollar because the spread between the hedged asset and the hedge instrument moves unpredictably.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basis Risk — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Perfect hedges rarely exist; most hedges leave a residual spread risk that can multiply or shrink the effective loss.</div>

|   |   |
|---|---|
| **Basis definition** | Spot price minus futures (or hedge instrument) price |
| **Hedger's loss** | Occurs when basis widens or narrows unexpectedly, moving against the intended offset |
| **Perfect hedge scenario** | Basis is zero; this is rarely achieved in practice |
| **Common culprits** | Grade differences, delivery location, timing mismatch, counterparty credit |
| **Examples** | Corn miller hedging with wheat, airline hedging jet fuel with crude oil, investor hedging stock-index gap |
| **Liquidity link** | Liquid, standardized hedges (S&P 500 futures) have tighter, more predictable basis than niche assets |

</aside>

## The Basics: Why Hedges Are Imperfect

An ideal [hedge](/derivatives-hedging/) would lock in a price or value, eliminating all risk. A corn processor expecting to buy corn in three months could, in theory, buy a corn futures contract now, agreeing to accept delivery at a pre-set price. When spot price rises, the futures gain balances the higher purchase cost; when it falls, the futures loss offsets the lower cash cost. Zero net exposure.

In practice, no such symmetry exists. The futures contract specifies a particular grade, quality, and delivery location. The actual corn the processor buys will differ slightly. Futures may settle in Kansas City; the processor sources from Iowa. Futures specify No. 2 yellow corn; the processor occasionally buys No. 3. The result is a *spread* between what the futures price moved and what the cash price moved. This spread—called the **basis**—becomes the unhedged remainder.

**Basis** is defined formally as the spot (cash) price minus the futures (or other hedge instrument) price. If corn in Iowa is trading at $5.00 per bushel and December futures are at $4.95, the basis is +$0.05. When the processor buys actual corn and offsets the futures, that +$0.05 gap is retained. If the basis widens to +$0.10 before the hedge is lifted, the processor loses money on the basis move alone, even though the overall price move was hedged.

## Why Basis Moves Unexpectedly

Basis is not static. It shifts due to:

**Convergence to delivery.** As futures contracts approach expiration, their price converges toward the spot price. A trader holding a futures position into delivery faces this inexorable convergence. For most participants, convergence is predictable and manageable; the basis tightens on schedule.

**Supply and demand shocks.** If a weather event damages corn in Iowa but not Kansas, the Iowa basis (cash price relative to Kansas-delivery futures) will widen. The local shortage makes actual cash corn more valuable relative to the standardized futures. A processor hedged with Kansas futures is now under-protected.

**Grade and quality differentials.** If a hedger locks in a hedge using a standard grade but then must buy higher-quality material (commanding a premium), the basis widens against the hedger. An airline hedging heating oil (a low-grade refinery product) with crude-oil futures is exposed to the spread between crude and refined products; if refineries suddenly command higher margins, crude futures do not capture the full move.

**Counterparty and credit effects.** The basis on a corporate bond futures contract may widen if the underlying issuer's credit rating drops sharply, causing the cash bond to fall faster than the futures, which settle into a more generic index. The credit-driven spread is not captured by the hedge.

**Timing mismatches.** A hedger expecting to hold a position for six months may use a three-month futures contract, rolling it forward at expiration. If the roll is executed at an unfavorable spread, basis risk crystallizes. An equity-index portfolio manager hedging S&P 500 exposure with Russell 2000 futures faces permanent basis risk because the indices move differently over time.

## Real-World Examples

**Airline fuel hedging:** An airline knows it will burn 100 million gallons of jet fuel next quarter. It buys crude-oil futures to hedge. But jet fuel is refined; its relationship to crude oil depends on refinery margins and supply-demand for refined products. If a refinery shuts down temporarily, refined-fuel prices spike while crude lags. The airline's futures hedge is insufficient. The basis widens, and the airline pays more in actual fuel than the futures gain covers. This is basis risk realized.

**Corn miller.** A miller knows he will need 1 million bushels of corn in four months. Corn futures exist, but he buys corn-futures contracts. However, corn prices vary by location (basis varies geographically). If he is located in the Southeast, where basis is typically +$0.15 to the Kansas City futures, a drought in the Midwest (reducing supply locally and widening the local basis) means his actual cost rises faster than the Kansas City futures move. He is under-hedged.

**Stock-portfolio beta hedging.** An equity manager holds a $50 million portfolio concentrated in tech stocks and wants to hedge market risk. He sells S&P 500 futures. But the portfolio outperforms the index when growth stocks rally and underperforms when value stocks rally. The basis—the performance gap between his portfolio and the index—moves unexpectedly. In a sector rotation, basis risk can be substantial.

## Measuring Basis Risk

Hedgers typically estimate basis risk by examining historical correlations and spreads. A strong correlation between the cash asset and the hedge instrument suggests lower basis risk. Conversely, weak correlation means the basis is more likely to move substantially.

Basis risk can be quantified using [Value-at-Risk](/value-at-risk/) (VaR) applied to the basis spread itself, not the underlying asset. A hedger might calculate: "In 95% of outcomes, the basis moves by no more than $0.08. In 5% of scenarios, it moves by more." This sets realistic expectations for residual exposure.

Some hedgers use a ratio: if the correlation between cash and futures is 0.95, they might over-hedge by 5% (buy 105 futures contracts to cover 100 units of the cash asset) to absorb expected basis widening. This is often called **basis adjustment** or **tailing the hedge**.

## When Basis Risk Becomes Material

Basis risk is trivial when:
- The hedged asset and hedge instrument are identical (e.g., hedging an S&P 500 ETF with S&P 500 futures).
- The correlation is near-perfect and historically stable.
- The basis is very small relative to price volatility.

Basis risk becomes material when:
- The hedged asset and hedge are poor substitutes (e.g., international equity index hedged with domestic futures).
- The time horizon is long, allowing basis to drift significantly.
- The basis itself is volatile—it moves unpredictably day-to-day.
- Delivery locations, grades, or settlement mechanics differ substantially.

## Practical Mitigation

Sophisticated hedgers:
1. **Choose the tightest hedge available.** Use a futures contract on the exact asset or its nearest liquid proxy.
2. **Use cross-hedges selectively.** If hedging an illiquid asset (e.g., a single stock position) with an index future, acknowledge the basis risk explicitly and size accordingly.
3. **Monitor basis regularly.** Track the historical range of the basis spread and alert to widening that suggests shifting market structure.
4. **Adjust dynamically.** As the basis-forecast changes, rebalance the hedge ratio to maintain desired risk exposure.
5. **Diversify hedge instruments.** For large exposures, use multiple instruments (futures, options, swaps) to reduce reliance on a single imperfect hedge.

## See also

<div class="wiki-seealso">

### Closely related

- [Derivatives & Hedging](/derivatives-hedging/) — foundation for understanding basis risk in hedging strategies
- [Futures Contract](/futures-contract/) — primary instrument in which basis risk manifests
- [Counterparty Risk](/counterparty-risk/) — credit changes can widen basis unexpectedly
- [Concentration Risk in a Small Portfolio](/concentration-risk-small-portfolio/) — basis risk magnifies concentrated exposures
- [Interest-Rate Swap](/interest-rate-swap/) — basis risk applies to swap spreads as well

### Wider context

- Correlation — statistical relationship underlying basis-risk prediction
- [Value-at-Risk](/value-at-risk/) — framework for quantifying basis-risk tails
- [Hedge Fund](/hedge-fund/) — actively manages basis risk in complex hedges
- [Commodity](/copper/) — agricultural and energy commodities carry large, unpredictable basis risk

</div>
