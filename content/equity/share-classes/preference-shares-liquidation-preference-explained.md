---
title: "Liquidation Preference on Preference Shares Explained"
description: "Liquidation preference on preference shares: 1x non-participating vs participating, multiple preference mechanics, and exit payout examples at different valuations."
keywords:
  - liquidation preference preference shares explained
  - liquidation preference
  - participating preferred
  - non-participating preferred
  - preferred stock exit
  - venture capital payouts
---

*A liquidation preference on preference shares is a contractual right that guarantees preferred shareholders receive a fixed amount per share before common shareholders get anything, in the event of acquisition, bankruptcy, or dissolution. The preference can be "non-participating" (capped at the preference amount) or "participating" (allowing holders to choose between the preference and their pro-rata share of all proceeds, whichever is larger). Understanding which type, and at what multiple, is crucial—it determines who wins and loses at every possible exit valuation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquidation Preference — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for preferred equity structures." />

<div class="wiki-infobox-caption">Preferred shareholders get paid first at exit; the preference amount and participation rights determine who captures upside.</div>

|   |   |
|---|---|
| **1x preference** | Preferred shareholder gets back $1 for every $1 invested, before others receive anything |
| **Participating preference** | After receiving 1x, holder also gets pro-rata share of remaining proceeds |
| **Non-participating preference** | Holder receives only the preference; no additional upside |
| **Multiple preference** | 2x, 3x, or higher preference means $2–$3 per share invested before common payout |
| **Waterfall order** | Preference payouts go through series in reverse order (Series Z before A) |

</aside>

## Why Liquidation Preference Exists

Venture capital and private equity investors take risk. They invest millions in a company with no guarantee it will succeed. If the company is acquired for less than the total invested capital—a "down sale"—investors could lose money. Liquidation preference is insurance: it ensures preferred investors recoup their investment before common shareholders or founders capture anything.

Without liquidation preference, a company valued at $100 million at IPO might later be acquired for $50 million. If preferred investors put in $60 million at earlier rounds, they would own shares worth only $50 million (their pro-rata slice). They'd lose $10 million. With a 1x liquidation preference, they are guaranteed to receive their $60 million back first, and only the remaining $50 - $60 = negative amount goes to common shareholders—so common shareholders get nothing.

In a successful up-exit (acquisition at a price higher than all invested capital), liquidation preference matters less. All investors—preferred and common—receive pro-rata proceeds, and the preference becomes academic because there's enough money for everyone.

## Non-Participating Preference: The Standard

The most common form is **1x non-participating preference**. This means:

1. Preferred shareholders receive $1 per preferred share invested before any common shareholder receives anything.
2. After paying out the preference, all remaining proceeds are split pro-rata among ALL shareholders (preferred and common) based on share count, not class.
3. Preferred shareholders get no additional upside beyond their pro-rata share.

**Example: Non-participating exit**

- Series A invested $10 million for 1 million Series A preferred shares. 1x preference.
- Common shareholders own 2 million common shares (assume 50% of all shares).
- Company is acquired for $50 million.
- Payout waterfall:
  - Series A gets $10 million (1x preference).
  - Remaining: $50M - $10M = $40 million.
  - This $40M is split pro-rata: Series A owns 33% of all shares (1M / 3M), common owns 67% (2M / 3M).
  - Series A receives: $40M × 33% = $13.3M.
  - Common shareholders receive: $40M × 67% = $26.7M.
  - Series A total: $10M + $13.3M = $23.3M.
  - Common total: $26.7M.

## Participating Preference: Double-Dipping

**Participating preference** (also called "full participation" or "double-dip") allows the holder to receive BOTH the preference amount AND a pro-rata share of remaining proceeds. It's more aggressive:

1. Preferred shareholder receives their full liquidation preference ($1 per share).
2. The holder then ALSO participates in the remainder pro-rata with common shareholders.
3. This can result in preferred shareholders receiving more than their ownership percentage would normally entitle them to.

**Example: Participating preference exit (same facts as above)**

- Series A has 1x participating preference.
- Company acquired for $50 million.
- Payout waterfall:
  - Series A gets $10 million (preference).
  - Remaining: $40 million.
  - Series A participates pro-rata: $40M × 33% = $13.3M.
  - Common shareholders: $40M × 67% = $26.7M.
  - Series A total: $10M + $13.3M = $23.3M.
  - Common total: $26.7M.

In this example, participating vs. non-participating made no difference because proceeds exceeded the total preference amount. But watch what happens in a down-sale:

**Example: Down-sale with participating preference**

- Same facts, but company acquired for $15 million.
- Series A has 1x participating preference.
- Payout waterfall:
  - Series A gets $10 million (preference).
  - Remaining: $15M - $10M = $5 million.
  - Series A participates pro-rata: $5M × 33% = $1.67M.
  - Common shareholders: $5M × 67% = $3.33M.
  - Series A total: $10M + $1.67M = $11.67M.
  - Common total: $3.33M.

The participating preference allows Series A to capture $11.67M of $15M—77%—despite owning only 33% of shares. Common shareholders, who own 67% of the company, get only $3.33M. This is sometimes called "pay-to-play" financing because participating preferred is common in later-stage down-rounds where the latest investors demand extra protection.

## Multiple Preferences (2x, 3x)

Some series have preferences above 1x. A 2x preference means preferred shareholders get $2 per share invested before anyone else receives anything. This is rare in venture but more common in distressed financings or turnarounds.

**Example: 2x preference**

- Series A invested $10 million for 1 million shares at a 2x preference.
- Company acquired for $15 million.
- Payout waterfall:
  - Series A gets $20 million (2x preference on $10M).
  - But the acquisition is only $15M total, so Series A gets all $15M.
  - Common shareholders get nothing.

Higher preferences are a negotiation point: they reflect the risk and bargaining power of the later investor. A struggling company raising a survival round might accept a 2x preference to secure funding, accepting that the founders (who hold common stock) are likely to be wiped out.

## Preference Stacking and Waterfall Order

Most companies have multiple preferred series: Series A, B, C, etc. Liquidation preferences are paid out in reverse order of investment (Series Z before A). This is called the "waterfall" or "preference stack."

**Example: Multi-series waterfall**

- Series A invested $10M (1x preference, non-participating).
- Series B invested $20M (1x preference, non-participating).
- Series C invested $30M (1x preference, non-participating).
- Total invested: $60M.
- Company acquired for $50M.
- Payout waterfall:
  - Series C: First $30M of the $50M.
  - Series B: Next $20M (none left).
  - Series A: Gets nothing.
  - Common: Gets nothing.

In this down-sale, only Series C is made whole. Series A and B investors lose capital, and common shareholders (including founders) receive zero. This cascading effect means early investors often see losses in unsuccessful exits because later-stage investors' preferences eat up all proceeds.

## When Liquidation Preference Matters Most

Liquidation preference is most consequential in three scenarios:

1. **Down-sales or modest exits**: If a company is acquired below the total invested capital, preference determines who loses money. Non-participating preferred holders are protected up to their preference; common shareholders are often wiped out.

2. **Bankruptcy or restructuring**: In a Chapter 11 reorganization, liquidation preference determines creditor priority and who receives new equity in the reorganized entity.

3. **Competition between rounds**: Later-stage investors negotiate preference terms as a way to ensure earlier investors bear downside risk. A Series B investor with a 1x non-participating preference is safer than one with no preference if the company later struggles.

In explosive up-exits—acquisition for 5x or 10x invested capital—liquidation preference becomes almost irrelevant because there's enough to pay all preferred shareholders their pro-rata share plus more. The preference is "out of the money."

## See also

<div class="wiki-seealso">

### Closely related

- [How Share Class Conversion Works](/how-share-class-conversion-works/) — how preferred shares convert to common at exit
- [Preferred Stock](/preferred-stock/) — definition and rights of preferred shareholders
- [Acquisition](/acquisition/) — M&A deals and exit processes
- [Redemption Rights Equity](/redemption-rights-equity/) — investor repurchase rights

### Wider context

- [Private Equity Fund](/private-equity-fund/) — PE investor structure and return objectives
- [Venture Capital](/hedge-fund/) — VC financing and exit expectations
- [Leverage Buyout](/leveraged-buyout/) — how acquisition financing affects equity payouts
- [Capital Flows](/capital-flows/) — equity and debt capital in corporate finance

</div>
