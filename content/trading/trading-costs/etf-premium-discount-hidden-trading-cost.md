---
title: "ETF Premium and Discount as a Hidden Trading Cost"
description: "An ETF trading at a premium to NAV costs more than its holdings; trading at a discount means the buyer gets a bargain but a seller locks in a loss."
keywords:
  - etf premium discount
  - etf trading cost hidden
  - etf net asset value
  - nav premium trading loss
  - etf bid-ask spread
  - intraday etf cost
---

*An ETF can trade at a **premium** or **discount** to its [net asset value](/net-asset-value/) (NAV)—the true value of its underlying holdings. When you buy an ETF at a premium, you overpay relative to what you own; when you sell at a discount, you underprice it. This divergence is an invisible layer of cost on top of the quoted [bid-ask spread](/bid-ask-spread/), often unnoticed by retail investors but critically important to active traders and large institutional flows.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ETF Premium and Discount — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics and costs." />

<div class="wiki-infobox-caption">Price divergence from NAV is a real cost that can dwarf the quoted spread for certain funds or market conditions.</div>

|   |   |
|---|---|
| **Premium** | ETF price > NAV; buyer overpays relative to holdings; premium% = (Price − NAV) / NAV |
| **Discount** | ETF price < NAV; buyer underpays or seller takes a loss; discount% = (NAV − Price) / NAV |
| **Typical range** | 0.01%–0.10% for large liquid funds; 0.5%–2% for small, illiquid, or stress periods |
| **Cause** | Supply/demand imbalance, creation/redemption delays, or closed-end fund-style premium |
| **Cost to trader** | Premium paid at entry or discount taken at exit; additive to spread cost |
| **Arbitrage driver** | [Authorized participants](/authorized-participant/) create/redeem shares to close premium-discount gaps |

</aside>

## Why ETFs trade away from NAV

The NAV of an ETF is calculated once daily at market close—it is the true value per share of the fund's holdings, published by the fund sponsor. But the ETF's market price (what you pay to buy or receive to sell on the exchange) can deviate from this value because trading happens continuously throughout the day, and supply-demand imbalances occur.

If more investors want to buy an [ETF](/etf/) than sell it, the market price rises above the NAV—a premium. If selling pressure outweighs buying, the price falls below NAV—a discount. For liquid, large-cap [index funds](/index-fund/), this divergence is usually tiny (under 0.05%). For smaller, less-traded funds or funds holding illiquid assets (emerging-market equities, bonds, commodities), the premium or discount can persist at 0.5% or higher.

During market stress—flash crashes, liquidity crunches, or gap openings after hours—premiums and discounts can widen to 1–3% or more. A fund tracking corporate bonds might trade at a 2% discount during a credit panic because the bonds themselves are illiquid and prices are stale.

## How premium and discount function as cost

When you buy an ETF at a 0.10% premium, you are paying slightly more per share than the NAV of the holdings you receive. If the premium later shrinks to zero (which it often does as arbitrage works), you lock in a small loss. Conversely, selling at a discount means you receive less per share than the NAV—a real loss relative to the intrinsic value.

These costs are hidden because they don't appear in the commission or spread—they are purely a price mismatch. Consider a concrete example:

| Scenario | NAV per share | Market price | Effective cost |
|----------|---------------|---------------|-----------------|
| Buy at premium | $100.00 | $100.10 | +0.10% |
| Sell at discount | $100.00 | $99.85 | −0.15% |
| Buy and later sell at parity | $100.00 | Buy $100.10; sell $100.00 | −0.10% realized loss |

If you buy the ETF at a 0.10% premium and sell later when the premium has closed, you lose 0.10%—pure cost unrelated to spread. For a day trader or a large institution rebalancing a portfolio, these fractions compound across many trades.

## When premiums and discounts widen

Premiums and discounts are typically smallest during the core trading hours (9:30 a.m.–4 p.m. Eastern) when the NAV-updating mechanism and [arbitrage](/algorithmic-trading/) keep prices tethered to value. They widen when:

- **Foreign markets have moved overnight**: A fund tracking Japanese or European equities trades hours before those markets open. Investors react to overnight moves, bidding up or down the ETF price, but the NAV won't update until the foreign market closes and is priced into the next day's calculation. Until then, the premium or discount persists.

- **The fund holds illiquid assets**: A bond ETF might hold corporate or emerging-market bonds that don't trade frequently. If a credit event occurs, bond prices gap down on Reuters/Bloomberg screens, but the ETF price can't arbitrage until the bonds can actually be sold. The discount widens temporarily.

- **Creation/redemption is delayed or unavailable**: [Authorized participants](/authorized-participant/) (APs) are the market makers who create new ETF shares (by depositing the underlying holdings) and redeem shares (by receiving the holdings back). This process normally takes one to three days and keeps premiums tight. If an AP goes offline or if the underlying market is closed, the redemption pipeline clogs, and premiums can drift.

- **Market stress and liquidity drought**: During flash crashes or severe dislocations, trading halts, the underlying market may be closed or only partially tradeable, and APs pull back from creation/redemption. Premiums and discounts can blow out to 2–5% or more.

## The arbitrage mechanism

The reason premiums and discounts don't widen indefinitely is arbitrage. If an ETF trades at a significant premium, an AP can:

1. Buy the underlying securities in the open market
2. Deposit them to the ETF sponsor and receive freshly created ETF shares
3. Sell those shares at the elevated premium price
4. Lock in a profit

This arbitrage removes the supply shortage driving the premium, pushing the price back toward NAV. Similarly, a large discount triggers reverse arbitrage: buy the discount-priced ETF, redeem the shares for the underlying holdings, and sell those holdings at a markup. Competitive arbitrage by many APs keeps premiums tight most of the time.

However, arbitrage fails during certain conditions. If the underlying market is closed (e.g., a bond fund trying to arbitrage after the bond market has shut for the day), or if the assets are so illiquid that the AP cannot execute the underlying trades without moving prices dramatically, arbitrage is blocked or too costly to execute, and the premium or discount persists.

## Impact on different fund types

Premiums and discounts vary by fund structure and assets:

- **Large-cap US equity ETFs** (e.g., tracking the [S&P 500](/sp-500-index/)): nearly continuous arbitrage keeps premiums under 0.01%
- **Small-cap and international equity ETFs**: 0.05–0.20% premium/discount is common
- **Bond ETFs**: 0.10–0.50% ranges; wider during credit stress
- **Commodity ETFs** (holding physical metals or futures): can trade at persistent 1–2% premiums due to storage/financing costs
- **Emerging-market ETFs**: 0.20–1% ranges; wider after hours or during crises
- **Leveraged and inverse ETFs**: larger daily premiums due to complexity and lower liquidity

## The trader's perspective

A retail investor buying a single share of SPY (an S&P 500 ETF) at a 0.02% premium will likely never notice the cost. But a trader flipping a position intraday or a portfolio manager rebalancing $100 million feels every basis point (0.01%). If you buy at a 0.10% premium and sell at a 0.15% discount, you've lost 0.25% before even accounting for the spread—a cost structure that can swamp [performance fees](/performance-fee/).

Active traders monitor ETF premiums in real-time; many trading platforms now display NAV alongside market price. Experienced traders time their entry and exit to avoid large discounts and premiums, or they deliberately exploit them when arbitrage is broken (e.g., buying a discount-priced fund when they believe the discount will close).

## See also

<div class="wiki-seealso">

### Closely related

- [ETF](/etf/) — definition and structure of exchange-traded funds
- [Net Asset Value](/net-asset-value/) — the true per-share value of an ETF's holdings, published daily
- [Bid-Ask Spread](/bid-ask-spread/) — the quoted transaction cost; separate from and often smaller than premium/discount cost
- [Authorized Participant](/authorized-participant/) — market maker that creates and redeems shares to arbitrage premiums and discounts
- [Liquidity Risk](/liquidity-risk/) — how thinly traded funds experience wider discounts and premiums

### Wider context

- [ETF Premium and Discount](/etf-premium-discount/) — dedicated article on the mechanism and measurement
- [Index Fund](/index-fund/) — passive funds that typically have tight premiums
- [Arbitrage](/algorithmic-trading/) — the trading activity that keeps premiums and discounts bounded
- [Market Making](/market-maker-trading/) — role of APs and dealers in tightening bid-ask spreads and premiums

</div>
