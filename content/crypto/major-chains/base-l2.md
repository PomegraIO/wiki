---
title: "Base"
description: "Coinbase's Ethereum Layer 2, built on the OP Stack, scales transaction throughput while remaining under a single sequencer and eventual Ethereum settlement."
keywords:
  - base l2
  - layer 2
  - optimistic rollup
  - op stack
  - ethereum scaling
image: "/svg/crypto.svg"
---

*Ethereum's 15-second blocks are too slow and expensive for everyday transactions. **Base**—Coinbase's Layer 2 rollup—bundles user transactions off-chain, posts a compressed summary to Ethereum, and lets users trade, swap, and interact with near-instant finality and fractional-cent gas costs. It's built on the **OP Stack**, meaning Coinbase didn't invent the rollup; they deployed and customised an open-source blueprint designed for exactly this purpose.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Base — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain technology." />

<div class="wiki-infobox-caption">Coinbase's Ethereum L2 scales with Ethereum settlement but one-click user experience.</div>

|   |   |
|---|---|
| **Blockchain type** | Layer 2 optimistic rollup |
| **Settlement chain** | Ethereum |
| **Consensus mechanism** | Single sequencer (Coinbase-operated); fraud proofs |
| **Native asset** | Ether (same as Ethereum) |
| **Stack** | OP Stack (derived from Optimism) |
| **Launch** | Mainnet August 2023 |
| **Architecture** | Rollup with Ethereum as settlement |
| **Block time** | ~2 seconds |

</aside>

## Why Ethereum needs Layer 2

Bitcoin processes ~7 transactions per second. Ethereum does ~15. Credit cards handle thousands. When demand spikes—say, after an airdrop or a popular NFT launch—Ethereum clogs. Fees spike to dollars per transaction. Wallets sit empty because moving tokens costs more than the tokens are worth.

This is a design constraint, not a bug. Ethereum prioritises security and decentralisation over throughput. Every node must validate every transaction, which means every node processes every block. Add more throughput, and you exclude nodes from running locally, pushing the network toward centralisation.

Layer 2s solve this by moving transactions off-chain. Users submit transactions to a **sequencer** (a centralised server) instead of the main chain. The sequencer batches these transactions, posts a compressed summary to Ethereum (a "rollup"), and users get near-instant confirmation. Ethereum acts as a security anchor, not a bottleneck.

The tradeoff: you're trusting the sequencer not to steal your funds (though rollup cryptography ensures it can't reorder or censor transactions). You're also introducing latency before the transaction is *settled* to Ethereum—if the sequencer goes down, you might have to wait to recover your funds.

Most users find this tradeoff acceptable. Olympus DAO researchers found that 99% of transactions on rollups are for non-financial purposes (social, gaming, tooling), where a few hours of sequencer downtime is tolerable.

## The OP Stack and Optimism

Base isn't a unique invention. It's an instance of the **OP Stack**, an open-source toolkit for launching optimistic rollups. Optimism (the company) built OP Stack and deployed it for their own rollup. Coinbase, Uniswap Labs, and others have deployed their own instances.

An **optimistic rollup** works like this: the sequencer batches thousands of transactions, hashes them, and posts the hash to Ethereum. Ethereum doesn't execute these transactions—it takes the sequencer's word (optimistically assumes they're valid). If someone finds a bad transaction, they can post a **fraud proof** to Ethereum, which then re-executes that transaction and slashes the sequencer.

This design is elegant. Posting to Ethereum is cheap (Base's sequencer pays a few cents per batch, amortised across thousands of users). Fraud proofs ensure honesty without Ethereum needing to re-execute the world.

The OP Stack abstracts the complexity. Coinbase didn't write the consensus logic, state machine, or EVM emulator. They deployed a stack, configured it, and added Coinbase-specific features (like optimised onboarding for Coinbase users).

## Why Coinbase runs it

Coinbase's angle is clear: remove friction from crypto adoption. A user on Coinbase can now bridge assets to Base with one click, trade on Base at 1/100th Ethereum's gas cost, and bridge back to Coinbase to cash out—all from a trusted brand they already have an account with.

This is different from Arbitrum or Optimism, which are community-governed rollups aimed at decentralisation. Base, by contrast, is Coinbase's product. Coinbase runs the sequencer. Coinbase benefits from transaction volume (and can subsidise fees to attract users). Coinbase controls the narrative.

This centralisation is a feature, not a bug, for Coinbase's users. They get the rollup's speed and one-click experience with a company they know will be around in five years (unlike a venture-funded rollup that might get acquired or pivot). Coinbase's brand is the guarantee.

But it means Base lacks the decentralisation credibility of Ethereum or even Arbitrum. If Coinbase decides to censor transactions, or decides to shut down the sequencer, users have limited recourse. The OP Stack's fraud-proof mechanism theoretically ensures Coinbase can't steal funds, but pragmatically, they control user experience.

## Ecosystem and adoption

Base has grown rapidly. As of mid-2024, it ranks in the top five rollups by TVL and daily transactions. The DeFi ecosystem (Uniswap, Aave, Curve) has all deployed to Base. Layer 1 alternatives like Solana are direct competitors, but Base has advantages: Ethereum security, access to Coinbase's distribution, and the halo effect of being "Ethereum with speed."

Gaming has been a significant vertical. On-chain games that need cheap and fast transactions have adopted Base. The onboarding for Coinbase users is seamless (many Base users never knew they were using a rollup—they just saw "fast transactions").

But Base hasn't captured the mindshare or culture of L1 chains like Bitcoin, Ethereum, or even Solana. Rollups are often perceived as "Ethereum's training wheels"—you use them because Ethereum is congested, but you'd rather be on L1.

This perception may be unfair. Base's sequencer is fast enough and reliable enough for most real-world use cases. Ethereum settlement provides security most L1s aspire to. But competing on Ethereum's network effects while being subordinate to Ethereum is a perpetual disadvantage.

## Sequencer risk and decentralisation roadmap

Base's biggest weakness is sequencer centralisation. If Coinbase's sequencer goes down, the Base chain halts. Users can still withdraw to Ethereum (the security net), but they can't transact on Base until Coinbase brings the sequencer back online.

This is not theoretical. During the 2023 Ethereum Shanghai upgrade, Base briefly went offline due to sequencer issues. Users were fine (no loss of funds), but trust took a hit.

Coinbase has announced plans to decentralise the sequencer—eventually allowing multiple parties to propose blocks. This is technically complex and introduces new attack surfaces. Optimism and Arbitrum have experimented with decentralised sequencers (Arbitrum One uses a decentralised sequencer from its sequencer committee). But Base remains centrally operated.

The roadmap promises decentralisation. But promises ring hollow until it's done. For now, depositing significant funds on Base means trusting Coinbase's infrastructure and governance more than you'd trust Ethereum's.

## Settlement and finality

Base transactions are fast (confirmation in ~2 seconds) but not final until they're settled to Ethereum. Ethereum produces blocks roughly every 12 seconds. Base batches post to Ethereum perhaps once per minute (or more frequently if gas is cheap).

This introduces two kinds of time:
- **Base finality**: your transaction is confirmed and irreversible within Base (if the sequencer says so).
- **Ethereum finality**: your transaction is settled to Ethereum and irreversible by any actor (including Coinbase).

For most transactions, Base finality is enough. You can trade, transfer, or interact with confidence. But for high-value transfers or if you're concerned about Coinbase governance, Ethereum settlement matters.

The OP Stack's fraud-proof system (once enabled, which it isn't yet on Base) will theoretically guarantee that only valid transactions settle to Ethereum. Until then, users are trusting Coinbase's honesty. This is not a radical departure from most crypto users' assumptions, but it's worth noting.

## See also

<div class="wiki-seealso">

### Closely related

- [Arbitrum](/arbitrum/) — competing optimistic rollup with earlier launch and decentralised governance
- [Optimism](/optimism/) — the foundation and creator of OP Stack
- [Optimistic rollup](/optimistic-rollup/) — Base's mechanism for scaling
- [Ethereum](/ethereum/) — Base's settlement chain and security anchor
- Layer 2 — what Base is; category of scaling solutions

### Wider context

- Scalability trilemma — the fundamental tension Layer 2s address
- Sequencer — the centralised actor Base relies on
- Fraud proof — the mechanism ensuring sequencer honesty
- Finality — how transactions become irreversible
- Bridge — how assets move between Ethereum and Base

</div>