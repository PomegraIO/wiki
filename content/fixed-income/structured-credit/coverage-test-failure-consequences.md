---
title: "Coverage Test Failure Consequences in Structured Credit"
description: "Coverage test failure in CLOs and CDOs triggers cash diversion: subordinate tranches stop receiving principal paydown. Learn what happens next and how breaches are cured."
keywords:
  - coverage test failure
  - CLO structured credit
  - OC test IC test
  - collateralized loan obligation
  - subordinate tranche consequences
  - cash diversion trigger
image: "/svg/fixed-income.svg"
---

*A **coverage test failure** in a collateralized loan obligation (CLO) or collateralized debt obligation (CDO) instantly rewires the payment waterfall. When an Overcollateralization (OC) test or Interest Coverage (IC) test breaches, principal that would normally pay down subordinate tranches gets redirected to pay down the senior notes instead. This mechanic protects senior holders from default risk by locking junior investors into a waiting period until the tests heal.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Coverage Test Failure — Key Consequences</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A test breach flips the payment order and locks junior tranches out of principal recovery.</div>

|   |   |
|---|---|
| **OC test failure trigger** | Portfolio collateral value falls below threshold (typically 93–105%) |
| **IC test failure trigger** | Portfolio interest income falls below threshold (typically 1.3–2.0x service costs) |
| **Immediate consequence** | Principal payment waterfall redirects; subordinate tranches receive no paydown |
| **Senior tranches** | Continue receiving interest; receive excess principal until test heals |
| **Subordinate tranches** | Receive interest only; principal is blocked until coverage ratio improves |
| **Time horizon to cure** | Usually 3–12 months; some can persist for years in distressed portfolios |
| **Manager remediation** | Sale of underperforming assets, prepayment acceleration, asset swaps |

</aside>

## What the Tests Actually Measure

Before understanding failure, you need the mechanics. An OC test compares the current market value (or par value for harder-to-mark assets) of the portfolio collateral against the outstanding balance of the bond tranches. If a CLO has $400 million in loans outstanding but they're now worth only $370 million in a market downturn, the OC ratio is $370 ÷ $400 = 0.925, or 92.5%. Most deals require an OC of at least 95%. The test fails.

An IC test divides the dollar amount of interest and principal paydown the portfolio generates each quarter by the service costs (interest due on all outstanding bonds plus management fees). If the portfolio is earning $3 million per quarter but the service costs are $2.5 million, the IC ratio is 1.2x—a breach if the deal requires 1.5x. Again, the test fails.

These tests exist because they forecast whether subordinate tranches will eventually be repaid. A falling OC ratio warns that loan defaults are accelerating or borrower credit is deteriorating. A falling IC ratio flags that the collateral is not generating enough cashflow to service all bonds safely. Triggering a test failure is the deal's first alarm.

## How Principal Gets Diverted

Inside a normal CLO, the payment waterfall works like this: each month, loan interest and principal paydowns flow in. Money is first used to pay the trustee, then interest on senior bonds, then interest on mezzanine bonds, then interest on equity. Any leftover goes to principal paydown of senior bonds, then mezzanine, then equity.

When an OC or IC test fails, that waterfall flips. Interest payments continue normally for everyone. But the principal paydown step changes: instead of funding junior tranches, all excess principal goes to pay down the senior bond balances until the test heals. This is called "stepping up in priority" or "cash trap."

Practically, this means:
- A mezzanine bondholder who expected to receive $50,000 in principal that quarter gets $0.
- The equity holder, which was expecting a distribution, gets nothing.
- The senior bondholder receives the full $50,000, shrinking their outstanding balance and improving the OC ratio.

The longer the breach persists, the more principal subordinate tranches miss. In a severe downturn, a junior bondholder could go 12–24 months with no principal recovery, even though they're receiving interest on time.

## Why This Protects Senior Creditors

Senior bondholders are the safest tier. They have first claim on all cash and lose money only if the entire portfolio defaults. A coverage test failure is a warning sign, and diverting principal to them reduces their exposure. By forcing the OC ratio back above 95%, the deal mathematically guarantees a bigger cushion: if loans default, there's more collateral cushion before the senior notes take losses.

An IC test failure signals that the portfolio isn't generating enough interest to cover service costs if defaults accelerate further. By forcing principal paydown, the deal shrinks the total outstanding bonds faster, lowering future service costs. This is self-healing: fewer bonds outstanding = lower interest owed each quarter = higher IC ratio.

The effect is punitive to subordinate bondholders but mathematically sound for deal structure. It's a trade-off baked into the offering documents when the tranche is sold. Junior holders accept the principal suspension risk in exchange for higher yields.

## How Long Can a Breach Last?

Most CLO deals expect a coverage test to fail for a quarter or two during normal market cycles, then heal. In a 2015 energy downturn or 2020 COVID shock, tests can stay broken for 6–12 months. In genuinely distressed portfolios—say, a CDO issued in 2006 holding subprime mortgage exposure during the financial crisis—tests can fail for years.

During prolonged failures, junior tranches essentially become locked equity. They're no longer amortizing; they're waiting for the collateral to recover or for the manager to take action. Some are eventually paid off at par or discounted; others are written down.

## How Managers Cure a Breach

The fund manager or collateral manager doesn't want a long-lived test failure. It signals to the market that the deal is struggling, which damages the manager's reputation and makes future CLO issuance harder. Managers deploy several levers:

**Asset sales**: Sell underperforming loans at a small loss, replace them with higher-quality loans. This raises the OC ratio if the replacement loans are safer and the collateral pool strengthens overall.

**Prepayment acceleration**: Call loans from borrowers who are prepaying. If the manager redirects prepayment proceeds to pay down bonds (rather than reinvest in new loans), the outstanding debt shrinks, improving both OC and IC.

**Interest rate hedging**: In a low-rate environment where IC is failing, locking in forward interest rate expectations via [swaps](/swap/) can improve forward IC projections.

**Asset swaps**: Exchange a weak loan for a stronger one at par or near-par, lifting credit quality without a realized loss.

**New equity injection**: Rarely, the manager injects new capital to buy bonds or absorb losses, triggering a reset.

If none of these work, the manager may be replaced (per the deal documents), the bonds may be restructured, or the deal enters workout—a slower path to eventual repayment or loss realization.

## Real-World Example: A Hypothetical CLO in Downturn

Imagine a CLO issued with a 95% OC test and 1.5x IC test. The collateral is 80 leveraged buyout loans, each $5 million. In steady state:
- Portfolio value: $400M; outstanding bonds: $320M; OC = 125%.
- Quarterly interest generated: $2.4M; service costs: $1.6M; IC = 1.5x.

A recession hits. Loan defaults accelerate. Three borrowers default; their loans fall to 50 cents on the dollar. The portfolio drops to $385M in value. OC is now $385M ÷ $320M = 1.21, or 121%. The OC test (95%) still passes.

But loan interest payments also drop—fewer loans are paying in full. Quarterly interest is now $2.1M. Service costs remain $1.6M. IC is 1.31x. The IC test (1.5x) fails.

Once the test fails, the manager must direct all excess principal (not just the waterfall excess) to senior paydown. The manager also sells two weak loans at a loss, replacing them with higher-quality loans. This boosts interest generation back to $2.2M. IC moves to 1.375x—still failing. After another quarter of asset sales and prepayment redirects, interest is back to $2.5M, IC = 1.56x, and the test heals. Mezzanine bondholders resume receiving principal paydowns.

## The Investor Impact

For a bondholder, a coverage test failure is a yield event but not a default. You keep receiving interest. Your principal just doesn't amortize. If the failure lasts three months, you've lost three months of principal recovery—a real opportunity cost because you could have reinvested that money. If it lasts two years, the cost is higher: two years of principal was trapped, and the longer duration exposure hurt if rates rose.

Equity holders in a failed-test scenario often see distributions cut to zero. They funded the deal for return, and while interest-paying tranches sleep, equity is washed out. This is the risk they accepted.

## See also

<div class="wiki-seealso">

### Closely related

- Collateralized loan obligation — CLO structure and mechanics
- [Tranche](/tranche/) — How securitizations are divided into payment tiers
- Overcollateralization — The ratio protecting senior creditors
- [Interest coverage ratio](/interest-coverage-ratio/) — How to measure debt service capacity
- Collateralized debt obligation — The broader family of structured credit

### Wider context

- [Credit cycle](/credit-cycle/) — How loan stress evolves in macro downturns
- [Securitization](/securitization/) — Creating tradable bonds from loan pools
- [Default rate](/default-rate/) — Measuring actual loan loss frequency
- [Stress testing](/stress-testing/) — Scenario analysis for portfolio risk
- Workout — How distressed credit is resolved

</div>
