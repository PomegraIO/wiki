---
title: "Crypto Sub-Account Trading Explained"
description: "Crypto sub-accounts let traders partition funds into separate trading accounts on an exchange. Learn how they work, why traders use them, and the custody implications."
keywords:
  - crypto sub account
  - sub-account trading
  - exchange accounts
  - position isolation
  - crypto custody
---

*Crypto sub-accounts (also called sub-accounts or virtual accounts) are partitioned accounts within a single exchange that allow a trader to segment funds and maintain separate order books and positions. A trader might use one sub-account for spot trading, another for [derivatives](/derivatives-hedging/), and a third for a different strategy or client. Each sub-account typically has its own balance sheet, [API keys](/cryptocurrency-exchange/), and trading history, but funds remain under the trader's main account—not segregated in separate [custody](/custodian/). This architecture simplifies multi-strategy management and risk isolation without requiring accounts at multiple exchanges, though it comes with custody and operational trade-offs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Crypto Sub-Accounts — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Sub-accounts partition trading and risk within a single exchange, not across separate custodians.</div>

|   |   |
|---|---|
| **Core benefit** | Isolate positions, strategies, and API access without multiple exchange accounts |
| **Typical use** | Separate spot and futures trading; manage multiple strategies or clients |
| **Custody status** | Funds remain commingled in the exchange's main account; not segregated |
| **API access** | Each sub-account can have dedicated API keys and IP whitelisting |
| **Capital transfer** | Usually instant or near-instant between sub-accounts on the same exchange |
| **Risk isolation** | Partial—loss in one sub-account from liquidation affects only that position |
| **Popular platforms** | Binance, Kraken, Coinbase Pro (though feature availability varies by exchange) |

</aside>

## How Sub-Accounts Work

Most cryptocurrency exchanges that offer sub-account functionality let a primary user create one or more child accounts under their main login. From a technical standpoint, the exchange maintains a master wallet for the trader's total balance, but the [trading engine](/cryptocurrency-exchange/) tracks internal ledger entries for each sub-account.

**Example structure:**

| Sub-Account | Purpose | Balance | Status |
|---|---|---|---|
| Main Account | Default trading | 10 BTC | Active |
| Spot Trading | Long-term holds | 3 BTC | Active |
| Futures | Leveraged positions | 5 BTC | Active |
| Client A | Managed portfolio | 2 BTC | Active |

Each sub-account has its own order book and position history. If a trader places a buy order in the Spot Trading sub-account, it does not affect the Main Account or Futures sub-account balances. The trader can use different [API keys](/cryptocurrency-exchange/) for each sub-account, enabling separate bots or algorithms to run independently.

## Why Traders Use Sub-Accounts

### Risk Isolation

A liquidation or drawdown in one sub-account does not immediately affect others. A trader running a leveraged futures strategy in one sub-account can be confident that a 100x position blow-up will not drain the spot portfolio in another sub-account. This mental and operational boundary reduces systemic risk to the trader's overall position.

### Operational Segregation

Different trading strategies often require different rules and monitoring. A swing-trading sub-account might trade in minutes; a buy-and-hold sub-account might sit untouched for months. Separate sub-accounts allow a trader to run different bots, alert thresholds, and rebalancing logic without cross-contamination.

### Client and Manager Segregation

Institutional traders or fund managers often use sub-accounts to isolate client portfolios. One sub-account might hold Fund A's capital, another Fund B's. Each has its own reporting, fee tracking, and withdrawal rights. While not true segregation (funds are not held at separate custodians), it simplifies internal bookkeeping and reduces the risk of accidentally mixing client assets.

### API Key Isolation

If a trader runs automated bots, each sub-account can have dedicated API keys with specific permissions (trade-only, no withdrawal, IP-restricted, etc.). If one API key is compromised, the attacker gains access only to that sub-account's balance and positions—not the entire portfolio.

### Multiple Strategies Without Multiple Exchanges

A trader might want to run a mean-reversion bot, a trend-following bot, and a market-making bot simultaneously. Rather than opening accounts at three different exchanges, the trader can spin up three sub-accounts at one exchange, reducing operational overhead and [counterparty risk](/counterparty-risk/).

## Custody and Commingling Risk

The critical caveat is that sub-accounts are *not* segregated accounts. The exchange holds all sub-account balances in a commingled pool under the trader's main account. If the exchange experiences a [liquidation](/liquidation/) or insolvency, the trader's claim against the exchange is the total balance across all sub-accounts, not separate protected tiers.

This differs from:

- **Segregated accounts** — Physical or accounting separation at a single custodian or across multiple custodians, where client assets are isolated from the institution's own capital.
- **Separate custodians** — Holding assets at different entities (e.g., one fund's assets at one exchange, another fund's at a second exchange), which isolates counterparty risk.

Sub-accounts offer convenience and some internal operational isolation, but they do *not* mitigate exchange [counterparty risk](/counterparty-risk/). If Binance fails, a trader with 5 sub-accounts there loses access to all of them equally.

## How Funds Move Between Sub-Accounts

Most major exchanges allow instant or near-instant transfers of assets between sub-accounts on the same platform. The exchange's backend simply moves a ledger entry; no [blockchain](/blockchain-fundamentals/) transaction occurs. This speed and zero [transaction cost](/cryptocurrency-exchange/) make sub-accounts convenient for reallocating capital across strategies.

However, transfers *out* of the exchange (to an external wallet) typically require the withdrawal to come from the specific sub-account holding the funds. A trader cannot transfer from Sub-Account A to Sub-Account B, then withdraw from Sub-Account C, without moving assets explicitly.

## Platform Differences

**Binance** — Offers sub-accounts with full feature parity (spot, [futures](/futures-contract/), margin). Each sub-account can have independent API keys. Sub-accounts are free to create and manage.

**Kraken** — Supports sub-accounts but with limitations on certain trading pairs and features. API isolation is less granular than Binance.

**Coinbase Pro** — Does not offer sub-accounts; users must open separate accounts (with separate email addresses) to partition portfolios.

**FTX** (before collapse) — Had robust sub-account functionality. Many traders favored it for its API flexibility.

**OKX** — Offers sub-accounts with advanced permission controls and separate trading pairs per sub-account.

Availability and features vary; traders should verify current offerings at their preferred exchange.

## Accounting and Tax Reporting

Sub-accounts complicate [tax reporting](/tax-bracket-investor/). Each sub-account generates independent trading history, realized gains, and losses. Regulatory frameworks in most countries treat all sub-accounts under the same taxpayer as a single consolidated portfolio, so the trader must aggregate sub-account activity for [Form 8949](/form-8949/) or local equivalents. Many crypto-tax software tools struggle with multi-sub-account reconciliation, requiring manual adjustment or exports from the exchange.

## See also

<div class="wiki-seealso">

### Closely related

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — The platform hosting sub-accounts
- [Custody](/custodian/) — The commingling risk inherent in sub-account architecture
- [Counterparty Risk](/counterparty-risk/) — The exchange failure risk sub-accounts do not mitigate
- [Blockchain Fundamentals](/blockchain-fundamentals/) — Underlying ledger technology; sub-accounts are exchange-layer features
- [Derivatives Hedging](/derivatives-hedging/) — A common use case for sub-account segregation

### Wider context

- [Bitcoin](/bitcoin/) — Primary asset traded across exchange sub-accounts
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Broader platform economics and architecture
- [Futures Contract](/futures-contract/) — Common derivative traded in isolated sub-accounts
- [Form 8949](/form-8949/) — US tax reporting that must aggregate sub-account trades

</div>
