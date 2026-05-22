---
title: "Liquidation Preference"
description: "The order in which security holders are paid in bankruptcy, restructuring, or acquisition; determines how proceeds are distributed."
keywords:
  - liquidation preference
  - preference stack
  - waterfall
  - seniority
  - bankruptcy
---

*A **liquidation preference** sets the order in which different classes of security holders (preferred stock, common stock, debt) receive proceeds when a company is sold, acquired, or wound down. Preferred shareholders typically rank ahead of common shareholders, and creditors rank ahead of all equity holders. The preference waterfall is a critical lever in [venture capital](/wiki/venture-capital-fund/) and [leveraged buyout](/wiki/leveraged-buyout/) (LBO) deals.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Rank order** | Secured debt → unsecured debt → preferred equity → common equity |
| **Common variants** | Non-participating preferred, participating preferred, pari passu (equal rank) |
| **Typical VC structure** | Series A gets 1× preference; Series B gets 2× preference; Series C gets 3×+ |
| **Effect on returns** | Subordinate classes get residual only after senior classes are paid in full |
| **Founder risk** | Common shareholders (often founders) can be wiped out in low-value outcomes |
| **Deal impact** | Higher preference multiple = higher threshold for exit valuation to benefit common holders |
| **Reverse splits** | If cash is insufficient, preference holders may receive partial payment or nothing |

</aside>

## Understanding the liquidation waterfall

Imagine a startup acquired for $100 million. The balance sheet shows:
- $20 million in debt
- 1 million shares of Series B Preferred (1× liquidation preference)
- 5 million shares of common stock

The waterfall pays out in order:

1. **Creditors (debt holders)** receive $20 million
2. **Series B preferred** holders receive min($80 million, 1× × value of shares) = $40 million (assuming they funded half the company)
3. **Common shareholders** receive the remaining $40 million

If the company is instead acquired for $25 million:

1. **Creditors** receive $20 million
2. **Series B preferred** holders receive $5 million (the remainder), wiping out common shareholders
3. **Common shareholders** receive $0

This scenario is devastating for founders and employees holding common stock. They invested years of effort and sacrifice, but the [preference stack](/wiki/anti-dilution-provisions/) leaves them with nothing. This is why [anti-dilution](/wiki/anti-dilution-provisions/) provisions and [option pools](/wiki/employee-stock-options/) are so critical in VC financing.

## Preference multiples and cumulative effect

Venture-backed companies often raise multiple [funding rounds](/wiki/venture-capital-fund/). Each round carries its own preference multiple:

- **Series A**: 1× preference (if liquidation, Series A gets 1× the amount it invested before any downstream preferences)
- **Series B**: 2× preference (if liquidation, Series B gets 2× its investment amount before common holders see anything)
- **Series C**: 3× preference (or more)

The multiples stack. If Series A invested $5 million, Series B invested $10 million, and Series C invested $15 million, the preference stack in a $40 million exit is:

1. **Series C**: min(40, 15 × 3) = $40 million → gets $40 million, capped by total proceeds
2. **Series B**: gets $0 (all cash exhausted by Series C's preference)
3. **Series A**: gets $0
4. **Common**: gets $0

Series C has taken over the [upside](/wiki/upside/) while later-stage rounds bear the [downside](/wiki/downside/) risk. In a higher-value exit ($200 million), Series C gets $45 million (15 × 3), Series B gets $20 million (10 × 2), Series A gets $5 million (5 × 1), and common gets the remaining ~$130 million.

## Participating versus non-participating preferred

**Non-participating preferred** (the older default): Holders choose the better of (a) their preference multiple or (b) their pro-rata share of remaining proceeds.

Example: In a $40 million exit with Series A having invested $5 million:
- Preference: $5 × 1 = $5 million
- Pro-rata if treated as common: $5M / $20M × $40M = $10 million
- Series A takes the better option: $10 million

**Participating preferred** (common in later-stage VC): Holders get their preference *plus* their pro-rata share of remaining proceeds—a "double dip."

Same example:
- Series A gets $5 million preference, then pro-rata share of remaining $35 million = $5M + ($5M / $20M × $35M) = $5M + $8.75M = $13.75 million

Participating preferred is more favorable to later-stage investors and more dilutive to earlier holders and common shareholders. It is heavily negotiated in deal terms.

## Liquidation preference in acquisition deals

In mergers and acquisitions, the preference determines how [transaction proceeds](/wiki/business-combination-purchase/) are distributed. An investment banker values a company, but the preference controls who gets paid.

Founders and employees often focus on the headline price ("We're selling for $100 million!") but should scrutinize the preference stack. If the company has multiple rounds of participating preferred, the founder's equity stake could be worth far less than a pro-rata share of the headline price.

This tension is why [earnout provisions](/wiki/earnout-provision/) and [equity rollovers](/wiki/equity-swap/) are common in M&A: the acquirer offers cash (which goes to senior holders) and equity in the surviving entity (which aligns later-stage and common holders to the post-deal success).

## Preference in bankruptcy and restructuring

In [bankruptcy](/wiki/liquidation/), the [preference waterfall](/wiki/debt-seniority/) is enforced by law. [Senior debt](/wiki/senior-bond/) holders have [liens](/wiki/lien/) on assets and get paid first. [Unsecured creditors](/wiki/credit-risk/) (often employees owed wages) come next. [Preferred equity](/wiki/preferred-stock/) holders come next, and [common equity](/wiki/common-stock/) holders are last.

In practice, common shareholders almost always receive nothing in bankruptcy. Even preferred shareholders often receive only a fraction of their preference if assets are insufficient.

[Chapter 11 bankruptcy](/wiki/bankruptcy/) allows for restructuring without liquidation. A company with significant asset value but temporary cash flow problems can reorganize under bankruptcy court protection. The preference waterfall still applies: creditors must be treated at least as well as in an equivalent liquidation scenario (the "absolute priority rule").

## Anti-dilution provisions and preference clawback

The interaction between [anti-dilution provisions](/wiki/anti-dilution-provisions/) and liquidation preference is complex. If a down round (lower price per share) occurs, earlier investors often receive anti-dilution protection, increasing their preference multiple.

A Series A investor with a 1× preference in a Series B down round might receive an increased preference multiple (say, 1.5×) to offset the lower valuation. This "clawback" protects earlier investors but dilutes founders and common holders further, sometimes to the point of non-viability.

## Implications for founders and employees

For **founders**, a large preference stack can mean that even if the company is acquired for an impressive headline price, their common stock is worthless if the preferences exhaust the proceeds. This is why successful founders in later funding rounds often negotiate ["advisor shares"](/wiki/option-pool/) or [common stock equivalence](/wiki/vesting-schedule/) clauses to preserve upside.

For **employees**, [stock options](/wiki/employee-stock-options/) vest into common stock. If the option strike price is set at the current valuation (as it should be), an exit well below subsequent funding round valuations can leave the options underwater. An employee granted options at a $10 million valuation sees those options worthless if the eventual exit is $30 million and the preference stack consumes all proceeds.

This is why [option pools](/wiki/esop/) of 10–20% of the company are negotiated, and why late-stage startups grant [RSUs (restricted stock units)](/wiki/restricted-stock-units/) instead of options to later hires—RSUs are already common stock (or its equivalent) and are not subject to underwater strike prices.

## Negotiating and structuring preferences

In VC term sheets, the preference is one of the most contentious items:

- **Multiply**: Is it 1×, 2×, or 3× the investment amount?
- **Participating or non-participating**: Can investors double-dip into remaining proceeds?
- **Cumulative or non-cumulative**: Do unpaid preferences carry forward to the next exit, or are they capped?
- **Pari passu or stacked**: Do all preferred shares rank equally, or do later rounds have priority?

Founders push for lower multiples (1×) and non-participating provisions. Investors push for higher multiples and participation. In hot markets with many funding options, founders have leverage; in down markets, investors do.

## The preference stack's hidden geometry

A simple math: if a company raises $5M (Series A), $10M (Series B), and $15M (Series C), and the eventual exit is $60M, the preference stack typically looks like:

- Series C: $15M × 1× = $15M (non-participating), leaving $45M
- Series B: $10M × 1× = $10M (non-participating), leaving $35M
- Series A: $5M × 1× = $5M (non-participating), leaving $30M
- **Total to preferred: $30M; Common gets: $30M**

But if Series B and C are participating:
- Series C: $15M + (15/30 × $45M) = $15M + $22.5M = $37.5M
- Series B: $10M + (10/30 × $7.5M) = $10M + $2.5M = $12.5M
- Series A: $5M + (5/30 × $0M) = $5M + $0M = $5M
- **Total to preferred: $55M; Common gets: $5M**

The common shareholders (founders, employees) are squeezed from a $30M claim to a $5M claim by the waterfall structure.

<div class="wiki-seealso">

### Closely related
- [Preferred stock](/wiki/preferred-stock/) — equity with senior claims, often with liquidation preference
- [Anti-dilution provisions](/wiki/anti-dilution-provisions/) — protections for preferred shareholders against down rounds
- [Venture capital term sheet](/wiki/venture-capital-fund/) — the contract documenting a VC investment
- [Enterprise value](/wiki/enterprise-value/) — the total value available to all security holders

### Wider context
- [Bankruptcy](/wiki/liquidation/) — legal process for unwinding insolvent companies
- [Leveraged buyout](/wiki/leveraged-buyout/) — acquisition financed with debt, senior to equity
- [Equity waterfall](/wiki/equity-waterfall/) — the distribution of proceeds to all equity classes
- [M&A](/wiki/merger/) — mergers and acquisitions where preference determines payouts

</div>
