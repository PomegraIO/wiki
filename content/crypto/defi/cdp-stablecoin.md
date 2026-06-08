---
title: "CDP Stablecoin"
description: "Stablecoin minted from collateralized debt positions, backed by crypto collateral and stabilized through stability fees and liquidation."
keywords:
  - cdp stablecoin
  - collateralized debt position
  - stablecoin minting
  - stability fee
  - crypto-backed stablecoin
  - over-collateralization
image: "/svg/crypto.svg"
---

*A **CDP stablecoin** is a stablecoin minted against collateralized debt positions—a borrower deposits cryptocurrency collateral and mints new stablecoin tokens up to a collateral ratio, with the debt tracked as a position that must be repaid to recover the collateral.*

<div class="wiki-hatnote">

For the underlying lending mechanism, see [Overcollateralized Lending](/overcollateralized-lending/). For the automatic enforcement of positions at risk, see [Liquidation Mechanism](/liquidation-mechanism/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CDP Stablecoin — key facts</div>

<img src="/svg/crypto.svg" alt="An abstract editorial mark for the cryptocurrency and decentralized finance topic." />

<div class="wiki-infobox-caption">Decentralized stablecoins minted by users themselves, backed by collateral, not company reserves.</div>

|   |   |
|---|---|
| **What it is** | Stablecoin created by minting debt against cryptocurrency collateral |
| **Also called** | Collateral-backed stablecoin, crypto-backed stablecoin, synthetic stablecoin |
| **Backing mechanism** | Over-collateralized crypto deposits, not company reserves |
| **Key cost** | Stability fee (interest paid to maintain the peg) |
| **Redemption** | Burn the stablecoin and unlock the collateral |
| **Risk source** | Collateral volatility, stability fee pressure on the peg |

</aside>

## The concept: minting stablecoins from collateral

A stablecoin's core purpose is to maintain a stable value—usually pegged to a major currency like the US dollar. Conventional stablecoins (USDC, USDT) achieve this by holding dollar reserves in bank accounts; every stablecoin in circulation is backed 1:1 by dollars held in trust.

CDP stablecoins take a different approach: instead of centralized reserve backing, they are minted on-demand by users who deposit cryptocurrency collateral. A user locks 2 ETH (worth, say, $6,000) into a smart contract and mints 4,000 DAI (a CDP stablecoin). The 4,000 DAI is now circulating as currency, and the user's collateral is locked as security for that debt.

This mechanism is entirely decentralized: no company holds reserves, no bank account is needed, and minting happens peer-to-smart-contract. The trade-off is that the collateral must be substantially more valuable than the minted stablecoin—typically 150–200%—to absorb collateral price volatility and ensure the protocol remains solvent even if collateral crashes.

## Stability fees and the cost of minting

Unlike borrowing stablecoins in a traditional lending pool, minting CDP stablecoins incurs a **stability fee**—an ongoing interest rate paid by the CDP holder. If the stability fee is 5% annually, a borrower of 4,000 DAI would owe 200 DAI per year to maintain the position. The fee is usually not paid directly; instead, it accrues, increasing the debt balance automatically.

The stability fee serves two purposes:

**Incentivizing repayment**: No borrower wants debt to grow indefinitely. A meaningful fee encourages users to repay their debt (burn the stablecoin) and unlock collateral when they no longer need the borrowed stablecoins. This naturally limits the supply of circulating stablecoins.

**Defending the peg**: If the stablecoin trades below its peg (say, 1 DAI = $0.99), higher stability fees make borrowing more expensive, reducing new mint supply. Fewer new stablecoins plus organic redemptions eventually restore the peg. Conversely, if supply is constrained and the stablecoin trades above the peg (1 DAI = $1.01), the protocol can lower stability fees to encourage minting, increasing supply back to the peg.

Stability fees are typically set via governance vote, with a risk committee or community deciding the appropriate rate based on market conditions.

## Collateral tiers and risk management

CDP protocols usually accept multiple collateral types—ETH, stablecoins, governance tokens, LP tokens—each with different risk parameters. Higher-risk collateral (newer tokens, highly volatile assets) is permitted only at lower collateral ratios, meaning users can mint fewer stablecoins per dollar of collateral. Stable collateral (USDC, USDT) might allow minting at 90% ratio; volatile collateral (Ethereum) might cap at 60%; speculative tokens might be capped at 20%.

This creates a risk hierarchy: a borrower seeking maximum liquidity per collateral dollar should deposit the safest assets. Those betting on volatility accept lower borrowing capacity in exchange for exposure to appreciation.

## The incentive to maintain the peg

Multiple forces work to keep a CDP stablecoin's market price near its peg:

**Arbitrage**: If DAI trades at $0.98, arbitrageurs can buy $0.98 worth of DAI (in market), burn it to unlock collateral worth $1.50+, and profit. This buying pressure pushes DAI price back up toward the peg. Conversely, if DAI trades at $1.02, minters have an incentive to mint more (borrowing at near-peg rates and selling at a premium), increasing supply and pushing price back down.

**Redemption**: Any CDP holder can burn their stablecoins to recover collateral at a fixed rate (1 stablecoin = 1 dollar worth of collateral, assuming no accrued fees). If the market price drifts from this redemption rate, rational participants step in. This creates a price ceiling (users won't pay more than they can redeem for) and floor (users won't sell for less than they can recover).

**Governance intervention**: If the peg breaks persistently, the protocol can adjust stability fees or collateral ratios to influence supply and demand.

## Liquidation and solvency

Like all [overcollateralized lending](/overcollateralized-lending/), CDP positions face liquidation if collateral value falls below a threshold. If ETH price drops 30%, a position that was adequately collateralized at 160% might fall to 112%, triggering liquidation. The collateral is seized, auctioned, and the proceeds repay the stablecoin debt. Any surplus goes to the original CDP holder.

Liquidation protects the protocol: it ensures every stablecoin in circulation remains backed by sufficient collateral. Without liquidation, a prolonged bear market could leave the protocol insolvent—more stablecoins owed than collateral value backing them.

## Dai as the archetype

MakerDAO's Dai is the most prominent CDP stablecoin, having circulated since 2015 with a track record of maintaining its peg through volatile markets. Dai's architecture includes:

- Multiple collateral types (ETH, USDC, Link, etc.), each with distinct risk parameters
- Stability fees voted on by MKR (Maker) governance token holders
- A "Stability Fund" that absorbs small losses and protects the peg temporarily
- Regular collateral audits and risk assessments

Other protocols (Liquity, Aave's GHO, Curve's crvUSD) offer CDP stablecoins with variations in collateral acceptance, fee structures, and governance models. Most have failed to achieve significant scale relative to Dai, often because network effects favor the largest stablecoin (better liquidity, deeper trading pairs, wider acceptance) and because Maker's early-mover advantage is difficult to overcome.

## Risks and limitations

CDP stablecoins are not risk-free:

**Collateral concentration**: If most CDPs are collateralized with Ethereum, a crash in Ethereum triggers cascading liquidations, potentially causing system-wide insolvency if collateral value drops faster than liquidations can execute.

**Stability fee spiral**: During bear markets, stability fees may need to rise sharply to defend the peg, making minting prohibitively expensive and shrinking the collateral base just when the protocol needs it most.

**Liquidation cascades**: If many CDPs liquidate simultaneously, the auction of seized collateral can depress its price, triggering further liquidations and potentially undercollateralizing the protocol.

**Governance risk**: Decisions on stability fees and collateral parameters are made via token holder votes, which can be manipulated by large holders or executed poorly by a dispersed community.

Despite these risks, CDP stablecoins remain valuable because they are truly decentralized, require no trust in a company's reserves, and allow borrowers to mint stablecoins on-demand without identity verification or credit assessment.

## See also

<div class="wiki-seealso">

### Closely related

- [Overcollateralized Lending](/overcollateralized-lending/) — the underlying mechanism for CDP collateral management
- [Liquidation Mechanism](/liquidation-mechanism/) — how the protocol enforces collateral ratios
- [Yield Aggregator](/yield-aggregator/) — strategies that deposit stablecoins into lending protocols
- [Distributed Ledger](/distributed-ledger/) — the blockchain enabling these automated protocols
- [Cryptocurrency Exchange](/cryptocurrency-exchange/) — where CDP stablecoins are traded and arbitraged

### Wider context

- [Stablecoin](/stablecoin/) — the broader category of price-stable cryptocurrencies
- [Interest Rate](/interest-rate/) — the stability fee as a floating cost of capital
- [Monetary Policy](/monetary-policy/) — how governance adjusts stability fees to influence supply

</div>
