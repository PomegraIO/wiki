---
title: "Delinquency"
description: "A borrower's failure to make a required loan or mortgage payment on time, typically measured as the percentage of a pool's borrowers who are 30+ days overdue."
---

*Delinquency is a leading indicator of default. When a borrower misses a payment, they enter delinquency. Some recover and catch up. Others continue to fall behind and eventually default. In structured credit, delinquency metrics are watched obsessively because they predict losses weeks or months in advance. A jump in delinquencies in a mortgage pool today signals imminent defaults tomorrow.*

## Stages of delinquency

Delinquency is measured in stages based on how many months a payment is overdue:

- **30+ day delinquent**: One payment missed.
- **60+ day delinquent**: Two payments missed.
- **90+ day delinquent**: Three payments missed (often triggers formal default and servicing actions).
- **120+, 150+, 180+ day delinquent**: Severe delinquency; foreclosure or charge-off is imminent.

A loan moves through these stages as time passes without payment. Some loans cure (the borrower catches up) and leave delinquency. Others progress to higher stages and eventually default.

## Delinquency rates and pool monitoring

Securitization trustees and servicers publish monthly or quarterly delinquency statistics:

- **30+ day delinquency rate**: Percentage of the pool that is 30+ days overdue.
- **Serious delinquency rate**: Often defined as 90+ days overdue or in foreclosure.
- **Loan loss rate**: Percentage of the pool that has been written off (removed from the pool due to default and recovery).

A pool of 1,000 mortgages with a 2% 30+ day delinquency rate has 20 borrowers one month overdue. Investors scrutinize these metrics monthly. A jump (2% to 3%) signals stress; a drop (2% to 1.5%) signals improvement.

These statistics are published in monthly factor data or investor reports, accessible to all bondholders. Transparency is mandated post-2008.

## Delinquency is an early warning signal

Delinquency rates lead default rates. A rise in delinquencies predicts future losses. When unemployment spikes (recession hits), 30-day delinquencies typically rise within months, followed by 90-day delinquencies and then defaults weeks later.

Models of pool performance use delinquency as a leading indicator. A modeler might estimate:

"Based on rising 30-day delinquencies, I forecast 90-day delinquencies to rise from 1.5% to 2.5% in three months, with ultimate defaults 50% of 90-day levels."

Armed with this forecast, an investor can estimate future losses and adjust portfolio positioning.

## Delinquency triggers in securitizations

Many securitizations include delinquency triggers that automatically activate protective mechanisms:

**Delinquency cascade trigger**: If serious delinquency (90+) exceeds a threshold (e.g., 5%), excess cash flow is diverted to pay down senior bonds faster instead of going to junior tranches.

**Servicer replacement trigger**: If delinquencies are unusually high and rising, investors may have the right to replace the servicer.

These triggers protect investors by automatically taking action when collateral stress appears. No human judgment required; the trigger fires based on a metric.

## Cures and defaults: the fork in the road

Once delinquent, a loan can either cure or default. Cure rates vary by delinquency stage and economic condition:

**At 30 days**: 50–80% of borrowers cure (make up the missed payment). This is relatively early; many are one-off misses due to timing or illness.

**At 60 days**: 40–60% cure. The borrower might negotiate a payment plan.

**At 90 days**: 20–40% cure. By this stage, many borrowers have given up or cannot catch up.

**At 120+ days**: 10–20% cure. Most are on a path to foreclosure.

The other borrowers default. In economic downturns, cure rates plummet and default rates soar.

## Delinquency by borrower segment

Delinquency is not uniform across a pool. Subprime mortgages (low FICO borrowers) have higher delinquency rates than prime. Variable-rate mortgages have higher delinquency when rates adjust upward. Borrowers in weak labor markets have higher delinquency.

Servicers (and modelers) break down delinquency by segment: by FICO band, by origination year (vintage), by geography, by rate type (fixed vs. ARM). A servicer might report:

"Serious delinquency is 2.5% overall, but 5% for subprime borrowers, 3% for prime, and 1.5% for super-prime."

This granularity lets investors spot deterioration in specific segments. If prime delinquency is rising (historically stable), it signals broader economic stress.

## The servicer's role in managing delinquency

When a payment is due and not received, the servicer:

1. Sends a reminder to the borrower (phone, mail, email).
2. If payment is still not received, initiates a late fee and delinquency procedures.
3. For borrowers in hardship (job loss, illness, divorce), the servicer offers alternatives to foreclosure: loan modification, forbearance (pause on payments), or refinancing.
4. If the borrower does not respond or cannot pay, the servicer initiates foreclosure.

A servicer's goal (and contractual obligation) is to minimize delinquencies through early contact and loss mitigation. Effective servicers work with borrowers proactively; poor servicers wait for payments to be very late before acting.

Post-2008 regulation requires servicers to offer loss-mitigation options before foreclosure. This reduces defaults but increases the timeline (forbearance might delay payment for months).

## Delinquency and securities trading

Bond prices move on delinquency expectations. A mortgage bond trading at 102 might fall to 100 if delinquency jumps unexpectedly, signaling future losses. Traders track delinquency data like equity traders track earnings reports.

Some investors build delinquency models to forecast losses before they appear in official default rates. A sophisticated mortgage investor might have real-time data feeds on delinquencies across multiple servicers and pools, updating loss forecasts constantly.

## Delinquency in different asset classes

Delinquency is highest in credit cards (which are unsecured and have high default rates) and lowest in mortgages (which are secured and borrowers prioritize housing payments).

**Mortgages**: 1–3% serious delinquency in normal times; spikes to 5–10% in recessions.

**Auto loans**: 2–4% serious delinquency; cars are repossessed quickly so borrowers are incentivized to keep current.

**Credit cards**: 3–6% delinquency; unsecured, so defaults are common.

**Student loans**: 3–6% serious delinquency; large portfolio means absolute numbers are massive.

Securitizations of each asset class are calibrated to these different delinquency regimes.

## Delinquency and the 2008 crisis

The subprime mortgage crisis saw delinquency rates spike from 1–2% (2005–2006) to 8–12% (2009–2010) for subprime pools. Servicers were overwhelmed; foreclosure inventories ballooned. Delinquencies persisted (borrowers were in long-term forbearance or slow foreclosure) for years.

The Mortgage Bankers Association's delinquency index became a closely watched metric signaling the crisis's severity.

## Delinquency monitoring going forward

In modern securitizations, delinquency is monitored continuously. Investor reports disclose delinquency rates, trend analysis, and segmentation. Algorithms flag unusual patterns (sharp jumps, geographic concentration) for manual review.

The practice ensures that credit deterioration is caught early and investors can adjust positioning or demand higher spreads before losses materialize.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/default-rate/">Default Rate</a> — the endpoint of delinquency progression.</li>
<li><a href="/wiki/probability-of-default/">Probability of Default</a> — modeled using delinquency data.</li>
<li><a href="/wiki/securitization/">Securitization</a> — delinquency is monitored in all securitizations.</li>
<li><a href="/wiki/mortgage-backed-security/">Mortgage-Backed Security</a> — MBS delinquency is most closely tracked.</li>
<li><a href="/wiki/loan-modification/">Loan Modification</a> — servicers use modifications to cure delinquency.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/credit-risk/">Credit Risk</a> — delinquency signals credit stress.</li>
<li><a href="/wiki/asset-backed-security/">Asset-Backed Security</a> — all ABS report delinquency rates.</li>
<li><a href="/wiki/servicer-risk/">Servicer Risk</a> — servicers manage delinquencies.</li>
</ul>
</div>
