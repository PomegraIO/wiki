---
title: "AML Onboarding vs Ongoing Monitoring"
description: "AML onboarding performs one-time identity and risk verification at account opening, while ongoing monitoring continuously surveys behavior for suspicious activity—each addresses different fraud and money-laundering stages."
keywords:
  - aml onboarding vs ongoing monitoring
  - aml onboarding process
  - aml continuous monitoring
  - kyc requirements ongoing
image: /svg/regulation.svg
---

*Anti-money laundering (AML) compliance splits into two distinct phases. **Onboarding** is the gatekeeping stage: verify who the customer is, check sanction lists, and assess their risk profile *before* the account opens. **Ongoing monitoring** is continuous surveillance of their behavior—transaction patterns, geography, counterparties—to catch changes in risk or signs of suspicious activity *after* the account is active. Both are required, but they answer different questions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">AML Onboarding vs Ongoing Monitoring — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation." />

<div class="wiki-infobox-caption">Gatekeeping at entry; surveillance during tenure.</div>

|   |   |
|---|---|
| **Onboarding timing** | Before account opening (or during enrollment) |
| **Ongoing timing** | For the life of the relationship |
| **Onboarding focus** | Who is this customer? Are they sanctioned? What is their risk? |
| **Ongoing focus** | Are their transactions consistent with their profile? Has risk changed? |
| **Key tools (onboarding)** | Identity verification, KYC form, sanction screening, politically exposed person (PEP) check |
| **Key tools (ongoing)** | Transaction monitoring, behavioral analytics, periodic risk reassessment |
| **Regulatory basis** | Bank Secrecy Act (BSA), FinCEN guidance, FINRA rules |

</aside>

## The onboarding phase: Know your customer at entry

When a customer opens an account, the institution must collect and verify their identity. This is Know Your Customer (KYC) and it is the foundation of AML.

**What happens during onboarding:**
1. **Identity verification:** Collect a government ID and confirm the customer's name, date of birth, address. This may involve document checks or third-party databases.
2. **Beneficial ownership determination:** If the customer is a business or trust, identify the true owner(s)—the people who ultimately control or benefit from the entity. A shell company cannot hide behind a corporate veil.
3. **Sanction and watchlist screening:** Check the customer name against the [Office of Foreign Assets Control (OFAC) list](/aml-onboarding-vs-ongoing-monitoring/), FBI lists, state and international sanction lists, and politically exposed person (PEP) databases.
4. **Risk profile assessment:** Assign a risk rating—low, medium, or high—based on factors like geography, industry, transaction size, and complexity. A customer in a high-risk jurisdiction who plans large wire transfers is flagged at entry.
5. **Source of funds verification:** For high-risk customers, confirm that funds being deposited come from legitimate sources (employment, sale of property, inheritance, etc.).

The goal is simple: **don't knowingly open an account for a criminal, a sanctioned entity, or someone financing terrorism.** Onboarding is the gate.

## Ongoing monitoring: Continuous surveillance during the relationship

Once the account is open, the obligation doesn't end. Ongoing monitoring is *continuous* surveillance of the customer's activity to detect:
- **Suspicious transactions** that deviate from the customer's known profile
- **Behavioral changes** (sudden spikes in volume, new geographies, new counterparties)
- **Red flags** that may indicate money laundering or sanctions evasion

**What happens during ongoing monitoring:**
1. **Transaction monitoring:** Every deposit, withdrawal, and transfer is screened against rules. Does a customer normally deposit $500 checks and suddenly wire $50,000 overseas? That gets flagged.
2. **Threshold alerts:** Transactions above a certain size (e.g., all cash deposits over $10,000 or wire transfers over $100,000) trigger review.
3. **Behavioral analysis:** Compare transaction patterns to the baseline established at onboarding. A retiree living in Des Moines who suddenly receives wire transfers from six new counterparties in Moscow is a red flag.
4. **Periodic risk reassessment:** At least annually (or per policy), re-evaluate the customer's risk rating. Has their geography changed? Has their business model shifted? Has new adverse information emerged?
5. **Sanction re-screening:** Customer names are periodically re-screened against updated sanction lists; a customer innocent at onboarding may become sanctioned later.

## When monitoring triggers re-screening or remediation

Ongoing monitoring is not passive observation. When a red flag emerges, the institution investigates and may take action:

**Mild concerns:** If monitoring reveals a transaction that is unusual but plausible (e.g., a business owner who normally receives domestic transfers suddenly receives a wire from a new foreign supplier), the compliance team may reach out to the customer for a business explanation.

**Escalated concerns:** If a pattern suggests money laundering, sanctions evasion, or terrorist financing, the institution files a Suspicious Activity Report (SAR) with FinCEN (within 30 days), typically without notifying the customer (tipping off is prohibited).

**Risk rating upgrades:** If periodic reassessment reveals that a customer's risk has increased (e.g., a business customer enters a high-risk jurisdiction), the institution may:
- Increase ongoing monitoring frequency
- Require enhanced due diligence (EDDue diligence)
- Impose transaction limits or request additional documentation
- In extreme cases, terminate the relationship

**Account closure:** If the risk becomes unmanageable or a customer is found to be sanctioned, the account may be closed, though the institution must follow regulatory procedures and often must file a SAR before closing.

## Common differences in practice

| Aspect | Onboarding | Ongoing Monitoring |
|--------|-----------|-------------------|
| **Frequency** | Once, at account opening | Continuous, lifetime of account |
| **Action trigger** | New account request | Transaction activity, periodic review |
| **Information source** | Customer provided + external databases | Customer transactions + market data + news |
| **Decision** | Approve or reject account | Escalate, investigate, file SAR, upgrade risk, or close |
| **Reversibility** | Account not opened if rejected | Remediation possible; account can be downgraded or closed |

## Periodic vs automated monitoring

**Periodic reassessment** (often annual) is a manual review of the customer's overall risk profile. Has their business changed? Have they moved? Has their net worth decreased? This is human judgment informed by updated information.

**Automated monitoring** runs transaction rules continuously. Most deposits over $10,000 trigger a threshold report; all wire transfers over $100,000 are logged; transactions to countries on the SDN list are blocked outright.

The two complement each other. Automation catches volume spikes and obvious red flags. Periodic manual review catches subtle patterns that algorithms might miss (e.g., "this retiree never transacted with Jamaica, but now receives $5,000 wires every week").

## The role of customer risk rating

At onboarding, each customer receives a risk rating:
- **Low-risk:** A salaried employee with a local address, no foreign connections, small transactions.
- **Medium-risk:** A small business, regular international transactions, or a customer in a moderate-risk jurisdiction.
- **High-risk:** A politically exposed person, a business in a high-risk jurisdiction, someone with a complex beneficial ownership structure, or a customer in a sanctioned country.

The risk rating determines the *intensity* of ongoing monitoring. A low-risk customer might be reassessed annually; a high-risk customer might be reviewed quarterly or more often.

## Enhanced due diligence (EDD)

When ongoing monitoring reveals that a customer's risk has elevated—or if they were initially rated high-risk—the institution may trigger Enhanced Due Diligence (EDD). This is deeper investigation than standard onboarding:
- Additional verification of beneficial owners
- Detailed source of funds documentation
- Site visits or third-party validation of the customer's business
- More frequent transaction review
- Approval requirements for large or unusual transactions

EDD is resource-intensive and typically reserved for genuinely concerning cases.

## Why these are legally distinct

The [Bank Secrecy Act](/aml-onboarding-vs-ongoing-monitoring/) and FinCEN guidance treat onboarding and ongoing monitoring as separate obligations. Institutions must:
- Have written policies for customer identification (onboarding)
- Have written policies for ongoing monitoring and suspicious activity reporting
- Train staff on both
- Audit compliance with both

An institution can pass onboarding but fail ongoing monitoring (e.g., opening accounts correctly but never detecting money laundering), or vice versa. Regulators grade each separately. Fines often reflect failures in one or both.

## See also

<div class="wiki-seealso">

### Closely related

- [AML Compliance Framework](/aml-onboarding-vs-ongoing-monitoring/) — The broader regulatory structure governing AML programs
- [KYC (Know Your Customer)](/aml-onboarding-vs-ongoing-monitoring/) — The identity verification cornerstone of onboarding
- [Suspicious Activity Report (SAR)](/aml-onboarding-vs-ongoing-monitoring/) — Filed when ongoing monitoring detects suspicious behavior
- [OFAC Sanctions List](/aml-onboarding-vs-ongoing-monitoring/) — The primary tool for sanction screening
- [Beneficial Ownership](/aml-onboarding-vs-ongoing-monitoring/) — Identified during onboarding; re-verified in ongoing monitoring
- [Politically Exposed Persons (PEP)](/aml-onboarding-vs-ongoing-monitoring/) — A high-risk customer category identified at onboarding and monitored closely

### Wider context

- [Bank Secrecy Act](/aml-onboarding-vs-ongoing-monitoring/) — The foundational U.S. statute requiring AML programs
- [Dodd-Frank Act](/dodd-frank-act/) — Extended AML requirements to shadow banking
- [Compliance Exception Reporting](/compliance-exception-reporting-how-it-works/) — The formal process for documenting and escalating monitoring findings
- [Counterparty Risk](/counterparty-risk/) — A related concern in transaction monitoring
- [Sanctions and Embargoes](/aml-onboarding-vs-ongoing-monitoring/) — What sanction screening prevents

</div>
