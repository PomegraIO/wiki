---
title: "Free-Float Shares vs Total Shares in Index Construction"
description: "Why index providers weight companies by free-float shares rather than total shares, and how that changes index weights."
keywords:
  - free float vs total shares
  - free-float adjustment index
  - market capitalization calculation
  - index weighting
  - index provider methodology
  - publicly traded shares
---

*An **index using free-float shares vs total shares** will assign a different weight to companies with concentrated ownership. Free-float counts only shares available for public trading, excluding founder blocks and government stakes. This makes the index more liquid and fairer to typical investors, because they cannot actually buy the founder's shares.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Free-Float vs Total Shares — The weight difference</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions and markets." />

<div class="wiki-infobox-caption">The same company, two different index weights, depending on share count method.</div>

|   |   |
|---|---|
| **Total shares outstanding** | All shares, including founder block & restricted shares |
| **Free-float shares** | Only shares openly tradable in the market |
| **Market cap (total)** | Price × total shares |
| **Market cap (free-float)** | Price × free-float shares |
| **Index weight (total)** | Higher if founders hold large block |
| **Index weight (free-float)** | Lower, excluding locked-up shares |
| **Investor impact** | Free-float closer to replicable portfolio weight |

</aside>

## The Basic Distinction

**Total shares outstanding** is the absolute count of all shares a company has issued. This includes founder shares, board shares, restricted employee stock, government stakes, and every publicly tradable share. If a company has issued 1 billion shares total, that is the count.

**Free-float shares** is the subset of total shares that are actually available for public trading. If the founder owns 100 million of those shares and never plans to sell them, only 900 million shares are in the free float. If an employee holds 10 million shares as a long-term grant that vest gradually but are restricted by lock-up agreements, those shares may be excluded from the free float until the restriction expires.

An [index provider](/index-provider/) that builds an [index](/sp-500-index/) using total shares will assign the company a weight based on 1 billion shares times the stock price. An index provider using free-float methodology will use only 900 million shares, resulting in a lower weight for that stock in the index.

The difference affects how much of the index an investor must hold to replicate the benchmark. If you hold a cap-weighted index based on total shares, you are overweighting the company because you can only buy the 900 million free-float shares, yet the index assumes you hold the weighting of all 1 billion. You end up with a different portfolio than the index weight implies.

## Why Indexes Switched to Free-Float

Before the 2000s, most major stock indexes used total shares outstanding to calculate [market capitalization](/market-capitalization/). The S&P 500, NASDAQ, and many international benchmarks shifted to free-float weighting as markets globalized and as the limitations of total-share weighting became clear.

The core problem is replicability. An investor trying to track an index should be able to buy the exact basket of securities in the exact weights stated by the index. If the index assumes you own 100 million founder shares that are not for sale, you cannot actually replicate the index. You can only buy the free float, meaning your portfolio will deviate from the benchmark.

This matters for [index funds](/index-fund/) and [exchange-traded funds](/etf/). Managers of these funds must hold weights that mirror the index. If the index includes illiquid or non-tradable shares in its calculation, the fund either cannot replicate it perfectly or must use a tracking methodology (buying what it can) that deviates from the stated weights.

Free-float weighting solved this problem. By including only shares that can actually be bought, the index construction reflects reality: the shares available to investors.

## How Free-Float Changes Index Weights

Consider two examples at the same price but with different ownership structures.

**Company A:**
- Total shares: 1 billion
- Free-float shares: 900 million (founder owns 100 million)
- Stock price: $100
- Market cap (total): $100 billion
- Market cap (free-float): $90 billion

**Company B:**
- Total shares: 1 billion
- Free-float shares: 1 billion (no founder block)
- Stock price: $100
- Market cap (total): $100 billion
- Market cap (free-float): $100 billion

In a total-shares index, both companies have identical weight (same market cap). In a free-float index, Company B is weighted 11% higher because only 900 million shares of Company A are tradable. If the index has $1 trillion in assets, Company A's weight falls by $10 billion (the difference between $100B and $90B weight).

For index fund managers, this is crucial. If they must replicate a free-float index, they can buy all 1 billion shares of Company B, but only 900 million shares of Company A (the public float). The free-float methodology ensures their actual holdings match the index's weights.

## Government and Restricted Shares

Free-float exclusions are not limited to founder blocks. Many countries have government-owned stakes in companies (especially in Europe and Asia). A [central bank](/central-bank/) might hold shares, or the state might own a strategic stake in a utility or telecommunications company. These government shares are typically restricted from public trading (or can only be traded through special mechanisms) and are excluded from the free float.

Similarly, restricted shares granted to employees or executives under [equity compensation](/equity-financing/) plans may be held in trust or subject to lock-up agreements. Until these restrictions expire and shares are released to the market, they are not part of the free float.

[Index providers](/index-provider/) have detailed rules about what counts as restricted and when shares enter the free float. A typical threshold is that shares must be *unrestricted and available for public purchase* without legal or contractual limitations. Shares that vest gradually but are not yet released do not count. Shares sold under a lock-up agreement (common in IPOs) do not count until the lock-up expires.

## Index Adjustment Mechanics

When an [index](/sp-500-index/) uses free-float methodology, the calculation looks like this:

1. **Determine total shares** outstanding for the company (from SEC filings in the U.S.)
2. **Identify restricted shares**: founder stakes, government holdings, employee grants under lock-up, treasury shares
3. **Calculate free-float shares**: total shares minus restricted shares
4. **Apply free-float factor**: often expressed as a percentage (e.g., 85% float factor means only 85% of shares count)
5. **Calculate index weight**: (stock price × free-float shares) / total index market cap

This calculation happens quarterly or semi-annually as holdings change. If a founder sells shares or restrictions expire, the free-float increases, and the company's index weight rises. If a company buys back shares, the float may shrink, lowering the weight.

## Implications for Portfolio Tracking

For [passive investors](/index-fund/), free-float weighting is a quiet advantage. Their portfolios align better with the index because the weights reflect actual tradable supply. For [active traders](/momentum-investing/) trying to beat the index, free-float changes create a consideration: when restricted shares are about to expire, a company's index weight may shift, requiring flows of index-tracking capital.

Free-float also affects the [liquidity](/liquidity-risk/) of stocks in the index. A company with a large founder block and small free float will have less trading activity relative to its total market cap. An index portfolio holding that stock will have higher market impact when rebalancing, because fewer shares are available to trade.

## Global Variations

Most developed markets have converged on free-float weighting. The [S&P 500](/sp-500-index/), NASDAQ-100, MSCI indexes, and FTSE all use some form of free-float adjustment. However, the precise definition varies. Some indexes include a gradual ramp-up for newly released shares (a "float factor" that rises over time), while others snap shares in or out when restrictions expire.

Emerging markets and less liquid exchanges sometimes use total-shares weighting, either because the infrastructure for tracking free-float is less developed or because governments want their stakes counted fully in the index (a political motivation).

## See also

<div class="wiki-seealso">

### Closely related

- [Index provider](/index-provider/) — The firms that set weighting methodologies
- [Market capitalization](/market-capitalization/) — The numerator in index weight calculations
- [Index fund](/index-fund/) — Passive vehicles that must track free-float indexes precisely
- [Share buyback](/share-buyback/) — How companies reduce free-float shares
- [Authorized-participant](/authorized-participant/) — Entities that create/destroy index fund shares

### Wider context

- [S&P 500 Index](/sp-500-index/) — The benchmark that pioneered free-float weighting
- [Exchange-traded fund](/etf/) — Index-tracking vehicles affected by free-float methodology
- [Equity financing](/equity-financing/) — How restricted shares are issued
- [Liquidity risk](/liquidity-risk/) — How free-float size affects tradability
- [Stock exchange](/stock-exchange/) — Where free-float shares trade

</div>
