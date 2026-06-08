---
title: "Free-Float Adjustment"
description: "Adjusting index weights to exclude non-tradeable shares held by insiders and governments, reflecting only freely available stock."
keywords:
  - free float
  - index adjustment
  - tradeable shares
  - ownership structure
  - institutional index
image: "/svg/markets.svg"
---

*A **free-float adjustment** modifies an index's weighting by excluding shares that are locked up in insider hands, held by related parties, or controlled by government. Only freely tradeable shares — the float — count toward determining each stock's weight. This reflects the actual investable supply and prevents disproportionate index exposure to tightly held firms.*

<div class="wiki-hatnote">

For the mechanics of adjusting all index weights to reflect a stock's free float, see [index rebalancing](/index-rebalancing/).

</div>

## Why raw capitalisation misleads

A naive [market capitalisation](/market-capitalization/) approach multiplies share price by total shares outstanding. But not all shares are equal. In many countries — particularly in Asia, the Middle East, and Latin America — substantial equity stakes are locked in the hands of founders, families, or state bodies. These holders have no intention to sell; their shares are effectively off the market.

Consider a hypothetical company with 1 billion shares trading at $10, yielding a $10 billion market cap. If a founding family owns 700 million shares and never sells, the truly tradeable float is only 300 million shares. A naive market-cap-weighted index would treat it as a $10 billion company; an accurate index should treat it as controlling only $3 billion of investable capital. The difference is not academic: it means investors are overexposed to a firm whose supply shock (if the family ever exited) could be devastating.

## Defining "free float"

Free float is the percentage of shares that are freely tradeable. It excludes:

- **Strategic insider holdings:** founder and director stakes acquired before the [initial public offering](/initial-public-offering/)
- **Related-party cross-holdings:** shares held by subsidiaries, family trusts, or other entities under common control
- **Government blocks:** central bank or ministry equity stakes (common in privatised utilities)
- **Employee restricted stock units (RSUs) and options** not yet vested (in some methodologies)
- **Lock-up agreements:** temporarily restricted shares held by pre-IPO investors or underwriters

Free float percentages are typically disclosed in prospectuses and earnings reports. Index providers like FTSE, MSCI, and S&P calculate them using regulatory filings, management disclosures, and direct inquiries to company investor relations teams.

## The impact on index composition

Free-float adjustment shrinks the weight of tightly controlled firms and expands the weight of widely held ones. In the MSCI EM (Emerging Markets) index, free-float adjustment can reduce a single company's weight by 30–60% if its founder or government ownership is substantial.

The practical effect is felt in emerging-market indices and sector-specific indices. A telecommunications monopoly in a developing nation — the classic case — might dominate by raw cap but represents little opportunity for foreign investors, because the bulk of equity is state-owned. Free-float adjustment rebalances the index to represent what investors can actually buy.

## The mechanics of adjustment

The simplest approach is multiplicative. If a stock has a 60% free float, its index weight is calculated as:

**Adjusted weight = (share price × total shares outstanding × free-float %) / total index market value**

Many indices go further, capping the adjustment at a maximum free float (say, 100%) to avoid quirks, and rounding to avoid tiny fractional weights that create trading friction.

The result is that if you own the index and it is free-float adjusted, your portfolio composition more closely tracks what the index provider intends: a basket of stocks weighted by their investable supply, not their theoretical capitalisation.

## Controversy and revisions

Free-float methodology is not static. Index providers periodically review and tighten definitions. A stock's free-float classification can shift if a founder increases holdings (reducing it) or if a government stake is privatised (increasing it). These adjustments trigger [index reconstitution](/index-reconstitution/) events and can move the market if a large shift occurs.

There is also debate over what counts. Some argue that a 5% holding by a related entity should be considered free (since it is still tradeable), while others count any known affiliation as restricted. Different index providers use different thresholds, so the MSCI, FTSE, and Russell indices can classify the same stock differently.

## Impact on performance and liquidity

Free-float adjustment typically favors developed markets (where ownership is more dispersed) over emerging markets (where concentrated ownership is endemic). It also underweights family-controlled and state-linked businesses, which can tilt an emerging-market index away from companies with economic moats but concentrated control.

For traders and institutional investors, the adjustment also serves as a proxy for [liquidity](/liquidity-risk/). A stock with 20% free float is harder to buy and sell in size than one with 100% free float, all else equal. By weighting by free float, the index mechanically allocates more weight to more-liquid names.

Conversely, the adjustment can introduce distortions. If a family stakes a controlling interest but the market price surges, the company's free-float weight falls while its price rises — a mismatch that creates [arbitrage](/market-maker-trading/) opportunities for sophisticated traders who can exploit the lag between market moves and index rebalancing.

## See also

<div class="wiki-seealso">

### Closely related

- [Index rebalancing](/index-rebalancing/) — periodic reset of constituent weights in an index
- [Market capitalization](/market-capitalization/) — total value of a firm, the traditional index weighting metric
- [Index reconstitution](/index-reconstitution/) — addition and deletion of stocks from an index
- [Liquidity risk](/liquidity-risk/) — risk that an asset cannot be bought or sold in sufficient volume without moving price
- [Initial public offering](/initial-public-offering/) — first time shares of a company are sold to the public
- [Fundamental index](/fundamental-index/) — alternative weighting by accounting metrics rather than price

### Wider context

- [Stock exchange](/stock-exchange/) — marketplace where equities trade
- [Emerging markets](/factor-investing/) — countries with developing capital markets and often concentrated ownership
- [Index fund](/index-fund/) — passive fund tracking a market benchmark

</div>
