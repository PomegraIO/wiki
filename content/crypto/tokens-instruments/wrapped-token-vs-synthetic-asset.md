---
title: "Wrapped Token vs Synthetic Asset in DeFi"
description: "Wrapped tokens are collateral-backed bridges for cross-chain assets; synthetics track prices via oracles. Learn the risk and trust trade-offs of each approach."
keywords:
  - wrapped token vs synthetic asset
  - wrapped token crypto
  - synthetic asset defi
  - wbtc vs synthetic bitcoin
image: "/svg/crypto.svg"
---

*A **wrapped token** is a collateral-backed representation of an asset on a different blockchain—WBTC on Ethereum, for example, is backed 1:1 by actual Bitcoin held in custody. A **synthetic asset** is a price-tracking token that derives its value from an oracle feed, not physical collateral—one synthetic USD (sUSD) tracks the USD price via an oracle, not a vault of actual dollars. Wrapped tokens require a trusted custodian but offer simple redemption; synthetics are decentralized but expose holders to oracle risk and liquidation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Wrapped vs Synthetic — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two mechanisms for representing off-chain or cross-chain assets on-chain, with different trust and efficiency trade-offs.</div>

|   |   |
|---|---|
| **Wrapped tokens** | Custodial, collateral-backed, 1:1 redemption |
| **Examples** | WBTC, WETH, wrapped stablecoins |
| **Trust assumption** | Trust the custodian to hold collateral safely |
| **Synthetic assets** | Oracle-backed, price-pegged, algorithmically minted |
| **Examples** | sUSD, sEURO, perpetual futures tracking indices |
| **Trust assumption** | Trust the oracle to report accurate prices |

</aside>

## The bridge problem in cross-chain DeFi

Before wrapped and synthetic tokens, moving assets between blockchains was a practical nightmare. Bitcoin lives on the Bitcoin blockchain; Ethereum lives on Ethereum. If you wanted to use Bitcoin in an Ethereum DeFi protocol, you had to sell Bitcoin, buy Ethereum-native assets, and use those instead—losing the exposure to Bitcoin's price. Alternatively, you could use a centralized exchange to send Bitcoin from Bitcoin blockchain to an Ethereum address (which would simply receive nothing, because Bitcoin addresses do not exist on Ethereum).

Wrapped and synthetic tokens solve this by creating a proxy: a representation of Bitcoin (or any asset) that lives on Ethereum and can be used in Ethereum DeFi. The proxy trades and behaves like the underlying asset, but it is a new token that exists only on Ethereum. The difference lies in how that proxy is created and backed.

## Wrapped tokens: custodial collateral

A **wrapped token** is issued by a custodian who locks the underlying asset and mints a corresponding wrapped token 1:1. WBTC (Wrapped Bitcoin) works like this: you send Bitcoin to the Wrapped Bitcoin custodian, who holds it in a vault (usually multi-sig, meaning multiple signers must approve moves). In exchange, the custodian mints and sends you WBTC on Ethereum, equal in amount to your deposited Bitcoin. If you later burn the WBTC, the custodian sends you Bitcoin back.

The trust model is simple: you trust the custodian (or the multi-sig holders) to safeguard the collateral and honor the 1:1 redemption. If the custodian is reputable, well-insured, and transparent about reserves, the wrapped token is secure. If the custodian is compromised, goes insolvent, or freezes the vault, you lose your asset. This is counterparty risk—the risk that the middleman fails you.

Wrapped tokens are popular because they are straightforward and efficient. The supply is always backed 1:1 by reserves. There is no risk of liquidation or depeg (price divergence from the underlying). WBTC will always trade at or near Bitcoin's price because any divergence creates an arbitrage opportunity: if WBTC trades at $40,000 and Bitcoin at $43,000, a trader can buy WBTC, burn it for Bitcoin, and pocket the difference.

Common wrapped tokens include:
- **WBTC**: Bitcoin wrapped on Ethereum, Polygon, Arbitrum, and other chains.
- **WETH**: Ethereum wrapped on Polygon, Arbitrum, and sidechains (yes, Ethereum wraps itself—necessary for cross-chain DEX compatibility).
- Stablecoin wrappers: USDC, USDT, and DAI exist natively on multiple chains but are sometimes "wrapped" when bridged.

## Synthetic assets: oracle-backed, decentralized

A **synthetic asset** is a token whose value is derived algorithmically from an oracle price feed, not backed by collateral. The issuer does not hold Bitcoin; instead, they track Bitcoin's price via an oracle (a data provider that publishes Bitcoin's price on-chain) and adjust the synthetic token's behavior to maintain a 1:1 peg to that price.

Consider Synthetix's sUSD. It is not backed by vaults of USD. Instead, it is minted by staking SNX tokens as collateral and algorithmically maintains a 1:1 price peg with USD through:
1. **Oracle pricing**: The oracle feeds the USD price into the Synthetix protocol.
2. **Minting and burning**: Users can mint sUSD by locking SNX as collateral. If sUSD trades above $1, arbitrageurs can mint sUSD (at $1 value) and sell it for $1.10, profiting $0.10 per unit and increasing supply until price falls back to $1.

Another variant: perpetual futures and leverage products like dYdX's synthetic ETH. These use oracles to track Ethereum's price and allow users to long or short the price via collateralized positions. The token's value moves with the oracle-reported price, not held assets.

## Wrapped vs. synthetic: key trade-offs

**Collateral vs. oracle risk**: Wrapped tokens require trusting a custodian and the integrity of the vault. Synthetic assets require trusting the oracle—the data source reporting prices. If an oracle is hacked, manipulated, or feeds stale prices, the synthetic's peg breaks. If a custodian is compromised, the wrapped token becomes worthless. Neither is "safer"; the risks are categorical.

**Liquidation**: Wrapped tokens do not liquidate. Your WBTC is backed 1:1 by Bitcoin; it cannot drop in value relative to Bitcoin except through exchange slippage. Synthetic assets are often collateralized—you stake collateral to mint them—and are subject to liquidation. If sUSD is minted by staking SNX at a 300% collateral ratio, and SNX price falls 50%, your collateral is liquidated to maintain protocol solvency. This liquidation risk does not exist for wrapped tokens.

**Decentralization**: Wrapped tokens are custodial. WBTC is issued by a company (Ren, originally; later governance through a decentralized DAO). Synthetic assets are often minted and managed by decentralized protocols. You mint sUSD by interacting with Synthetix smart contracts; no company custodian is involved. This decentralization is appealing ideologically, but it does not eliminate risk—it redistributes it from a custodian to the oracle and protocol.

**Efficiency**: Wrapped tokens are straightforward and heavily traded; liquidity is deep. Synthetic assets often have lower liquidity in secondary markets, creating wider spreads. However, synthetics enable products that wrapped tokens cannot easily support: you can hold synthetic leverage (e.g., 3x synthetic Ethereum) without wrapping actual collateral across chains.

**Redemption**: Wrapped tokens have simple redemption: burn WBTC, receive Bitcoin. Synthetic assets do not have redemption in the traditional sense. You do not burn sUSD to receive USD; you trade it for USD on a DEX, or you unwind your collateralized position by burning sUSD and unlocking your staked collateral. This difference can be important if you need guaranteed off-chain conversion.

## Examples and use cases

**Wrapped Bitcoin (WBTC)** bridges Bitcoin into Ethereum DeFi. A trader who wants Bitcoin exposure but wants to use Ethereum DeFi can deposit Bitcoin, receive WBTC, deposit WBTC into a Uniswap liquidity pool, and earn fees. The WBTC is always backed by Bitcoin in the vault, so there is no liquidation or peg risk.

**Synthetix synths** (sUSD, sETH, sAUD, etc.) are synthetic assets tracking various commodities, currencies, and indices. A trader can mint sUSD, trade it for sEURO (both tracking real-world prices), and profit on currency movements, all on-chain and without a centralized currency exchange. But minting requires collateral, and if prices move sharply, positions liquidate.

**dYdX perpetuals** are synthetic leverage products. A trader deposits collateral, goes 10x long on Ethereum using a synthetic leveraged token, and borrows against the oracle price feed. If the market moves against the trader, the position liquidates. This product is impossible with wrapped tokens—you cannot "wrap 10x leverage" because you only have one Bitcoin to wrap.

## Peg stability and arbitrage

Wrapped tokens maintain their peg through simple arbitrage: any meaningful divergence from the underlying asset creates a profitable trade that brings price back to parity. Synthetic assets maintain pegs through more complex incentive mechanisms, oracle-based pricing, and liquidations. Wrapped tokens are structurally more stable; synthetics are operationally more complex but more flexible.

A wrapped token that trades significantly below the underlying (e.g., WBTC at $41,000 when Bitcoin is $43,000) creates an arbitrage: buy WBTC, redeem it for Bitcoin, sell Bitcoin. This trade is instantly profitable if liquidity is available. Synthetic assets rely on minting and burning incentives; if the oracle fails, the peg can break catastrophically.

## Regulatory clarity

Wrapped tokens face scrutiny as potential securities or derivatives, depending on custody structure and claims. Most regulators view WBTC as a custodial arrangement, similar to holding an asset at a bank—not a security. Synthetic assets face harder questions: do they constitute unregistered derivatives? This varies by jurisdiction and is still evolving.

## See also

<div class="wiki-seealso">

### Closely related

- [Fan Token Explained](/fan-token-explained/) — tokens issued for fan engagement and voting
- [Token Unlock Schedule](/token-unlock-schedule/) — how synthetic and wrapped tokens are released to stakeholders
- [Fungible vs Non-Fungible Token](/fungible-vs-non-fungible-token/) — wrapped and synthetic tokens are fungible by design
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where wrapped and synthetic tokens are traded

### Wider context

- [Ethereum](/ethereum/) — the primary chain hosting wrapped and synthetic token ecosystems
- [Bitcoin](/bitcoin/) — the most commonly wrapped asset, enabling Bitcoin use in Ethereum DeFi
- [Distributed Ledger](/distributed-ledger/) — the foundational technology enabling cross-chain bridges
- [Derivatives Hedging](/derivatives-hedging/) — synthetic assets as on-chain derivatives

</div>
