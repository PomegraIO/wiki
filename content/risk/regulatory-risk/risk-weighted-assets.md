---
title: "Risk-Weighted Assets"
description: "A regulatory framework that scales bank exposures by asset risk weight to calculate the denominator of capital adequacy ratios."
keywords:
  - capital adequacy
  - risk weights
  - basel iii
  - regulatory capital
  - asset risk
  - bank supervision
image: "/svg/risk.svg"
---

*A **risk-weighted asset** (RWA) is a bank exposure scaled by a risk weight set by regulators to reflect the probability and loss severity of that asset. Summing all weighted exposures yields the denominator for [capital ratio](/capital-adequacy/) tests: a bank with USD 100 million in capital and USD 1 billion in risk-weighted assets has a 10% capital-to-RWA ratio.*

## Why raw assets are not a measure of bank safety

A balance sheet full of cash, Treasury bills, and AAA-rated bonds is safer than one packed with high-leverage commercial real-estate loans and junk-rated corporate debt. Yet a simple [leverage ratio](/leverage-ratio-forex/) (capital divided by total assets) treats them identically. If a bank has USD 100 billion in assets but USD 90 billion of that is US Treasuries and USD 10 billion is subprime mortgages, the asset totals look the same as a bank with USD 100 billion in loans across diverse sectors. The risk is not the same.

Risk-weighting solves this by assigning each asset class a weight based on default probability and loss-given-default. Governments bonds get a weight of 0% (zero risk, at least in the bank's home currency); investment-grade corporate debt gets 100%; unrated corporate debt or certain commercial mortgages get 150% or higher. A USD 100 million position in US Treasuries contributes USD 0 million to risk-weighted assets; a USD 100 million corporate loan contributes USD 100 million to RWA (or more, if the weight is 150%). The same notional size, vastly different regulatory footprint. This forces banks to think about composition, not just size.

## Standard approach versus internal ratings

Regulators offer two main frameworks for deriving risk weights. Under the **standardized approach**, banks use buckets set by regulators. Sovereigns get 0–150% depending on credit rating and currency; banks get 20–150%; mortgage-backed securities get 50–100%; unrated corporates get a flat 100%. The weights are conservative and published, making comparisons transparent. A bank using the standardized approach must hold, say, 8% capital against risk-weighted assets, which is the global minimum under Basel III.

Under the **[internal ratings-based approach](/internal-ratings-based-approach/)**, large banks build proprietary models to estimate probability of default (PD) and loss-given-default (LGD) for each borrower or loan class. Regulators review these models and set risk weights as functions of the estimated PD and LGD. This approach is theoretically more accurate—a bank's model might assign a precise 15% weight to mid-market corporate loans with certain characteristics, rather than the standardized 100%—but it also hands banks discretion over inputs and introduces model risk. A flawed or optimistic model understates true losses and lets the bank hold less capital than warranted.

Most large global banks use the internal ratings-based approach for corporate and bank exposures; many blend standardized and IRB methods across portfolios. Regulatory approval is required, and supervisors conduct annual validation reviews. The trade-off is intuitive: IRB is more efficient (lower capital drag on profitable lending) but demands higher operational rigor and model governance. After the 2008 crisis and the subsequent shift toward stricter regulation, many regulators have tightened IRB approval standards and added floors to prevent capital from falling too far below the standardized approach result.

## The calculation and leverage constraint

Computing RWA is mechanical once weights are in place. For each asset, multiply the exposure (book value, or for derivatives a more complex formula) by the risk weight; sum across the entire balance sheet and off-balance sheet items (derivatives, loan commitments, etc.). A bank with USD 1 billion in sovereigns (0% weight), USD 5 billion in investment-grade corporate loans (100% weight), and USD 2 billion in residential mortgages (say, 35% weight) has:

RWA = (1 × 0%) + (5 × 100%) + (2 × 35%) = 0 + 5 + 0.7 = USD 5.7 billion

If capital is USD 450 million, the Tier 1 ratio is 450 ÷ 5,700 = 7.9%, just above the Basel III global minimum of 7%.

But RWA is not the whole story. Banks also face a **leverage ratio** (Tier 1 capital divided by total assets, unweighted), set at 3% under Basel III. The leverage ratio is a backstop: it prevents banks from gaming the risk-weighting system by loading up on assets that regulators underweight. A bank cannot achieve a high RWA ratio purely by holding low-weight assets if its leverage ratio still binds. In practice, the leverage ratio is often less constraining for well-capitalized banks but becomes a real constraint for those that have heavy customer lending or trading books.

## Gaming and regulatory response

Risk-weights are politically sensitive. The higher the weight on, say, mortgages, the more capital a bank must hold against its mortgage book, which raises the cost of mortgages to borrowers and slows the housing market. Banks lobby for lower weights on their largest exposures (mortgages, syndicated loans, trade finance). Regulators must balance competitive fairness—do not let one sector's lobbying win a subsidy in capital terms—with economic impact. The 2008 crisis revealed another problem: banks' internal models were too optimistic during booms. The models assigned low default probabilities to borrowers and low loss-given-default to mortgaged properties, understating RWA and understating required capital.

Regulators have responded with tighter validation, floor rules (capital under IRB must not fall below 70–80% of standardized approach capital), and periodic recalibration of standardized weights. The European Union recently tightened mortgage risk-weights to push back against declining lending standards. The US Federal Reserve imposes annual [stress testing](/stress-testing/) of bank portfolios under adverse scenarios, a complement that forces banks to consider tail risks the static risk-weight framework misses.

## The RWA denominator and capital adequacy

The power of RWA lies in its simplicity as a common denominator. Regulators can compare banks across geographies and business lines using a single metric: Tier 1 ratio, Tier 1 common ratio, total capital ratio, all expressed as a percentage of RWA. A bank that shrinks its RWA by shedding risky loans or securitizing mortgages improves its reported ratios instantly (good for the bank, potentially bad for regulatory discipline if the intent is to look safer, not be safer). This creates a perverse incentive: banks can window-dress by transferring risk rather than genuinely strengthening the balance sheet.

The [countercyclical buffer](/countercyclical-capital-buffer/), conservation buffer, and [G-SIB surcharge](/g-sib-surcharge/) all apply to RWA, so the denominator is critical infrastructure for macroprudential policy. A 1% countercyclical buffer on a bank with USD 500 billion RWA means USD 5 billion in extra capital required. If the same bank's RWA is measured using loose IRB models, that USD 500 billion is an underestimate, and the USD 5 billion buffer is inadequate.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital Adequacy](/capital-adequacy/) — the regulatory framework that risk-weighted assets denominate
- [Internal Ratings-Based Approach](/internal-ratings-based-approach/) — the method some banks use to compute risk weights
- [Countercyclical Capital Buffer](/countercyclical-capital-buffer/) — a capital add-on expressed as a percentage of RWA
- [G-SIB Surcharge](/g-sib-surcharge/) — another capital overlay that applies to RWA
- [Credit Risk](/credit-risk/) — the underlying risk that weights aim to measure
- [Stress Testing](/stress-testing/) — the complement to static risk-weighting that tests tail scenarios

### Wider context

- [Leverage Ratio Forex](/leverage-ratio-forex/) — the unweighted capital backstop
- [Securitization](/securitization/) — a technique banks use to reduce RWA by transferring risk
- [Basel III](/capital-adequacy/) — the international accord that standardizes RWA frameworks
- [Federal Reserve](/federal-reserve/) — a major regulator of RWA rules in the United States
- [Dodd-Frank Act](/dodd-frank-act/) — US statute embedding RWA requirements in regulation

</div>
