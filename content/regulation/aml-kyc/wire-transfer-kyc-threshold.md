---
title: "Wire Transfer KYC Threshold Rules"
description: "Dollar thresholds triggering KYC collection and verification of originator and beneficiary details on domestic and international wire transfers under AML rules."
keywords:
  - wire transfer kyc threshold
  - aml know your customer requirements
  - wire transfer originator information
  - beneficiary verification rules
  - cross-border wire transfer limits
  - bank kyc obligations
image: /svg/regulation.svg
---

*The **wire transfer KYC threshold requirement** sets out the dollar amounts above which banks must collect, verify, and transmit information about who is sending and receiving funds. For domestic transfers, the rules are relatively lenient; for cross-border wires, the thresholds are lower and the compliance burden is much heavier, reflecting the heightened money-laundering risk on international flows.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Wire Transfer KYC Thresholds — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Banks must identify and verify both sides of a wire at specific dollar levels to prevent illicit fund movement.</div>

|   |   |
|---|---|
| **Domestic wires** | No amount threshold; originating bank must verify originator identity |
| **International wires** | All amounts trigger originator and beneficiary information requirements |
| **Originator detail** | Name, account number, address, identification |
| **Beneficiary detail** | Name, account number, and institution routing details |
| **Penalties** | Sanctions, civil liability, and criminal prosecution for violations |
| **Enforcement** | [SEC](/securities-and-exchange-commission/), FinCEN, banking regulators via [FINRA](/finra/) |

</aside>

## Domestic wire transfer KYC rules

Under the Patriot Act and the Bank Secrecy Act (BSA), banks must maintain Know Your Customer (KYC) procedures that verify the identity of their customers. For domestic wire transfers, the compliance rule does not hinge on a dollar amount; rather, banks must implement reasonable procedures to verify the identity of any customer sending funds.

In practice, this means the originating bank must confirm that the person or entity initiating the wire is who they claim to be. If the customer has an established account relationship, the bank typically relies on pre-existing identity verification. If the wire comes from a new customer, the bank must collect and verify identification before processing—a passport, driver's license, EIN, or other government-issued credential.

The originating bank is not required to send originator information with domestic wires (though many do voluntarily for audit trails). The receiving bank is not obligated to verify the information. The threshold for heightened scrutiny kicks in for international wires or for transactions that trigger Suspicious-Activity-Reports (SARs) based on dollar size or pattern.

## International wire transfer KYC and originator-beneficiary rules

Cross-border wires trigger much stricter compliance. The Dodd-Frank Act (Section 1028) and subsequent guidance from the Federal Reserve and the Office of the Comptroller of the Currency (OCC) require that banks obtain, verify, and transmit **originator and beneficiary information** on all international wires.

**Originator information required:**
- Name and account number (if any)
- Address of the originator
- Identification number (passport, national ID, tax ID, or driver's license)

**Beneficiary information required:**
- Name and account number (if any)
- Address of the beneficiary (or, if unknown, statement that address is unavailable)
- Beneficiary institution routing details (SWIFT code, ABA number, or equivalent)

The originating bank must include this information in the wire instruction sent to the next bank in the payment chain. Each intermediary bank must preserve the information and pass it along; the receiving bank must receive and retain it.

There is no dollar threshold for these requirements: all international wires, regardless of amount, must include originator and beneficiary KYC data. A $100 transfer from New York to London must be accompanied by the same documentation as a $10 million wire.

## Enhanced due diligence and higher-risk thresholds

While no hard dollar threshold applies to basic originator-beneficiary rules, banks apply risk-based triggers for enhanced due diligence (EDD):

- **Transactions $10,000 and above** to certain jurisdictions or beneficiary types may prompt additional scrutiny, including verification of the beneficiary's beneficial ownership and source of funds.
- **Correspondent banking arrangements** (a bank in one country holding an account at a bank in another) face heightened standards and must conduct EDD before opening or maintaining the relationship.
- **High-risk jurisdictions** (those designated by the Financial Action Task Force or the U.S. Treasury) trigger EDD at lower thresholds or even blanket restrictions.

## Recordkeeping and retention

Banks must retain records of all wire transfer data—originator, beneficiary, and amount—for at least five years. For international wires, banks must maintain the full originator and beneficiary KYC information in a format that allows them to produce it on demand to regulators.

The [SEC](/securities-and-exchange-commission/) and [FINRA](/finra/) conduct regular examinations of broker-dealer wire-transfer compliance. Violations can result in:
- Cease-and-desist orders
- Civil penalties (often millions of dollars)
- Criminal prosecution for knowing violations
- Customer restitution if funds were diverted through negligence

## Intermediary bank responsibilities

When a wire passes through multiple banks before reaching the final destination, each intermediary bank is responsible for preserving and forwarding originator and beneficiary information. If an intermediary fails to pass along the data, it has violated the rule—even if the originating bank provided it.

Large banks operating as SWIFT participants or correspondent banks maintain automated systems that parse wire instructions and extract KYC data. Smaller banks or non-bank payment services may struggle with compliance if they lack the infrastructure. Fintech firms that offer money transfer have become significant vectors for non-compliance, leading to enforcement actions and the requirement to partner with licensed banks.

## Exceptions and special cases

**Established customer accounts:** If both originator and beneficiary are established customers of their respective banks, and the banks have pre-existing KYC files, some guidance allows for streamlined verification. However, the originator-beneficiary data must still be transmitted on the wire.

**Domestic wires to international accounts:** A U.S. bank sending a domestic wire to a U.S. branch of a foreign bank typically follows domestic rules. But if the funds are then moved internationally from that branch, the second leg is subject to international rules.

**Beneficial ownership transparency:** Increasingly, regulators expect banks to verify not just that the named customer is real, but who ultimately owns or controls the account. This is especially true for company accounts and trust accounts, where the account holder may be a shell entity.

## FinCEN guidance and enforcement trends

The Financial Crimes Enforcement Network (FinCEN) publishes regular advisories on high-risk originator-beneficiary patterns:
- Requests to send funds to a different beneficiary than originally stated (a red flag for fraud)
- Wires from high-risk jurisdictions or to shell-company beneficiaries
- Structuring: multiple small wires that circumvent the $10,000 Currency-Transaction-Report (CTR) threshold, even though wire transfers themselves have no dollar threshold

Violations discovered in examinations often result in Matters Requiring Attention (MRAs) or formal enforcement. The largest recent penalties have involved correspondent banks that failed to implement adequate filters and received wires from sanctioned entities or high-risk jurisdictions.

## See also

<div class="wiki-seealso">

### Closely related

- AML and KYC fundamentals — core anti-money-laundering and customer verification rules
- Beneficial ownership and shell companies — verifying who truly controls accounts
- Correspondent banking and settlement — international bank-to-bank transfers
- Sanctions compliance and blocked parties — preventing wires to restricted entities
- Suspicious Activity Reports (SARs) — when and how banks report suspicious wires
- Bank Secrecy Act compliance — broader anti-money-laundering framework

### Wider context

- Financial Crime Enforcement Network (FinCEN) — regulator overseeing wire compliance
- SWIFT and international payments — the system that carries cross-border wires
- Regulatory penalties and enforcement — consequences of KYC violations

</div>