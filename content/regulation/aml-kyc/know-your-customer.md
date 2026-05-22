---
title: "Know Your Customer"
description: "Customer identification procedures required to verify identity and assess risk in anti-money-laundering compliance."
keywords:
  - know-your-customer
  - kyc-procedures
  - customer-due-diligence
  - aml-compliance
  - identity-verification
---

*Know Your Customer (KYC) is a regulatory requirement mandating that financial institutions, brokers, and money-services businesses identify and verify the identity of their customers, assess the risk they pose, and monitor their accounts for suspicious activity. It is the foundation of anti-money-laundering and counter-terrorism-financing frameworks worldwide.*

<aside class="wiki-infobox">

| Phase | Requirement | Purpose | Timing |
|-------|---|---|---|
| **Customer Identification Program (CIP)** | Verify identity; collect personal data | Establish who the customer is | At account opening |
| **Customer Due Diligence (CDD)** | Assess risk; understand source of funds | Know the customer's risk profile | At opening + ongoing |
| **Enhanced Due Diligence (EDD)** | Deeper investigation for high-risk customers | Mitigate elevated risk | When triggered |
| **Ongoing Monitoring** | Review activity; file reports if suspicious | Catch illicit activity mid-stream | Continuous |

</aside>

## Customer Identification Program (CIP)

CIP is the initial step: collecting personally identifiable information (PII) and verifying it. A financial institution must:

1. Collect: Name, date of birth, address, identification number (Social Security, passport, national ID).
2. Verify: Cross-check the information against government ID, credit reports, or third-party databases.
3. Record: Maintain the collected information in compliance with retention rules.

For individuals, CIP typically requires a government-issued ID (driver's license, passport). For businesses, it requires proof of incorporation and identification of beneficial owners.

Challenges: identity theft and synthetic identities (fabricated persons using real Social Security numbers). Banks use [multi-factor](/wiki/multi-factor-portfolio/) verification: ID + address + credit check + manual review.

## Customer Due Diligence (CDD)

CDD goes deeper: understanding the customer's risk profile, source of wealth, and purpose of the account.

KYC forms ask questions like:
- What is your occupation and estimated net worth?
- What is the source of funds you plan to deposit (salary, inheritance, business)?
- What is the purpose of the account (retail investing, business operations, international transfers)?
- Do you have politically exposed persons (PEPs) related to you?

Banks use CDD to assign risk tiers:
- **Low risk**: Salaried employee, domestic transfers, modest amounts.
- **Medium risk**: Business owner, international transfers, higher volumes.
- **High risk**: Politically exposed person, complex ownership, large cash deposits, countries of concern.

Higher-risk customers trigger [enhanced-due-diligence](/wiki/enhanced-due-diligence/), more frequent monitoring, and possible account restrictions or closure.

## Enhanced Due Diligence (EDD)

EDD applies when CDD suggests elevated risk. Examples triggering EDD:

- **PEP (Politically Exposed Person)**: Government officials, family members, close associates. PEPs are globally screened; bank relationships require senior approval.
- **Country risk**: Citizens of, or transfers to, countries under [sanctions](/wiki/sanctions-screening/) (Iran, North Korea, Syria, Russia post-invasion) trigger automatic EDD.
- **Source of funds concerns**: Large deposits without clear source, frequent international transfers, round-number amounts suggesting structuring.
- **Business type**: Cash-intensive businesses (casinos, jewelry, real estate) face higher scrutiny.

EDD involves deeper investigation: source-of-funds documentation, beneficial-ownership verification, background checks, law-enforcement queries.

## Beneficial ownership disclosure

Under modern AML regimes (e.g., the U.S. [Corporate-Transparency-Act](/wiki/beneficial-ownership-disclosure/) enacted 2021), financial institutions must identify beneficial owners—the ultimate natural persons who control an account or entity.

A shell company registers with a registered agent; the agent is not the beneficial owner. Banks must pierce the corporate veil to identify who actually controls the entity. This prevents [money-laundering](/wiki/anti-money-laundering/) via shell companies.

Beneficial-ownership disclosure also feeds FinCEN's Customer Identification Database, allowing law enforcement to trace illicit funds across institutions.

## Ongoing monitoring and [Suspicious Activity Reports (SARs)](/wiki/aml-compliance/)

KYC does not stop at onboarding. Banks must continuously monitor accounts for suspicious patterns:
- **Unusual activity**: Deposits far exceeding stated income.
- **Structuring**: Multiple small deposits below reporting thresholds (deliberately avoiding $10k+ triggers).
- **Circular flows**: Money in and out with no apparent business purpose.
- **Sanctions violations**: Transfers involving blacklisted entities or countries.

When suspicious activity is detected, the financial institution files a [Suspicious Activity Report (SAR)](/wiki/aml-compliance/) with FinCEN (in the U.S.) or equivalent authority. SARs are confidential; tipping off the customer is illegal.

Banks maintain SAR tiers: low-risk accounts file SARs for $10k+ suspicious deposits; high-risk accounts trigger SARs at lower thresholds.

## KYC in different sectors

**Banks**: Comprehensive CIP + CDD + ongoing monitoring; subject to federal examiners.

**Brokers/dealers**: SEC and [FINRA](/wiki/finra/) require KYC; the standard is less stringent than banking but still rigorous.

**Money services**: Western Union, PayPal, crypto exchanges; subject to [FinCEN](/wiki/fincen-reporting/) rules and state-level money-transmitter regs.

**Casinos**: Subject to Bank Secrecy Act; must verify high-limit players and file Currency Transaction Reports ([CTRs](/wiki/currency-transaction-reporting/)).

**Crypto exchanges**: Increasingly regulated; must KYC users (though privacy advocates resist); high-risk jurisdictions face delisting.

## Challenges and costs

KYC is burdensome:
- **Cost**: Banks spend billions on compliance annually—hiring compliance staff, investing in identity-verification tech, conducting audits.
- **False positives**: Legitimate activity flags as suspicious, leading to frozen accounts and customer frustration.
- **Regulatory divergence**: Each jurisdiction has rules; multinational firms must maintain variant compliance per jurisdiction.
- **Emerging tech**: Biometric verification, blockchain-based identity, decentralized identity systems are evolving; legacy systems struggle to adapt.

Crypto has illuminated KYC's challenge: decentralized finance (DeFi) has no KYC because there is no central authority to enforce it. This creates a regulatory gap—criminals can use DeFi to launder money, while legitimate users demand privacy.

## Privacy and data protection

KYC collects vast amounts of personal data. Data breaches expose customers to identity theft. The EU's [GDPR](/wiki/gdpr/) constrains how long banks can retain PII; the U.S. has no equivalent. Balancing AML compliance (need data) and privacy (minimize data collection) is an ongoing tension.

## Gatekeeping role

Banks act as *gatekeepers* in the AML system. They are the first line of defense against illicit flows. If banks fail to KYC and file SARs, criminals evade detection. Conversely, if banks are overly aggressive, they can exclude legitimate customers (a phenomenon called "de-risking" in the developing world, where banks close correspondent accounts with risky jurisdictions).

<div class="wiki-seealso">

### Closely related
- [Anti-Money-Laundering](/wiki/anti-money-laundering/) — The broader AML compliance framework.
- [Customer Due Diligence](/wiki/customer-due-diligence/) — Deeper customer risk assessment.
- [Enhanced Due Diligence](/wiki/enhanced-due-diligence/) — EDD for high-risk customers.

### Wider context
- [Sanctions Screening](/wiki/sanctions-screening/) — Checking against blacklists.
- [AML Compliance](/wiki/aml-compliance/) — Operational anti-money-laundering programs.
- [Beneficial Ownership](/wiki/beneficial-ownership-disclosure/) — Identifying true owners.

</div>
