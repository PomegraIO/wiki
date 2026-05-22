---
title: "Bull Spread (Call)"
description: "Multi-leg options strategy combining a long call and short higher-strike call to reduce upfront cost and cap profit potential."
keywords:
  - bull spread call
  - call spread
  - vertical spread
  - limited-risk options strategy
---

*A **Bull Spread (Call)** is a [derivative](/wiki/derivative-accounting-hedging/) strategy that combines a long [call option](/wiki/call-option/) at a lower strike price with a short call at a higher strike price, both with the same expiration date. The strategy reduces the upfront [premium](/wiki/option-premium/) cost compared to a naked long call, while sacrificing unlimited upside potential in exchange for a defined maximum profit and known maximum loss.*

<aside class="wiki-infobox">

| Component | Detail |
|---|---|
| **Long Leg** | Buy call at lower strike (A) |
| **Short Leg** | Sell call at higher strike (B) |
| **Net Premium Outlay** | Debit (cost to enter) |
| **Max Profit** | Strike B − Strike A − Net Premium |
| **Max Loss** | Net Premium Paid |
| **Breakeven** | Long Strike + Net Premium |
| **Time Decay** | Negative (short call benefits you) |
| **Implied Volatility** | Mixed effect (long and short offsets) |

</aside>

## Why sell premium to finance a call

The bull call spread addresses a key problem: long calls are expensive. If an [at-the-money (ATM)](/wiki/at-the-money/) call costs $3 and the underlying is moving slowly, you lose money to [theta](/wiki/theta-option-greeks/) (time decay) even if you're right about direction. By selling an out-of-the-money (OTM) call at a higher strike, you collect [premium](/wiki/option-premium/) that offsets your long call's cost. For example, you might buy a $100 call for $3 and sell a $110 call for $1.50, netting a debit of $1.50 instead of $3. The tradeoff: if the stock rallies to $115, your profit is capped at $10 − $1.50 = $8.50 instead of $15. Most of the time, though, the stock doesn't rocket that far, so the reduction in cost provides better risk-adjusted returns.

## The defined-risk profile

Unlike a naked long call, which has theoretically unlimited loss (the premium paid) and unlimited upside, the bull spread is completely hedged. Your maximum loss is the net debit paid, and your maximum gain is the difference between the strikes minus the debit. This two-dimensional bounded outcome makes the bull spread popular with traders who want directional bullish exposure but with known, manageable risk. For a trader with a $10,000 account, knowing that a single position can lose, say, $300 maximum (the net debit), allows for precise [position sizing](/wiki/position-limit-regulations/) and [portfolio risk management](/wiki/risk-management/).

## Implied volatility and vega effects

The bull spread has a blended [vega](/wiki/vega-option-greeks/) (volatility sensitivity): you are long vega on the lower-strike call and short vega on the higher-strike call. If [implied volatility](/wiki/implied-volatility/) increases, the long call gains more value than the short call (because the long call is lower-strike and has more vega exposure in absolute terms), so the spread benefits from an [implied volatility spike](/wiki/volatility-smile/). Conversely, if volatility collapses, the spread loses. This is why bull call spreads are often preferred in low-volatility environments where you expect the stock to rise moderately but volatility to remain range-bound. In a [black swan](/wiki/black-swan/) event, where volatility spikes alongside a downside move, the spread suffers from both directional loss and negative gamma.

## Practical strike selection and cost

Strike selection depends on your bullish conviction and cost tolerance. A wide spread (e.g., $100 / $110 call) costs less to enter than a tight spread (e.g., $100 / $102 call), but has lower profit per dollar risked. Some traders use spreads where the higher strike is at or slightly out of the money, betting that the stock will reach that level but not exceed it. Others use very tight strikes (1–2 percentage points apart) for situations where they expect a modest move and want to maximize the probability of maximum profit. The [risk-reward ratio](/wiki/risk-parity-strategy/) is a key decision variable.

## Comparison to other spread strategies

The bull call spread is one variant of a **[vertical spread](/wiki/vertical-spread/)** — a multi-leg strategy using two options at different strikes on the same underlying, with the same expiration. A **[bear call spread](/wiki/bear-call-spread/)** is the opposite: selling a lower-strike call and buying a higher-strike call, creating a bearish position with defined risk. A **[bull put spread](/wiki/bull-put-spread/)** uses put options instead of calls but has the same bullish directional bet. The four combinations (bull call, bull put, bear call, bear put) form a complete suite of [vertical spread](/wiki/vertical-spread/) strategies. Each has subtle differences in [theta](/wiki/theta-option-greeks/) and [vega](/wiki/vega-option-greeks/) behavior that make them preferable in different market regimes.

## Breakeven and probability of profit

The breakeven price is the lower strike plus the net premium paid. For a $100 / $110 spread with a $1.50 net debit, breakeven is $101.50. The probability of profit (POP) is the probability the stock closes above breakeven at expiration. For a $1.50 debit in a $100 stock, the breakeven is 1.5% above the current price — a relatively high probability of success, especially if the stock is expected to drift upward. However, high POP comes with low reward: the maximum profit is only $8.50 on a $1.50 risk, a 5.67:1 reward-to-risk ratio. The formula is: the wider the spread, the more premium collected, the lower the cost, but the higher the cap on profit.

## Rolling and adjustment

Many traders use bull spreads as part of a dynamic strategy, rolling the spread as the underlying moves or as expiration approaches. If the stock shoots up past the upper strike, some traders will "roll up" the spread — closing the original spread and opening a new one at higher strikes — to capture additional upside. Conversely, if the stock falls and is heading toward maximum loss, rolling to a lower strike or extending the expiration can sometimes salvage the trade. Rolling requires careful attention to transaction costs and tax implications.

## Common use cases

Bull call spreads are popular in several contexts. A trader might use them to reduce the cost of establishing a directional position in a stock they expect to rise modestly. A portfolio manager might layer them on top of a long stock position as a way to generate income (the short call premium) while capping upside — an income-generating strategy. Options traders sometimes use them as a [carry trade](/wiki/carry-trade/) on very liquid names, where the debit is small and the probability of max profit is high, allowing them to manage many such spreads simultaneously.

## Expiration behavior and gamma

As expiration approaches, [gamma](/wiki/gamma-option-greeks/) increases, meaning prices change more rapidly near the strike prices. A bull spread that is close to the upper strike may swing dramatically in the final days: a small upward move pushes it to max profit, a small downward move drops it well below max. This makes the final week of a bull spread's life both risky and opportunity-rich for traders who want to actively manage positions.

<div class="wiki-seealso">

### Closely related
- [Call Option](/wiki/call-option/) — the long leg
- [Bear Call Spread](/wiki/bear-call-spread/) — the inverse directional strategy
- [Bull Put Spread](/wiki/bull-put-spread/) — bearish variant using puts
- [Vertical Spread](/wiki/vertical-spread/) — the general category

### Wider context
- [Option Premium](/wiki/option-premium/) — cost and credit dynamics
- [Greeks](/wiki/options-greeks/) — [delta](/wiki/delta-option-greeks/), [gamma](/wiki/gamma-option-greeks/), [vega](/wiki/vega-option-greeks/) behavior
- [Implied Volatility](/wiki/implied-volatility/) — affects spread profitability
- [Options Clearing Corporation](/wiki/options-clearing-corporation/) — settlement and regulation

</div>
