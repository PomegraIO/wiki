---
title: "Polkadot XCM Cross-Chain Messaging"
description: "XCM is Polkadot's message format for cross-chain asset transfers and program execution. Explains how parachains and external chains interoperate."
keywords:
  - polkadot xcm cross-chain messaging
  - xcm protocol polkadot
  - cross-chain asset transfer polkadot
  - parachain communication
  - xcm instructions
  - interoperability polkadot
image: "/svg/crypto.svg"
---

*The **Polkadot XCM** (Cross-Consensus Message) format is a language for sending arbitrary instructions and assets across parachains, bridges, and external blockchains connected to the Polkadot ecosystem. Unlike traditional point-to-point bridges, XCM decouples the message format from the transport layer, allowing a single standard to route commands and tokens across heterogeneous chains.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Polkadot XCM — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A standardized message protocol enabling cross-chain operations without proprietary adapters.</div>

|   |   |
|---|---|
| **Core purpose** | Define and execute instructions across chain boundaries (asset transfers, contract calls, etc.). |
| **Format** | Stack-based bytecode; each XCM instruction operates on a state machine. |
| **Transport** | Agnostic to how messages arrive; can travel via parachain channels, bridges, or external relays. |
| **Common operations** | Transfer assets, mint/burn, execute smart contract calls, lock funds, report status. |
| **Versioning** | Multiple XCM versions coexist; chains must negotiate which version to use. |
| **Execution model** | Deterministic; the same message yields the same outcome on every run (if chain state is identical). |
| **Typical use** | Move staking tokens between parachains, bridge assets from Ethereum, swap cross-chain. |

</aside>

## The problem XCM solves

Polkadot's architecture splits the network into a central relay chain and up to hundreds of parachains—each with its own state, [smart contract](/smart-contract/) runtime, and validator set. Without a common messaging standard, cross-chain operations would require custom bridges and adapters for every pair of chains. A bridge from Acala to Moonbeam would be unique; a bridge from Acala to Centrifuge would require different logic. This duplicates work and fragments liquidity.

XCM provides a lingua franca. Any parachain or external chain can emit an XCM message without knowing the recipient's internal implementation. The recipient interprets the message according to the XCM spec and executes the requested action (or rejects it). A single bridge (or routing layer) can then carry XCM messages across chain boundaries, and each chain's runtime is responsible for understanding and executing XCM instructions targeted at it.

## XCM structure: instructions and registers

An XCM message is a sequence of instructions, each one modifying an internal state machine. The machine maintains several registers:

- **Origin**: Which account or parachain is sending the message.
- **Holding register**: Assets currently under the message's control (to be transferred, locked, or minted).
- **Execution context**: Which chain is executing the message and what permissions apply.

A typical XCM message might look (in conceptual form):

1. **WithdrawAsset** — Remove 100 units of Token X from the sender's account and place them in the holding register.
2. **BuyExecution** — Use some of the held assets to pay for the cost of executing remaining instructions on the destination chain.
3. **DepositAsset** — Transfer the remaining held assets to a target account on the destination chain.
4. **SetAppendix** — Attach a callback instruction to report success or failure back to the origin.

Each instruction is executed in order, and if any fails, the message stops (though the appendix may still run to signal the error).

## Asset representation and teleportation

XCM distinguishes between two cross-chain asset models:

**Teleportation** — Assets are burned on the sending chain and minted on the receiving chain. This requires tight trust and consensus: both chains must agree on the teleport protocol, and the total supply must be synchronized. Teleportation works well for native tokens of a parachain (e.g., Acala's ACA token teleporting to other parachains). The "teleported" asset on the destination is a wrapped representation, but it is fungible with the original and can be teleported back.

**Reserve-backed transfers** — A token lives on a "reserve" chain (e.g., USDT on a staking contract on Polkadot's relay chain or on an external bridge). When transferred to a destination chain, the token is minted as a wrapped version backed by a reserve held on the origin chain. The destination chain's version is a liability of the reserve chain. This model is more permissive (no consensus required, only that the reserve chain and destination chain agree on the protocol) but introduces counterparty risk: the destination depends on the reserve chain's solvency and honesty.

A third model, **liquidity pools**, uses [automated market makers](/automated-market-maker/) to convert tokens on-chain; less common in XCM but increasingly used for cross-chain swaps.

## Common XCM instructions

XCM defines dozens of instructions. A few essentials:

| Instruction | Purpose |
|---|---|
| **WithdrawAsset** | Deduct assets from an account and place in the holding register. |
| **DepositAsset** | Send held assets to a beneficiary account. |
| **TransferAsset** | Atomic shorthand for withdraw, then deposit. |
| **BuyExecution** | Consume held assets to pay for execution fees on the destination chain. |
| **SendXcm** | Send another XCM message to a further destination (enables nested routing). |
| **Transact** | Execute an extrinsic (or smart contract call) on the destination chain. |
| **LockAsset** | Lock an asset until a condition is met or a timeout expires. |
| **ReportError** | Send an error notification back to the origin. |
| **SetAppendix** / **SetErrorHandler** | Attach fallback logic if the main message fails. |

The set is extensible; chains can define custom instructions if needed.

## Message routing: how XCM gets delivered

XCM itself is a format, not a transport. Messages must be carried by some mechanism:

**Parachain channels** — Parachains connected to the Polkadot relay chain can exchange XCM messages via special "horizontal" messaging queues built into the relay chain. A parachain sends an XCM to another parachain's input queue, and the destination processes it on the next block.

**Bridges** — External chains (e.g., Ethereum, Cosmos, or Bitcoin) connected to Polkadot via bridges (e.g., via a bridge pallet or a dedicated bridge chain like Polkadot's Parity) can send and receive XCM messages. The bridge translates between the external chain's native format and XCM.

**Smart contracts** — Some parachains run the XCM interpreter as a smart contract, allowing application-level logic to send XCM messages without relay-chain consensus. This enables more flexible (but potentially riskier) routing.

## XCM versions and compatibility

XCM has evolved through multiple versions (v0, v1, v2, v3, v4), each adding features and fixing issues. The challenge is that older and newer versions coexist; not all chains upgrade immediately.

When a sending chain and destination chain support different XCM versions, they must negotiate:
- The **highest common version** is used (e.g., if sender supports v3 and receiver supports v2, they use v2).
- Alternatively, a **transpiler** converts messages between versions.
- If no common version exists, the message is rejected.

This compatibility burden is a known pain point. Developers must check version support before routing messages to an unfamiliar destination.

## Execution guarantees and failure handling

XCM messages are **deterministic** within a single chain: given the same state and the same XCM input, every run produces the same outcome. However, messages are not **atomic** across chains. A message can succeed on the sending chain but fail on the destination, or vice versa.

If an XCM instruction fails, execution stops and the remaining instructions are skipped (unless an error handler is attached). For example:

1. Sender teleports 100 ACA to a destination parachain.
2. The message includes an instruction to swap 50 ACA for USDT on the destination.
3. If the swap fails (due to slippage or insufficient liquidity), the **swap** instruction fails, but the **teleport** has already succeeded. The 100 ACA is now on the destination chain, unswapped.

To mitigate this, messages can include an **appendix** (a fallback set of instructions) or error handlers. For example:

- If the swap fails, execute an appendix that deposits the 100 ACA to a safe account instead of trying again.
- If that appendix also fails, emit a **ReportError** instruction to notify the origin.

This is not true atomicity, but it allows for graceful degradation.

## Practical examples: staking and bridges

**Cross-parachain staking**: A user on Acala (parachain 1) wants to stake ACA tokens on Moonbeam (parachain 2) in a liquid-staking pool. The user constructs an XCM message:
1. Withdraw 1000 ACA from their Acala account.
2. Send to Moonbeam.
3. Deposit 1000 ACA to the liquid-staking pool contract.
4. Receive liquid-staking receipt tokens (e.g., stACA) back to their Moonbeam account.

The relay chain routes the message via the horizontal channel, and Moonbeam's runtime executes it.

**Bridge from Ethereum**: A bridge relayer watches an Ethereum smart contract. When a user locks 10 USDT, the relayer constructs an XCM message:
1. Mint 10 units of a wrapped USDT token on the destination Polkadot parachain.
2. Deposit to the user's account.

The bridge validates that the lock on Ethereum is final before submitting the XCM.

## Risks and limitations

**Oracle dependence** — XCM itself does not include oracle data. If an XCM message needs to execute based on the price of an asset, it must fetch the price from an oracle—introducing price-feed risk and potential disputes.

**Bridging risk** — While XCM is a solid protocol, the bridges that carry it are often custom and have suffered exploits. A bridge hack can move funds maliciously across chains, even if the XCM format itself is correct.

**Version fragmentation** — The coexistence of multiple XCM versions creates a fragmented ecosystem. New chains or major upgrades can introduce version incompatibilities.

**Execution latency** — Messages are not instant. A cross-chain transaction may take several block times to confirm on both chains, creating a window for state changes that invalidate the message's assumptions.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart contract](/smart-contract/) — what XCM messages can invoke on destination chains
- [Blockchain fundamentals](/blockchain-fundamentals/) — distributed consensus underlying cross-chain messages
- [Distributed ledger](/distributed-ledger/) — shared state management across chains
- [Proof of stake](/proof-of-stake/) — Polkadot's consensus mechanism, which secures XCM execution

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where wrapped cross-chain tokens are traded
- [Ethereum](/ethereum/) — a major source and destination of XCM messages via bridges
- [Bitcoin](/bitcoin/) — increasingly connected via bridges that use XCM-like standards
- [Yield curve](/yield-curve/) — analogy: rates at different maturities; XCM enables different "settlement curves" across chains

</div>
