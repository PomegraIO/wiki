---
title: "How ETF Arbitrage Keeps Price Close to NAV"
description: "How ETF arbitrage works: how authorized participants use creation and redemption to close premiums and discounts, keeping ETF market price anchored to net asset value."
keywords:
  - etf arbitrage keeps price on nav
  - authorized participant creation redemption
  - etf premium discount mechanism
  - how etfs stay fairly valued
image: /svg/markets.svg
---

*An **ETF** trading 2% above its underlying assets should seem like a free lunch—but it rarely stays that way. **How ETF arbitrage works** through the creation-redemption mechanism exploited by authorized participants keeps the market price of an ETF anchored to its true net asset value. This mechanism is the plumbing that makes ETF trading reliable and efficient.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ETF Arbitrage — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Authorized participants close ETF premiums and discounts by creating or redeeming shares directly with the fund.</div>

|   |   |
|---|---|
| **The mechanism** | [Authorized participants](/authorized-participant/) can create/redeem large blocks of shares at [net asset value](/net-asset-value/) |
| **What it fixes** | ETF [premium](/etf-premium-discount/) or [discount](/etf-premium-discount/) to underlying value |
| **Who does it** | Institutional traders and market makers (authorized participants only) |
| **Cost to arbitrageur** | Small—transaction fees and bid-ask spreads are negligible vs. the premium/discount |
| **How fast it works** | Minutes to hours for a 2% premium to close |
| **Why it matters** | Prevents ETF prices from drifting far from actual asset values |

</aside>

## The problem: why an ETF might trade at a premium or discount

In a normal stock market, the price of Apple rises or falls based on supply and demand. An [ETF](/etf/) is different—it is a *container* holding a basket of assets with a known [net asset value](/net-asset-value/). If the NAV is $100 per share but the ETF trades at $102, investors see a 2% premium.

This can happen because:

- **Supply constraints.** If the underlying assets (say, emerging-market bonds) are hard to trade in the secondary market, demand for the ETF can exceed supply, pushing the price up.
- **Closure to new creations.** If the fund is closed to new share creation, the supply of ETF shares is fixed, and price can diverge from NAV.
- **Information lags.** The NAV is calculated once a day at the market close, while the ETF trades continuously. Intraday, the ETF price can drift above or below the stale NAV.
- **Demand for convenience.** Some investors prefer to buy ETF shares on an exchange rather than purchase the underlying assets directly. That convenience can carry a premium.
- **Structural demand.** Certain ETF share classes (like the hedged or inverse variants) may experience persistent demand imbalances.

Without a mechanism to close the gap, ETF prices could remain detached from their true value, undermining the whole promise of passive index tracking.

## How creation and redemption work

Every [authorized participant](/authorized-participant/)—typically a large institutional broker or dealer—has the contractual right to create and redeem large blocks of ETF shares directly with the fund at the NAV. This happens through an *in-kind* exchange:

**Creation (when ETF trades at a premium):**

1. An authorized participant sees the ETF trading at $102 while the NAV is $100.
2. They assemble a basket of the underlying assets (a **creation unit**, typically 10,000 to 100,000 shares) worth exactly $100 per share.
3. They deliver this basket to the fund and receive a block of new ETF shares—also valued at exactly $100 per share.
4. They immediately sell the new ETF shares on the stock exchange at $102.
5. **Profit:** $2 per share, minus transaction costs.

The act of selling new ETF shares on the exchange increases the supply of ETF shares, pushing the price down toward the NAV. As the premium narrows, the arbitrage opportunity shrinks until it is too small to profit from after paying commissions and spreads.

**Redemption (when ETF trades at a discount):**

1. An authorized participant sees the ETF trading at $98 while the NAV is $100.
2. They buy a large block of ETF shares on the exchange at $98 each.
3. They deliver these shares to the fund and receive back a basket of the underlying assets worth $100 each.
4. They sell or hold the underlying assets.
5. **Profit:** $2 per share, minus transaction costs.

The act of buying ETF shares on the exchange reduces the supply, pushing the price up toward the NAV.

## Why this keeps premiums and discounts tiny

The arbitrage is profitable precisely when the premium or discount is *larger than the transaction cost*. The moment a 2% premium emerges, authorized participants flood in to create new shares and sell them. Each new share sold puts downward pressure on the price. Within minutes to hours, the premium shrinks to, say, 0.05%—the point where transaction fees eat any further profit.

The result: ETF prices typically stay within 0.1% to 0.2% of their NAV under normal trading conditions. This is invisible to most retail investors but critical to the integrity of the product.

For comparison, closed-end funds do not have this mechanism. A closed-end fund can trade at a 10% discount or premium to its NAV for *years*, with no automatic correction mechanism. This is why ETFs have largely displaced closed-end funds for passive index tracking.

## How it handles stressed markets

When underlying markets become illiquid (a *crash, a flash crash, or a liquidity crisis in a specific asset class*), the creation-redemption mechanism can slow or break:

- **Stale NAVs.** If the underlying bonds or foreign stocks cannot be traded, the NAV becomes stale, and the creation-redemption process may pause.
- **Wider bid-ask spreads.** As the cost to assemble or disassemble a creation unit rises, authorized participants demand a larger premium or discount to justify the trade.
- **Temporary premiums/discounts.** During the March 2020 COVID sell-off, some bond ETFs traded at 3–5% discounts to NAV, as the creation process broke down temporarily.

However, once the underlying assets regain liquidity, the creation-redemption machine restarts, and the ETF price quickly converges back to NAV.

## The economics for authorized participants

The arbitrage is a low-margin business:

- **Profit per trade:** Often $0.50 to $5 per 100,000-share creation unit—tiny as a percentage.
- **Scaling.** Authorized participants execute thousands of creation-redemption trades per day across dozens of ETFs, compounding small margins into meaningful revenue.
- **Risk management.** The participant must assemble or disassemble baskets quickly and hold inventory briefly, exposing them to market moves. Larger premiums/discounts attract more participants, which accelerates the close.

This is why creation-redemption arbitrage is performed almost exclusively by institutional market makers with scale, not retail traders. Retail investors cannot profitably access creation-redemption mechanisms—they can only buy and sell ETF shares on an exchange like everyone else.

## Limits to the mechanism

The creation-redemption mechanism keeps ETF prices anchored under *normal* conditions, but it has boundaries:

- **It requires liquid underlying assets.** An ETF holding illiquid private-market assets (like some real-estate or commodity funds) cannot rely on tight premiums-discounts because creating or redeeming a large block is expensive.
- **It requires active authorized participants.** If only one or two market makers are active in an obscure ETF, the mechanism may be slow.
- **Extreme stress can overwhelm it.** During the fastest, most violent market crashes, the time lag between price and creation-redemption can widen sharply.

But in the routine case—a broad equity [index fund](/index-fund/) or [bond ETF](/bond-etf/) with trillions of assets under management—the mechanism is so efficient that prices almost never drift more than a rounding error from NAV.

## See also

<div class="wiki-seealso">

### Closely related

- [ETF](/etf/) — the broader product structure that relies on this mechanism
- [Net asset value](/net-asset-value/) — the true value that ETF prices anchor to
- [Authorized participant](/authorized-participant/) — the institutional traders who execute the arbitrage
- [ETF premium discount](/etf-premium-discount/) — the deviation this mechanism minimizes
- [Bid-ask spread](/bid-ask-spread/) — the transaction cost that limits arbitrage profit

### Wider context

- [Index fund](/index-fund/) — the most common use case for ETFs
- [Market maker trading](/market-maker-trading/) — another source of price efficiency
- [Liquidity risk](/liquidity-risk/) — what can break the mechanism in crises
- [Price discovery](/price-discovery/) — how markets converge toward fundamental value

</div>
