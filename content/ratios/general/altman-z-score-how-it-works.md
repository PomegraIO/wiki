---
title: "Altman Z-Score: How the Bankruptcy Prediction Model Works"
description: "The Altman Z-Score combines five weighted financial ratios to estimate bankruptcy risk. Learn how the model works, what its score zones mean, and why it still matters for credit analysis."
keywords:
  - altman z-score how it works
  - bankruptcy prediction model
  - z-score formula
  - financial distress model
  - insolvency prediction
image: /svg/ratios.svg
---

*The **Altman Z-Score** is a statistical model that synthesizes five weighted financial ratios into a single number, ranging from below 1 to above 3, to forecast the risk that a company will enter bankruptcy within two years. Developed by Edward Altman in 1968, it remains a textbook tool in credit analysis and equity research, though its accuracy depends on industry, accounting choices, and the economic cycle.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Altman Z-Score — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for ratios and financial metrics." />

<div class="wiki-infobox-caption">A weighted sum of five balance-sheet and income-statement ratios that flags financial distress.</div>

|   |   |
|---|---|
| **Formula** | Z = 1.2X₁ + 1.4X₂ + 3.3X₃ + 0.6X₄ + 1.0X₅ |
| **Safe zone** | Z > 2.99 (low bankruptcy risk) |
| **Gray zone** | 1.81 < Z < 2.99 (uncertain) |
| **Distress zone** | Z < 1.81 (high bankruptcy risk) |
| **Horizon** | Predicts failure within 2 years |
| **Original accuracy** | ~95% one year before bankruptcy |
| **Best for** | Manufacturing firms; auditors and lenders |

</aside>

## The Five Ratios and Their Weights

The Altman Z-Score pulls from two accounting statements: the balance sheet and the income statement. Each ratio measures a different financial health dimension—liquidity, profitability, leverage, solvency, and operational efficiency—and is assigned a weight based on statistical correlation with bankruptcy.

**X₁: Working Capital / Total Assets (weight 1.2)**

Working capital is current assets minus current liabilities, a measure of short-term liquidity. Dividing by total assets normalizes it for firm size. A negative working capital (current liabilities exceed current assets) signals near-term cash strain and often precedes failure. The 1.2 weight reflects how strongly negative working capital predicts distress.

**X₂: Retained Earnings / Total Assets (weight 1.4)**

[Retained earnings](/retained-earnings/) accumulated over the firm's lifetime show whether management has reinvested profits or faced steady losses. Mature, stable firms accumulate high retained earnings; young or chronically unprofitable firms show low values. The 1.4 weight is the model's highest, because retained earnings are a powerful cumulative signal of profitability history.

**X₃: EBIT / Total Assets (weight 3.3)**

[EBIT](/ebitda/) (earnings before interest and tax) divided by total assets is an operational profitability metric, independent of capital structure. A firm earning little EBIT relative to its asset base cannot service debt or fund operations from operations. The 3.3 weight reflects that this ratio alone is highly predictive of distress.

**X₄: Market Value of Equity / Book Value of Total Liabilities (weight 0.6)**

This ratio compares what shareholders believe the firm is worth (market cap) to the accounting value of what it owes. A high ratio (market value >> liability book value) signals confidence. A low ratio or declining market cap warns of deteriorating equity value relative to debt claims. The 0.6 weight is low because equity markets are volatile; the ratio is useful but less stable than accounting ratios.

**X₅: Sales / Total Assets (weight 1.0)**

Asset turnover—revenue divided by total assets—measures how efficiently a firm deploys its asset base to generate sales. Low turnover suggests underutilized assets, poor pricing power, or stagnating demand. The 1.0 weight treats it as a secondary indicator, less diagnostic than profitability or liquidity alone.

## How to Calculate the Score

Gather the most recent annual [balance sheet](/balance-sheet/) and [income statement](/income-statement/) (10-K for US public companies). Extract or compute:

- Current assets, current liabilities, total assets, total liabilities (from balance sheet)
- Retained earnings, EBIT, net sales (from balance sheet and income statement)
- Market capitalization (stock price × shares outstanding)

Then plug into:

**Z = 1.2 × (Current Assets − Current Liabilities) / Total Assets**
**+ 1.4 × Retained Earnings / Total Assets**
**+ 3.3 × EBIT / Total Assets**
**+ 0.6 × Market Cap / Total Liabilities**
**+ 1.0 × Sales / Total Assets**

For example, a manufacturer with $100M in assets, $80M in liabilities, $20M in annual EBIT, $40M in retained earnings, $200M in sales, $30M in current assets, $15M in current liabilities, and a $300M market cap would score:

Z = 1.2 × (15/100) + 1.4 × (40/100) + 3.3 × (20/100) + 0.6 × (300/80) + 1.0 × (200/100)
Z = 0.18 + 0.56 + 0.66 + 2.25 + 2.00 = 5.65

A score of 5.65 is well above 2.99, indicating low bankruptcy risk.

## The Three Zones

The original model defined two critical thresholds, establishing three regions:

**Safe Zone (Z > 2.99):** The firm is unlikely to file for bankruptcy within two years. Management can focus on growth and shareholder returns with minimal solvency risk. Lenders and investors treat the firm as creditworthy.

**Gray Zone (1.81 < Z < 2.99):** The model is ambiguous. The firm is not yet in acute distress, but warning signs are present. Leverage may be rising, profitability slowing, or working capital tightening. Close monitoring is warranted, and changes to other metrics matter. Lending spreads widen; equity valuations become more sensitive to earnings misses.

**Distress Zone (Z < 1.81):** The model flags high bankruptcy risk. The combination of low profitability, weak liquidity, or high leverage creates a fragile position. The firm may survive if conditions improve rapidly, but absent a turnaround, insolvency becomes likely. Lenders demand higher rates or collateral; equity investors demand steep discounts or avoid the stock.

## Historical Accuracy and Known Gaps

Altman's original 1968 study showed ~95% accuracy in identifying firms that would fail within one year and ~83% within two years. This impressive track record propelled the model into textbooks and credit practice. However, subsequent research has documented substantial limitations.

The model was calibrated on industrial manufacturers in the 1960s. It performs best on traditional manufacturing firms with visible assets, long operating histories, and straightforward capital structures. It performs poorly on banks, insurance companies, utilities, and other regulated industries—these sectors have different balance-sheet structures and regulatory constraints that the model does not account for.

High-growth tech and biotech firms often appear distressed by the Z-Score (low earnings, high cash burn) yet survive for years if they have adequate cash or access to capital. The model penalizes investment-phase firms and misses market-driven solvency. Conversely, firms with high retained earnings and low EBIT can appear safer than they are if they face sudden demand collapse.

The gray zone is genuinely ambiguous; many firms score between 1.81 and 2.99 and never fail. Altman himself acknowledged that the zone reflects genuine uncertainty and should prompt deeper analysis, not a pass/fail judgment.

## Modern Variants and Adjustments

Over decades, researchers and practitioners have tweaked the model. Altman himself published a revised formula for non-manufacturing and private firms. A common adjustment for private firms substitutes book value of equity for market capitalization, since market prices are unavailable. Some analysts weight X₄ differently or drop it entirely for private-company analysis.

Others add industry-specific variables—cash-flow margins for retailers, loan-loss provisions for banks—to the baseline five ratios. These variants can improve accuracy within a narrow sector but reduce the model's generality.

The Altman Z-Score is best used as one input among several. Combine it with [debt-to-equity](/debt-to-equity-ratio/) analysis, [interest coverage](/interest-coverage-ratio/) ratios, cash-flow metrics, and industry-specific stress factors. A declining Z-Score trend often matters more than a single year's score; watch for deterioration in working capital, eroding profitability, or rising leverage.

## When and Why It Still Matters

Credit officers and auditors still use the Z-Score to flag portfolio risk, allocate review resources, and document due diligence. Private equity firms use it as a screening tool before acquiring distressed assets. Distressed-debt investors track Z-Scores across portfolios to time entry and exit points.

The model endures because it is transparent, reproducible from public data, and captures the fundamental trade-offs between liquidity, profitability, and leverage. Its limitations are well understood, and users who stay within its boundaries—manufacturing firms with at least a few years of history—still find it valuable. The key is treating it as a diagnostic pointer, not prophecy.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Coverage Ratio](/interest-coverage-ratio/) — A direct measure of debt service ability; complements the Z-Score's leverage signals
- Working Capital — The short-term liquidity component of the Z-Score
- [Debt-to-Equity Ratio](/debt-to-equity-ratio/) — Another leverage metric used to assess solvency alongside the Z-Score
- [EBIT](/ebitda/) — The operational profit measure embedded in the Z-Score
- [Return on Assets](/return-on-assets/) — A profitability ratio that helps contextualize the Z-Score's EBIT component

### Wider context

- [Credit Rating](/credit-rating/) — How ratings agencies assess default risk, with similar but more complex methodologies
- Financial Distress — The broader concept the Z-Score attempts to predict
- [Balance Sheet](/balance-sheet/) — The source document for most Z-Score inputs
- [Income Statement](/income-statement/) — Where EBIT and sales figures come from

</div>
