---
title: "ETF Net Asset Value"
description: "The end-of-day value per share of an ETF's holdings, calculated by dividing the fund's total assets minus liabilities by shares outstanding."
keywords:
  - etf valuation
  - nav
  - fund pricing
  - market price
  - premium discount
image: /svg/funds.svg
---

*An **ETF Net Asset Value** (NAV) is the closing-bell value per share of an exchange-traded fund's underlying basket of securities, calculated daily by the [ETF sponsor](/etf-sponsor/) as total fund assets minus liabilities, divided by shares outstanding. Because ETFs trade continuously throughout the day while NAV is computed only once daily, the ETF's market price often diverges from its NAV—sometimes trading at a premium or discount that can create or destroy value for unwary investors.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ETF Net Asset Value — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark representing fund architecture and valuation." />

<div class="wiki-infobox-caption">End-of-day value per share, the NAV is distinct from the real-time trading price.</div>

|   |   |
|---|---|
| **What it is** | Total fund assets minus liabilities, divided by shares outstanding, published daily at market close |
| **Also called** | NAV, fund value, intrinsic value |
| **Calculated by** | The [ETF sponsor](/etf-sponsor/) or [custodian](/etf-custodian/), based on closing prices of holdings |
| **Published** | Once daily, typically after 4 p.m. ET in the US |
| **Real-time equivalent** | [Indicative NAV](/indicative-nav/), updated continuously during trading hours |
| **Common divergence** | Market price may trade at premium or discount to NAV; larger spreads reflect market demand |
| **Used for** | Assessing true fund value, detecting mispricings, redemption pricing for institutional investors |

</aside>

## Why NAV is calculated at close, not intraday

The NAV of an ETF is a backward-looking number: it reflects the closing prices of all securities in the fund at the end of each trading day. The [ETF sponsor](/etf-sponsor/) or its agent (often the [custodian](/etf-custodian/)) collects the day's closing valuations, settles any cash flows, and publishes a single NAV figure, usually between 4 and 6 p.m. Eastern Time. This one-per-day calculation made sense historically when funds were less liquid and pricing infrastructure was simpler; it remains the official measure for [SEC](/securities-and-exchange-commission/) reporting, tax, and [redemption](/redemption-rights-equity/) purposes.

The trade-off is clear: traders cannot rely on NAV to guide them during the trading day. An ETF tracking the S&P 500 is worth something different at 10 a.m. than at 4 p.m., yet only the closing NAV is official. This is why [indicative NAV](/indicative-nav/) exists—a real-time estimate designed to keep market prices honest.

## Market price versus NAV: the premium and discount

Because ETFs trade on [exchanges](/stock-exchange/) alongside stocks, their market prices are set by supply and demand—bid and ask orders from thousands of traders. The NAV, in contrast, is a mechanical calculation of what the fund's holdings are actually worth. When the market price exceeds NAV, the ETF trades at a premium. When it falls below, there is a discount.

A small premium or discount (under 0.5%) is normal and reflects [bid-ask spreads](/bid-ask-spread/), [trading costs](/market-maker-trading/), and the natural lag between intraday trading and closing NAV. Larger discrepancies can signal genuine mispricings. If a broad-market ETF trades at a 2% discount for days, traders may buy it in size, then redeem the shares to the sponsor in exchange for the underlying securities—pocketing the arbitrage. This [creation](/authorized-participant/) and [redemption](/redemption-rights-equity/) mechanism is what keeps ETF prices anchored to NAV over time.

## Why NAV matters for different investors

For buy-and-hold investors, NAV is chiefly useful as a sanity check. If you own an [index fund](/index-fund/) tracking the broad market, the day-to-day premium or discount is noise; you care about the underlying portfolio's true value. For [active traders](/algorithmic-trading/) or those timing entry and exit, a deep discount may signal an opportunity to buy cheaply and redeem, or it may indicate market stress.

Institutional investors, especially [authorized participants](/authorized-participant/) who handle ETF creation and redemption, live by NAV. They arbitrage between the secondary market (where the ETF trades) and the primary market (where they trade underlying securities directly with the sponsor). If the ETF trades below NAV, they can buy it on the exchange, redeem for the underlying securities, and sell those securities separately—locking in the spread. This mechanism requires an accurate, transparent NAV.

## How NAV is calculated in practice

The formula is straightforward:

NAV per share = (Total Assets – Total Liabilities) / Shares Outstanding

On paper, this is simple. In practice, valuation complexity arises when the fund holds hard-to-price instruments—international equities trading on distant exchanges, illiquid bonds, or derivatives. The [custodian](/etf-custodian/) must decide whether to use closing prices from each security's home market or apply a delayed adjustment if markets have moved since close. Most sponsors use closing prices from the relevant market where each security traded, applying standard valuation rules from the [SEC](/securities-and-exchange-commission/) and [generally accepted accounting principles](/generally-accepted-accounting-principles/).

## The gap between NAV and trading price: arbitrage and market stress

On calm trading days, the arbitrage machinery keeps ETF prices within a few basis points of NAV. But during market dislocations—sharp drops, liquidity crises, or flight-to-safety rallies—the gap can widen. In the COVID-19 crash of March 2020, even core bond ETFs traded at steep discounts to NAV because investors panic-selling outpaced the ability of [authorized participants](/authorized-participant/) to redeem and rebalance. Wide NAV discounts then served as a warning signal that redemption capacity was strained and liquidity was breaking down.

For this reason, [SEC](/securities-and-exchange-commission/) rules require sponsors to disclose when an ETF is trading at an unusual discount, and to post [indicative NAV](/indicative-nav/) data to help market participants assess fair value in real time.

## See also

<div class="wiki-seealso">

### Closely related

- [Indicative NAV](/indicative-nav/) — real-time estimated NAV updated throughout the trading day
- [ETF Sponsor](/etf-sponsor/) — the asset manager responsible for calculating and publishing NAV
- [ETF Custodian](/etf-custodian/) — the bank that holds securities and often assists in NAV computation
- [ETF Premium-Discount](/etf-premium-discount/) — the gap between market price and NAV, and what it signals
- [Authorized Participant](/authorized-participant/) — the institution that arbitrages between ETF price and NAV via creation and redemption
- [Net Asset Value](/etf-net-asset-value/) — concept extended to closed-end funds and mutual funds

### Wider context

- [ETF](/etf/) — overview of exchange-traded funds and their mechanics
- [Index Fund](/index-fund/) — structure of funds designed to track an index
- [Secondary Market](/secondary-market/) — where ETF shares trade after issuance
- [Redemption Rights (Equity)](/redemption-rights-equity/) — the mechanism by which authorized participants convert shares to underlying securities
- [Bid-Ask Spread](/bid-ask-spread/) — component of trading costs that affects ETF pricing

</div>
