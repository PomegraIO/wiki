---
title: "Virtual Asset Service Provider"
description: "FATF-regulated entity category that subjects crypto exchanges and custodians to anti-money-laundering compliance and licensing requirements."
keywords:
  - virtual asset service provider
  - vasp
  - fatf
  - aml-compliance
  - crypto-regulation
  - travel-rule
  - financial-action-task-force
image: "/svg/crypto.svg"
---

*A **Virtual Asset Service Provider** (VASP) is any business that offers custody, transfer, or exchange services involving crypto assets — defined by the Financial Action Task Force as entities whose primary business activity includes accepting, holding, or transferring virtual assets on behalf of customers. The VASP framework is the most consequential global regulatory category for crypto platforms.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Virtual Asset Service Provider — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for financial regulation and cryptocurrency." />

<div class="wiki-infobox-caption">FATF's primary tool for extending AML rules into crypto market infrastructure.</div>

|   |   |
|---|---|
| **Definition source** | Financial Action Task Force (FATF) Guidance on Virtual Assets (2019) |
| **Regulatory scope** | Exchanges, custodians, wallet providers, payment processors, coin mixers |
| **Primary obligation** | Anti-money-laundering licensing, customer identification (KYC), transaction reporting |
| **Travel rule** | VASPs must collect and transmit customer identity data on transfers >$3,000 (proposed) |
| **Enforcer** | National financial regulators and AML supervisors; FATF sets standards, members enforce |
| **Compliance cost** | Scales with firm size; medium platforms typically spend $1–10M+ annually on compliance stack |

</aside>

## Why FATF created the VASP category

The Financial Action Task Force — an intergovernmental 39-member organisation focused on combating financial crime — recognised in 2019 that traditional AML rules assumed bank accounts and licensed institutions. Crypto platforms operated in legal grey zones: a exchange could process billions in daily volume with no KYC, no transaction reporting, and no licence. This created both genuine crime risk and regulatory arbitrage: criminals could convert fiat to crypto, move it across borders, and re-cash it with minimal trace.

The VASP definition extended the banking rulebook into crypto. If you run an exchange, hold customer assets, or facilitate transfers on behalf of users, you are a VASP and subject to the same AML licensing regimes as banks. This shift moved crypto from a regulatory footnote to a regulated financial infrastructure category.

## What activities make you a VASP

The FATF definition is functional, not technical. You are a VASP if you:

- **Accept and transfer virtual assets on behalf of customers.** Running an exchange, a hosted wallet service, or a payment processor all qualify. A private custody service holding only your own funds is not a VASP.
- **Accept fiat deposits and convert them to crypto.** The on-ramp itself triggers VASP status, even if you don't hold the crypto afterward.
- **Commingle customer assets or operate a hot wallet with customer funds.** Self-custodial wallet software (e.g., MetaMask) where you hold only your own keys is not VASP-regulated. But a custodian holding keys or operating a shared wallet is.
- **Run a mixing or tumbling service.** Deliberately obscuring the origin of funds makes you an even higher-risk VASP.

Non-custodial protocols, decentralised exchanges, and peer-to-peer direct transfers fall outside the definition — you're not a business accepting customer assets. But in practice, regulators often blur these boundaries, subjecting founders and node operators of ostensibly decentralised platforms to licensing pressure.

## The travel rule and transaction reporting

The VASP framework's most operationally burdensome rule is the "[travel rule](/)" — a FATF requirement that when you initiate a transfer above a threshold (commonly $3,000, though some jurisdictions set lower limits), you must collect the name, account number, and address of the customer on the sending side and pass that information to the receiving VASP. Think of it as the crypto equivalent of wire transfer compliance.

In traditional banking, correspondent banks embed this data in the wire message itself. In crypto, the data must travel off-chain via a separate channel, API, or custody protocol. Smaller platforms and non-custodial services struggle because they have no way to collect or verify the customer sending the funds.

The travel rule remains only partially implemented globally. Most exchanges comply with major jurisdictions (USA, EU, UK), but enforcement is fragmented and enforcement of received transactions is weaker than enforcement of sent ones.

## Licensing and jurisdictional fragmentation

FATF sets the standard; national regulators enforce it. The result is a patchwork:

- **USA**: VASPs must register with FinCEN and comply with [Securities and Exchange Commission](/securities-and-exchange-commission/) or [Commodity Futures Trading Commission](/)-style licensing depending on asset type. State-level money transmitter licences add 50+ additional regimes.
- **EU**: The Markets in Crypto Regulation (MiCA) treats VASPs as financial institutions requiring authorisation.
- **Singapore, Hong Kong, Switzerland**: Tiered licensing for retail platforms and professional custodians.
- **Unco-operative jurisdictions**: Smaller islands and developing economies offer lax or no VASP licensing, attracting platforms that want to avoid compliance.

A single global platform typically needs 10–20+ licences, each requiring annual reporting, audits, and local compliance staff. This cost favours consolidation: large exchanges can amortise licensing across millions of users; small platforms face regulatory barriers to entry.

## Customer identification and record-keeping

All VASPs must implement know-your-customer (KYC) rules and maintain records. This means:

- Verifying customer identity (passport, government ID, facial recognition) before allowing deposits or withdrawals.
- Collecting beneficial ownership information for corporate accounts.
- Maintaining transaction logs indefinitely.
- Filing suspicious activity reports (SARs) if unusual behaviour is detected.

Non-custodial platforms and privacy-preserving services often reject VASP classification explicitly to avoid these obligations, positioning themselves outside the financial system. This has created a two-tier ecosystem: regulated "banking-like" platforms (Coinbase, Kraken) with high operational cost but access to traditional banking infrastructure, and unregulated alternatives that tolerate higher payment friction and regulatory risk.

## The debate over stablecoin issuers

A contentious question: is a stablecoin issuer a VASP? FATF treats issuance as VASP activity, meaning stablecoin issuers must hold reserves and maintain governance fitting licensed entities. This has pushed issuers toward banking partnerships (as [Tether](/tron/) and [USDC](/)-issuing Circle have done) and away from purely on-chain issuance. Some jurisdictions (notably El Salvador, briefly) exempted certain stablecoins from VASP rules, but this is the exception.

## Compliance cost and market impact

The VASP framework has created a multi-billion-dollar compliance industry: audit firms, KYC software vendors, transaction monitoring platforms, and regulatory consulting. For a large exchange processing millions of transactions monthly, compliance can cost $5–50M annually.

The compliance burden has directly affected market structure. Geographic arbitrage in crypto has narrowed because major platforms are regulated in the same jurisdictions. Decentralised finance (DeFi) has grown partly as a regulatory alternative, since many DeFi protocols genuinely don't fit the VASP definition. And custodial services remain concentrated: Coinbase, Kraken, and a handful of others hold the majority of retail-custodied crypto globally because they can afford compliance.

## See also

<div class="wiki-seealso">

### Closely related

- [Know Your Customer compliance](/)-entry covering the identification rules VASPs enforce
- [Anti-money laundering](/)-regulation covering the crime-detection obligations behind VASP licensing
- [Cryptocurrency exchange](/)-entry on how platforms operate under VASP framework
- [Stablecoin](/)-entry on regulatory status of stablecoin issuers as VASPs
- [Financial Action Task Force](/)-entry on the intergovernmental organisation setting VASP standards

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — technical foundation for understanding asset transfer
- [Cryptocurrency regulation by jurisdiction](/)-entry on how rules vary globally
- [Proof of stake](/proof-of-stake/) — consensus model relevant to chain governance and custody
- [Distributed ledger](/distributed-ledger/) — technical architecture underlying VASP networks

</div>
