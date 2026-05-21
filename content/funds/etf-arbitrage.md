---
title: "ETF Arbitrage"
description: "ETF arbitrage is the profit opportunity when an ETF's market price diverges from its underlying NAV. Authorized participants exploit these gaps by simultaneously buying one asset and selling the other, keeping ETF prices efficient."
keywords:
  - ETF arbitrage
  - cash arbitrage
  - conversion arbitrage
  - NAV divergence
  - authorized participant
  - fund
image: "/svg/funds.svg"
---

*[ETF arbitrage](/etf-arbitrage) is the profit opportunity that arises when an [ETF](/etf)'s trading price diverges from the [NAV](/etf-premium-discount) — the true underlying value of its holdings. When this gap emerges, [authorized participants](/authorized-participant) can buy one asset (either the ETF shares or the underlying basket of securities) and simultaneously sell the other, locking in a risk-free profit. This arbitrage process keeps [ETF](/etf) prices aligned with value.*

<div class="wiki-hatnote">

This entry covers ETF arbitrage mechanically. For the pricing mechanism, see [ETF premium and discount](/etf-premium-discount); for who executes arbitrage, see [authorized participant](/authorized-participant).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ETF Arbitrage — key facts</div>

<img src="/svg/funds.svg" alt="A price chart showing an ETF price briefly diverging from NAV" />

<div class="wiki-infobox-caption">Arbitrage opportunities enforce pricing discipline in ETF markets.</div>

|   |   |
|---|---|
| **What it is** | Risk-free profit from ETF-NAV price divergence |
| **Also called** | Cash arbitrage, conversion arbitrage |
| **Participants** | [Authorized participants](/authorized-participant), market makers, high-frequency traders |
| **How often it occurs** | Constantly; arbitrage windows typically milliseconds to seconds |
| **Typical profit margin** | 0.1% to 0.5% per trade (can be wider during market stress) |
| **Capital required** | Millions to tens of millions |
| **Execution speed** | Microseconds (for professional traders) |

</aside>

## How ETF arbitrage works: a concrete example

Suppose the S&P 500 is worth 5,000 points, and an [equity ETF](/equity-etf) holding the index should be worth $500 per share. Here is what happens if it trades at $501 instead:

**The arbitrage:**

1. An [authorized participant](/authorized-participant) sees the ETF trading at $501, above its true value of $500.
2. The AP buys a basket of the 500 stocks that replicate the S&P 500 index for $500 (the fair value).
3. **Simultaneously**, the AP sells the [ETF](/etf) short at $501.
4. The AP delivers the basket of stocks to the fund and redeems them for ETF shares.
5. The AP covers the short by delivering the newly created ETF shares.
6. **Result:** The AP bought at $500 and sold at $501, locking in a $1 profit per share, or 0.2%.

The AP's profit is guaranteed because it happened before anything moved. The AP was not betting on price direction; it was purely capturing the divergence between the market price and [NAV](/etf-premium-discount).

## Why arbitrage prices are imperfect

[ETF arbitrage](/etf-arbitrage) is not genuinely risk-free in practice. Several frictions limit it:

**Transaction costs.** The AP must pay commissions, [bid-ask spreads](/etf-bid-ask-spread), and market impact to buy the 500 stocks. These costs eat into the profit. If the basket costs 0.15% in transaction costs to gather, but the arbitrage opportunity is only 0.2%, the profit shrinks to 0.05%, barely worth executing.

**Time delays.** Gathering 500 stocks (or a large bond portfolio) takes time. In that time, prices move. The stocks might fall 0.1% before the AP has finished gathering them, turning what looked like a 0.2% profit into a 0.1% profit.

**Funding costs.** The AP must borrow capital to execute the trade, paying short-term interest rates. These borrowing costs chip away at profits.

**Underlying illiquidity.** Some [ETFs](/etf) hold illiquid bonds, emerging market stocks, or other securities that are expensive to trade. The transaction cost to gather a basket can be steep, limiting arbitrage.

## Convergence and divergence: what causes gaps

[ETF](/etf) prices and [NAV](/etf-premium-discount) diverge mainly during market stress or gaps:

**Market gaps.** When the stock market gaps open sharply (due to overnight news or geopolitical shocks), [ETFs](/etf) can gap open differently than their [NAV](/etf-premium-discount). The underlying stocks might gap 3% but the ETF price 2%, creating an arbitrage opportunity.

**Overnight and international.** [ETFs](/etf) holding international stocks or bonds face time-zone challenges. When the Tokyo market closes and the New York market opens, an [ETF](/etf) holding Japanese stocks might diverge from its [NAV](/etf-premium-discount) because the US price is set before the underlying assets finish trading.

**Liquidity crises.** During financial stress (like March 2020), [ETFs](/etf) can trade at steep premiums or discounts to [NAV](/etf-premium-discount) because:
  - The AP market makers become risk-averse and stop creating/redeeming.
  - Investors panic-sell [ETFs](/etf) indiscriminately, pressing prices below [NAV](/etf-premium-discount).
  - The underlying securities become hard to trade, making arbitrage expensive.

In the COVID crash, some bond [ETFs](/etf) traded at 5%+ discounts to [NAV](/etf-premium-discount) because the underlying bonds became illiquid and difficult to trade.

## When arbitrage breaks

The arbitrage mechanism can fail if:

1. **APs withdraw.** If all [authorized participants](/authorized-participant) stop creating and redeeming due to stress or capital constraints, prices can drift without correction.
2. **Custody issues.** If there is a problem with the [ETF](/etf)'s custodian (the institution holding the securities), APs may refuse to redeem until the issue is resolved.
3. **Regulatory intervention.** If markets are closed or trading is halted, arbitrage cannot execute.
4. **Leverage constraints.** APs operate with leverage and margin. If leverage constraints tighten, APs may be unable to finance the arbitrage trade.

## Who benefits from ETF arbitrage

Retail investors benefit indirectly because arbitrage keeps [ETF](/etf) prices tight and efficient. You do not capture the arbitrage profit yourself, but you benefit from tight [bid-ask spreads](/etf-bid-ask-spread) and efficient pricing.

[Authorized participants](/authorized-participant) and market makers profit directly. An AP that can execute arbitrage trades in milliseconds can capture 0.1%–0.3% per trade, compounding to substantial returns when executed thousands of times per day.

High-frequency trading firms also profit from [ETF arbitrage](/etf-arbitrage), often operating at microsecond timescales, capturing profit margins so small that only machine trading makes them worthwhile.

## Historical context

[ETF arbitrage](/etf-arbitrage) was one of the forces that made [ETFs](/etf) practical. Before [creation and redemption](/etf-creation-redemption) mechanisms, fund prices could drift significantly from [NAV](/etf-premium-discount) because there was no way to arbitrage the difference. The arbitrage mechanism is why [ETFs](/etf) have become so efficient and why they have largely displaced [mutual funds](/mutual-fund).

## See also

<div class="wiki-seealso">

### Closely related

- [ETF](/etf) — the broader category
- [Authorized participant](/authorized-participant) — who executes arbitrage
- [ETF creation and redemption](/etf-creation-redemption) — what enables arbitrage
- [ETF premium and discount](/etf-premium-discount) — what arbitrage corrects
- [ETF bid-ask spread](/etf-bid-ask-spread) — related transaction cost

### Wider context

- [Stock exchange](/stock-exchange) — where arbitrage trades execute
- [Broker](/broker) — facilitates arbitrage trades
- [Index fund](/index-fund) — most common arbitrage target
- [Stock](/stock) · [Bond](/bond) — underlying holdings
- [Market capitalization](/market-capitalization) — impacts arbitrage scale

</div>
