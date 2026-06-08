---
title: "Indicative NAV"
description: "A real-time estimated net asset value of an ETF's holdings, updated throughout the trading day to help traders assess fair value and detect premiums or discounts."
keywords:
  - inav
  - etf pricing
  - real-time nav
  - fair value
  - trading premium
image: /svg/funds.svg
---

*An **Indicative NAV** (iNAV) is an intraday, continuously updated estimate of an exchange-traded fund's per-share value based on real-time or near-real-time pricing of its holdings. Unlike the official [ETF Net Asset Value](/etf-net-asset-value/), which is published once daily at market close, iNAV appears on trading venues and data terminals during market hours, allowing traders to gauge whether an ETF is trading at a fair price, premium, or discount to its true underlying value in the moment.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Indicative NAV — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark representing fund architecture and valuation." />

<div class="wiki-infobox-caption">Real-time NAV estimate that helps traders spot mispricings during the trading day.</div>

|   |   |
|---|---|
| **What it is** | Continuously updated estimate of an ETF's value per share, based on current prices of underlying holdings |
| **Also called** | iNAV, intraday NAV, fair value estimate |
| **Updated** | Every 15 seconds or faster, throughout trading hours |
| **Published by** | [ETF sponsors](/etf-sponsor/), exchanges, and market data vendors |
| **Official NAV** | Published once daily at market close; iNAV is indicative only |
| **Use case** | Helps traders detect premiums/discounts and assess fair entry or exit prices during the day |
| **Data inputs** | Real-time (or 15-second delayed) prices of all holdings; currency rates for international ETFs |

</aside>

## Why iNAV exists: filling the information gap

Before iNAV became standard in the 2000s, traders faced an awkward problem. The [official NAV](/etf-net-asset-value/) wasn't published until hours after the market closed, yet the ETF itself traded continuously during the day. If you were deciding whether to buy an ETF at 2 p.m., you had no current measure of what its holdings were actually worth. You could estimate by tracking index levels and individual stock prices, but that was labor-intensive and error-prone. Enter iNAV: a machine-readable, continuously refreshed proxy for intrinsic value.

iNAV is calculated by the [ETF sponsor](/etf-sponsor/) (or a data vendor acting on the sponsor's behalf) using the real-time prices of the fund's holdings. For a simple [index ETF](/index-fund/) tracking the S&P 500, iNAV is computed by applying current prices of all 500 stocks to their weights in the fund, adding cash, subtracting expenses, and publishing the result every few seconds. The math is transparent and mechanical, making it a reliable reference point for market participants and regulators alike.

## How traders use iNAV to detect mispricings

The gap between an ETF's market price and its iNAV is the premium or discount. On most days, this gap is tiny—a few basis points—because [authorized participants](/authorized-participant/) stand ready to arbitrage any material divergence. If an ETF trading at $100 has an iNAV of $99.50, sophisticated traders can buy the ETF, redeem it directly to the sponsor in exchange for the underlying securities, and immediately sell those securities in the cash market—locking in the 50-basis-point profit.

However, iNAV premiums and discounts can spike during market stress or when liquidity dries up. In March 2020, when credit markets seized up and bond ETFs were swamped with redemption requests, some high-yield bond ETFs traded at discounts of 5% or more to their iNAV—a signal that redemption capacity was strained and the fund was under genuine strain. Traders watching iNAV in real time saw this signal immediately; those relying on the daily NAV figure discovered the problem only after the fact.

## iNAV for different fund types

For simple, liquid equity ETFs, iNAV is straightforward. The sponsor uses real-time or near-real-time quotes for all holdings, applies a straightforward weighting, and publishes. For more complex ETFs—those holding international stocks, commodities, or bonds—iNAV is trickier but still feasible. An [international equity ETF](/etf/) holding stocks on multiple exchanges uses the most recent quote from each exchange, adjusted for currency moves. A commodity ETF holding [crude oil](/crude-oil/) or [natural gas](/natural-gas/) futures adjusts for the latest futures prices.

The most challenging case is the [closed-end fund](/closed-end-fund/) or niche [actively managed ETF](/actively-managed-fund/), where some holdings may be illiquid or priced infrequently. In these cases, iNAV may rely on model-based fair values, index levels, or slight delays in data—e.g., using the prior day's close for truly illiquid positions. The [SEC](/securities-and-exchange-commission/) requires sponsors to publish iNAV with clear documentation of sources and any material data delays.

## The regulatory mandate and market structure

The [SEC](/securities-and-exchange-commission/) requires ETF sponsors to publish iNAV data for all funds and mandates that exchanges disseminate it to the public. This is part of the broader effort to make ETF pricing transparent and to prevent the kind of mispricings that plagued older closed-end funds, which often traded at steep discounts because retail investors had no sense of true value.

Most iNAV data flows through major quote services—Bloomberg, FactSet, and the exchange feeds themselves—and appears on [alternative trading systems](/alternative-trading-system/), broker platforms, and news terminals. Retail traders can see iNAV on their brokers' order tickets, comparing it to the current bid and ask. This transparency has been a competitive advantage for ETFs versus mutual funds, which publish NAV only once daily and thus cannot offer intraday guidance.

## The distinction: iNAV is not the official NAV

It bears repeating: iNAV is an estimate, not the official fund value. The [ETF Net Asset Value](/etf-net-asset-value/) published at market close is what matters for tax reporting, accounting, performance measurement, and redemptions. If you redeem shares, you receive the official NAV price from that day. But during trading, iNAV is your best clue to whether you're paying a fair price.

On rare occasions, a data error or exchange glitch can cause iNAV to diverge wildly from the true intrinsic value of the holdings. In extreme cases, exchanges have halted trading in an ETF if iNAV becomes materially stale or erroneous. These incidents are rare because data feeds are redundant and sponsors actively monitor iNAV quality.

## See also

<div class="wiki-seealso">

### Closely related

- [ETF Net Asset Value](/etf-net-asset-value/) — the official daily NAV; iNAV is a continuous estimate
- [ETF Sponsor](/etf-sponsor/) — the firm responsible for calculating and publishing iNAV
- [ETF Premium-Discount](/etf-premium-discount/) — how iNAV is used to detect when an ETF is mispriced relative to holdings
- [Authorized Participant](/authorized-participant/) — the trader or firm that arbitrages between iNAV and market price
- [Bid-Ask Spread](/bid-ask-spread/) — trading spread; a narrow iNAV-to-price gap indicates tight spreads and good liquidity

### Wider context

- [ETF](/etf/) — overview of exchange-traded fund structure and mechanics
- [Index Fund](/index-fund/) — funds that track an index use iNAV to keep prices aligned with index levels
- [Secondary Market](/secondary-market/) — where iNAV applies; pricing during active trading
- [Price Discovery](/price-discovery/) — iNAV contributes to efficient pricing discovery in ETF markets
- [Market Maker (Trading)](/market-maker-trading/) — market makers rely on iNAV to manage ETF inventory and quote prices

</div>
