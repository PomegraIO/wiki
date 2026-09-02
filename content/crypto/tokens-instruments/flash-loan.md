---
title: "Flash Loan"
description: "An uncollateralized, instantly funded loan that must be repaid within a single transaction block."
---

*A flash loan is a permissionless loan of any amount that must be borrowed, used, and repaid within a single blockchain transaction (typically within milliseconds). The protocol does not require collateral; it trusts that the repayment logic is built into the transaction itself. If the transaction reverts (fails to repay), the entire operation is reversed as if it never happened. Flash loans have enabled sophisticated trading strategies but have also been weaponized in billions of dollars' worth of exploits.*

## How flash loans work

A user calls a flash loan contract with a function that says: "Give me 10 million USDC instantly." The contract transfers the USDC to the user's address (or smart contract) and executes a callback function specified by the user. Within that callback, the user can do anything: swap tokens, call other protocols, borrow more, liquidate positions. At the end of the callback, the protocol requires the user to repay the original amount plus a small fee (typically 0.05–0.3%).

If the repayment succeeds, the transaction is finalized and the borrower has profited. If the repayment fails, the entire transaction reverts: any swaps, liquidations, and new borrows are undone, and the loan is cancelled as if it never happened. The blockchain returns to its pre-transaction state.

This is only possible because blockchain transactions are atomic. Either the entire transaction succeeds and is recorded on the chain, or it fails and is rolled back. There is no intermediate state.

## The economic opportunity

Flash loans enable arbitrage and liquidation strategies that were previously impossible. Consider this scenario:

1. An arbitrageur borrows 10 million USDC via flash loan.
2. They use the USDC to buy Bitcoin on Exchange A at $40,000/BTC.
3. They immediately sell the Bitcoin on Exchange B at $40,500/BTC.
4. They receive $40,500 × 250 = 10.125 million USDC.
5. They repay the flash loan (10 million USDC + 0.05 million in fees).
6. They pocket the 0.075 million USDC profit.

Without flash loans, the arbitrageur would need to own 10 million USDC upfront, limiting the number of profitable trades they could execute. Flash loans democratize arbitrage: any smart contract can borrow, and the only constraint is that the trade must profit enough to cover the fee.

Similarly, flash loans enable liquidations. If a user has borrowed against collateral and the collateral value falls, a liquidator can flash loan the full repayment amount, liquidate the position, and profit from the price difference—without needing to own the repayment amount initially.

## Security exploits and cascading failures

Flash loans have been weaponized. If a protocol is poorly designed, an attacker can use a flash loan to:

1. Borrow a massive amount of an asset.
2. Use it to temporarily manipulate the price of another asset (by swapping into an illiquid pool).
3. Exploit a protocol that relies on faulty price oracles.
4. Extract funds or collateral.
5. Repay the flash loan and pocket the stolen value.

High-profile exploits include:

- **bZx (2020):** Attackers flash loaned 7,500 ETH, manipulated the price of certain tokens, and liquidated positions on a lending protocol. Stolen value: ~$1 million.
- **Pancake Bunny (2021):** Attackers flash loaned 30 million USDC, manipulated token prices, and drained the protocol's reserves. Stolen value: ~$45 million.
- **Curve (2023):** Attackers exploited a pool with vulnerable pricing, using flash loans to amplify the attack. Stolen value: ~$50 million across multiple protocols.

These exploits have driven losses in the billions of dollars and sparked intense debate over whether flash loans should exist at all.

## Defending against flash-loan attacks

Protocols defend themselves by using more robust price oracles. Instead of relying on the current spot price (which can be manipulated in a single transaction), they use:

- **Time-weighted average price (TWAP).** The average price over the last hour, day, or week. A flash loan manipulation only affects the current price, not the long-term average.
- **Multiple oracle sources.** Querying prices from several independent sources and using the median. This makes it harder for a single-source manipulation to succeed.
- **Circuit breakers.** Halting operations if the price moves beyond a threshold, requiring operator intervention.
- **Decentralized oracles.** Services like Chainlink provide price data sourced from multiple exchanges and validators, making manipulation much harder.

## The regulatory question

Regulators and policymakers have questioned whether flash loans should be restricted. Some argue they should require collateral or take multiple transactions to settle, eliminating the atomic property that makes them attractive. Others defend them as a legitimate financial tool that, like any tool, can be misused.

Current regulation is sparse. Most countries have not explicitly addressed flash loans. In the EU, regulators have suggested they might fall under circuit-breaker or position-limit rules, but enforcement is uncertain.

## The limit of flash-loan utility

Flash loans are useful only for opportunities that can be exploited in a single transaction. They cannot fund long-term positions, cannot be used to bet on price movements over days or weeks, and cannot fund illiquid assets that cannot be liquidated instantly. Their primary use cases are arbitrage, liquidation, and exploitation. As DeFi matures and protocols become more robust to exploits, the economic value of flash loans for legitimate arbitrage may exceed their value for attacks, but the risk of systemic failure from a single exploited protocol remains substantial.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/automated-market-maker/">Automated Market Maker</a> — often targets of flash-loan attacks due to price manipulation.</li>
<li><a href="/wiki/liquidation-value/">Liquidation Value</a> — flash loans are often used to execute liquidations.</li>
<li><a href="/wiki/arbitrage-pricing-theory/">Arbitrage Pricing Theory</a> — the economic foundation of flash-loan arbitrage.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/decentralized-exchange/">Decentralized Exchange</a> — a common target of flash-loan attacks.</li>
<li><a href="/wiki/ethereum/">Ethereum</a> — the blockchain where most flash loans originate.</li>
<li>Proof of Work — improving oracle design is key to flash-loan defense.</li>
</ul>
</div>
