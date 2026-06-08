---
title: "Block Proposal Slot Auction Mechanics"
description: "Block proposal slot auctions let builders bid for the right to fill a proposed block, and proposers earn the highest bid. This mechanism concentrates MEV and separates block building from validation."
keywords:
  - block proposal slot auction mechanics
  - proposer builder separation
  - mev in blockchain auctions
  - ethereum block building
  - validator rewards block auctions
  - mev extraction flow
image: /svg/crypto.svg
---

*A **block proposal slot auction** is a mechanism where block builders compete by bidding for the right to construct (fill) a block that a validator-proposer has been chosen to propose. The proposer accepts the highest bid, collects the proceeds as additional income beyond base rewards, and the winning builder gets to include transactions and capture any remaining MEV. This design emerged to manage maximal extractable value in proof-of-stake systems.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Block Proposal Slot Auction — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for crypto and blockchain." />

<div class="wiki-infobox-caption">Builders bid for slots; proposers collect bid revenue; MEV is separated from validation.</div>

|   |   |
|---|---|
| **Who participates** | Block builders, block proposers (validators), relay operators |
| **What's being auctioned** | Right to fill one block in the blockchain |
| **Duration of auction** | Typically 4–12 seconds (varies by network) |
| **Winning criterion** | Highest bid in ETH (or equivalent native asset) |
| **Proposer role** | Receives bid value; attests to block header (does not build the block) |
| **Builder role** | Constructs the actual block with transactions and collects MEV beyond the bid |
| **MEV distribution** | Bid to proposer; remaining MEV to builder |
| **Relay role** | Intermediary that broadcasts bids and ensures honesty |
| **Key benefit** | Proposers earn extra revenue; builders professionalize block construction |

</aside>

## The Problem: MEV and Block Construction

In early proof-of-stake designs, a single validator would propose and build its own block. This validator could observe the transaction mempool, reorder transactions, insert private transactions, and capture all MEV (maximal extractable value)—the profit available from exploiting transaction order or information asymmetry.

This created several problems:

1. **Centralization pressure**: Only sophisticated validators with advanced infrastructure could profitably extract MEV. Small validators lagged; over time, MEV-aware validators grew larger and more dominant.

2. **Transaction ordering risk**: Users could be sandwich-attacked: a validator would insert a front-running transaction before a user's swap, execute the swap, and then execute a back-running transaction to pocket the profit.

3. **Fairness**: Users had no guarantee of fair treatment. Validators could explicitly favor certain transactions based on a bribe.

To mitigate these issues, the Ethereum community (and others) adopted a two-layer design: separate the roles of block proposal (validation) and block building.

## The Two-Layer Model: Proposers and Builders

In the current design:

1. **Validators are chosen to propose blocks** (just as before). However, proposers no longer build their own blocks.

2. **Specialized builders compete to construct blocks**. Builders collect transactions from the mempool, order them, and construct a complete block. They then bid for the right to have their block proposed.

3. **A relay intermediates the process**. The relay collects bids from multiple builders, ensures the highest bid wins, and communicates the winning block to the proposer.

4. **The proposer receives the bid value** (paid in ETH) as a reward for agreeing to attest to and finalize the builder's block.

## How a Slot Auction Unfolds

**Step 1: Block slot opens.** A validator is chosen to propose the next block in the consensus layer. It signals its intention to the network and relays.

**Step 2: Builders assemble blocks.** Multiple builders race to construct the best block for that slot. They source transactions from the public mempool, private transaction pools (flashbots bundles), and private order flow. They simulate each transaction, estimate gas fees, and calculate the MEV available.

A builder might construct a block containing:

- Ordinary transactions from the public mempool (fee revenue to the builder)
- A sandwich attack on a large swap (MEV profit to the builder)
- Private transactions that pay for priority (MEV profit to the builder)
- Arbitrage or liquidation opportunities the builder sources itself (MEV profit)

Let's say the builder estimates the block will generate 2 ETH in total value: 0.5 ETH in ordinary transaction fees, and 1.5 ETH in MEV profit (sandwich attacks, arbitrage, liquidations). The builder computes that it can bid up to 1.4 ETH and still make a 0.1 ETH profit.

**Step 3: Builders submit sealed bids.** Builders submit their bids and block headers to the relay (or multiple relays). The bid is sealed: the relay sees the amount but cannot yet see the full block contents (to prevent frontrunning by the relay itself).

**Step 4: Relay selects the highest bidder.** The relay collects bids from all builders and identifies the highest bid. The relay does not execute or validate the block at this point; it simply records which builder bid the most.

**Step 5: Proposer receives the winning bid and block.** The relay communicates the winning block header and the bid amount to the proposer. The proposer learns that the builder is offering, say, 1.4 ETH to have its block proposed.

**Step 6: Proposer accepts and signs.** The proposer verifies the block header (syntax, basic validity), checks that the bid amount is accurate, and signs the block header. This signature commits the validator to proposing this block to the network. The proposer now has a claim on 1.4 ETH.

**Step 7: Builder receives the signed header.** The builder receives the signed block header from the relay. This signature proves the proposer has committed. The builder now broadcasts the full block (header + all transactions) to the network.

**Step 8: Network validates and includes the block.** Nodes receive the block, validate all transactions, verify the proposer's signature, and include the block in the chain. The proposer's reward (1.4 ETH) is now locked in the block as execution layer profit (paid out of MEV or base fees).

**Step 9: Builder profits.** The builder has paid 1.4 ETH to the proposer but has constructed a block worth 2 ETH in total value. The builder nets 0.6 ETH (the 2 ETH value minus the 1.4 ETH bid).

## MEV Distribution Under Slot Auctions

The slot auction splits MEV into two parts:

| Party | Receives |
|-------|----------|
| **Proposer** | The winning bid (e.g., 1.4 ETH) |
| **Builder** | Remaining MEV (e.g., 2 ETH value minus 1.4 ETH bid = 0.6 ETH) + ordinary transaction fees |

Note that the proposer does not see the full block until after signing. In principle, the builder could construct a block with less value than the bid claims and submit it anyway. To prevent this, the relay can implement slashing: if the block is invalid or worth much less than the bid, the builder forfeits collateral or is banned from future auctions.

This arrangement aligns incentives:

- **Builders benefit from finding and executing the most valuable MEV opportunities**, because they keep everything above the bid.
- **Proposers benefit from competition among builders**, because more builders = higher bids.
- **Users benefit modestly** because the separation of roles reduces validator incentive to sandwich attacks (though builders still do).

## Relay Operators and Trust

The relay is a new, centralized component. It must:

1. Collect bids honestly and identify the true highest bid.
2. Withhold the full block from the winning builder until the proposer has signed the header.
3. Enforce slashing rules if a builder submits a block worth much less than the bid.

If a relay is dishonest, it could:

- Lie about the highest bid (favoring a particular builder).
- Censor a builder's bid (preventing a high bid from being seen).
- Share block contents with other builders before the proposer signs (allowing a rival builder to frontrun).

To reduce relay risk, the Ethereum community encourages multiple relays and has developed relay monitoring and slashing mechanisms. However, as of 2025, the relay market remains somewhat concentrated, with a few relays handling the majority of bids.

## Impact on Centralisation and MEV

The slot auction mechanism has:

- **Professionalized block building**: Large, technically sophisticated builders now dominate block construction. This has actually increased centralisation at the builder layer, though it has reduced the concentration of MEV wealth flowing directly to individual validators.

- **Distributed proposer income**: Smaller validators now earn extra income (the bid value) even if they cannot extract MEV themselves. This has helped smaller validators remain competitive.

- **Reduced MEV visibility for users**: Because MEV is now bundled and auctioned, users have less clarity on exactly how much MEV is being extracted from their transactions. This is a privacy gain for builders but a transparency loss for users.

- **Maintained large MEV flows**: The total MEV extracted has not decreased; it has simply been redirected to builders and proposers rather than concentrated in the hands of a few large validators.

## Relation to Other MEV Mechanisms

Slot auctions coexist with other MEV strategies:

- **In-protocol MEV** (e.g., liquidations, arbitrage by the protocol itself): Builders still extract this and bid accordingly.

- **Private transaction pools and bundles** (e.g., Flashbots Bundles): Builders still source private order flow and include bundles in bids.

- **Encrypted mempools and threshold encryption** (future): If adopted, these could reduce observable MEV and change bidding dynamics.

The slot auction is not the final word on MEV. It is a pragmatic interim design that has made MEV more structured and reduced extreme centralization while preserving builder income.

## See also

<div class="wiki-seealso">

### Closely related

- MEV Extraction — maximal extractable value and frontrunning in blockchains
- [Proof of Stake](/proof-of-stake/) — consensus mechanism underlying slot auctions
- [Smart Contract](/smart-contract/) — transactions that builders include in blocks
- [Ethereum](/ethereum/) — network that pioneered the proposer-builder separation design
- Block Reward — how validators and builders are compensated

### Wider context

- Consensus Mechanism — broader category of blockchain decision-making
- [Validator](/validator/) — role in proof-of-stake networks
- Transaction Pool — mempool from which builders source transactions
- [Distributed Ledger](/distributed-ledger/) — blockchain fundamentals
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where MEV often originates (sandwich attacks on swaps)

</div>
