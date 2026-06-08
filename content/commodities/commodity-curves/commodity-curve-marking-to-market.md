---
title: "Marking a Commodity Forward Position to Market Using the Curve"
description: "How do traders reprice commodity forwards daily? Learn how the forward curve sets unrealized mark-to-market gains and losses on open positions."
keywords:
  - marking commodity forward to market
  - forward position valuation curve
  - unrealized gains commodity futures
  - commodity forward repricing
  - forward curve mark-to-market
image: /svg/commodities.svg
---

*When a trader or company holds an open commodity [forward contract](/forward-contract/), its value changes daily as the forward curve shifts. **Marking to market** means repricing that contract to the current curve, recording the unrealized gain or loss, and adjusting cash collateral if required. The process anchors risk management and accounting for all commodity hedgers and speculators.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Marking to Market — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities." />

<div class="wiki-infobox-caption">Daily repricing of open forward positions using the current forward curve determines unrealized gains and losses.</div>

|   |   |
|---|---|
| **Mark method** | Current forward price for the same delivery month minus original contract price |
| **Updated daily** | Markets close; curve is snapshot-in-time; MTM recorded to books |
| **Collateral trigger** | Losses trigger [variation margin](/variation-margin/) calls; gains release collateral |
| **Accounting** | Under [ASC 606](/asc-606/), changes in value are often recognized in P&L |
| **Risk driver** | Curve shifts (levels, slope, shape) directly move portfolio mark |

</aside>

## What marking to market means

Suppose a refiner locked in a forward purchase of crude oil for delivery in three months at $75/barrel, with a contract size of 1,000 barrels. The total [notional](/notional-value/) value is $75,000.

A week later, the three-month crude forward contract has risen to $78/barrel. The refiner's position is now worth $78,000 in **current market terms**. The unrealized gain is $3,000 (or $3/barrel × 1,000).

That $3,000 is the **mark-to-market profit** or MTM gain. It is "unrealized" because the position has not yet settled; the refiner still owns a contract to buy at $75, and if prices later fall to $72, the gain will shrink or turn into a loss.

**Marking to market** is the daily process of:

1. Reading the current forward curve (or the relevant forward price for the delivery month).
2. Comparing it to the original contract price.
3. Calculating the gain or loss.
4. Recording it in the financial statements and risk dashboard.

This is standard practice for [derivatives](/derivatives-hedging/) and forwards under modern accounting standards ([ASC 606](/asc-606/) and IFRS 9) and is mandatory for financial institutions and many corporates.

## How the forward curve drives the mark

The forward curve is a schedule of forward prices for each future delivery month. For crude oil, it might look like:

| Month | Forward Price |
|-------|---------------|
| Jan 2026 | $74.50/bbl |
| Feb 2026 | $75.20/bbl |
| Mar 2026 | $76.10/bbl |
| Apr 2026 | $76.80/bbl |

If our refiner's three-month forward contract settles in March, the relevant forward price is **$76.10**. That is the price at which the market would trade a new March contract today. Therefore, the refiner's contract—which locked in $75.00—is now worth $76.10 in market terms.

Mark = (Current forward price − Original contract price) × Contract size
Mark = ($76.10 − $75.00) × 1,000 = **$1,100 unrealized gain**

If the curve shifts lower the next day (March forward drops to $75.80), the unrealized gain shrinks to $800. If the curve drops below $75.00, the position becomes a loss.

## Why the forward curve changes

The forward curve is not static. It shifts daily—sometimes hourly—as traders reassess supply-demand expectations, [interest rates](/interest-rate/), storage costs, convenience yield, and macroeconomic outlook.

**Parallel shifts** (entire curve moves up or down equally) affect all forward positions by the same magnitude. A refiner with a long forward position gains if prices rise; a farmer short (having pre-sold) gains if prices fall.

**Slope changes** (steepness of contango or backwardation shifts) affect positions differently depending on their maturity. A refiner with a near-term forward and a farmer with a far-term forward react opposite to a curve steepening.

**Convexity and kinks** (shape distortions, e.g., a seasonal winter premium) cause non-uniform repricing. A natural gas marketer with January and June positions sees the Jan forward rally and Jun forward fall if a cold-winter forecast emerges; the mark-to-market depends entirely on where in the curve the position sits.

## Daily MTM workflow in practice

A commodity desk typically marks positions in the evening (after market close) or in real-time during trading hours. The workflow is:

1. **Extract forward curve.** Download or subscribe to the current curve from the exchange or a data vendor (e.g., Reuters, Bloomberg).
2. **Identify contract legs.** For each open position, note the delivery month, original price, contract size, and direction (long or short).
3. **Look up current price.** Find the current forward price for that delivery month on the curve.
4. **Calculate P&L.** (Current − Original) × Size = Daily MTM gain/loss.
5. **Aggregate.** Sum all positions to get net portfolio MTM.
6. **Record it.** Post to general ledger, risk system, and management reporting.
7. **Assess collateral.** If losses exceed a threshold (set by counterparty or risk policy), trigger a variation margin call or meet collateral demand.

Large energy or metals traders may perform this continuously during market hours to monitor intraday swings.

## Collateral and variation margin

Forward contracts (especially OTC) often include collateral agreements. If a mark-to-market loss occurs, the losing party must post additional [variation margin](/variation-margin/)—cash or liquid securities—to secure the counterparty against default.

**Example**: A refiner is long a crude forward (committed to buy). Oil prices fall, and the position moves $100,000 to loss. The collateral agreement requires posting $100,000 in cash or Treasury bonds to the counterparty immediately. If the refiner cannot post, the counterparty can terminate the contract, forcing the refiner to unwind at today's worse prices.

This collateral mechanism is what makes mark-to-market not just an accounting exercise but a **real cash and credit event**. A company with inadequate liquidity can face a collateral call that forces asset sales or draws on credit lines.

## Comparison to exchange-traded futures

[Futures contracts](/futures-contract/) are marked to market daily by the clearinghouse; variation margin is automatically transferred at settlement each evening. OTC forwards require manual tracking and often have longer settlement windows, creating counterparty credit risk between mark dates.

The forward curve for a futures market is highly transparent (bid-ask spreads are published); for OTC forwards, the trader may have to interpolate or use broker quotes, introducing valuation uncertainty.

## Accounting treatment

Under [ASC 606](/asc-606/) (the revenue recognition standard) and IFRS 9 (financial instruments), the change in a forward contract's fair value is typically recognized in **profit and loss** each period, not deferred to settlement. This means a refiner locking in crude at $75 and seeing it rise to $78 must report a $3,000 gain in that quarter's earnings, even though cash does not change hands until delivery.

Hedging relationships (e.g., a refiner hedging actual feedstock purchases) can sometimes qualify for **hedge accounting**, which defers P&L matching to revenue recognition. But the underlying MTM process—repricing to the curve—is identical.

## Forward curves in different markets

Not all commodities have liquid forward curves spanning many months or years. For illiquid forward markets, traders may need to:

- Use broker quotes (which carry wider bid-ask spreads).
- Interpolate prices between quoted maturities.
- Resort to model-based pricing (discounting spot plus storage and financing costs) if no market curve exists.

For crude oil, natural gas, and metals, exchange-traded futures curves are the standard reference. For agricultural commodities, both futures and cash forward markets contribute.

## See also

<div class="wiki-seealso">

### Closely related

- Commodity Forward Curve — The sequence of forward prices across contract months
- [Forward Contract](/forward-contract/) — Over-the-counter bilateral commodity agreements
- [Basis Risk](/basis-risk/) — Risk from widening or narrowing cash-forward gap
- Convenience Yield — Why holding physical commodity sometimes beats owning the forward
- [Prompt Date and Roll Window](/prompt-date-roll-commodity/) — How expiry and rolling reshape the curve
- Marked to Market — General principles of daily position repricing

### Wider context

- [Fair Value](/fair-value/) — Definition of current market value for accounting
- [ASC 606](/asc-606/) — Revenue recognition and financial instrument standards
- [Derivatives](/derivatives-hedging/) — Hedging and speculation with forwards and options
- [Futures Contract](/futures-contract/) — Exchange-traded commodity contracts
- [Variation Margin](/variation-margin/) — Daily cash settlement of gains and losses

</div>
