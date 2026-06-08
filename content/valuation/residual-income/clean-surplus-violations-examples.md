---
title: "Clean Surplus Violations: Common Examples and Adjustments"
description: "How to identify and adjust for clean surplus violations—OCI, stock buybacks, and direct equity charges—in residual income models."
keywords:
  - clean surplus violations examples
  - other comprehensive income accounting
  - residual income model adjustments
  - comprehensive income clean surplus
image: /svg/valuation.svg
---

*The **clean surplus assumption**—the foundation of residual income valuation—assumes that all changes in book equity flow through net income. But items charged directly to equity, such as **other comprehensive income (OCI)**, unrealized gains, and stock-based compensation, violate this principle. Understanding which items break clean surplus and how to adjust comprehensive income in your model is essential to avoid systematically overvaluing or undervaluing a firm.*

Residual income models rely on the clean surplus relation: book equity at the end of the period equals book equity at the start, plus net income, minus dividends. In symbols: BV(t) = BV(t-1) + NI(t) − D(t). The beauty of this formula is that it isolates the "excess return"—residual income—that the firm earns above its cost of equity. But if items bypass the income statement and hit equity directly, the clean surplus assumption fails, and your valuation becomes unreliable.

<div class="wiki-hatnote">

For a technical primer on residual income models themselves, see [residual income valuation](/residual-income-valuation/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clean Surplus Violations — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">OCI, buybacks, and direct charges break the clean surplus link between equity and earnings.</div>

|   |   |
|---|---|
| **Primary culprit** | Other comprehensive income (OCI): FX translation, actuarial gains/losses, available-for-sale securities |
| **Second major source** | Treasury stock (share buybacks) and direct equity charges |
| **The fix** | Adjust book equity forward and/or reframe NI as comprehensive income |
| **Key metric affected** | Residual income and [return on equity](/return-on-equity/) |
| **Impact on valuation** | Undervalues if you ignore positive OCI; overvalues if you ignore negative OCI |
| **Analyst approach** | Use comprehensive income instead of net income in forecasts, or manually add/subtract OCI |

</aside>

## The Clean Surplus Relation and Why It Breaks

The clean surplus relation is elegant precisely because it ties all equity changes to earnings:

**BV(t) = BV(t-1) + NI(t) − Dividends(t)**

Under this assumption, the only way book value grows is if you earn more than you distribute. This allows you to forecast equity growth directly from net income forecasts, and it ensures that your residual income (defined as NI minus cost of equity times beginning book value) captures true economic value creation above the hurdle rate.

But **under [GAAP and IFRS](/generally-accepted-accounting-principles/)**, not all equity changes flow through net income. Items recorded in **other comprehensive income** bypass the income statement:

- Unrealized gains or losses on available-for-sale securities
- Foreign currency translation adjustments
- Actuarial gains and losses on pension obligations
- Cash flow hedging derivatives
- Revaluation surpluses (IFRS only)

These hit the balance sheet directly, widening or narrowing equity, but they don't appear in net income. The result: your clean surplus assumption breaks. Book value can change by a significant amount that has nothing to do with net income, which means your residual income calculation will be wrong.

## Common Examples of Violations

### Foreign Currency Translation Adjustments (FX OCI)

A multinational firm with a subsidiary in Japan holds yen-denominated assets and liabilities. When the dollar strengthens against the yen, the subsidiary's equity, when translated back to the parent's reporting currency, declines. Under [IFRS](/international-financial-reporting-standards/) and U.S. GAAP, this loss is recorded in OCI, not in net income.

**Impact**: A Japanese subsidiary might report stable local profitability (positive yen-denominated net income), but the parent's consolidated equity shrinks due to FX translation losses in OCI. If you forecast net income growth and ignore OCI, you'll overestimate future book equity, leading to overstated residual income and overvaluation.

**Adjustment**: Either (a) forecast comprehensive income (net income plus OCI) instead of net income, or (b) separately track OCI items and adjust book equity manually.

### Available-for-Sale (AFS) Securities

A bank or insurance company holds a bond portfolio marked to market. As interest rates rise, the market value of the bonds falls. Under GAAP, unrealized losses on AFS securities flow through OCI, not net income.

**Impact**: If the company's book equity includes AFS assets, rising rates will shrink both the assets and equity via OCI, even if net income is unchanged. Your residual income model will miss this loss of economic value if you use net income only.

**Adjustment**: Use comprehensive income, which includes the AFS loss. Alternatively, if you're forecasting long-term residual income, decide whether unrealized mark-to-market swings are persistent or temporary; if temporary, you might smooth them.

### Pension and Actuarial Gains/Losses

A company with a defined-benefit pension plan is exposed to actuarial volatility. If discount rates fall, the present value of future pension liabilities rises, creating an actuarial loss. Under GAAP, these losses can be recorded in OCI (or amortized through net income over time, depending on the accounting policy).

**Impact**: A profitable company with a large pension deficit can see its book equity swing wildly based on interest rates, irrespective of operational performance. Net income stays stable while OCI causes the equity base to fluctuate.

**Adjustment**: Forecast comprehensive income, or separately adjust for expected long-term pension contributions (which do flow through cash). Many analysts exclude actuarial volatility as not representative of recurring economic returns.

### Share Buybacks and Treasury Stock

When a company repurchases its own shares, the transaction reduces equity directly. The shares are held as treasury stock on the balance sheet and reduce shareholders' equity. This is a dividend in substance—the company is returning cash to equity holders—but it bypasses net income.

**Impact**: If you forecast net income and dividends but don't account for buybacks, you'll overestimate book equity growth. A company that buys back $500M in shares has reduced equity by $500M, even though net income is unchanged. Residual income will then be overstated because you're applying the cost of equity to a book value that's too high.

**Adjustment**: Treat buybacks as a form of dividend. Either (a) include them explicitly in the clean surplus formula: BV(t) = BV(t-1) + NI(t) − Cash Dividends − Buybacks, or (b) use shares outstanding to adjust your EPS forecast (since buybacks reduce the share count, EPS can grow even if net income is flat).

### Direct Equity Charges (Goodwill Impairments, Restructuring)

Under certain accounting rules, companies may write down goodwill or other intangibles directly against equity, rather than through the income statement. Similarly, some restructuring charges or write-downs may bypass the P&L under specific GAAP rules.

**Impact**: A firm's book value can drop sharply without a matching hit to net income, violating clean surplus.

**Adjustment**: Identify these charges and adjust the opening book value forward to reflect the actual equity base available for valuation.

## How to Adjust Your Residual Income Model

### Method 1: Use Comprehensive Income Instead of Net Income

The simplest fix is to replace net income with **comprehensive income** (net income plus OCI). This ensures that all equity changes flow through your valuation:

**BV(t) = BV(t-1) + Comprehensive Income(t) − Dividends − Buybacks**

You then calculate residual income as:

**RI(t) = Comprehensive Income(t) − [Cost of Equity × BV(t-1)]**

This ensures clean surplus is restored and your model captures all economic gains and losses.

**Pros**: Mechanically sound and complete.  
**Cons**: OCI is noisy and often temporary (e.g., FX swings). If you use raw comprehensive income, you might embed transient losses or gains into your terminal value, distorting valuation.

### Method 2: Adjust Book Equity and Keep Net Income

Separately forecast net income and identify the clean surplus violations. Adjust book equity year by year to reflect OCI:

**BV(t) = BV(t-1) + NI(t) + OCI(t) − Dividends − Buybacks**

Then use net income for residual income, but updated BV:

**RI(t) = NI(t) − [Cost of Equity × BV(t-1)]**

This is cleaner if you believe OCI is temporary or if you want to forecast its drivers explicitly (e.g., FX headwinds, pension adjustments) separately from operating performance.

**Pros**: Lets you control OCI assumptions and distinguish operating returns from accounting adjustments.  
**Cons**: Requires more granular forecasting and judgment about persistence.

### Method 3: Manual Scrubbing

For a one-time valuation, you might manually reconstruct the clean surplus relation using unsmoothed data. Pull the actual balance sheet changes, decompose them into income, dividends, and direct equity changes, and reverse-engineer the clean surplus base.

**Pros**: Maximum transparency and control.  
**Cons**: Labor-intensive and requires deep balance-sheet knowledge.

## Example: A Simple Adjustment

Suppose Company X reports:

- Year 1 net income: $100M
- Year 1 OCI: +$20M (unrealized gains on AFS securities)
- Year 1 dividends: $30M
- Year 1 buybacks: $10M
- Beginning book equity: $1,000M
- Cost of equity: 10%

**Under dirty surplus (ignoring OCI)**:  
BV(1) = $1,000 + $100 − $30 − $10 = $1,060M  
RI(1) = $100 − (10% × $1,000) = $0M (no excess return)

**Under clean surplus (including OCI)**:  
BV(1) = $1,000 + $100 + $20 − $30 − $10 = $1,080M  
RI(1) = $120 − (10% × $1,000) = $20M (excess return recognized)

The difference in residual income ($0M vs. $20M) compounds over the forecast horizon and can materially affect valuation.

## Red Flags for Clean Surplus Violations

- **Foreign currency volatility**: Firms with significant offshore operations and volatile FX should trigger OCI scrutiny.
- **Large pension obligations**: Check the footnotes for actuarial gains/losses.
- **Active buyback programs**: These reduce equity outside net income.
- **Trading or available-for-sale securities**: Banks, insurers, and asset managers face this risk.
- **Goodwill and intangible write-downs**: Watch the equity section of the balance sheet.
- **Revaluations (IFRS firms)**: Non-U.S. companies may revalue property and intangibles directly to equity.

## Key Takeaway

The clean surplus assumption is powerful but fragile. If you ignore OCI, buybacks, and direct equity charges, your residual income model will misstate book value and, in turn, overvalue or undervalue the firm. The fix is mechanical: either use comprehensive income instead of net income, or manually adjust book equity for clean surplus violations. Either way, be explicit about the adjustments in your model documentation and reconciliation.

## See also

<div class="wiki-seealso">

### Closely related

- [Residual income valuation](/residual-income-valuation/) — The foundation for using clean surplus
- [Return on equity](/return-on-equity/) — Impacted by clean surplus violations
- [Comprehensive income](/comprehensive-income/) — Understanding OCI and total equity changes
- Book value — What clean surplus governs
- [Share buyback](/share-buyback/) — A direct equity charge outside net income
- Other comprehensive income — The chief source of violations

### Wider context

- [Accrual accounting](/accrual-accounting/) — Why comprehensive income exists
- [Balance sheet](/balance-sheet/) — Where violations appear
- [Generally accepted accounting principles](/generally-accepted-accounting-principles/) — Rules governing OCI classification

</div>
