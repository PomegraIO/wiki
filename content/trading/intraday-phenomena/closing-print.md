---
title: "Closing Print"
description: "The final transaction price recorded at official market close, used for end-of-day settlement and benchmark pricing."
keywords:
  - closing price
  - market close
  - settlement price
  - intraday trading
  - benchmark
---

*The **closing print** is the price of the final transaction executed at or after the official market close time. For stocks and ETFs on U.S. exchanges, this is the price of the last trade executed at 4 p.m. Eastern Time (or the [closing auction](/wiki/closing-auction/) price if the auction concludes with a cross). The closing print is the basis for daily [settlement](/wiki/settlement-cycles/) and the official end-of-day price reported in newspapers and used for fund valuations.*

<div class="wiki-hatnote">
For the intra-day trading phenomenon at the close, see <a href="/wiki/closing-auction/">/wiki/closing-auction/</a>. For the analogous opening price, see <a href="/wiki/opening-print/">/wiki/opening-print/</a>.
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Official Time** | 4:00 p.m. ET for U.S. equities and ETFs |
| **Determination Method** | Last traded price, or closing auction cross if applicable |
| **Settlement Basis** | All T+2 settlement obligations use the closing print |
| **Fund Valuation** | Mutual funds and ETFs mark positions at the closing print |
| **Derivatives Expiration** | Options and futures use closing print to determine [settlement](/wiki/cash-settlement/) |
| **Data Reporting** | Closing print is disseminated to all market data feeds within seconds |
| **Regulatory Role** | Official daily price for Form 13F and institutional reporting |
| **Manipulation Risk** | Closing prints can be subject to layering, spoofing, or wash trading |

</aside>

## How the closing print is determined

On a typical trading day, the stock market closes at 4 p.m. ET. The closing print is determined in one of two ways, depending on whether a formal [closing auction](/wiki/closing-auction/) is held.

For stocks listed on Nasdaq, the Nasdaq Official Close is the price at which the final trade executes in the continuous market at or before 4 p.m. ET. If no trade executes exactly at 4 p.m., the last trade before 4 p.m. is the closing print. This is a straightforward, mechanical definition.

For stocks listed on the NYSE, the situation is more formal. The exchange runs an intra-day continuous auction from open to 3:59:59.999 p.m., then a dedicated **closing auction** from 3:59:59 to 4:00:00 p.m. ET. The closing auction aggregates buy and sell orders, and the exchange crosses as many shares as possible at a single price — the closing auction price. This price is the closing print. If the auction produces a buy-sell imbalance and cannot clear all shares, the exchange publishes the uncrossed quantity and the reference price used in the auction, and the last trade in the continuous market before 4 p.m. becomes the closing print.

The closing auction mechanism exists to serve large institutional traders who want to execute at a single, transparent price at market close. It also ensures that mutual funds and ETFs can price their positions with precision, since they must compute their end-of-day net asset value (NAV) using a closing price.

## Why the closing price matters

The closing print is the official price for that day's settlement. Every [equity transaction](/wiki/settlement-cycles/) settled under T+2 (two business days) uses the closing price of the transaction date as the reference for delivery and payment. If you buy 1,000 shares of stock XYZ at $50 and hold overnight, your position is marked to the closing print at day's end. If it closes at $49, your mark-to-market loss is $1,000.

[Mutual funds](/wiki/mutual-fund/) and [ETFs](/wiki/etf/) use the closing print to compute their net asset value (NAV) at the end of each trading day. The NAV determines the price at which investors can buy or sell shares of the fund. If an ETF holds 100 stocks and they all close 1% lower, the fund's NAV falls by approximately 1%. Fund managers and retail investors rely on the closing print to know the fund's daily performance and to price buy/sell orders placed after market close.

[Options](/wiki/option/) and [futures](/wiki/futures-contract/) that expire at end-of-day or end-of-quarter use the closing print to determine settlement. An [in-the-money option](/wiki/in-the-money/) expires for cash or stock delivery based on the closing print on its expiration date. A stock futures contract settles to the final settlement price, which is typically the closing print (or a volume-weighted average of the last few minutes of trading).

## The closing print and market manipulation

Because the closing print is so important — it affects settlement, fund valuations, derivatives expiration, and the reported performance of portfolios — it is a target for manipulation. The SEC and market regulators have identified several abusive practices:

**Closing cross manipulation** involves an investor placing a large buy or sell order just before the closing auction, attempting to move the auction price in a direction favorable to their position. If an investor holds a short position in a stock and wants the closing print to be lower (to reduce their loss), they might flood the closing auction with sell orders at low prices, pushing the reference price down artificially.

**Layering and spoofing** refer to placing multiple orders with no intent to execute them, creating the appearance of demand or supply to attract other traders. A trader might place a large buy order at 3:59:59 p.m., then immediately cancel it if the stock price is rising, to benefit short positions or futures positions that are repriced using the closing print.

The SEC has brought enforcement actions against traders and firms for manipulating closing prints, including cases where sophisticated traders colluded with brokers to execute trades at prices that benefited their derivatives positions.

## After-hours trading and the official close

After the 4 p.m. official close, many stocks continue trading in after-hours venues (Electronic Communication Networks and broker-operated systems). However, these trades are not considered part of the official closing print. The closing print is the final trade at or before 4 p.m. ET.

After-hours prices can move substantially — a stock might close at $50 but trade down to $48.50 after-hours if news breaks post-close. However, the next day's [opening print](/wiki/opening-print/) is determined by the opening auction at 9:30 a.m. ET, and the official daily prices use the 4 p.m. closing print for the previous day and the 9:30 a.m. opening print for the next day. After-hours prices are recorded, reported to FINRA, and disseminated, but they do not affect the official closing price used for settlement and fund NAV.

## The closing print in different market segments

**Bonds** settle in secondary markets at various times throughout the day; there is no universal "closing print" for bonds, though the last trade before the bond market closes (typically around 5 p.m. ET) is often cited as the day's price.

**Currencies** trade 24 hours globally. The "closing print" concept is less relevant; instead, prices are cited as of specific fix times (e.g., the 4 p.m. ET fix for major currency pairs).

**Commodities** futures contracts traded on the CME close at 4 p.m. CT (5 p.m. ET) for energy and agricultural products, and other times for different contracts. Each contract's closing print is the last trade before the official close time for that product.

## Reporting and dissemination

The closing print is disseminated to all market participants within seconds of the official close through the [SIP](/wiki/sip-securities-information-processor/) (Securities Information Processor) feeds that aggregate data from all U.S. stock exchanges. Reuters, Bloomberg, and other financial data vendors publish the closing print immediately, and it becomes the reference price in broker-dealer systems, index calculations, and public databases.

<div class="wiki-seealso">

### Closely related
- <a href="/wiki/closing-auction/">/wiki/closing-auction/</a> — The formal auction mechanism at market close
- <a href="/wiki/opening-print/">/wiki/opening-print/</a> — The opening price determination
- <a href="/wiki/settlement-cycles/">/wiki/settlement-cycles/</a> — How trades settle and prices are used
- <a href="/wiki/after-hours-trading/">/wiki/after-hours-trading/</a> — Trading after the official close

### Wider context
- <a href="/wiki/etf/">/wiki/etf/</a> — How closing prices affect fund valuations
- <a href="/wiki/option-expiration/">/wiki/option-expiration/</a> — How closing prices determine derivative settlement
- <a href="/wiki/market-surveillance/">/wiki/market-surveillance/</a> — Detecting manipulative trading
- <a href="/wiki/trade-reporting/">/wiki/trade-reporting/</a> — How trades are recorded and disseminated

</div>