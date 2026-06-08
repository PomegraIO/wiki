---
title: "Forced Transaction Inclusion in Rollups"
description: "Forced inclusion is a censorship-resistance mechanism that lets users bypass a rollup sequencer and submit transactions directly to Ethereum when the sequencer refuses to include them."
keywords:
  - forced transaction inclusion
  - rollup censorship resistance
  - sequencer bypass
  - layer 2 fairness
image: "/svg/crypto.svg"
---

*A **forced-inclusion mechanism** is a safety valve that allows users to compel a rollup sequencer to include their transactions (or face financial consequences) when the sequencer tries to censor or stall them. By submitting a transaction directly to Ethereum's smart contract, a user can guarantee inclusion in the rollup, even if the sequencer refuses to cooperate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forced Inclusion — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">User protection against sequencer censorship.</div>

|   |   |
|---|---|
| **How it works** | User submits transaction to Ethereum contract; if sequencer ignores it for N blocks, it's forced into the rollup by protocol |
| **Cost** | Expensive (user must pay Ethereum gas); used only when censorship is imminent |
| **Activates** | After a timeout (typically 24 hours or longer), proving the sequencer is unresponsive |
| **Prevents** | Sequencer from indefinitely censoring a user's transactions |
| **Drawback** | Does not protect against sequencer reordering or MEV; only against outright refusal |

</aside>

## The Sequencer Censorship Problem

In most [Layer 2 rollups](/layer-2-scaling/) today, a single sequencer (or a small quorum) decides which transactions are included and in what order. This is efficient—one entity batches transactions and posts them to Ethereum—but it introduces a risk: the sequencer can **censor** a user by refusing to include their transactions, without breaking any rule or proving wrongdoing.

Imagine you want to close a leveraged position on a decentralized exchange, or withdraw your funds from a rollup. If the sequencer decides to censor you, you're stuck waiting indefinitely. You can't force the sequencer to process your transaction; you can only wait and hope.

Forced inclusion is the antidote. It says: "A user shouldn't be trapped indefinitely by a malicious sequencer. There must be a way out."

## How Forced Inclusion Works

The mechanism typically unfolds in two phases:

**Phase 1: User requests inclusion**

The user submits a transaction directly to the rollup's smart contract on Ethereum, encoding the action they want (e.g., "withdraw 100 tokens"). The contract records this request and starts a timer—say, 24 hours.

**Phase 2: If the sequencer ignores it**

If the sequencer includes the transaction in the rollup within the timeout, nothing further happens; the transaction is processed normally.

If the sequencer refuses to include it and the timeout expires, the contract forces inclusion by applying the transaction during the next state update. The rollup is obligated to process the forced transaction, or the state root (the cryptographic commitment to the rollup's current state) is invalidated and the rollup halts.

To make this credible, the sequencer must post **bonds** (collateral) to Ethereum. If a sequencer censors a forced transaction and is caught, it loses part of its bond as a penalty. This financial incentive keeps the sequencer honest: the cost of censoring exceeds the gain.

## Why Forced Inclusion Doesn't Solve All Sequencer Problems

Forced inclusion is powerful but not a panacea. It protects against **censorship by refusal**, but not against other sequencer misbehaviors.

**What forced inclusion prevents:**

- Indefinite stalling: A user can always force their transaction through after the timeout.
- Permanent lock-up: Users can always exit the rollup, even if the sequencer won't cooperate.

**What forced inclusion does NOT prevent:**

- **MEV (maximal extractable value):** The sequencer can still reorder your transaction to extract profit.
- **Front-running:** The sequencer can see your transaction and insert its own ahead of it.
- **Short-term delays:** The sequencer can stall you for up to the timeout window (often 24 hours).

For full fairness, forced inclusion needs to be combined with other mechanisms, like [enshrined rollups](/enshrined-rollup-ethereum/) (which give Ethereum validators control of sequencing) or commit-reveal schemes (which hide transaction contents until they're sealed in a block).

## The Timeout Window

The timeout is a critical parameter. Too short, and the sequencer is constantly forced to include user transactions, increasing costs and reducing efficiency. Too long, and users can be censored for days or weeks, defeating the purpose.

Most rollups set the timeout at 24 hours, a compromise:

- **Short enough** that users can exit or recover funds within a business day.
- **Long enough** that normal rollup operations aren't disrupted by forced-inclusion requests.

Some systems use a longer timeout (48 hours or more) for less-critical transactions, and a shorter timeout (1 hour) for emergency exits. The tradeoff reflects the designers' view of how much censorship risk is acceptable.

## Practical Example

Suppose Alice has $10,000 in a stablecoin on an Optimism-like rollup, and the sequencer censors her for unknown reasons. Here's what happens:

1. **Day 1:** Alice submits a forced-inclusion request to Ethereum to withdraw her $10,000.
2. **Day 1–24:** The sequencer has a 24-hour window to include Alice's withdrawal in the rollup. It refuses, either out of malice or because it's insolvent.
3. **Day 2 (midnight):** The timeout expires. The rollup contract on Ethereum automatically processes Alice's withdrawal, crediting her Ethereum address with $10,000 equivalent.

Alice has her funds back, albeit on mainchain (and she paid Ethereum gas fees to force inclusion). The sequencer's behavior has been proven hostile, and its bond may be slashed.

## Financial Incentives: Bonds and Slashing

For forced inclusion to work, the sequencer must have real stakes in the game. The mechanism relies on **sequencer bonds**:

When a sequencer joins a rollup, it posts a bond—say, $1 million in Ethereum or stablecoins. This bond is held in escrow by the smart contract.

If a sequencer censors a forced transaction:

1. The transaction is forced into the rollup state.
2. The contract detects the censorship (the sequencer signed off on a state root that violates the forced-inclusion rule).
3. A portion of the sequencer's bond is slashed and distributed to the user who submitted the forced request (as compensation) or burned.

The slashing penalty must be large enough that censoring a $100 transaction is not worth the reputational or financial risk. If the slashing is too small, the sequencer might rationally accept the loss.

## Forced Inclusion in Different Rollup Types

**Optimistic rollups** (like Optimism and Arbitrum) have built-in forced-inclusion mechanisms as a core safety feature. Users can always submit transactions to the contract; if the sequencer ignores them, they're forced in after the timeout. This is almost universally implemented.

**ZK rollups** (like StarkNet and some versions of zkSync) support forced inclusion but with a wrinkle: the sequencer must produce a valid zero-knowledge proof for every transaction, including forced ones. This is computationally expensive and can't be batched as efficiently. Some ZK rollups use a hybrid: fast, optimistic inclusion for normal sequencer batches, and slower, ZK-proven inclusion for forced transactions.

## The Cost of Forced Inclusion

Here's the catch: forcing a transaction through Ethereum costs **Ethereum gas**. If a user has to force-include a transaction, they pay Ethereum's gas fees directly (maybe $50–$500 in a high-congestion period), plus the rollup's own fee for that transaction.

This makes forced inclusion a last resort, not a normal path. Most users won't use it unless the sequencer is actually censoring them. The high cost acts as a deterrent to frivolous use and keeps the mechanism in the background, used only when needed.

## See also

<div class="wiki-seealso">

### Closely related

- [Layer 2 Scaling](/layer-2-scaling/) — the category forced inclusion serves
- [Optimistic Rollup](/optimistic-rollup/) — the rollup type most commonly using forced inclusion
- ZK Rollup — an alternative rollup type with different inclusion guarantees
- [Volition: User-Chosen Data Storage in ZK Rollups](/volition-user-choice-data-storage/) — another user-protection mechanism in scaling
- [Enshrined Rollups on Ethereum](/enshrined-rollup-ethereum/) — a longer-term alternative to sequencer reliance

### Wider context

- MEV and Maximal Extractable Value — a sequencer problem forced inclusion does not address
- [Smart Contract](/smart-contract/) — the underlying technology for forced-inclusion contracts
- [Ethereum](/ethereum/) — the base layer where forced inclusion is anchored
- Censorship Resistance — the principle forced inclusion protects

</div>
