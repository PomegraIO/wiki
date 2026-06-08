---
title: "DeFi Looping: How Recursive Borrowing Creates Leverage"
description: "DeFi looping leverage explained: how depositing collateral, borrowing, and redepositing amplifies yield and exposure—and the liquidation cascade that ends loops."
keywords:
  - defi looping
  - recursive borrowing
  - leverage in crypto
  - liquidation risk
  - yield farming
image: /svg/crypto.svg
---

*In decentralized finance, **DeFi looping**—the practice of repeatedly depositing collateral, borrowing against it, and redepositing the borrowed funds—is how traders amplify their exposure to an asset or yield without obtaining a traditional loan. It works until [liquidation risk](/counterparty-risk/) forces the loop to unwind.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DeFi Looping — Key Facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for decentralized finance." />

<div class="wiki-infobox-caption">Mechanical leverage through repeated collateralization and borrowing.</div>

|   |   |
|---|---|
| **Mechanism** | Deposit → Borrow → Redeposit → Repeat |
| **Liquidity source** | Protocol's lending pool or money market |
| **Collateral requirement** | Varies by protocol; typically 150–200% of borrowed amount |
| **Price that triggers liquidation** | When collateral value falls below minimum ratio |
| **Number of loops possible** | 5–15+ in practice before diminishing returns |
| **Liquidation risk** | Exponential; grows with each loop |

</aside>

## How a Loop Works: Step by Step

Imagine you hold 1 Ethereum (ETH) worth $3,000 and want more exposure without capital. You:

**Loop 1:** Deposit 1 ETH as collateral in a lending protocol like Aave. Borrow $2,000 worth of stablecoin (USDC) at 150% collateral ratio. Use the $2,000 to buy 0.67 ETH. Total ETH: 1.67.

**Loop 2:** Deposit the 0.67 ETH as additional collateral. Borrow another $1,335 in USDC (at 150% ratio). Buy 0.45 ETH. Total ETH: 2.12.

**Loop 3:** Deposit 0.45 ETH, borrow $900, buy 0.3 ETH. Total ETH: 2.42.

After just three loops, you have increased your ETH position from 1.0 to 2.42—a 142% gain in exposure—using only the collateral you already owned, plus recursive borrowing. Each loop borrows against the newly acquired asset, creating a multiplicative effect.

The formula for total leverage is straightforward: after *n* loops at a collateral ratio *r*, your position is multiplied by roughly (1 + 1/*r*)^*n*. At 150% collateral (1.5×), three loops yield about 2.42× leverage. Ten loops yield ~7×.

## Why Traders Loop

**Yield amplification** is the primary driver. Suppose you deposit ETH in a yield farming protocol earning 12% APY. Your real return is just the 12%. But if you loop to 3× leverage, you earn 36% on your original capital—until liquidation strikes or the underlying yield collapses.

**Directional bets** also motivate looping. If you believe ETH will rise 50%, a simple purchase captures that 50% gain. But using a loop to build 3× leverage on ETH lets you capture a 150% return on the same initial capital—provided the price does move in your favor.

**Capital efficiency** appeals to professional traders. Looping lets them control larger positions than their dry powder would normally allow. A hedge fund might loop to access multi-million-dollar exposure to an emerging token or yield farm that they believe is mispriced.

## The Liquidation Cascade

The mirror image of opportunity is risk. Each loop increases the [liquidation risk](/counterparty-risk/) of your entire position. If ETH falls from $3,000 to $2,000 (a 33% drop), your 1 original ETH is now worth $2,000. Your total debt across all loops might still be $4,500 in stablecoin. Your position is now underwater: $2,000 collateral supporting $4,500 debt. The protocol's [smart contract](/smart-contract/) automatically liquidates your holdings to repay the debt, often at a penalty (flash loan fees, slippage, liquidation discounts).

This is the liquidation cascade. Because each loop increases both your position size and debt load, a single unfavorable price move can trigger automatic liquidation of the entire stack. A 33% decline in collateral value is often enough to wipe out a 3× leveraged loop position entirely.

Real-world example: In the crypto crash of May 2022, traders who had looped LUNA or other volatile assets lost everything in minutes. The speed was brutal because [liquidation](/liquidation/) is mechanical—no human can pause or negotiate.

## Loop Mechanics: Borrowing Terms

Different protocols offer different collateral and borrowing rates:

- **Aave:** Allows up to 80% LTV (loan-to-value) on stable assets, meaning you can borrow $0.80 for every $1 of collateral. This translates to a 125% collateral ratio (1 ÷ 0.8).
- **Compound:** Similar terms, but rates vary by asset and market conditions.
- **Curve Finance:** Allows much higher leverage (10×+) on stablecoin-to-stablecoin swaps because the price risk is minimal.

The borrowing rate (interest paid) also multiplies. If you loop 5× and the protocol charges 8% APY on borrowed stablecoins, your annual debt service is not 8% on your original capital—it is 8% on 4× your capital, or 32% in total interest cost. That eats deeply into yield gains.

## Yield vs. Interest: The Math

A simple check: does the yield you earn exceed the interest you pay?

Scenario A: You loop 3× for 12% yield on a staking protocol, but pay 6% interest on borrowed funds.

- Gross yield: 12% × 3 = 36%
- Interest cost: 6% × 2 (the debt portion) = 12%
- Net return: 36% − 12% = 24% on your original capital

Profitable. But if yields fall to 8% and rates rise to 8%:

- Gross yield: 8% × 3 = 24%
- Interest cost: 8% × 2 = 16%
- Net return: 24% − 16% = 8%

The spread collapses. This is why looping is most attractive in high-yield environments or bull markets, and most dangerous when yields are tightening or volatility spikes.

## Risk Beyond Liquidation

**[Smart contract](/smart-contract/) risk** is material. The protocols you loop through (Aave, Compound, Curve) are decentralized, audited but not foolproof. A single bug could freeze your collateral or force liquidation at disadvantageous prices.

**Oracle manipulation risk** arises when the price feed that protocols use to determine collateral value is stale or can be exploited. Flash loan attacks in 2022 targeted oracle weaknesses to trigger artificial liquidations.

**Impermanent loss** affects looping on DEX liquidity pools. If you loop and deposit into an automated market maker (AMM), the pool's price movement can cause you to lose value even if the underlying asset rises.

**Regulatory risk** is mounting. Several jurisdictions are cracking down on leveraged retail crypto trading. Some platforms are disabling looping features.

## Looping Strategies: Real Examples

**Stablecoin looping:** Deposit $10,000 USDC, borrow $7,500 USDC, buy $7,500 worth of a high-yield stablecoin wrapper (e.g., convex cvxCRV). Earn 20%+ APY on the $17,500 notional, pay 6% interest on the debt. Net: ~34% return on $10k capital. Risk: low (both assets are stablecoins), as long as the yield protocol does not break.

**Volatile asset looping:** Deposit $10,000 ETH, loop to 3× ($30,000 notional). Earn 10% staking yield (12% × 3 = 36% gross), pay 8% interest on the borrowed $20k (16% total). Net: 20% return. Risk: high. A 25% ETH crash liquidates the position.

**Delta-neutral looping:** Borrow an asset, loop into it, and simultaneously short a correlated index to hedge price risk. Yields pure carry (the interest spread), with vastly reduced liquidation risk. Sophisticated, capital-intensive, and mostly used by quants.

## When to Loop and When to Avoid

**Loop when:**
- Yield (earned on total position) exceeds interest (paid on debt) by at least 5–10% after fees.
- Volatility is low and you expect it to stay low.
- You can stomach a 30%+ drawdown in collateral without panic-selling.
- The protocol is battle-tested and has ample liquidity.

**Avoid looping when:**
- You are borrowing at rates equal to or higher than yield earned.
- You are looping on highly volatile assets (small-cap tokens, meme coins).
- You cannot access the interface during a price crash (exchange downtime, network congestion).
- Liquidation would wipe you out financially.

## See also

<div class="wiki-seealso">

### Closely related

- [Smart Contract](/smart-contract/) — the code that executes looping and liquidation
- [Counterparty Risk](/counterparty-risk/) — lender solvency and protocol failure
- [Liquidation](/liquidation/) — forced position closure when collateral falls below threshold
- [Yield Farming](/yield-farming/) — earning returns on capital in DeFi
- [Distributed Ledger](/distributed-ledger/) — the underlying blockchain technology

### Wider context

- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where you buy and sell the underlying assets
- [Leverage Ratio in Forex](/leverage-ratio-forex/) — traditional leverage mechanics for comparison
- [Derivatives Hedging](/derivatives-hedging/) — protective strategies that pair with looping
- [Proof of Stake](/proof-of-stake/) — yield source for many looping strategies

</div>
