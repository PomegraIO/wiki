---
title: "Futures Roll Cost Explained"
description: "Futures roll cost is the economic gain or loss when closing a near-month contract and reopening in a later month. Learn how contango and backwardation affect roll costs."
keywords:
  - futures roll cost explained
  - contract rollover
  - contango backwardation cost
  - futures calendar spread
  - roll yield
image: /svg/derivatives.svg
---

*The **futures roll cost** is the economic gain or loss incurred when a trader closes a position in a near-month [futures contract](/futures-contract/) and reopens an equivalent position in a later-dated contract, capturing the price difference between the two contracts. This cost is the primary expense of maintaining a futures position beyond the front contract's expiration.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Roll Cost — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Rolling is mandatory when near-month contracts expire; the cost depends on the curve shape.</div>

|   |   |
|---|---|
| **Definition** | Price difference between old contract (closed) and new contract (opened) |
| **Contango scenario** | Deferred contracts trade higher; rolling costs money (you sell low, buy high) |
| **Backwardation scenario** | Deferred contracts trade lower; rolling makes money (you sell high, buy low) |
| **Magnitude** | Depends on storage costs, [interest-rate](/interest-rate/), and convenience yield for the commodity |
| **Impact on returns** | Negative roll cost in contango can erase a significant portion of commodity fund returns |
| **Timing** | Traders typically begin rolling 2–4 weeks before front contract [expiration-date](/expiration-date/) |
| **Example** | Closing a Dec contract at $95 and opening a Jan at $98 = −$3/contract roll loss |

</aside>

## The basic mechanics

A [futures contract](/futures-contract/) has a fixed [expiration-date](/expiration-date/). A trader long crude oil on a December contract cannot simply hold it forever; when December expires, the position must be closed. To maintain exposure to crude oil beyond December, the trader sells (closes) the December contract and simultaneously buys (opens) a January contract for the same amount.

The roll cost is the difference in price between the two trades:

**Roll cost per contract = (New contract price − Old contract price) × multiplier**

If the December contract is trading at $95/barrel and the January contract is trading at $98/barrel, the trader sells at $95 and buys at $98, locking in a $3/barrel loss. With crude futures traded in units of 1,000 barrels, the total cost is $3,000 per contract rolled.

Over a year, a trader maintaining a long position through multiple rolls can incur substantial cumulative costs—or capture gains, depending on market structure.

## Contango: a drag on long positions

When the [futures](/futures-contract/) market is in **contango**, later-dated contracts trade at higher prices than near-month contracts. This is the normal state for many commodities, driven by the cost of storing the physical commodity, financing costs, and insurance.

For a long trader (one holding the contract for upside price exposure), contango is painful. Every time you roll, you sell the cheaper near-month contract and buy the more expensive deferred contract. You are consistently buying high and selling low. This drag compounds, especially in steep contango where the price difference is large.

A classic example: if crude averages $100/barrel with a 3% annual contango curve, a trader rolling every month through the year will incur roughly $3/barrel in cumulative roll losses, even if the spot price stays flat at $100. This is why commodity [ETFs](/etf/) tracking contango-heavy markets often underperform the spot price, and why long-only commodity investors must factor roll cost into their return expectations.

## Backwardation: a gift to long positions

When the market is in **backwardation**, near-month contracts trade at higher prices than deferred contracts. This occurs when immediate supply is tight or consumption is urgent—a convenience yield effect. For a long trader, backwardation is favorable: you are selling the expensive near-month and buying the cheaper deferred, locking in a gain.

A trader holding an August contract at $102/barrel and rolling into September at $100/barrel gains $2 on the roll. In a consistently backwardated market, rolls are profitable, and cumulative roll gains can offset or exceed normal carry costs.

## Numerical example: a year-long roll cycle

Imagine a trader enters a long crude position in January, intending to hold through the year. Here is a stylized roll schedule in contango:

| Month | Contract | Price | Action | Roll P&L |
|-------|----------|-------|--------|----------|
| January | Feb | $100 | Buy Feb at $100 | — |
| February | Mar | $102 | Sell Feb at $100, buy Mar at $102 | −$2 |
| March | Apr | $103.50 | Sell Mar at $102, buy Apr at $103.50 | −$1.50 |
| April | May | $105 | Sell Apr at $103.50, buy May at $105 | −$1.50 |
| May | June | $105.80 | Sell May at $105, buy June at $105.80 | −$0.80 |

(continuing through December)

Cumulative roll cost over the six months shown: −$6.80/barrel, or −6.8% of the entry price. Over a full year in moderate contango, the cumulative drag could reach 8–12% of capital.

This is why passive commodity-etf investors often see their funds underperform a buy-and-hold of the physical commodity: the roll cost in contango is a real, ongoing expense.

## Roll cost and strategic positioning

Professional traders and [hedge funds](/hedge-fund/) monitor roll costs carefully because they affect position sizing and strategy. If contango is very steep, a trader might:

- Reduce exposure to rolling commodities and shift to equities or [bonds](/bond/).
- Use cash-and-carry strategies, buying the physical commodity and selling futures, to arbitrage the contango.
- Shorten [holding-period](/holding-period/) and accept more frequent trading costs to reduce cumulative roll drag.

Conversely, in backwardation, traders might increase commodity exposure because roll costs are favorable or even profitable.

## Relation to spot price expectations

Roll costs are not arbitrary—they reflect the market's embedded cost of storage, [interest-rate](/interest-rate/) carry, and supply/demand imbalance. A persistently steep contango signals that storage and financing are expensive relative to expected spot price increases. This is economically rational: the market is charging you for the privilege of deferring physical delivery.

However, if you believe spot prices will rise sharply, the roll cost is a sunk cost worth bearing. A trader expecting $120 crude by year-end will gladly pay $6.80/barrel in roll costs to maintain a long position through contango.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures-contract](/futures-contract/) — The instrument being rolled
- [Contango](/contango/) — Deferred contracts trade higher; causes roll losses for long traders
- [Backwardation](/backwardation/) — Deferred contracts trade lower; causes roll gains for long traders
- [Expiration-date](/expiration-date/) — When the old contract expires and rollover is forced
- [Carry-trade](/carry-trade/) — Roll costs are part of the total carry cost

### Wider context

- [Forwards-contract](/forward-contract/) — Similar to futures but settled bilaterally; no roll cost
- Commodity-etf — Passive funds incur roll costs as a drag on returns
- [Hedge-fund](/hedge-fund/) — Professional managers actively monitor and manage roll costs
- [Derivatives-hedging](/derivatives-hedging/) — Hedgers also face roll costs and must budget them
- [Interest-rate](/interest-rate/) — Affects financing cost component of contango

</div>
