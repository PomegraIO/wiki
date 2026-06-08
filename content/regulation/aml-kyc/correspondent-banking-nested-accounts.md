---
title: "Nested Accounts in Correspondent Banking"
description: "How third-party banks use correspondent relationships to access payment systems while evading direct oversight, creating AML-KYC compliance gaps and detection methods."
keywords:
  - nested accounts correspondent banking
  - correspondent banking risk
  - aml compliance correspondent banks
  - layered accounts banking
  - indirect access payment systems
  - third-party correspondent exposure
image: "/svg/regulation.svg"
---

*A **nested account** is an account that a third-party bank maintains at a correspondent bank under the name of an intermediary bank, allowing the third party to access the correspondent's payment and settlement services without appearing directly in the relationship or undergoing the same due diligence scrutiny. This structure creates a layered chain of liability and compliance risk that complicates anti-money-laundering oversight.*

Correspondent banking—where one bank ("the correspondent") holds accounts and clears payments on behalf of another bank ("the respondent")—is essential to global finance. It allows smaller regional banks, non-bank financial institutions, or even foreign branches to access payment networks, international settlements, and dollar-denominated processing. But correspondent relationships are also prime vehicles for circumventing compliance controls. One of the most opaque variants is the nested account arrangement, in which a third party routes activity through multiple banks rather than maintaining a direct relationship with the correspondent.

## How Nested Accounts Form

The mechanics are straightforward. Bank A (the correspondent) opens an account for Bank B (the intermediary or agent bank). Bank C (the third-party beneficiary, often a smaller or less-regulated bank, or a non-bank payment processor) then uses Bank B's account to transmit and settle its own payment flows. Bank A sees only Bank B; Bank B becomes the gateway. Bank C avoids direct [credit-risk](/credit-risk/) exposure and avoids triggering Bank A's customer-onboarding requirements.

This layering can occur with or without Bank A's awareness. In some cases, Bank A knowingly accommodates it as a service to Bank B (which may be an affiliate, partner, or client). In others, Bank A's monitoring systems fail to flag it as unusual activity on an otherwise legitimate correspondent account. The key red flag is *indirect beneficial ownership*: Bank C's customers' funds flow through Bank B's account at Bank A, but Bank A has no direct [know-your-customer (KYC)](/know-your-customer/) relationship with Bank C or its end clients.

## Why This Creates Compliance Gaps

Nested accounts fracture the chain of customer identification and beneficial-ownership verification. The [Basel Committee on Banking Supervision](/central-bank/) and the Financial Action Task Force (FATF) expect correspondent banks to:

1. Know their direct customers (respondent banks) through full KYC
2. Understand the respondent's customer base and beneficial owners
3. Monitor for suspicious activity at each layer

Nested structures allow a bank to obscure its true customer base. Bank A audits Bank B's governance and liquidity; Bank B may have done minimal KYC on Bank C; Bank C's end-user clients remain invisible to Bank A. A correspondent bank might inadvertently be settlement partner to money-laundering networks, sanctions evasion schemes, or terrorist financing without ever seeing the underlying actors.

The problem is compounded when the intermediary bank (Bank B) is in a higher-risk jurisdiction, or when Bank B itself is under weak [capital-adequacy](/capital-adequacy/) or governance standards. Bank A's [counterparty-risk](/counterparty-risk/) assessment of Bank B may be sound, but Bank C might be insolvent, unregistered, or complicit in financial crime.

## Regulatory Expectations

In 2015–2016, the Office of the Comptroller of the Currency (OCC) and Federal Reserve focused enforcement attention on nested-account problems, particularly in correspondent relationships with foreign banks. The U.S. regulators emphasized that nested accounts do not exempt the correspondent bank from knowing the beneficial owners and sources of funds flowing through the account.

The [Dodd-Frank Act](/dodd-frank-act/) and subsequent guidance on beneficial-ownership identification require financial institutions to pierce through intermediaries to identify natural-person controllers and beneficiaries. Under the FinCEN rule on beneficial ownership (effective 2024), even non-bank financial institutions must report their beneficial owners to a central registry. This pressure has made nested accounts riskier to maintain and more likely to trigger regulatory scrutiny.

## Detection and Monitoring Methods

Modern correspondent banks use several signals to detect nested-account arrangements:

**Transaction pattern analysis**: If Bank B's account shows activity that is inconsistent with Bank B's stated business (e.g., a regional bank with no foreign-trade operations suddenly routing remittances), the correspondent's monitoring systems should flag it.

**Customer due diligence callbacks**: A correspondent bank should periodically ask Bank B to certify the identities, ownership structure, and customer base for which it is acting. If Bank B's answers don't align with account activity, nested arrangements may be disclosed.

**Wire-transfer compliance**: Under AML-KYC rules, wire transfers must include originator and beneficiary information. If a transfer routed through Bank B's account originates from a bank or customer unknown to Bank A's records for Bank B, the anomaly triggers investigation.

**Third-party testing and audits**: External auditors or consultants hired to stress-test correspondent relationships specifically look for evidence that accounts are being used by entities not listed in the respondent bank's KYC profile.

**Regulatory data-matching**: Central banks and regulators share information about suspicious correspondent accounts. A bank identified as moving illicit funds may prompt inquiries to all its upstream correspondents.

## Risk Mitigation

Correspondent banks now commonly:

- Require explicit contractual language prohibiting third-party use of the account without prior written consent and full KYC
- Implement automated transaction filters that flag activity inconsistent with the respondent bank's declared business
- Conduct periodic "look-through" reviews of the respondent's customer base and beneficial ownership (related to the [look-through requirement](/look-through-requirement-fund-beneficial-ownership/) principle)
- Set strict limits on wire-value thresholds for accounts with elevated nesting risk
- Require sign-off from compliance and credit officers before opening a new correspondent account, with mandatory review of any third-party usage

For respondent banks, the practical upshot is that maintaining a nested-account structure is now far costlier and slower. Many have instead formed direct correspondent relationships with the third-party banks they wish to serve, bringing transparency and reducing the compliance burden on the correspondent bank.

## The Broader Landscape

Nested accounts remain a known vulnerability in the correspondent banking ecosystem, even as detection tools improve. Jurisdictions with weak AML frameworks still enable them, and smaller banks in developing markets may lack the technical infrastructure to monitor their own downstream relationships. This continues to motivate the shift toward direct correspondent relationships and toward blockchain-based settlement systems that could eventually reduce the need for correspondent-banking intermediaries altogether.

## See also

<div class="wiki-seealso">

### Closely related

- [Know Your Customer (KYC)](/know-your-customer/) — Customer identity verification required by regulators
- [Anti-Money Laundering (AML)](/anti-money-laundering/) — Compliance framework to detect illicit financial flows
- [Look-Through Requirement for Fund Beneficial Ownership](/look-through-requirement-fund-beneficial-ownership/) — Obligation to identify ultimate owners through layers
- [Counterparty Risk](/counterparty-risk/) — Credit and operational exposure from correspondent relationships
- Beneficial Ownership — Natural persons who ultimately own or control an entity
- Compliance Risk — Regulatory and legal risks from failed controls

### Wider context

- [Dodd-Frank Act](/dodd-frank-act/) — U.S. financial regulation framework post-2008
- [Federal Reserve](/federal-reserve/) — Central bank overseeing payment systems and bank safety
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — U.S. regulator of securities and disclosure
- Financial Crime Compliance — Broader AML and sanctions enforcement
- [Capital Adequacy](/capital-adequacy/) — Minimum regulatory capital requirements

</div>
