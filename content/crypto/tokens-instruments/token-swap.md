---
title: "Token Swap"
description: "An exchange of one cryptocurrency token for another, either on a decentralized or centralized platform."
---

*A token swap is a transaction in which a user exchanges one token for another, typically mediated by a [decentralized-exchange](/wiki/decentralized-exchange/) (DEX) or [centralized-exchange](/wiki/centralized-exchange/) (CEX). If you own Bitcoin but want Ethereum, you swap your Bitcoin for Ethereum using a market-making mechanism. Token swaps are the foundational mechanism of the cryptocurrency trading ecosystem.*

<aside class="wiki-infobox">
<div class="wiki-infobox-title">Token Swap — key facts</div>
<table>
<tr><th>Types</th><td>Centralized (CEX), decentralized (DEX), atomic swaps</td></tr>
<tr><th>Price discovery</th><td>Order book or automated market maker (AMM)</td></tr>
<tr><th>Settlement</th><td>Instant on-chain or T+2 in traditional settlement</td></tr>
<tr><th>Custody</th><td>Self-custody (DEX) or exchange custody (CEX)</td></tr>
</table>
</aside>

## Centralized vs. decentralized swaps

A centralized exchange (Coinbase, Kraken, Binance) operates an order book where buyers and sellers post prices and quantities. When your buy order meets a sell order, the trade executes. You deposit your tokens into the exchange's custody, specify how much you want to buy or sell and at what price, and the exchange matches you with a counterparty. Settlement is fast (milliseconds) because the exchange controls both balances. The trade-off is custody risk: if the exchange is hacked or goes bankrupt, your tokens are lost.

A decentralized exchange (Uniswap, Curve, SushiSwap) operates an [automated-market-maker](/wiki/automated-market-maker/) (AMM) where you trade against a liquidity pool, not a human counterparty. You deposit your token into the contract, specify which token you want in return, and the AMM calculates the fair exchange rate based on the ratio of assets in the pool. Settlement is on-chain and takes minutes (for Ethereum) to hours (for Bitcoin or Layer 1 chains). Custody is self-custody—you control your own private keys, so you cannot be robbed by exchange failure.

## How pricing works on an AMM

An automated market maker maintains an invariant: the product of the token quantities in the pool stays constant. If a pool has 100 Token A and 1,000 Token B, the invariant is 100 × 1,000 = 100,000. If you swap 10 Token A for Token B, the new state is 110 Token A and 909 Token B (110 × 909 ≈ 100,000). You receive 91 Token B for 10 Token A, an effective exchange rate of 9.1:1. This is different from the "spot price" of 10:1 you would expect based on the initial pool ratio. The difference is called slippage.

The larger your swap relative to the pool size, the more slippage you incur. This incentivizes large traders to split orders across multiple pools or use alternative venues. It also means that decentralized swaps become inefficient for very large orders without deep liquidity.

## Atomic swaps and cross-chain swaps

An atomic swap is a peer-to-peer exchange of tokens on different blockchains without an intermediary. User A holds Bitcoin and wants Ethereum; User B holds Ethereum and wants Bitcoin. They can perform an atomic swap by using time-locked smart contracts that ensure fairness: neither party can steal from the other without forfeiting their own tokens.

Atomic swaps are theoretically elegant but rarely used in practice because they require both parties to come to agreement, and finding trading partners is costly. Most cross-chain swaps instead use wrapped tokens: User A converts Bitcoin to Wrapped Bitcoin (WBTC) on Ethereum, then swaps it for Ethereum. The wrapping introduces centralized custody (the issuer of WBTC), but it is far simpler than atomic swaps.

## Pricing efficiency and market integration

If Bitcoin trades at $40,000 on Coinbase and $40,200 on Kraken, an arbitrageur can buy at Coinbase, sell at Kraken, and capture the $200 spread. This arbitrage quickly eliminates price discrepancies across exchanges, so that the same token trades at nearly the same price everywhere.

Decentralized exchanges can have significant price discrepancies with centralized exchanges if the liquidity is thin or if transaction costs are high. Bridging these discrepancies is profitable for arbitrageurs but requires capital and sophisticated execution.

## Transaction costs and order types

A centralized exchange typically charges a flat percentage fee (0.1–0.5% per trade). A decentralized exchange (Uniswap, Curve) charges a smaller fee (0.01–0.3%) plus the cost of the blockchain transaction (gas fees). On Ethereum, gas fees can add $10–$100 to a swap. On Layer 2 solutions (Arbitrum, Optimism), gas is much cheaper (pennies).

Decentralized exchanges typically support only market orders—you swap a quantity of Token A for Token B at the best available price. Some support limit orders through additional contracts that watch the price and execute when it reaches your target. Centralized exchanges support limit orders natively, allowing you to specify: "Sell 10 BTC when the price reaches $41,000."

## Flash loans and swap mechanics

A flash loan is an uncollateralized loan that you must repay within a single transaction. Using a flash loan, a trader can borrow a large amount of tokens, swap them on multiple exchanges to capture arbitrage opportunities, and repay the loan plus fees—all within one atomic transaction. If the arbitrage does not profit enough to cover the fee, the entire transaction reverts.

Flash loans have enabled sophisticated trading strategies but have also been weaponized in exploits: attackers use flash loans to temporarily manipulate token prices, then liquidate positions or steal value, then repay the loan. Several billion dollars in losses have resulted from flash-loan exploits.

## Taxation and compliance

Each token swap is typically a taxable event in most countries. If you swap 1 Bitcoin (worth $40,000) for Ethereum (worth $40,000), you have realized a capital gain of zero (if you bought the Bitcoin at $40,000). But if you bought it at $30,000 and sold at $40,000, you have a $10,000 capital gain and must pay tax on it. Tracking these events across thousands of swaps is complex, and many users fail to report them accurately.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/decentralized-exchange/">Decentralized Exchange</a> — the primary platform for token swaps using AMMs.</li>
<li><a href="/wiki/centralized-exchange/">Centralized Exchange</a> — traditional platforms for token swaps using order books.</li>
<li><a href="/wiki/automated-market-maker/">Automated Market Maker</a> — the pricing mechanism for decentralized swaps.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/liquidity-pool/">Liquidity Pool</a> — the reserves that enable token swaps on DEXs.</li>
<li><a href="/wiki/slippage/">Arbitrage Pricing Theory</a> — the theory underlying arbitrage that keeps prices aligned.</li>
<li><a href="/wiki/ethereum/">Ethereum</a> — the blockchain hosting most token swap platforms.</li>
</ul>
</div>
