---
title: "Minimum Tick Size in a Futures Contract"
description: "What a tick is, how minimum tick size is defined, and how to convert one-tick moves into dollar profit and loss."
keywords:
  - minimum tick size futures contract
  - tick size futures
  - futures contract tick
  - price tick definition
  - minimum price increment
  - tick value
image: "/svg/derivatives.svg"
---

*The **minimum tick size** in a [futures contract](/futures-contract/) is the smallest allowable price increment — the smallest amount by which a futures price can change. On an S&P 500 E-mini futures contract, a tick is 0.25 index points. Understanding the tick and converting it to dollars is essential because profit and loss are always measured in tick increments.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Minimum Tick Size — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Every futures contract has a minimum price increment; tick value converts that increment to dollars.</div>

|   |   |
|---|---|
| **Definition** | Smallest allowable change in futures price |
| **Varies by** | Contract type, exchange, notional size |
| **Examples** | 0.25 S&P 500 E-mini, 0.01 crude oil, 0.0001 euro/dollar FX |
| **Tick value** | Dollar value of one tick move (contract multiplier × tick size) |
| **Practical impact** | Determines minimum profit, maximum precision, bid-ask spread |
| **Set by** | Exchange or contract specification; not negotiable |

</aside>

## What Is a Tick?

A **tick** is one minimum price movement in a futures contract. It is the granularity of price quoting and trading. Just as a stock might move in pennies ($ 0.01), a futures contract moves in ticks. The size of a tick depends on the contract.

Examples:

- **S&P 500 E-mini (ES)**: 0.25 index points
- **Crude oil (CL)**: 0.01 dollars per barrel
- **Euro/U.S. dollar (EUR/USD) futures**: 0.0001 (one basis point)
- **30-year U.S. Treasury bond (ZB)**: 1/32 of a point (0.03125)
- **Japanese yen (JY)**: 0.000001 (one one-millionth)

The tick is set by the exchange or contract specification and is not negotiable. You cannot buy or sell at a price between ticks. If crude oil is trading at $75.43 and the tick is $0.01, the next quote up must be $75.44; you cannot place an order at $75.435.

## Tick Value: Converting Ticks to Dollars

The tick alone does not tell you the profit or loss in dollars. For that, you multiply the tick by the **contract multiplier** — the size of the underlying exposure each contract represents.

**Tick Value = Tick Size × Contract Multiplier**

### Worked Examples

**S&P 500 E-mini (ES)**
- Tick size: 0.25 index points
- Contract multiplier: $50 per index point
- Tick value: 0.25 × $50 = **$12.50 per tick**

If you are long one ES contract and it moves up by one tick (0.25 points), you make $12.50. If it moves up 10 ticks (2.5 points), you make $125.

**Crude Oil (CL)**
- Tick size: $0.01 per barrel
- Contract multiplier: 1,000 barrels
- Tick value: $0.01 × 1,000 = **$10 per tick**

One tick of profit on one crude oil contract = $10. If crude moves from $75.50 to $75.85 (a move of 35 ticks), your profit is 35 × $10 = $350.

**Euro/U.S. Dollar Futures (6E on CME)**
- Tick size: 0.0001 (0.01 cents)
- Contract multiplier: 125,000 euros
- Tick value: 0.0001 × 125,000 = **$12.50 per tick**

One tick move on 6E = $12.50 profit or loss.

**U.S. Treasury 30-Year Bond (ZB)**
- Tick size: 1/32 of a point (each point is 1% of par, or $1,000 per contract)
- Contract multiplier: $100,000 face value
- Tick value: (1/32) × $1,000 = **$31.25 per tick**

(In practice, Treasury bond futures also allow sub-tick trading in halves of the minimum tick, but the minimum tick itself has this value.)

## Why Tick Size Matters

**Profit granularity**: The minimum dollar profit you can make on a single contract is one tick value. On crude oil, $10 is the smallest win. On ES, it is $12.50. Traders who scalp (hold for very short periods) may aim for 1–3 tick profits; that is their only viable profit target given transaction costs.

**Bid-ask spreads**: The bid-ask spread is quoted in ticks. A typical spread on ES might be 1–2 ticks; on crude oil, 1 tick. The bid-ask spread in dollars is the spread size (ticks) × tick value. A 1-tick spread on crude oil = $10 cost to entry; a 2-tick spread = $20.

**Transaction costs**: Every round trip (buy and sell, or sell and buy) costs the bid-ask spread plus commissions. If you make a 5-tick profit but the spread is 2 ticks, your net profit is only 3 ticks. This is why retail traders struggle: small tick values mean small spreads, but also mean small profits, and one bad trade wipes out many good ones.

**Price precision and volatility**: Contracts with very small tick sizes (like FX futures at 0.0001) appear to move in many increments; those with larger ticks (like Treasury bonds at 1/32) move in fewer visual increments. But the *economic* size of a tick should reflect the contract's typical volatility and the trader's time horizon. A tick that is too large forces traders to accept worst execution (their order is filled at a worse price because they cannot get the exact tick they want); a tick that is too small increases trading costs and does not add useful precision.

## Tick Size and Market Structure

Exchanges set tick size to balance:

- **Liquidity**: Smaller ticks allow more price discovery and tighter spreads, but can encourage high-frequency trading that destabilizes smaller players.
- **Participation**: Larger ticks make the spread easier to justify to retail traders, but may widen inefficiently.
- **Notional size**: Contracts with large multipliers (like Treasury bonds at $100,000) have larger dollar ticks to keep bid-ask spreads in reasonable dollars; FX contracts have tiny ticks because the notional size is enormous.

In 2010, the U.S. SEC experimented with tick-size changes for certain stocks. The research found that smaller ticks increased trading volume but narrowed spreads did not always improve execution for retail investors. The relationship is complex.

## Sub-Tick Trading and Fractional Shares

Modern electronic markets sometimes allow trades *between* the minimum tick. This is common in equities (fractional shares) and some Treasury futures (which allow trades in 1/64 or finer). However, the listed minimum tick is still the standard for quotes and order placement. Sub-tick trading is usually a feature for block trades or negotiated sales, not for routine orders.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the standardized agreement with a defined tick size
- [Bid-Ask Spread](/bid-ask-spread/) — the transaction cost quoted in ticks
- [Futures Contract Pricing](/futures-contract/) — why tick size affects notional exposure
- [Market Order](/market-order/) — filled at the next available tick
- [Limit Order](/limit-order/) — placed at a specific tick

### Wider context

- [Exchange](/stock-exchange/) — the entity that sets tick sizes
- [Market Maker](/market-maker-trading/) — supplies quotes and tightens spreads
- [High-Frequency Trading](/algorithmic-trading/) — sensitive to tick size and execution speed
- [Leverage Ratio Forex](/leverage-ratio-forex/) — how small ticks affect leverage in FX
- [Derivatives Hedging](/derivatives-hedging/) — professional context for futures trading

</div>