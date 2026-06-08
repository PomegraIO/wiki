---
title: "Soulbound Token"
description: "A non-transferable, non-sellable blockchain token permanently tied to a single wallet address, used for verifiable credentials and reputation."
keywords:
  - soulbound token
  - non-transferable token
  - on-chain credential
  - verifiable reputation
  - wallet identity
image: "/svg/crypto.svg"
---

*A **soulbound token** (SBT) is a blockchain token that cannot be transferred, sold, or given away once issued—it is permanently bound to the wallet that minted or received it. Also called a "soul," the receiving wallet is the immutable holder. Soulbound tokens encode verifiable credentials (university degrees, professional licenses, attestations of conduct) on-chain, creating a portable record of identity and reputation without requiring a centralised issuer.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Soulbound Token — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for on-chain identity and credentials." />

<div class="wiki-infobox-caption">A non-transferable token encoding an on-chain credential tied permanently to a wallet address.</div>

|   |   |
|---|---|
| **What it is** | Non-transferable ERC-721 or ERC-1155 token tied to a single wallet ("soul") |
| **Core property** | Cannot be sold, given, or transferred; mint, hold, or burn only |
| **Use cases** | Educational credentials, professional licenses, membership, community status, voting history |
| **Issuer** | Any entity (university, corporation, DAO, protocol) can mint SBTs to wallets |
| **Revocation** | Most SBTs allow the issuer to revoke, but cannot be transferred by the holder |
| **Standard** | Non-standard; proposed in ERC-5192 and various implementations |

</aside>

## The core mechanic: non-transferability as a feature

In traditional blockchain tokens, non-fungible tokens (NFTs) are freely transferable. You can sell an NFT on OpenSea, gift it, or use it as collateral. This flexibility is valuable for collectibles and digital art but inappropriate for credentials.

A soulbound token inverts this. The smart contract explicitly prohibits transfer: if Alice receives an SBT from a university asserting she has a master's degree, Alice owns it permanently. She cannot sell it to Bob or hide it. Bob cannot claim Alice's credential by paying for it. The token is an immutable claim about Alice's identity or achievement, locked to her wallet address (her "soul").

Technically, a soulbound token is often a modified ERC-721 (NFT standard) or ERC-1155 (semi-fungible standard) with the `transfer` and `approve` functions disabled or overridden to revert. Only the token's issuer can mint (issue) or revoke (burn); the holder has no exit.

## Why soulbound tokens matter for identity

Blockchain credentials have long faced a fundamental problem: how do you prove you are who you claim to be without a centralised authority (a government, a company, a school)?

Soulbound tokens solve this by making identity and credentials inseparable from a wallet address. When MIT issues an SBT to Alice's Ethereum address attesting to her graduation, anyone can query the blockchain and verify the claim instantly, without asking MIT. The credential is self-hosted; Alice controls her wallet key and thus proof of ownership.

This has implications for autonomous systems. A decentralised organisation (DAO) can require members to hold a specific SBT (e.g., an attestation of good standing) to vote or access services. A lending protocol can offer lower interest rates to borrowers with high-reputation SBTs. A community can use SBTs to track contributions and distribute benefits accordingly.

For individuals in countries with weak institutional infrastructure, soulbound tokens are a way to build a portable, censorship-resistant record of credentials. A refugee can carry proof of their medical degree across borders without relying on a government registry.

## Issuance and revocation: who vouches for you

A soulbound token's value depends entirely on the issuer's credibility. If a random wallet issues an SBT claiming you are a doctor, it is worthless. If Harvard issues one, it carries weight.

This creates a **certificate-of-authority problem**: how do you know the issuer is legitimate? In traditional systems, a government oversees and certifies universities. On-chain, there is no authority; instead, reputation accrues over time. A wallet that has issued millions of high-quality credentials earns trust. An unknown wallet's credentials are ignored.

Some protocols attempt to solve this by establishing **issuer registries**—lists of "verified" issuers vetted by a DAO or consortium. But this re-introduces centralisation: who controls the registry? This tension between decentralisation and credibility is unresolved.

Revocation is another critical feature. If someone misrepresents themselves (a fake doctor), the issuer should be able to revoke their SBT. Most soulbound systems allow issuers to burn tokens they've minted, removing the credential. But revocation is not instantaneous; revoking an SBT requires an on-chain transaction that takes time and costs fees. A person with a revoked SBT might temporarily use it before the revocation is visible.

## Use cases: where soulbound tokens add value

**Educational credentials** are the most natural fit. A university issues SBTs to graduates, encoding their degree and graduation date on-chain. Employers can verify credentials instantly without contacting the university. Graduates carry the credential across borders and job platforms.

**Professional licenses** follow the same model. A bar association issues SBTs to attorneys; a medical board issues them to physicians. The credential is portable and always verifiable.

**Community membership and status** use SBTs to track participation. A DAO issues SBTs to early contributors, encoding how many governance tokens they helped bootstrap. These SBTs might unlock benefits (airdrops, voting power, status badges) without being sellable.

**Voting history and contribution records** can be encoded in SBTs. A protocol that issues an SBT for each proposal you voted on creates a permanent record of your participation, useful for assessing influence or rewarding long-term participants.

**Attestations of conduct** are more nuanced. An employer might issue an SBT attesting to an employee's performance, but only with the employee's consent. A financial counterparty might issue an SBT confirming you paid a loan on time, building a credit history on-chain.

Less successfully, some projects have tried to use SBTs for **anti-Sybil mechanisms**—proving you are one unique human, not multiple accounts. The idea is that a protocol issues one SBT per verified person, and contracts can check you hold only one. In practice, verifying identity on-chain without privacy violations is hard; most anti-Sybil SBTs rely on centralised identity providers (World ID, BrightID), which reintroduces the intermediary problem.

## Privacy, consent, and the downside

Soulbound tokens create a persistent on-chain record of your credentials, visible to anyone querying the blockchain. This is a feature for transparency but a liability for privacy.

Imagine an SBT encoding that you received substance-abuse treatment, or that you filed for bankruptcy, or that you were fired from a job. Anyone can see this by querying your wallet's SBT history. In some countries, this public credential might harm your opportunities unfairly.

Privacy solutions exist (zero-knowledge proofs allowing you to prove you have an SBT without revealing details, encrypted SBTs that only you can read), but they are nascent and not widely implemented.

Consent is another issue. If an issuer can unilaterally mint an SBT to your wallet, you might receive credentials you didn't ask for or approve. Early soulbound systems mostly require the recipient to mint the token themselves (you visit a link, approve the transaction, and the SBT is issued to your wallet). But protocols could be designed to allow push issuance, creating a risk of unwanted tagging.

## The broader identity problem: verifiable claims vs. truth

A soulbound token proves that an issuer made a claim about you on a specific date. It does not prove the claim is true. If a corrupt university issues fake SBTs, they are still SBTs—verifiable but false.

This is why soulbound tokens work best in systems where:
1. The issuer is incentivised to be honest (reputation matters, or they face legal liability).
2. Multiple issuers can compete and specialise (you can get credentials from different sources, reducing concentration of power).
3. Verification is cheap (anyone can independently audit the issuer's standards).

In cases where issuers lack strong incentive to be truthful—or where verification is expensive—soulbound tokens are less useful.

## Comparison to traditional credentials

Traditional credentials (diplomas, certificates, licenses) are physical or held by a registry. To verify one, you contact the issuer, which takes days and costs money.

Soulbound tokens are instant and free to verify, assuming you have wallet software. But they depend on blockchain infrastructure; if Ethereum fails or is inaccessible, your SBTs are locked away.

Traditional credentials are private by default (you choose what to share). Soulbound tokens are public by default (anyone can query your wallet). Privacy-preserving SBTs are emerging but require more effort to deploy.

## Standards and adoption barriers

Soulbound tokens lack a widely-adopted standard. ERC-5192 proposes a standard for non-transferable tokens, but uptake has been slow. Most SBT implementations are custom smart contracts, limiting interoperability.

Adoption remains tiny. Most institutions have not issued SBTs; most people have never received one. The ecosystem is experimental. Until major universities, governments, or employers begin issuing SBTs routinely, the network effects are weak and SBT value is speculative.

## See also

<div class="wiki-seealso">

### Closely related

- [Synthetic asset](/synthetic-asset-crypto/) — on-chain token tracking an off-chain asset price
- [Token bonding curve](/token-bonding-curve/) — mathematical pricing formula for deterministic token supply
- [Leveraged token](/leveraged-token/) — ERC-20 maintaining fixed leverage through daily rebalancing
- [Distributed-ledger](/distributed-ledger/) — shared decentralized database underpinning soulbound registries
- Smart contract — self-executing code encoding credential issuance rules
- Wallet — software storing private keys and receiving on-chain tokens

### Wider context

- [Ethereum](/ethereum/) — primary blockchain platform for soulbound token deployment
- Decentralised organisation — governance structure that uses SBTs for membership and voting rights
- Identity — portable, verifiable claim about who you are
- Reputation system — mechanism for building trust based on historical credibility
- Blockchain governance — mechanisms for collective decision-making using on-chain credentials

</div>
