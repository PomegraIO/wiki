---
title: "NEAR Protocol Account Model"
description: "NEAR Protocol uses human-readable account names and an access-key system instead of cryptographic addresses, enabling sub-accounts and streamlined key recovery."
keywords:
  - near protocol account model
  - near human readable accounts
  - near access keys
  - near sub-accounts
  - near vs ethereum accounts
  - near protocol key recovery
image: "/svg/crypto.svg"
---

*The **NEAR Protocol account model** uses human-readable names like `alice.near` instead of hexadecimal addresses, and associates multiple access keys with each account rather than tying a single private key to a single signature type. This design trades some cryptographic minimalism for better usability and flexibility.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">NEAR Accounts — named and multi-key</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">NEAR reimagines blockchain accounts around human names and separate keys for different permissions.</div>

|   |   |
|---|---|
| **Account identifier** | Human-readable name (e.g., `alice.near`) |
| **Address format** | Not hex; registered as a name on chain |
| **Keys per account** | Multiple; each with separate permissions |
| **Key types** | Full access, function-call restricted |
| **Sub-account support** | Yes; e.g., `wallet.alice.near` |
| **Key recovery** | Easier; no private-key exodus to rebuild |
| **Comparison** | Ethereum uses addresses derived from keys |

</aside>

## The naming system

In Ethereum and Bitcoin, your account is your address: a fixed string derived from your public key, typically 42 characters (`0x...`) or 34 characters for Bitcoin. You generate a keypair, hash it, and that hash is your identity forever. There's no name registry; the address is both identity and proof of ownership.

NEAR inverts this. An account is a name, registered on the blockchain itself. `alice.near` is the account. That name gets stored in the global registry, and only the owner of `alice.near` can authorize transactions from it. The name is mnemonic—easier to remember, share, and verify than a 40-character hex string.

Names are competitive. Like domain names, the first to register `bob.near` owns it. NEAR allows names of 2+ characters. Names ending in `.near` are reserved and managed by the protocol; you can also create sub-accounts under your own account (e.g., `bob` can create `trading.bob` or `vault.bob`), and only `bob` controls those sub-account names.

## The access-key system

Instead of a single private key per account, NEAR accounts can hold multiple access keys. Each key has specific permissions. This is a major departure from Ethereum's model, where one private key signs all transactions.

**Full-access keys** sign any transaction the account owner authorizes. You use these when you need unrestricted control—moving funds, deploying contracts, or altering the account.

**Function-call restricted keys** can only invoke specific smart contracts or specific functions within contracts. For example, you might create a function-call key that can call the `swap()` function on a decentralized exchange but cannot access your vault contract. If that key is compromised, an attacker can't drain your funds; they can only execute the functions you've whitelisted.

This is valuable for security. Instead of carrying around a single master key, a user can:
- Keep a full-access key in cold storage
- Use a function-call key on their phone for day-to-day transactions
- Hand a single-use or short-lived function-call key to an app they don't fully trust
- Rotate keys without changing their account name

## Sub-accounts and hierarchical control

NEAR allows account owners to create sub-accounts. If you own `alice.near`, you can create `wallet.alice.near` or `trading.alice.near`, and each sub-account is its own entity with its own keys and state.

This is useful for:
- **Segregated wallets**: A user might keep savings in `vault.alice.near` and a spending wallet in `wallet.alice.near`.
- **Delegated authority**: A custodian holding `trading.alice.near` can execute trades without holding the master `alice.near` account.
- **App isolation**: A game might create `gaming.alice.near` so that if the game is hacked, only the gaming account—not the main account—is at risk.

Sub-accounts inherit the parent account's recovery capabilities in some cases (depending on implementation), but they are separate accounts for the purposes of state and smart-contract execution.

## Contrast with Ethereum

Ethereum's model is simpler and more atomic: one private key, one derived public key, one address. You control your account with that key and nothing else. There's no name registry; addresses are deterministic math.

NEAR's model is more complex but more flexible:
- Names are registered on-chain, requiring a slight overhead.
- Multiple keys per account add state management and UI complexity.
- Sub-accounts introduce hierarchical namespacing, which is powerful but adds cognitive load.

For new blockchain users, NEAR's human-readable names are friendlier. Telling someone to send funds to `alice.near` is clearer than asking them to copy-paste a 42-character hex address and pray they get it right. But for developers and power users comfortable with cryptography, Ethereum's directness is elegant.

## Key rotation and recovery

NEAR's multi-key design enables smoother key management. If a function-call key is compromised, you can revoke it without touching your full-access key. If you lose your phone, you can replace the phone's key by signing with your computer's key.

Ethereum accounts can't rotate keys at the account level; the account *is* the key. You can move funds to a new address, but the old address still exists, and you have to manage migrations yourself.

Some NEAR applications build recovery mechanisms on top of the account model. For instance, a user might designate a backup key or a trusted friend's public key, and if the main key is lost, a recovery contract can restore access. This is possible because accounts are named and keys are explicit; it's harder in Ethereum's address-as-key model.

## Smart contracts and state

NEAR's account model doesn't change how smart contracts work fundamentally—they still execute in a virtual machine and modify state. But the named-account system means contracts can reason about human-friendly identifiers and make access-control decisions based on key type (full-access vs. function-call).

A contract might check: "Is this function being called by a full-access key?" If so, unrestricted. "Is it a function-call key?" Then restrict to whitelisted operations. This enables fine-grained permission models that Ethereum must implement manually via code logic.

## Adoption and ecosystem impact

NEAR's account model has made onboarding smoother for non-technical users. Wallets on NEAR can offer better UX because they can handle account recovery and multi-device access more elegantly than pure Ethereum wallets.

However, it introduces a naming bottleneck. In Ethereum, account creation is instant and free (you just generate a keypair). In NEAR, you must register a name on-chain, which costs tokens and adds latency. This keeps accounts from being throwaway; it encourages users to maintain fewer, more intentional accounts.

The model also changes how decentralized finance (DeFi) works. Protocols must account for the possibility of function-call keys with restricted permissions, which can enable novel contract designs but also complicates key recovery and account delegation logic.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof of Stake](/proof-of-stake/) — NEAR's consensus mechanism
- [Smart Contract](/smart-contract/) — code execution on NEAR
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where NEAR tokens trade
- [Distributed Ledger](/distributed-ledger/) — the underlying technology
- [Private Placement](/private-placement/) — how NEAR tokens were distributed early on

### Wider context

- [Blockchain Fundamentals](/blockchain-fundamentals/) — the broader context for account design
- [Ethereum](/ethereum/) — alternative account model for comparison
- [Bitcoin](/bitcoin/) — simpler address scheme

</div>
