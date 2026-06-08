---
title: "Account Abstraction on Layer 2"
description: "Layer 2 rollups can implement account abstraction natively, allowing smart contract wallets and custom transaction logic without mainchain limitations."
keywords:
  - account abstraction layer 2
  - l2 smart contract wallets
  - erc-4337 on rollups
  - native account abstraction
image: "/svg/crypto.svg"
---

*Layer 2 rollups are ideal environments for implementing **account abstraction** because they have full control over their state-transition rules and don't face Ethereum mainchain's protocol constraints. Users can run smart contract wallets with custom validation logic, batched transactions, and gas sponsorship without the architectural workarounds required on Ethereum.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Account Abstraction on Layer 2 — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Native smart wallet support on scaling layers.</div>

|   |   |
|---|---|
| **What it enables** | Smart contract accounts as the default; no need for externally owned accounts (EOAs) |
| **Why L2 is easier** | Rollups control consensus rules; no need for mainchain hard forks or workarounds |
| **Common approach** | Sequencer or bundler collects user operations and batches them into transactions |
| **User benefit** | Better UX (no private key, social recovery, flexible gas payment) and lower fees through batching |
| **Tradeoff** | More dependencies on sequencer or bundler; not purely trustless like mainchain |

</aside>

## The Mainchain Constraint

On [Ethereum mainchain](/ethereum/), account abstraction is difficult because consensus rules treat externally owned accounts (EOAs) specially: only an EOA can pay gas and initiate a transaction. If you want to use a smart contract wallet instead, you must work around this constraint—either by relying on a meta-transaction relayer (trusted intermediary) or by implementing ERC-4337, which creates a separate "mempool" of user operations processed by bundlers.

Both approaches add friction and dependencies. ERC-4337, the mainchain standard, works but introduces new slippage points: bundlers can delay or refuse to bundle your transaction, and smart contract wallets depend on a relayer or bundler staying solvent.

[Layer 2 rollups](/layer-2-scaling/), by contrast, have full sovereignty. The rollup defines its own state-transition function and consensus rules. There's no need to ask Ethereum for permission or work within mainchain constraints. **The rollup can simply bake account abstraction into its consensus layer.**

## How Native Account Abstraction Works on L2

In a rollup that implements native account abstraction, the sequencer treats smart contract accounts and EOAs identically. Both can initiate transactions; both can pay gas; both are validated the same way (by invoking a user-defined validation function).

**Typical flow:**

1. User (or their wallet) creates a smart contract account on the rollup. No private key is needed; the account can be secured via social recovery, multisig, or any custom logic the user chooses.
2. User wants to execute a transaction (send tokens, swap on a DEX, etc.). They sign a message with their preferred signing key (or keys) and submit it to the rollup's transaction pool.
3. The sequencer (or a bundler) receives the signed message (called a "user operation" in this context). It checks whether the user's account is willing to pay for the transaction.
4. If the account's validation logic approves, the sequencer includes the transaction and the account pays gas from its balance.

No distinction between smart accounts and EOAs. No special relayer layer. No mainchain fallback needed.

## Why Rollups Enable This

Rollups have three advantages that make native account abstraction straightforward:

**1. Protocol sovereignty:** The rollup's state-transition function is flexible. Designers can change consensus rules without a mainchain hard fork. They can say, "All accounts are smart contract accounts; all transactions go through a validation function," and that's law on the rollup.

**2. Sequencer control:** The sequencer processes transactions in the order it chooses (subject to fairness mechanisms). It can easily batch user operations, combine them, and amortize the cost of validation and state updates. This drives down per-transaction overhead.

**3. Lower gas cost:** Rollups are cheaper than mainchain anyway (due to data compression and shared infrastructure). Adding smart contract logic doesn't proportionally increase cost; a smart account transaction on L2 can cost 1–5 cents, while the same transaction would cost dollars on mainchain.

## Smart Wallet Features on L2

Native account abstraction on L2 unlocks user-friendly features that mainchain EOAs can't offer:

**Social recovery:** If you lose your signing key, designated friends or family can help you recover access by signing a recovery transaction. Your account is secured without a single private key; it's secured by your social graph.

**Multisig:** Multiple signers can be required for large transactions. A business account might require 3 of 5 partners to approve a withdrawal.

**Sponsored gas:** A business or a DAO can sponsor gas fees for their users. Users don't hold Ethereum; they just use the app, and the DAO pays for their transactions. The UX feels web2-native.

**Batching:** Users can queue up multiple transactions (swap, bridge, staking) and have them all execute in one atomic batch, reducing slippage and fee overhead.

**Session keys:** A user can create temporary signing keys with limited scope (e.g., "spend up to $10 today") for mobile dApps or gaming, without needing to carry their master key.

None of these are easy on mainchain. On L2, they're native.

## Trade-offs: Rollup-Level Dependencies

The flip side is that native account abstraction on L2 introduces new dependencies—all at the rollup level rather than the mainchain.

**Sequencer risk:** If the rollup's sequencer censors or stalls, you can't submit transactions. Yes, most rollups have [forced inclusion](/forced-transaction-inclusion-rollup/) as a safety valve, but that requires posting to Ethereum and waiting 24 hours. For normal operation, you're dependent on the sequencer's liveness.

**Bundler risk:** If the rollup uses a bundler model (like ERC-4337), you're also dependent on bundler availability. A bundler can refuse to bundle your operation.

**Validator set trust:** You're trusting the rollup's validator set to honestly apply the state-transition rules. If validators become corrupt, accounts can be drained. (This risk exists on mainchain too, but Ethereum's validator set is much larger and more diverse than most rollups'.)

These risks are real but not necessarily fatal. Many users accept them in exchange for better UX and lower costs. The tradeoff shifts: mainchain gives you maximal decentralization but poor UX; L2 gives you good UX but introduces layer-specific risks.

## Comparison to Mainchain ERC-4337

ERC-4337 is Ethereum mainchain's standardized approach to account abstraction. It works by creating a separate mempool ("alt-mempool") of user operations, separate from regular transactions. Bundlers listen to this mempool, collect operations, and submit bundles to a smart contract on mainchain.

**ERC-4337 pros:**
- Fully mainchain-based; no L2 trust assumptions.
- Works with any wallet and app that implements the standard.

**ERC-4337 cons:**
- Bundlers are a new entity; they can censor or reorder operations.
- Operations are expensive because they go through mainchain gas pricing.
- Extra validation and contract calls add overhead.

**Native L2 account abstraction pros:**
- Integrated into the rollup's consensus; no separate bundler layer needed.
- Much cheaper than mainchain ERC-4337.
- Sequencer can optimize state transitions for smart accounts.

**Native L2 pros cons:**
- Non-standard; each rollup might implement it differently.
- Dependent on the rollup's sequencer and validator set.

Many rollups (like StarkNet, which requires smart contract accounts) opt for native abstraction. Others (Arbitrum, Optimism) support both: they run ERC-4337 for mainchain compatibility, but allow rollup-level account abstraction as an alternative.

## Real-World Example

Imagine a mobile gaming app on StarkNet (a rollup with native account abstraction):

1. **User onboarding:** A player downloads the app and signs up. The app creates a smart contract account for them, protected by their email and a backup phone number (social recovery).

2. **No wallet setup:** The player never sees a private key. They just log in like a normal web2 app.

3. **In-game transactions:** The player buys an in-game asset. The game sponsor pays the gas fee. The transaction costs less than a cent.

4. **Lost phone:** If the player loses their phone, they prove their identity by email and regain access to their account in minutes. No seed phrase, no vault. They can immediately resume playing.

This UX is nearly impossible on mainchain. On L2 with native account abstraction, it's standard.

## Protocol-Level vs. Application-Level Abstraction

It's worth noting that "native account abstraction" comes in degrees:

- **Full protocol-level abstraction:** The rollup's state-transition function treats all accounts as smart contracts and validates all transactions via custom logic. Examples: StarkNet, Starkware rollups.

- **Application-level abstraction:** The rollup supports EOAs natively (for compatibility and efficiency) but allows dApps to implement smart account abstraction via contracts. Examples: Arbitrum, Optimism with ERC-4337.

Both are valid. Protocol-level abstraction is more elegant and gas-efficient. Application-level abstraction is easier to implement and leaves room for evolving standards.

## See also

<div class="wiki-seealso">

### Closely related

- [Layer 2 Scaling](/layer-2-scaling/) — the environment that enables native account abstraction
- ERC-4337 — the mainchain standard for account abstraction
- [Forced Transaction Inclusion in Rollups](/forced-transaction-inclusion-rollup/) — the safety valve against sequencer censorship
- [Volition: User-Chosen Data Storage in ZK Rollups](/volition-user-choice-data-storage/) — another L2 design that empowers users
- [Optimistic Rollup](/optimistic-rollup/) — one rollup type implementing account abstraction

### Wider context

- [Smart Contract](/smart-contract/) — the technology underlying smart contract wallets
- Externally Owned Account (EOA) — the traditional Ethereum account type
- [Ethereum](/ethereum/) — the mainchain for comparison
- Meta-Transaction Relayer — a workaround on mainchain

</div>
