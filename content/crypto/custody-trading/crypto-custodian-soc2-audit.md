---
title: "SOC 2 Audits for Crypto Custodians"
description: "What SOC 2 Type II reports cover for crypto custodians, why institutional investors require them, and what they do and do not verify."
keywords:
  - soc 2 audit crypto custodian
  - soc 2 type ii crypto
  - institutional crypto custody
  - crypto asset security audit
  - custodian compliance
  - crypto security standards
image: "/svg/crypto.svg"
---

*A **SOC 2 audit** is an independent security assessment of a **crypto custodian's** controls over data security, availability, and operational integrity. Institutional investors—funds, corporations, platforms—nearly universally require a SOC 2 Type II report before committing digital assets, yet the audit does not verify custody process correctness, individual private-key security, or regulatory compliance by the custodian.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">SOC 2 for Crypto Custodians — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency and digital assets." />

<div class="wiki-infobox-caption">An institutional gatekeeping standard that has become the market norm for crypto custody, though with important limitations.</div>

|   |   |
|---|---|
| **Type I** | Snapshot audit covering a point in time (6 months of controls) |
| **Type II** | Rolling audit covering 6–12 months of control operation (institutional standard) |
| **Covers** | Security, availability, processing integrity, confidentiality, privacy |
| **Auditor** | Big Four or equivalent CPA firm, independent of custodian |
| **What it does verify** | Control design and operation, access logs, incident response, segregation of duties |
| **What it does NOT verify** | Custody functionality accuracy, individual key protection, regulatory suitability, against fraud |
| **Typical cost** | $50K–$300K+ depending on scope and custodian size |
| **Institutional requirement** | De facto standard for >$1M+ digital asset custody |

</aside>

## What SOC 2 Actually Is

SOC 2 stands for Service Organization Control 2, a framework developed by the American Institute of CPAs (AICPA) for assessing the control environment of service providers—in this case, custodians holding digital assets on behalf of clients. The report is issued by an independent certified public accountant after auditing the custodian's control design and operation over a defined period.

A **Type II report** (the institutional standard) certifies that the custodian maintained specified controls *in operation* for at least 6 months, typically 12. This is materially different from a Type I ("snapshot") report, which attests to control design at a single point in time. Institutional investors are willing to trust only Type II because Type I proves almost nothing about whether a company actually runs the controls it claims.

The audit examines five "trust service criteria": security, availability, processing integrity, confidentiality, and privacy. A custodian may be audited against all five or a subset (typically security and availability are mandatory; the others depend on custodian design and customer requirements).

## What a SOC 2 Type II Report Covers

A SOC 2 Type II engagement examines the custodian's systems, policies, and personnel behavior. Auditors will review:

- **Access controls**: Who can access private keys, systems, and data; how are credentials issued, revoked, and monitored?
- **Change management**: How are software updates, configuration changes, and infrastructure modifications approved and tracked?
- **Segregation of duties**: Are key generation, signing, approval, and monitoring split across different staff members?
- **Physical security**: How are hardware wallets, key-management systems, and data centers protected against unauthorized entry?
- **Incident response**: Does the custodian have a documented process for detecting and responding to breaches?
- **System monitoring and logging**: Are all material operations logged and reviewed for anomalies?
- **Cryptographic key management**: Are keys generated, stored, and destroyed according to documented standards?
- **Disaster recovery and business continuity**: Can the custodian restore operations after a failure?

Auditors will interview staff, test system logs and approval workflows, and verify that documented procedures are actually followed. They issue a detailed report describing the control environment, any deficiencies found, and whether controls operated effectively throughout the measurement period.

## What SOC 2 Does NOT Verify

Institutional investors often harbor misconceptions about SOC 2's scope. The report does **not**:

- **Verify that custody transactions are correct.** A custodian with excellent access controls and segregation of duties can still send tokens to the wrong address, execute a faulty smart contract, or lose coins through operational error. SOC 2 audits the *environment*, not the output.
  
- **Guarantee that private keys are actually secure.** SOC 2 checks whether the custodian *claims* to use hardware wallets or HSMs, and whether they log and control access to those devices. It does not independently verify that the devices have not been compromised, nor does it audit the chip-level firmware or cryptographic implementations.
  
- **Attest to regulatory compliance.** A custodian with a pristine SOC 2 report may still fail to comply with [SEC](/securities-and-exchange-commission/) custody rules, FinCEN regulations, or state money-transmission laws. SOC 2 is a technical-operational standard, not a regulatory one.
  
- **Cover fraud or insider theft.** If a custodian's CFO has a key-signing privilege and walks out with the private keys, SOC 2 will show that the control system granted that person access (correct). It will not prevent the crime. A SOC 2 audit is forgiving of insider threats if the insiders are authorized.
  
- **Assess the custodian's financial solvency.** SOC 2 does not review balance sheets, insurance policies, or entity structure. A custodian with perfect controls could still go bankrupt and be unable to return assets.

## Why Institutional Investors Require It

Despite its limitations, institutional adoption of SOC 2 as a gatekeeping requirement for crypto custody has been nearly universal since around 2018. The reasons:

1. **Standardization.** SOC 2 is a recognized, defined standard auditable by multiple firms. It gives institutional compliance officers a checklist to tick.

2. **Due diligence shortcut.** Evaluating a custodian's security from first principles requires deep technical expertise (hardware security module design, key-ceremony protocols, incident response procedures). SOC 2 outsources that work to a Big Four firm.

3. **Insurance and indemnification.** Some digital asset insurance policies require SOC 2 Type II as a condition of coverage. This creates downstream pressure to require SOC 2 from custodians.

4. **Regulatory tailwind.** While SOC 2 itself is not a regulatory requirement, regulators (SEC, OCC) have called it a "reasonable industry standard" for custody of institutional assets. Institutions requiring SOC 2 also satisfy regulatory expectations.

5. **Market consensus.** Once a few major funds and platforms required SOC 2, it became a competitive necessity. Custodians without SOC 2 lost deal flow.

## The Audit Process and Timeline

A SOC 2 engagement typically proceeds as follows:

1. **Scoping (2–4 weeks).** The custodian and auditor agree on which systems, locations, and trust service criteria are in scope. A crypto custodian might scope only US data centers, or include global facilities.

2. **Interim testing (2–3 months).** Auditors interview staff, review policies, test access logs and change approval, and verify that the described environment matches reality.

3. **Measurement period (6–12 months).** The custodian operates under observation. Auditors periodically sample logs, approval records, and incidents to verify that controls are working as described.

4. **Final fieldwork and issuance (1–2 months).** Auditors complete final testing, draft the report, and issue the final attestation.

The total timeline from initial engagement to report issuance is typically 12–18 months. Cost scales with custodian size and scope; small custody providers might spend $50K, while large global custodians spend $300K+.

## Exclusions and Limitations of Scope

Smart institutional investors scrutinize the *scope* of a SOC 2 engagement. A custodian may have a SOC 2 Type II report covering its US infrastructure, but not its international operations, third-party integrations, or disaster-recovery sites. If an investor's assets are held partly in an unaudited facility, the report is only partially relevant.

Additionally, a SOC 2 audit is **not** a penetration test. Auditors do not attempt to hack systems or bypass controls. They verify that stated controls are in place and operating; they do not independently simulate an adversary attack.

## See also

<div class="wiki-seealso">

### Closely related

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — trading platforms that often also provide custodial services
- [Custodian](/custodian/) — institutional entity holding assets on behalf of a client
- [Digital Asset Insurance](/cryptocurrency-exchange/) — coverage often contingent on SOC 2 compliance
- [Distributed Ledger](/distributed-ledger/) — underlying technology that custodians secure
- [Blockchain Fundamentals](/blockchain-fundamentals/) — consensus and cryptography underlying custody

### Wider context

- [Bitcoin](/bitcoin/) — the original digital asset and primary custody use case
- [Ethereum](/ethereum/) — smart-contract platform raising custody complexity
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — institutional trading infrastructure
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator establishing custody expectations

</div>
