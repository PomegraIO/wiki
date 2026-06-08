---
title: "DeFi Yield Farming Risks"
description: "Yield farming risks include smart contract exploits, rug pulls, liquidation from price drops, and impermanent loss in liquidity pools."
keywords:
  - defi yield farming risks
  - yield farming liquidation
  - impermanent loss
  - rug pull crypto
  - smart contract exploit yield
---

*Yield farming—depositing crypto into DeFi protocols to earn token rewards—carries concentrated risks often invisible to casual participants. **Smart contract exploits**, **rug pulls** (developers stealing funds), **impermanent loss** (unfavorable price movement of pooled assets), and **liquidation cascades** can quickly wipe out gains or entire positions. The opportunity for high returns comes paired with genuine risk of total loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Yield Farming Risks — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for cryptocurrency." />

<div class="wiki-infobox-caption">High yields often reflect high-risk positions, not market inefficiencies.</div>

|   |   |
|---|---|
| **Smart contract risk** | Code bugs or exploits allow theft of pooled funds |
| **Rug pull** | Developers exit with depositors' capital and rewards |
| **Impermanent loss** | Price divergence causes losses even if both assets increase |
| **Liquidation risk** | Borrowed positions are force-closed if collateral value falls |
| **Token risk** | Farming rewards are new/illiquid tokens that crash post-farming |
| **Bridge/wrap risk** | Wrapped assets backing the farm may fail or unpeg |

</aside>

## Smart contract exploits

Every yield farm is built on smart contracts—code that executes automatically without intermediaries. When code has bugs or exploits, the consequences are immediate and often irreversible.

Examples of real DeFi hacks:

- **Curve Finance (2023)**: A vulnerability in one of Curve's stablecoin swap contracts allowed an attacker to drain liquidity pools worth tens of millions.
- **Poly Network (2021)**: An exploit in a cross-chain bridge allowed a thief to steal over $600 million from various yield farming pools.
- **Compound (2024)**: A misconfiguration in a token distribution contract briefly over-distributed rewards, creating unintended arbitrage opportunities that depositors exploited.

Yield farmers are exposed to code risk directly. If the pool's smart contract is exploited, your deposited capital can vanish in minutes. Unlike traditional finance, there is no insurance fund or regulatory backstop; the loss is permanent.

Audits reduce but don't eliminate this risk. Many exploited protocols *had* audits—audits catch obvious bugs but miss subtle or creative attack vectors.

## Rug pulls and exit scams

A rug pull occurs when protocol developers drain the project's funds and disappear, typically:

1. Launching a new yield farm or token with very high APY (annual percentage yield).
2. Attracting deposits from yield farmers seeking high returns.
3. Selling the reward tokens or liquidity pool reserves into the market.
4. Withdrawing the proceeds, disabling withdrawals, or abandoning the protocol.
5. Farmers are left holding worthless reward tokens and (sometimes) locked or stolen liquidity.

Rug pulls range from outright theft (e.g., locking deposits in a contract that only developers can call) to more subtle exits (e.g., simply ceasing development, letting the smart contract deprecate, and allowing liquidity to evaporate).

Flags for rug pull risk:

- **Anonymous or low-reputation developers**: A team with no track record and hidden identities is a red flag.
- **Excessive APY**: If a farm offers 1,000% APY or higher, the yield is unsustainable and likely supported by unsustainable token printing or theft.
- **Opaque governance**: No clear mechanism for users to upgrade or stop the protocol if problems emerge.
- **No audits or minimal documentation**: A protocol that won't pay for audits or disclose code likely has something to hide.
- **Rapidly changing contracts or sudden withdrawals**: Signs developers are moving money or changing terms.

Rug pulls are common in nascent DeFi ecosystems. Many appear legitimate for weeks or months before the exit. There is no surefire protection except due diligence and investing only what you can afford to lose.

## Impermanent loss in liquidity pools

Automated market makers (AMMs) like Uniswap operate on a simple formula: **x × y = k**, where x and y are the quantities of two assets in a liquidity pool. To earn fees, farmers must deposit equal dollar values of two tokens, which sit in the pool and execute trades.

Here is the catch: as the price of one asset moves relative to the other, the pool automatically rebalances to maintain the formula. Farmers end up holding more of the asset that decreased and less of the asset that increased.

Example:

- You deposit 1 ETH + 1,000 USDC (assuming 1 ETH = $1,000) into a Uniswap pool.
- Your liquidity provider (LP) share is 50% of the pool (for simplicity).
- Over time, Ethereum rallies to $2,000.
- The pool rebalances: you now hold 0.7 ETH + 1,414 USDC (the pool has sold your ETH to other traders wanting to buy it).
- Your total value is 0.7 × $2,000 + 1,414 = $1,414 × $2 + $1,414 = approximately $2,828.
- However, if you had simply *held* 1 ETH + 1,000 USDC, you'd have $2,000 + $1,000 = $3,000.
- The difference ($172) is your impermanent loss.

The word "impermanent" suggests the loss could reverse if prices return to the original ratio—and it can. But in real trading, prices rarely return to exact starting points. The loss often becomes permanent.

Farmers offset impermanent loss with trading fees earned from the pool, but in high-volatility markets, impermanent loss often exceeds fee income. Reward token APY may appear generous but often just compensates for expected impermanent loss—sometimes inadequately.

## Liquidation cascades

Some yield farming strategies involve borrowing crypto (e.g., via Aave or Compound) to amplify returns. A farmer might:

1. Deposit $10,000 in collateral (e.g., ETH).
2. Borrow $5,000 in USDC against that collateral.
3. Use the $5,000 to enter the farming pool alongside their original $10,000.
4. Earn yield on $15,000 instead of $10,000.

This leverage increases returns—but it also increases risk. If ETH's price drops 25%, the collateral is worth $7,500, and the protocol will liquidate (force-close) the borrowing position to protect itself. The farmer loses the collateral, loses the farm position, and must repay the borrowed amount.

In extreme market stress, liquidations cascade: as one farmer's position is liquidated, it dumps assets on the market, dropping prices further and triggering other liquidations. This cascade can cause a death spiral in the farming protocol, wiping out pools and leaving many farmers with total or near-total losses.

## Reward token risk

Yield farming rewards are typically paid in the protocol's own governance or utility token. The farmer earns, for example, 500% APY in governance tokens—which sounds fantastic until the tokens begin trading publicly and crash 80% in value.

This happens because:

- **Infinite supply**: Yield farming token rewards can be printed endlessly, diluting value.
- **Sell pressure**: Farmers immediately sell rewards to lock in gains or pay farming expenses, dumping tokens into the market.
- **Lack of utility**: The reward token may have no real use or revenue backing it.
- **Market saturation**: Early users earn cheap tokens that balloon in value; later users earn cheap tokens that plummet.

Many yield farms are structured more like Ponzi schemes than sustainable businesses: early participants earn high returns paid from later participants' deposits, until the scheme collapses as the token crashes and new deposits dry up.

## Tax implications of yield farming

Yield farming creates a tax complication: you owe income tax on rewards the moment they are earned, not when you sell them.

If you earn 500 governance tokens worth $1,000 on the day of receipt, you owe income tax on $1,000 at your ordinary income rate (up to 37% in the US), even if the tokens crash to $100 by the time you sell them. You may have lost money overall while owing tax on the original $1,000.

This tax timing mismatch catches many yield farmers off guard. Combined with farming losses, liquidations, and rug pulls, the tax bill can exceed remaining capital.

## Due diligence checklist for yield farmers

- **Team**: Known, doxxed developers with a track record.
- **Audits**: Third-party smart contract audits from reputable firms; review audit findings.
- **Economics**: Understand what backs the high APY. Is it sustainable or dependent on endless token printing?
- **Liquidity**: Can you exit easily? Check whether deposits and withdrawals are working normally.
- **Insurance**: Does the protocol have insurance or security fund? (Not a guarantee but a sign of seriousness.)
- **Lock-in periods**: Can you withdraw your principal at any time? Long lock-ins increase risk.
- **Test size**: Farm only capital you can afford to lose completely. Never use borrowed money for speculative yield farming.
- **Exit plan**: Know your target APY and exit price for the rewards token. Farming rewards that crash to zero are no longer a return—they are a loss.

## See also

<div class="wiki-seealso">

### Closely related

- Smart contract risk — Code vulnerabilities underlying DeFi protocols
- [Cryptocurrency exchange](/cryptocurrency-exchange/) — Where farming rewards are sold
- [Liquidation](/liquidation/) — Force-closure of leveraged positions
- [Wrapped token: how it works](/wrapped-token-how-it-works/) — Bridge assets used in many farming pools
- [Crypto airdrop tax treatment](/crypto-airdrop-tax-treatment/) — Tax treatment of yield rewards

### Wider context

- [Hedge fund](/hedge-fund/) — Traditional leverage and illiquidity analogues
- Cryptocurrency fundamentals — Broader DeFi ecosystem context
- [Debt-to-equity ratio](/debt-to-equity-ratio/) — Leverage metrics applicable to farming positions
- [How a blockchain hard fork works](/how-a-blockchain-hard-fork-works/) — Protocol upgrades can affect farming terms

</div>
