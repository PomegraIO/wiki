---
title: "Volition Hybrid Rollup"
description: "A rollup where users choose per-transaction whether data is stored on-chain or posted to a cheaper external data availability layer."
keywords:
  - volition
  - hybrid rollup
  - data availability choice
  - rollup scaling
  - user preference
  - transaction cost
image: "/svg/crypto.svg"
---

*A **volition hybrid rollup** is a scaling solution that lets users decide, for each transaction, whether to store transaction data on the settlement layer (expensive, maximally secure) or on a cheaper external [data availability layer](/data-availability-layer/) (faster, lower cost, trusts an external validator set). The same rollup handles both paths seamlessly.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volition Hybrid Rollup — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain architecture." />

<div class="wiki-infobox-caption">Users trade settlement security for transaction cost, per transaction.</div>

|   |   |
|---|---|
| **What it is** | A rollup offering per-transaction choice between on-chain and external data storage |
| **User lever** | Each transaction specifies its preferred data availability guarantee |
| **On-chain path cost** | Higher fees but proof of data stored in Ethereum (or settlement layer) |
| **External path cost** | Lower fees, data stored on cheaper [data availability layer](/data-availability-layer/) like Celestia |
| **Proof type** | Usually [zero-knowledge](/zero-knowledge-rollup/) to allow both paths with the same verification |
| **Key tradeoff** | Throughput and cost per transaction vs. direct settlement guarantee |

</aside>

## The core idea: menus instead of mandates

Traditional rollups impose a uniform data availability policy: all transactions go to one place, usually Ethereum blobs or an external data availability chain. For a user sending 1 dollar, that policy might be expensive or overkill. For a user settling a mortgage or moving a million-token balance, the same policy might feel weak.

A volition rollup inverts this. Instead of deciding for all users, the protocol lets each user specify their data availability preference when they sign the transaction. One user might say "I trust the Ethereum validator set; please post my data on-chain and charge me the blob fee." Another says "I trust Celestia's validators for this small transfer; post it there and charge me less." The rollup executes both, computes a single state root, and proves correctness of both paths with one zero-knowledge proof.

This flexibility is economically powerful. High-value or sensitive transactions anchor to Ethereum. Routine payments use cheaper external storage. The same account can do both in the same block.

## How the proof system must work

Naively, this seems impossible: if different transactions store data in different places, how can a single proof cover both? The answer lies in zero-knowledge proofs' flexibility. A ZK proof doesn't verify data directly; it verifies that the transactions executed correctly *given the data*. It doesn't care where the data physically is.

Here's the execution flow:

1. The sequencer collects transactions flagged for on-chain and external storage.
2. For on-chain transactions, the sequencer posts data to Ethereum (or the settlement layer) as usual.
3. For external transactions, the sequencer posts data to the external [data availability layer](/data-availability-layer/) (e.g., Celestia) and includes commitments (hashes or Merkle roots) of that data in the ZK proof inputs.
4. The sequencer constructs a single ZK proof that says: "I executed all these transactions in this order, assuming the on-chain data is correct (I'll prove that) and the external data matches the commitments (provided in the proof's public input)."
5. The proof is posted to the settlement layer. Verifiers check the proof; they don't re-fetch all the data because the proof attests to its correctness.

This works because the ZK proof is a cryptographic guarantee that the computation is sound. Verifiers trust the proof, not re-execution. On-chain data is directly verifiable by Ethereum's consensus; external data is vouched for by the external layer's consensus and the proof.

## Cost stratification and practical trade-offs

On-chain transactions typically cost 2–10 times more than external transactions, depending on network conditions and the relative cost of blob space vs. the external layer.

High-value transactions naturally gravitate on-chain. A 1-billion-dollar treasury transfer warrants the safety premium. Microtransactions and routine account-to-account transfers gravitate external. A 10-dollar payment to a friend can live on Celestia with the same finality guarantees as on-chain—just a different validator set.

Some applications mandate on-chain data for all users (for regulatory or business reasons). Others encourage external data to maximise throughput. Exchanges and lending protocols might use on-chain for deposits and withdrawals, external for internal transfers.

This stratification is honest economics: you pay more for more security. A volition rollup simply lets users and applications see and act on that difference, rather than hiding it in an average fee.

## Who verifies external data?

This is the crux of trust. For on-chain transactions, Ethereum's validator set guarantees data availability. For external transactions, it falls to the external [data availability layer](/data-availability-layer/)'s validators.

If you choose to store data on Celestia, you're trusting Celestia's 100+ validators to keep the data available. This is weaker than Ethereum's 500,000+ stakers, but Celestia is purpose-built for cheap, high-volume storage, so it compensates with economic incentives and fast recovery protocols. If Celestia's validators collude to withhold data, the transaction is lost—but the ZK proof is still valid on-chain, and the rollup's state is unchanged.

This risk is real but priced in. Users making external choices know they're accepting an external validator set's honesty. The application (or the rollup's governance) sets policy: "External data gets one week of guarantees on Celestia," "On-chain data gets unlimited access from Ethereum," etc.

Some volition rollups hedge by requiring rollup validators to also run light clients on the external layer, creating redundancy. Others tie external data verification to the rollup's own slashing mechanism: if a sequencer posts a proof claiming to have stored data externally but the external layer denies it, the rollup's validators can challenge and slash the sequencer.

## Governance and user education

Volition design creates a new governance problem: what are the supported external layers? How long does each store data? What happens if an external layer goes down?

The rollup must publish clear policy: "Data availability Layer A: 7 days, Celestia validators." "Layer B: 30 days, AVail validators." Users choosing Layer A accept that if they don't access their data within 7 days, they risk losing recovery options (though the on-chain state remains valid).

This demands user education that most rollups have not yet invested in. Many users don't understand the difference between "my data is on-chain" and "my data is external." A poorly designed volition rollup could see users accidentally picking external storage for high-value transactions and then panicking when data expires.

The best volition rollups make the default choice safe (on-chain for high values, external for dust) and provide UI warnings for unusual choices.

## Real-world instances and limitations

Starknet has researched volition extensively but has not widely deployed it. The infrastructure for cheaply posting to Starknet's own data availability layer (or to Celestia) is mature, but the proof system overhead—generating proofs that cover both paths—adds latency. For a high-throughput rollup, this proof generation cost can be substantial.

Another friction: most users don't want to choose. They want the rollup to be cheap and fast, period. Asking them to toggle a data availability preference adds cognitive load and potential for error. The rollup that automates this choice (inferring from transaction size, sender history, or explicit intent fields) will win user adoption over one that exposes the lever directly.

Volition is powerful for applications that can internalise the choice. A lending protocol might store collateral on-chain and internal transfers external. An exchange might store order books external and settlement on-chain. But for retail user-facing apps, volition remains a layer-2 primitive that builders use, not end-users invoke.

## See also

<div class="wiki-seealso">

### Closely related

- [Data Availability Layer](/data-availability-layer/) — the external storage option for volition transactions
- [Zero-Knowledge Rollup](/zero-knowledge-rollup/) — the proof system that makes volition's flexibility possible
- [ZkVM Architecture](/zkvm-architecture/) — the virtual machine used to generate proofs for volition execution
- [Proof Aggregation](/proof-aggregation/) — compressing volition proofs further by aggregating many into one
- Sequencer — the rollup operator routing transactions to their chosen data layer
- Ethereum Blob — the settlement-layer data availability option

### Wider context

- Rollup — the broader scaling solution that volition is a variant of
- [Blockchain Fundamentals](/blockchain-fundamentals/) — foundation concepts
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — typical application for volition designs

</div>
