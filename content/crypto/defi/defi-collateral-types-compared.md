---
title: "DeFi Collateral Types Compared"
description: "Comparing volatile crypto, liquid staking tokens, and stablecoins as collateral in lending protocols—risk, efficiency, and usage patterns."
keywords:
  - defi collateral types compared
  - crypto collateral lending
  - stablecoin collateral
  - liquid staking collateral
  - collateral efficiency defi
image: "/svg/crypto.svg"
---

*DeFi collateral comes in three broad classes: volatile crypto assets (ETH, BTC), liquid staking tokens (stETH, rETH), and stablecoins (USDC, DAI). Each offers different tradeoffs in capital efficiency, liquidation risk, and oracle dependencies. Borrowers choose based on borrowing costs, collateral haircuts, and risk tolerance; lenders evaluate collateral quality and diversification.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DeFi Collateral Types — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Capital efficiency rises with collateral quality and price stability, but so does liquidation speed.</div>

|   |   |
|---|---|
| **Volatile crypto** | ETH, BTC, MATIC; high APY borrow, low LTV, high liquidation risk |
| **Liquid staking tokens** | stETH, rETH, cbETH; moderate APY, medium-high LTV, oracle-dependent |
| **Stablecoins** | USDC, DAI, USDT; lowest APY, highest LTV, counterparty risk |
| **Typical LTV range** | Volatile: 50–65%, LSTs: 70–85%, Stablecoins: 85–95% |
| **Primary risk** | Volatile: price, LSTs: de-peg, Stablecoins: issuer solvency |
| **Best for borrowers** | Volatile: speculation, LSTs: yield stacking, Stablecoins: leverage |

</aside>

## Volatile Crypto as Collateral: ETH and BTC

Volatile crypto assets are the backbone of DeFi collateral. Ethereum and Bitcoin—the two largest cryptocurrencies by market cap—are accepted as collateral on nearly every lending protocol. They offer deep liquidity, strong price discovery, and community recognition, making oracle risk manageable.

However, volatility comes with strings attached. A loan-to-value (LTV) ratio on ETH is typically 60–65%, meaning you can borrow $60–65 for every $100 in ETH collateral. By contrast, USDC might have an 85% LTV. This haircut reflects price risk: a 20% drop in ETH price forces liquidation if you've borrowed at high LTV.

Borrowing costs on volatile assets are steep—often 4–8% APY on major protocols—because lenders demand compensation for price volatility. A borrower using ETH collateral might pay 6% to borrow USDC, effectively betting that ETH will appreciate enough to offset the borrow cost. This makes volatile collateral less suitable for passive borrowing; it's preferred by traders and leveraged yield farmers betting on asset appreciation.

## Liquid Staking Tokens: stETH, rETH, cbETH

Liquid staking tokens (LSTs) occupy the middle ground. stETH (Lido's ETH derivative) and rETH (Rocket Pool's) represent claims on staked ETH earning 3–4% annual rewards. For collateral purposes, this is attractive: an LP gets passive staking yield plus borrowing capacity on the same capital.

A typical LST LTV is 75–85%, higher than raw ETH but lower than stablecoins. Borrow rates on LST collateral are 2–4%, lower than volatile crypto but higher than stablecoins. This creates an arbitrage: borrow stablecoins against stETH at 2.5%, lend them out at 4%, and pocket the 1.5% spread while earning staking yield on the collateral (net yield ~5%). This strategy is called "yield stacking" and is a major driver of LST collateral demand.

The tradeoff is oracle and de-peg risk. An LST's value is derived from its underlying asset (ETH) plus accumulated staking rewards. If the staking service fails or pauses withdrawals, the LST can de-peg (trade below its underlying value). A 10% de-peg immediately erodes borrowing capacity and triggers liquidations if LTV thresholds are breached.

## Stablecoins: Capital Efficiency Maximized

Stablecoins—USDC, DAI, USDT—offer the highest LTV (85–95%) and lowest borrow costs (0.5–2% APY). They're ideal for borrowers seeking leverage without price risk. A borrower using $100 USDC collateral can borrow $85 of additional USDC, then deploy that for yield farming, trading, or other strategies.

The capital efficiency is powerful but brittle. Stablecoin LTVs assume zero price volatility and rely entirely on issuer solvency. USDC's LTV is high because it's fully backed and regulated; USDT's is slightly lower due to opacity concerns; DAI's varies by collateral composition. A stablecoin depegging (collapsing to $0.98 or less) breaks the model: lenders face losses, borrowers face liquidation even if they collateralized "safely."

Stablecoins also carry counterparty risk. USDC's issuer (Circle) holds the reserves; if Circle fails or regulators seize USDC, the collateral loses value. This is distinct from price risk and cannot be hedged on-chain.

## Comparing LTV, Borrow Rate, and Liquidation Speed

Here's how the three collateral types stack up on a typical lending protocol:

| Collateral | LTV | Borrow APY | Price Risk | Liquidation Speed | Best Use |
|---|---|---|---|---|---|
| ETH | 60% | 6% | High | Slow (deep liquidity) | Leveraged bets on ETH |
| stETH | 80% | 3% | Moderate (de-peg) | Medium | Yield stacking |
| USDC | 90% | 1% | Low | Fast (instant) | Leverage and leverage-recycling |

The "liquidation speed" reflects how quickly collateral can be sold if a borrower falls below LTV. ETH has deep trading pairs and DEX liquidity; liquidating $1M of ETH takes seconds. stETH has decent but thinner liquidity; liquidating might require minutes. USDC, being perfectly liquid with other stablecoins, is instant—but that speed cuts both ways: underwater positions liquidate quickly.

## Multi-Collateral Portfolios and Concentration Risk

Most sophisticated DeFi users hold a diversified collateral portfolio. A borrower might post:
- 50% of collateral as stETH (high yield, reasonable LTV)
- 30% as ETH (stable, recognized, liquid)
- 20% as USDC (emergency buffer, high LTV)

This mix captures staking yield on the LST, price upside on ETH, and capital efficiency on stablecoins. The weighted-average LTV is roughly 75%, providing a margin of safety.

Protocols also diversify on the supply side. Lending protocols accept multiple collateral types to reduce single-asset risk; if all collateral were stETH and stETH de-pegged, the protocol would fail. Diversification is reflected in LTV policies: each asset gets a specific haircut based on its risk profile.

## De-Peg Risk Specific to LSTs

Liquid staking tokens carry a subtle but critical risk absent from volatile crypto and stablecoins: de-peg risk. An LST can de-peg for several reasons:

1. **Validator exit queue delays**: If staking withdrawals get congested (many validators exiting simultaneously), users holding LST might withdraw slowly, creating demand for immediate liquidity and temporary de-pegs.
2. **Staking service insolvency or pause**: If Lido (or another service) pauses, is hacked, or defaults, stETH might trade at a large discount to its underlying value.
3. **Underlying asset weakness**: If ETH crashes and staking becomes unprofitable, LST demand might collapse.

A 5% stETH de-peg is recoverable if you have low LTV; a 15% de-peg can trigger liquidations. This is why LST LTVs are capped below their theoretical value. A stETH worth $2000 + $80 in staking rewards might have a theoretical "backing" of $2080, but lending protocols cap LTV at $1600 ($2000 × 80% LTV) to absorb de-pegs.

## Oracle Dependencies and Price Feeds

All collateral depends on oracles to determine prices and trigger liquidations. Volatile crypto assets use decentralized oracles (Chainlink) feeding multiple exchange prices; these are robust but not infallible. LSTs rely on derivative pricing models; stETH's oracle reports its ETH value plus accrued staking rewards. Stablecoins use price-feed fallbacks (e.g., USDC → USD spot rate → other stablecoins).

An oracle failure can trigger false liquidations or allow underwater borrowing. Most protocols layer safeguards: multiple oracle feeds, price staleness checks, and liquidation delays. But no oracle is perfect, and oracle manipulation has been a source of past attacks.

## Real-World Example: Yield Stacking with stETH

A typical yield-stacking scenario:
1. Deposit $100,000 stETH into a lending protocol.
2. Borrow $75,000 USDC at 2.5% APY against it.
3. Lend that $75,000 to a Curve gauge or money market earning 4% APY.
4. Net: earn 3.5% staking yield on $100k stETH + (4% − 2.5%) = 1.5% on $75k borrowed = $3,500 + $1,125 = $4,625 annually (4.6% total).

This is attractive, but liquidation risk is real. A 20% drop in stETH value (either price or de-peg) puts the position underwater; a 5–10% drop might already trigger liquidation depending on exact LTV settings. Yield stacking is profitable during stability but painful during volatility.

## Collateral Hierarchy and Risk Tiers

Sophisticated protocols tier collateral: some assets can be posted as collateral, some can be borrowed, some can do both, and some can only be borrowed. This structure prevents circular lending and manages risk. For example:

- **Tier 1**: ETH, BTC, USDC—can be collateral or borrowed.
- **Tier 2**: stETH, rETH, DAI—can be collateral; borrowing restricted or carries higher interest.
- **Tier 3**: Niche tokens—only borrowable, never collateral; used for flash loans or isolated lending.

This tiering ensures core risk assets remain stable while allowing flexibility for sophisticated users.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquid Staking Tokens as DeFi Collateral](/liquid-staking-token-as-defi-collateral/) — Deep dive on LST-specific risks and oracle dependencies
- [DeFi Fee Tier Selection for Liquidity Providers](/defi-fee-tier-selection/) — How collateral composition affects LP returns
- [Vote-Escrow Bribe Markets in DeFi](/ve-token-bribe-market/) — Governance token collateralization and voting power
- [Liquidation](/counterparty-risk/) — Mechanics of collateral auctions and haircuts
- [Oracle Risk](/price-discovery/) — Price feeds and de-peg detection
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — Underlying liquidity for collateral sales

### Wider context

- [Ethereum](/ethereum/) — Primary collateral asset
- [Stablecoins and Pegging](/inflation/) — Stablecoin mechanisms and failure modes
- [Leverage](/debt-to-equity-ratio/) — Collateral enables leverage strategies

</div>
