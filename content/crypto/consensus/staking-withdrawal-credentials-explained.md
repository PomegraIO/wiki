---
title: "Staking Withdrawal Credentials Explained"
description: "Withdrawal credentials are the two data formats that tell Ethereum where staked ETH goes when withdrawn: BLS to a new validator, or 0x01 execution-layer address."
keywords:
  - staking withdrawal credentials explained
  - eth withdrawal credentials types
  - bls withdrawal credentials
  - execution address withdrawal
  - validator stake withdrawal
  - ethereum staking setup
---

*A **staking withdrawal credential** is the on-chain directive that tells the Ethereum consensus layer where to send staked ETH (or validator rewards) when the validator exits or is penalized. There are two formats: **BLS credentials**, which route rewards to a new validator account, and **0x01 execution-layer credentials**, which withdraw directly to an Ethereum address. The type is immutable once set; choosing the wrong format delays or prevents stake access.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Staking Withdrawal Credentials — Formats and Withdrawal Rules</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for blockchain consensus." />

<div class="wiki-infobox-caption">Withdrawal credentials define the release path for validator deposits and rewards.</div>

|   |   |
|---|---|
| **0x00 BLS credentials** | Points to another validator key; rewards compound in the validator's balance but stake cannot exit. Legacy format; rarely used now. |
| **0x01 execution credentials** | Points to an Ethereum address (like a wallet or smart contract); both rewards and full stake can be withdrawn to that address. |
| **Why immutable** | Changing credentials would require consensus-layer logic update; not possible for running validators. |
| **Setting the credential** | Done once, at deposit time, in the deposit contract transaction. Later automated conversion from 0x00 to 0x01 is possible but requires a separate contract call. |
| **Staked amount lockup** | With 0x00 BLS, stake is locked until converted. With 0x01, partial or full withdrawal happens automatically after 256 epochs (~27 hours). |
| **Rewards destination** | 0x00: stay in validator balance, earning compounding interest (only if validator stays active). 0x01: paid to the execution address, available immediately. |

</aside>

## The Two Credential Formats

When a validator deposits 32 ETH to the Ethereum deposit contract, the deposit includes a "withdrawal credential"—32 bytes of data that the consensus layer stores and checks every time that validator has a balance event (exit, penalty, or reward accrual).

### 0x00: BLS Withdrawal Credentials

The **0x00 format** points to a BLS public key (used in the consensus layer for signing blocks). This was the original design. When a validator with 0x00 credentials exits or is slashed, the consensus layer cannot move the ETH anywhere; the stake sits in the validator's balance, growing if rewards accrue or shrinking if penalties apply.

The stated intent was to allow stake compounding: a validator could earn rewards while the principal remained at the consensus layer, earning interest without reinvestment friction. However, 0x00 credentials have a critical flaw: **there is no automated way to withdraw the stake.** The validator can signal intent to exit, and the balance will eventually be withdrawn to... nowhere, unless the credential is upgraded.

### 0x01: Execution-Layer Withdrawal Credentials

The **0x01 format** (introduced as part of the Shapella upgrade in April 2023) specifies an Ethereum execution-layer address—a regular wallet address or smart contract. This unlocked the ability to actually withdraw stake.

With 0x01 credentials:
- **Partial withdrawals** happen automatically: validator rewards above 32 ETH are swept to the execution address every few epochs.
- **Full withdrawals** occur when the validator exits the active set; the entire remaining balance goes to the specified address.
- **Timing**: Withdrawals process within ~27 hours (256 epochs) after the request.

This format is the practical standard for new validators. It means you can choose any Ethereum address—a cold wallet, a hardware wallet, a smart contract—and stake will eventually arrive there.

## Setting Withdrawal Credentials at Deposit

The withdrawal credential is specified **once, when the 32 ETH is deposited to the deposit contract.** The deposit transaction includes the credential in its encoded parameters. Once set, it cannot be changed for that validator.

Most staking tools (Lido, Rocket Pool, solo-staking launchers like Stereum) default to 0x01 and ask you to provide the execution address. You paste in your address, the tool encodes it into the credential, and it stays locked to that address for the life of the validator.

If you accidentally set 0x00, or you used an older staking UI before 0x01 was standard, your stake is not lost—but you cannot withdraw it until you **convert the credential.** Conversion requires submitting a signed message from the BLS key to an on-chain contract, proving you control the original key. After conversion, 0x01 withdrawals start flowing.

## Why Withdrawal Credentials Matter for Stake Access

The seemingly technical detail of credential format determines when you can touch your stake.

**0x00 validators are stuck.** Even if the validator has earned rewards or accumulated a balance, there is no on-chain mechanism for the consensus layer to send that ETH anywhere. The balance sits frozen. A validator with 0x00 can exit the validator set (signaling with their signing key), and the balance will accrue or lose value, but never leave. Conversion to 0x01 is the only escape, and it requires the original BLS key.

**0x01 validators flow naturally.** Exit the validator, and within 27 hours, the balance flows to your specified address. No extra steps, no signing, no maintenance. Rewards above 32 ETH leave automatically; full principal follows after exit.

This difference is why the industry moved so decisively to 0x01 after Shapella. A validator cannot use staking as a true product (with custodians, liquid staking tokens, or withdrawal streams) unless stake can actually exit.

## Execution Address Options and Smart Contracts

The execution address in a 0x01 credential can be:
- **An EOA (externally owned account)**: A wallet you control with a private key. Simplest and most common.
- **A smart contract**: Funds could go to a withdrawal contract that distributes them, applies taxes, or triggers other logic. Advanced users sometimes do this for operational flexibility.

Note: The address itself has no say in accepting the withdrawal. Withdrawals are forced—the consensus layer credits the address regardless of whether it is a contract and whether that contract has code to handle the funds. If you point to a contract that cannot receive ETH (a contract with no payable fallback), the withdrawal will fail at the execution layer, and the validator will be stuck with the balance forever. This is rare and requires deliberate error, but it is possible.

## Credential Format and Validator Liquidity Products

[Liquid staking pools](/liquid-staking-token/) and custodians rely entirely on 0x01 credentials. A liquid staking service like Lido accepts your 32 ETH, gives you a token (stETH) representing a claim, and runs validators on your behalf. The validators have 0x01 credentials pointing to the Lido smart contract, which collects rewards and batches full withdrawals back to stakers.

Without 0x01, this model would not work: the service could earn rewards, but they would be trapped in the consensus layer.

## See also

<div class="wiki-seealso">

### Closely related

- [Validator](/validator/) — The entity that deposits stake and sets credentials.
- [Proof of Stake](/proof-of-stake/) — The consensus mechanism that requires withdrawal credentials.
- [Smart Contract](/smart-contract/) — Can be the target of execution-layer withdrawal credentials.
- [Ethereum](/ethereum/) — The blockchain that uses withdrawal credentials in its validator system.
- [Liquid Staking Token](/liquid-staking-token/) — Depends on 0x01 credentials to enable withdrawal flows.

### Wider context

- Cryptocurrency Custody — Custody of withdrawal addresses is critical to stake access.
- [Distributed Ledger](/distributed-ledger/) — Broader blockchain withdrawal and credential concepts.
- Consensus Mechanisms — Types of consensus that use similar stake-locking rules.

</div>
