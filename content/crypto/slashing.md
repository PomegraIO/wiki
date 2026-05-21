---
title: "Slashing"
description: "Slashing is a penalty mechanism in proof-of-stake blockchains where validators lose part or all of their staked collateral for misbehaviour. It is the enforcement mechanism that makes proof-of-stake secure."
keywords:
  - slashing
  - proof-of-stake
  - validator penalty
  - misbehaviour
  - collateral loss
  - consensus enforcement
image: "/svg/crypto.svg"
---

*A **slashing** is a penalty in [proof-of-stake](/proof-of-stake/) blockchains where a [validator](/validator/) loses part or all of their staked collateral for violating protocol rules. Slashing is the enforcement mechanism that keeps validators honest, making attacks economically irrational.*

<div class="wiki-hatnote">

This entry covers slashing as a mechanism. For the staking process, see [staking](/staking/); for validators, see [validator](/validator/); for proof-of-stake consensus, see [proof-of-stake](/proof-of-stake/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Slashing — key facts</div>

<img src="/svg/crypto.svg" alt="Validator collateral being slashed" />

<div class="wiki-infobox-caption">Slashing: automatic penalties for protocol violations.</div>

|   |   |
|---|---|
| **Trigger** | Validator misbehaviour (double-signing, equivocation, etc.) |
| **Enforcement** | Automatic (protocol-enforced) |
| **Penalty** | 1–100% of staked collateral |
| **Irreversible** | Yes (cannot be undone) |
| **Examples of violations** | Double-signing, voting for conflicting chains |
| **Networks** | [Ethereum](/ethereum/), [Cardano](/cardano/), [Polkadot](/polkadot/) |
| **Purpose** | Make attacks economically irrational |

</aside>

## Slashable offences

Validators can be slashed for:

1. **Proposing two conflicting blocks.** A validator cannot propose two different blocks at the same height/slot.
2. **Equivocation (double-voting).** A validator cannot vote for two different chains at the same time.
3. **Inactivity (on some networks).** Failing to participate when selected can result in minor penalties.

The specific slashable offences vary by network. [Ethereum](/ethereum/) slashes for double-signing and surrounding votes; [Cardano](/cardano/) slashes for double-signing.

## Penalty amounts

Penalties vary by severity:

- **Inactivity penalties.** ~1% of annual rewards per epoch (minor).
- **Minor slashing.** 1–10% of stake for voting violations.
- **Major slashing.** 50–100% for double-signing.

On [Ethereum](/ethereum/), double-signing can result in ~33% penalty initially, with additional penalties if multiple validators are slashed simultaneously.

## Economic security

Slashing makes attacks economically irrational. If a validator controls 1% of stake (~$40 million on [Ethereum](/ethereum/) in 2024) and double-signs:

- They lose 50%+ of their stake (~$20 million).
- They gain... nothing (the attack fails because other validators reject the invalid block).

This asymmetry — large penalty for small/no gain — makes attacks irrational.

## Criticism: the "nothing at stake" problem

Some early critics of proof-of-stake worried about the "nothing at stake" problem: if validators can vote for multiple chains with no cost, what prevents consensus failure?

The answer is slashing. Unlike [proof-of-work](/proof-of-work/), where you consume electricity for the chain you mine (the "stake" is extrinsic), in [proof-of-stake](/proof-of-stake/) you literally lose money for bad behaviour (the "stake" is intrinsic).

## Automatic enforcement

Slashing is automatic and enforced by the protocol. If a validator double-signs, the network automatically detects it, includes proof in a block, and executes the slash without human intervention.

This is crucial: slashing cannot be forgiven, reversed, or avoided. A validator cannot sue to get their money back.

## Withdrawal delays and exit queue

When a validator is slashed, they are immediately removed from the active validator set. However, they cannot immediately withdraw their remaining stake. On [Ethereum](/ethereum/):

- Slashed validators enter an exit queue.
- They wait ~27 hours to fully exit.
- Their remaining stake is returned.

This delay allows the network to detect and respond to attacks before exits complete.

## Collective slashing

On some networks, if many validators are slashed simultaneously (indicating a coordinated attack), additional penalties apply. On [Ethereum](/ethereum/), the slashing penalty increases if multiple validators are slashed in the same period, making coordinated attacks more expensive.

## Edge cases and implementation risks

Slashing is enforced by code, and code can have bugs. A slashing bug could accidentally penalise honest validators or fail to penalise dishonest ones.

For example, in early [Ethereum](/ethereum/) testing, a bug in the slashing code was discovered and fixed before mainnet. Any such bug could undermine security.

## Restaking and secondary slashing

Advanced protocols like Eigenlayer introduce **restaking** — staking your already-staked ETH to secure multiple networks. This can introduce additional slashing risks: if you restake on a compromised application, you could be slashed on that application and lose your original ETH.

## Incentive compatibility

For slashing to work, it must be **incentive-compatible** — rational validators must prefer honest participation over attacks. This requires:

1. **Slashing penalty > expected gain from attack.** The penalty must exceed what an attacker could gain.
2. **Fast detection.** Attacks must be detected quickly, before an attacker can extract value.
3. **Credible threat.** Validators must believe slashing will actually occur.

All three conditions must hold for slashing to provide security.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-stake](/proof-of-stake/) — the consensus mechanism
- [Validator](/validator/) — who can be slashed
- [Staking](/staking/) — what is at risk
- [Ethereum](/ethereum/) — implements slashing
- [Restaking](/restaking/) — advanced slashing risks

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- [Proof-of-work](/proof-of-work/) — alternative security model (no slashing)
- 51% attack — what slashing prevents

</div>
