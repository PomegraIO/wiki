---
title: "ETF Premium and Discount"
description: "An ETF premium occurs when an ETF's market price exceeds its NAV; a discount occurs when the price falls below NAV. Premiums and discounts normally stay tight (under 0.1%) due to ETF arbitrage, but widen during market stress."
keywords:
  - ETF premium
  - ETF discount
  - NAV divergence
  - pricing
  - fund
image: "https://picsum.photos/seed/etf-premium-discount/900/600"
---

*An **ETF premium** occurs when an [ETF](/etf)'s market trading price exceeds its [NAV](/etf-premium-discount) — the underlying value of its holdings. An **ETF discount** occurs when the trading price falls below [NAV](/etf-premium-discount). For large, liquid [ETFs](/etf), premiums and discounts are usually tiny (0.01%–0.05%). But for specialized [ETFs](/etf) or during market stress, they can widen dramatically, creating investment risks.*

<div class="wiki-hatnote">

This entry covers the pricing phenomenon. For what causes premiums and discounts, see [ETF arbitrage](/etf-arbitrage); for the mechanism that corrects them, see [ETF creation and redemption](/etf-creation-redemption).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ETF Premium and Discount — key facts</div>

<img src="https://picsum.photos/seed/etf-premium-discount/900/600" alt="A chart showing ETF price above and below NAV line" />

<div class="wiki-infobox-caption">Premiums and discounts measure the gap between market price and intrinsic value.</div>

|   |   |
|---|---|
| **What it is** | The gap between ETF price and underlying NAV |
| **Also called** | Premium/discount to NAV, closed-end fund discount |
| **Premium** | Price > NAV (you overpay for the underlying) |
| **Discount** | Price < NAV (you get a bargain) |
| **Normal range** | ±0.01% to ±0.05% for liquid ETFs |
| **Stress range** | Can widen to ±1% or more during market crashes |
| **What causes widening** | Liquidity stress, flight to quality, underlying illiquidity |
| **What corrects it** | [ETF arbitrage](/etf-arbitrage), [authorized participants](/authorized-participant) |

</aside>

## What NAV means

The [NAV](/etf-premium-discount) — or **net asset value** — is the true underlying value of an [ETF](/etf). It is calculated as:

```
NAV = (Total value of holdings - Liabilities) / Number of shares outstanding
```

For an [equity ETF](/equity-etf) holding 500 stocks worth $500 million with 1 million shares outstanding, the [NAV](/etf-premium-discount) is $500 per share. This is what the fund is actually worth if you liquidated it.

The [NAV](/etf-premium-discount) is recalculated continuously throughout the trading day as stock prices move. [ETF](/etf) issuers publish the [NAV](/etf-premium-discount) multiple times per second, and independent financial data providers publish it on all major financial websites.

## Premiums and discounts in normal conditions

For a large, liquid [ETF](/etf) like SPY (S&P 500 ETF), the trading price and [NAV](/etf-premium-discount) are almost always within 0.01% of each other. Why?

**[ETF arbitrage](/etf-arbitrage).** If SPY trades at a 0.1% premium to [NAV](/etf-premium-discount), an [authorized participant](/authorized-participant) instantly:

1. Buys the underlying 500 stocks at [NAV](/etf-premium-discount).
2. Exchanges them for newly created SPY shares.
3. Sells those SPY shares on the market at the premium price.
4. Locks in a 0.1% profit.

This arbitrage happens so fast and so constantly that premiums and discounts stay negligible.

However, small premiums and discounts persist because [authorized participants](/authorized-participant) face real costs:

- **Bid-ask spreads** when trading the 500 underlying stocks.
- **Market impact** from buying 500 stocks simultaneously.
- **Borrowing costs** to finance the arbitrage position.
- **Operational costs** and regulatory fees.

These costs (typically 0.02%–0.05%) set a natural limit on how tight premiums and discounts can compress. An [AP](/authorized-participant) will not arbitrage if the gap is smaller than the transaction cost.

## Premiums and discounts in stress

During market turmoil, premiums and discounts can widen dramatically:

**March 2020 COVID crash.** Bond [ETFs](/etf) that held illiquid corporate bonds traded at 2%–5% discounts to [NAV](/etf-premium-discount). Why? Because:

- The underlying bonds became hard to trade; [bid-ask spreads](/etf-bid-ask-spread) on bonds widened from 0.05% to 1%.
- [APs](/authorized-participant) became risk-averse and stopped creating/redeeming.
- Investors panic-sold [ETFs](/etf) indiscriminately, pressing prices down.
- The true [NAV](/etf-premium-discount) itself was uncertain because the bonds were not actively trading.

**Leveraged ETF crashes.** During a sharp market drop, [leveraged ETFs](/leveraged-etf) sometimes trade at steep premiums or discounts because they hold [derivatives](/option) with their own bid-ask spreads and liquidity issues. A 3x leveraged [ETF](/etf) might trade at a 2%+ premium during a crash.

**Closed-end fund analogues.** Some specialized [ETFs](/etf) — those holding illiquid assets like emerging market bonds or private equity — behave more like [closed-end funds](/closed-end-fund) and trade at persistent premiums or discounts because [arbitrage](/etf-arbitrage) is costly.

## Why premiums and discounts matter

**For buy-and-hold investors.** If you buy an [ETF](/etf) at a 0.5% premium and hold it for 20 years, you overpaid by 0.5%. In a compounding scenario, this costs you 0.025% per year in foregone returns. It is not catastrophic, but it is a leak.

**For timing traders.** If you buy an [ETF](/etf) at a 1% discount, you got a bargain. If you sell when the premium/discount normalizes, you profit from the reversion. Some traders specialize in arbitraging premiums and discounts.

**For specialized ETFs.** If you hold a bond [ETF](/etf), emerging market [ETF](/etf), or other illiquid fund, monitoring the premium/discount is important. A widening discount might signal that the fund is becoming harder to trade or that [APs](/authorized-participant) are withdrawing.

## How to monitor premiums and discounts

Most financial websites (Yahoo Finance, Google Finance, broker platforms) display the ETF's current price and [NAV](/etf-premium-discount) side by side. You can calculate:

```
Premium/Discount (%) = (Price - NAV) / NAV × 100
```

For daily monitoring:

- **Positive number:** The [ETF](/etf) is trading at a premium (overpriced).
- **Negative number:** The [ETF](/etf) is trading at a discount (underpriced).

Comparing the current premium/discount to the fund's historical average tells you if the divergence is unusual.

## See also

<div class="wiki-seealso">

### Closely related

- [ETF](/etf) — the broader category
- [ETF arbitrage](/etf-arbitrage) — what corrects premiums/discounts
- [Authorized participant](/authorized-participant) — who arbitrages divergences
- [ETF creation and redemption](/etf-creation-redemption) — the mechanism enabling arbitrage
- [ETF bid-ask spread](/etf-bid-ask-spread) — related transaction cost

### Wider context

- [Closed-end fund](/closed-end-fund) — often trades at persistent discounts
- [Stock exchange](/stock-exchange) — where ETF prices are set
- [Index fund](/index-fund) — most common ETF type
- [Stock](/stock) · [Bond](/bond) — underlying holdings
- [Market capitalization](/market-capitalization) — impacts [NAV](/etf-premium-discount) calculation

</div>
