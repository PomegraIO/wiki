---
title: "Contango Cost for Long Futures Holders"
description: "Contango cost for long futures holders occurs when rolling forward costs money; persistent contango erodes returns on repeatedly-rolled positions."
keywords:
  - contango cost long futures holder
  - rolling futures in contango
  - futures roll yield
  - contango losses futures
image: /svg/derivatives.svg
---

*The **contango cost for long futures holders** is the cumulative loss incurred by investors who repeatedly roll long positions forward through an upward-sloping futures curve. Each time you close an expiring contract and buy a farther month at a higher price, you realize a loss that compounds over months or years of holding, cutting into returns even if the underlying commodity never moves.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Contango Cost — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Rolling long positions in contango transfers wealth from the holder to the counterparty at each expiry.</div>

|   |   |
|---|---|
| **Core problem** | Buying far-month contracts at prices higher than near-month contracts |
| **Who feels it** | Long-term holders, passive tracking funds, buy-and-hold hedgers |
| **When it strikes** | Every rollover—no relief until the market enters [backwardation](/backwardation/) or flat |
| **Magnitude** | Depends on the size of the [contango](/contango/) spread; can compound to 10–40% annualized drag |
| **Typical markets** | Crude oil, heating oil, natural gas, agricultural commodities in normal storage conditions |

</aside>

## How rolling in contango works

When you own a futures contract approaching expiry, you have two choices: take delivery (if eligible) or roll the position forward. Rolling means selling the front-month contract that's about to expire and buying a farther-out expiry. In a [contango](/contango/) market—where forward prices are higher than near-term prices—this swap is a loss.

Say crude oil front-month futures trade at $80/barrel and the three-month contract trades at $82/barrel. You own 10 contracts expiring in weeks. To keep your position alive, you sell at $80 and buy at $82, locking in a $2/barrel loss immediately. Multiply that across your position and time, and it adds up.

The financial reality is you're paying a spread—the storage cost, insurance, and financing differential embedded in the curve—every single roll. In normal markets with ample physical supply and storage capacity, contango becomes a tax on persistence.

## The mathematical effect on long-term returns

A practical example: An investor holds crude oil through a year of rolling, starting with front-month at $75/barrel. Each quarter:

| Quarter | Near-month price | Far-month price | Roll loss/barrel |
|---------|------------------|-----------------|------------------|
| Q1      | $75.00           | $77.00          | $2.00            |
| Q2      | $76.50           | $78.50          | $2.00            |
| Q3      | $77.50           | $79.50          | $2.00            |
| Q4      | $78.00           | $80.00          | $2.00            |

At year-end, the spot price is $78, up $3 from the entry of $75—a 4% gain. But the investor paid $8 in rolling costs (4 rolls × $2). Net loss: $5/barrel, or roughly **–6.7% total return**. The commodity moved up, yet the strategy lost money. This is the contango cost in action.

The compounding effect is worse with larger spreads or shorter holding horizons where you roll more frequently. A commodity fund tracking monthly rolls faces this drag consistently.

## Why funds and passive investors bear this cost

[Exchange-traded funds (ETFs)](/etf/) and passive commodity trackers that hold futures are often forced into this dynamic. They must roll on a published, predictable schedule. Sophisticated traders know this and front-run the rolls, bidding up the far-month contracts just before the fund needs to execute. The fund mechanically rolls at the worst price, eating the spread.

Passive oil-tracking funds have lost significant value this way during periods of persistent contango (notably in 2011–2016 in crude oil). The underlying commodity price barely moved, but the fund's value declined due to constant roll losses.

## Backwardation as a relief valve

When the market flips into [backwardation](/backwardation/)—where near-month contracts are priced higher than far-month—the dynamic reverses. Rolling becomes profitable. Near-month crude at $82 and three-month at $80 means you sell high and buy low, capturing $2/barrel on every roll. Long holders who survived contango periods can recoup losses during brief backwardation windows.

However, backwardation tends to be temporary, driven by supply crunches or delivery squeezes. Investors cannot rely on it, so the contango cost remains a material drag on long-term returns.

## Hedger versus speculator considerations

For corporate hedgers—airlines buying oil futures to lock in fuel costs, for example—the contango cost is often acceptable because they're locking in certainty. The "cost" is really just the insurance premium embedded in the curve. A airline that knows it will buy fuel every quarter accepts rolling in contango as part of operations.

Speculators or financial investors with no end-use obligation for the commodity cannot justify the cost. They're paying for storage and carry they don't need, purely to maintain market exposure. This is why [commodity index funds](/index-fund/) historically underperformed the spot price of oil or wheat: the contango drag.

## Strategies to minimize the cost

Sophisticated investors who want commodity exposure try several approaches:

- **Buy physical and store it** (infeasible for most financial investors, but used by industrial players)
- **Use [options](/option/)** to gain directional exposure without rolling futures
- **Trade the [calendar spread](/calendar-spread-futures-explained/)** between front and back months, capturing contango or backwardation profits explicitly
- **Avoid passive roll schedules**—trade discretionally, rolling when the spread is narrowest
- **Hold bonds** or other inflation hedges instead of futures commodities in deep contango

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — when forward prices exceed spot prices
- [Backwardation](/backwardation/) — the opposite market structure; can relieve contango losses
- [Futures Contract](/futures-contract/) — the standardized derivative mechanism enabling rolling
- [Calendar Spread Futures Explained](/calendar-spread-futures-explained/) — profiting directly from curve structure
- [Commodity Index Funds](/index-fund/) — passive trackers that face sustained roll drag
- [Carry Trade](/carry-trade/) — borrowing to fund long exposure; contango is an anti-carry cost

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — why hedgers tolerate contango as insurance cost
- [Forward Contract vs Futures Contract](/forward-contract-vs-futures-contract/) — understanding roll mechanics
- [Futures Margin Call Mechanics](/futures-margin-call-mechanics/) — capital requirements when holding rolled positions
- [Time Value](/time-value/) — how curve structure reflects financing and storage

</div>
