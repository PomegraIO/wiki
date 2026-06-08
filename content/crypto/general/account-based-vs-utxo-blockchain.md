---
title: "Account-Based vs UTXO Blockchain Models"
description: "How Ethereum's account model and Bitcoin's UTXO model differ in design, privacy, and smart-contract support."
keywords:
  - account based vs utxo blockchain
  - account-based blockchain
  - UTXO blockchain model
  - Bitcoin ledger design
  - Ethereum ledger model
  - blockchain architecture
image: /svg/crypto.svg
---

*The two dominant blockchain ledger designs take fundamentally different approaches to storing and spending value. **Account-based** blockchains (Ethereum, most newer chains) treat users as accounts with balances, like a bank: you check your account, deduct a payment, and update the balance. **UTXO-based** blockchains (Bitcoin, Litecoin) treat money as discrete coins: you spend an old coin by referencing it and proving ownership, creating new coins in the process. The choice affects privacy, transaction throughput, smart-contract expressiveness, and the complexity of transaction validation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Account-Based vs. UTXO — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain." />

<div class="wiki-infobox-caption">Two ledger designs; radically different trade-offs in simplicity and capability.</div>

|   |   |
|---|---|
| **Core abstraction** | Accounts with balances (account-based) vs. Discrete spent/unspent coins (UTXO) |
| **Balance lookup** | Direct account state; single source of truth (account) vs. Scan unspent outputs; implicit (UTXO) |
| **Transaction** | Debit account A, credit account B (account) vs. Consume old output, create new outputs (UTXO) |
| **Change handling** | Automatic; new balance reflects debit (account) vs. Explicit; change address receives unspent amount (UTXO) |
| **Privacy level** | Lower; account balance is visible to chain (account) vs. Higher; no explicit balance; output ownership obscured (UTXO) |
| **Smart contracts** | Native support; contract state, loops, complex logic (account) vs. Limited; script language; no persistent state (UTXO) |
| **Parallelization** | Harder; state conflicts if multiple txs touch same account (account) vs. Easier; outputs are atomic; no conflicts unless same output spent twice (UTXO) |
| **Examples** | Ethereum, Solana, Polkadot, Cardano (mix) | Bitcoin, Litecoin, Monero |
| **Typical throughput** | Higher initially; state contention limits scaling (account) vs. Naturally parallel; higher throughput potential (UTXO) |
| **User experience** | Simpler; automatic balance tracking (account) vs. More complex; change, UTXOs to manage (UTXO) |

</aside>

## The account-based model: bank-like simplicity

An account-based blockchain assigns each user an account, identified by an address. The account holds a balance (e.g., 10 ETH). To spend, the user submits a transaction that says "debit my account by X, credit address Y by X." The network updates the account balance instantly.

**Key properties:**
- **State**: Each account has a nonce (transaction counter) and a balance. Contracts have storage (key-value maps).
- **Transaction validity**: A transaction is valid if the account nonce is correct and the balance is sufficient.
- **Simplicity**: Users think in terms of "I have 10 coins" and "I send 5 coins"—intuitive and familiar.

**Example transaction (Ethereum):**
```
From: 0xAlice
To: 0xBob
Amount: 1 ETH
Nonce: 42
```

Alice's account nonce increases to 43; her balance decreases by 1 ETH; Bob's balance increases by 1 ETH. The transaction is atomic.

## The UTXO model: coin-by-coin spending

A UTXO (Unspent Transaction Output) blockchain tracks *outputs*: coins created by prior transactions that have not yet been spent. To spend, you must reference the specific output by its transaction ID and index, prove you own it, and create new outputs.

**Key properties:**
- **State**: No account balances; only a set of unspent outputs (each with a value, owner, and conditions).
- **Transaction validity**: A transaction is valid if all inputs reference real, unspent outputs and are signed correctly.
- **Spending**: An output can be spent only once, in exactly one transaction. It either exists or it doesn't.

**Example transaction (Bitcoin):**
```
Input: Reference to a prior output (tx123, index 0) worth 5 BTC, signed by Alice
Output 1: 4 BTC to 0xBob
Output 2: 1 BTC to 0xAlice (change address)
Fee: 0 BTC (implicit)
```

The old output (5 BTC) is now marked spent. Two new outputs are created. Alice receives change; Bob receives the payment.

## The privacy angle

**Account-based privacy:**
Because the account balance is always visible and directly queryable, an observer can see:
- How much each account holds.
- The running balance of any address over time.
- The entire flow of funds.

This is bad for financial privacy. Ethereum addresses can sometimes be de-anonymized by cross-referencing on-chain data with exchange deposits or other public information.

**UTXO privacy:**
Because there are no "account balances," only discrete coins, the privacy model is slightly different:
- An observer sees outputs and their values, but not their owner (if keys are well-managed).
- A coin can be mixed or sent through many hands before reaching its final destination.
- Coins of different amounts can be aggregated in ways that obscure intent.

Bitcoin itself offers privacy only through pseudonymity (a random address). But the UTXO model enables privacy enhancements like CoinJoin (multiple parties mixing their coins) and Confidential Transactions (hiding amounts). Monero, a UTXO blockchain, uses similar techniques for much stronger privacy by default.

## Smart contracts and expressiveness

This is the defining difference for modern blockchains.

**Account-based contracts:**
Ethereum's account model lets contracts maintain state. A contract is an account that stores data (like a database row) and has executable code. Transactions invoke the contract, which can:
- Read and write its own storage.
- Read other contracts' storage (though not write).
- Call other contracts (and recurse).
- Use loops, conditionals, and state transitions.

A decentralized exchange, lending protocol, or voting system can be written because the contract remembers state across transactions.

**UTXO contracts:**
Bitcoin's UTXO model uses scripts—small programs that validate spending conditions. A script can check signatures, verify hashes, and enforce time locks. But scripts are:
- Stateless: They cannot read or write persistent storage. Each output is isolated.
- Non-recursive: A script cannot call another script directly.
- Limited: Bitcoin's script language deliberately lacks loops and complex logic.

This is intentional: Bitcoin prioritizes validation simplicity and security over expressiveness. A full-featured smart contract platform would require persistent storage, which the UTXO model doesn't provide natively.

## Scalability and parallelization

**Account-based bottlenecks:**
If two transactions touch the same account (e.g., two payments from Alice), they must be ordered sequentially. The validator must apply the first transaction, update Alice's nonce and balance, then apply the second. State contention limits parallel processing. At high transaction volumes, this becomes a bottleneck.

**UTXO parallelization:**
Transactions that spend different outputs can be validated in parallel. Output A and Output B are independent. Unless the same output is referenced twice (a double-spend), there is no conflict. This natural parallelism makes UTXO designs potentially more scalable.

In practice, both designs face scaling challenges, but they hit them from different angles. Account-based designs need sharding or layer-2s to manage state contention. UTXO designs need mechanisms to manage the growing set of unspent outputs (UTXO bloat).

## User experience and complexity

**Account model:** Users check "Do I have enough?" and send. The network handles nonces, change, and balance updates automatically. Mental model is straightforward.

**UTXO model:** Users must:
- Track which of their outputs are unspent.
- Select outputs to spend (coin selection).
- Generate change addresses and handle change.
- Avoid sending the same output twice.

This is why most UTXO wallets hide complexity behind a "select coins automatically" feature. But the abstraction leaks: if a user sends two transactions in quick succession and both reference the same unspent output, one will fail. Fee estimation is also more explicit (sum of inputs minus sum of outputs = fee).

## Hybrid and extended models

Some blockchains blend elements:

**Cardano (extended UTXO):**
Cardano is UTXO-based but extends scripts to allow limited state through [smart contracts](/smart-contract/). Outputs can carry arbitrary data (datum) and contracts can read that data. This offers some smart-contract expressiveness while retaining UTXO parallelism.

**Account with UTXO-like features:**
Account-based blockchains can layer UTXO-like logic through contract-based tokens. A token is a contract that maps addresses to balances. Transfer functions check and update those mappings, adding UTXO-like properties.

## Practical trade-off summary

**Choose account-based if:**
- You want to build a complex DeFi protocol with stateful contracts.
- User experience and simplicity matter more than peak throughput.
- You expect developers to write rich business logic (lending, trading, governance).
- Users are comfortable with standard interface conventions (nonces, balance updates).

**Choose UTXO if:**
- You prioritize validation simplicity and high throughput.
- Privacy enhancements matter (coins can be mixed more naturally).
- You expect transactions to be mostly independent (payments, transfers).

Bitcoin remains the gold standard for UTXO design; Ethereum remains the gold standard for account-based design. Neither is "better"—they optimize for different goals. The UTXO model is proven secure and efficient; the account model is proven flexible and developer-friendly.

## See also

<div class="wiki-seealso">

### Closely related

- [Bitcoin](/bitcoin/) — the original UTXO blockchain
- [Proof of work](/proof-of-work/) — consensus mechanism in UTXO chains
- [Proof of stake](/proof-of-stake/) — consensus mechanism in account-based chains
- [Smart contract](/smart-contract/) — programs enabled by account-based design
- [Distributed ledger](/distributed-ledger/) — the broader category of decentralized records
- [Blockchain fundamentals](/blockchain-fundamentals/) — foundational concepts

### Wider context

- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where coins from both models are traded
- [Market capitalization](/market-capitalization/) — valuation of chains using both models
- [Initial public offering](/initial-public-offering/) — fundraising for blockchain projects
- [Capital asset pricing model](/capital-asset-pricing-model/) — framework for pricing crypto assets

</div>