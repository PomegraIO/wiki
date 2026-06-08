---
title: "Waterfall Analysis: Preferred vs Common Stock in Private Companies"
description: "How waterfall analysis models liquidation preferences and participation rights to allocate proceeds between preferred and common shareholders in private companies."
keywords:
  - waterfall analysis preferred common stock
  - liquidation preferences
  - preferred stock participation
  - private company distributions
  - cap table modeling
  - shareholder waterfall
image: "/svg/valuation.svg"
---

*A **waterfall analysis** models how proceeds from an exit (sale, merger, or wind-down) flow through a cap table to each shareholder class based on liquidation preferences and participation rights. Understanding this distribution sequence is essential because preferred shareholders often claim earlier or richer payouts than common holders.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Waterfall Analysis — Key Facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Liquidation preferences and participation rights determine how exit proceeds split between preferred and common shares.</div>

|   |   |
|---|---|
| **Definition** | Model showing the order and amount each shareholder class receives in a distribution event |
| **Core input** | Total exit proceeds; cap table with each class's terms |
| **Key variable** | Whether preferred has "1x", "non-participating", or "participating" rights |
| **Typical order** | Senior preferred → Junior preferred → Common → Extras (convertible debt, options) |
| **Critical lever** | Participation cap; whether preferred converts to common to capture upside |
| **Used for** | M&A modeling, negotiating financing terms, founder compensation scenarios |

</aside>

## Why Waterfall Analysis Matters

When a private company exits, the first question shareholders ask is: how much do I get? The answer depends not just on the sale price, but on what rights are attached to each class of stock. A founder who owns 40% in common shares might end up with far less than 40% of the proceeds if the company raised multiple rounds of preferred stock with liquidation preferences.

A waterfall analysis makes this distribution explicit. It avoids surprises, surfaces incentive misalignments, and helps negotiators understand why a preferred shareholder might block or push for a particular exit price.

## The Basic Waterfall Sequence

The typical order of payouts in an exit is:

1. **Expenses and debt** — transaction fees, legal costs, bank debt, convertible notes are paid off first.
2. **Senior-most preferred stock** — often Series A or earlier rounds, with a specified liquidation preference multiple (e.g., 1x, 2x).
3. **Next-junior preferred** — Series B, C, etc., in order of seniority.
4. **Participation or conversion decision** — preferred shareholders choose whether to exercise their participation right or convert to common and share pro-rata.
5. **Common stock** — whatever remains goes to common holders in proportion to their ownership.

This order is crucial. If Series A preferred shareholders have a 1x liquidation preference and the company exits for $50 million after Series A invested $10 million, Series A gets at least $10 million before anyone else. Only the excess flows to later shareholders and common holders.

## Liquidation Preferences Explained

A **liquidation preference** is a contractual right that gives preferred shareholders priority to receive their investment back (or a multiple of it) before common shareholders are paid. The most common forms are:

**1x or straight preference:** Preferred shareholders receive $1 for every $1 invested before anyone else gets paid. A Series A that invested $5 million demands $5 million out before a penny goes to common.

**Multiple preference (2x, 3x):** Preferred shareholders receive $2 or $3 per $1 invested. A 2x preference with a $5 million investment means Series A gets $10 million off the top, then the remainder is split.

**Participating vs non-participating:** A non-participating preference means the preferred investor gets their money back (or multiple) and then converts to common to share pro-rata in what's left. A participating preference allows them to take their payout AND participate in the remaining proceeds as if they'd converted to common.

## A Concrete Example

Imagine a company is being sold for $30 million. The cap table is:

| Class | Shares | Price/Share | Total Invested | Liquidation Multiple |
|-------|--------|-------------|-----------------|----------------------|
| Series A Preferred | 1,000,000 | $1 | $10 million | 1x non-participating |
| Common | 2,000,000 | $0.50 | — | — |

With a 1x non-participating preference, the Series A waterfall works like this:

1. Series A gets $10 million (their 1x preference satisfied).
2. Remaining proceeds: $30M − $10M = $20 million.
3. Series A converts to common and shares pro-rata. Series A owns 1M / 3M total shares = 33.3%.
4. Series A's final payout: $10M + (33.3% × $20M) = $10M + $6.67M = **$16.67 million**.
5. Common holders get (66.7% × $20M) = **$13.33 million**.

If instead Series A had a participating 1x preference:

1. Series A gets their $10 million preference.
2. Series A **also** participates in the remaining $20 million pro-rata (33.3% × $20M = $6.67M).
3. Series A's final payout: $10M + $6.67M = **$16.67 million** (same as before, because they already owned 33.3%).
4. Common holders get **$13.33 million** (same).

But if Series A had a **2x participating** preference:

1. Series A gets $20 million (2x their $10 million investment).
2. Series A also participates in what remains: $30M − $20M = $10 million.
3. Series A's share of that remaining $10M: 33.3% × $10M = $3.33M.
4. Series A's final payout: $20M + $3.33M = **$23.33 million**.
5. Common holders get only **$6.67 million** (much worse).

This example shows why the participation cap and multiple matter enormously. A 2x participating preference can dramatically shift proceeds from common to preferred shareholders.

## When Preferred Investors Convert Instead of Take Preference

In a very strong exit (high valuation), preferred shareholders often **choose to convert to common** and abandon their liquidation preference. Why? Because their pro-rata common share is worth more than their preference.

Example: A company exits for $100 million, Series A invested $5 million at 1x preference. If Series A is 10% of the cap table, their conversion value is 10% × $100M = $10M, far more than their 1x preference payout of $5M. They convert and pocket $10M.

The waterfall model must therefore include a decision node: will each preferred class exercise their preference, or convert and gamble on the common pool? Sophisticated analyses will calculate the conversion threshold—the exit value at which preferred holders flip from preferring their payout to converting.

## Building a Waterfall Model

A practical waterfall model includes:

- **Exit price assumption** — test multiple scenarios (conservative, base, upside).
- **Complete cap table** — every share class, each shareholder's holdings, vesting status if relevant.
- **Term sheet details** — each preferred series' liquidation multiple, participation rights, conversion ratio.
- **Debt and expenses** — what gets paid before shareholders.
- **Calculation logic** — a clear sequence that honors preferences and decides conversions.

Spreadsheet-based models are standard. Rows represent each shareholder or class; columns show the waterfall at each step (preference, post-preference, conversion decision, final payout). The model becomes especially valuable when founders negotiate financing terms or evaluate exit offers; it shows whose interests align and where conflicts arise.

## Interaction with [Options](/option/) and Convertible Notes

Employees holding options must decide whether to exercise before an exit or treat options as worthless if they're underwater. [Convertible notes](/convertible-bond/) often have conversion triggers tied to the exit, converting to preferred stock before the waterfall runs. A complete waterfall includes a section for option exercises and convertible conversions before the preference waterfall begins.

## When Preferred Gets Nothing

In a low exit (fire sale), preferred shareholders may receive nothing. If the company sells for $5 million and has $8 million in Series A liquidation preferences alone, Series A gets their payout, and common holders get zero. This possibility is why common shareholders scrutinize preference terms at fundraising time and why founders sometimes refuse to raise capital with aggressive preferences.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquidation Preference](/liquidation-preference/) — the contractual right underlying the waterfall
- Participating Preferred Stock — when preferred investors share in the upside
- Cap Table — the registry of all share holdings the waterfall relies on
- [Pre-Money vs Post-Money Valuation](/pre-money-post-money-valuation-difference/) — connected investor ownership math
- [Convertible Bond](/convertible-bond/) — often part of the waterfall sequence

### Wider context

- [Equity Financing](/equity-financing/) — why companies raise preferred stock in the first place
- [Merger](/merger/) — a common trigger for waterfall distributions
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulatory oversight of preferred terms

</div>
