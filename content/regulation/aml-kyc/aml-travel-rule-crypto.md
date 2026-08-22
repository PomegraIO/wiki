---
title: "AML Travel Rule for Crypto Transfers"
description: "AML Travel Rule for cryptocurrency: FATF requirements for virtual asset providers to share originator and beneficiary information on transfers above the threshold."
keywords:
  - aml travel rule cryptocurrency
  - fatf travel rule crypto
  - virtual asset service provider
  - crypto transfer reporting
image: /svg/regulation.svg
---

*The FATF Travel Rule requires virtual asset service providers (VASPs) to exchange originator and beneficiary information when customers transfer cryptocurrency above certain thresholds — replicating the wire-transfer reporting mandate for traditional banking. Unlike bank wires, which move through standardized SWIFT rails, crypto transfers happen on public [blockchains](/blockchain-fundamentals/)), so compliance requires new infrastructure and coordination.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FATF Travel Rule for Crypto — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation topics." />

<div class="wiki-infobox-caption">FATF rules require originator and beneficiary identity sharing for large crypto transfers, mirroring traditional wire-transfer rules.</div>

|   |   |
|---|---|
| **Issuing body** | Financial Action Task Force (FATF); not a law, but guidance adopted by most countries |
| **Trigger threshold** | Transactions ≥ $3,000 USD equivalent; some jurisdictions set different floors |
| **Required data** | Originator name, originator account, beneficiary name, beneficiary account |
| **Transmission method** | Not standardized (SWIFT doesn't exist for crypto); VASPs use APIs, messaging, or custodians |
| **Scope** | Transfers between VASPs; unaffected if both parties use the same exchange |
| **Enforcement** | By national regulators (SEC, CFTC, FinCEN in U.S.); varies by jurisdiction |

</aside>

## What the FATF Travel Rule is and where it came from

The "Travel Rule" originated in 1989 in U.S. banking regulation (31 CFR 1020.210). When a bank sends a wire transfer, it must include the sender's name, account, and the recipient's information — so the receiving bank knows who sent the money. The rule combats money laundering) and terrorist financing by preserving a clear chain of identity.

In 2015, the Financial Action Task Force (FATF) — an intergovernmental body focused on combating financial crime — updated its recommendations to include virtual assets and [cryptocurrency exchanges](/cryptocurrency-exchange/)). Recommendation 16 requires countries to ensure virtual asset service providers apply the same originator and beneficiary information requirements as traditional financial institutions.

By 2023, most major jurisdictions had adopted the Travel Rule in law or regulation. The U.S. implemented it through FinCEN guidance (May 2023) for money transmitters. The EU embedded it in MiCA (Markets in Crypto-Assets). Hong Kong, Singapore, Japan, and others followed suit. Compliance is now a material operational and legal requirement for any VASP handling significant transaction volume.

## Who must comply: VASPs and unhosted wallets

The Travel Rule applies to **virtual asset service providers** — entities that hold, custody, or facilitate the transfer of customer cryptocurrency. This includes:

- Centralized exchanges (Coinbase, Kraken, Binance, FTX before its collapse).
- Custody providers and asset managers (Fidelity, Grayscale, Gemini).
- Payment processors integrating crypto (Strike, Flexa).
- Staking services and DeFi protocols offering custody.

The rule **does not directly apply to unhosted wallets** — self-custody private keys held by individuals. If an individual sends crypto from a personal wallet to an exchange, the individual is not a VASP and has no Travel Rule obligation. However, the receiving VASP must still identify the sender (or treat it as a high-risk transaction).

A transaction between two customers of the same VASP does not trigger the Travel Rule, because the VASP already knows both parties. The rule applies to **transfers between VASPs** — when customer A at Exchange 1 sends crypto to customer B at Exchange 2.

## The data requirement

The rule mandates that the originating VASP transmit, and the beneficiary VASP receive, the following information:

- **Originator name** and account identifier (often the customer's account ID, wallet address, or email).
- **Beneficiary name** and account identifier.

Some regulators (including FinCEN's guidance) also ask for originator and beneficiary addresses, birth dates, or account opening dates, though the core four fields are the foundation.

The originating VASP must verify the beneficiary's information with the receiving VASP *before* transmitting the funds, or ensure transmission and verification occur together. This differs from traditional banking, where the receiving bank verifies information *after* receipt; crypto's pseudonymous nature requires forward verification.

## Compliance challenges: no SWIFT equivalent

Traditional wire transfers flow through SWIFT, a standardized, closed network with agreed-upon message formats and routing. When a U.S. bank sends a wire to a German bank, both use SWIFT MT103 messages; the receiving bank verifies the sender's identity through SWIFT and correspondent banking relationships.

Cryptocurrency, by contrast, uses public blockchains. A transaction broadcast to the Bitcoin or Ethereum network is immutable and does not pause for identity verification. The blockchain only records addresses (pseudonymous identifiers), not names or account details.

This gap created a compliance problem. A VASP cannot encode Travel Rule data directly into a blockchain transaction without creating privacy leaks (broadcasting customer names on a public ledger violates GDPR) in Europe and conflicts with FinCEN guidance in the U.S., which discourages putting PII on-chain).

Instead, VASPs developed alternative transmission methods:

1. **Direct API communication.** Exchange A calls Exchange B's API, submitting originator/beneficiary data before releasing the blockchain transaction.
2. **Third-party intermediaries.** Protocol providers like Notabene, TrustExceptions, and Sygna Bridge built compliance layers that VASPs plug into, handling data transmission and storage.
3. **On-chain data anchoring.** Some projects encode hashes of Travel Rule data on-chain (not the PII itself), with the full data held in a private database.
4. **Custodian networks.** Large institutional custodians (Fidelity, Coinbase Custody) handle Travel Rule data transmission between clients.

## Threshold rules and the $3,000 benchmark

The FATF standard is $3,000 USD equivalent, though jurisdictions can set higher thresholds. The U.S. FinCEN guidance mirrors this; the EU's MiCA implements a lower threshold of €1,000 (roughly $1,100 USD) for some purposes.

The threshold is evaluated at the time of the transaction. If the crypto's market price fluctuates after the transfer is committed, the original price at the time of transfer determines applicability. Some guidance allows for a reasonable short-term reference rate (e.g., the midpoint between bid and ask at the moment of transmission).

Structuring transactions to avoid the threshold — deliberately splitting one $5,000 transfer into five $900 transfers — is a red flag for suspicious activity and may trigger AML) investigations. Regulators assume that repeated small transfers among the same parties are intentional avoidance.

## Sanctions screening and originator risk

Beyond basic identity information, VASPs must also screen both originator and beneficiary against sanctions lists (OFAC in the U.S., EU Consolidated List in Europe) and AML) watchlists. If the originator or beneficiary is sanctioned or matches a known fraudster, the VASP must block or freeze the transaction.

This creates operational friction: a VASP cannot release a transfer to another VASP until it has confirmed that both parties are not sanctioned. If the beneficiary's VASP later discovers the originator was sanctioned, it may face regulatory scrutiny for having processed the transaction.

Many VASPs now require the beneficiary VASP to confirm beneficiary identity *and* sanctions screening before the originating VASP broadcasts the transaction. This synchronous verification adds latency (transfers may take minutes instead of seconds) but reduces post-transfer regulatory risk.

## Self-hosted wallet challenges and the "unhosted wallet" debate

A complicating case: customer A at Exchange 1 sends crypto to a self-hosted wallet (unhosted wallet) they control. The receiving VASP (Exchange 2) is not in the picture; instead, the customer self-custodies.

Under FinCEN's guidance, the originating VASP must still perform Travel Rule obligations: it must collect and record the name and account information of the beneficiary. In this case, the originator is the customer; the beneficiary is themselves, at a self-hosted address.

Some regulators proposed stricter rules: prohibit VASPs from sending to unhosted wallets unless the customer first proves they own the wallet. This would require customers to sign a cryptographic message proving private-key control. Several proposed rules (notably, New York's BitLicense) took this approach, creating massive operational burden.

After industry pushback and practical testing, most regulators have relaxed this stance. Current guidance typically allows a VASP to send to an unhosted wallet *if* the sending customer attests that they own it, though the VASP must keep records of that attestation.

## Cross-border complexity

The Travel Rule applies to transfers that cross VASP boundaries, regardless of geography. A customer in Singapore sending crypto to a customer in California triggers it; so does a transfer within the same country between two different exchanges.

However, enforcement and interpretation vary by jurisdiction. Some countries (El Salvador, for a time) were crypto-permissive and did not implement Travel Rule rules. Others (China, Russia) prohibited crypto exchanges entirely. This creates fragmentation: a VASP operating globally must comply with the strictest rules among all jurisdictions its customers inhabit, or exit high-compliance regions.

The EU's MiCA is stricter than the U.S. FinCEN guidance in some respects; a U.S. exchange serving European customers must meet MiCA's Travel Rule requirements for those customers, even if more demanding than FinCEN's baseline.

## Practical impact on customer experience

In practice, the Travel Rule has introduced visible friction:

- **Withdrawal delays.** A customer withdrawing from an exchange to an unhosted wallet must now supply the exchange with an attestation. The exchange verifies this before releasing funds, adding 15 minutes to 24 hours.
- **Destination verification.** Exchanges require the customer to specify the destination wallet address *and* confirm they control it.
- **Reduced anonymity.** The privacy of crypto transfers has decreased; most VASPs now hold detailed records of which customer owns which wallet address, traceable to on-chain activity.
- **Reduced custody flexibility.** Some customers can no longer seamlessly move crypto between exchanges or custodians; the receiving entity must be a Travel Rule-compliant VASP.

## Ongoing evolution: stablecoins and unhosted wallets

As **stablecoins** and tokenized assets grow, regulators are debating whether Travel Rule rules should apply. The EU's MiCA specifies that Travel Rule requirements apply to transfers of "significant stablecoins." The U.S. has not yet issued definitive guidance, though the trend is toward inclusion.

Also evolving: **unhosted wallet regulations.** The EU's travel rule requirements in MiCA include stricter rules on customer-to-unhosted-wallet transfers, with enhanced verification and record-keeping. The U.S. FinCEN has not gone as far but continues to monitor.

Some jurisdictions and privacy advocates have questioned whether Travel Rule rules are compatible with GDPR) and privacy laws, since the rule requires VASPs to store and share customer PII. This debate will likely intensify as regulatory frameworks mature.

## See also

<div class="wiki-seealso">

### Closely related

- AML and KYC — the broader anti-money-laundering and know-your-customer framework
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — the regulated entities responsible for Travel Rule compliance
- [Blockchain Fundamentals](/blockchain-fundamentals/) — the technical substrate for crypto transfers
- Sanctions — OFAC and other sanctions lists that VASPs must screen against
- MiCA (EU Regulation) — the European Markets in Crypto-Assets regulation implementing Travel Rule rules
- Money Laundering — the financial crime that Travel Rule is designed to combat

### Wider context

- FATF (Financial Action Task Force) — the international body issuing Travel Rule guidance
- Wire Transfer Rules — the traditional banking precedent for the Travel Rule
- FinCEN (Financial Crimes Enforcement Network) — the U.S. agency implementing Travel Rule guidance
- Regulatory Compliance for Crypto — broader crypto regulatory landscape

</div>
