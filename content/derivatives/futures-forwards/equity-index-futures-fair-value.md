---
title: "Equity Index Futures Fair Value and the Dividend Adjustment"
description: "How dividend yields affect equity index futures fair value calculation and why futures trade at a discount near ex-dividend dates."
keywords:
  - equity index futures fair value
  - cost of carry formula
  - dividend adjustment futures
  - futures discount dividend
  - index futures valuation
  - basis futures dividend
image: "/svg/derivatives.svg"
---

*The **equity index futures fair value calculation** starts with the spot price of the index and adjusts for the cost of carrying the underlying to expiration. Crucially, dividends paid by constituents between now and settlement are subtracted from that cost, because the holder of the actual index receives those dividends while the futures buyer does not—so futures trade at a discount near ex-dividend dates.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fair Value Formula — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Fair value bridges the gap between owning the index today and owning it via futures at settlement.</div>

|   |   |
|---|---|
| **Core formula** | Fair Value = Spot + (Cost of Carry) − (Dividend Yield) |
| **Cost of carry** | Interest rate × days to expiration ÷ 360 |
| **Dividend yield** | Expected cash dividends as % of index value |
| **Why it matters** | Arbitrageurs profit if futures diverge significantly from fair value |
| **Typical discount** | 0.5–2% below spot in normal conditions near ex-dates |
| **Time to expiration** | Larger contracts settle 90+ days out, widening the cost of carry |

</aside>

## The Carry Cost Baseline

Start with a simple question: if an S&P 500 index tracker trades at 5,000 today, what should a [futures-contract] expiring in exactly one month be worth?

Intuitively, if you buy the futures, you're locking in a price now but won't own the index for 30 days. In that time, you forgo the ability to invest that capital elsewhere. If risk-free interest rates are 5% per year, the cost of that one-month delay is:

**Carry Cost = 5,000 × 0.05 × (30 ÷ 365) ≈ $20.55**

So fair value before dividends would be **$5,020.55**. The future should trade above spot because you're paying for the privilege of deferring settlement.

In practice, costs of carry also include repo rates (the rate at which traders finance index positions), initial margin costs, and transaction spreads. But the core principle is the same: carrying the index forward in time has a cost, and futures must compensate the buyer for it.

## The Dividend Subtraction

Here's the crucial twist: holding the actual S&P 500 index entitles you to all dividends paid by the 500 constituents. The futures buyer receives nothing. On ex-dividend dates—when the index drops by the dividend amount—the futures holder still owns the same contract. The cash divergence grows.

If the index is expected to pay a 1.8% annual yield over the next month (a typical range), that's another cost to subtract:

**Dividend Yield Cost = 5,000 × 0.018 × (30 ÷ 365) ≈ $7.40**

Revised fair value:

**Fair Value = 5,000 + 20.55 − 7.40 = $5,013.15**

The futures now trade above spot by only $13.15 instead of $20.55. The dividend yield cuts the fair value premium by over a third.

## A Real Example: Near an Ex-Dividend Date

Suppose on June 1st the S&P 500 index trades at 5,200. Multiple large constituents will pay dividends on June 15. The expected total dividend is $9 per index point, or $46.8M if the index is notionally $5,200.

An S&P 500 [futures-contract] expiring June 20 (19 days away) now has:
- **Carry cost**: 5,200 × 0.05 × (19 ÷ 365) = $13.51
- **Dividend yield**: Expected $46.8M ÷ (5,200 × 500 contracts outstanding in index) = approximately $9 per point → 5,200 × 0.018 × (19 ÷ 365) = $4.84

Fair value: **5,200 + 13.51 − 4.84 = $5,208.67**

But wait: June 15 is *after* the futures' June 20 settlement. So dividends paid on June 15 won't be collected by the index holder before the contract settles. The buyer of June futures gets the dividends anyway, so there's no subtraction for them.

For *later* contracts (e.g., September), which settle after the June 15 ex-date, the dividend is a real cost. Futures on those later expirations will trade at a sharper discount to spot than the nearer June contract.

## Why Arbitrageurs Care

If the June futures trade at 5,205 (below fair value of 5,208.67), an arbitrageur spots a mispricing:

1. **Buy the futures contract** at 5,205.
2. **Short the index** (via an ETF or direct short) at 5,200.
3. **Hold until expiration**, collecting the dividends on the short (which go to the lender of the shares).
4. **Settle the futures** and close the short.

The arbitrage profit is roughly the gap between fair value and the actual futures price, minus transaction costs and financing. Arbitrageurs execute these trades constantly, keeping futures prices in line with the fair value formula.

Conversely, if futures trade significantly *above* fair value, index traders will buy the spot index, short futures, and lock in a risk-free return. Both trades push prices back to equilibrium.

## The Cost-of-Carry Formula in Full

The complete formula used by traders:

**Fair Value = Spot × [1 + r × (T/360)] − (Dividends × Present Value Factor)**

Where:
- **r** = risk-free rate (repo or Treasury yield)
- **T** = days to settlement
- **Dividends** = expected cash dividends per share × number of shares in the index
- **Present Value Factor** accounts for the exact timing of each dividend payment

For quarterly-paying indices like the S&P 500, the dividends are lumpy (concentrated in March, June, September, December). Futures expiring immediately after a dividend month will show a sharper discount than those expiring in the off months.

## Convergence and the Final Day

As a [futures-contract] approaches expiration, its price must converge to the spot index value. The fair value formula still holds, but with T approaching zero, the carry cost shrinks to zero, and any remaining dividends have already been paid. On the settlement day itself, the futures and spot prices are typically identical (or differ only by a penny or two due to rounding).

This convergence is guaranteed by arbitrage. If September futures trade at a 50-cent discount on the day of settlement, arbitrageurs buy futures and short spot, locking in an instant profit. The buying pressure on futures drives the price up to parity.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures-Contract](/futures-contract/) — The derivative instrument being priced
- [Dividend](/dividend/) — The cash payment that reduces futures fair value
- [Interest-Rate-Risk](/interest-rate-risk/) — How rate changes affect the carry cost
- [Basis-Risk](/basis-risk/) — The risk that futures and spot prices diverge unexpectedly
- [SP-500-Index](/sp-500-index/) — The underlying for the most heavily traded index futures

### Wider context

- [Derivatives-Hedging](/derivatives-hedging/) — Common uses of index futures
- [Forward-Contract](/forward-contract/) — The theoretical concept fair value is based on
- [Market-Maker-Trading](/market-maker-trading/) — Who actively arbitrages mispricings
- [Financial-Reporting-Standards](/international-financial-reporting-standards/) — How futures positions are marked in financial statements

</div>
