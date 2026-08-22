---
title: "Loss Severity"
seo_title: "Loss Severity: How Much a Default Really Costs"
description: "Loss severity is the share of a defaulted loan balance lost after collateral recovery and costs. The formula, drivers, and role in structured credit."
---

*When a borrower defaults, the lender does not simply lose the entire loan balance. It seizes collateral, sells it, and recovers some proceeds. Loss severity measures the shortfall: if a $300,000 mortgage defaults and the house sells for $200,000 after foreclosure costs, loss severity is 33% ($100,000 loss ÷ $300,000 exposure). In structured credit, loss severity is one of the three drivers of expected credit losses and is critical to pricing and structuring securitizations.*

## The formula: loss severity in context

Expected loss on a pool of loans is: **Expected Loss = Probability of Default × Loss Severity × Exposure at Default**

If a mortgage pool has:
- PD = 1% (1% of mortgages default annually)
- Severity = 40% (40% of defaulted balance is lost)
- EAD = $300,000 (average balance)

Then expected loss per loan is 1% × 40% × $300,000 = $1,200.

Loss severity is often expressed as a percentage or as recovery rate (complement of severity). A 40% severity is equivalent to 60% recovery—the lender recovers 60% of the defaulted balance.

## Determining loss severity: historical data

Loss severity is estimated from historical default data. A bank looks at mortgages that defaulted in past years and calculates:

- Outstanding balance at time of default
- Sale price of the property (via foreclosure)
- Foreclosure costs (legal, realtor commissions, property maintenance, title insurance)
- Time to sale (carrying costs during foreclosure)
- Recovery, net of all costs

The net recovery as a percentage of outstanding balance is the recovery rate. Severity = 100% - Recovery Rate.

For example:
- Balance at default: $300,000
- Sale proceeds: $200,000
- Foreclosure costs: $20,000
- Recovery: $200,000 - $20,000 = $180,000
- Recovery rate: $180,000 ÷ $300,000 = 60%
- Severity: 40%

## Severity varies by asset class

Different collateral types have different severities due to repleability and time-to-recovery:

**Mortgages**: 30–60% severity
- Collateral (real estate) is relatively illiquid; foreclosure takes months.
- Carrying costs (taxes, insurance, maintenance) mount during foreclosure.
- Market conditions matter: in booming markets, severity is lower (properties sell quickly at good prices); in downturns, severity is higher.

**Auto loans**: 15–40% severity
- Cars are highly liquid; a repossessed car can be sold in days.
- Depreciation is rapid; a 3-year car repossessed after default has lost significant value.
- Condition and mileage affect recovery.

**Credit cards**: 70–100% severity
- No collateral to repossess; the default is an unsecured loss.
- Recovery is limited to collection agencies or legal judgments, which are slow and uncertain.
- Debtors often cannot be collected from (judgment-proof).

**Equipment leases**: 20–50% severity
- Equipment can be repossessed and remarketed quickly.
- Condition and technology obsolesce affect recovery.

## Factors affecting severity

**Loan-to-Value (LTV)**

For mortgages, LTV is a primary severity driver. A mortgage with 80% LTV (80% of property value financed) has lower severity than a 95% LTV mortgage. Why? If both default:

- 80% LTV, home worth $500K: balance $400K, sells for $400K (some foreclosure costs), recovery ~95%, severity ~5%.
- 95% LTV, home worth $500K: balance $475K, sells for $400K, recovery 84%, severity ~16%.

An originator models severity as a function of LTV. High-LTV loans have higher severity.

**Geographic concentration**

Local real-estate markets matter. In a strong market (like much of the post-2020s), homes sell quickly at prices near appraised value, recovery is high, severity is low. In weak markets (rust belt, post-employment decline), homes sit on the market, sell at discounts, severity is high.

Securitization deal documentation often breaks out severity by geography. A pool with 20% of mortgages in high-risk geographies might have higher overall severity.

**Time to resolution**

The longer foreclosure takes, the higher the costs. States with judicial foreclosures (requiring court approval, slower) have higher severities than non-judicial states. A 12-month foreclosure accumulates 12 months of property tax, insurance, maintenance, and carrying costs. An 18-month foreclosure accumulates more.

Post-2008, some states reformed foreclosure law to protect homeowners, slowing the process further. This increased severity.

**Economic conditions**

Severity is not constant; it varies with economic conditions. In recessions, home prices fall and foreclosures backlog, increasing severity. In booms, prices rise and foreclosures clear quickly, reducing severity.

Credit loss models account for this by stress-testing severity assumptions. A model might assume 40% severity in normal conditions but 60% severity in recession (home prices down 20%, higher carrying costs, slower sales).

## Recovery mechanisms

**Foreclosure sale**

For mortgages, the primary recovery path is foreclosure and sale of the property. The lender forecloses, takes title, and sells the home. Recovery = sale price minus selling costs.

**Deficiency judgment**

If the foreclosure sale does not recover the full balance, the lender might pursue a deficiency judgment against the borrower (in non-recourse states, this is not allowed). A judgment is difficult to enforce against a borrower who has already defaulted, so deficiency recovery is often minimal.

**Cure by the borrower**

A borrower in default might cure before foreclosure (pay the arrears and legal costs). This avoids foreclosure and recovery is 100%. The likelihood of cure depends on the borrower's equity (if underwater, unlikely to cure) and income recovery.

**Insurance and guarantees**

Some mortgages are insured (private mortgage insurance, or PMI). If a mortgage defaults and is underwater, PMI pays the lender. This reduces loss severity for the lender. Similarly, agency mortgages (Fannie Mae, Freddie Mac) are guaranteed; the agency makes whole, reducing severity to zero for investors.

## Adjusting severity assumptions

Securitizations disclose assumed severity, but investors often model different severities to stress-test structures:

- **Base case**: Originator's assumption (e.g., 40% severity for mortgages)
- **Conservative case**: Higher severity (e.g., 50%) to account for possible downturn
- **Stress case**: High severity (e.g., 60%) to model severe recession

An investor running stress scenarios finds: if severity hits 60% instead of 40%, how much of my tranche remains whole? If the answer is "only with 30% OC" and the deal has 15% OC, the investor demands a higher spread to compensate.

## Severity and negative equity

In securitizations, negative equity is a severity accelerator. A borrower with a $300,000 mortgage on a house worth $250,000 (underwater by $50,000) has lost equity and default incentive. If the borrower defaults:

- House sells for $200,000 (further decline)
- Foreclosure costs: $15,000
- Recovery: $200,000 - $15,000 = $185,000
- Loss: $300,000 - $185,000 = $115,000
- Severity: 38%

But the borrower also had no incentive to cure (underwater borrowers default and stay in foreclosure). Severity was higher than it would have been for an above-water borrower.

The 2008 crisis saw severity spike dramatically due to negative equity. Millions of borrowers became underwater, walking away from homes. Foreclosure sales depressed prices further. Severity estimates from 2006 (20–30%) were blown through by 2010–2012 (50%+ for subprime).

## Modeling and forecast uncertainty

Severity is estimated, not known. Different models, using different historical periods and assumptions, produce different forecasts. This uncertainty is embedded in securitization structures.

A conservatively structured deal assumes high severity (55–60% for mortgages). An aggressively structured deal might assume lower severity (30–35%), betting that the market will recover quickly if defaults occur.

Higher assumed severity requires higher credit support (more tranches, higher OC), making the deal harder to issue. Lower assumed severity allows lower support, making the deal easier to sell. But it also makes the deal riskier if actual severity exceeds forecast.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/probability-of-default/">Probability of Default</a> — the other main input to loss calculation.</li>
<li><a href="/wiki/exposure-at-default/">Exposure at Default</a> — the third input to loss calculation.</li>
<li><a href="/wiki/credit-loss-model/">Credit Loss Model</a> — models incorporate severity assumptions.</li>
<li><a href="/wiki/securitization/">Securitization</a> — severity drives tranche sizing.</li>
<li><a href="/wiki/mortgage-backed-security/">Mortgage-Backed Security</a> — MBS are especially sensitive to severity.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/credit-risk/">Credit Risk</a> — severity is a component of credit risk.</li>
<li><a href="/wiki/recovery-rate/">Recovery Rate</a> — the inverse of severity.</li>
<li><a href="/wiki/structured-finance/">Structured Finance</a> — severity assumptions underpin structures.</li>
</ul>
</div>
