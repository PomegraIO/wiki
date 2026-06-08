---
title: "Simple Agreement for Future Equity"
description: "A convertible instrument that grants rights to future equity on a priced round without interest or maturity date."
keywords:
  - SAFE
  - simple agreement future equity
  - convertible instrument
  - seed funding
  - startup capital
image: "/svg/equity.svg"
---

*A **Simple Agreement for Future Equity** (SAFE) is a lightweight contract that grants an investor the right to own equity in a company at a future date, typically when the company raises a priced funding round. Unlike a convertible note, a SAFE accrues no interest, has no maturity date, and is classified as equity rather than debt from inception, making it simpler to issue and cleaner legally for issuers.*

## Origins and rise to dominance

SAFEs were invented by Y Combinator and released as open-source documents in 2013, displacing convertible notes as the go-to pre-Series A instrument. The motivation was simple: convertible notes are complicated. They accrue interest, have maturity dates, and carry debt-like accounting treatment that can tangle cap tables and raise questions with auditors. A SAFE strips these away. An investor hands cash to a startup with a promise: "When you raise a future round at a set price, I get equity at a discount to that price." No debt, no interest, no expiration. For early-stage founders raising $100k–$2m, SAFEs are now the default first choice, and most experienced investors accept them without pushback.

## Mechanics: discount and valuation cap

A SAFE is essentially an option on future equity, with two main parameters: **discount** and **valuation cap**. 

When the startup eventually raises a priced round (typically [Series A](/initial-public-offering/), or even Series Seed), the SAFE converts. The investor's money converts to equity at whichever is lower: the Series A price, or a discounted version of it. The discount is typically 20–30%. So if Series A is at $10 per share and the investor's SAFE carries a 20% discount, they convert at $8 per share. The valuation cap adds a ceiling: if the Series A values the company very high, the SAFE investor doesn't want to be priced entirely at that high valuation. A SAFE cap of $5m means that even if Series A values the company at $20m, the SAFE investor's conversion is capped as if the company were worth $5m.

These terms reward early risk-taking. An investor backing a pre-revenue startup takes more risk than an investor in Series A; the discount and cap compensate by giving them more favorable pricing.

## No maturity date or interest

Unlike a convertible note, a SAFE has no maturity date. The startup doesn't owe the money back on a given date if it hasn't raised a Series A. This is immensely valuable for founders, because it removes the pressure of a ticking clock. A SAFE can sit on the cap table for 3, 5, or even 10 years while the startup grows. It also means the startup cannot trigger a debt default by missing a repayment date.

The absence of interest simplifies accounting. A convertible note accrues interest over time, which creates a growing liability on the balance sheet. A SAFE avoids this, remaining a simple promise to convert until the triggering event occurs.

## Conversion triggers

A SAFE typically converts on:

1. **Priced equity round**: The most common trigger. If the company raises a Series A (or Series Seed, or any round with a per-share price), the SAFE converts automatically.
2. **IPO**: If the company goes public without a priced round, SAFE holders convert at a price determined by the company's pre-IPO valuation, usually through negotiation or a formula.
3. **Liquidity event**: If the company is sold or undergoes a major [merger](/merger/), the SAFE converts (or is cashed out at a payout amount set in the agreement).
4. **Optional conversions**: A SAFE may allow the holder to convert on demand at any time, though this is rare.

If none of these occurs and the company dies, the SAFE holder gets nothing. They have no [liquidation preference](/liquidation-preference/)—they are not creditors and do not stand ahead of equity holders in the event of dissolution. This is the key risk: SAFEs are equity-like in upside (all converted equity), equity-like in downside (lose everything if the company fails), but sit outside the formal equity structure until conversion.

## SAFE vs. convertible notes

A convertible note is a debt instrument with an interest rate and a maturity date. If the startup hasn't raised a priced round by maturity, the note typically converts to equity at a pre-set cap or, in some cases, must be repaid. This creates awkward scenarios: a startup that's thriving but hasn't yet raised Series A must either pay back notes or negotiate an extension. 

SAFEs avoid this. They sit quietly, accumulating no interest, with no repayment obligation. From an investor's perspective, a note offers more protection (interest, maturity, potential repayment) but more complexity. A SAFE is a pure bet on the company's success: if it succeeds, the investor converts and wins; if it fails, the investor loses the initial investment.

Most early-stage investors now prefer SAFEs because they're faster to negotiate and cheaper to legal-review (templates are available free, and many investors accept them without modification).

## Drawbacks and risks

**Investor downside**: A SAFE holder has no guaranteed return if the company fails, no claim to assets on liquidation, and no interest accumulation. They are betting entirely on a priced round or IPO. Some investors mitigate this by diversifying across many SAFEs, betting that enough will hit to compensate for failures.

**Founder ambiguity**: A SAFE creates cap-table ambiguity until conversion. A founder raising a Series A must disclose all SAFEs to Series A investors and model their conversion impact. If many SAFEs exist, the founder's effective ownership post-Series A can be surprisingly small. Some founders underestimate this and are shocked at the dilution.

**Valuation cap negotiations**: If the startup is extremely successful and raises Series A at a very high valuation, the valuation cap becomes valuable to SAFE holders but painful for Series A investors and founders. A SAFE issued at a $5m cap that matures when Series A values the company at $100m creates tension and potential legal disputes over the conversion mechanics.

## Multi-type SAFEs and customization

Y Combinator publishes several SAFE templates: Standard, Post-Money, and MFN (Most Favored Nation). The Post-Money SAFE is more founder-friendly because it includes the SAFE amount in the post-money valuation, diluting fewer parties in the next round. MFN clauses allow SAFE holders to adopt the better terms if other SAFEs are issued with more favorable discounts or caps.

Most SAFEs are lightly customized or used as-is from the template, reinforcing their simplicity. Heavy customization defeats the purpose.

## Regulatory and accounting treatment

Accounting standards treat SAFEs as equity (or equity-like) rather than debt. This is cleaner for startups' financial statements than convertible notes, which must be classified as liabilities until conversion. Regulators generally treat SAFEs as securities, so founders must ensure SAFE issuances comply with securities laws (typically through exemptions like Regulation D in the US or similar regimes elsewhere).

## See also

<div class="wiki-seealso">

### Closely related

- [Equity Financing](/equity-financing/) — the general category of capital-raising via share issuance
- [Convertible Bond](/convertible-bond/) — similar instrument in the fixed-income world, with interest and maturity
- [Series Seed Preferred](/series-seed-preferred/) — the next stage, a priced preferred share issuance
- [Common Stock](/common-stock/) — the share class that SAFE investors convert into
- Anti-Dilution Rights — protection mechanisms that some SAFE variants include
- [Management Shares](/management-shares/) — founder-controlled shares that often coexist with SAFE holders

### Wider context

- [Initial Public Offering](/initial-public-offering/) — a conversion trigger for SAFEs that haven't yet converted
- [Merger](/merger/) — an exit event that triggers SAFE conversion or payout
- Venture Capital — the investor base that uses SAFEs
- Seed Funding — the round SAFEs typically bridge

</div>
