---
title: "Net Stable Funding Ratio"
description: "A Basel III liquidity metric measuring whether a bank has enough stable funding to cover stable funding needs over one year."
keywords:
  - net stable funding ratio
  - nsfr
  - basel iii
  - bank liquidity
  - stable funding
image: "/svg/ratios.svg"
---

*The **net stable funding ratio** is a regulatory threshold that requires banks to maintain sufficient stable funding to cover their funding needs over a one-year horizon. Introduced by the Basel Committee as part of the post-2008 regulatory overhaul, it sits alongside the [liquidity-coverage-ratio] to ensure that institutions can survive severe short and medium-term stress.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Net Stable Funding Ratio — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for financial ratios." />

<div class="wiki-infobox-caption">Basel III minimum of 100% guards against medium-term funding drying up.</div>

|   |   |
|---|---|
| **Formula** | Available Stable Funding ÷ Required Stable Funding |
| **Minimum target** | 100% |
| **Time horizon** | One year |
| **Regulated by** | Basel Committee (global standard) |
| **First implemented** | 2015 (voluntary), 2018 (mandatory) |
| **Related metrics** | [Liquidity-coverage-ratio], [Current-cash-debt-coverage-ratio] |

</aside>

## Why banks need a one-year funding cushion

The 2008 crisis revealed that banks could be liquid today but broken tomorrow. Lehman Brothers had access to intraday credit minutes before collapse; its funding evaporated because counterparties stopped rolling over overnight borrowing. The industry had optimized for the typical day, not the tail event.

The net stable funding ratio enforces a minimum assumption: if you cannot raise short-term funding for a full year, you should not rely on it. The logic is simple. A bank borrows overnight at cheap rates because lenders know they can pull out tomorrow. In panic, they do pull out—all at once. A bank forced to survive without wholesale funding markets for twelve months learns to build retail deposits, long-term debt, and other sticky liabilities. That friction is the point.

Most regulators imposed the 100% minimum in 2018, giving institutions three years to comply. The largest global banks now report NSFR quarterly; it is as material to solvency scrutiny as [capital-adequacy-ratio] thresholds. A ratio above 100% means you pass; below 100% violates the standard. But like all regulatory floors, the real game is marginal: is your ratio 101% or 150%? A bank at 101% has no buffer for deterioration; one at 150% has chosen conservatism (or faces structural illiquidity in its business model).

## How it is calculated

The calculation separates the balance sheet into two categories: available stable funding (the numerator) and required stable funding (the denominator).

**Available stable funding** includes deposits (especially retail deposits with low flight risk), long-term debt, subordinated debt, and retained earnings. It excludes or heavily haircuts short-term wholesale funding, repo, and derivatives cash. The regulator assigns each liability bucket a stability weight: retail deposits might be 90% or 100% stable (unlikely to flee), while unsecured wholesale funding three months or less might be 0% stable (expect to lose it all).

**Required stable funding** is the opposite exercise. What funding does the bank need to retain? Long-term assets (mortgages, illiquid corporate loans) need to be funded over a long runway; they get a high required-funding weight. Cash and government securities held to maturity might require only 5% of their value in stable funding (almost liquid). Trading assets, derivatives, and contingent liabilities get variable weights based on volatility and rehypothecation risk.

The ratio itself is deceptively simple once categories are assigned:

Available Stable Funding ÷ Required Stable Funding = NSFR

At 100%, every dollar of required stable funding is covered by a dollar of available stable funding. Below 100%, the gap is an implicit bet that wholesale markets will always be open. Above 100%, the bank has a buffer. Regulators do not mandate a single ideal level—they mandate the floor. A ratio of 130% is prudent; 100% is compliant but tense.

## The trade-off: stable funding is expensive

The constraint creates a real economic tension. Stable funding costs more. Retail deposits earn interest; long-term debt carries a yield; both are sticky because the funding is cheap for the lender and available. Overnight wholesale funding, in normal times, is cheaper for the bank. A bank that lives at exactly 100% NSFR has optimized for low-cost short-term funding and accepted tail risk. Raising that ratio to 110% or 120% means issuing more long-term bonds or aggressively gathering stable deposits—both eat into net-interest margins.

This creates a persistent complaint from smaller and emerging-market banks: NSFR effectively subsidises large, systemically important institutions that can access the [federal-reserve] and other central banks in crisis, and have been deemed "too big to fail." A large US bank can issue two-year debt at a known price; a regional bank in a country without a strong central bank backstop finds no bid at any price when stress arrives. Stable funding that is theoretically available but practically unavailable does not count, yet smaller banks struggle to demonstrate it exists.

## NSFR and the broader Basel III landscape

The net stable funding ratio is one pillar of Basel III's liquidity framework. The [liquidity-coverage-ratio] is the short-term sibling—it requires banks to survive 30 days without market funding, holding a buffer of very liquid assets. The LCR is more binding in practice on many days; the NSFR is the one-year stress test.

Together, they create a ladder: survive one month (LCR), then survive one year (NSFR). Neither addresses solvency—they assume the balance sheet is sound—but they prevent the "funding run" from being an express route to bankruptcy. If you run out of money before you run out of time, solvency is moot.

Large internationally active banks report both. Domestic banks often report only NSFR, or only the ratios their home regulator mandates. The US Federal Reserve and the [securities-and-exchange-commission] applied NSFR requirements to US bank holding companies with assets above $100 billion, starting around 2019. European banks report to their national competent authorities under the Capital Requirements Directive. The globality of the standard is uneven—which is why NSFR is often called a "Basel III minimum" rather than a universal law.

## Reading an NSFR disclosure

When you see a bank's NSFR in an earnings report or annual filing, the headline figure is the ratio itself. If JPMorgan reports 110% NSFR, it has stable funding equal to 110% of its required funding—a 10 percentage-point buffer above the regulatory minimum. Beneath the headline are the category weights: how much of the bank's funding is deposits versus bonds, and how much of its assets require long-term funding versus are already liquid.

A bank that publishes 101% NSFR with 60% of funding in deposits is structurally different from one at 101% with 40% deposits and 40% long-term debt. The first lives on retail stickiness; the latter on capital-market access. When capital markets freeze, the second is fragile.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquidity-coverage-ratio](/liquidity-coverage-ratio/) — thirty-day stress test requiring liquid asset buffers
- [Current-cash-debt-coverage-ratio](/current-cash-debt-coverage-ratio/) — operating cash flow measure of debt repayment capacity
- [Cash-flow-to-debt-ratio](/cash-flow-to-debt-ratio/) — operating cash flow divided by total debt outstanding
- Capital-adequacy-ratio — minimum regulatory equity-to-risk-weighted-assets threshold
- [Receivables-to-payables-ratio](/receivables-to-payables-ratio/) — working capital liquidity metric for operating firms

### Wider context

- [Basel III](/basel-iii/) — post-crisis regulatory framework for bank capital and liquidity
- [Central-bank](/central-bank/) — lender of last resort that can temporarily substitute for market funding
- [Systemic-risk](/systemic-risk/) — interconnection that turns one bank's failure into industry-wide shock
- [Monetary-policy](/monetary-policy/) — interest rate and quantitative tools that set funding availability

</div>
