---
title: "CSD Nominee Structure Explained"
description: "Explains how a CSD holds securities in nominee name for many beneficial owners, the legal implications of layered ownership, and differences from direct registration."
keywords:
  - csd nominee structure
  - nominee structure securities
  - csd nominee holder
  - beneficial owner nominee
  - securities custody
  - settlement and clearing
---

*In most modern securities markets, a central securities depository (CSD) holds shares in its own name—or the name of a single "nominee"—on behalf of thousands of beneficial owners. A retail investor who buys shares through a broker does not receive a printed certificate in their name; instead, the CSD records an electronic entry showing the investor as the beneficial owner, while the depository holds the shares in its nominee name. This layered structure solves operational problems but creates ambiguity: the beneficial owner has economic rights (dividends, voting), but legal title rests elsewhere, and in insolvency or fraud, rights can become contested.*

<div class="wiki-hatnote">

This entry covers the custody structure for dematerialized securities. For the broader settlement process, see settlement and clearing, [custodian](/custodian/), and [distributed ledger](/distributed-ledger/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CSD Nominee Structure — Key Facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A three-tier ownership structure: legal holder, nominee, and beneficial owner.</div>

|   |   |
|---|---|
| **Definition** | CSD holds shares in its own name (or a nominee's) for many beneficial owners |
| **Parties involved** | CSD, nominee (often CSD itself), [custodian](/custodian/), beneficial owner |
| **Dematerialized** | Shares are electronic; no physical certificates change hands |
| **Legal owner** | The nominee (usually CSD); beneficial owner has no direct claim to shares |
| **Economic rights** | Beneficial owner receives dividends, voting rights, but does not hold legal title |
| **Insolvency risk** | Beneficial owner ranks as unsecured creditor in nominee/CSD insolvency |
| **Alternative** | Direct registration (rare in U.S. equities, common in some emerging markets) |

</aside>

## The Three-Tier Ownership Model

Modern securities settlement relies on a three-tier structure:

1. **The CSD or depository**: Holds the shares in its own name or in the name of a nominee.
2. **The nominee**: A legal entity (often the CSD itself, or a subsidiary) that appears as the registered owner in the issuer's cap table.
3. **The beneficial owner**: The investor—individual, fund, or institution—who owns the economic interest but has no direct legal claim to the shares.

When you buy shares through a broker, the flow is:

- You (beneficial owner) instruct your broker to buy.
- Your broker settles the trade through the CSD.
- The CSD (or its nominee) takes legal title to the shares.
- The CSD records you as the beneficial owner in its electronic ledger.
- You receive a statement showing your holding, but no certificate arrives.

The CSD is not acting as a custodian in the traditional sense (holding on your explicit instruction). Instead, the CSD is the *infrastructure* through which all settlement occurs; your beneficial ownership is recorded in the CSD's system, but the CSD itself (or its nominee) is the registered legal owner.

## Why Nominee Structures Exist

Before dematerialization, shares were evidenced by physical stock certificates. A investor held the certificate; the investor's name appeared in the issuer's shareholder register. Settlement meant physically delivering the certificate to the buyer.

Physical settlement became impractical as trading volume grew. Handling millions of certificates daily was expensive, slow, and prone to theft or loss. Dematerialization—converting shares into electronic form—solved this. But dematerialization created a problem: if shares are electronic and held centrally, how do you preserve the legal rights of the individual beneficial owner?

The nominee structure was the solution. A single entity (the CSD or a subsidiary) holds all shares legally, but the CSD's records track who the beneficial owner is. This allows:

- **Rapid settlement**: No need to change the registered owner's name every trade; only the CSD's internal ledger is updated.
- **Netting**: The CSD can net orders and settle in bulk, reducing operational risk.
- **Custody efficiency**: One entity, the CSD, manages custody; brokers and investors do not.
- **Bankruptcy remoteness**: Shares are held by the CSD, a neutral infrastructure entity, not by any single trader or bankrupt broker.

## Legal vs. Economic Ownership

The split between legal and beneficial ownership is the linchpin of nominee structures. Legally, the nominee (CSD) owns the shares. Economically, you do.

As the beneficial owner, you have:

- **Economic rights**: Entitlement to dividends, proceeds from corporate actions.
- **Voting rights**: Ability to vote at shareholder meetings (though voting is often exercised through a proxy or the CSD).
- **Sale rights**: Ability to sell the shares; proceeds go to you.

But you have no *legal title*. If a court issues a judgment against you, the judgment creditor cannot seize the shares directly from the issuer's register—because your name is not on it. The creditor can only attach your beneficial interest held at the CSD.

This separation creates legal gaps. If the CSD becomes insolvent:

- Are your shares part of the CSD's estate, available to the CSD's creditors?
- Or are they ring-fenced as client property, inaccessible to the CSD's creditors?

This depends on how the jurisdiction's law treats nominees. Some jurisdictions (e.g., UK, Netherlands) have strong legal frameworks protecting beneficial owners; others are murkier. In a major insolvency, beneficial owners may rank as unsecured creditors, below secured lenders and employees.

## Contrast with Direct Registration

In a **direct registration** model, the beneficial owner's name appears directly in the issuer's shareholder register. The investor holds legal title, not a nominee.

Direct registration is common in some emerging markets (e.g., India, Brazil) and is available in the U.S. for certain securities, though rarely used for equities. It avoids the legal complexity of nominee structures: if you are the registered owner, you own the shares outright. Insolvency of a custodian or broker cannot affect your ownership.

But direct registration is slower to settle; the issuer's register must be updated for every trade. It is operationally inefficient at large scale.

## Voting and Corporate Actions

When a company declares a dividend, the nominee (CSD) is the legal recipient. The CSD then distributes dividends to beneficial owners according to its records.

When shareholders vote, the nominee's voting power is often exercised via a **proxy voting arrangement**. The CSD appoints a proxy (often itself or a designated agent) to vote on behalf of beneficial owners. Beneficial owners can usually instruct the proxy how to vote, but the infrastructure is indirect.

For certain corporate actions—stock splits, mergers, rights offerings—the CSD processes the action and updates beneficial owners' accounts. The nominee structure allows the CSD to act as a central processor, reducing the issuer's burden of managing millions of individual shareholders.

## Practical Risks and Protections

The nominee structure is robust in stable, well-regulated jurisdictions. But risks persist:

- **Commingling**: All beneficial owners' shares are commingled in the nominee's account. If there is fraud or accounting error, many beneficial owners could be affected simultaneously.
- **Nominee bankruptcy**: Rare, but if the nominee entity itself becomes insolvent, beneficial owners may face delays or losses if the jurisdiction does not ring-fence client property.
- **Regulatory failure**: If the CSD's regulator fails to supervise properly, misconduct (theft, misappropriation) could go undetected.

Protections vary by jurisdiction:
- **DTCC** (U.S.): Operates under Securities and Exchange Commission supervision; participants' assets are segregated and insured.
- **Euroclear/Clearstream** (Europe): Subject to EU settlement regulations; strong legal safeguards.
- **Emerging market CSDs**: Standards vary widely; some face higher counterparty risk.

## Modern Challenges: Blockchain and Direct Ownership

Distributed ledger technology (blockchain) offers an alternative: securities recorded directly to beneficial owners' wallet addresses, with settlement on a peer-to-peer basis rather than via a central CSD.

Early experiments have explored issuing shares or bonds directly on blockchain, with each investor holding legal title in a digital wallet. This eliminates the nominee layer and its legal ambiguities. However, blockchain-based systems currently lack the operational robustness, regulatory clarity, and settlement finality that CSDs provide, so adoption remains limited to niche use cases.

## See also

<div class="wiki-seealso">

### Closely related

- [Custodian](/custodian/) — Entities holding securities on behalf of clients
- Settlement and clearing — The infrastructure that CSD nominee structures enable
- [Distributed ledger](/distributed-ledger/) — Alternative technology for recording ownership
- [Stock](/stock/) — The security being held in nominee structure
- Depository trust — Organizations operating CSD functions

### Wider context

- Beneficial ownership — Concept underlying nominee structures
- [Counterparty risk](/counterparty-risk/) — Risk from reliance on CSD solvency
- [Smart contract](/smart-contract/) — Future technology for automating nominee-like functions
- Securities regulation — Legal framework governing CSDs

</div>
