---
title: "Internet Computer"
description: "A blockchain that executes smart contracts directly as native code on dedicated hardware rather than in a virtual machine or emulated environment."
keywords:
  - internet computer
  - canister smart contracts
  - blockchain execution
  - dfinity
  - smart contract performance
image: "/svg/crypto.svg"
---

*The [Internet Computer](/internet-computer/) is a public [blockchain](/distributed-ledger/) operated by DFINITY that runs smart contracts—called canisters—as WebAssembly binaries executed directly on dedicated hardware, rather than in an Ethereum-like virtual machine. This direct execution model permits substantially higher throughput and lower latency than chains that emulate a single virtual machine across a distributed consensus layer.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Internet Computer — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain topics." />

<div class="wiki-infobox-caption">A blockchain that runs smart contracts as native WebAssembly on specialised hardware.</div>

|   |   |
|---|---|
| **What it is** | A [blockchain](/distributed-ledger/) that executes smart contracts (canisters) in WebAssembly runtime directly on nodes |
| **Smart contract model** | Canisters—WebAssembly modules with persistent state, HTTP API, and message passing |
| **Consensus** | [Proof of Stake](/proof-of-stake/) with threshold cryptography |
| **Transaction model** | Asynchronous message passing between canisters; no global transaction ordering |
| **Native token** | ICP (Internet Computer Protocol) |
| **Key differentiator** | Direct hardware execution rather than EVM emulation; higher throughput |

</aside>

## The virtual machine bottleneck

When [Ethereum](/ethereum/) launched, it introduced the Ethereum Virtual Machine (EVM)—a standardised bytecode interpreter that runs on every validator node. This design choice was pragmatic: any device capable of running the EVM could become a validator, lowering barriers to entry and distributing validation widely.

But the EVM imposes a cost. Every transaction must be executed on the EVM bytecode interpreter running on every node in the network. If a transaction takes 1 millisecond to execute on a modern CPU, and consensus requires that thousands of nodes execute it in lock-step, the bottleneck is not computation—it is the coordination of computation. The network's throughput ceiling is determined by the slowest node, multiplied by how many transactions you can pack into a single block. For [Ethereum](/ethereum/), this yields roughly 15–30 transactions per second in practice.

Rollups like [Scroll](/scroll/) and Optimism partially escape this trap by bundling many transactions into a single [Ethereum](/ethereum/) transaction, then executing them on dedicated hardware outside the main chain and posting a proof back to [Ethereum](/ethereum/). That works, but it adds latency and introduces a trusted coordinator.

## Internet Computer's direct execution model

The Internet Computer abandons the idea of a single universal virtual machine. Instead, it partitions the network into subnets, each of which holds copies of a subset of canisters (smart contracts). Within a subnet, nodes reach [consensus](/central-bank/) via threshold cryptography and a Byzantine fault-tolerant protocol on the ordering of incoming messages.

Canisters are WebAssembly modules compiled ahead of time. When a message arrives for a canister, the nodes in that canister's subnet execute the WebAssembly code directly—not interpreted through a bytecode VM, but run natively using a WebAssembly runtime. This is faster and more flexible than the EVM. Developers can write canisters in Rust, TypeScript, or other languages that compile to WebAssembly; they are not constrained to Solidity or EVM bytecode.

Each canister has its own persistent state stored on-chain. Messages between canisters and from external users are asynchronous. Unlike [Ethereum](/ethereum/), where a transaction atomically affects multiple contracts and updates the global state in a single block, Internet Computer messages are delivered sequentially to each canister, and a canister's response may not arrive immediately. This asynchronous model is more complex for developers to reason about, but it allows the network to execute many canisters in parallel without global coordination.

Because subnets do not all order transactions together, the Internet Computer does not have a single canonical "block" in the way [Bitcoin](/bitcoin/) or [Ethereum](/ethereum/) do. Instead, each subnet produces its own finality independently. Inter-subnet communication is deferred—messages are queued and delivered asynchronously. This design allows the network to scale: you can add more subnets and more canisters without slowing down consensus on any one subnet.

## Practical implications

The trade-off is that development is different. An [Ethereum](/ethereum/) developer is used to atomic transactions and synchronous contract calls; Internet Computer development requires reasoning about message queues and eventual consistency. The programming model is less familiar to the Web3 developer base, which partly explains why Internet Computer's adoption lags behind [Ethereum](/ethereum/).

That said, the throughput advantage is real. Internet Computer subnets can handle thousands of transactions per second. Canister execution latency is lower than EVM contract calls, because WebAssembly runs faster than bytecode interpretation. If your application can tolerate asynchronous semantics, Internet Computer offers superior performance.

The network also includes an HTTP gateway that allows canisters to serve HTTP directly to browsers, without an intermediary. This design target—replacing traditional cloud infrastructure—is reflected in the canister model. You can run a full web application (frontend and backend) on Internet Computer without traditional servers.

## Governance and risk

Internet Computer uses [Proof of Stake](/proof-of-stake/) for validator selection and rewards. The network is governed by token holders through a decentralised nervous system (DNS), a smart contract that manages protocol upgrades and parameter changes. ICP tokens are staked to participate.

The direct execution model introduces some security risks. Because canisters run WebAssembly directly, the sandbox must be robust—WebAssembly runtime implementations can have exploits. [Ethereum](/ethereum/) contracts are constrained by the EVM's limited instruction set; a canister's WebAssembly code has more power and thus more surface area for bugs.

## See also

<div class="wiki-seealso">

### Closely related

- [Blockchain Fundamentals](/blockchain-fundamentals/) — underlying consensus and execution concepts
- [Proof of Stake](/proof-of-stake/) — consensus model used by Internet Computer
- [Distributed Ledger](/distributed-ledger/) — technology category Internet Computer belongs to
- [Ethereum](/ethereum/) — major smart contract platform with different execution model
- Smart Contracts — general concept of on-chain code execution

### Wider context

- [Flow](/flow-blockchain/) — alternative L1 scaling approach
- [Celo](/celo/) — another L1 with different design priorities
- [Scroll](/scroll/) — L2 scaling solution for Ethereum
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where ICP is traded
- [Bitcoin](/bitcoin/) — original blockchain without smart contracts

</div>
