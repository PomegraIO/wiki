---
title: "Return on Capital Employed vs ROIC"
description: "ROCE vs ROIC: both measure profit per dollar of capital invested, but differ in how capital is defined. Learn when to use each metric and how definitions affect results."
keywords:
  - roce vs roic
  - return on capital employed
  - return on invested capital
  - roic definition
  - roce definition
  - capital efficiency
image: "/svg/ratios.svg"
---

*Return on Capital Employed (ROCE) and Return on Invested Capital (ROIC) are often used interchangeably, but they measure slightly different things: both divide profit by capital invested, but the definitions of "capital" and "profit" shift between them. The choice of metric can materially change the result and what story it tells about capital efficiency.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ROCE vs ROIC — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two cousins of capital efficiency; same family, different denominator.</div>

|   |   |
|---|---|
| **ROCE** | EBIT ÷ (Equity + Net Debt); capital employed is book value-based |
| **ROIC** | NOPAT ÷ (Equity + Net Debt); adjusts profit for taxes and capital structure |
| **Capital base** | Both include equity and debt; definitions of "invested capital" differ |
| **Key difference** | ROIC often adds back items excluded from equity (deferred taxes, R&D capitalization) |
| **When ROCE > ROIC** | Operating income is high but not adjusted for tax burden or non-operating items |
| **Use case** | ROCE: quick screening; ROIC: deeper analysis of true after-tax capital returns |

</aside>

## The core tension: definitions of capital and profit

Both ROCE and ROIC answer the same question: *How much profit does the company generate per dollar of capital deployed?* A company returning 15% on capital is more efficient than one returning 10%, all else equal. The metrics diverge because "capital" and "profit" can be defined multiple ways, and different analysts choose differently.

**ROCE (Return on Capital Employed)** typically uses a simpler formula:

ROCE = EBIT / (Equity + Net Debt)

**ROIC (Return on Invested Capital)** uses an after-tax version:

ROIC = NOPAT / (Equity + Net Debt)

Where NOPAT is Net Operating Profit After Tax. The denominator—capital employed—is often similar between the two, but the numerator changes: ROIC adjusts operating profit for the actual tax burden, whereas ROCE uses the raw [EBIT](/ebit-margin-vs-ebitda-margin/).

## Why the after-tax adjustment matters

The conceptual purpose of ROIC is to measure the *after-tax* return on capital, since that is what is actually available to reinvest or distribute. A company earning 20% EBIT return looks impressive until you realize the statutory tax rate is 35%; the after-tax return available to capital providers is closer to 13%.

ROCE, by contrast, ignores taxes entirely. It asks: *What profit did operations generate, before any claims by the government?* That can be useful for comparing companies across jurisdictions with different tax rates, but it does not reflect the true economic return to the company's owners and lenders.

Consider a manufacturing company with $100 million in EBIT and $500 million in capital employed. Its ROCE is 20%. If the effective tax rate is 25%, its NOPAT is $75 million, and its ROIC is 15%. Both numbers are correct; they answer different questions. ROIC tells you what is left after taxes. ROCE tells you what operations generated before taxes.

## Denominator variation: what counts as "capital employed"

The simple formula—capital employed = equity + net debt—is a starting point. But sophisticated analysts adjust it:

**Lease obligations.** Operating leases are now capitalized under [ASC 606](/asc-606/) accounting, but some analysts add lease obligations to capital even if they are off-balance-sheet in older reports, to compare companies with different financing structures.

**Deferred tax liabilities and assets.** Some ROIC frameworks add deferred tax liabilities to the denominator (capital that the tax system is essentially funding) and exclude deferred tax assets (unrealized tax shields). Others exclude both and use only balance-sheet equity and interest-bearing debt.

**Goodwill and intangible assets.** A company that grew through acquisition carries goodwill on its balance sheet; one that grew organically does not. Including or excluding goodwill changes the capital base. Some analysts exclude goodwill to isolate returns on *tangible* capital; others include it because it represents actual cash paid for capital assets (even if that asset is a customer list or brand).

**Capitalized R&D.** The balance sheet expenses R&D, even though it is an investment. Some analysts capitalize a portion of R&D and add it to the capital base, to show the true capital tied up in innovation. This is especially important in pharma and software.

**Working capital.** Some frameworks include [accounts receivable](/accounts-receivable/) and inventory in capital employed (money tied up in operations); others focus only on long-term capital (equity and long-term debt).

These variations are not errors; they reflect different purposes. If you are comparing two manufacturing companies head-to-head, standardizing treatment of lease obligations and goodwill is essential. If you are analyzing whether a company is destroying or creating shareholder value over time, capitalizing R&D and excluding non-operating items may be appropriate.

## When ROCE is higher than ROIC

ROCE typically exceeds ROIC because it is not adjusted for taxes. The higher the tax rate, the greater the gap. A company with a 25% ROCE and a 35% tax rate will have an ROIC around 16%. The two metrics are consistent; ROIC is just the after-tax version.

But gap patterns can reveal anomalies:

- **Very low tax rates.** If a company's ROCE and ROIC are nearly identical, it may be enjoying a low effective tax rate—either through tax credits, loss carryforwards, or jurisdiction arbitrage. That is material to long-term returns because it is often temporary.

- **Deferred tax adjustments.** If ROIC significantly exceeds ROCE, the analyst may be adding back deferred tax items in the capital base or numerator in ways that inflate returns. This is a sign to scrutinize the framework.

- **Non-operating items in EBIT.** EBIT sometimes includes one-time gains or unusual items that are not sustainable operating profit. ROIC frameworks that use NOPAT often exclude these, so the metric is more conservative.

## Practical use: when to use each metric

**Use ROCE for quick screening.** If you want a fast, balance-sheet-based measure of how efficiently a company is deploying capital without getting lost in tax adjustments and accounting nitpicks, ROCE works. It is especially useful when comparing companies in the same jurisdiction (so tax rates are similar) or when tax rates are transparent and stable.

**Use ROIC for detailed analysis.** If you are building a [discounted cash flow](/discounted-cash-flow-valuation/) model, evaluating acquisition targets, or comparing companies across tax jurisdictions, ROIC is more rigorous. It adjusts for the tax friction that materially affects real returns.

**Use both.** Many analysts calculate both ROCE and ROIC and look at the gap as diagnostic. A stable, predictable gap (driven by a consistent tax rate) is reassuring. A widening gap or an unexpectedly large gap signals something worth investigating.

## The relationship to other profitability metrics

ROIC and ROCE sit atop the hierarchy of profitability metrics. They are more holistic than [EBIT margin](/ebit-margin-vs-ebitda-margin/) or [operating margin](/negative-operating-margin-meaning/) because they account for capital efficiency, not just profit margin. A company with a 5% operating margin but a 20% ROIC is using capital very efficiently; one with a 20% operating margin but a 10% ROIC is tying up excessive capital per dollar of profit.

For this reason, ROIC and ROCE are favored by value investors and capital allocators. They answer the question: *Is management deploying capital at a return above the company's cost of capital?* If ROIC exceeds the [cost of equity](/cost-of-equity/) and cost of debt, the company is creating value. If it is below, capital is being destroyed, even if the company is profitable on a [net income](/income-statement/) basis.

## Limitations of both metrics

Neither metric is perfect.

- **Backward-looking balance sheets.** Capital employed is often measured at book value, which does not reflect the actual economic value of assets. A company with valuable real estate or brand may have far more economic capital than the balance sheet suggests.
- **Accounting conservatism and aggression.** Capitalization policies vary. One company expenses R&D; another capitalizes it. Comparisons require normalization.
- **Temporary tax effects.** A low effective tax rate one year (from loss carryforwards or discrete items) inflates ROIC temporarily.
- **Capital intensity obscured.** Two companies with identical ROIC may have very different capital structures. One might be asset-light with leverage; the other might be capital-intensive with conservative debt. The metric does not distinguish.

The metrics are most useful as a **trend analysis tool** within a company and as a **screening tool** across peers in the same industry and capital structure, after normalizing for accounting differences.

## See also

<div class="wiki-seealso">

### Closely related

- [EBIT Margin vs EBITDA Margin](/ebit-margin-vs-ebitda-margin/) — operating profit metrics that feed into ROCE and ROIC
- [Negative Operating Margin Explained](/negative-operating-margin-meaning/) — when ROIC is negative due to operating losses
- [Gross Profit Per Employee](/gross-profit-per-employee/) — workforce capital efficiency, complementary metric
- [Cost of Equity](/cost-of-equity/) — the hurdle rate that ROIC is compared against
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — ROIC informs long-term value creation models

### Wider context

- [Return on Equity](/return-on-equity/) — related metric focused on shareholder equity only
- [Return on Assets](/return-on-assets/) — similar concept applied to total assets
- [Debt-to-Equity Ratio](/debt-to-equity-ratio/) — capital structure affects the denominator
- [Cost of Debt](/cost-of-debt/) — weights the debt portion of capital cost
- [Capital-Asset-Pricing-Model](/capital-asset-pricing-model/) — framework for determining required return on capital

</div>
