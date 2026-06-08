---
title: "Float-Adjusted Market Cap in Index Construction"
description: "Why index providers exclude locked-in shares and government stakes when weighting stocks."
keywords:
  - float adjusted market cap index
  - free float market capitalization
  - float adjustment weighting
  - index construction methodology
image: /svg/institutions.svg
---

*Most major stock indexes do not weight companies by their total market capitalization. Instead, they use **float-adjusted market cap**, which excludes shares that are locked up—held by founders, governments, or long-term insiders—and therefore unavailable for public trading. This adjustment ensures that index weights reflect the portion of each company that traders can actually buy and sell.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Float-Adjusted Market Cap — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Index weights are based on the freely tradeable portion of each company, not total outstanding shares.</div>

|   |   |
|---|---|
| **Definition** | Market capitalization calculated using only shares available for public purchase, excluding restricted or closely held stock. |
| **Synonym** | Free-float market cap |
| **Shares excluded** | Founder and insider holdings, government ownership, employee restricted stock, long-term cross-holdings. |
| **Index adoption** | S&P 500, MSCI indexes, FTSE, most modern indexes use float adjustment. |
| **Impact vs. full market cap** | Index weight can differ materially for government-owned or founder-controlled companies. |
| **Calculation** | (Stock price) × (Shares outstanding) × (Float adjustment factor) |

</aside>

## The problem with full market cap weighting

Imagine an index that weights companies by total market capitalization: price per share times all shares outstanding. That works fine for a widely held, public company. But it breaks down for enterprises where a controlling block is locked away.

Consider a country's sovereign wealth fund that owns 60% of a major national oil company. In a pure market-cap index, that stock's weight would be based on all its outstanding shares. But the fund is not selling its stake—it is a strategic, permanent holding. The 40% of shares that trade freely on the exchange determine the stock's actual market value and [liquidity](/wiki/liquidity-risk/), not the locked-up majority.

If an index held a stock at its full market-cap weight, a portfolio tracking that index could not replicate the index exactly. The index fund would need to buy more shares than are actually available for purchase. The problem is not academic: it is real for emerging-market stocks, state-owned enterprises, and closely held founders' companies.

Float adjustment solves this by reweighting based on tradeable shares only.

## How float adjustment is calculated

Index providers determine a **float adjustment factor**—the percentage of shares deemed freely available for trading.

A stock with 100 million shares outstanding might have:
- 40 million held by the founder and family (restricted)
- 15 million held by the government (strategic)
- 45 million trading on the public exchange

The float-adjusted factor is 45 / 100 = 0.45. If the stock trades at $50, its full market cap is $5 billion, but its float-adjusted market cap for indexing purposes is $5 billion × 0.45 = $2.25 billion.

Index providers typically define float thresholds by category:
- **Founder/insider holdings** are excluded entirely if locked by contract or regulatory restriction.
- **Government ownership** is usually excluded in full, since governments rarely sell.
- **Cross-holdings** (Company A owns shares of Company B, which are not for sale) are excluded.
- **Employee stock options** and vesting stock are counted as float only when exercisable or when vesting dates are near.
- **Secondary and preferential shares** may be excluded or adjusted if they carry different voting or liquidity rights.

## Which indexes use float adjustment

Nearly all modern large-cap indexes use float adjustment:

**S&P 500** has used float-adjusted weighting since 2005. Before that, it was a pure market-cap index, but the shift was made to improve [index fund](/wiki/index-fund/) replicability.

**MSCI Indexes** globally (MSCI World, MSCI Emerging Markets, etc.) use float adjustment as standard practice.

**FTSE Indexes** (U.K.) incorporate float adjustment to account for government and cross-holdings in multinational companies.

**Nikkei 225** in Japan uses float-adjusted weighting, critical given the prevalence of cross-shareholdings among Japanese corporations.

A few legacy or specialized indexes still use full market cap—but they are exceptions. Float adjustment is now industry standard.

## Float adjustment and emerging markets

Float adjustment matters most in emerging markets, where government ownership and founder control are common. A large-cap index in a developing economy might have 10–20% of its weight adjusted downward because of locked holdings.

This creates practical effects. When a [index fund](/wiki/index-fund/) tracking an emerging-market index tries to buy constituents, it finds that the available supply of shares is much smaller than a full market-cap weighting would suggest. The fund may face wider [bid-ask spread](/wiki/bid-ask-spread/) or move the price against itself more easily.

Conversely, when a government privatizes a company and releases previously restricted shares into the float, the index automatically increases that stock's weight. No manual rebalancing is needed; the float adjustment factor rises mechanically.

## Float adjustment vs. price discovery

Float adjustment is not the same as liquidity. A stock can have a low float but very high daily trading volume (like early-stage companies with few free shares but heavy trading). Conversely, a stock with high float but thin trading spreads will be listed at a higher weight but may be harder to buy in size.

[Index providers](/wiki/index-provider-revenue-model/) do account for this distinction when monitoring indexes. Some indexes add a second screen: minimum liquidity requirements or minimum trading volume, independent of float. A company might have a high float but be de-listed from an index if it fails a liquidity test.

## The impact on index funds and trackers

Float-adjusted weighting makes indexes far easier to replicate. A fund tracking an index can actually buy the constituent shares without running out of supply. Index [expense ratio](/wiki/expense-ratio/) are lower as a result because the logistics of tracking are simpler.

For investors, this is nearly invisible—the benefit appears as slightly lower fees and tighter [tracking error](/wiki/etf/). But it is meaningful. Early indexes that used pure market-cap weighting sometimes had drift between index performance and fund performance, especially for large moves in stocks with high restricted holdings.

## Float adjustment and activist investors

Float adjustment creates an interesting dynamic for activist investors and [proxy fight](/wiki/proxy-fight/) campaigns. An activist fund knows that even if it builds a large position in a company, its voting power might be disproportionate relative to its ownership. If 50% of the company is locked away in founder shares with separate voting rights, the activist's 10% stake is actually 20% of the float—but only 10% of votes.

Index providers must balance this: they use float for index weight calculations, but voting rights are separate. A founder with 50% locked shares still controls 50% of votes, regardless of float adjustment.

## Criticism and edge cases

Float adjustment is not without critics. Some argue that it is ad hoc: index providers must make judgment calls about what is "restricted" and for how long. A founder planning to gradually release shares might have them counted as restricted today and float over a multi-year horizon. Different index providers can reach different conclusions.

Also, float adjustment can be gamed. If a company orchestrates a secondary offering specifically to increase its float and boost its index weight, it gains prominence even if no fundamental change has occurred. Index rules require that float adjustments reflect real economic constraints, not corporate engineering—but enforcement is subjective.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Capitalization](/wiki/market-capitalization/) — the core metric underlying float adjustment
- [Index Reconstitution Frequency](/wiki/index-reconstitution-frequency/) — how often float-adjusted weights are reviewed
- [Index Fund](/wiki/index-fund/) — funds that track float-adjusted indexes
- [Index Exclusion Criteria](/wiki/index-exclusion-criteria/) — related screening rules for index membership
- [Bid-Ask Spread](/wiki/bid-ask-spread/) — liquidity costs that float adjustment helps minimize
- [Expense Ratio](/wiki/expense-ratio/) — lower fees enabled by easier index replication

### Wider context

- [S&P 500 Index](/wiki/sp-500-index/) — a major index using float adjustment
- [ETF](/wiki/etf/) — funds built on float-adjusted indexes
- [Price Discovery](/wiki/price-discovery/) — how the tradeable portion of a stock affects its market value
- [Proxy Fight](/wiki/proxy-fight/) — activist campaigns that are affected by voting vs. float distinctions

</div>
