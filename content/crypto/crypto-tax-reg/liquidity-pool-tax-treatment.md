---
title: "Liquidity Pool Deposits and Withdrawals: Tax Treatment"
description: "Tax treatment of DeFi liquidity pool deposits, LP token receipts, and withdrawal gains or losses including impermanent loss handling."
keywords:
  - liquidity pool tax treatment
  - liquidity pool deposits taxable event
  - LP token tax
  - impermanent loss tax
  - defi liquidity pool taxes
image: /svg/crypto.svg
---

*Whether depositing tokens into a DeFi **liquidity pool tax treatment** question hinges on a crucial IRS distinction: does the swap trigger a taxable event? The answer is yes—you are disposing of one asset for another (the LP token), and that disposal creates a capital gain or loss, plus ongoing tax obligations as you earn fees and face impermanent loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquidity Pool Tax Treatment — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency topics." />

<div class="wiki-infobox-caption">LP deposits are taxable swaps; fees are ordinary income; withdrawals trigger additional gains or losses.</div>

|   |   |
|---|---|
| **Deposit (swap to LP token)** | Taxable event—you dispose of Token A for Token B |
| **Gain/loss recognition** | Difference between FMV of tokens in and FMV of LP tokens received |
| **Fee income (rewards)** | Taxable as ordinary income on the date earned |
| **Impermanent loss** | Only deductible if withdrawal occurs at a net loss to original deposit value |
| **Withdrawal (LP token redemption)** | Taxable event—LP tokens exchanged for underlying tokens |
| **Holding period** | Separate for each token and LP token; LP token date begins at deposit |

</aside>

## Deposits trigger a taxable swap

When you deposit two tokens into a liquidity pool on Uniswap, SushiSwap, or another decentralized exchange, you are executing a **taxable event**. You are disposing of Token A and Token B in exchange for LP tokens—a form of staking that represents your claim on the pool's assets and fee revenue.

From the IRS perspective, this is a [cryptocurrency exchange](/cryptocurrency-exchange/)—a swap of one asset for another. Even though no central exchange processes the transaction and no broker issues a 1099-K, the taxable event is identical to selling Bitcoin for Ethereum on Coinbase. You must recognize any capital gain or loss on the tokens you contributed.

Example: You deposit 10 Ethereum (worth $20,000) and 100 USDC (worth $100) into a Uniswap V2 pair. You receive LP tokens worth $20,100. Your cost basis in the Ethereum was $5,000 and in the USDC was $100. You recognize a capital gain of $15,000 on the Ethereum (sale at $20,000, basis $5,000) and zero gain on the USDC. The LP tokens themselves are treated as a new asset with a cost basis of $20,100 (the FMV you received them for).

## How to calculate the gain or loss on deposit

The taxable gain or loss on the deposit transaction is:

**Gain/Loss = FMV of LP tokens received − (FMV of Token A at deposit + FMV of Token B at deposit)**

If the sum of the tokens you put in is worth $20,100 and you receive LP tokens worth exactly $20,100 (common in most pools), the gain is zero. However, if slippage occurs or if the pool has a 0.25% entry fee, your LP tokens might be worth slightly less—say $20,075. Then you recognize a $25 loss on the deposit itself.

To track this precisely, record:
- The date of deposit
- The exact amount and type of each token deposited
- The FMV of each token from a major exchange at the moment of deposit (or the block timestamp)
- The exact amount and type of LP tokens received
- The FMV of the LP token at receipt (using a DeFi price oracle or calculator)

## Fee income is taxable as ordinary income

As your LP tokens sit in the pool, they earn a share of the trading fees paid by liquidity consumers. On Uniswap V3, for instance, you earn 0.01%, 0.05%, 0.30%, or 1.00% of all trades that occur at your price range. This fee revenue is **taxable ordinary income** on the date it is earned—not when you harvest or withdraw it.

The tricky part: determining the exact date and amount earned. Many DeFi interfaces show accrued fees in real time, but the IRS expects a defensible valuation. The fairest approach is to take the USD equivalent of fees earned at the moment they accrue in the smart contract, using price feeds from a major exchange (Coinbase, Kraken, etc.) for each token on that date.

Example: On July 15, 2024, Uniswap shows you have earned 0.05 Ethereum in fees. Ethereum is trading at $2,500 on July 15. You must report $125 as ordinary income for the tax year 2024, even if you have not yet harvested the fees.

This creates a painful scenario: if you leave fees in the pool and Ethereum crashes to $1,000 by the time you harvest in December, you still owe tax on the $125 (ordinary income, no loss offset), but the fees are now worth only $50. The loss is a capital loss on the LP tokens or the harvested tokens, but it cannot offset the ordinary income tax already incurred.

## Impermanent loss and whether it is deductible

**Impermanent loss** occurs when the price ratio of the two tokens in a pool diverges from the ratio when you deposited them. If you deposited equal value of Token A (10 units) and Token B (100 units), and later Token A rises 50% while Token B stays flat, the pool automatically rebalances to reduce your Token A exposure and increase Token B exposure (via arbitrage). When you withdraw, you have fewer Token A and more Token B than you deposited—the difference is the impermanent loss.

The IRS has not issued official guidance on whether impermanent loss is deductible. Most tax professionals treat it as follows:

- **If you withdraw at a net loss** (the total value of tokens you withdraw is less than the total value of tokens plus fees you deposited), you may claim a [capital loss](/long-term-capital-gain-tax/) on the LP token position. The loss is the difference between your basis (cost of LP token at deposit) and the FMV of assets you withdrew.

- **If you withdraw at a net gain or break-even**, no additional loss is recognized for impermanent loss itself. Impermanent loss is built into the lower withdrawal value and is factored into your capital gain or loss on the LP token when redeemed.

The safest approach: track the total value of your LP position (tokens + earned fees) at withdrawal. If it is worth less than your basis, claim the difference as a capital loss. If worth more, claim the difference as a capital gain.

## Withdrawals are a second taxable event

When you withdraw from the liquidity pool (redeem your LP tokens), you execute another taxable event. You are exchanging LP tokens for the underlying tokens, and any difference in value is taxable.

Example: You withdraw your LP tokens and receive 9.5 Ethereum (impermanent loss) and 102 USDC (plus accrued fees). Your LP tokens had a basis of $20,100. The Ethereum is worth $23,750 (at $2,500 per unit) and the USDC is worth $102. Total received is $23,852. Your capital gain on the withdrawal is $23,852 − $20,100 = $3,752.

This is separate from the gain or loss on the original tokens (Ethereum and USDC) when you first withdrew them. Those tokens have their own cost basis (the FMV at the moment you withdrew them), and if you sell them later, you will owe tax on any subsequent appreciation.

## Holding periods and long-term vs. short-term treatment

The holding period for the LP tokens begins on the date you deposited and received them. If you withdraw after holding the LP tokens for more than one year, any capital gain on the withdrawal is long-term. If you withdraw within one year, it is short-term.

This is independent of the holding period for the underlying tokens. If you held Ethereum for three years before depositing it, that three-year holding period does not transfer to the LP tokens. The LP token holding period starts fresh at deposit.

Example: You deposit Ethereum you bought in 2022 (three-year hold) on June 1, 2024, receive LP tokens, hold them until July 1, 2025, and withdraw. Your withdrawal gain is long-term (held LP tokens over one year) even though the Ethereum itself has a longer hold. But the tokens you withdrew have a new holding period starting July 1, 2025; if you sell them in September 2025, that is short-term (under one year).

## Concentrated liquidity and Uniswap V3 complications

Uniswap V3 and similar "concentrated liquidity" protocols allow you to provide liquidity only within a specific price range, earning more fees but carrying more impermanent loss if prices move outside that range. This adds complexity: you must track which price ranges you supplied liquidity to, when you rebalanced (moved your liquidity), and the cost basis of each rebalance.

Each rebalance is a new deposit/withdrawal transaction pair. If you move your liquidity up the range, you are withdrawing from the old range (triggering a gain/loss) and depositing in the new range (triggering another gain/loss plus a new LP token with a fresh cost basis and holding period). Document every rebalance meticulously, or you will face unreconciled tax positions on audit.

## Accounting for multiple pools and staking rewards

If you provide liquidity to multiple pools (e.g., Uniswap, SushiSwap, Curve), treat each as a separate [tax lot](/tax-lot/). If the protocol also distributes governance tokens (SushiSwap distributes SUSHI) or other rewards, these are separate taxable events at the moment of receipt, valued at that moment's FMV.

## See also

<div class="wiki-seealso">

### Closely related

- [Cost Basis](/cost-basis/) — how the IRS defines the cost of an asset at purchase
- [Capital Gains Tax](/long-term-capital-gain-tax/) — taxation of investment income
- [Fair Value](/fair-value/) — how the IRS determines asset value for tax reporting
- [Form 8949](/form-8949/) — how to report gains and losses on Schedule D
- [Tax Lot](/tax-lot/) — tracking individual purchases for precise gain/loss calculation

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — how asset swaps are taxed
- Deferred Compensation — rules on yield and staking income
- [Derivative Pricing](/derivatives-hedging/) — related pricing concepts for complex instruments

</div>
