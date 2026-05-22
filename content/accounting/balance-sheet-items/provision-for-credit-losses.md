---
title: "Provision for Credit Losses"
description: "An accounting reserve on a lender's balance sheet representing the estimated amount of loan defaults and write-offs expected in the future."
keywords:
  - credit loss
  - loan loss reserve
  - balance sheet
  - bank accounting
---

*A **Provision for Credit Losses** (PCL) is a line item on a bank's or financial institution's [balance sheet](/wiki/balance-sheet/) representing a reserve of cash or equity set aside to cover expected [loan defaults](/wiki/default-rate/), [charge-offs](/wiki/charge-off/), and other credit losses. It is an accounting estimate of future losses built from historical loss rates and forward-looking economic assumptions.*

<aside class="wiki-infobox">

| Key Fact | Detail |
|---|---|
| **Purpose** | Reserve for expected future loan defaults |
| **Accounting method** | Current IFRS 9 / CECL (expected-loss model) |
| **Timing** | Recognized when loan is originated, adjusted annually |
| **Driver of volatility** | Changes in economic outlook and loss assumptions |
| **P&L impact** | Increases when losses expected to rise; releases credit the reserve when losses are better than forecast |
| **Regulatory minimum** | Basel III requires [capital adequacy](/wiki/capital-adequacy/) rules that are informed by credit losses |

</aside>

## Why lenders must estimate future losses

A bank originates a $500 million [loan portfolio](/wiki/credit-risk/) on January 1. By December 31, some loans will have defaulted; others will be recovered partially. The bank must recognize the *expected* cost of these losses in its annual financial statements, not just the losses that have actually occurred.

Under the old "incurred loss" model (used until 2020 in most jurisdictions), a bank recognized a credit loss only when a borrower actually defaulted. This created a pro-cyclical bias: during a boom, loan losses looked small because defaults hadn't yet happened; the reserve was inadequate. When recession arrived and defaults spiked, the reserve had to be built up suddenly, amplifying the earnings shock and tightening [capital](/wiki/tier-1-capital/) availability just when the economy needed credit most.

The new **expected credit loss** model (IFRS 9 in most of the world, the [Current Expected Credit Loss](/wiki/credit-loss-model/) standard in the US) flips this. A bank must estimate losses the moment a loan is made, based on historical [default rates](/wiki/default-rate/), borrower [credit ratings](/wiki/credit-rating/), and the economic outlook. This reserve is built gradually over the life of the loan, smoothing earnings and maintaining capital buffers before a crisis hits.

## How PCL is calculated

The provision is the sum of three components:

1. **Stage 1 (performing loans):** Expected losses over the next 12 months, based on the borrower's current credit rating and historical loss rates for that rating cohort.

2. **Stage 2 (loans showing signs of stress):** Expected losses over the remaining life of the loan if the borrower has experienced a significant increase in credit risk since origination, even if no payment is yet overdue.

3. **Stage 3 (credit-impaired loans):** Expected losses on loans where a borrower is in default or where loss is probable.

For a typical $10 million corporate loan to a BBB-rated borrower:

- Stage 1: 0.15% × $10M = $15,000 (1-year expected loss)
- Stage 2: 2% × $10M = $200,000 (if credit metrics deteriorate mid-loan)
- Stage 3: 50% × $10M = $5 million (if borrower defaults)

The bank adds these to the balance sheet as a debit to its [income statement](/wiki/income-statement/) ("provision expense") and a credit to the liability account ("allowance for credit losses").

## Linking PCL to economic assumptions

The second key driver of PCL after loss rates is the **economic outlook**. During a strong economy, even Stage 1 loans carry lower expected losses because default rates are historically low. During a recession forecast, the bank must increase the provision because historical loss data from past downturns suggests higher loss rates.

A bank might increase its macroeconomic assumptions (e.g., "unemployment will hit 7% in 2025" or "commercial real estate cap rates will spike 200 basis points") and re-estimate its portfolio's [expected loss](/wiki/expected-loss-model/) accordingly. This forward-looking component is the source of most provision volatility. A bank with good data and stable economic assumptions will show a stable PCL as a percentage of loans. A bank that suddenly increases the provision suggests management is bracing for economic deterioration.

## PCL on the balance sheet

The provision is shown net of loans, as an "allowance for credit losses" contra-account:

**Balance Sheet excerpt:**

```
Loans and advances to customers:        $50 billion
Less: Allowance for credit losses:      $900 million
Net loans and advances:                 $49.1 billion
```

A $100 million default on a Stage 3 loan that was fully provisioned reduces the allowance and the gross loans by equal amounts; net loans are unaffected. But if a default exceeds the provision (e.g., a $150 million loss on a $100 million provision), the excess flows through the [income statement](/wiki/income-statement/) as a charge and reduces equity.

The allowance is not cash—it is a [deferred tax asset](/wiki/deferred-tax-asset/) or equity reserve. When a loan actually defaults, the bank writes off the loan amount against the allowance, reducing both gross loans and the reserve. This is why the allowance must be calibrated correctly: if it is too small, actual losses will wipe out earnings; if it is too large, the bank is holding capital it could deploy.

## Regulatory capital and PCL

Regulators, especially under [Basel III](/wiki/basel-iii/), tie [capital adequacy](/wiki/capital-adequacy/) requirements to PCL. A bank with a larger allowance is implicitly holding more capital against credit risk, improving its [capital ratios](/wiki/tier-1-capital/). During the 2008 financial crisis, banks with inadequate provisions were forced to raise capital or cut lending precisely when the economy was weakest. Modern PCL standards aim to prevent that by requiring earlier, larger provisions during good times.

<div class="wiki-seealso">

### Closely related
- [Expected Loss Model](/wiki/expected-loss-model/) — The three-stage calculation of credit losses
- [Charge-Off](/wiki/charge-off/) — When a loan is finally written off the books
- [Credit Risk](/wiki/credit-risk/) — The underlying risk that PCL measures
- [Credit Rating](/wiki/credit-rating/) — The credit score used to estimate loss rates

### Wider context
- [Balance Sheet](/wiki/balance-sheet/) — The financial statement where PCL appears
- [Capital Adequacy](/wiki/capital-adequacy/) — Regulatory capital rules informed by credit losses
- [Basel III](/wiki/basel-iii/) — International standards governing bank credit provisioning
- [Income Statement](/wiki/income-statement/) — Provision expense flows through P&L

</div>
