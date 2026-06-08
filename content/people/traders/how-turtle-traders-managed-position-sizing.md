---
title: "How the Turtle Traders Managed Position Sizing"
description: "The ATR-based unit sizing formula Richard Dennis taught his Turtles and why volatility-adjusted sizing was central to the system's edge."
keywords:
  - turtle traders position sizing
  - how turtle traders managed position sizing
  - atr position sizing formula
  - volatility-adjusted position sizing
  - trend following position size
image: "/svg/people.svg"
---

*The Turtle Traders, a group of novices trained by commodities legend Richard Dennis in the 1980s, proved that a mechanical [trend-following](/trend-following/) system could beat the market. But the system's edge rested as much on *how much* to bet as on *when* to buy. Dennis taught them to size every position by the volatility of the underlying asset—measured by Average True Range (ATR)—so that a wild commodity contract and a tame bond future risked the same dollar amount per unit. This simple idea transformed a mediocre system into a profitable one.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Turtle position sizing — key facts</div>

<img src="/svg/people.svg" alt="An abstract editorial mark for people and traders." />

<div class="wiki-infobox-caption">Risk per trade stays flat; volatility shrinks or grows the position size to match.</div>

|   |   |
|---|---|
| **Core metric** | ATR (20-day Average True Range); a volatility measure |
| **Sizing rule** | Position size = Fixed dollar risk / ATR; smaller ATR = bigger position |
| **Outcome** | Same dollar risk across all trades; no oversized bets on quiet markets |
| **Key insight** | Volatile trades require smaller units; calm markets allow bigger units |
| **Risk management** | Caps [drawdown](/market-cycle/) by keeping volatility risk constant |
| **Contrast with fixed shares** | Buying 100 shares of every stock risks wildly different amounts; ATR-adjusted sizing normalizes risk |

</aside>

## The volatility problem

Before Turtles, most traders either bought a fixed number of shares or a fixed dollar amount. A trader might buy 100 shares of every stock, or $10,000 of every position. But this ignores volatility. A $10,000 position in a sleepy utility—moving ±$50 per week—faces vastly less risk than $10,000 in a biotech—moving ±$500 per week. Over the same holding period, the biotech could wipe out 10x more capital. A system that doesn't account for this is flying blind.

Dennis saw this clearly. His Turtle system was purely mechanical: enter long on a 20-day breakout, exit on a 10-day breakdown, apply a stop loss. By itself, this rule set was not remarkable. The innovation was sizing. Dennis taught the Turtles to measure each market's volatility and adjust the position size so that **a 2% ATR move would cost the same dollar amount across all positions**.

This was elegant. It meant that a crude oil contract—volatile, swinging 50 cents per barrel—would be traded in much smaller units than a gold contract—less volatile per unit. A single unit of corn (5,000 bushels) could be sized smaller than 100 shares of Coca-Cola if corn was more volatile. The Turtles would adjust position size every day, as ATR changed, staying in sync with market turbulence.

## The ATR calculation and the unit formula

ATR is straightforward to compute. For each day:

1. Calculate the true range: max( High - Low, |High - Prior Close|, |Low - Prior Close| )
2. Average the true range over the past 20 days.

ATR is not volatility in the statistical sense ([standard deviation](/concentration-risk/) of returns), but it's correlated and simpler to calculate by hand in the 1980s. A stock moving ±$2 per day has an ATR around $2–3. A stock moving ±$10 per day has an ATR around $10–15.

The Turtle position size formula was:

**Position size = (2% of account) / ATR**

If a trader had a $1 million account, the 2% risk was $20,000. If the ATR of crude oil was $0.50 per barrel, each position in crude was 40,000 barrels (20,000 ÷ 0.50). If the ATR of natural gas was $0.03 per unit, the position was 667,000 units (20,000 ÷ 0.03). Smaller ATR meant bigger position.

The beauty: a 2% adverse ATR move on any position cost roughly $20,000—the same max loss per trade. This **normalized risk across all markets**, so the system didn't blow up on the quiet ones and didn't starve on the volatile ones.

## Why this works: mean reversion and trend capture

Volatility and trend interact in non-obvious ways. A market in a strong trend often shows high volatility; a range-bound market shows low volatility. By sizing inversely to volatility, the Turtles captured a natural adjustment:

- In a calm market (low ATR), they were overweight, ready to ride a trend if one started.
- In a whipsaw market (high ATR), they were underweight, protecting capital from false breakouts.

This sounds like market timing, but it's not—it's *time-invariant risk management*. The system did not try to predict volatility; it simply matched position size to current volatility, so that risk stayed constant.

Also, trend-following systems need scale to work. A 1-year trend move of 20% looks the same in a market that moved ±1% daily and one that moved ±5% daily. The system enters on the same signal; the volatility-adjusted sizing ensures that it commits enough capital to capture the trend while managing the day-to-day noise.

## A worked example

Suppose you have a $100,000 account and two markets: Stock A and Commodity B.

- Stock A has an ATR of $4. Position size = $2,000 / $4 = 500 shares.
- Commodity B has an ATR of $0.20 per unit. Position size = $2,000 / $0.20 = 10,000 units.

If both trade against you by one ATR move:
- Stock A loses: 500 shares × $4 = $2,000.
- Commodity B loses: 10,000 units × $0.20 = $2,000.

Same loss, same risk, across two wildly different assets. If you had instead bought 500 shares of both, and Commodity B swung $0.40 against you, you'd lose $4,000 on Commodity B and only $2,000 on Stock A—an unequal risk.

## Adjusting as volatility changes

The Turtles recalculated ATR and position size regularly, often daily. If a market's volatility spiked (ATR doubled), the position size halved immediately. If volatility collapsed (ATR fell), the position size grew. This meant the system was always hedge-fund-like: dynamic, responsive, not stale.

This daily recalculation also protected against a subtle trap: leverage by accident. A trader who buys a fixed number of shares when the market is calm, then watches volatility explode, is suddenly over-leveraged without intending to be. Turtle sizing prevented this. As volatility rose, position size fell, [drawdown](/market-cycle/) risk stayed bounded.

## The edge: risk management over prediction

Dennis believed (and the Turtles proved) that the edge in trading is not predicting market direction—it's managing risk and capturing large moves. The Turtle system was not high-win-rate; it had many small losses and a few large wins. But because position sizing was risk-aware, the large wins paid for the losses and returned profit.

A naive trend follower might buy 100 shares of every breakout, lose money overall, and blame the system. The same system, with volatility-adjusted sizing, could turn profitable. The difference is pure [portfolio management](/asset-allocation/): giving capital to the trades that matter (the ones in line with risk appetite) and starving the ones that don't.

## Modern variants

Today, [risk parity](/asset-allocation/) funds use similar logic: instead of holding 60% stocks and 40% bonds (which is 90% of volatility in stocks), they hold an equal dollar amount of [beta](/beta/) across stocks, bonds, commodities, and other assets. The math is the same: size positions inversely to volatility.

Algorithmic trading firms use volatility-adjusted position sizing as standard. A [machine learning](/algorithmic-trading/) model might predict direction, but the trade size is still capped by volatility to keep [value at risk](/value-at-risk/) constant. The Turtles' insight became industry orthodoxy.

## See also

<div class="wiki-seealso">

### Closely related

- [Trend following](/trend-following/) — the entry and exit logic Turtles used
- [Average True Range (ATR)](/implied-volatility/) — the volatility metric powering the sizing
- [Risk parity](/asset-allocation/) — modern extension of volatility-adjusted sizing
- [Drawdown](/market-cycle/) — what ATR sizing constrains
- [Leverage](/leverage-ratio-forex/) — ATR sizing as a way to prevent leverage surprises
- [Value at risk](/value-at-risk/) — the risk metric position sizing controls

### Wider context

- [Portfolio management](/asset-allocation/) — the larger framework for sizing decisions
- [Market maker](/market-maker-trading/) — who the Turtles were competing against
- [Commodities](/crude-oil/) — the primary markets Turtles traded
- [Volatility smile](/volatility-smile/) — how market volatility varies
- [Backtesting](/momentum-investing/) — how the system was validated

</div>
