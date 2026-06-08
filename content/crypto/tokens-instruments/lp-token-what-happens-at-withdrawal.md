---
title: "LP Token: What Happens When You Withdraw Liquidity"
description: "When you withdraw liquidity and redeem LP tokens, the protocol calculates your share of the pool and returns the underlying assets. Fee settlement and share dilution affect returns."
keywords:
  - lp token withdrawal
  - liquidity provider tokens
  - dex redemption mechanics
  - impermanent loss
  - pool share calculation
image: /svg/crypto.svg
---

*When a liquidity provider withdraws assets from a decentralized exchange pool and redeems their **LP tokens**, the protocol calculates their ownership share of the pool, returns the proportional underlying assets, and settles any accrued fees. The amount you receive reflects both gains from trading fees and losses from price movement since deposit—what many call impermanent loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">LP Token Withdrawal — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for crypto." />

<div class="wiki-infobox-caption">Redeeming an LP token converts it back to the underlying pool assets.</div>

|   |   |
|---|---|
| **What you redeem** | LP token (proof of pool ownership) |
| **What you receive** | Both assets from the pool in proportion to your share |
| **Share calculation** | (Your LP tokens / Total LP tokens) × Pool reserves |
| **Fee settlement** | Accumulated trading fees added to pool; you receive your share |
| **Timing** | Immediate (on-chain, no settlement lag) |
| **Price impact** | Large withdrawals may trigger slippage; protocol rebalances |
| **Comparison** | [Mutual fund redemption](/mutual-fund/) mechanics (similar concept) |

</aside>

<div class="wiki-hatnote">

This article assumes familiarity with liquidity pools and LP tokens. For an introduction, see the articles on [liquidity provider tokens](/smart-contract/) and decentralized exchanges.

</div>

## The deposit-withdrawal cycle

To understand withdrawal, first recall the deposit. When you provide liquidity to a pool—say, Ethereum and USDC on Uniswap—you deposit equal value of both assets. The protocol issues you LP tokens (proof of ownership), representing your share of that pool's reserves.

While your liquidity sits in the pool, traders swap assets through it, paying a small fee (typically 0.01–0.3%, depending on the pool tier). Those fees accumulate and are added back into the pool reserves, growing the reserve total.

Your LP tokens stay static in count, but their value increases because the pool reserves grew. When you exit, you redeem those tokens and receive both assets back at their current pool prices.

## How the protocol calculates your share

The redemption formula is straightforward:

**Your share = (Your LP tokens / Total LP tokens in circulation) × Each asset in the pool**

For example, suppose a Uniswap ETH/USDC pool has:

- 1,000 ETH and 2,000,000 USDC in reserves
- 100,000 LP tokens in circulation
- You own 1,000 LP tokens (1% of the pool)

When you redeem your 1,000 tokens, you receive:
- (1,000 / 100,000) × 1,000 ETH = 10 ETH
- (1,000 / 100,000) × 2,000,000 USDC = 20,000 USDC

You get 10 ETH and 20,000 USDC. This maintains the 1,000 ETH to 2,000,000 USDC ratio (the pool's current ratio) and your 1% ownership of both assets.

The pool automatically calculates this; you don't negotiate or bid. You submit a transaction to burn (destroy) your LP tokens, and the protocol immediately transfers the assets to your wallet.

## Fee settlement at withdrawal

Fees are the main reason your withdrawal is worth more than your initial deposit (in the happy case).

Every swap through the pool incurs a fee—typically 0.01%, 0.05%, 0.3%, or 1%, depending on the pool's fee tier and the token pair. These fees are not withdrawn; instead, they are left in the pool, increasing the total reserves.

Because you own a share of the pool (represented by your LP tokens), you own a proportional share of those fees.

If the pool earned 100,000 USDC in fees while you held 1% of the pool, you own 1% of those fees (1,000 USDC). This is reflected in the pool's reserve total when you exit. The formula automatically includes these fees; no separate settlement step is needed.

Example with fees:

- Pool starts with 1,000 ETH and 2,000,000 USDC.
- 50 ETH in volume trades occur; 0.3% fee collected = 0.15 ETH worth ~300 USDC in fees.
- Fees sit in the pool. Reserves are now ~1,000.15 ETH and ~2,000,300 USDC.
- You redeem 1% and receive (1% × 1,000.15 ETH) and (1% × 2,000,300 USDC).
- Your share of fees = 0.0015 ETH + 3 USDC (1% of the accumulated 300 USDC-equivalent).

Your withdrawal includes those fees automatically.

## Impermanent loss and the price-movement penalty

Here's the catch: while you earn fees, you also suffer losses if the prices of the two assets diverge.

Suppose you deposit when ETH is $2,000 and USDC is $1 (1 ETH = 2,000 USDC). You deposit 10 ETH and 20,000 USDC (equal value, 1:2,000 ratio).

Three months later, ETH is $3,000. The pool's ratio adjusts. Arbitrage traders have removed ETH and added USDC, so the pool now holds more USDC and less ETH—perhaps 8 ETH and 30,000 USDC. Your 1% stake means:

- 0.08 ETH (lost 0.02 ETH)
- 300 USDC (up 100 USDC)

In dollar terms at current prices:
- 0.08 ETH × $3,000 = $240
- 300 USDC = $300
- Total = $540

But if you had not provided liquidity—if you'd simply held 10 ETH and 20,000 USDC separately—you'd have:
- 10 ETH × $3,000 = $30,000
- 20,000 USDC = $20,000
- Total = $50,000

By providing liquidity, you have only $540 instead of $50,000. This $49,460 difference is impermanent loss (IL). It arises because the pool forces you to maintain the 1:2,000 ratio by selling ETH at sub-market prices and buying USDC at sub-market prices. Arbitrage traders exploit this imbalance, and you pay for their profit.

**Impermanent loss is not a fee charged by the protocol; it's an opportunity cost.** You suffer it whenever the prices of the two assets diverge significantly. Fees offset it: if the pool earned enough trading fees, your net withdrawal might still beat a simple hold. But large price moves can overwhelm fee income.

## Slippage and execution risk

When you submit a withdrawal transaction, the blockchain processes it asynchronously. Between the time you sign and the time it executes, the pool reserves may change (other traders may have swapped). This can shift your received amounts slightly—slippage.

For large withdrawals (e.g., a whale removing 10% of the pool), slippage is material. You might specify a "minimum output" (e.g., "I want at least 10 ETH and 19,500 USDC, or revert the transaction"). If the pool has shifted so much that you'd receive less, the transaction fails, protecting you from a surprise loss.

Smaller withdrawals in deep pools often have negligible slippage (0.01–0.1%).

## Multi-asset pools and complex fee structures

Most examples use simple two-asset (pair) pools. But modern protocols support multi-asset pools (three or more assets). Balancer and Curve support many-asset pools. In these, your LP token still represents a share of all assets in the pool, and withdrawal still calculates your proportional share of each. The math scales; fees are distributed across all assets.

Some protocols also use tiered fee structures: in Uniswap v3, liquidity providers can concentrate their capital in a tight price range, earning higher fees but with more exposure to impermanent loss.

## Gas costs and transaction finality

On Ethereum, withdrawing liquidity costs gas fees (the transaction cost to settle the trade on-chain). On other blockchains, gas is cheaper but non-zero. This cost slightly reduces your net withdrawal.

Also, withdrawal is immediate and final. Unlike traditional finance, where redemptions might settle in T+2 (two days), a blockchain withdrawal is confirmed in minutes (sometimes seconds on fast chains). There is no settlement leg; the token is burned and assets are transferred in the same transaction.

## Common withdrawal scenarios

**Happy case: fees exceed impermanent loss**

A tight-spread pair like USDC/USDT has minimal price divergence. Fees accumulate while IL remains negligible. You withdraw profitably.

**Volatile pair: IL dominates fees**

A newly listed altcoin pair with high trading volume and wild price swings. Fees are good, but IL is severe. If the token rallies, you lose heavily; if it crashes, you still lose but differently. You may end up worse off than just holding the assets.

**Stable-pair: fees minus gas**

USDC/USDT, DAI/USDC pairs have almost no IL because the prices are pegged. Your profit is almost purely the fee income, minus gas costs. This is why stable-pair liquidity provisioning is low-risk but also low-return.

## Tax and accounting considerations

Withdrawing LP tokens is a taxable event in most jurisdictions. You realize a gain or loss equal to the difference between your withdrawal amount and your cost basis (the value of assets you initially deposited). Calculating your cost basis and gain/loss is complex: you must track the original deposit date, price, and fee accrual over time.

Many exchanges and blockchain tools (e.g., Etherscan, Zapper) provide transaction history, but proper tax accounting often requires specialized crypto tax software.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart-contract](/smart-contract/) — the code that governs LP token minting and burning
- [Impermanent loss](/impermanent-loss/) — the price-divergence penalty at withdrawal
- [Distributed-ledger](/distributed-ledger/) — blockchain settlement and transaction finality
- [Cryptocurrency-exchange](/cryptocurrency-exchange/) — DEX structure and pool mechanics
- [Proof-of-stake](/proof-of-stake/) — staking is distinct from liquidity provision but related

### Wider context

- [Blockchain-fundamentals](/blockchain-fundamentals/) — transaction execution and on-chain computation
- [Ethereum](/ethereum/) — the primary platform for DEX liquidity pools
- [Swap](/swap/) — the opposite transaction (entering a pool)
- [Liquidity-risk](/liquidity-risk/) — the risk of not being able to exit

</div>
