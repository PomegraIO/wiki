---
title: "Maintenance Margin"
description: "Maintenance margin is the minimum account equity required to keep a position open, with a margin call issued if equity falls below it."
keywords:
  - maintenance margin
  - margin call
  - minimum equity
  - futures trading
  - risk control
image: "/svg/derivatives.svg"
---

*The **maintenance margin** is the minimum account equity required to maintain an open [futures contract](/futures-contract/) or short option position. It is typically set at 70–80% of the [initial margin](/initial-margin/). If daily [mark-to-market](/mark-to-market/) losses cause account equity to fall below maintenance margin, the broker issues a **margin call**, requiring the trader to deposit additional funds immediately or close positions. Maintenance margin enforces discipline and reduces counterparty risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maintenance Margin — key facts</div>

<img src="/svg/derivatives.svg" alt="Account equity declining toward maintenance margin" />

<div class="wiki-infobox-caption">Maintenance margin triggers forced action when breached.</div>

|   |   |
|---|---|
| **Percentage** | Typically 70–80% of initial margin |
| **Trigger** | Margin call when equity falls below this |
| **Action required** | Deposit funds or close position immediately |
| **Set by** | Exchange/clearing house, broker may require higher |
| **Varies with** | Contract volatility, market conditions |
| **Cushion** | Space between initial and maintenance |
| **During stress** | Requirements rise, cushion shrinks |
| **Liquidation risk** | Breaching means forced exit at bad prices |
| **Account monitoring** | Daily via mark-to-market settlement |

</aside>

## Maintenance margin mechanics

Example:
- Initial margin: $5,000
- Maintenance margin: $3,500 (70%)
- Trader deposits: $5,000
- Account equity starts: $5,000
- Daily loss: −$2,000 (price moves against trader)
- Remaining equity: $3,000

The equity of $3,000 is **below** maintenance margin ($3,500). Margin call issued immediately. Trader must deposit $500 to restore equity to $4,000 (above maintenance), or close the position.

## The margin call process

1. Exchange notifies broker that account is below maintenance.
2. Broker notifies the trader (typically after market close).
3. Trader must deposit funds or close position **before next market open** (or same day depending on broker rules).
4. If trader does not act, broker automatically liquidates positions (forcibly closes them) at market prices.

Forced liquidations can occur at terrible prices if the market gaps overnight or liquidity is thin.

## Cushion between initial and maintenance

The gap between initial margin ($5,000) and maintenance margin ($3,500) is the **cushion** ($1,500). This cushion gives the trader room to absorb losses before facing a margin call.

In normal markets, this cushion is sufficient. During crises (high volatility, gap moves), the cushion can evaporate quickly.

## Margin call consequences

A margin call forces the trader to:
1. **Deposit cash immediately** (depletes cash reserves)
2. **Close positions** at market prices (may lock in losses)
3. **Liquidate other assets** (sells stocks, bonds to raise cash)

This is why traders must understand their leverage and margin risk.

## Variation across brokers and exchanges

Exchanges set **minimum** maintenance margin requirements. Individual brokers often require higher margins (more conservative). A trader might see:
- Exchange minimum: 70% of initial
- Broker requirement: 75% of initial

The broker's requirement is what matters.

## Portfolio-level margin

Large, institutional traders with diversified portfolios may have **portfolio margin**, where maintenance is calculated on the portfolio's aggregate risk rather than per-contract. This can reduce margins significantly.

## See also

<div class="wiki-seealso">

### Closely related

- [Initial margin](/initial-margin/) — cushion starts here
- [Futures contract](/futures-contract/) — subject to maintenance margin
- [Mark-to-market](/mark-to-market/) — daily calculation triggering calls
- [Margin call](/mark-to-market/) — triggered when equity falls below maintenance
- [Liquidation](/stock-market/) — forced if call not met

### Risk management

- Leverage — creates margin risk
- [Position sizing](/asset-allocation/) — relates size to account
- [Stop loss](/stock-market/) — limiting loss before margin call
- [Account monitoring](/stock-market/) — daily equity tracking

### Broker and exchange

- [Clearing house](/stock-exchange/) — sets margin requirements
- [Broker](/broker/) — enforces maintenance margin
- [Forced liquidation](/stock-market/) — consequence of breaching

### Deeper context

- [Derivative](/option/) — the family of instruments
- [Risk control](/hedge-fund/) — maintenance margin is critical
- [Trading](/stock-market/) — leverage and margin essential to understand

</div>
