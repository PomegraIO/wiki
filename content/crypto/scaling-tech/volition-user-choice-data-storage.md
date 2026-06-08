---
title: "Volition: User-Chosen Data Storage in ZK Rollups"
description: "Volition lets users decide per transaction whether data is stored on-chain or off-chain, trading cost against settlement certainty in zero-knowledge rollups."
keywords:
  - volition data storage
  - zk rollup scaling
  - on-chain vs off-chain data
  - user choice transaction cost
image: "/svg/crypto.svg"
---

*A **volition** system lets users choose on a per-transaction basis whether that transaction's data is posted to the Ethereum mainchain or stored off-chain, striking a middle ground between cheaper rollups and immediate settlement finality. This hybrid approach gives users direct control over the cost-security tradeoff for each action they take.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volition — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">User-chosen data availability in scaling systems.</div>

|   |   |
|---|---|
| **Core tradeoff** | On-chain posting costs more but settles immediately; off-chain posting is cheaper but relies on sequencer honesty |
| **Data availability** | On-chain data is censorship-resistant and verifiable by any party; off-chain data depends on the operator's availability promise |
| **User agency** | Each transaction allows the sender to select their preferred storage layer |
| **Common in** | Zero-knowledge rollups and some validity-proof systems |
| **Downside** | Adds complexity to the protocol and UX; not all applications benefit equally |

</aside>

## How Volition Data Storage Works

In a standard zero-knowledge rollup, all transaction data is either posted to Ethereum (the expensive, safe path) or kept off-chain by the sequencer (the cheap, risky path). Volition splits the difference by letting users decide **per transaction** which storage layer suits their needs.

When you submit a transaction in a volition system, you specify a flag: "post this to Ethereum" or "keep this off-chain." If you choose on-chain storage, the rollup operator posts your transaction data to mainchain in a blob or calldata, paying Ethereum's gas fees; you bear part of that cost through higher transaction fees, but your data becomes publicly verifiable forever. If you choose off-chain storage, the rollup operator stores your data in their system (or a distributed store), and your transaction settles much more cheaply—but the security of that transaction now depends on the operator's promise to keep the data available and eventually let you exit.

The system is called "volition" because it respects the user's **volition**, or will: each party decides where to place their trust and what they will pay.

## The Cost-Security Tradeoff

The entire premise of volition rests on a fundamental market: users who don't mind taking counterparty risk can save significantly by opting for off-chain data, while users who demand censorship resistance or want to fully exit the rollup without asking the operator for help can pay for on-chain posting.

**On-chain data advantages:**

- Data is recorded on Ethereum for all time; anyone can verify the transaction happened.
- You can exit the rollup unilaterally—prove your balances directly to the Ethereum contract without the sequencer's cooperation.
- High censorship resistance; no single entity can delete or reorder your transaction data.

**Off-chain data advantages:**

- Transaction fees are much lower because the rollup operator doesn't pay to post to Ethereum.
- Faster perceived settlement (though the finality guarantee is weaker).
- Ideal for high-frequency, low-value actions where a few cents in gas savings matter.

**The catch with off-chain data:** If the sequencer or data provider disappears or acts maliciously, you lose the ability to independently prove your state. In the worst case, you must trust the operator's backup systems, or the rollup's failsafe mechanism, to recover your funds. This is why volition works best when users consciously choose which transactions warrant off-chain data—a bet that the operator will stay solvent and honest long enough for those transactions to settle.

## Who Benefits From Volition?

Different users have different risk appetites and use cases.

**DeFi traders and large-value users** typically prefer on-chain data. The cost of posting is small compared to the value at stake, and full verifiability is worth paying for. If they intend to exit the rollup or prove their position without trusting the sequencer, on-chain data is non-negotiable.

**Casual gamers, microtransaction users, and social apps** are the natural audience for off-chain data. A $0.01 game action doesn't justify a $0.50 gas fee; off-chain data lets the rollup operator batch and amortize costs, bringing fees down to cents or less.

**Long-term liquidity providers** might mix both: on-chain for the initial deposit and the final withdrawal (to avoid sequencer dependency), but off-chain for routine rebalancing and interim trades.

Volition puts the decision in the user's hands rather than forcing a one-size-fits-all model.

## Volition vs. Standard Rollups and Validiums

Volition sits at a design crossroads.

A standard ZK rollup posts all data on-chain; cost is high, security is maximum. A validium keeps all data off-chain; cost is low, security depends on the operator and a quorum of data providers. Volition is a hybrid: some transactions on-chain, some off-chain, chosen by the user at transaction time.

The practical advantage is flexibility, but the cost is added protocol complexity. Validators must handle mixed data sources, users must understand the implications of each choice, and the interface (wallet UX) must make the tradeoff clear without overwhelming users.

Some rollups have experimented with volition; others find the added complexity outweighs the benefit and instead optimize for a single dominant use case—all on-chain for heavy DeFi, or all off-chain for light gaming.

## Implementation and Exit Mechanisms

For volition to be secure, the rollup must have robust exit mechanisms for both on-chain and off-chain data.

If you posted your transaction on-chain, exiting the rollup is straightforward: you prove your state using the on-chain data as reference, and Ethereum's contract can validate your claim without needing the sequencer.

If you posted your transaction off-chain, exiting requires the operator to provide your data (or, if they refuse, you must initiate a longer challenge protocol). Some volition systems use a **force-exit** window: if the operator doesn't provide off-chain data within a time limit, the rollup reverts to on-chain posting or lets users escalate to Ethereum's contract directly. Others use a quorum of external data providers who collectively promise to store and serve the data if the sequencer vanishes.

The mechanism must make the off-chain path safe enough that users feel comfortable opting into it, while acknowledging the inherent tradeoff.

## Practical Examples

Imagine a stablecoin protocol on a volition rollup:

- **Large transfers between institutions** (e.g., $1 million) are posted on-chain so both parties have full transparency and can exit independently.
- **Retail payments** ($10–$100 amounts) are posted off-chain so merchants can accept them for under $0.01 in fees.
- **Sweeps from an exchange** back to a user's personal wallet are on-chain so the user retains full custody proof.

Each participant chooses based on their own risk tolerance and the transaction's importance.

## See also

<div class="wiki-seealso">

### Closely related

- ZK Rollup — the base layer technology that volition extends
- Validium — fully off-chain data alternative to volition
- [Forced Transaction Inclusion in Rollups](/forced-transaction-inclusion-rollup/) — another mechanism to protect users from censoring sequencers
- [Account Abstraction on Layer 2](/account-abstraction-layer-two/) — orthogonal scaling technique that pairs well with volition
- [Enshrined Rollups on Ethereum](/enshrined-rollup-ethereum/) — longer-term protocol evolution

### Wider context

- [Layer 2 Scaling](/layer-2-scaling/) — the category that includes rollups and volition systems
- [Ethereum](/ethereum/) — the base layer where data is posted
- [Blockchain Fundamentals](/blockchain-fundamentals/) — foundational concepts

</div>
