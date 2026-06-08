---
title: "Rebasing Token"
description: "Tokens that algorithmically adjust supply and every holder's balance to maintain a target price peg through periodic positive or negative rebases."
keywords:
  - rebasing
  - token supply
  - cryptocurrency
  - price peg
  - algorithmic stablecoin
  - elastic supply
image: "/svg/crypto.svg"
---

*A **rebasing token** automatically adjusts the total supply and proportionally increases or decreases every holder's balance—a mechanism designed to keep price pinned to a target level. Rather than burning or minting coins, rebasing directly shrinks or expands each wallet, creating the most direct path to price stability, though the approach has proven fragile in practice.*

<div class="wiki-hatnote">

For cryptocurrency price stability via collateral or algorithmic mechanisms, see [stablecoin](/stablecoin/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rebasing Token — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract mark representing digital assets and token mechanisms." />

<div class="wiki-infobox-caption">Tokens that adjust each holder's balance algorithmically to keep price on peg.</div>

|   |   |
|---|---|
| **What it is** | A token contract that periodicially resets every wallet's balance to move price toward a target |
| **How it works** | If price is above peg, supply expands (positive rebase); if below, contracts (negative rebase) |
| **Rebase frequency** | Typically daily or every 8 hours, driven by price feeds or oracle data |
| **Effect on value** | Each rebase changes your balance, though your proportional ownership stays the same |
| **Notable examples** | AMPL (Ampleforth), TIME, FORTH |
| **Key risk** | Death spirals when rebase feedback amplifies price decline rather than stabilizing |

</aside>

## How rebasing maintains the peg

A [stablecoin](/stablecoin/) aims to hold a target price—typically $1 USD—so it can function as currency. Collateral-backed coins like USDC hold reserves; algorithmic designs use clever incentives. Rebasing tokens take a third path: they treat the supply itself as the adjustment variable.

Suppose a rebasing token targets $1. If the market price rises to $1.20, the contract automatically expands the supply by 20%, giving every holder 20% more tokens. Your one thousand coins become twelve hundred coins, but so does everyone else's—proportional ownership stays unchanged. The new supply chases demand downward, pushing price back toward $1.

If price falls to $0.80, the contract contracts supply, cutting every holder's balance by 20%. You now hold eight hundred coins. Fewer coins, less total supply, less selling pressure—theoretically price climbs back to $1.

The mechanism is mathematically elegant: it breaks the zero-sum tension between new printing and existing holder dilution. When price rises, everyone gets richer (more tokens), so expansion feels fair. When price falls, everyone shares the pain equally (fewer tokens), creating shared sacrifice rather than selective loss.

## The information problem and oracle risk

For rebasing to work, the contract needs a reliable price signal. Most rebase tokens rely on oracles—external data feeds that report the current market price on [cryptocurrency exchanges](/cryptocurrency-exchange/). The contract watches the oracle, compares price to the target, and executes a rebase if price drifts more than a threshold (the "band").

But oracles are vulnerable. If the oracle is manipulated, attacked, or delayed, the rebase can be triggered at the wrong time, or worse, not triggered when needed. A flash loan attack or trading bot can artificially spike price, trigger an unwanted positive rebase, and crash the token afterward. Conversely, if the oracle lags and price plummets in real time, the rebase might be too slow to help.

This is not a minor edge case. Early rebasing tokens suffered repeated oracle failures and price peg breaks. The more decentralized and permissionless the oracle, the more vulnerable; the more centralized and controlled, the less the token appeals to pure [blockchain](/blockchain-fundamentals/) principles.

## The feedback trap: death spirals

Rebasing tokens face a unique feedback loop that can spiral to zero. If price begins to drift below the peg, the contract executes a negative rebase—shrinking everyone's balance. But the shrink itself can trigger panic: "My balance got cut; maybe this is failing." Holders sell, price falls further, another negative rebase triggers, more panic, more selling.

This is a "death spiral." Each rebase is supposed to encourage buying (if you shrink supply, scarcity rises and price should follow); instead, shrinking balances create the opposite psychological effect—fear of further cuts. The feedback becomes vicious rather than corrective.

This dynamic hit several rebasing tokens hard. AMPL, the most famous rebase experiment, suffered multiple downward spirals in which negative rebases accelerated losses rather than stopping them. Rebase tokens with locked or staked positions (Time) tried to soften the blow by cushioning holder pain, but that reduced the mechanism's incentive punch.

## Rebasing versus minting and burning

Other stablecoins use traditional minting and burning: create new coins to support price, destroy coins to reduce supply. Rebasing sounds simpler—no new coins enter the market separately, no separate burning wallets—but it's not obviously better.

In fact, minting and burning can be less disruptive. They change total supply without touching every wallet. A rebasing system that cuts your balance by 20% creates immediate distress, even if your proportional ownership is preserved. The psychological and operational friction is higher: exchanges have to suspend trading during rebases, wallet software breaks, contract integrations fail.

Minting, by contrast, is invisible to most users. New supply enters circulation, but it doesn't reach into every user's pocket and shrink their holdings.

## Why rebasing persists despite fragility

Several reasons keep rebasing tokens alive in smaller pockets of the ecosystem. First, they're intellectually compelling—the elegance appeals to pure mechanism designers. Second, they sidestep debates about who gets new supply (in minting-based systems, early holders or protocol treasuries often capture new inflation). Rebasing feels more egalitarian, even if the outcome is the same: everyone bears the cost equally.

Third, rebasing enabled some tokens to avoid traditional stablecoin regulation. If your token isn't a "stablecoin" per se but rather an "elastic supply" asset, regulators paid less attention—at least initially. That regulatory gray zone has narrowed considerably.

## Rebasing in practice today

AMPL (Ampleforth) remains the most active rebasing experiment, now focusing on use cases where volatility matters less—backing other stablecoins or protocols rather than being used directly as currency. TIME tokens used rebasing combined with staking to create a rebase-on-stake mechanic, where locked holders earn extra rebase rewards.

Both have survived longer than casual observers expected, but neither has achieved the sustained price stability and widespread adoption that collateral-backed coins like USDC have earned. Rebasing remains a niche mechanism.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquid staking token](/liquid-staking-token/) — derivative tokens enabling staking rewards with transferability
- [Stablecoin](/stablecoin/) — tokens targeting a fixed price, via collateral or algorithm
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — platforms where token prices are discovered and traded
- [Blockchain fundamentals](/blockchain-fundamentals/) — distributed ledger systems underlying tokens
- Token — digital assets on a blockchain
- Oracle — data feeds supplying off-chain information to smart contracts

### Wider context

- [Distributed ledger](/distributed-ledger/) — decentralized record-keeping systems
- [Proof of work](/proof-of-work/) — mining-based consensus mechanism
- [Proof of stake](/proof-of-stake/) — staking-based consensus mechanism
- [Initial public offering](/initial-public-offering/) — comparing token launches to traditional equity sales
- Volatility — price swings and their measurement

</div>
