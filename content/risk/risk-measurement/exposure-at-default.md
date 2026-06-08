---
title: "Exposure at Default"
description: "The outstanding credit exposure when a counterparty defaults; a critical input for assessing credit risk and regulatory capital."
keywords:
  - credit exposure
  - counterparty default
  - credit risk
  - capital requirement
  - loss severity
image: /svg/risk.svg
---

*The **exposure at default (EAD)** is the total value of assets or obligations a lender or investor stands to lose if a counterparty defaults at a specific moment. It measures the outstanding exposure—whether a loan balance, derivative position, or facility commitment—at the precise time of default, not before or after.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Exposure at Default — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for credit and financial exposure." />

<div class="wiki-infobox-caption">The dollar amount at risk the moment a counterparty fails to pay.</div>

|   |   |
|---|---|
| **What it is** | The outstanding credit exposure at the moment of default |
| **Also called** | EAD, amount at risk |
| **Key input for** | [Credit risk](/credit-risk/) models, regulatory [capital adequacy](/capital-adequacy/) calculations, loan loss reserves |
| **Timing** | Measured at the instant of default, not at origination or maturity |
| **Formula component** | Expected Loss = EAD × [Loss Given Default](/credit-risk/) × Probability of Default |
| **Regulatory use** | Basel III capital framework, Dodd-Frank stress tests, CCR models |

</aside>

## Why EAD matters more than the original loan amount

A loan's EAD is not simply its original principal. If a borrower has already repaid $200,000 of a $500,000 loan, the EAD is closer to $300,000—the amount actually exposed when default occurs. For [derivatives](/credit-risk/), the calculation is trickier: a currency swap with negative market value to the counterparty has lower EAD; the same swap with positive value carries higher EAD, because only the market-to-market cost of replacement matters at default.

This forward-looking aspect makes EAD volatile. Banks must estimate what their exposure will be on any given future date, not just today. A borrower with a $5 million revolving credit facility might have drawn only $1 million now—so current EAD is $1 million—but could draw another $4 million tomorrow, raising EAD to $5 million. Prudent risk management and regulatory [capital](/capital-adequacy/) frameworks require assumptions about how much additional debt borrowers will draw before defaulting.

## How EAD feeds into loss calculations

The legal foundation of credit risk is deceptively simple: **Expected Loss = EAD × Probability of Default × Loss Given Default**. All three factors matter equally. A high-EAD exposure to a creditworthy counterparty can still produce material loss if [loss given default](/credit-risk/) is severe (low recovery). Conversely, a small EAD to a risky obligor may be acceptable because the total loss is capped by size.

Banks and institutional investors use this framework to allocate capital, set [pricing](/credit-risk/), and reserve for losses. Regulatory bodies use it to enforce minimum [capital](/capital-adequacy/) levels: riskier exposures require more capital. The formula becomes powerful when applied across a portfolio: if a bank can estimate EAD for every counterparty and facility, aggregate expected loss, and measure the tail risk (worst-case loss in a market stress), it can price credit risk rationally and stay solvent.

## Estimating EAD for different instruments

For a vanilla amortising loan, EAD declines predictably as the borrower repays. For a [bond](/bond/), EAD is par value plus accrued coupons. But [derivatives](/credit-risk/) and [off-balance-sheet](/credit-risk/) commitments are harder. Banks must model future market movements and borrower behaviour.

A [floating-rate bond](/bond/) will fluctuate in value with interest rates. If rates fall, the bond's market value rises, raising EAD. If rates rise, the bond's value falls, lowering EAD. A [currency swap](/credit-risk/) depends entirely on whether the counterparty owes the bank money (positive exposure) or the bank owes them (zero exposure). Banks use historical volatility and correlation assumptions to model the distribution of future exposures across their derivative portfolios, a practice called *potential future exposure* (PFE).

Undrawn [credit facilities](/credit-risk/)—amounts the borrower can draw but hasn't yet—are trickier. A bank must estimate the *credit conversion factor* (CCF), the fraction of the undrawn amount likely to be drawn before default. If a $10 million facility has a CCF of 75%, the EAD is $7.5 million. In practice, CCFs vary by facility type: working capital lines have higher CCFs than unused mortgage commitments, because borrowers in distress draw more on overdrafts.

## Regulatory and portfolio implications

Under Basel III, banks must calculate EAD for every significant exposure and sum these across their portfolio to determine minimum required capital. This makes EAD estimation not just a risk-management exercise but a regulatory compliance function. Regulators publish guidance on CCFs for different asset classes, but banks' internal models can be more granular.

EAD is also central to stress testing. In a recession or financial crisis, EAD often spikes: borrowers draw on committed facilities, mark-to-market losses on derivatives widen, and new defaults occur at higher underlying EAD. A bank that modelled EAD as static—never growing or shrinking—would be caught flat-footed. The [Dodd-Frank Act](/dodd-frank-act/) requires banks to model EAD sensitivity to macroeconomic scenarios, so regulators can assess whether banks retain enough capital to survive a severe downturn.

Portfolio managers also use EAD to track [concentration risk](/concentration-risk/). If one client represents 30% of the bank's total credit exposure, the institution faces idiosyncratic risk. Stress-testing that concentration—what if that client's default occurred during a market downturn?—requires careful EAD projection.

## The gap between expected and realized EAD

Theory and practice often diverge. When a counterparty enters financial distress, it may stop drawing on committed facilities (EAD falls) or accelerate draws (EAD rises). In the 2008 financial crisis, some borrowers drew fully on backup credit lines precisely when banks were weakest and most exposed. Meanwhile, mark-to-market exposure on derivatives can swing wildly. A bank hedged to a seemingly low EAD can find that hedge counterparties themselves default, wiping out the protection.

This mismatch is called *wrong-way risk*: when the counterparty's probability of default rises precisely as EAD to that counterparty increases. A bank with heavy exposure to a distressed firm's [bonds](/bond/) faces wrong-way risk if the bond value (EAD) rises as the firm weakens—because market pricing reflects default probability. Good risk governance distinguishes EAD estimated in normal times from EAD in stress scenarios, and stress-tests the gap.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit risk](/credit-risk/) — the probability and severity of loss from a counterparty default
- [Loss given default](/credit-risk/) — the fraction of EAD not recovered after default
- [Capital adequacy](/capital-adequacy/) — minimum capital required by regulators, scaled by EAD
- [Backtesting VaR](/backtesting-var/) — validating risk models against realized outcomes
- [Counterparty risk](/counterparty-risk/) — the risk that a derivative or lending counterparty defaults
- [Concentration risk](/concentration-risk/) — excessive exposure to one counterparty or sector
- [Credit spread](/credit-spread/) — the yield premium compensating for credit risk

### Wider context

- [Dodd-Frank Act](/dodd-frank-act/) — U.S. regulation imposing stricter capital and stress-testing rules
- [Basel III](/capital-adequacy/) — international standard for bank capital adequacy
- [Expected loss](/credit-risk/) — the ex-ante loss from a credit portfolio
- [Value at Risk](/credit-risk/) — a statistical measure of maximum expected loss at a given confidence level

</div>
