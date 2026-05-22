---
title: "Sanctions Screening"
description: "Process of checking customer identities against government-issued lists of sanctioned individuals and entities."
keywords:
  - sanctions screening
  - aml compliance
  - kyc procedures
  - government sanctions lists
---

*Sanctions screening is a compliance procedure that checks every customer, transaction partner, and beneficial owner against government sanctions lists to identify and block transactions with individuals or entities under economic sanctions. Financial institutions must perform this check at account opening, during ongoing [customer due diligence](/wiki/customer-due-diligence/), and for certain outbound payments.*

<aside class="wiki-infobox">

| Element | Detail |
|---------|--------|
| **Regulatory bodies** | OFAC (US), UN, EU, UK, others by jurisdiction |
| **Screening frequency** | At onboarding; ongoing for periodic reviews |
| **False positive rate** | Often 1–5% depending on name-matching precision |
| **Primary lists screened** | OFAC SDN, UNSC, consolidated EU/UK lists |
| **Penalties for failure** | Fines up to tens of millions, criminal liability |
| **Matched records** | Typically trigger transaction hold or account freeze |

</aside>

## The regulatory mandate

Under [anti-money laundering](/wiki/anti-money-laundering/) (AML) and [sanctions compliance](/wiki/aml-compliance/) rules, financial institutions are legally required to screen customers. In the US, the [Office of Foreign Assets Control (OFAC)](/wiki/cfpb-regulator/) publishes the Specially Designated Nationals (SDN) list—thousands of individuals and entities subject to US economic sanctions. Institutions that process payments must check whether the sender, receiver, or beneficiary appears on that list. The same applies to [United Nations sanctions](/wiki/country-risk/), European sanctions, and UK sanctions lists. A match—or even a reasonable suspicion of a match—requires the institution to block the transaction and file a [suspicious activity report](/wiki/anti-bribery-compliance/).

## Name matching and false positives

Sanctions screening is technically a name-matching problem. A customer provides "John Smith" and an address; the system queries the government list for "John Smith." But names have variant spellings, transliteration issues (Arabic and Cyrillic characters), and common overlap. The same "Ali Mohamed" appears on sanction lists and in millions of legitimate customers. Precision matters: too strict and legitimate customers get blocked (friction); too lenient and sanctions evasion slips through (legal exposure). Most institutions use multiple-field matching (name + date of birth + nationality + address) to reduce false positives, but rates of 1–5% are typical. Each match triggers a manual review by a compliance officer.

## Ongoing monitoring and beneficial ownership

Initial screening at account opening is just the start. Institutions must re-screen periodically—quarterly or annually—against updated government lists, since sanctions lists grow and change. Additionally, [beneficial ownership](/wiki/beneficial-ownership-identification/) rules require identification of the true individuals behind corporate accounts. If a customer creates a shell company and later the company's CEO is sanctioned, the institution must detect that link and freeze the account. This ongoing surveillance is labor-intensive and increasingly automated by [compliance testing](/wiki/compliance-testing-regime/) software that cross-references customer records against the latest lists.

## OFAC and beyond

In the United States, OFAC under the Treasury Department is the primary sanctions authority. But many large financial institutions also screen against:
- **UN Sanctions Committees** — Lists of entities sanctioned under resolutions.
- **EU and UK lists** — Particularly relevant for cross-border payments to Europe.
- **Consolidated lists** — Third-party aggregators combine OFAC, UN, and regional lists into a single searchable database.

A US bank processing a wire to London must check not just OFAC, but potentially UK and EU sanctions too. Multinational institutions screen against dozens of lists simultaneously.

## Transaction holds and regulatory reporting

When a name matches a sanctions list, the typical workflow is:
1. **Auto-hold** — The transaction is blocked pending review.
2. **Manual investigation** — A compliance officer verifies whether it is a true positive (the customer really is sanctioned) or a false positive (name collision, variant spelling).
3. **Escalation** — If likely a true positive, the institution files a "[Suspicious Activity Report](/wiki/fincen-reporting/)" (SAR) or notification to OFAC.
4. **Account freeze** — If the customer themselves are sanctioned, the entire account is typically frozen and the customer is notified (though timing can be sensitive for enforcement reasons).

False positives lead to customer friction but are preferable to missing a true positive, which can result in fines of tens of millions of dollars, as well as criminal liability for knowing sanctions evasion.

## Technology and automation

Modern sanctions screening is entirely automated. When a customer initiates a wire transfer, the system instantly queries the transaction details (names, addresses, amounts) against sanctions databases. Results come back in milliseconds. Most matches are auto-cleared as false positives (common names). True hits are escalated to human review. Some institutions use [machine learning](/wiki/algorithmic-trading/) to improve matching accuracy by learning patterns in historical false positives. Advanced systems also track beneficial owners and apply [sanctions screening](/wiki/gatekeeping-role-aml/) to wire-transfer intermediaries, not just the direct parties.

## Challenges and cost

Sanctions screening, while mandatory, is expensive and operationally burdensome. The compliance teams needed to review matches, maintain list feeds, and document reviews are substantial. Smaller institutions often outsource to third-party compliance vendors. The volume of false positives means significant manual review—a compliance officer might spend 70% of their time clearing false hits from "Smith" or "Mohamed" name collisions. Additionally, the geopolitical environment changes quickly; new sanctions are announced, requiring updates within hours. An institution that fails to update its screening list faces [regulatory liability](/wiki/financial-regulation-and-supervision/).

<div class="wiki-seealso">

### Closely related
- [Anti-Money Laundering](/wiki/anti-money-laundering/) — Broader regulatory framework encompassing sanctions screening
- [Customer Due Diligence](/wiki/customer-due-diligence/) — Initial and ongoing customer verification
- [Know Your Customer](/wiki/kyc/) — Identification and verification of customer identity
- [Beneficial Ownership Identification](/wiki/beneficial-ownership-identification/) — Tracing true owners of accounts

### Wider context
- [Financial Regulation and Supervision](/wiki/financial-regulation-and-supervision/) — Regulatory oversight of financial institutions
- [Compliance Testing Regime](/wiki/compliance-testing-regime/) — Audit and compliance verification procedures
- [Enhanced Due Diligence](/wiki/enhanced-due-diligence/) — Heightened verification for high-risk customers

</div>
