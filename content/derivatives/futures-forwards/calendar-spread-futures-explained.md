---
title: "Calendar Spread Futures Explained"
description: "A calendar spread in futures buys one contract expiry and sells another, profiting from changes in the price curve between maturities."
keywords:
  - calendar spread futures explained
  - futures calendar spread strategy
  - calendar spread profitability
  - curve trading futures
image: /svg/derivatives.svg
---

*A **calendar spread in futures** is a strategy where you simultaneously buy a contract expiring in one month and sell a contract expiring in another month, typically of the same commodity. Rather than betting on absolute price direction, you profit from shifts in the gap between the two maturities—the [curve](/yield-curve/) structure—allowing traders to harvest the shape of the futures market itself.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Calendar Spread Futures — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Pure curve exposure: you win if the spread you sold contracts relative to the spread you bought.</div>

|   |   |
|---|---|
| **Structure** | Long far-month contract + short near-month contract |
| **Profit driver** | Narrowing or widening of the [contango](/contango/) or [backwardation](/backwardation/) spread |
| **Market outlook** | Neutral on spot price; bullish on curve flattening (or bearish on steepening) |
| **Leverage** | Typically lower [margin](/margin-call-forex/) requirement than outright directional trades |
| **Typical hold** | Weeks to months; often closed before the near-month expires |

</aside>

## The basic setup and mechanics

Suppose crude oil trades as follows:

| Expiry  | Price    |
|---------|----------|
| 1-month | $85.00   |
| 3-month | $87.00   |

The spread is $2.00 in [contango](/contango/). You execute a calendar spread by:
1. **Selling** the 1-month contract at $85.00
2. **Buying** the 3-month contract at $87.00

You are short the spread at $2.00. Your P&L is tied entirely to how that $2.00 changes, not whether crude oil goes to $80 or $90.

Two weeks later, the market shifts. The 1-month is now $86.50, and the 3-month is $87.50. The spread has narrowed to $1.00. You close the trade:
- Buy back the short 1-month at $86.50 (loss of $1.50)
- Sell the long 3-month at $87.50 (gain of $0.50)
- Net loss: $1.00

You made money because the spread contracted, even though crude rallied overall. You were "short the spread," and tightening is profitable for shorts.

## When calendar spreads are profitable

Calendar spreads profit when the curve reshapes in your favor. The core conditions are:

**Contango flattening**: You sell the front month (high contango) and buy the back month (lower contango). If the curve flattens—the premium for carrying contracts forward shrinks—both legs move closer together. Your short gains more than your long loses.

**Backwardation steepening**: You buy the front month (high backwardation, i.e., low price) and sell the back month (less backwardation). If backwardation deepens—the inversion widens—your long gains more than your short loses.

**Storage and financing changes**: If carrying costs fall (interest rates drop, or storage becomes cheaper), [contango](/contango/) contracts. Spreads narrow. A trader short contango wins. This happens frequently in commodities when central banks ease or supply pressures ease.

**Supply or demand shocks at one maturity**: A supply outage might spike the front-month contract far more than far-months, widening the backwardation and tightening contango. A calendar spread trader who is positioned correctly captures this revaluation.

## The relationship to contango cost for long holders

Calendar spreads are the inverse of the [contango cost for long futures holders](/contango-cost-for-long-futures-holder/). Passive long investors roll and lose; calendar spread traders harvest that same move. When contango persists, speculators deliberately short near-term and long far-term to profit. This activity is what keeps the curve from steepening infinitely.

## Margin efficiency and risk

Calendar spreads typically require less margin than outright directional positions because the two legs partly offset. Instead of posting margin for a full long position, you might post margin on only the net difference. However, the trade is not riskless.

If the curve steepens sharply—contango expanding instead of contracting—both legs can move against you in absolute terms. The front-month might tank while the back-month holds up, widening the spread in the opposite direction. You lose on both ends.

The trade also has *rolling risk*. As the near-month contract approaches expiry, liquidity concentrates in the front contract, and the spread can become volatile or hard to exit cleanly.

## Common applications

**Commodities with stable contango**: Crude oil, natural gas, heating oil, and agricultural futures in normal conditions maintain steady contango. Traders systematically short contango spreads, betting curve shapes remain anchored. This is a low-risk, high-frequency strategy for systematic traders.

**Anticipating supply or demand shifts**: A trader who believes storage costs will fall (contango will tighten) might short the spread. One who expects a supply squeeze (backwardation will deepen) might long the spread, buying near and selling far.

**Curve positioning**: Asset managers use calendar spreads to express views on the shape of the curve without betting on spot prices. This is useful when volatility in absolute levels is high but the curve structure is stable.

## Risks and execution pitfalls

- **Liquidity gaps**: Far-month contracts can trade with wider bid-ask spreads. Execution costs can erase small profits.
- **Expiry mismatch**: If you are long July and short May, you must close or roll the May position before it expires. Forced rolling in adverse conditions kills the trade.
- **Curve steepening**: If contango expands (not contracts), your short position loses money, and you exit at a loss.
- **Storage shocks**: An unexpected storage facility outage or geopolitical event can dislocate the curve in ways the model doesn't predict.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — the normal structure calendar spreads often exploit
- [Backwardation](/backwardation/) — the inverted curve; calendar spreads profit when it changes
- [Contango Cost for Long Futures Holders](/contango-cost-for-long-futures-holder/) — the flip side of the same market dynamic
- [Futures Contract](/futures-contract/) — the instrument enabling these strategies
- [Spread](/bid-ask-spread/) — the concept of buying one asset and selling another
- [Derivatives Hedging](/derivatives-hedging/) — why hedgers also use spreads to reduce cost

### Wider context

- [Futures Margin Call Mechanics](/futures-margin-call-mechanics/) — capital requirements for spread positions
- [Forward Contract vs Futures Contract](/forward-contract-vs-futures-contract/) — understanding expiry mechanics
- [Price Discovery](/price-discovery/) — how trading spreads reveals true curve value
- [Momentum Investing](/momentum-investing/) — related to riding curve reshaping trends

</div>
