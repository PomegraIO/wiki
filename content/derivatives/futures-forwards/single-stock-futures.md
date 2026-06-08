---
title: "Single Stock Futures"
description: "Standardised futures contracts on individual equities, enabling leverage and short positions on company shares."
keywords:
  - single-stock futures
  - equity derivatives
  - leverage
  - short positions
  - equity hedging
image: "/svg/derivatives.svg"
---

*A **single stock future** is a [futures contract](/futures-contract/) whose underlying is a single company's [common stock](/common-stock/). Like [stock index futures](/stock-index-futures/), they trade on exchanges, require margin, and settle in cash. Yet because they track one equity rather than a basket, they carry different [basis](/cash-and-carry-arbitrage/), [volatility](/volatility-smile/), and [margin](/margin-call-forex/) characteristics than index contracts, and face more regulatory scrutiny in many jurisdictions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Single Stock Futures — key facts</div>

<img src="/svg/derivatives.svg" alt="A financial contract symbol representing derivatives and leverage." />

<div class="wiki-infobox-caption">Standardised leverage on individual company shares, distinct from options in settlement mechanics.</div>

|   |   |
|---|---|
| **What it is** | [Futures contract](/futures-contract/) on an individual [common stock](/common-stock/) |
| **Settlement** | Cash-settled; mark-to-market daily |
| **Contract size** | Usually 100 shares per contract |
| **Price quotation** | Per-share basis (e.g., $150 per share) |
| **Leverage** | Typically 5:1 to 10:1 initial margin |
| **Dividend treatment** | Adjusted at ex-dividend dates; no voting or ownership rights |
| **Expiry** | Usually quarterly or monthly |
| **Jurisdictions** | US, UK, Europe, Asia-Pacific; banned or restricted in some markets |

</aside>

## Why single-stock futures exist alongside options

Both [options](/option/) and [futures](/futures-contract/) on individual stocks offer leverage and directional exposure. But they differ fundamentally in structure. An [option](/option/) gives the *right* to buy or sell at a fixed [strike price](/strike-price/); a [future](/futures-contract/) is an *obligation* to exchange the stock at a set price. 

Futures require margin from both buyer and seller. Options place the burden on the seller (the writer). For a trader who is simply bullish on a stock and wants leverage without time decay ([theta](/theta/)), a long stock future is often cleaner than an out-of-the-money call. For a trader seeking defined risk and the option to walk away, an [option](/option/) is superior. Institutions often use both, depending on horizon and liquidity needs.

## Why margin differs from index futures

Holding a position in a single stock is riskier than holding a diversified index. A single company can gap 20–30% on earnings or a scandal; the [S&P 500 Index](/sp-500-index/) rarely moves that sharply in one day. As a result, single-stock futures typically demand higher [margin](/margin-call-forex/) (lower leverage) than [index futures](/stock-index-futures/).

Initial margin on an [index future](/stock-index-futures/) may be 5–8% of notional value; on a single stock, it might be 10–15%, depending on [volatility](/volatility-smile/). Maintenance margin—the minimum you must hold—is set by the exchange and is usually around 75% of initial margin. Fall below it, and you receive a margin call and must deposit cash or sell positions.

## The basis and dividend adjustments

Like all futures, a single-stock future has a [basis](/cash-and-carry-arbitrage/): the difference between the futures price and the spot stock price. In theory, the basis should equal the [cost of carry](/cash-and-carry-arbitrage/)—mainly the risk-free [interest rate](/interest-rate/) times the price, minus expected [dividends](/dividend/).

When a company pays a [dividend](/dividend/), the futures contract is adjusted downward by the dividend amount at the [ex-dividend](/dividend/) date. This makes economic sense: if you own the stock, you receive cash; if you own the future, you do not. The adjustment prevents arbitrage.

A [cash-and-carry arbitrage](/cash-and-carry-arbitrage/) strategy—buy the stock, sell the future—is profitable when the future is overpriced relative to the stock plus carry costs. But transaction costs (bid-ask spreads, borrow rates for [short selling](/short-selling/) the stock) often eliminate the edge for all but the largest traders.

## Liquidity: the critical constraint

Single-stock futures are far less liquid than [index futures](/stock-index-futures/) or [options](/option/). On the most-traded stocks (mega-cap tech, for instance), there may be depth; on smaller or less-favoured names, bid-ask [spreads](/bid-ask-spread/) are wide and volume is thin.

This illiquidity matters. A trader holding a large position in a single-stock future may struggle to close it without moving the price. For retail investors, this is a serious risk. Many brokers restrict leverage on single-stock futures to dampen blow-ups. Institutional portfolio managers prefer [options](/option/) or traditional [short selling](/short-selling/) of stocks for most hedging purposes.

## Hedging and speculative uses

A company insider expecting her equity grant to vest in three months but worried the stock will fall might short a [forward](/cash-and-carry-arbitrage/) (or futures) contract to lock in a price. This hedge is simpler and cheaper than an [option](/option/) (which has an [option premium](/option-premium/)), though it eliminates upside if the stock rallies.

A speculative trader betting a stock will outperform the [index](/stock-index-futures/) might buy the stock future and sell [index futures](/stock-index-futures/), a statistical arbitrage. The correlation between the stock and the index drives profitability.

## Regulatory context: why they're rare in some markets

Single-stock futures were banned in the United States from 1982 to 2001, partly due to concerns about market manipulation and conflicts with the options industry. When the ban lifted, adoption was slow. Most US brokers do not actively promote them. In some countries, single-stock futures remain heavily restricted.

The UK, Europe, and Asia have more active single-stock futures markets, partly because equities options developed differently and partly due to institutional demand. Nevertheless, even in liquid markets, options remain far more actively traded than futures for individual stocks.

## Settlement and delivery myths

Single-stock futures are cash-settled, not physically settled. You do not receive 100 shares; instead, your account is credited or debited the difference between the contract price and the spot price. This removes delivery risk but also means you cannot use a long futures position to actually own the stock—you must buy the stock in the [cash market](/primary-market/) separately.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the mechanics and economics of standardised forward contracts
- [Stock Index Futures](/stock-index-futures/) — futures on diversified indices; higher leverage, lower idiosyncratic risk
- [Option](/option/) — the alternative leveraged instrument on individual equities
- [Common Stock](/common-stock/) — the underlying equity being contracted
- [Cash-and-Carry Arbitrage](/cash-and-carry-arbitrage/) — exploiting spot-futures mispricing
- [Short Selling](/short-selling/) — the mechanism for bearish exposure without derivatives
- [Dividend](/dividend/) — the cash distribution adjusted in futures pricing

### Wider context

- [Margin Call (Forex)](/margin-call-forex/) — how margin requirements are enforced across derivatives
- [Leverage (Forex)](/leverage-ratio-forex/) — the amplification of returns and risks via borrowed capital
- [Volatility Smile](/volatility-smile/) — how implied volatility varies with strike; relevant to option vs. futures choice
- [Price Discovery](/price-discovery/) — how derivative markets contribute to information in spot markets
- [Stock Exchange](/stock-exchange/) — the venue where underlying equities trade

</div>
