---
title: "Commodity Index Spot Return vs Excess Return vs Total Return"
description: "Understand the three commodity index return series: spot, excess, and total returns—what each includes, how they differ, and when to use each for fair performance comparison."
keywords:
  - commodity index spot return
  - commodity index excess return
  - commodity index total return
  - commodity returns comparison
  - commodity index performance
  - futures roll cost
---

*A **commodity index spot return** tracks the price change of the underlying physical commodities; **excess return** adds the income from rolling futures; **total return** blends both, alongside any financing adjustments. Knowing which series you're analyzing is essential to understanding what a manager or index actually earned.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Commodity Index Returns — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Three parallel return series tell different stories about commodity performance.</div>

|   |   |
|---|---|
| **Spot return** | Pure commodity price movement, no roll costs or financing |
| **Excess return** | Spot plus roll yield from [futures-contract](/futures-contract/) curve positioning |
| **Total return** | Excess return plus financing (lending/borrowing) adjustments |
| **Roll yield** | Profit (contango) or loss (backwardation) from rolling expiring contracts |
| **When prices rise together** | All three series move in sync; roll matters more in sideways markets |
| **Common use** | Institutional benchmarking; passive index funds publish all three |

</aside>

## Why Three Separate Return Series Exist

Commodity indices are constructed differently from stock or bond indices. A stock index simply holds the shares; the return is the price change plus dividends. But a commodity index cannot practically store physical oil or wheat. Instead, it gains exposure through [futures-contract](/futures-contract/) positions that must be rolled (closed out and reopened) as contracts near expiration.

This rolling process creates a structural return component—the **roll yield**—that is separate from the underlying commodity price movement. Modern commodity index publishers report three returns to let users see each piece independently. A manager choosing between strategies, or an investor comparing two commodity index funds, needs to know which return is being quoted. Spotting the difference can reveal why an index outperformed or lagged.

## Spot Return: The Commodity Price Change Alone

**Spot return** is the simplest: it is the change in the spot (or nearest-contract) commodity price, plus any coupon-like payments. If crude oil trades at $80/barrel on January 1 and $85/barrel on December 31, the spot return is approximately +6.25%, regardless of futures contract rolls.

Spot return isolates the pure commodity value movement. It answers the question: "If I could costlessly hold the physical commodity, what would my return be?" In practice, you cannot do this for all commodities (storing crude oil or copper requires infrastructure), but spot return is the economically "clean" baseline.

Spot returns are useful for:
- Comparing long-term commodity trends across different time periods
- Understanding the actual commodity value proposition without operational noise
- Assessing [basis](/basis/) changes and storage dynamics in grain or energy markets

However, spot return does not reflect what a real investor experiences. It ignores the cost of rolling futures or any financing charges.

## Excess Return: Adding the Roll Yield

**Excess return** = spot return + roll yield.

Roll yield is the profit or loss from rolling [futures-contract](/futures-contract/) positions as they near expiration. When the [futures-contract](/futures-contract/) curve is in [contango](/contango/)—meaning further-out contracts trade higher than nearer ones—rolling is mechanically unfavorable. You sell a nearby contract and buy a farther-out one at a higher price, effectively realizing a loss. The opposite happens in [backwardation](/backwardation/): selling the nearby contract and buying the further-out one at a lower price produces a gain.

Consider a stylized example:
- January futures for crude oil: $80/barrel
- March futures for crude oil: $82/barrel
- The index holds January; rolls to March when January expires
- The index **loses** $2 per barrel rolling from January to March (contango cost)
- If crude spot price held flat, the excess return would be negative despite stable supply and demand

Over a full year, this roll cost compounds. In deeply contangoized markets (common during supply gluts), the excess return can substantially lag the spot return. In backwardated markets, excess return can outpace spot return.

Excess return is closer to what an index fund investor actually sees, because it includes the real cost of staying invested in the futures curve.

## Total Return: Including Financing Adjustments

**Total return** = excess return + financing adjustment (or equivalently, spot return + roll yield + financing).

The financing adjustment reflects the interest cost or rebate earned on the cash collateral securing the [futures-contract](/futures-contract/) positions. When an investor holds a [futures-contract](/futures-contract/), margin (collateral) is posted. In low interest-rate environments, the cost of posting that collateral is small. In high rates, it becomes material.

A simplified example:
- Excess return: +3%
- Cash collateral earning very low interest rate (e.g., 0.25%)
- Total return: approximately +2.75%

Total return is the most complete picture for a passive index fund or pension plan tracking commodity exposure, because it reflects the full economic outcome of holding the position through the fund's financing structure.

## When Each Return Series Matters

**Use spot return when:**
- Assessing the fundamental commodity market (supply, demand, inventory).
- Comparing long-term commodity trends independent of recent market structure.
- Evaluating a manager's skill at selecting which commodities to buy (i.e., pure commodity picking, not roll management).

**Use excess return when:**
- Comparing commodity index funds or passive strategies against each other.
- Understanding the role of contango or backwardation in recent performance.
- Checking whether a commodity strategy is benefiting from favorable [futures-contract](/futures-contract/) curves.

**Use total return when:**
- Reconciling the actual price movement you observe in a fund's net asset value ([net-asset-value](/net-asset-value/)).
- Benchmarking a commodity fund against a stated benchmark, which usually specifies total return.
- Assessing the full opportunity cost of holding commodity exposure in a portfolio.

## Roll Yield in Practice: Two Market Regimes

In **contango** (normal supply conditions), farther-out contracts trade at premiums. Rolling forward is costly. Many commodity markets spend extended periods in contango—energy, especially crude oil, tends toward contango except during supply disruptions. Grain markets shift between contango and backwardation seasonally. During contango, excess return lags spot return by an amount that depends on the curve's steepness and the roll frequency.

In **backwardation** (tight supply or demand), nearer contracts trade above far contracts. Rolling is profitable. Backwardation is less stable and typically associated with supply stress (e.g., during an oil shock or crop failure). When backwardation persists, excess return exceeds spot return—a valuable hidden benefit for index holders.

A commodity index published its three return series over a five-year period:
- Spot return: +8% annualized
- Excess return: +5% annualized (roll cost in persistent contango)
- Total return: +4.8% annualized (modest financing drag at low rates)

Understanding this breakdown explains why the index underperformed the commodity itself: the futures structure imposed a structural cost.

## How Index Providers Handle the Three Series

[Index-provider](/index-provider/) firms like S&P, Bloomberg, and Thomson Reuters publish all three return series for their commodity indices. Some funds explicitly track one series; others blend them. Always check the prospectus or fact sheet to see which return is being reported.

A common pitfall: comparing a spot-return commodity index against an actively managed commodity fund that publishes total return. The fund will appear to underperform, even if the manager's commodity selection was skilled—the manager's true edge is buried in the roll cost difference.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the vehicle commodity indices use, and the rolling dynamic
- [Contango](/contango/) — when farther contracts trade higher, imposing a cost on index holders
- [Backwardation](/backwardation/) — when nearer contracts trade higher, benefiting index holders
- [Basis](/basis/) — the spread between spot and futures, related to the economics of storage
- [Index Provider](/index-provider/) — firms that construct and publish commodity indices and their returns
- [Net Asset Value](/net-asset-value/) — how commodity index funds report daily value, reflecting all three returns

### Wider context

- [Commodity Index Spot Return vs Excess Return vs Total Return](/commodity-index-spot-return-vs-excess-return/) — this article
- [Derivatives Hedging](/derivatives-hedging/) — how institutional investors manage commodity exposure
- [Market Timing](/market-timing/) — the risk of trying to avoid contango or backwardation rolls
- [Performance Fee](/performance-fee/) — how commodity managers are compensated and how returns are measured
- [Factor Investing](/factor-investing/) — commodity returns as a portfolio factor

</div>
