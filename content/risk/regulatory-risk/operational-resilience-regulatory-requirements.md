---
title: "Operational Resilience Regulatory Requirements for Banks"
description: "Operational resilience rules require banks to identify critical services, set tolerance thresholds, and test their ability to recover within those limits."
keywords:
  - operational resilience
  - regulatory requirements
  - bank resilience
  - impact tolerance
  - stress testing
  - business continuity
  - financial regulation
---

*Banks now face **operational resilience regulatory requirements** that force them to map critical services, set "important business services," establish impact tolerances, and test their ability to survive disruptions within those tolerances. The UK and EU implemented these rules to prevent cascading failures that could threaten financial stability.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Operational Resilience — Key Requirements</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk and resilience." />

<div class="wiki-infobox-caption">Regulators now mandate that banks prove they can recover from disruption.</div>

|   |   |
|---|---|
| **Key regulators** | UK FCA, PRA; EU EBA, ECB |
| **Core mandate** | Identify critical services; set impact tolerances; test recovery ability |
| **Impact tolerance** | Maximum acceptable harm (e.g., "recover deposits within 2 days") |
| **Testing frequency** | Annual or per-requirement; varies by jurisdiction and bank size |
| **Failure consequence** | Enforcement action; potentially capital add-ons or restrictions |
| **Timeline** | UK: phased 2021–2025; EU: phased 2024–2026 |

</aside>

## What Is Operational Resilience?

Operational resilience is the ability of a bank to deliver important business services even during severe disruption—whether from cyber attack, data center failure, third-party service collapse, or natural disaster. Rather than assuming disruptions won't happen, regulators now require banks to prove they *will* survive them and keep serving customers.

The concept emerged after a series of operational outages caused public damage: a bank's payment system goes down for hours, millions of customers cannot access deposits; a cloud provider fails, and dependent banks lose access to critical data. Regulators recognized that a single bank's operational failure can ripple through the financial system and harm the real economy. So instead of auditing for compliance with detailed rules, regulators now demand that banks demonstrate *resilience*—the capacity to absorb shock and recover.

## The Core Framework: Important Business Services and Impact Tolerances

Under operational resilience rules, every bank must identify which services are **important business services** (IBS). These are the activities that, if lost or severely degraded, would harm customers, the financial system, or financial stability. For a large universal bank, this might include: payments and settlement, deposit taking, corporate lending, securities custody.

For each important business service, the bank must set an **impact tolerance**—a limit on how much harm the bank will accept before recovery must be complete. Impact tolerance is not a single metric; it is multi-dimensional. It might include:

- **Duration**: "Deposits must be accessible within 2 hours of disruption"
- **Data loss**: "No customer data may be permanently lost"
- **Financial loss**: "The bank will not incur more than £10 million in uninsured losses"
- **Customer impact**: "No more than 5% of eligible transactions may fail"

The impact tolerance is a decision by the bank, but it must be reasonable, documented, and approved by the board and regulators. It answers the question: "What level of disruption is the bank willing to live with?"

## Resilience Testing and Scenario Design

Once impact tolerances are set, the bank must test its ability to meet them under stress. The testing framework typically includes:

**Scenario-based stress tests**: The bank designs scenarios—cyber attacks, third-party failures, natural disasters, staffing collapse—and simulates the impact on each important business service. Can the bank recover deposits within 2 hours? Can it maintain settlement within the tolerance?

**Reverse stress testing**: The bank asks: "What disruption would push us beyond our impact tolerance?" This helps identify vulnerabilities and concentration risks.

**Third-party dependencies**: The bank maps its critical third-party service providers (cloud, payment networks, data vendors) and tests what happens if one of them fails. Many banks discovered they depend heavily on a single cloud provider or a small set of market infrastructure operators.

**Recovery planning**: For each scenario, the bank documents how it would recover—which backup systems activate, which staff are mobilized, which customers are prioritized, how long recovery takes.

Testing is not a one-time audit. Regulators expect annual testing, or more frequent if the regulatory rules require it. If a test fails—if the bank cannot meet its impact tolerance under the scenario—it must identify root causes and remediate.

## UK and EU Implementation

The **UK Financial Conduct Authority (FCA)** and **Prudential Regulation Authority (PRA)** began phasing in operational resilience rules in 2021, with a staged compliance timeline. Large banks faced earlier deadlines; smaller firms had more time. The PRA expects banks to complete impact tolerance-setting, service mapping, and initial testing by 2025.

The **European Banking Authority (EBA)** and **European Central Bank (ECB)** launched a parallel framework for EU banks, with similar requirements but slightly different timelines. The EU framework is still being finalized, but the direction is the same: impact tolerance, scenario testing, recovery capability.

Both regimes apply to large, systemically important banks first, then cascade to smaller institutions. The rationale: large banks' failures impose systemic costs, so they must be more resilient.

## Third-Party and Concentration Risk

A major focus of operational resilience testing is **third-party risk**. Many banks now depend on cloud providers, fintech integrations, or market infrastructure operators. If AWS goes down, a bank using AWS for critical services faces immediate disruption. If SWIFT (the global payments network) fails, all settlement stops.

Regulators now require banks to:
- Map all third-party dependencies for important business services
- Negotiate recovery-time agreements with critical vendors
- Test failover to backup providers
- Monitor third-party concentration (avoid over-reliance on a single vendor)

Some banks have discovered they cannot meet their impact tolerance without diversifying vendors or negotiating faster recovery commitments. This has sparked negotiations between banks and cloud providers over service-level agreements.

## Governance and Board Accountability

Operational resilience is not a technical IT function alone. The framework requires board-level ownership. Directors must approve impact tolerances, understand the testing results, and authorize remediation spending. If a bank cannot meet its impact tolerance, this is a governance failure.

Regulators expect documented board oversight: minutes showing directors reviewed resilience metrics, understood gaps, and approved budgets to close them. If a bank later suffers an operational failure and regulators discover the board never reviewed resilience testing, enforcement follows.

## Consequences of Non-Compliance

Banks that fail to set reasonable impact tolerances, conduct adequate testing, or meet their tolerances face:

- **Enforcement action**: Cease-and-desist letters, fines, or restrictions on business activities
- **Capital add-ons**: The PRA may impose additional [capital-adequacy](/capital-adequacy/) requirements if a bank's resilience is judged weak
- **Restrictions on new services or mergers**: A bank unable to meet operational resilience standards may be prohibited from launching new services or acquiring other banks
- **Reputational damage**: Public enforcement action signals to customers and counterparties that the bank is operationally weak

A few banks have already faced enforcement warnings for inadequate resilience planning.

## See also

<div class="wiki-seealso">

### Closely related

- [Risk-Weighted Assets](/risk-weighted-assets/) — How capital adequacy intertwines with operational resilience
- [Stress Testing](/stress-testing/) — Scenario design and bank resilience under economic shock
- [Capital Adequacy](/capital-adequacy/) — Regulatory capital buffers that support resilience
- [Systemic Risk](/systemic-risk/) — Why bank failures threaten the broader financial system

### Wider context

- [Central Bank](/central-bank/) — Regulatory authority and financial stability mandate
- [Federal Reserve](/federal-reserve/) — US regulatory approach (different from UK/EU)
- [Going Concern](/going-concern/) — Accounting treatment of business viability under stress

</div>
