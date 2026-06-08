---
title: "Why a Commodity ETF Price Diverges from Spot Price"
description: "Explains why a commodity ETF price and spot price differ due to futures rolls, contango/backwardation, fund structure, and ongoing expenses."
keywords:
  - commodity etf price vs spot price
  - commodity etf tracking error
  - futures contango backwardation
  - commodity etf divergence
image: "/svg/commodities.svg"
---

*A **commodity ETF price** rarely mirrors the underlying spot commodity price one-for-one, even when both move in the same direction. The gap stems from three sources: the ETF's reliance on [futures contracts](/futures-contract/) instead of physical delivery, the roll cost incurred when near-term futures expire and must be replaced with later contracts, and the fund's [expense ratio](/expense-ratio/) and cash drag. Understanding this divergence is essential for investors expecting a pure spot-price play.*

## Why commodity ETFs use futures, not physical commodity

Most commodity ETFs do not hold barrels of crude oil, bushels of corn, or tons of gold sitting in a warehouse. Instead, they own a rotating portfolio of [futures contracts](/futures-contract/). Why the indirection?

**Cost and logistics**: Storing physical crude oil requires pipelines, tanks, and security. Storing gold requires secure vaults. Storing agricultural commodities requires climate-controlled facilities and insurance. For a fund managing hundreds of millions of dollars, these costs would dwarf the [expense ratio](/expense-ratio/) the fund charges—often 0.5% to 1% annually. The fund would be insolvent.

**Fungibility**: Futures contracts are liquid, standardized, and traded 24/5 on exchanges. A fund can increase or decrease its exposure instantly without arranging shipment or storage. This speed and liquidity matter for efficient [authorized participant](/authorized-participant/) creation and redemption (the mechanism by which ETFs stay near their [net asset value](/net-asset-value/)).

**Transparency**: A futures-based fund's holdings are clear and publicly reported. A physical fund must conduct regular audits of warehouse holdings and report on purity or quality, adding friction.

A handful of commodity ETFs (chiefly gold and silver) do hold physical metal, but they charge higher [expense ratios](/expense-ratio/) (0.25%–0.40%) to cover storage and insurance. Most oil, natural gas, agricultural, and precious metal ETFs are futures-based.

## The roll and contango drag

Futures contracts expire. A contract labeled "WTI Crude Oil September 2025" ceases to exist on a specified expiration date. Before that date arrives, the fund must close its position in the expiring contract and open an equivalent position in a later contract—a process called a **roll**.

The roll creates the largest source of divergence from spot price. Here's why:

If the futures curve is in **contango** (a normal condition), later-dated contracts trade at a premium to near-term contracts. If September crude trades at $80 per barrel and December crude trades at $82, rolling from September to December means selling the cheaper contract and buying the more expensive one. The fund realizes a loss, which reduces its net asset value below what the spot price alone would suggest.

**Worked example**: A crude oil ETF holds 100 September futures at $80 each. It rolls these into 100 December futures at $82 each. The roll loss is (82 - 80) × 100 = $200. That loss flows into the fund's NAV, dragging returns below the spot price gain.

Contango is the norm in most commodity markets during normal supply-and-demand conditions. It reflects the [cost of carry](/cost-of-carry/)—the real cost of storing the commodity, insuring it, and financing it. Investors in futures demand compensation for these costs, so later contracts trade higher.

Over a full year, a monthly-rolling commodity ETF in persistent contango can lag the spot price by 5%–20%, depending on the contango curve's steepness and the commodity's volatility. This is not a bug in the fund's design; it is the inevitable cost of using futures.

## Backwardation: the rare reversal

When **backwardation** occurs (near-term contracts trade higher than later ones), the math flips. Rolling from September at $82 to December at $80 means buying the cheaper contract and realizing a gain. Over time, backwardation can help a commodity ETF outperform the spot price.

Backwardation signals supply stress or immediate scarcity. It is common in natural gas during winter, in crude oil during geopolitical crises, and in grains during crop shortages. But it is temporary. Once supply eases or the crisis recedes, the market returns to contango and the gains reverse.

A fund that gets lucky and rolls during prolonged backwardation will outperform—but this is not a reliable edge. Most of the time, especially in commodity markets at rest, contango is the rule.

## Expense ratio and cash drag

The fund's stated [expense ratio](/expense-ratio/) (annual fee) is deducted from the fund's returns, creating a second source of underperformance relative to spot price. A fund charging 0.75% annually will lag the spot price by 0.75 percentage points per year, assuming the spot price does not move.

In addition, funds often carry a small cash position to facilitate daily [authorized participant](/authorized-participant/) creation and redemption. This cash earns low or zero interest, dragging returns. Over time, the cash drag is small but visible in long-term comparisons.

## Contango vs backwardation and the broader curve

To understand roll cost, you need to grasp the shape of the futures curve:

**Normal contango curve**: Near-term contracts are cheap, progressively further-out contracts are more expensive. This happens when carrying costs are positive (storage, insurance, financing). A fund rolling down the curve every month loses money.

**Flat curve**: All contracts trade at similar prices. Rolling costs are minimal.

**Steep contango**: Later contracts are *much* more expensive than near-term ones. Roll costs are severe.

**Backwardated curve**: Near-term contracts are expensive, later contracts are cheaper. Rolling saves money.

The curve shape changes based on supply and demand. During a supply glut (e.g., excess crude oil production), later contracts cheapen (because urgency to store is low), and the curve steepens into contango. During a shortage, near-term contracts premium up sharply, and the curve may invert into backwardation.

## Tracking error and performance drag over time

Over a 1–3 year horizon, a futures-based commodity ETF typically lags the spot price by 2%–10% per year, depending on the commodity, the contango curve, and the fund's rolling schedule.

**Gold**: Often exhibits modest contango (2%–3% annualized). Gold ETFs using futures or spot have historically tracked closely.

**Crude oil**: Exhibits volatile contango and occasional backwardation. A crude oil ETF can lose 5%–15% in a single year due to rolls, even if the spot price is flat.

**Natural gas**: Notoriously steep contango in normal times. Natural gas ETFs have been notorious for underperformance, losing 20%–50% in some years as the curve inverts dramatically.

**Grains (corn, soybeans, wheat)**: Contango is usually moderate, but the curve shifts sharply during seasonal peaks and shortages.

This drift is not a hidden cost; it is embedded in the fund's NAV and reflected in its price. An investor who buys a crude oil ETF and holds it while WTI spot trades sideways will see the ETF decline, not because the fund manager is incompetent, but because the roll cost is real.

## Multiple-times leveraged and inverse commodity ETFs

Leveraged and inverse commodity ETFs amplify the roll cost problem. A 2x leveraged crude oil ETF might outperform oil itself during sharp rallies, but it compounds the roll loss during contango. Over a multi-year period, leveraged commodity ETFs tend to produce especially poor long-term returns relative to spot prices. Inverse commodity ETFs (betting on price declines) suffer similar decay.

These products are marketed for short-term tactical positions, not buy-and-hold strategies. Holding them for years is almost guaranteed to produce returns far worse than the spot price move alone would suggest.

## Checking a commodity ETF's actual vs. target return

To evaluate whether a specific commodity ETF is tracking reasonably, compare its **year-to-date** or **one-year return** to the spot commodity return over the same period. Most major financial platforms (Bloomberg, Yahoo Finance, commodity exchange websites) report both.

A crude oil ETF should track within a few percentage points of spot crude for short periods. Over longer periods (3–5 years), expect larger deviations. If an ETF is significantly ahead or behind historical norms for the commodity, check the fund's prospectus for clues: is it using a different rolling strategy, holding cash, or carrying a higher expense ratio?

## The spot-price replication alternative

A handful of commodity ETFs and structured products attempt to track spot price more directly by holding actual futures *and* managing the roll mathematically or through [derivatives](/derivatives-hedging/). These are rarer and often more expensive. For most investors, the standard futures-based ETF is the practical choice, and the roll cost is the price of access.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the underlying instrument commodity ETFs hold
- [Contango](/contango/) — the normal commodity futures market state driving tracking error
- [Backwardation](/backwardation/) — the inverted state that temporarily helps ETF returns
- [Commodity ETF](/commodity-etf/) — the broader category of commodity-linked funds
- [Expense Ratio](/expense-ratio/) — the fund fee contributing to divergence
- [Net Asset Value](/net-asset-value/) — the daily valuation that reflects accumulated roll costs

### Wider context

- [ETF](/etf/) — the overall fund structure and how creation/redemption works
- [Authorized Participant](/authorized-participant/) — the market makers who keep ETF prices near NAV
- [Cost of Carry](/cost-of-carry/) — the economic reason contango exists
- Commodity — the underlying asset class
- Roll Risk — a broader category of futures-replacement risk

</div>
