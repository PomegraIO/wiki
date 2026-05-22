---
title: "Customer Due Diligence"
description: "Extended verification of higher-risk customers to identify beneficial owners and assess financial crime risk."
keywords:
  - customer due diligence
  - KYC
  - AML compliance
  - beneficial ownership
---

*The **customer due diligence (CDD)** is an enhanced know-your-customer process that financial institutions apply to higher-risk account holders, requiring detailed verification of identity, beneficial ownership, and source of funds. CDD is a core requirement under [AML compliance](/wiki/aml-compliance/) regimes globally.*

<div class="wiki-hatnote">For the foundational KYC process, see <a href="/wiki/know-your-customer/">Know Your Customer</a>. For the broader AML framework, see <a href="/wiki/anti-money-laundering/">Anti-Money Laundering</a>.</div>

<aside class="wiki-infobox">

| Element | Standard | Enhanced (CDD) |
|---|---|---|---|
| **Identity verification** | Document + database check | Biometric, third-party confirmation, ongoing monitoring |
| **Source of funds** | Assumed; not documented | Verified; traced to legitimate source |
| **Beneficial ownership** | 25%+ threshold | May require deeper tracing; structures investigated |
| **PEPs (politically exposed persons)** | Basic check | Detailed screening; source verification |
| **Documentation** | Annual refresh | Updated quarterly or on significant transaction |
| **Frequency of review** | At account opening; periodic | Continuous; triggered by activity flags |

</aside>

## What triggers enhanced due diligence?

CDD is mandatory for account types and customer profiles deemed higher-risk. Triggers include:

**Politically exposed persons (PEPs)**: Individuals holding prominent public office (ministers, judges, generals, heads of state) pose inherent risk due to bribery and corruption exposure. Their families and close associates are also covered. A financial institution must verify that their wealth is legitimate and monitor transactions for unusual patterns.

**Corporate vehicles of unclear beneficial ownership**: Shell companies, offshore vehicles, trusts with obscured beneficial owners, and entities in high-corruption jurisdictions require tracing to identify the true controller. Layers of companies can hide [money laundering](/wiki/anti-money-laundering/) or sanctions evasion.

**High-risk jurisdictions**: Countries on FATF grey or black lists (or designated by OFAC, FinCEN) trigger enhanced scrutiny. A customer with business operations in North Korea, Syria, or other sanctioned areas faces automatic CDD requirements.

**Unusual transaction patterns**: A dormant account that suddenly receives a $5 million transfer, or a retiree conducting daily large cash deposits, triggers CDD review. The institution must understand the source and purpose.

**Third-party customer acquisition**: When a bank acquires another bank's customer book, or when a correspondent banking relationship is established, CDD is often applied to inherited customer bases to assess risk.

## The CDD process: practical steps

**1. Identify beneficial ownership**: For corporate accounts, the institution must trace through all ownership layers to identify the natural person who ultimately owns or controls the entity. If a holding company owns 25% of a subsidiary, the institution traces the holding company's owners. Trusts must be opened to identify grantors, trustees, and beneficiaries.

**2. Verify source of wealth**: For high-net-worth customers and business-account holders, the institution requests documentation showing how the customer accumulated wealth. A mining executive should have records of mining revenues and equity sales. A professional should show licensing and employment records. If documentation is unavailable or contradictory, the risk is elevated.

**3. Screen against sanctions and PEP databases**: The customer and beneficial owners are screened against:
- OFAC Specially Designated Nationals (SDN) list
- UN, EU, UK, and other sanctions lists
- World Bank Politically Exposed Persons (PEPs) databases
- FATF grey and black lists
- FinCEN lists and alerts

Positive matches require escalation and often account closure.

**4. Assess political or corruption risk**: CDD for PEPs includes inquiry into the political context. A minister in a high-corruption country poses higher risk than a mayor in a transparent jurisdiction. The institution assigns a risk score reflecting the risk environment.

**5. Document source of funds**: For large transactions or account openings, the customer provides a written statement or documentation showing the source of the funds entering the account. This might be:
- Equity sale proceeds (with evidence of sale)
- Loan documentation (with lender details)
- Business revenues (with tax returns and business records)
- Inheritance (with probate or estate documentation)

**6. Continuous monitoring**: CDD does not end at account opening. The institution monitors transaction patterns for changes and flags unusual activity. If a previously dormant customer suddenly increases transaction volume, or if transaction patterns change materially, CDD review is refreshed.

## Beneficial ownership identification

A recurring challenge in CDD is identifying beneficial owners hidden by corporate structures. The beneficial owner is the natural person who ultimately owns or controls the entity, as opposed to the legal (registered) owner.

**Corporate structures**: A company's shares may be held by another company, which is held by a trust, which is held by another corporate entity. CDD requires tracing this chain to the human at the top. If the chain cannot be traced, the account is typically closed or restrictions are applied.

**Trusts**: Who is the beneficial owner of a trust? The beneficial owner may be the trustee, the beneficiary, the grantor, or some combination. CDD requires clarification. A revocable trust (grantor controls it) has a different beneficial owner than an irrevocable charitable trust (beneficiaries are beneficiaries; grantor has limited control).

**Layered vehicles**: Offshore structures often include multiple corporate layers to obscure beneficial ownership. A company in the British Virgin Islands (BVI) owns 20% of a Delaware corporation, which owns 15% of a Panama entity, which owns a stake in a Singapore entity, which owns the bank account. CDD requires unwinding all layers, which can be time-consuming and may require hiring investigators.

**Beneficial ownership thresholds**: Regulators typically use a 25% ownership threshold. An entity with a 25%+ owner is reported; smaller owners are assumed to be passive. However, lower thresholds (15%, 10%) are used in some jurisdictions or for higher-risk entities.

## Enhanced due diligence for specific sectors

Financial institutions apply sector-specific CDD variations:

**Trade finance and import-export**: Importers and exporters are screened for trade-based money laundering risk. Documentation of goods shipment, bill of lading, and correspondence with suppliers is reviewed. Unusual routes (purchasing from one country for sale in a geographically close competitor) raise suspicion.

**Real estate and property**: Beneficial ownership of property investors is verified. CDD includes on-site visits and verification of property legal title. Cash purchases of high-value property (especially in major financial centers) trigger enhanced scrutiny.

**Casinos and gaming**: Gaming facilities are required to apply CDD to high-value customers and patrons making large cash transactions. Cash-based operations are inherently higher-risk for money laundering.

**Correspondent banking**: When a bank provides services to other banks (especially in high-risk jurisdictions), CDD on the correspondent bank is extensive. The correspondent bank's beneficial owners, risk management, and compliance record are verified.

## Regulatory frameworks and enforcement

CDD is mandated under:

- **USA**: [Bank Secrecy Act](/wiki/aml-compliance/) (1970), as amended by [USA PATRIOT Act](/wiki/anti-money-laundering/) (2001); FinCEN rules
- **EU**: 4th and 5th Money Laundering Directives; FATF Recommendation 10
- **UK**: [Money Laundering Regulations](/wiki/aml-compliance/) (2017)
- **FATF**: 40 Recommendations on AML and combating terrorist financing

Non-compliance carries severe penalties. Banks have paid multi-billion-dollar fines for CDD failures:
- **HSBC** (2012): $1.9 billion for failing to apply CDD in Mexico operations, allowing drug cartel money laundering.
- **Deutsche Bank** (2015): $630 million for failings in AML controls, including CDD.
- **Westpac** (2020): $700 million for deficient CDD and customer risk assessment.

Regulators conduct periodic audits and enforcement actions to ensure CDD compliance.

## Technology and CDD: eKYC and automation

The industry has evolved toward electronic CDD (eKYC) and automation to reduce friction and improve accuracy:

- **Digital identity verification**: Biometric matching (facial recognition, fingerprints) against government-issued ID databases
- **Beneficial ownership screening**: Software that crawls corporate registries and cross-references company directors against PEP lists
- **Sanctions screening**: Real-time screening of customer names against updated sanctions lists; automated alerts for matches
- **Risk scoring**: Machine learning models that assess customer risk profiles and assign risk scores

These tools improve speed and consistency but require careful calibration. False positives (incorrectly flagging a customer as high-risk) can result in account closures and reputational harm. False negatives (missing actual risks) can result in regulatory penalties.

## Challenges and ongoing evolution

**Privacy vs. transparency**: CDD requires collection of detailed personal information. Regulators must balance the need to combat money laundering against privacy rights and data protection regulations (GDPR in the EU, state privacy laws in the US).

**Cross-border coordination**: Beneficial ownership records are fragmented across jurisdictions. A company registered in Delaware may have beneficial owners in five countries. No single global registry exists, making CDD investigations costly and time-consuming.

**Corruption in source countries**: If a PEP's wealth came from corruption in their home country, detecting it requires investigation in that jurisdiction, which may be hostile or lack transparent records.

**Cost and burden on small institutions**: CDD compliance requires investment in technology, training, and investigative staff. Smaller financial institutions struggle to bear these costs, reducing competition and potentially pushing customers to unregulated channels.

<div class="wiki-seealso">

### Closely related
- [Know Your Customer](/wiki/know-your-customer/)
- [Anti-Money Laundering](/wiki/anti-money-laundering/)
- [AML Compliance](/wiki/aml-compliance/)
- [Beneficial Ownership Identification](/wiki/beneficial-ownership-identification/)

### Wider context
- [Enhanced Due Diligence](/wiki/enhanced-due-diligence/)
- [Politically Exposed Persons](/wiki/gatekeeping-role-aml/)
- [Bank Secrecy Act](/wiki/aml-compliance/)
- [Sanctions Screening](/wiki/sanctions-screening/)

</div>
