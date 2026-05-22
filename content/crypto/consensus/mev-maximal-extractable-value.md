---
title: "MEV (Maximal Extractable Value)"
description: "Front-running and priority ordering in block production, where validators extract value through transaction ordering."
keywords:
  - MEV
  - maximal extractable value
  - front-running
  - block production
  - validator extractable value
---

*Maximal Extractable Value (MEV, formerly "Miner Extractable Value") refers to profits that validators, miners, or block builders can extract by strategically ordering, including, or excluding transactions in a block. Examples include front-running, sandwich attacks, and arbitrage trades that validators execute with knowledge of pending transactions. MEV is a persistent issue in [blockchain](/wiki/blockchain-fundamentals/) networks, affecting fairness, transaction costs, and security.*

<aside class="wiki-infobox">

| Item | Details |
|------|---------|
| **Definition** | Value extracted by transaction reordering or manipulation |
| **Actors** | Validators, miners, block builders, searchers |
| **Examples** | Front-running, sandwich attacks, arbitrage |
| **Impact** | Raises user costs; benefits protocol insiders |
| **Mitigation** | Encrypted mempools, fair-ordering protocols, burn mechanisms |
| **Ethereum PoS** | Post-[Merge](/wiki/ethereum-merge/), validators extract MEV |

</aside>

## Understanding MEV and transaction ordering

In a blockchain network, transactions are collected in a mempool, and a validator (in proof-of-stake) or miner (in proof-of-work) selects and orders them into a block. This ordering power creates opportunity for extraction. If a validator sees a pending transaction in the mempool (e.g., a large [decentralized exchange](/wiki/decentralized-exchange/) trade), the validator can:

1. Place their own transaction before it (front-running) to exploit the price movement
2. Place their own transaction after it to capture the new equilibrium price
3. Exclude the transaction entirely if it is unprofitable or competitive

This ability to see and reorder pending transactions is called [mempools](/wiki/pool/) visibility, and the value extracted is MEV.

## Front-running and sandwich attacks

Front-running is the classic MEV extraction strategy. A user submits a large trade: "swap 100 ETH for USDC." The validator sees this in the mempool and observes that the 100-ETH trade will move the price of ETH lower. The validator inserts a small transaction before the user's: "swap 1 ETH for USDC at the current price." The user's 100-ETH trade then executes at a worse price (lower USDC received), and the validator's 1-ETH transaction is front-run, captured at the better price.

A sandwich attack extends this. The validator places a buy transaction before the user's large trade (front-running), benefits from the price impact, and then exits right after (back-running). The user is sandwiched and loses value.

On Uniswap and other [automated market makers](/wiki/automated-market-maker/), these attacks are rampant. Searchers and validators constantly probe the mempool for profitable transactions to front-run or sandwich. Users often experience significantly worse prices than quoted due to MEV extraction.

## Arbitrage and liquidation MEV

Another MEV source is arbitrage. If a token trades at different prices on two exchanges—Uniswap at $100, Coinbase at $102—a validator can submit a transaction that buys on Uniswap and sells on Coinbase, pocketing the spread. The validator's transaction priority gives them an advantage in capturing this arbitrage before other traders.

[Liquidation](/wiki/liquidation/) MEV is especially significant in lending protocols. If a borrower is close to liquidation (their collateral value has fallen below the required ratio), any trigger transaction that liquidates them becomes valuable. A liquidator (often a searcher or validator) submits a liquidation transaction and receives a penalty reward. Multiple liquidators compete to be first, driving up gas fees.

## Flash loan and DeFi protocol MEV

[Flash loans](/wiki/flash-loan/) (loans that must be repaid within a single transaction) enable complex MEV attacks. A searcher takes a flash loan, uses it to execute an arbitrage or liquidation, and repays the loan with profits, all within one block. This democratized MEV extraction beyond miners/validators to searchers, but it also increased the complexity and cost of attacks.

DeFi protocols have become battlegrounds for MEV extraction. Uniswap, Curve, Aave, and other protocols suffer constant front-running, creating poor user experience and reducing the profitability of arbitrage for ordinary traders (who compete with organized MEV extractors).

## Measurement and quantification

Searchers and researchers track MEV on public blockchains using tools like MEV-Inspect and Flashbots. Ethereum has seen cumulative MEV extraction in the hundreds of millions of dollars. Much of this is captured by specialized MEV bots and professional searchers, though validators and miners capture a portion through transaction ordering.

Post-[Ethereum Merge](/wiki/ethereum-merge/) (transition to proof-of-stake in September 2022), [validators](/wiki/validator/) replaced miners. Validators now extract MEV by accepting transactions from block builders (specialized entities that construct blocks and sell them to validators). This separation of duties (block building vs. validation) was designed to reduce MEV, but it created a new market—the MEV supply chain—where block builders and validators coordinate extraction.

## Mitigation strategies

Several approaches to reduce MEV have been proposed:

1. **Encrypted mempools**: Hide pending transactions from validators until they are included in a block. This prevents front-running but introduces censorship risk and complexity.

2. **Fair-ordering services**: Third-party sequencers that commit to ordering transactions fairly (e.g., FIFO) rather than optimally for MEV extraction. Examples include Chainlink FSS and MEV auction protocols.

3. **MEV-resistant layer 2 designs**: Rollups and sidechains can impose ordering constraints or use consensus algorithms less susceptible to MEV.

4. **MEV burn**: Capture MEV and redirect it to protocol treasuries or burn it entirely, removing the incentive for extraction. Flashbots has proposed MEV-Burn for Ethereum.

5. **Threshold encryption**: Transactions remain encrypted until a threshold of validators has agreed to include them, preventing individual validator MEV extraction.

## MEV and consensus security

There is debate over whether MEV helps or hurts consensus security. On one hand, MEV revenue incentivizes validators to stay engaged and stake capital. On the other hand, MEV creates a centralization risk: validators with privileged access to information (e.g., through relationships with searchers or block builders) can extract more MEV, attracting stake and consolidating power.

The [Ethereum Merge](/wiki/ethereum-merge/) transition illustrated the issue. Post-Merge, professional block builders captured most MEV, creating a specialized industry. This raised concerns about liveness and censorship resistance: if block builders are concentrated, they could censor transactions or order them in ways that harm users.

## MEV on Layer 2 and alternative blockchains

MEV is less severe on [layer 2 rollups](/wiki/optimistic-rollup/) and alternative blockchains that use different consensus or ordering mechanisms. Solana's leader-based ordering, Avalanche's subnet architecture, and Cosmos-based chains have experimented with MEV-resistant designs. But all systems face the fundamental challenge: someone must order transactions, and whoever does has incentive to extract value.

## Future outlook

MEV is likely to remain an issue as long as blockchains exist. The most promising mitigations involve protocol-level changes (encrypted mempools, threshold encryption, fair ordering) combined with application-level defenses (splitting orders, using DEX aggregators, choosing low-MEV rollups). Complete elimination is unlikely without sacrificing other desirable properties (e.g., transparency, decentralization).

<div class="wiki-seealso">

### Closely related
- [Blockchain Fundamentals](/wiki/blockchain-fundamentals/) — Core blockchain concepts
- [Decentralized Exchange](/wiki/decentralized-exchange/) — Primary venue for MEV extraction
- [Flash Loan](/wiki/flash-loan/) — Tool enabling complex MEV attacks
- [Validator](/wiki/validator/) — Operator extracting MEV post-[Merge](/wiki/ethereum-merge/)

### Wider context
- [Ethereum Merge](/wiki/ethereum-merge/) — Transition where MEV dynamics changed
- [Automated Market Maker](/wiki/automated-market-maker/) — Protocol experiencing front-running
- [Consensus Layer Security](/wiki/consensus-layer-security/) — Security implications of MEV
- [Validator Economics](/wiki/validator-economics/) — Incentives for validators including MEV

</div>