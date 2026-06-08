---
title: "Travel Rule for Crypto"
description: "FATF's mandate for virtual asset service providers to transmit originator and beneficiary data on transfers above threshold amounts."
keywords:
  - travel rule
  - virtual asset service provider
  - fatf
  - crypto compliance
  - aml
  - originators and beneficiaries
image: "/svg/crypto.svg"
---

*The **Travel Rule** is a Financial Action Task Force (FATF) recommendation that requires virtual asset service providers (VASPs) to transmit originator and beneficiary information—name, address, account number—whenever they move crypto above a certain threshold for a customer. Originally written in 1989 for wire transfers in traditional finance, the FATF extended it to crypto in 2019, creating a compliance headache for exchanges, custodians, and wallet operators that few have fully resolved.*

The Travel Rule's intent is clear: prevent money laundering and terrorism financing by ensuring the same customer data flows with a transaction through crypto rails as it does through banks. But implementation has been contentious because crypto was built to eliminate intermediaries, not add compliance teams. Eight years after the FATF codified the rule, most jurisdictions still lack a working technical standard, and enforcement remains patchy.

## Why FATF wrote it for crypto at all

In 2019, the Financial Action Task Force issued updated guidance treating cryptocurrency transfers the same as traditional wire transfers. The original Travel Rule, born in 1989 for fiat wire systems, simply required banks to pass along basic originating and receiving customer information. The FATF reasoned: a transfer is a transfer. If a terrorist or launderer can move millions through crypto without any originator data attached, the AML apparatus—which relies on tracing money flows—becomes useless.

The rule targets VASPs: any entity that holds crypto on behalf of customers or exchanges it for fiat or other crypto. That includes exchanges, custodians, lending platforms, and some wallet providers. It does not apply to self-hosted wallets (a deliberate gap that crypto enthusiasts exploited). Transfers between two individuals' own wallets need not comply—the rule only binds institutional intermediaries.

## The threshold and what gets transmitted

Most jurisdictions set the threshold at transfers above USD 3,000 or EUR 3,000. Below that floor, the Travel Rule does not apply. Above it, the originating VASP must obtain and send to the beneficiary's VASP:

- The originator's name, address, and account identifier (usually a wallet address)
- The beneficiary's name, account identifier, and address (if available)

This seems straightforward on paper. In practice, attaching data to a blockchain transaction is impossible—a Bitcoin transfer is a ledger entry, not a message. VASPs therefore built off-chain channels: API bridges, messaging protocols, and shared databases to hand off customer information before the transaction settles on-chain. But no single standard dominated. Corridors between major exchanges might work; corridors between a small exchange and a decentralised protocol adapter remain broken.

## Who must comply and where it matters

Compliance depends on jurisdiction and regulation. The European Union mandated Travel Rule compliance in its Markets in Crypto-Assets Regulation (MiCA); most EU VASPs comply, though unevenly. The United States has not yet codified the Travel Rule into federal law, leaving compliance to the Financial Crimes Enforcement Network (FinCEN) guidance and state regulators—a patchwork that has delayed adoption. Japan, Singapore, and the UAE have implemented versions. Many smaller jurisdictions have not yet required it, creating arbitrage: lightly regulated exchanges in those regions see higher inbound and outbound crypto volume from users seeking to avoid the compliance burden.

The Travel Rule's biggest impact hits exchanges sending to peer exchanges, and exchanges sending to unhosted wallets. If a customer withdraws to a private wallet address, the sending exchange still must attempt to obtain the receiving-side customer data—or refuse the withdrawal. Many exchanges now ask customers to verify that receiving addresses are their own before processing large withdrawals; others simply block withdrawals above the threshold unless the customer confirms the address. Neither approach is perfect, but both reduce Travel Rule friction.

## Unresolved technical and practical problems

Seven years into FATF guidance, no single messaging standard has achieved dominance. The open-source project InterVASP, the proprietary protocol Notabene, and a handful of proprietary exchange-to-exchange APIs each serve portions of the market. A VASP must integrate with multiple protocols to cover its counterparties—expensive and time-consuming. Smaller exchanges and newer chains often have no compliance infrastructure at all.

Privacy remains contested. Some argue that attaching full customer identity to a blockchain address undermines crypto's pseudonymity and makes all future transactions from that address traceable. Others counter that the Travel Rule need not be public: customer data travels off-chain, and the on-chain transaction remains a wallet address. But suspicion persists that linking identity once creates permanent surveillance. That tension has slowed adoption among privacy-focused communities and driven volume toward unregulated offshore venues.

Unhosted wallet transfers pose a unique problem. If a customer sends crypto to their own hardware wallet or to a peer's wallet for personal reasons, the sending VASP has no way to obtain beneficiary customer data—the wallet is not held by a VASP. Most major exchanges have responded by restricting large withdrawals to previously whitelisted addresses or requiring additional verification. This effectively freezes access to self-hosted wallets for high-frequency large withdrawals, a loss of one crypto's promised benefits but a pragmatic VASP response.

## Enforcement and where the rule actually works

Enforcement is strongest in the EU under MiCA. Regulators conduct on-site exams and can levy fines for non-compliance. US enforcement has been lighter: FinCEN has issued guidance but has not brought major enforcement actions specifically for Travel Rule failures, though it may do so as standards mature. Most enforcement to date has been indirect—a VASP ordered to improve AML controls is told Travel Rule compliance is part of that order.

The rule works best between large regulated exchanges in compliant jurisdictions. Transfers between Coinbase and Kraken, for instance, travel with full Travel Rule compliance. But transfers to emerging-market exchanges, decentralised platforms, or unregulated venues remain largely untraced. That partial compliance—where regulated corridors are safe and unregulated ones are not—is the current state. It reduces, but does not eliminate, the risk of AML evasion.

## See also

<div class="wiki-seealso">

### Closely related

- [MICA Regulation](/mica-regulation/) — The EU's licensing and disclosure framework for crypto issuers and service providers.
- [Crypto Self-Employment Tax](/crypto-self-employment-tax/) — When trading or mining triggers self-employment tax liability.
- [Crypto FBAR and FATCA Reporting](/crypto-fbar-fatca/) — Foreign account disclosure requirements for offshore crypto holdings.
- Anti-Money Laundering — The global compliance regime the Travel Rule enforces.
- Virtual Asset Service Provider — Definition and scope of entities subject to the Travel Rule.

### Wider context

- Sanctions and Crypto — How OFAC restrictions affect exchanges and custody.
- Decentralised Finance and Regulation — Why DeFi platforms struggle with Travel Rule compliance.
- [Bitcoin](/bitcoin/) — The original crypto asset whose transfers first prompted the rule.
- [Ethereum](/ethereum/) — The most-transacted blockchain outside Bitcoin.
- [Stablecoins](/stablecoin/) — Asset-backed tokens where Travel Rule compliance matters most.

</div>
