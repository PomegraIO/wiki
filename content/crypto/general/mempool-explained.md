---
title: "Mempool Explained"
description: "The waiting room for unconfirmed blockchain transactions, where miners and validators select transactions by fee priority."
keywords:
  - what is a mempool in crypto
  - mempool transaction selection
  - bitcoin mempool fees
  - blockchain pending transactions
  - miner transaction priority
---

*Every blockchain maintains a waiting room for transactions that have been broadcast but not yet included in a block. The **mempool** (memory pool) is where unconfirmed transactions queue up, ranked by the fees they offer. Miners and validators scan it, select high-fee transactions, and pack them into blocks. Understanding mempool dynamics explains why your transaction costs vary wildly and how to predict confirmation times.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Mempool — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">A transaction's fate hinges on its position in the queue and the fees it offers.</div>

|   |   |
|---|---|
| **Purpose** | Holds unconfirmed transactions awaiting block inclusion |
| **Size limit** | Network-dependent; Bitcoin ~300 MB default |
| **Transaction ranking** | By [fee per byte](/pip/) (sat/byte for Bitcoin, wei/gas for Ethereum) |
| **Eviction policy** | Lowest-fee transactions dropped if mempool fills |
| **Fee spike trigger** | Network congestion; rapid increase when demand spikes |
| **Mempool monitoring** | Public; explorers and APIs track real-time state |

</aside>

## What Happens After You Broadcast

When you send a cryptocurrency transaction, you broadcast it to the network's nodes. The transaction includes your signature, inputs (coins you are spending), outputs (where they go), and a fee. But it does not go straight into a block. Instead, every full node that receives it stores it in memory, in a data structure called the mempool.

The mempool is temporary storage. Transactions live there until they are either:
1. **Included** in a block and confirmed (then removed from mempool and written to the blockchain)
2. **Evicted** due to mempool capacity limits or [timeout](/interest-rate-risk/) (default 72 hours without confirmation on Bitcoin)
3. **Double-spent** (you broadcast a conflicting transaction that confirms instead)

Nodes check each incoming transaction for validity: valid signature, no double-spend, sufficient fee (or free-to-the-node if relayed from a peer). Invalid transactions are rejected immediately and never enter the mempool.

## Mempool Size and Capacity

Full nodes maintain a **mempool** in RAM. The default maximum size is network-dependent. Bitcoin's default is ~300 MB; Ethereum's is larger and varies. Once a mempool fills, the node begins evicting the lowest-fee transactions to make room for incoming high-fee ones.

This creates a fee market. During quiet times, you can broadcast a 1 sat/byte (satoshi per byte) transaction and it will sit in the mempool indefinitely—but most nodes will evict it within 72 hours if it is not confirmed. During congestion (like a major price move or exchange outage), the mempool fills, and transactions under 50 sat/byte are evicted. Your low-fee transaction never gets a chance; you must rebroadcast it with a higher fee.

## Fee-Based Ranking and Selection

Miners and validators choose which transactions to include in blocks by scanning the mempool. Their goal: maximize fee revenue. So they prioritize transactions by fee per unit size.

For Bitcoin, the unit is bytes. A simple transaction is ~250 bytes. If two transactions in the mempool are:
- Transaction A: 2,500 satoshis, 250 bytes = 10 sat/byte
- Transaction B: 1,000 satoshis, 200 bytes = 5 sat/byte

A rational miner includes Transaction A first because it offers higher fee density.

For Ethereum, the unit is gas. A simple transfer costs 21,000 gas. If the mempool shows:
- Transaction A: 50 gwei gas price, 21,000 gas = 1.05 ETH fee
- Transaction B: 30 gwei gas price, 21,000 gas = 0.63 ETH fee

Miners include A first. Both transactions are identical in complexity, so the fee per gas (gwei) is the only differentiator.

## Mempool Congestion and Dynamic Fees

Most wallet software displays a "slow/standard/fast" fee option. These are snapshots of the mempool's current state:

- **Slow**: You offer the median fee in the mempool; your transaction is middle-of-the-queue.
- **Standard**: Slightly above median; likely to confirm in the next 1–2 blocks.
- **Fast**: Top 10% of fees; confirm in the next block, or within 1–2 blocks.

When network demand spikes—a popular NFT drop, a major price move, exchange outage—everyone rushes to transact simultaneously. The mempool fills. Wallet software recalculates and shows "standard" fees suddenly at 100 sat/byte (instead of 10). Users complain; in reality, the mempool has shifted and miners are now selecting only the highest-fee transactions.

Once congestion eases, fees collapse. The same wallet shows "standard" at 5 sat/byte again. This happens within minutes on Ethereum (due to block time of ~12 seconds) and can take hours on Bitcoin (~10 minutes between blocks).

## Child Pays for Parent (CPFP)

If you broadcast a transaction with too low a fee and it stalls in the mempool, you can accelerate it by broadcasting a **child** transaction that spends the unconfirmed output of the stuck transaction. The child transaction includes a high fee.

Miners now see both transactions together and calculate total fee / total bytes. If the total fee is attractive, they include both. The child "pays for the parent"—the low-fee parent gets confirmed because the high-fee child makes the package worthwhile.

Bitcoin supports CPFP. Ethereum does not (its [mempool](/mempool-explained/) mechanics are different; you would [resubmit](/blockchain-finality/) with a higher fee instead).

## Replace-By-Fee (RBF)

Bitcoin transactions can signal **replace-by-fee**. If your low-fee transaction is stuck, you broadcast a conflicting transaction that spends the same input but includes a higher fee. Nodes replace the old transaction with the new one in their mempool.

The new transaction must pay more than the old one *plus* the fee you are asking miners to accept for adding the replacement. This prevents spam.

Ethereum does not have formal RBF, but you can achieve similar results by resubmitting the transaction with a higher gas price and nonce. The newer transaction replaces the old one in node mempools.

## Public Mempool Data and Fee Estimation

Mempool state is public. Blockchain explorers (like Mempool.space for Bitcoin or Etherscan for Ethereum) display real-time mempool size, fee distribution, and pending transactions. You can watch your transaction's status and see how long it is likely to take.

Fee estimation services (Mempool.space, EIP-1559 transaction simulators) analyze the mempool and predict what fee you need to confirm in the next N blocks. These estimates are probabilistic—they work well on average but fail in extreme volatility.

## Priority Fees and EIP-1559

Ethereum's EIP-1559 (September 2021) introduced a different mempool model. Transactions include:
- **Base fee**: Set by protocol based on network congestion; auto-adjusted.
- **Priority fee** (tip): You offer miners extra to prioritize your transaction.

The base fee is burned; the priority fee goes to miners. This decouples the total price from the miner incentive, making fee estimation clearer. A wallet can set base fee = mempool-derived, priority fee = user preference (slow/standard/fast = 1 gwei / 2 gwei / 5 gwei, say).

Bitcoin does not have base fees but operates on the same principle: miners scan the mempool, sort by fee per byte, and pack blocks.

## Mempool Attacks and Edge Cases

Attackers sometimes exploit mempool mechanics:

- **Dust attacks**: Broadcast many low-value, low-fee transactions to clog the mempool and crowd out normal transactions.
- **Transaction pinning**: Broadcast a transaction, then its child with a very high fee, preventing the parent from being evicted. Used in certain cross-chain scenarios.
- **Sybil attacks**: Run many nodes to broadcast conflicting transactions and confuse the network about which is canonical.

Mempool policies (minimum fee requirements, maximum tx size, rate limiting) protect against these. Individual nodes can set stricter policies, but they cannot enforce rules stricter than the consensus protocol allows.

## See also

<div class="wiki-seealso">

### Closely related

- [Bitcoin](/bitcoin/) — how mempool selection works in the original proof-of-work blockchain
- [Blockchain Finality Explained](/blockchain-finality-explained/) — what happens after a transaction leaves the mempool
- [Ethereum](/ethereum/) — EIP-1559 and how Ethereum's mempool fee model evolved
- [Proof-of-Work](/proof-of-work/) — why miners care about fee revenue
- [Pip](/pip/) — foreign exchange terminology; analogous fee-per-unit ranking in crypto

### Wider context

- [Market Maker (Trading)](/market-maker-trading/) — how bots exploit mempool data for MEV
- [Operational Risk](/operational-risk/) — mempool congestion as a systematic failure mode
- [Fee-Based Pricing](/cost-basis/) — how transaction fees fit into overall cryptocurrency economics

</div>