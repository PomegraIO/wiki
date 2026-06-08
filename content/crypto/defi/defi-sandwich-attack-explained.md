---
title: "Sandwich Attacks in DeFi Explained"
description: "How sandwich attacks in DeFi work: bots front-run and back-run user swaps to extract value. Learn how slippage settings reduce exposure."
keywords:
  - sandwich attack defi
  - mev front running
  - slippage protection
  - mempool monitoring
  - flash bot swaps
image: /svg/crypto.svg
---

*A **sandwich attack** in DeFi is a form of theft where a bot monitors a user's pending swap in the mempool, places its own transaction before and after the target transaction, and captures the price movement as profit. The attacker buys the same token before the user's large swap pushes the price up, then sells after the price spike—pocketing the difference while the user receives fewer tokens than expected. Slippage tolerances and private transaction pools are the primary defenses.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sandwich Attacks — how they work</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Bots exploit mempool visibility and transaction ordering to extract value from user swaps.</div>

|   |   |
|---|---|
| **What it is** | Front-running and back-running a user transaction to profit from price movement |
| **Who profits** | Attacker; loss borne by the victim trader |
| **Primary vector** | Public mempool; readable pending transactions |
| **Main defense** | Slippage tolerance; private relays; MEV-resistant pools |
| **Cost to victim** | 0.5–5% of swap value typical; can exceed 20% in volatile conditions |

</aside>

## How a sandwich attack unfolds

The mechanics are straightforward. A user prepares a large [swap](/stock-exchange/) on a decentralized exchange (DEX) and broadcasts it to the [blockchain](/blockchain-fundamentals/). Before the transaction is included in a block, it sits in the **mempool**—a public holding area where every node on the network can see it.

An automated bot—often called a "searcher"—monitors the mempool in real time. When it spots a profitable pending transaction (e.g., a user trading 100 ETH for stablecoin), it calculates the impact: that volume will drive the ETH price higher on the DEX's automated market maker. The bot then:

1. Places its own transaction *before* the user's swap, buying ETH at the lower pre-impact price.
2. Lets the user's large order execute, which pushes the ETH price up.
3. Places a second transaction *after* the user's swap, selling its newly purchased ETH at the inflated price.

The attacker exits with a profit; the user receives fewer stablecoin than if there had been no interference. The loss is typically the difference between the expected price and the actual filled price—hidden in slippage and paid directly to the attacker instead of to a liquidity pool.

## Why mempool visibility enables attacks

Public blockchains publish transactions before they finalize. On Ethereum, this transparency is intentional and necessary for decentralization—every node must know what is pending. But the same property that makes the network secure makes it readable to sophisticated observers. Searchers run full nodes and see pending transactions the instant they arrive.

Attackers also pay higher gas fees to jump ahead of the user's transaction, or use custom block-building arrangements with validators to guarantee ordering. When validators produce blocks, they can order transactions—a power called MEV (Maximal Extractable Value)—and sophisticated bots bid heavily for favorable orderings.

In practice, this means front-running is not random or rare. On high-volume DEXs, sandwich attacks happen thousands of times daily, extracting billions in value from retail and institutional traders alike.

## Slippage tolerance and its limits

The primary user-side defense is a **slippage tolerance**: a percentage limit set on the user's wallet or DEX interface. If the swap price drifts beyond that tolerance, the transaction fails and the user loses only gas fees.

For example, if you set slippage to 0.5% and submit a swap, the DEX calculates the current market price. If the actual fill price is worse than market price + 0.5%, the transaction reverts. Sandwich attackers must push prices hard enough to exceed your tolerance to succeed.

However, slippage tolerance is not a perfect shield:

- **It does not prevent loss**; it only prevents *worse* loss. A 0.5% tolerance still allows 0.5% extraction per swap.
- **Tight tolerances cause failures**. If you set 0.1% on a volatile pair, legitimate price movement may revert your trade, and you resubmit, wasting gas.
- **Large orders are always visible**. Even with protection, a multi-million dollar swap cannot hide its impact; an attacker knows roughly what price movement to expect and can estimate profit.

Slippage tolerance is better understood as a circuit breaker than a solution.

## Private transaction pools and batch auctions

The second layer of defense is privacy. **Private relays** like MEV-Protect and [Flashbots](/cryptocurrency-exchange/) Protect let users send transactions directly to builders or special pools instead of broadcasting to the public mempool. The trade-off is centralization: the relay operator knows your transaction, and you must trust they do not front-run you themselves.

**Batch auctions** take a different approach. Protocols like MEV-Burn and Intent-based MEV protocols collect transactions over short intervals, randomly order them, and execute all at the same price. If everyone in a batch trades at the same spot price (the opening price, or a randomized selection), no one trades against a price moved by another user in the batch. Sandwich attacks become unprofitable.

These defenses exist on newer chains and protocols but have not yet matured into reliable, widespread protections across Ethereum's largest DEXs.

## Why sandwich attacks persist

Even with defenses, sandwich attacks remain common because:

1. **The profit bar is low**. Extracting 0.5% from a $100,000 swap—$500—is easy money for a bot that runs thousands of times daily.
2. **Defenses are fragmented**. Most users do not use private relays; most DEXs do not employ batch auctions. A single [swap](/stock-exchange/) on Uniswap v3 is still exposed.
3. **Attacker competition is fierce**. Multiple bots scan the mempool simultaneously. Even if one attack fails, another succeeds, and the market for MEV extraction is efficient.
4. **Validator incentives align with attacks**. Validators earn MEV rewards, creating little pressure to block or hide front-running.

A user making a single large swap today should expect to lose 0.2–2% to sandwich attacks and general slippage, depending on the pair and time of day.

## Broader systemic impact

Sandwich attacks are a form of information asymmetry theft. They do not create value; they extract it from participants who move prices. This drag on retail trading increases costs and discourages entry into DeFi. Institutional traders, who can afford private relays or split their orders into smaller pieces, face lower friction—a cost borne by smaller players.

The attacks also highlight a deeper problem: [blockchain](/blockchain-fundamentals/) transparency, while essential for security, enables predatory behavior that centralized exchanges prevent through order batching and private order books. DeFi trades that should occur at a fair price instead occur at a front-run price, with value leaking to searchers rather than to the protocol or liquidity providers.

## See also

<div class="wiki-seealso">

### Closely related

- [Slippage protection in trading](/bid-ask-spread/) — how price impact and slippage tolerance work
- [MEV in DeFi](/cryptocurrency-exchange/) — maximal extractable value and miner/searcher incentives
- [Batch auctions and Intent-based swaps](/defi-lending-interest-rate-model/) — mechanisms that reduce sandwich vulnerability
- [Mempool and transaction ordering](/blockchain-fundamentals/) — why pending transactions are visible
- [Flash loans and smart contract risks](/defi-lending-interest-rate-model/) — related DeFi security concepts

### Wider context

- [Decentralized exchanges](/stock-exchange/) — how DEXs differ from order books
- [Automated market makers](/cryptocurrency-exchange/) — the liquidity model that sandwich attacks exploit
- [Cryptocurrency volatility](/currency-volatility/) — why large swaps cause price slippage
- [Blockchain security and cryptography](/blockchain-fundamentals/) — foundations of decentralized systems

</div>
