---
title: "How Indexes Handle Dual-Class and Multi-Class Share Structures"
description: "How index providers weight dual class shares, voting vs economic rights, and whether multi-class companies are included or excluded."
keywords:
  - dual class shares index inclusion rules
  - multi-class share structures index treatment
  - share class voting rights weighting
  - index provider policies classification
image: "/svg/institutions.svg"
---

*Dual-class and multi-class share structures create a tension for major stock indexes: companies with unequal voting rights violate the principle of one-share-one-vote, yet excluding them wholesale removes large chunks of market value.* Index providers—[S&P Dow Jones](/sp-500-index/), MSCI, and others—have evolved their policies over two decades from outright exclusion to nuanced weighting rules that account for voting control while still including the economic interest. Understanding how these rules work explains why some founders retain superpowers while shareholders accept diluted governance.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dual & Multi-Class Shares — index treatment</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions." />

<div class="wiki-infobox-caption">Index rules now accommodate founder control via voting-power adjustments.</div>

|   |   |
|---|---|
| **Definition** | Companies with two or more share classes having different voting rights |
| **Common structure** | Class A (10 votes per share), Class B (1 vote per share) |
| **Inclusion approach (modern)** | Included, but with voting-weight or float adjustments |
| **Weighting method** | Economic weight vs voting weight; often capped at float |
| **Exclusion scenarios** | Extreme imbalances; some non-voting shares |
| **Index change impact** | Rebalancing when company changes class structure |
| **Examples** | Google, Facebook, Berkshire Hathaway (multi-class) |

</aside>

## The Core Tension

A stock index's fundamental purpose is to represent the investable market. If index providers excluded all multi-class companies, they would eliminate Google, Facebook, Berkshire Hathaway, and dozens of other large-cap holdings—distorting the market picture significantly.

Yet a pure voting-weight approach creates a different problem: a founder with 51% of votes might own only 5% of economic value. Weighting the company solely on voting power would understate the economic interest of public shareholders and overstate the control value of the founder's stake.

Index providers have settled on a middle ground: **multi-class companies are included, but their weighting is adjusted to reflect a blend of voting control and economic ownership.** The adjustment varies by provider and has tightened over time as proxy advisory firms and institutional investors demanded stronger governance standards.

## S&P Dow Jones and the Voting Rule

S&P Dow Jones Indices (which manages the S&P 500, S&P 1500, and others) adopted formal voting-rule policies that exclude or restrict shares with extremely unequal voting rights.

Under S&P's rules, companies with more than one share class are generally _included_ if:

1. The company is otherwise eligible (liquidity, market cap, domicile).
2. The voting differential is not so extreme as to constitute non-voting shares.

Companies with non-voting shares or shares with zero votes are typically _excluded_. This filters out structures like some European companies' preference shares or Chinese Class H shares with no voting power.

For multi-class structures that _are_ included, S&P generally weights the company by its **float-adjusted market cap**—the total economic value of all share classes multiplied by their public ownership percentage. This approach treats voting rights as a governance issue, not a weighting metric, and keeps the index's economic exposure true to actual market capitalization.

However, S&P reviews each multi-class company case-by-case. If voting concentration is judged to undermine minority shareholder protection, the company may be removed from the index or face float adjustments.

## MSCI's Governance-Inclusive Approach

MSCI, which constructs indexes used by many active and passive managers, has adopted a more explicit governance lens.

MSCI includes multi-class companies but applies **quality and governance screens** that can reduce their weighting or trigger removal if voting imbalances conflict with its governance standards. For companies in its MSCI All Country World Index (ACWI) and MSCI USA Index, MSCI assesses:

- **Voting-to-economic spread:** How divergent are voting and ownership rights?
- **Sunset provisions:** Is there a date when multiple classes will merge?
- **Board independence:** Can minorities challenge founder-aligned directors?

Companies with extreme voting gaps and weak minority protections may be excluded outright. Those with moderate imbalances but decent governance frameworks (e.g., regular director elections, shareholder veto rights) are included, typically at float-adjusted weight.

MSCI also periodically reviews whether share class structures are _durable_. If a company's dual-class structure has an announced sunset, MSCI may factor that into whether to retain the company during the wind-down period.

## Float Adjustment and Voting Caps

The most common weighting tool for multi-class companies is **float adjustment**—excluding shares held by controlling shareholders (or shares with supernormal voting rights) from the weight calculation.

**Example:**

- **Company ABC:** 100M shares Class A (1 vote each), 100M shares Class B (10 votes each), both trading publicly.
- **Founder owns:** 60M Class B shares.
- **Public float:** 40M Class A + 100M Class B = 140M economic shares.
- **Voting power:** Founder controls 60M / (100M + 100M) = 30% of votes; public controls 70%.

An index using strict voting weight would allocate ABC's index membership to the founder's stake. Instead, a float-adjusted approach counts only the 140M publicly held shares and the economic value they represent, removing the voting lever from the calculation.

Float adjustments mean that founders with supernormal voting rights are _included_ in the index but do not receive extra weight simply because of voting concentration. The index remains neutral on governance structure and focuses on economic exposure.

Some indexes apply a **voting cap**—limiting any single share class to a maximum percentage of the company's index weight. For instance, a 3–5% voting cap would prevent any one share class from dominating a multi-class company's representation.

## Inclusion Thresholds and Evolution

In the 1990s and early 2000s, many index providers excluded multi-class companies outright. Dual-class structures were seen as governance red flags.

Over time—especially as tech founders and activist investors reshaped capital markets—indexes relaxed their stance. The rise of venture capital and founder-led growth companies normalized multi-class structures. Index providers realized that excluding them meant passive funds could not replicate market returns and active funds faced idiosyncratic tracking error.

**Modern consensus:** Multi-class companies are included, but with governance-sensitive adjustments. The thresholds vary:

- **S&P 500:** Includes most multi-class structures; adjusts for non-voting shares.
- **MSCI:** Includes multi-class structures if governance quality is adequate; excludes extreme cases.
- **Nasdaq-100:** Includes multi-class companies; uses float-adjusted weighting.
- **Russell Indexes:** Includes multi-class companies; adjusts for free float.

## When Companies Change Class Structure

A significant event for index providers is when a company **converts from single-class to multi-class** or vice versa.

If a founder issues a new superclass of shares as a dividend or spinoff (effectively consolidating voting power), the index provider reassesses the company's inclusion and weighting.

**Upside conversions** (moving to multi-class with founder control) may trigger:

- A review of governance policies and possible removal if the new structure breaches thresholds.
- A reweighting to reflect the new float after founder shares are isolated.
- Index constituent changes and reconstitution activity as the company adjusts.

**Sunset conversions** (collapsing dual-class back to single-class, as Google and Facebook have not done but some European companies have) can reverse earlier float adjustments and bring the company back to pure market-cap weighting.

## International Variations

Dual-class structures are more prevalent and accepted in Asia (Toyota, Samsung, Chinese companies with different voting classes for mainland and Hong Kong holders) and Europe (Volvo, Publicis) than in the United States. Index providers adjust their policies to local norms.

- **China:** A/H shares and red chips have forced index providers to develop custom voting rules.
- **Nordic countries:** Dual-class structures are common and historically accepted; indexes weight by economic value, not votes.
- **UK/US:** Greater hostility to voting imbalances; stronger governance screens.

MSCI, in particular, maintains different governance thresholds for developed markets versus emerging markets, reflecting varying shareholder protections and institutional norms.

## The Practical Impact on Investors

For a passive investor tracking an index, multi-class handling has limited day-to-day impact. Index funds rebalance to the index's weighting, which already reflects governance adjustments.

For active managers, multi-class companies present both an opportunity and a constraint. If an active fund believes founder-led governance is superior, it can overweight. If it believes voting imbalances create conflict risk, it can underweight or avoid the stock entirely. Index rules do not prevent these choices; they only establish how passive trackers represent the market.

For founders and boards, index inclusion—at any weight—matters enormously for liquidity and cost of capital. A company excluded from the S&P 500 or MSCI World faces reduced passive buying interest and tracking-error pressure from active funds. Understanding how index providers treat multi-class structures has become a central governance consideration for any company contemplating a dual-class recapitalization.

## See also

<div class="wiki-seealso">

### Closely related

- [Voting Rights](/voting-rights/) — the legal foundation of share class structure
- [Index Provider](/index-provider/) — how indexes are constructed and governed
- [Market Capitalization](/market-capitalization/) — the primary weighting metric that voting rules adjust
- [Index Fund](/index-fund/) — how passive funds track indexes with multi-class adjustments
- [Float-Adjusted Weighting](/market-capitalization/) — the technical adjustment tool for multi-class inclusion

### Wider context

- [Stock Exchange](/stock-exchange/) — listings governed by similar class-structure rules
- [Proxy Statement](/proxy-statement/) — where voting structures are disclosed
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulatory oversight of share class registration

</div>
