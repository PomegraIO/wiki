---
title: "Delegated Proof-of-Stake"
description: "Delegated proof-of-stake is a consensus mechanism where token holders vote for a small number of delegates who validate blocks. This reduces the number of validators while allowing all token holders to participate in governance."
keywords:
  - delegated proof-of-stake
  - dpos
  - validator
  - governance
  - delegation
  - voting
image: "/svg/crypto.svg"
---

*A **delegated proof-of-stake** (**DPoS**) is a consensus mechanism where token holders vote for a small number of delegates (typically 21–101) who validate blocks on their behalf. This allows high throughput and low energy use while giving all token holders a voice in governance through voting.*

<div class="wiki-hatnote">

This entry covers delegated proof-of-stake as a mechanism. For standard proof-of-stake, see [proof-of-stake](/proof-of-stake/); for proof-of-authority, see [proof-of-authority](/proof-of-authority/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Delegated Proof-of-Stake — key characteristics</div>

<img src="/svg/crypto.svg" alt="Token holders voting for delegates" />

<div class="wiki-infobox-caption">Delegated proof-of-stake: governance through voting for delegates.</div>

|   |   |
|---|---|
| **How it works** | Token holders vote for delegates; delegates validate blocks |
| **Who validates** | A small number of elected delegates |
| **Who has power** | All token holders, through voting |
| **Decentralisation** | Moderate (few validators, many voters) |
| **Energy cost** | Very low |
| **Speed** | Fast (delegates can reach consensus quickly) |
| **Governance** | On-chain voting by token holders |
| **Used by** | EOS, TRON, Cosmos (partial), Polkadot (variant) |

</aside>

## Mechanism

In delegated proof-of-stake, token holders vote for delegates. Each vote is weighted by the holder's token balance — owning 1% of tokens gives 1% of voting power.

Delegates with the most votes become validators. They validate transactions, produce blocks, and earn rewards. If a delegate misbehaves or is replaced in the next election cycle, they lose their position.

Election cycles vary by network:

- **EOS** — top 21 delegates validate; elections are continuous (every 30 seconds, the set can change).
- **TRON** — top 27 delegates (called super-representatives).
- **Cosmos** — top 125 validators.

## Advantages over standard proof-of-stake

**Scalability.** Fewer validators means faster consensus. Instead of thousands of validators reaching agreement (slow), dozens of delegates coordinate (fast).

**Accessibility.** Token holders without the technical skill or resources to run a validator can still participate through voting.

**Governance.** Voting is explicit and on-chain. Major governance changes require a vote.

**Energy efficiency.** Very few validators means minimal computational overhead.

## The delegation problem

A core challenge is ensuring delegates actually represent token holders' interests. In theory, a delegate can be voted out; in practice, voter apathy is common.

In many DPoS systems, a small number of token holders control most voting power, meaning a few entities effectively choose delegates. This defeats the purpose of decentralisation.

Additionally, delegates have incentives to centralise: a single delegate operator can run multiple delegates and capture a larger share of rewards. Some networks implement rules to prevent this (e.g., voting for closely related addresses is penalised).

## Comparison with proof-of-stake

| Aspect | Proof-of-Stake | Delegated Proof-of-Stake |
|--------|---|---|
| **Number of validators** | Thousands | Dozens to hundreds |
| **Speed** | Moderate | Fast |
| **Energy** | Very low | Very low |
| **Accessibility** | Requires staking | Only requires voting |
| **Governance** | Limited (protocol-level) | Extensive (on-chain voting) |
| **Centralisation risk** | Moderate | Higher |

Standard proof-of-stake (like [Ethereum](/ethereum/)) has more validators, making it more decentralised but slower. DPoS is more efficient but more centralised.

## Criticism

Critics argue that DPoS is plutocratic — wealth determines voting power. A billionaire can buy 51% of tokens and control the network indefinitely.

Others point out that voter apathy in DPoS is severe; often, fewer than 50% of tokens are actively voted. This means a small coalition can control delegates.

Proponents counter that all blockchains involve some degree of plutocracy (wealth buys mining power or staking power) and that DPoS's explicit voting at least makes power dynamics transparent.

## Examples

**EOS** — uses continuous voting for 21 delegates. EOS has experienced controversies where delegates coordinated to vote for each other, reducing meaningful competition.

**TRON** — 27 super-representatives are voted on by token holders; highly concentrated with a few entities controlling most validators.

**Cosmos** — uses a variant where validators are selected from a large pool of candidates based on voting, not limited to a fixed set.

## Variants

Some networks use **liquid delegated proof-of-stake**, where token holders can delegate voting power to others without locking tokens. This increases accessibility but introduces new attack vectors.

Others use **quadratic voting**, where voting power is the square root of token holdings. This attempts to reduce the influence of wealth, though it has other trade-offs.

## See also

<div class="wiki-seealso">

### Closely related

- [Proof-of-stake](/proof-of-stake/) — the parent mechanism
- [Validator](/validator/) — delegates who validate
- Governance token — used for voting in DPoS
- [Proof-of-authority](/proof-of-authority/) — another variant

### Wider context

- [Blockchain fundamentals](/blockchain-fundamentals/) — the underlying technology
- [Staking](/staking/) — earning rewards through delegation
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — where governance tokens trade

</div>
