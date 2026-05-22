---
title: "Market Data Vendor"
description: "Companies that provide real-time and historical market prices, trades, and analytics to traders, funds, and institutions."
keywords:
  - market data
  - price feeds
  - data vendor
  - trading infrastructure
---

*A market data vendor is a company that collects, aggregates, and distributes real-time and historical market prices, volumes, and trade information from exchanges and [alternative trading systems](/wiki/alternative-trading-system/). They are essential infrastructure for traders, brokers, asset managers, and risk managers who depend on current quotes and historical benchmarks.*

<div class="wiki-hatnote">
For exchange-provided data, see <a href="/wiki/market-data-feed-consolidated/">Consolidated Market Data</a>. For real-time feed technology, see <a href="/wiki/financial-information-exchange/">FIX Protocol</a>.
</div>

<aside class="wiki-infobox">

| Component | Role |
|-----------|------|
| **Real-time feeds** | Live quotes, trades, depth of book |
| **Historical data** | Years of tick-by-tick or OHLC data |
| **Derived products** | Volatility, correlations, risk analytics |
| **Clients** | Asset managers, hedge funds, brokers, risk teams |
| **Delivery method** | Dedicated line, cloud API, or data download |

</aside>

## Role in the market structure

Market data vendors sit between exchanges and end-users. Exchanges publish prices to the vendors, vendors normalize and distribute them. Traders can't wait for three separate exchanges to report each quote; vendors consolidate all sources into a single stream. [NASDAQ](/wiki/nasdaq/), the [NYSE](/wiki/new-york-stock-exchange/), and others mandate that prices go to a central processor (the [SIP](/wiki/sip-securities-information-processor/)), but the SIP's data is delayed by 15–20 minutes in the retail space. Vendors offer faster, direct feeds that compete on [latency](/wiki/latency-tier/).

This is profitable business. A large asset manager might spend $100,000–$1,000,000+ per year on market data—real-time feeds for stocks, futures, options, and currencies; historical databases; and analytics tools. Multiply that across thousands of institutional clients and the revenue is substantial.

## Major vendors

**Bloomberg Terminal** dominates buy-side (asset managers) and sell-side (broker-dealers) markets. It bundles real-time data, news, analytics, and trading tools into a single system. A Bloomberg terminal costs $24,000+ per year per user but has become an industry standard for institutional finance—many traders won't accept a job unless the firm provides one.

**Refinitiv** (formerly Thomson Reuters Financial & Risk) is another major player, offering similar capabilities at lower cost and with a different workflow. **S&P Global Market Intelligence** provides detailed corporate and market data, especially for fixed income.

For high-frequency trading (HFT) and algorithmic trading, vendors like **Exegy** and **Aktiv** provide ultra-low-latency feeds and co-location services. For the retail audience, **Yahoo Finance** and **Quandl** offer free or low-cost historical data, though with delays.

## Real-time vs. historical data

Real-time feeds carry the most recent bid-ask quotes and trade prints. A trader routing an order wants to know the best price available *now*, not five minutes ago. Real-time data also supports [technical analysis](/wiki/technical-analysis/), [algorithmic trading](/wiki/algorithmic-trading/), and [risk management](/wiki/value-at-risk/).

Historical data serves [backtesting](/wiki/backtesting/), [correlation analysis](/wiki/correlation-coefficient/), and regulatory compliance. A [value-at-risk](/wiki/value-at-risk/) model needs years of return history to estimate tail [volatility](/wiki/implied-volatility/). A fund manager reporting to investors needs performance data for the exact period the fund has been operating.

Vendors offer both. Bloomberg and Refinitiv keep 20–30 years of daily and intraday data. Specialized vendors like **Quandl** and **Intrinio** focus on historical OHLC (open-high-low-close) and time-series data for [backtesting](/wiki/backtesting/) and machine learning.

## Derived products and analytics

Beyond raw prices, vendors provide computed metrics:
- **Implied volatility** ([Greeks](/wiki/options-greeks/), Black-Scholes prices for options)
- **Correlation matrices** for [portfolio optimization](/wiki/asset-allocation/)
- **Index constituents** and weightings
- **Corporate actions** (dividends, splits, mergers) with adjusted-price histories
- **Heating oil**, **natural gas**, and commodity curves for energy trading
- **Currency rates** and [forward exchange rates](/wiki/forward-exchange-rate/) for FX trading

These derived products command premium pricing because they save the client engineering time and reduce calculation errors. A quantitative fund would rather pay for volatility surfaces than maintain a team to compute them.

## Distribution and API access

Historically, market data came via proprietary terminals (Bloomberg, Reuters) or NASDAQ-provided direct feeds. Modern vendors increasingly offer APIs and cloud-based access, making real-time data available to smaller firms and retail platforms.

Brokers like **Interactive Brokers**, **E*TRADE**, and **Fidelity** bundle free delayed market data with brokerage but charge for real-time feeds. Data aggregators like **Alpha Vantage** and **Polygon.io** wrap exchange APIs and offer a single access point for equities, options, and crypto data at developer-friendly pricing.

## Regulatory aspects

Market data vendors are regulated under securities laws because they must ensure accurate reporting and prevent front-running. In the U.S., the [SEC](/wiki/securities-and-exchange-commission/) oversees [SIP](/wiki/sip-securities-information-processor/) operations. In Europe, [MiFID II](/wiki/mifid-ii/) mandates transaction reporting and post-trade transparency, creating compliance burdens on vendors that distribute trade data.

Data pricing is also regulated. Exchanges can't charge unreasonable fees for their data, but enforcement is loose; vendors and exchanges regularly clash over pricing in front of regulators.

## Impact of market structure change

The rise of [alternative trading systems](/wiki/alternative-trading-system/) (dark pools, ATSs, crossing networks) has fragmented data sources. A single stock trade can occur on the NYSE, NASDAQ, a dark pool, or an ATS simultaneously. Vendors must aggregate from many sources in real-time, a technically complex and expensive job. This has driven consolidation—the largest vendors can afford the engineering overhead; smaller ones struggle and get acquired.

The [decimalization](/wiki/tick-size-regime/) of stock prices (from 1/16 to 1/100 in 2001) vastly increased the data flow. A vendor that handled thousands of quotes per second in 2000 now handles millions. This technical challenge has raised barriers to entry and reinforced the dominance of a few large vendors.

## Crypto market data

Cryptocurrency exchanges (Coinbase, Binance, Kraken) also publish price feeds, and specialized vendors (CoinGecko, CoinMarketCap) aggregate crypto prices and provide historical data. Unlike traditional equities, crypto data is fragmented and inconsistent across venues—there is no single source of truth—so vendors provide a coordination function.

<div class="wiki-seealso">

### Closely related
- [Alternative Trading System](/wiki/alternative-trading-system/) — Non-exchange venues where market data originates
- [SIP Securities Information Processor](/wiki/sip-securities-information-processor/) — Central consolidator of exchange-reported trades
- [Market Data Feed Consolidated](/wiki/market-data-feed-consolidated/) — Official pricing from exchanges and processors
- [FIX Protocol](/wiki/financial-information-exchange/) — Standard for transmitting market data and orders
- [Latency Tier](/wiki/latency-tier/) — Speed advantage in receiving market data

### Wider context
- [Algorithmic Trading](/wiki/algorithmic-trading/) — Trading systems that depend on real-time data feeds
- [Value at Risk](/wiki/value-at-risk/) — Risk model that uses historical data from vendors
- [Implied Volatility](/wiki/implied-volatility/) — Computed by vendors for options pricing
- [Asset Allocation](/wiki/asset-allocation/) — Portfolio optimization using correlation data from vendors
- [Securities and Exchange Commission](/wiki/securities-and-exchange-commission/) — Regulates vendor practices

</div>
