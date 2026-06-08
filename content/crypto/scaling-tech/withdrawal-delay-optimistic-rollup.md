---
title: "Withdrawal Delay in Optimistic Rollups"
description: "Why optimistic rollups require a 7-day challenge period before fund withdrawals and how fast-exit bridges work around it."
keywords:
  - optimistic rollup withdrawal delay
  - challenge period seven days
  - fast exit bridge
  - rollup withdrawal mechanism
  - fraud proof window
---

*Withdrawing funds from an **optimistic rollup** requires waiting a challenge period—typically seven days—because the rollup relies on fraud proofs to guarantee correctness. During this window, validators check that the rollup's state transition is valid; if fraud is detected, withdrawals are halted and the invalid state is reverted. Fast-exit bridges offer instant withdrawal by assuming the fraud-proof risk on behalf of users.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Withdrawal Delay in Optimistic Rollups — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The delay ensures fraud is detected before funds leave the system.</div>

|   |   |
|---|---|
| **Typical delay** | 7 days (604,800 seconds); Optimism, Arbitrum, Base |
| **Why it exists** | Time needed for validators to challenge a proposed state root; if valid, funds are unlocked |
| **What triggers it** | Withdrawal initiation; the clock starts when a user submits a withdrawal proof on Ethereum |
| **What happens during** | Validators monitor the rollup; anyone can submit a fraud proof if the state is invalid |
| **If fraud is detected** | All withdrawals from that batch are blocked; state is rolled back; bad sequencer is penalized |
| **How to bypass it** | Fast-exit bridges that front the capital and assume the fraud risk themselves |
| **Risk acceptance** | Bridge operator must trust the rollup but can absorb small fraud events; users gain instant liquidity |

</aside>

## Why Optimistic Rollups Need a Challenge Period

An optimistic rollup assumes all state transitions are correct unless proven otherwise. Instead of computing a validity proof for every batch (like ZK rollups do), optimistic rollups simply post the new state root and data to Ethereum, assuming it's valid.

If a sequencer or prover proposes an invalid state root, any validator can submit a **fraud proof** that demonstrates the invalidity by re-executing the disputed transactions and showing that the claimed state root is wrong. The fraud proof is verified on Ethereum's layer 1, and if valid, the invalid state is rejected and rolled back.

But fraud proofs take time to prepare and verify on chain. An honest validator must:

1. Download and verify the rollup's transaction data.
2. Execute the transactions in the dispute window.
3. Identify the specific dispute (which transaction execution step is wrong).
4. Construct a proof of the error and submit it on Ethereum.

This process can take hours to days depending on batch size and complexity. To be safe, Ethereum cannot allow withdrawals from a state root until it's proven correct or the window for fraud proofs expires.

Thus: a **challenge period**, usually seven days, during which any validator can submit a fraud proof. If no fraud is detected by the end of seven days, the state root is finalized and withdrawals are unlocked.

## The Mechanics of the Withdrawal Queue

When a user initiates a withdrawal from an optimistic rollup:

1. The user creates a withdrawal transaction on the rollup, specifying the amount and destination address on Ethereum.
2. The rollup includes this transaction in a batch and posts the batch to Ethereum.
3. The user submits a **withdrawal proof** on Ethereum showing that the transaction was included in a finalized batch.
4. Ethereum verifies the proof (via Merkle tree verification) and queues the withdrawal.
5. The challenge period begins. The user must wait seven days.
6. After seven days without a successful fraud proof, the state root is finalized.
7. The user can now claim their funds on Ethereum, and the withdrawal executes.

During the challenge period, the user's funds are not yet on Ethereum layer 1. They remain locked in the rollup's bridge contract, awaiting finalization.

## What Happens If Fraud Is Detected

If a validator detects an invalid state root and submits a valid fraud proof during the challenge period:

- The state root is revoked.
- All pending withdrawals from that batch are canceled.
- The user's funds remain in the rollup's bridge contract.
- The rollup's sequencer or prover is penalized (if there is a bond or stake system).
- Affected users must wait for the rollup to correct the error and post a new, valid state root.

This is rare in practice. Optimistic rollups like Optimism and Arbitrum have strong monitoring systems and validator incentives to catch fraud quickly. But the seven-day delay exists to give the system time to detect and prevent such attacks.

## Economic and User Experience Impact

A seven-day withdrawal delay is acceptable for many use cases but problematic for others. A user exiting a position during market volatility might miss the optimal time to execute. A user moving funds between rollups must wait a week, creating friction.

This delay has created a demand for faster exits, and bridges have filled that gap.

## Fast-Exit Bridges and How They Work

A fast-exit bridge allows a user to withdraw instantly by relying on a third party to verify the state and front the capital.

The mechanism: The bridge operator watches the rollup and verifies that the user's withdrawal transaction is valid (included in a rollup batch that will eventually finalize). The operator then immediately transfers the user's funds on Ethereum at a small discount (e.g., 0.1% fee). The operator then waits for the seven-day finalization window to close, claims the official withdrawal from the rollup contract, and pockets the fee.

From the user's perspective: Instant withdrawal, small fee. From the bridge operator's perspective: capital tied up for seven days, plus risk that the withdrawal is fraudulent and the state is rolled back.

If the rollup's state is rolled back, the bridge operator's claim is invalid, and they lose their capital (or must pursue claims against the rollup for compensation). In practice, this is rare, so the operator can profitably offer the service if they can aggregate demand and earn enough in fees.

**Examples**: Across many rollups, third-party bridges (and official bridge integrations) offer fast-exit liquidity. Optimism's official bridge includes a Rapid Release option (for certain partners) that allows faster withdrawal. Arbitrum has third-party services offering instant exits.

The fee varies from 0.05% to 0.5% depending on competition and rollup security assumptions.

## Trade-off: Liquidity vs. Trust

Using a fast-exit bridge trades finality certainty for liquidity. A user gets their funds instantly but depends on the bridge operator's willingness to pay them out. If the bridge operator is illiquid or defaults, the user may not get paid until the official seven-day window closes.

The official seven-day withdrawal is always available as a fallback, so users have a guaranteed exit even if bridges collapse. This "backstop" gives bridges confidence to offer liquidity.

For large withdrawals or users who cannot afford the bridge fee, waiting seven days is the standard path.

## Why Seven Days Specifically?

The seven-day window was chosen as a balance between:

- **Security**: Long enough for monitors to detect fraud and submit a proof, even if Ethereum is congested.
- **UX**: Short enough that it's not prohibitively slow for most use cases (not 30 days).
- **Validator hardware**: Long enough to allow sophisticated dispute games (like Optimism's newer interactive fraud proofs) to resolve without timing out.

Different rollups could choose different windows. Arbitrum One uses seven days; some newer rollups experiment with shorter windows (e.g., Optimism's newer upgrades discuss reducing it to 1–2 days with more sophisticated fraud-proof systems).

Shorter windows require faster fraud proof verification, which might mean more specialized hardware or accepting higher trust in the validators monitoring the rollup.

## Connection to Finality and Layer 2 Risk

The seven-day delay is one of the main differences between Ethereum layer 2 and a true sidechain or independent chain. Ethereum itself achieves practical finality in 12–15 minutes via consensus and economic slashing. An optimistic rollup achieves theoretical finality only after the fraud-proof window closes.

Users who need immediate finality guarantees (e.g., making a loan on Ethereum and using rollup funds as collateral) cannot do so until the rollup state is finalized. This creates a ceiling on how much value flows through the rollup initially.

Over time, as validator infrastructure matures and fraud-proof systems become more sophisticated, the window could shrink. But as long as fraud proofs remain the security model, some challenge period is necessary.

## See also

<div class="wiki-seealso">

### Closely related

- [Optimistic Rollup](/optimistic-rollup/) — rollup using fraud proofs for security
- Fraud Proof — cryptographic proof that a state transition is invalid
- Fast-Exit Bridge — service allowing instant withdrawal from rollups by fronting capital
- ZK Rollup — alternative scaling design without withdrawal delay
- Finality — when a transaction is guaranteed not to be rolled back
- Withdrawal Proof — Merkle proof that a withdrawal transaction is included in the rollup

### Wider context

- Ethereum Layer 2 — category of rollups and other solutions building on Ethereum
- Challenge Period — general concept of fraud-proof windows in blockchain systems
- State Root — cryptographic commitment to a blockchain's account state

</div>
