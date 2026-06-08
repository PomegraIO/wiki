---
title: "Illiquidity Discount on a Private Equity Stake"
description: "How to quantify the illiquidity discount when valuing a private company stake that cannot be freely bought or sold."
keywords:
  - illiquidity discount private equity stake
  - discount for lack of marketability
  - private stock valuation adjustment
  - restricted stock discount valuation
  - illiquidity private equity discount
image: /svg/valuation.svg
---

*An **illiquidity discount** is a percentage reduction applied to a private company's [fair value](/fair-value/) to account for the fact that the shares cannot be sold quickly or at market price. Unlike a publicly traded stock that can be sold in seconds, a private equity stake is locked in; that constraint reduces its worth to an investor.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Illiquidity Discount on Private Equity Stakes — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Illiquidity adjustments quantify the cost of being trapped in an unmarketable asset.</div>

|   |   |
|---|---|
| **Definition** | Percentage reduction to value for inability to sell privately held shares freely |
| **Typical range** | 20% to 50% depending on company maturity and exit timeline |
| **Common anchors** | Restricted-stock studies, option-pricing models, transaction data |
| **Contexts** | Gift tax valuations, buyout pricing, estate tax, litigation disputes |
| **Distinct from** | Marketability discount (which includes broader restrictions) |

</aside>

## What illiquidity discounts are and why they exist

A private equity stake has no ready buyer at a known price. If you own 5% of a venture-backed software company, you cannot call a broker and sell tomorrow at the market close. You are trapped until a liquidity event—a [leveraged buyout](/leveraged-buyout/), a secondary sale, or an [initial public offering](/initial-public-offering/). That exit may come in two years, five years, or a decade.

The longer you wait and the less certain the exit, the lower your stake's value *today*. An investor rationally discounts a private equity stake below what the same company would be worth on a public market, because they are sacrificing the option to exit at will.

The illiquidity discount is the quantification of that sacrifice. If a private company's business is valued at $10 million on a cash-flow basis, and similar public companies trade at $12 million, the illiquidity discount explains part of the gap. (Other gaps—minority ownership, control premium, company-specific risk—are separate.)

## Illiquidity discount versus discount for lack of marketability

The terms are sometimes used interchangeably but have distinct meanings. A **discount for lack of marketability (DLOM)** is the broad adjustment for any constraint on selling shares, including illiquidity *and* lack of publicly available financial information, limited buyer pools, and legal restrictions on transfer. An **illiquidity discount** specifically measures the time-value cost of being unable to sell quickly.

In practice, appraisers often blend them. When valuing a minority stake in a closely held company for gift tax or estate tax purposes, the appraiser might apply a DLOM of 30–40%, which encompasses both illiquidity and minority-status constraints.

## Quantifying illiquidity: restricted-stock studies

The most cited anchor is empirical data on **restricted stock discounts**. In the 1990s and 2000s, academic researchers (notably those cited in SEC interpretive releases) studied the price difference between unrestricted shares and restricted shares of the same company. A company might issue restricted stock to an insider at a lower price than it sold unrestricted shares to public investors. The discount—say, 30%—was a market-derived measure of the cost of illiquidity.

A typical restricted-stock study finds:

- **Small, illiquid private companies:** 35–50% discount
- **Mature private companies close to exit:** 20–35% discount
- **Restricted shares of public companies:** 15–30% discount (less illiquidity because the underlying business is liquid)

These studies are now decades old, and markets have shifted (more secondary sales, SPACs, direct listings), but they remain the standard touchstone for appraisers and courts.

## Option-pricing models

A more analytical approach uses **put-option valuation**. Imagine the shareholder has the right to sell their stake at a fixed price (the estimated fair value) on a specified future date (the expected exit). The longer the wait and the higher the volatility in valuation, the more valuable that put option. The cost of illiquidity is approximated as the value of that "insurance" the shareholder is forgoing by being locked in.

Using a Black-Scholes variant, you can estimate the value of a put option with:
- **Strike:** the estimated fair value of the stake today
- **Expiration:** the expected time to exit (e.g., three years)
- **Volatility:** the estimated volatility in the company's valuation over that period

A three-year illiquid stake in a volatile, early-stage company might have an implicit put value of 40% of current fair value; a mature, stable company might have a put value of only 15%.

## Typical illiquidity discount ranges by context

**Venture-backed startups (Series B–D):** 40–50% discount. Long exit timeline, high outcome volatility, binary success/failure.

**Mature, profitable private companies (5–10 years old):** 25–35% discount. More stable cash flows, but exit still uncertain.

**Pre-IPO private equity–backed companies (within 1–2 years of exit):** 15–25% discount. Exit is near, valuation is more stable.

**Family business minority stake:** 30–45% discount, often compounded with a 20–30% minority discount (for lack of control).

## Gift tax and estate tax applications

The IRS allows illiquidity discounts in calculating the gift or estate tax value of a private company stake. If a parent gives a child 10% of a family business valued at $5 million, the appraiser might apply a 35% illiquidity discount (+ a 30% minority discount), resulting in a taxable gift value of roughly $2.3 million instead of $500,000.

The discount is defensible if documented with comparable transactions, restricted-stock studies, or an independent appraisal. The IRS has challenged aggressive illiquidity discounts (combined with minority and other discounts that together reduce value by 60–70%) in high-profile cases; courts typically uphold discounts of 30–45% when properly supported.

## Leveraged buyout and acquisition contexts

When a [private equity](/private-equity-fund/) firm negotiates to acquire a company, it pays a price that implicitly reflects illiquidity. If the business is valued at $50 million on a [discounted cash flow](/discounted-cash-flow-valuation/) basis, but there are only three interested buyers (all private equity firms), the exit optionality is genuinely limited, and the buyer may negotiate a price that reflects a de facto illiquidity discount.

Secondary markets for late-stage venture and buyout stakes (secondary sales, continuation funds) have created reference pricing that effectively measures illiquidity discounts. A Series C stake selling in the secondary market at a 15–25% discount to the last primary round price illustrates real-world illiquidity costs.

## Litigation and appraisal disputes

Courts often depend on illiquidity discounts when valuing stakes in shareholder disputes, appraisal rights, or partnership dissolutions. An appraiser defending a valuation must cite restricted-stock studies or option-pricing analysis to justify the chosen discount. Overconfident assumptions—assuming a three-year exit when no clear path exists, or using low volatility assumptions for a high-risk business—invite challenge.

## See also

<div class="wiki-seealso">

### Closely related

- [Fair value](/fair-value/) — The starting point before illiquidity adjustment
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — The valuation method being adjusted for illiquidity
- [Leveraged buyout](/leveraged-buyout/) — Context where illiquidity discounts factor into deal pricing
- [Private equity fund](/private-equity-fund/) — Investors holding illiquid stakes and managing exit timing
- [Initial public offering](/initial-public-offering/) — The liquidity event that triggers illiquidity discount removal
- Valuation — The broader framework for private company pricing

### Wider context

- [Black-Scholes-model](/black-scholes-model/) — Option pricing framework for quantifying illiquidity
- Minority interest discount — Separate constraint on minority stakes
- [Secondary market](/secondary-market/) — Where private stakes are traded at illiquidity-adjusted prices
- [Estate tax](/estate-tax/) — Tax context where illiquidity discounts are commonly applied
- [Due diligence](/due-diligence/) — Valuation review process where illiquidity is assessed

</div>
