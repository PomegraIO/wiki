---
title: "EU Funds Transfer Regulation: Wire Transfer Rules Explained"
description: "What information payment service providers must include with wire transfers under EU Regulation 2015/847, and how it aligns with the FATF Travel Rule."
keywords:
  - eu funds transfer regulation
  - wire transfer rules compliance
  - payer payee information
  - eu travel rule
  - regulation 2015/847
  - payment service provider
image: "/svg/regulation.svg"
---

*The **EU Funds Transfer Regulation (2015/847)** requires payment service providers to include detailed payer and payee information—names, account numbers, and sometimes addresses—with cross-border wire transfers above certain thresholds. This regulation directly implements the Financial Action Task Force (FATF) Travel Rule, which mandates that all wire transfer intermediaries pass along originator and beneficiary data to combat money laundering and terrorist financing.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">EU Funds Transfer Regulation — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Wires within and into the EU must now carry payer and payee identity information at every hop.</div>

|   |   |
|---|---|
| **Regulation** | EU 2015/847, "Traceability of funds transfers." |
| **Scope** | Applies to all payment service providers (banks, FinTechs) handling transfers in EUR or from/to EU. |
| **Key requirement** | Include payer (originator) and payee (beneficiary) names and account identifiers with the transfer. |
| **Threshold** | All cross-border transfers in EUR; domestic transfers ≥ EUR 3,000. |
| **Alignment** | Implements the FATF Travel Rule at the EU level; similar rules now exist in 100+ jurisdictions. |
| **Compliance deadline** | June 2017 (for financial institutions); extended timelines for some smaller providers. |
| **Enforcement** | Member states' financial intelligence units (FIUs) and regulatory bodies (e.g., FCA, BaFin). |

</aside>

## The Regulation and Its Origins

**EU Regulation 2015/847**, adopted in December 2015 and implemented in June 2017, is the EU's legal instrument for combating financial crime through wire transfer transparency. It requires that all payment service providers—banks, electronic money institutions (EMIs), payment institutions, and crypto exchanges—include originator and beneficiary information on wire transfers.

The regulation emerged from Financial Action Task Force (FATF) mutual evaluation findings. The FATF, an inter-governmental organization fighting money laundering and terrorist financing, identified that wire transfers flowing through intermediaries often lost payer-beneficiary traceability, creating blind spots for law enforcement. Banks in Country A would send funds to banks in Country B, which would forward them to Country C, but the original sender's information might not propagate through the chain. Criminals exploited this opacity.

EU 2015/847 closes that gap by mandating end-to-end data flow. Every intermediary must pass along the originator (payer) and beneficiary (payee) information, creating a traceable chain even when multiple institutions handle a single transfer.

## Required Information: Originator and Beneficiary Data

The regulation specifies exactly what information must travel with the funds:

**Originator (payer) information:**
- Full name
- Account number (IBAN for EU transfers; otherwise a customer reference number unique to the payer)
- Address (sometimes optional if the payer is a financial institution itself)

**Beneficiary (payee) information:**
- Full name
- Account number (IBAN or equivalent identifier)
- Address (sometimes optional for certain beneficiaries)

This data must be included in the **remittance instructions** that accompany the transfer. If a bank sends EUR 50,000 to another bank on behalf of a customer, the originating bank's systems must embed the customer's name, account, and address in the payment message, and each intermediary bank must preserve this information and pass it onward.

The requirement applies to **cross-border transfers in EUR** without exception, and to **domestic transfers exceeding EUR 3,000**. This threshold was set to minimize compliance burden for small domestic transfers while capturing most high-value and all international flows.

## Wire Transfer Chains and Intermediary Obligations

A single wire often passes through multiple institutions:

*Scenario: Alice in Berlin sends EUR 100,000 to Bob in Tokyo.*
1. Alice's bank (Bank A, Berlin) receives the order and initiates the transfer.
2. Bank A sends the funds to its correspondent bank (Bank B, London), which settles with banks in Japan.
3. Bank B routes the funds to Bank C (a Japanese bank), which credits Bob's account.

Under EU 2015/847, **Bank A must include Alice's name, account, and address in the payment message**. **Bank B must preserve this information and pass it to Bank C**. **Bank C must retain the information and make it available to Bob and to Japanese authorities** upon request.

If any intermediary strips or loses the originator data, it violates the regulation. This requirement applies even if an intermediary is outside the EU; if it is handling a transfer involving an EU payer or payment service provider, it must comply.

**Refusal to execute**: If a payment service provider cannot obtain or verify the required information (e.g., the payer withholds their account number), the provider may refuse or freeze the transfer pending clarification. This gives compliance officers a clear legal basis to halt suspicious transfers.

## Alignment with the FATF Travel Rule

The **FATF Travel Rule** (Recommendation 16) is a non-binding international standard that says: "Countries should ensure that financial institutions sending funds obtain and hold originator information... and that receiving institutions obtain beneficiary information."

EU 2015/847 operationalizes this standard at the regional level. The FATF Travel Rule has no enforcement mechanism—it is advice to member states. But the EU transformed it into binding regulation with teeth: member states can fine non-compliant payment service providers.

Notably, the Travel Rule has been adopted or is being adopted by:
- **United States**: FinCEN published guidance in 2019 and 2021 on implementing the Travel Rule for money transmitters and banks.
- **United Kingdom**: Post-Brexit, the FCA maintains similar requirements under Money Laundering Regulations.
- **Japan, Singapore, Switzerland, Canada**: All have implemented comparable rules.
- **Crypto exchanges**: The FATF extended Travel Rule expectations to virtual asset service providers (VASPs), requiring them to pass along transaction originator data—a much harder technical problem since blockchains are pseudonymous.

This global convergence means that a payment service provider operating internationally must comply with EU 2015/847 in EU corridors, FinCEN Travel Rule guidance in USD corridors, and similar rules in other jurisdictions. Fragmentation has been a challenge, but interoperability is improving.

## Technical Implementation and Compliance Challenges

**Legacy systems**: Many banks built payment infrastructure in the 1990s and 2000s, before the Travel Rule existed. Retrofitting these systems to capture, validate, and propagate detailed originator and beneficiary information has been expensive and time-consuming.

**Message formats**: The regulation does not prescribe which technical message format (SWIFT, ISO 20022, etc.) to use, creating flexibility but also confusion. Different corridors and institutions may use different formats, and compatibility issues can delay transfers or force re-keying of data.

**Crypto exchanges**: When funds move from a bank to a crypto exchange (or vice versa), the boundary between regulated and less-regulated systems creates friction. A bank sending USD to an exchange must provide originator information, but the exchange might not have all fields. Similarly, when a user withdraws from an exchange to a self-hosted wallet, no beneficiary institution exists to receive the data—a gap the FATF is still trying to solve.

**Threshold ambiguity**: The EUR 3,000 threshold for domestic transfers in some member states has been interpreted differently. Some national authorities apply it strictly; others build in exemptions for recurring transfers (e.g., salary deposits).

## Penalties and Enforcement

Member states are responsible for enforcement. Penalties vary:
- **Fines** up to EUR 1–5 million or 1–10% of annual turnover for serious or repeated breaches.
- **Freezing of licenses** for payment service providers in persistent non-compliance.
- **Reputational harm**: Public lists of non-compliant firms published by financial intelligence units.

The **European Banking Authority (EBA)** coordinates guidance, and national authorities (e.g., the UK's FCA, Germany's BaFin, France's ACPR) enforce within their jurisdictions. Investigations typically begin when law enforcement or financial intelligence units request transaction data and find that intermediaries lack the required information.

## Exemptions and Special Cases

**Financial institution to financial institution**: If both the sender and receiver are financial institutions, some data requirements can be simplified. The rationale is that the institutions themselves are regulated and supervised, so full originator/beneficiary disclosure to a regulated counterpart is less critical.

**Transfers below thresholds**: Domestic transfers under EUR 3,000 are exempt in most EU member states, reducing compliance burden for small payments and consumer transactions.

**Transfers within a single entity**: Internal transfers—e.g., moving money between a bank's own accounts—are sometimes exempted.

These exemptions are narrow and strictly applied; they do not shield high-risk transfers.

## See also

<div class="wiki-seealso">

### Closely related

- [Anti-Money Laundering Compliance](/securities-and-exchange-commission/) — the broader AML framework that Regulation 2015/847 supports.
- [Dodd-Frank Act](/dodd-frank-act/) — U.S. financial regulation; Travel Rule implementation overlaps with Dodd-Frank surveillance rules.
- [Know Your Customer (KYC)](/securities-and-exchange-commission/) — the foundational data collection that feeds wire transfer origination.
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where Travel Rule implementation is most technically challenging.
- [Counterparty Risk](/counterparty-risk/) — financial institutions must vet counterparts before accepting transfers.

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — U.S. regulator; FinCEN sits within Treasury but coordinates globally on Travel Rule.
- [Bank of America](/bank-of-america/) — large bank navigating global Travel Rule compliance.
- [JPMorgan Chase](/jpmorgan-chase/) — major correspondent bank handling trillions in wires annually.
- [Business Cycle](/business-cycle/) — macroeconomic stress can increase money-laundering risk and trigger enforcement sweeps.
- [Distributed Ledger](/distributed-ledger/) — blockchain-based settlement systems are exploring Travel Rule compliance via cryptographic commitments.

</div>
