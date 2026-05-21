---
title: "Sybil Attack"
description: "An attack in which a single entity creates multiple identities to gain disproportionate voting power or economic benefit."
---

*A Sybil attack is a form of manipulation where an attacker operates many accounts or nodes—called "Sybil identities"—to appear as many distinct participants rather than one. In a voting system, a Sybil attacker might create 1,000 wallet addresses and use them to cast 1,000 votes, gaining 1,000 times the voting power of a single honest participant. In a blockchain network, an attacker might run 1,000 nodes to surround an honest node with adversarial peers. Sybil attacks are cheap in systems where creating identities is low-cost.*

## The identity creation problem

The fundamental challenge in decentralized systems is that anyone can create as many identities as they want. In a traditional company, voting shares are tracked by a central ledger, so creating fake votes is impossible. In a decentralized governance system, voting power is distributed to token holders, so if you own 1% of tokens, you have 1% of voting power—true whether you control one wallet or 100 wallets.

If governance is tied to "one person, one vote" (rather than "one token, one vote"), the system becomes vulnerable to Sybil attacks. How does the system verify that you are a unique person and not 100 different people? There is no way to do this without trusted intermediaries (KYC, identity documents), which contradicts the decentralization goal.

## Sybil attacks in mining and staking

In proof-of-work (mining), Sybil attacks are partially mitigated by the cost of hardware and electricity. To control 51% of Bitcoin mining, you must own 51% of the world's mining equipment. The hardware cost is enormous, which discourages Sybil attacks even though technically anyone can run a mining node.

In proof-of-stake, Sybil resistance is weaker. Validators are selected based on stake, not computational work. To control 51% of stake, you need to own 51% of the staked tokens. If you already own 51% of tokens, you do not need Sybil attacks; you already control the system. However, if you own less stake, you can try to fragment it across many validator identities to appear as many independent validators. Modern proof-of-stake systems try to make this costly by requiring a minimum stake per validator (e.g., 32 Ethereum to run an Ethereum validator), but determined attackers with sufficient capital can still mount attacks.

## Sybil attacks in airdrops and incentives

When a protocol distributes tokens via [token-airdrop](/wiki/token-airdrop/) (e.g., "every account with $1,000 in our protocol receives 10 tokens"), Sybil attackers split their capital across many accounts to maximize their allocation. If the airdrop gives 10 tokens per account regardless of size, splitting $100,000 across 100 accounts yields 1,000 tokens instead of 10.

This incentivizes protocols to use objective metrics (total value locked, transaction history) rather than per-account metrics. But Sybil attackers can also game objective metrics by spreading capital strategically.

## Sybil attacks in reputation systems

In peer-to-peer networks without central authority (like the early bitcoin p2p network or privacy-focused social networks), Sybil attacks are a fundamental vulnerability. If reputation is tracked at the node level, an attacker can:

1. Create 1,000 fake nodes.
2. Have all 1,000 connect to an honest node.
3. Surround the honest node, controlling its view of the network.
4. Feed it false information.

This is called a "Sybil attack" in network topology and is distinct from (but related to) voting attacks.

## Defenses against Sybil attacks

**Token-based voting.** If voting power is proportional to token holdings rather than account count, Sybil attacks are harder. You can create many accounts, but each account must hold tokens to vote. A determined attacker with capital can still attack, but the cost scales with voting power.

**Proof of personhood.** Some protocols have experimented with "proof of personhood" systems—using biometrics, government IDs, or social verification to ensure each person has only one identity. Worldcoin and Proof of Humanity are examples. But these systems reintroduce centralization and privacy concerns. Governments can demand access to the database; private companies can censor or manipulate membership.

**Reputation and history.** A system can weight voting power based on account age (older accounts get more power) or interaction history (accounts that have participated in the ecosystem get more power). This does not prevent Sybil attacks but raises the cost—the attacker must maintain many accounts over months or years, rather than creating them instantly.

**Decentralized identity.** Protocols like ENS (Ethereum Name Service) and Decentralized Identifiers (DIDs) allow users to build a portable identity across applications. If a reputation system can verify that an ENS name or DID is unique, Sybil attacks become harder. But again, this requires some form of identity verification, which contradicts anonymity.

**Economic commitment.** Some systems require Sybil participants to stake or lock capital. If creating an identity costs money, Sybil attacks become expensive. However, capital-rich attackers can still mount attacks if the reward is large enough.

## The unsolved problem

Despite research into Sybil resistance, there is no perfect solution. Every defense involves trade-offs:

- Token voting avoids Sybil resistance if the attacker is already capital-rich.
- Proof of personhood sacrifices anonymity and introduces centralized gatekeepers.
- Reputation systems are slow to deploy and can be gamed.
- Economic commitment is expensive for the attacker but also expensive for honest participants.

The most robust systems use multiple defense layers: token voting (making attacks capital-intensive), reputation (raising the cost by requiring history), and occasional human review (for high-stakes decisions). But no layer is perfect, and the Sybil problem remains a core unsolved challenge in decentralized systems.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/governance-token/">Governance Token</a> — voting systems vulnerable to Sybil attacks.</li>
<li><a href="/wiki/proof-of-stake/">Proof of Stake</a> — consensus systems partially vulnerable to Sybil attacks.</li>
<li><a href="/wiki/delegated-proof-of-stake/">Delegated Proof of Stake</a> — attempts to mitigate Sybil attacks through delegation.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/distributed-ledger/">Distributed Ledger</a> — the underlying technology vulnerable to Sybil attacks.</li>
<li><a href="/wiki/ethereum/">Ethereum</a> — networks where Sybil attacks are a practical concern.</li>
<li><a href="/wiki/token-airdrop/">Token Airdrop</a> — distributions vulnerable to Sybil gaming.</li>
</ul>
</div>
