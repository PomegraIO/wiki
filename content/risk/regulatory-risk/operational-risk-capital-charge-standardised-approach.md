---
title: "Operational Risk Capital Charge: The Standardised Approach"
description: "The standardised operational risk capital charge under Basel III: how the BI and ICs drive required capital without model complexity."
keywords:
  - operational risk capital charge
  - standardised approach operational risk
  - business indicator component
  - income component
  - basel iii operational risk
---

*The **operational risk capital charge** under Basel III's standardised approach replaces earlier, bank-proprietary advanced models with a formulaic method that combines a bank's business-indicator component (BIC) with an income-and-losses component (IC). No model approval needed—all banks calculate it the same way—but the result can be just as capital-intensive for banks with large, risky business lines.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Operational Risk Capital Charge — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for operational risk frameworks." />

<div class="wiki-infobox-caption">A two-component formula (business indicator + income losses) replaces proprietary models across all banks.</div>

|   |   |
|---|---|
| **Formula** | OpRisk charge = BI × BIC margin + IC losses |
| **Business Indicator (BI)** | Net interest income + net non-interest income (roughly gross revenue proxy) |
| **Component (BIC) margins** | 12%, 15%, or 18% depending on BI band (larger banks pay more) |
| **Income Component (IC)** | Realized operational losses over a 10-year look-back period |
| **Replaces** | Advanced Measurement Approach (AMA) and Standardised Measurement Approach (SMA) |
| **Binding date** | January 2023 (Basel III endgame implementation) |
| **Risk type coverage** | Internal fraud, external fraud, employment practices, clients/products, damage to assets, business disruption, execution failures |

</aside>

## The End of Advanced Models

For two decades, large banks built **Advanced Measurement Approaches** (AMAs) to calculate [operational-risk](/operational-risk/) capital. These models were bespoke: a bank would collect historical loss data, calibrate it to its business, and derive a capital charge. The theory was elegant—banks that managed [operational-risk](/operational-risk/) better would get lower charges—but implementation bred complexity and inconsistency. Different banks modeled the same risk differently. Model validation consumed armies of risk officers. And during stress periods, when operational losses spiked, banks discovered their models lagged reality.

In 2020, the Basel Committee scrapped AMA and replaced it with a **standardised operational risk capital charge**. The goal: transparency, comparability, and a formula that captures risk without requiring supervisory approval of proprietary mathematics.

## The Two-Component Formula

The standardised approach has two parts: a **business indicator** and an **income component**.

**Business Indicator (BI)**

The BI is a proxy for the bank's operational risk exposure. It is the sum of net interest income and net non-interest income—essentially, a bank's gross revenue before provisions and taxes. The logic: a larger, more complex operation faces more operational risk. A bank earning $50 billion annually will likely have greater exposure to operational losses than a $5 billion bank, all else equal.

However, BI alone is crude. A bank might have high revenue but low [operational-risk](/operational-risk/) due to tight controls. So the formula adds a margin that penalizes larger banks more, by band:

| Business Indicator Band | Margin (BIC) |
|-------------------------|--------------|
| BI < $1 billion | 12% |
| $1B ≤ BI < $30 billion | 15% |
| BI ≥ $30 billion | 18% |

A $100 billion revenue bank pays 18 percent of BI as its baseline operational risk charge. A $500 million bank pays 12 percent. This graduated structure ensures that systemic risk (concentrated in large banks) attracts proportional capital.

**Income Component (IC)**

The second pillar, the **Income Component**, adjusts for actual [operational-risk](/operational-risk/) track record. The IC is calculated as the average of operational losses (excluding gains) over a 10-year rolling window, adjusted for inflation and multiplied by a factor (typically between 1.0 and 1.5, set by the Basel Committee). The idea is that a bank with a history of material operational losses should hold more capital, regardless of business size.

Operational losses include:

- **Internal fraud**: Employee misconduct, rogue trading, misappropriation.
- **External fraud**: Theft, hacking, payment card fraud, theft of physical assets.
- **Employment practices and workplace safety**: Discrimination claims, sexual harassment settlements, workplace injuries.
- **Clients, products, and business practices**: Mis-selling, breach of fiduciary duty, unsuitable advice.
- **Damage to physical assets**: Disasters, storms, sabotage.
- **Business disruption and system failures**: IT outages, software bugs, third-party vendor failures.
- **Execution, delivery, and process management**: Settlement failures, fraud by counterparties, miscalculations, missed deadlines.

## Combined Charge

The final operational risk capital charge is the sum of these components. If a bank has a BI of $50 billion and an average 10-year IC of $200 million, and the IC factor is 1.0, the charge might be:

- BIC: $50B × 0.18 = $9.0 billion
- IC: $200M × 1.0 = $200 million
- **Total OpRisk charge: $9.2 billion**

This charge is converted into a risk-weighted asset equivalent (by dividing by the total capital ratio, typically 8 percent) and added to the bank's [capital-adequacy](/capital-adequacy/) calculation.

## Why This Replaces AMA

The standardised approach offers three advantages over AMA:

**Transparency**: All banks use the same formula. Regulators can compare operational risk capital across institutions. Investors understand what drives the charge.

**Speed**: No lengthy model validation cycles. A new large acquirer immediately calculates its charge based on combined BI and IC. Supervisors approve nothing—the math is public.

**Procyclicality restraint**: AMA models often underestimated risk in booms and overestimated in busts. The standardised formula, because it averages losses over 10 years, smooths this oscillation.

## Limitations and Criticisms

The standardised approach is not without flaws. The BI band-based structure is coarse: a $31 billion revenue bank pays 18 percent, while a $29 billion bank pays 15 percent, despite minimal operational risk difference. The IC component only captures realized losses; a bank that barely avoided a major fraud might face a lower charge than one that suffered a minor breach.

Moreover, the 10-year look-back for IC is both generous and harsh. A bank might exit a loss-making business or lose a major source of fraud—but that history lingers, inflating its charge. Conversely, a young bank with no loss history starts with IC = 0, which may not reflect true operational risk.

## Interaction with Pillar 1 and Pillar 2

The operational risk charge is part of a bank's total [Pillar-1](/pillar-2-capital-requirement-vs-pillar-1/) minimum capital requirement. It sits alongside [credit-risk](/credit-risk/) and [market-risk](/market-risk/) charges. Supervisors, in [Pillar 2](/pillar-2-capital-requirement-vs-pillar-1/), may add capital for operational risk concentrations (e.g., a bank with a history of settlement failures) or governance weaknesses.

Some jurisdictions phase in the standardised approach gradually, allowing banks to run it in parallel with legacy AMA models. Others implement immediately, forcing quick recalibration of capital plans.

## Data Quality and Granularity

Banks must rigorously classify and measure operational losses to calculate IC accurately. This has driven investment in loss databases and event tracking. Regulators expect banks to defend their IC calculations with detailed loss event documentation. A dispute over whether a $50 million litigation settlement counts as "clients/products" or "employment practices" can shift the IC by millions.

## See also

<div class="wiki-seealso">

### Closely related

- [Operational Risk](/operational-risk/) — the underlying risk type this charge is designed to cover
- [Capital Adequacy](/capital-adequacy/) — the framework within which the operational risk charge sits
- [Pillar 2 Capital Requirement vs Pillar 1](/pillar-2-capital-requirement-vs-pillar-1/) — supervisors may add capital on top of standardised charge for bank-specific operational risk
- [Tier 1 Capital](/tier-1-capital/) — the capital denominator against which the operational risk charge is measured

### Wider context

- [Credit Risk](/credit-risk/) — another major Pillar 1 capital charge component
- [Market Risk](/market-risk/) — the third Pillar 1 charge component
- [Liquidity Risk](/liquidity-risk/) — often becomes salient after operational failures
- [Concentration Risk](/concentration-risk/) — supervisors may penalize concentration in loss-prone business lines
- Risk Management — governance frameworks that inform capital adequacy judgments

</div>
