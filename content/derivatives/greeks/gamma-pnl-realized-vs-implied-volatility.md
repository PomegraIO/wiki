---
title: "Gamma P&L: Realized vs Implied Volatility"
description: "Gamma P&L arises when realized volatility exceeds implied volatility. Learn how long-gamma traders profit from daily rebalancing and delta hedging."
keywords:
  - gamma pnl
  - realized volatility
  - implied volatility
  - option greeks
  - gamma trading
  - delta hedging
image: /svg/derivatives.svg
---

*A long **gamma P&L** trader profits when the underlying asset moves more than the [option](/option/) market priced in—specifically, when **realized volatility** exceeds the [implied volatility](/implied-volatility/) baked into the [option premium](/option-premium/) paid. The edge comes from rebalancing the [delta](/delta/) hedge daily, capturing the volatility whipsaw.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Gamma P&L — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">The core mechanism: buy an option cheap (low IV), hope the stock moves big, rehedge often to lock in profits.</div>

|   |   |
|---|---|
| **Profit when** | Realized volatility > Implied volatility |
| **Loss when** | Realized volatility < Implied volatility |
| **Key lever** | Rehedge frequency (daily, hourly, continuous) |
| **Depends on** | Option Greeks: [gamma](/gamma/), [theta](/theta/), spot move |
| **Time decay** | Long gamma bleeds [theta](/theta/) if market sits still |
| **Typical setup** | Buy straddle or strangle; delta-hedge; rebalance |
| **Who does it** | Volatility traders, market makers, prop shops |

</aside>

## How Realized vs. Implied Volatility Creates Profit

When you buy an option, you pay a premium that reflects the market's expectation of future price moves. That expectation is encoded in [implied volatility](/implied-volatility/) (IV). If the stock moves more violently than IV predicted, and you have [gamma](/gamma/) (the right to buy or sell at predetermined strikes), you capture that excess movement—profit.

Here's the mechanism: buying a call or put gives you [gamma](/gamma/), which means your delta (directional exposure) increases or decreases as the spot price changes. When you rehedge by selling stock (if the price rose and your call is now further ITM) or buying stock (if it fell), you lock in a small profit on each move. If the stock keeps twitching, you keep rehedging and accumulating gains. Over the holding period, those rehedging profits add up.

Conversely, if the stock trades sideways and implied volatility was high, you bleed [theta](/theta/) (time value decay) without collecting volatility profits. Gamma and theta are at odds: gamma pays off movement; theta punishes standing still.

## A Worked Example: Five-Day Straddle

Imagine you buy a five-day straddle on a stock trading at $100:
- **Buy 1 call** at the 100 strike for $2.00
- **Buy 1 put** at the 100 strike for $1.80
- **Total premium paid**: $3.80 (this is the [implied volatility](/implied-volatility/) bet)
- **Implied volatility on these options**: 25% annualized

You are now long [gamma](/gamma/), meaning you profit from moves in either direction if you rehedge daily.

**Day 1**: Stock rallies to $101.50. Your call is now worth $2.30 (gross); your put is worth $1.00. Net position value: $3.30. You are down $0.50 from the premium paid—but your [delta](/delta/) is now positive (roughly +0.65 on the call, -0.35 on the put, net +0.30). You sell 30 shares at $101.50 to delta-hedge.

**Day 2**: Stock drops to $100.80. Your call falls to $2.10; your put rises to $1.60. Net position value: $3.70. You have now made back the Day 1 loss and gained $0.10. Your [delta](/delta/) is now slightly negative (roughly +0.40, -0.55, net -0.15). You buy back 15 shares at $100.80 to rebalance.

The profit on the hedge is:
- Sold 30 shares at $101.50 = +$3,045
- Bought 15 shares at $100.80 = -$1,512
- Net rehedge profit: +$33

This $33 came from the stock moving while you rehedged. If the stock moved $2 on Day 1 and $0.70 on Day 2, realized volatility (measured over the holding period) will be higher than the 25% IV you paid. Keep rehedging through Day 5, and if realized volatility beats 25%, the sum of all rehedging profits exceeds the time decay, and you exit with a gain.

## Why Daily Rehedging Matters

The frequency of rehedging is critical. Here's why:

**Continuous rehedging** (hourly, or theoretically every infinitesimal move) allows you to harvest every twitch. The math becomes elegant: your P&L is proportional to the difference between realized and implied variance over the holding period.

**Daily rehedging** is a practical compromise. You capture most moves but miss intra-day whipsaws. If the stock rallies $1 in the morning and sells off $0.80 by close, a daily rehedger sees the net $0.20 move; an hourly trader captures both legs.

**Weekly or less frequent rehedging** leaves money on the table. You miss gamma profits when you don't rebalance after large moves. This is why market makers rehedge multiple times per day.

## The Math: Realized vs. Implied Variance

The formal relationship is:

**Gamma P&L ≈ 0.5 × (Realized Variance − Implied Variance) × Gamma × Notional**

In plain English: if realized volatility (squared, to get variance) exceeds the implied variance you paid for, and you have gamma, you profit. The more gamma you own (shorter-dated, at-the-money options have high gamma), the larger the payoff for each unit of volatility surprise.

Over a five-day hold:
- Realized variance = the actual daily moves, squared and averaged
- Implied variance = (0.25)² = 0.0625, or 6.25% daily variance
- If actual variance turns out to be 0.08 (roughly 28% annualized), you profit
- If it's 0.04 (roughly 20% annualized), you lose

## Long-Gamma vs. Short-Gamma Tradeoffs

**Long gamma (buy options)**: You profit from realized volatility beating implied. You lose [theta](/theta/) if the market is quiet. You want big moves. Used by volatility traders betting the market is sleeping. Risk: if nothing moves, you bleed time value.

**Short gamma (sell options, like a market maker)**: You collect [theta](/theta/) (time decay) if the market is quiet. You lose if realized volatility explodes. You want the market flat or calm. Used by dealers trying to pocket bid-ask spread plus time decay. Risk: a surprise gap or spike can blow up the position.

Most firms run both: traders with bullish vol forecasts run long gamma; dealers run short gamma and hedge with long-dated options.

## Practical Constraints on Gamma P&L

**Transaction costs and bid-ask spread.** Each rehedge incurs a tiny slippage. On a tight bid-ask, this is negligible; on wide spreads, it adds up. For the strategy to work, the realized volatility gain must exceed rehedging friction.

**Borrow costs and dividends.** If you are long a call and short 100 shares to delta-hedge, you owe borrow fees on the short stock. On a dividend-paying stock, you collect dividends on the short—it's a wash. On growth stocks with high borrow rates, the cost can eat into gamma profits.

**Jump risk.** Gamma P&L assumes continuous rehedging. A gap move—a stock opening down 10% overnight—means you cannot rehedge in between. You suffer a loss on the mismatch between your option delta and your hedge. This is why volatility traders fear earnings reports and geopolitical shocks.

**Implied volatility surface shifts.** The example above assumes IV stays at 25%. If IV suddenly drops to 20%, your option value falls even if the stock doesn't move. This is [vega](/vega/) risk, orthogonal to gamma.

## See also

<div class="wiki-seealso">

### Closely related

- [Gamma](/gamma/) — the rate of delta change; core to the rehedging profit
- [Delta](/delta/) — position directional exposure; what you rehedge
- [Theta](/theta/) — time decay; the cost of holding long gamma
- [Implied Volatility](/implied-volatility/) — the market's volatility expectation you bet against
- [Vega](/vega/) — sensitivity to IV level changes
- [Black-Scholes Model](/black-scholes-model/) — theoretical framework for option pricing

### Wider context

- [Option](/option/) — the underlying contract and its Greeks
- [Derivatives Hedging](/derivatives-hedging/) — broader hedging strategies
- [Volatility Smile](/volatility-smile/) — IV varies by strike and maturity
- [Historical Volatility](/historical-volatility/) — realized volatility measurement

</div>
