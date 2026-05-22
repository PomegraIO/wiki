---
title: "Fund Valuation"
description: "The daily calculation of net asset value based on the current market prices of underlying securities."
keywords:
  - net asset value
  - fund pricing
  - daily valuation
  - asset pricing
---

*Fund valuation is the daily process of calculating a [mutual fund](/wiki/mutual-fund/) or exchange-traded fund's net asset value (NAV) by determining the current market value of all underlying securities and dividing by the number of shares outstanding. The NAV is the price at which fund shares are bought and sold, and it reflects the fund's total assets minus liabilities, divided evenly across all shareholder units.*

<aside class="wiki-infobox">

| Component | Role |
|---|---|
| **NAV formula** | (Total Assets − Total Liabilities) / Shares Outstanding |
| **Timing** | Calculated daily, usually at market close |
| **Price used** | Current market prices of holdings |
| **Illiquid assets** | Estimated fair value by pricing committee |
| **Frequency update** | Once per day for mutual funds; continuous for ETFs |
| **Investor use** | Price at which shares are bought or sold |

</aside>

## The NAV formula: the mathematical foundation

The [net asset value](/wiki/net-asset-value/) (NAV) is computed daily using a straightforward formula: take the total market value of all securities held by the fund, subtract any liabilities (management fees accrued, borrowings, accounts payable), and divide by the number of shares outstanding. The result is the NAV per share—the price at which investors buy into or exit the fund.

Example: A fund holds $100 million in stocks, $10 million in bonds, and $2 million in cash. Total assets are $112 million. The fund has $2 million in accrued expenses and a $5 million bank loan. Total liabilities are $7 million. Net assets are $105 million. If 10 million shares are outstanding, NAV per share is $10.50. Investors buy or sell fund shares at or very close to $10.50.

The NAV is distinct from the **market price** of fund shares in the secondary market. For [mutual funds](/wiki/mutual-fund/), the NAV is the official price; buy/sell transactions happen at NAV (plus or minus a small load, if applicable). For [exchange-traded funds](/wiki/etf/), the market price fluctuates throughout the trading day, while the NAV is calculated once (usually at market close). ETF shares trade at a small [premium or discount](/wiki/etf-premium-discount/) to NAV during the day because market demand can drive the price above or below the underlying asset value.

## Timing of valuation and data sources

Most mutual funds calculate NAV once per day, typically at 4 p.m. Eastern Time (the stock market close). All securities are priced at or very near their closing prices. Bond funds may use closing prices from bond markets, which close at different times than equities. Money market funds may use different pricing conventions. Pricing is usually handled by a third-party pricing service—companies like Interactive Data or Bloomberg provide market-level prices to fund administrators.

The [closing auction](/wiki/closing-auction/) in stock markets is the primary source for equity prices. Bonds, which trade over-the-counter with less frequent pricing data, are priced by dealers or interpolation. When a security is not actively traded on the valuation date, the pricing committee uses "fair value" estimation—mark-to-model approaches that estimate what the security would be worth if traded. This is more art than science and is where fund valuation becomes judgmental.

## Handling illiquid and hard-to-price securities

The biggest challenge in fund valuation is pricing illiquid or unique securities. A large fund holding emerging-market bonds, thinly traded equities, or private investments cannot always use closing market prices because these securities may not trade daily. The fund's pricing committee (often a subcommittee of the board) is responsible for determining fair value using available information.

Fair value methods include comparable company multiples, comparable transaction prices, discounted cash flow models, and broker quotes. The committee must document its methodology and apply it consistently. If the security is later traded at a public price, the committee can check its estimate against reality. Systematic overvaluation or undervaluation of illiquid securities would distort NAV and disadvantage incoming or exiting shareholders.

For many funds, illiquid securities are a small portion of assets and handled through standard hierarchies. For specialized funds—private equity funds, hedge funds, real estate funds—valuation is more complex and is often the main source of risk in the NAV calculation. Investors in these funds must trust the fund's pricing governance to be rigorous.

## Price impact of fund-wide transactions

When a large fund receives new investor money or experiences outflows, the NAV can be affected. If a fund receives $10 million in new deposits on a day when the market is falling, the fund receives cash at a moment of weakness. If the fund immediately deploys that cash into securities, it may buy at slightly worse prices than reflected in the NAV calculation (which occurred moments earlier). Similarly, when a large investor redeems shares, the fund may have to sell securities to meet the redemption, incurring transaction costs.

[Mutual funds](/wiki/mutual-fund/) often use a "swing pricing" mechanism to address this: if net flows are large, the NAV is adjusted upward (on deposit days) or downward (on redemption days) to reflect the trading costs incurred. This ensures that continuing shareholders are not disadvantaged by the costs of flows. The swing adjustment is typically small (a few basis points) and aims to be fair and transparent.

## NAV and fee calculations

The [management fee](/wiki/management-fee/) charged by the fund is often a percentage of average NAV. If a fund has an average NAV of $100 million and a 0.5% annual fee, the fee is $500,000 per year. The fee is usually calculated monthly or quarterly and accrued in the NAV. When you see the NAV reported, it already reflects the accrual of management fees.

Some fees, called "fulcrum fees," adjust based on the fund's performance relative to a benchmark. These are uncommon but require NAV to be recalculated if performance changes. More commonly, fees are flat percentages, unaffected by performance. The [expense ratio](/wiki/expense-ratio/) (total fees and expenses as a percentage of NAV) is disclosed to investors and affects returns. A fund with lower expenses will have a higher NAV over time, all else equal, because less is being charged.

## ETF intraday pricing and NAV premium/discount

ETFs are priced continuously throughout the trading day, unlike mutual funds. The market price of an ETF can drift above or below its NAV due to supply and demand. If many investors suddenly want to buy an ETF (perhaps because the underlying sector is hot), the market price may rise above NAV. If everyone wants to sell, it may fall below. This [ETF premium or discount](/wiki/etf-premium-discount/) is arbitraged away by [authorized participants](/wiki/authorized-participant/)—large institutions that can create and redeem ETF shares—but can persist for minutes or hours.

The NAV itself is calculated once per day, usually at market close. [ETF intraday pricing](/wiki/etf-intraday-pricing/) during the day relies on tracking the underlying holdings in real-time. Most ETF data providers publish an "indicative NAV" every 15 seconds, calculated from the latest mid-prices of the holdings. This allows traders to see what the ETF should be worth throughout the day, independent of its market price. The difference between market price and indicative NAV tells you how much premium or discount exists.

## Fund splits and distributions impact on NAV

When a fund makes a dividend or capital gains distribution, the NAV falls by the amount of the distribution on the ex-date. If a fund's NAV is $25 and it distributes $2 per share, the NAV on the ex-date becomes $23. The shareholder receives the distribution (cash or reinvested shares) and ends up with the same total value, but the NAV per share has declined. This is purely mechanical—the fund is not shrinking; value is simply being transferred from the fund to the shareholder.

A fund split (increasing the number of shares outstanding) has no impact on NAV. If a fund splits its shares 2-for-1, the NAV is halved, but the shareholder's total value is unchanged. They now own twice as many shares, each worth half as much. The NAV formula automatically handles this because it divides total assets by total shares outstanding.

## NAV as the investor's interface with the fund

For the investor, NAV is the most important piece of information. It is the price you pay to buy shares and the price you receive to sell shares. It is fully transparent—published daily and often quoted in financial media and on fund websites. When you invest $10,000 in a mutual fund, you receive $10,000 / NAV shares. If NAV is $25, you get 400 shares.

The NAV's accuracy depends on the quality of the underlying pricing and the rigor of the pricing committee. Undervaluation artificially depresses NAV, allowing new shareholders to buy shares cheaply relative to their true value, which is unfair to existing shareholders. Overvaluation does the opposite, penalizing new shareholders. The fund's board is responsible for ensuring the pricing process is sound. For most funds, NAV is calculated by a reputable third-party administrator and relies on standardized pricing data, making accuracy high. For specialized or illiquid funds, more caution is warranted.

<div class="wiki-seealso">

### Closely related
- [Net Asset Value](/wiki/net-asset-value/) — Fundamental pricing for fund shares
- [Mutual Fund](/wiki/mutual-fund/) — Open-end investment company structure
- [ETF](/wiki/etf/) — Exchange-traded fund structure and trading
- [ETF Premium Discount](/wiki/etf-premium-discount/) — NAV vs. market price divergence
- [Expense Ratio](/wiki/expense-ratio/) — Cost of fund ownership as % of assets

### Wider context
- [Fund Accounting](/wiki/fund-accounting/) — Record-keeping for fund assets and shares
- [Management Fee](/wiki/management-fee/) — Charge to manage the fund
- [Authorized Participant](/wiki/authorized-participant/) — Institutions that arbitrage ETF NAV
- [Price Discovery](/wiki/price-discovery/) — How market prices are established

</div>
