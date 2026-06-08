---
title: "Float Adjustment After Corporate Actions"
description: "How index providers recalculate float-adjusted weights after mergers, acquisitions, and secondary offerings to maintain index integrity."
keywords:
  - float adjustment
  - float adjustment after merger
  - index reconstitution
  - corporate actions index
  - float-adjusted index
  - index weight adjustment
---

*An **index float adjustment after mergers, acquisitions, or secondary offerings** is the recalculation an [index provider](/index-provider/) performs to update a stock's weight between scheduled rebalances. When a company's freely tradable share count changes, the index provider adjusts that constituent's float-adjusted representation to keep the index's construction rules intact.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Float Adjustment After Corporate Actions — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutional finance." />

<div class="wiki-infobox-caption">Index rules adapt to changes in tradable shares without waiting for the next quarterly rebalance.</div>

|   |   |
|---|---|
| **Trigger events** | Merger, acquisition, secondary offering, share buyback, founder lock-up expiry |
| **What changes** | Shares outstanding classified as "float" (freely tradable) |
| **Timing** | Usually effective 1–5 business days after corporate action closes |
| **Weight recalc** | New float = old float ± change; weight = (price × new float) / index divisor |
| **Index divisor** | Adjusted to prevent spurious index level jumps |
| **Rebalance schedule** | Interim adjustments bridge to next quarterly/annual rebalance |

</aside>

## Why float-adjusted weights change after M&A

When two companies merge, or when a company issues new shares via a secondary offering, the **freely tradable share count** of the surviving or issuing company changes overnight. An index built on [float-adjusted market capitalization](/market-capitalization/) must reflect that reality, or the index will misrepresent the true tradable weight of that stock.

Consider a merger: Company A buys Company B. Company A was in the index; Company B was not. The merged entity keeps Company A's ticker. On day one of the merger, Company A's outstanding shares jump because it issued new shares to pay for Company B. The index provider must immediately calculate how many of those new shares are actually tradable (not locked up, not held by insiders who cannot sell without restriction) and adjust Company A's weight in the index accordingly.

Similarly, in a secondary offering, a company issues new shares publicly. The company's share count jumps, but only some fraction may be newly tradable (the rest might be subject to lock-up periods). The index provider quantifies the freely tradable increment and adjusts the index weight.

Without this interim float adjustment, the index would carry an inaccurate representation of the company's true market weight until the next scheduled rebalance. For a large-cap company or a significant index constituent, that inaccuracy could distort the index return and confuse [index funds](/index-fund/) trying to track it.

## The mechanics of float recalculation

The [index provider](/index-provider/) follows a formal procedure:

1. **Identify the float change**: The corporate action results in a new number of shares outstanding and a new float count. For a merger, the surviving company's shares outstanding increase. For a secondary offering, the issuer's shares outstanding increase. For a buyback, they decrease. For founder lock-up expiry, the tradable float expands.

2. **Classify shares as float or restricted**: Not all new shares are immediately freely tradable. Shares held by founders (subject to lock-up), shares held by large anchor investors under trading restrictions, or shares held by the acquiring company (if the deal is not yet fully integrated) may count as restricted. The index provider studies the deal terms and SEC filings to determine what portion of the new share count qualifies as float.

3. **Calculate the new market cap component**: The index uses float-adjusted market cap, calculated as:
   ```
   Float-adjusted market cap = share price × float shares outstanding
   ```
   With the new float count, this component changes, even if the share price has not moved.

4. **Recalculate the constituent weight**: The constituent's weight in the index is:
   ```
   Weight = constituent float-adjusted market cap / sum of all constituent float-adjusted market caps
   ```
   If the index's total market cap has not changed, a constituent's float increase will lower its weight (dilution). If the merger adds a large company to the index, total market cap may jump, affecting all relative weights.

5. **Adjust the index divisor**: To prevent the index level itself from jumping spuriously (which would confuse index funds and create false rebalancing), the index provider adjusts the divisor so that the index level remains continuous across the corporate action. The divisor is recalculated to preserve the index level at the close of the prior day, with the new constituent weights baked in.

## When buybacks reduce float

A share **buyback** works in reverse. When a company repurchases and retires shares, the total shares outstanding and the float both shrink. The index provider detects this and recalculates the company's float-adjusted market cap using the lower float count.

If the company's buyback is massive (reducing shares by 10% or more), the company's weight in the index will shrink even if its share price rises. This happens because the float-adjusted market cap calculation is the product of price and shares; fewer shares means smaller market cap, regardless of per-share gains.

From the index provider's perspective, buybacks are simpler than mergers because there is no ambiguity about which shares are tradable—they are just gone. The float count is definitive.

## Handling lock-up expirations and restricted stock releases

Some corporate actions are less binary. When a founder's lock-up period **expires**, previously restricted shares become freely tradable. The float suddenly increases, even though the company's total shares outstanding and share price may not change.

The index provider monitors lock-up expiration dates and updates the float count on the expiration date. Similarly, when restricted stock grants vest and become tradable, the float expands.

These events often catch traders off-guard because the share price may not react until after the float adjustment hits the index. If a large company's float expands by 10% due to lock-up expiry, index funds holding the stock will need to rebalance, and the market can see selling pressure.

## Timing and effective dates

Corporate actions usually have a **record date**, a **closing date**, and an **effective date** in the relevant index. The index provider typically adjusts float counts **1 to 5 business days after the closing date**, once the merger agreement or secondary offering is finalized and share counts are official.

Large index providers publish exact effective dates in advance, signaling to the market when the float adjustment will be reflected in the index. [Authorized participants](/authorized-participant/) (who create and redeem [ETF](/etf/) shares) rely on these dates to arbitrage the index and the fund.

## Impact on index funds and ETFs

For [index funds](/index-fund/) and [ETFs](/etf/) tracking the index, a float adjustment creates a mechanical rebalancing moment. The fund must adjust its holding of the affected company to match the new index weight. If a company's weight shrinks due to float expansion (dilution), the fund will sell some shares. If the company's weight grows, the fund will buy.

This can be a source of [execution risk](/execution-risk/): if the fund needs to sell after a large float expansion, the market may be flooded with selling at that moment, and the fund may face slippage.

## The role of index rules documentation

Each index has published construction rules that specify how float adjustments are handled. Some indices adjust float quasi-continuously, whenever material changes occur; others batch adjustments until the next rebalance. Reading the index methodology is essential for understanding when and how a float adjustment will occur.

Index providers also publish **Corporate Actions Guides**, which walk through exactly how mergers, secondaries, buybacks, and other events are treated. These guides are publicly available and are the authoritative source for how an index will respond to a given corporate action.

## See also

<div class="wiki-seealso">

### Closely related

- [Market Capitalization](/market-capitalization/) — Understanding float-adjusted market cap as the foundation of index weighting
- [Index Fund](/index-fund/) — How funds track indices through corporate actions
- [Merger](/merger/) — The corporate action that most often triggers large float shifts

### Wider context

- [Index Provider](/index-provider/) — The institutions that maintain index methodology
- Rebalancing — Scheduled periodic adjustments and how interim adjustments fit in
- [Authorized Participant](/authorized-participant/) — Market makers who arbitrage index-fund mismatches

</div>
