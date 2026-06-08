---
title: "How a Blockchain Hard Fork Works"
description: "A blockchain hard fork is a protocol upgrade that breaks backward compatibility, splitting the chain when nodes refuse the new rules."
keywords:
  - blockchain hard fork
  - protocol upgrade fork
  - blockchain split
  - consensus rule change
  - cryptocurrency fork bitcoin ethereum
---

*A **blockchain hard fork** is an update to the protocol's consensus rules that is not backward-compatible — nodes running the old software reject blocks and transactions created under the new rules. When miners and nodes upgrade unevenly, the chain splits: old nodes continue on the original branch, new nodes follow the upgraded chain. Holders of the original asset typically receive an equivalent amount on both forks.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hard Fork — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">A protocol change so fundamental that non-upgrading nodes cannot follow the new chain.</div>

|   |   |
|---|---|
| **Non-backward-compatible** | Old software rejects new blocks outright |
| **Chain splits if participation is partial** | Both chains can coexist if enough nodes support each |
| **Asset duplication** | Holders typically own coins on both resulting chains |
| **Governance issue** | Contentious forks reveal disagreement about chain direction |
| **Requires broad consensus** | Success depends on adoption by miners, exchanges, wallets, and users |
| **Irreversible** | Once a hard fork occurs, the chains cannot merge without full re-sync |

</aside>

## What triggers a hard fork

Hard forks occur when developers want to introduce changes so significant that they alter the fundamental rules of the network. Common reasons include:

- **Security patches**: Fixing a critical vulnerability in the consensus mechanism (e.g., a bug that allows double-spending under certain conditions).
- **Feature additions**: Adding entirely new functionality that existing nodes cannot interpret (e.g., adding a new transaction type or increasing the block size).
- **Policy changes**: Altering economic parameters like block rewards, transaction fees, or supply caps.
- **Correcting past decisions**: Reversing or undoing previous rule decisions (e.g., thawing frozen funds after a contentious hack).

The key distinction is that these changes *violate* the old rules. An old node, running pre-fork software, sees a post-fork block and concludes it is invalid — because it contains transactions or data structures the old rules forbid.

## How the split happens

When a hard fork is activated:

1. **Developers release new software** with the upgraded rules.
2. **Nodes choose whether to upgrade.** Some update immediately; others delay; some never upgrade.
3. **At the fork block (a predetermined height)**, the network behavior diverges.
   - Upgraded nodes follow the new ruleset and build on blocks that satisfy the new rules.
   - Non-upgraded nodes reject any block breaking the old rules, and they continue mining or validating on their own branch.
4. **Two chains now exist**, each with its own transaction history from the fork block onward.
5. **Miners and pools** must choose which chain to secure (or mine both separately). Exchanges and wallets choose which branch they recognize.

The chain that retains the majority of hash power and economic support typically becomes the "true" continuation; the minority branch is often labeled a "fork" or "alt-chain." However, there is no technical rule that forces one chain to "win"—both are valid under their respective rulesets.

## Asset duplication and holder impact

Here is where hard forks directly affect anyone holding the original asset. If you own 10 Bitcoin before a fork, and the fork succeeds in creating two viable chains:

- You own 10 coins on the original chain.
- You own 10 coins on the new chain.
- Each may trade at a different price or eventually become worthless if a chain loses adoption.

This seems like a free gift, but it depends on *when* you held the coins and *where* they were stored:

- **Coins held before the fork**: You receive coins on both chains automatically (because the blockchain ledger before the fork is identical on both branches).
- **Coins held in a non-custodial wallet**: You control private keys, so you can access and spend coins on both chains.
- **Coins held on an exchange**: The exchange decides whether and how to credit you. Some exchanges distribute fork coins generously; others keep them; some credit them months later.
- **Coins acquired after the fork**: You buy coins on whichever chain(s) exist; you don't get duplicates.

The tax and accounting implications can be messy. The IRS has treated hard fork airdrops (where new coins appear in your wallet) as taxable ordinary income at fair market value at the moment of receipt, though treatment varies by jurisdiction.

## Soft forks vs. hard forks

A **soft fork** is a backward-compatible upgrade. New rules are stricter, but old nodes don't reject new blocks outright—they simply don't understand all the new features. Old software can still follow the chain because it only enforces a *subset* of the new rules. No chain split occurs, and no duplicate assets are created.

Example: If the protocol adds a new data field that old nodes ignore, old nodes can still verify that the transaction is valid under the old rules (even if they miss the new field). They will follow the updated chain.

A hard fork is the opposite: the new rules make it *impossible* for old nodes to follow without upgrading. A chain split is inevitable if non-upgraded nodes remain active.

## Contentious hard forks and governance

Some hard forks are uncontentious: nearly everyone agrees on the upgrade, and adoption is rapid and near-universal.

Others are contentious. Disagreement among developers, miners, or the community about the direction of the protocol can result in:

- Two forks, both with significant support, that persist as separate chains (Bitcoin Cash forked from Bitcoin in 2017 over the block size debate).
- Uncertainty about which chain will become the dominant one, causing market volatility and confusion.
- Exchanges and wallets that choose sides unevenly, fragmented user experience.

Contentious forks reveal the decentralized nature of blockchains: there is no central authority to declare which version is "correct." Instead, market forces and network participation determine which chain succeeds.

## Notable examples

**Bitcoin Cash (2017)**: Forked from Bitcoin to increase the block size limit from 1 MB to 8 MB (and later higher), aiming for faster, cheaper transactions. Supporters argued this was necessary for Bitcoin to function as everyday currency; opponents warned it would centralize mining. Bitcoin Cash still exists as a separate asset, trading at a much lower value than Bitcoin.

**Ethereum DAO fork (2016)**: After a hack drained $50 million in funds, Ethereum implemented a hard fork to reverse the transactions and return funds. This was deeply contentious: some saw it as violating the principle of immutability. The minority that opposed the fork continued on "Ethereum Classic," which persists today as a separate chain.

**Bitcoin XT, Unlimited, Classic (2015–2017)**: Multiple proposed hard forks to increase Bitcoin's block size and transaction capacity. All failed to achieve majority adoption; Bitcoin stuck with 1 MB blocks (and later soft-forked in SegWit to increase effective capacity).

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain fundamentals](/blockchain-fundamentals/) — How distributed ledgers maintain consensus without a central authority
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Where fork assets are traded and how exchanges handle splits
- [Distributed ledger](/distributed-ledger/) — The underlying technology that a hard fork splits
- [Proof of work](/proof-of-work/) — The consensus mechanism often at stake in hard fork debates
- [Ethereum](/ethereum/) — A chain that executed a controversial hard fork after the DAO hack

### Wider context

- [Bitcoin](/bitcoin/) — The original blockchain that has resisted hard forks
- Cryptocurrency fundamentals — Broader concepts including forks and network governance
- [Wrapped token: how it works](/wrapped-token-how-it-works/) — Cross-chain asset bridges created in response to chain fragmentation
- [Crypto airdrop tax treatment](/crypto-airdrop-tax-treatment/) — Tax implications of receiving new coins from forks

</div>
