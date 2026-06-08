---
title: "Celo"
description: "A blockchain that enables financial inclusion through phone-number-based addresses and mobile-first payments with stablecoin reserves."
keywords:
  - celo blockchain
  - mobile payments
  - phone number address
  - financial inclusion
  - stablecoin reserve
image: "/svg/crypto.svg"
---

*[Celo](/celo/) is a [blockchain](/distributed-ledger/) designed for financial inclusion, particularly in emerging markets and on mobile devices, by allowing users to send and receive value using a phone number rather than a hex address and maintaining an on-chain reserve to stabilise its native stablecoin. Unlike chains that treat accessibility as an afterthought, Celo embeds phone-number discovery and low fees into its core architecture.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Celo — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain topics." />

<div class="wiki-infobox-caption">A mobile-first blockchain focused on financial inclusion and peer-to-peer payments.</div>

|   |   |
|---|---|
| **What it is** | A [blockchain](/distributed-ledger/) designed for mobile payment with phone-number-based accounts and stablecoin backing |
| **Consensus model** | [Proof of Stake](/proof-of-stake/) with BFT |
| **Address system** | Phone numbers are linked to on-chain public keys via a decentralised identity oracle |
| **Native stablecoin** | Celo Dollars (cUSD) backed by a reserve of collateral and assets |
| **Governance token** | CELO |
| **Primary use case** | Remittances, peer-to-peer payments, financial services for unbanked users |

</aside>

## The last-mile problem in financial inclusion

Billions of people globally lack access to bank accounts, but many have mobile phones. Cryptocurrencies promise financial sovereignty without intermediaries, but they have historically required users to manage unfamiliar address strings (e.g. `0x742d35Cc6634C0532925a3b844Bc9e7595f42bE9`)—a friction point that excludes non-technical users. Asking someone in a developing country to remember or type a hex address is asking them to adopt a new literacy.

Celo's insight was to anchor on the phone number, which users already know. Instead of sending cryptocurrency to an address, you send it to a contact's phone number. Behind the scenes, that phone number is linked to a public key stored on the Celo blockchain, but the user never sees the machinery.

This simple inversion—phone-number-first rather than address-first—removes a psychological and practical barrier to entry. A remittance sender in a city knows their relative's phone number; they do not need to ask for a wallet address or learn what a private key is.

## The phone number oracle

Celo achieves phone-number-based addressing through an on-chain decentralised identity oracle called the Phone Number Hash Mapping. When a user wants to claim a phone number on Celo, they submit a hashed version of their number to the network (hashing protects privacy; the network does not store phone numbers in plaintext). Other nodes can then independently verify the hash. Once enough attestators have confirmed the hash, the mapping is published on-chain, linking the hash to the user's public key.

This design does not require a centralised identity provider (though Celo also supports traditional KYC when needed). The oracle is maintained by validators and community participants who run attestation services. If an attacker tries to claim someone else's phone number, other attestators will reject it.

The phone number oracle is not bulletproof. A determined attacker with access to a user's phone (via a SIM-swap or compromise) could claim ownership of that number. But for mainstream adoption, the security is sufficient, and the usability gain is massive. The trade-off is intentional.

## The on-chain reserve and stablecoin design

Celo issues [cUSD](/celo/), a stablecoin designed to hold its value relative to the US dollar, enabling users to save and spend without exposure to [cryptocurrency](/cryptocurrency-exchange/) volatility. Unlike [Bitcoin](/bitcoin/) or [Ethereum](/ethereum/), which expect users to tolerate price swings, cUSD is built for stability—critical for people with limited savings who cannot afford sudden depreciation.

cUSD is backed by collateral held in an on-chain reserve. The reserve accepts deposits of CELO tokens (Celo's governance and native asset) and other assets like Ethereum or [Bitcoin](/bitcoin/), which are converted into highly liquid positions. This collateral backs every cUSD in circulation. If the reserve becomes undercollateralised, market mechanisms (including penalties to reserve managers and incentives for arbitrage) adjust the system back to balance.

The reserve is managed on-chain, visible to anyone. This transparency is a feature: users can audit whether their stablecoin is actually backed. Contrast this with traditional stablecoins, where reserve claims are largely opaque and depend on periodic audits.

## Governance and the path to layer 2

Celo uses [Proof of Stake](/proof-of-stake/) for consensus, with CELO token holders proposing and voting on protocol changes. Early on, Celo maintained its own blockchain; since 2024, it has transitioned toward operating as an Ethereum layer 2 rollup using a zk-SNARK proof system, while preserving the phone-number registry and stablecoin design. This shift reduces the burden of maintaining a separate validator set while inheriting Ethereum's security.

## Adoption and challenges

Celo has gained traction in emerging markets, particularly in Latin America and Africa, where remittance costs are high and phone penetration is near-universal. It powers stablecoins issued by banks and fintech companies targeting underserved regions.

The main challenge is liquidity. A stablecoin is only useful if it can be easily converted to fiat currency (dollars, euros, local currency) without slippage. Celo's liquidity is improving but still lags USD Coin (USDC) or Tether (USDT), which benefit from deeper integrations with centralised exchanges. For a person in a village sending $50 to a relative, converting cUSD back to cash at a fair rate still requires intermediaries.

Additionally, while the phone-number model is intuitive, it is not magic. Phone numbers can be transferred, stolen via SIM-swap, or recycled after an account is closed. Celo's security depends on the diligence of attestators and users, not mathematical proof.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Stake](/proof-of-stake/) — Celo's consensus mechanism
- [Blockchain Fundamentals](/blockchain-fundamentals/) — distributed ledger concepts
- [Distributed Ledger](/distributed-ledger/) — technology category
- [Ethereum](/ethereum/) — Celo now settles as an Ethereum rollup
- [Bitcoin](/bitcoin/) — alternative blockchain, different use case

### Wider context

- [Flow](/flow-blockchain/) — another L1 focused on accessibility
- [Internet Computer](/internet-computer/) — alternative L1 with different architecture
- [Scroll](/scroll/) — Ethereum scaling solution
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where CELO trades
- Financial Inclusion — broader policy context for Celo's mission

</div>
