---
title: "Convertible Note to Equity Conversion Mechanics"
description: "Learn how convertible notes convert to equity: valuation cap and discount rate math, what triggers conversion, and how preferred share allocation works."
keywords:
  - convertible note conversion
  - equity conversion mechanics
  - valuation cap discount
  - qualified financing
  - preferred share allocation
  - startup funding
---

*A **convertible note** is a loan that converts into preferred shares at a future funding round (the **qualified financing**), rather than being repaid in cash. The conversion price is determined by either a **valuation cap** or a **discount rate** (or both, whichever is lower), ensuring early investors get a better price than later-stage investors. Understanding the mechanics reveals how founders and venture capitalists split ownership at each funding milestone.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Convertible Notes — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A bridge loan that converts at the next major financing round, awarding early investors a discount.</div>

|   |   |
|---|---|
| **Trigger** | Qualified financing (Series A, B, or later) reaching a minimum size |
| **Valuation cap** | Maximum implied valuation at conversion (lower = more shares for investor) |
| **Discount rate** | Percentage off the per-share price in the new round (typically 20–30%) |
| **Conversion price** | The lower of capped valuation or discounted new-round price |
| **Accrued interest** | Often added to principal before conversion, increasing share count |
| **Liquidation preference** | Convertible may be repaid as debt before equity in early exits |

</aside>

## Why Convertible Notes Exist

In the early stages of a startup, the company's value is hard to measure. A Series A investor will spend months on due diligence and negotiate a valuation with confidence. Seed investors—angels and early VCs—have much less information. A convertible note lets both parties defer the valuation debate. The company borrows money, and at the Series A, when the valuation is settled and a professional investor has done the math, the note converts.

This is cheaper and faster than negotiating a seed equity round. There is no need to agree on a specific share price up front. Instead, the note includes two "kickers"—the valuation cap and discount rate—that guarantee the seed investor gets shares at a discount to the Series A price. This compensates for their earlier risk.

## The Valuation Cap

The **valuation cap** is an upper bound on the startup's implied valuation at conversion. It is the ceiling; the actual valuation is typically higher.

**Example:** A seed investor buys a $100,000 convertible note with a $2 million valuation cap. In a Series A, the company is valued at $10 million by a professional investor. At conversion, the cap applies: the company's valuation for conversion purposes is capped at $2 million, not $10 million.

The math:
- Valuation cap: $2 million
- Post-money Series A valuation: $10 million (irrelevant for the note-holder)
- Convertible principal: $100,000
- Conversion price per share: $2,000,000 ÷ (pre-determined share count) = some price *X*

If the Series A is priced at, say, $5 per share, but the cap makes the effective note price $2 per share, the note-holder gets shares at $2 while new Series A investors pay $5. The note-holder receives roughly 2.5 times as many shares for the same $100,000.

**Why caps matter:** The lower the cap, the more shares the seed investor receives. A $1 million cap is more favorable to the seed investor than a $5 million cap. Caps reflect expectations about the company's trajectory and founders' willingness to dilute. Early-stage startups use aggressive caps (relative to current traction) to attract bold early money.

## The Discount Rate

The **discount rate** is a percentage reduction applied to the per-share price in the new round. It is a simpler, more direct mechanism.

**Example:** A note-holder converts with a 25% discount. The Series A price is $4 per share. The note-holder's conversion price is $4 × (1 − 0.25) = $3 per share.

**Why discounts matter:** Discounts are easier to understand than valuations caps. They directly tell the seed investor: "You get 25% off whatever the next investors pay." Typical discounts range from 15% to 30%.

## Which Controls Conversion: Cap or Discount?

Most convertible notes include *both* a cap and a discount. The investor gets whichever is more favorable—i.e., results in a lower conversion price (more shares).

**Scenario 1: Cap is favorable**

- Valuation cap: $2 million
- Series A price: $8 per share (implying $20 million valuation)
- Discount: 25%
- Capped conversion price: $2M implied price, say $3/share
- Discounted conversion price: $8 × 0.75 = $6/share
- **Investor uses the cap, converts at $3/share**

**Scenario 2: Discount is favorable**

- Valuation cap: $10 million
- Series A price: $2 per share (implying $5 million valuation)
- Discount: 25%
- Capped conversion price: roughly $3/share
- Discounted conversion price: $2 × 0.75 = $1.50/share
- **Investor uses the discount, converts at $1.50/share**

The "or the discount, whichever is lower" language ensures the seed investor always gets the best available deal.

## Accrued Interest and Share Count

Convertible notes typically accrue interest—often 5% to 8% per year—just like any loan. At conversion, the interest is not paid in cash; instead, it is added to the principal and converted into additional shares.

**Example:** A $100,000 note at 6% annual interest, held for 18 months, accrues $9,000 in interest. At conversion, the amount converted is $109,000, not $100,000. The note-holder receives roughly 9% more shares because of the accumulated interest.

This accrual is a major advantage of convertible notes compared to equity: the investor earns a return (the interest) even in a flat or down scenario. If the Series A never closes and the company winds down, the note-holder has debt status (they are owed principal plus interest) rather than common-stock status.

## The Mechanics of a Qualified Financing

Conversion is triggered by a **qualified financing**, typically defined as a round raising at least $500,000 to $1 million (depending on the note's terms) at a pre-determined price. Not every funding event triggers conversion. A bridge loan or secondary sale usually does not. But a Series A, Series B, or later VC round almost certainly does.

At conversion:
1. The company calculates the total principal plus accrued interest.
2. The conversion price is determined (lower of cap or discounted Series A price).
3. The note-holder receives a number of shares equal to (Principal + Interest) ÷ Conversion Price.
4. Those shares are typically preferred shares in the new round, with the same rights as shares purchased by the Series A investor.

## Ownership Dilution and the Path to Series A

Convertible notes are deliberately vague on share count until conversion because the share count depends on the Series A valuation, which is unknowable up front. This creates a source of tension: the founders want a high Series A valuation (which lowers the note-holders' share count), while note-holders want a low one (which increases their ownership).

A company that raises $500,000 in convertible notes at a $1 million cap, then raises a $5 million Series A at a $20 million post-money valuation, will see the note-holders convert at a significant discount. The founders will feel the dilution: what looked like a $20 million company has effectively given a substantial equity stake to seed investors at a $1–2 million implied valuation.

This is intentional design: early money deserves a discount for risk. But it shapes the equity structure for years.

## Pro Rata Rights and Follow-On Investing

Most convertible note agreements include **pro rata rights**, allowing the note-holder (now a preferred shareholder after conversion) to participate in future rounds at the same per-share price as new investors. This turns the seed investor into a recurring participant in the cap table.

A note-holder with $100,000 converted into 10,000 shares at a $20 million Series A post-money may later have the right to buy additional shares in Series B at the same per-share price, preserving their ownership percentage.

## See also

<div class="wiki-seealso">

### Closely related

- [Convertible-bond](/convertible-bond/) — the corporate debt analog, with equity warrants and conversion to common shares
- [Preferred-stock](/preferred-stock/) — the share class that note-holders receive upon conversion
- Valuation — how founders and investors agree on a company's worth
- [Equity-financing](/equity-financing/) — the broader landscape of raising money through share sales
- [Liquidation-preference](/liquidation-preference/) — the order in which investors are paid in an exit or wind-down

### Wider context

- [Initial-public-offering](/initial-public-offering/) — the exit event that fully liquidates note-holder preferred shares
- Venture-capital — the ecosystem of Series A through Series Z funding rounds
- [Hostile-takeover](/hostile-takeover/) — mergers where note-holder and preferred-shareholder rights matter
- [Leverage-ratio-forex](/leverage-ratio-forex/) — how debt and equity ratios affect financial structure (related for corporate capital structure)
- [Share-buyback](/share-buyback/) — how companies later repurchase convertible or preferred shares

</div>
