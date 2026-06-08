---
title: "Mean Reversion Trading"
description: "A statistical trading strategy that profits from price movements that stray far from historical averages, betting they will return to normal levels."
keywords:
  - mean reversion
  - statistical arbitrage
  - price normalization
  - momentum reversal
  - volatility trading
  - short-term trading
image: "/svg/strategies.svg"
---

*A **mean reversion trader** assumes that extreme price movements—far above or below historical norms—are temporary dislocations that eventually correct. The strategy enters positions to capture the snap-back, betting that volatility spikes or sentiment-driven rallies will give way to equilibrium.*

## What makes prices drift away from historical norms

Markets are efficient most of the time, but not always. Panic selling, euphoric rallies, algorithmic cascades, or supply shocks can push prices well beyond what historical variance alone would predict. When a stock rallies 30% in three days or a currency pair hits a 10-year high on speculation, the absolute level diverges from the statistical center of gravity established over months or years.

Mean reversion traders view these extremes as opportunities. They identify a "normal" range—typically via moving averages, standard deviation bands, or quantile-based thresholds—and bet that any movement beyond it is self-correcting. The logic is simple: a 50-year flood in a stock's valuation is unlikely to be permanent.

## How mean reversion traders measure extreme

The most common tools are **Bollinger Bands**, which plot moving averages plus and minus two standard deviations of price. When a stock touches or crosses the upper band, a mean reversion signal fires: sell. When it hits the lower band, buy. A trader might also look at **RSI (Relative Strength Index)** readings—values above 70 or below 30 suggest overbought or oversold conditions.

Another approach is [value-investing](/value-investing/) logic applied to the short term: if a stock's [price-to-earnings-ratio](/price-to-earnings-ratio/) shoots to 50x when the historical median is 15x, the trader expects compression. Some use [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) models to identify intrinsic value, then assume prices within two standard errors of that estimate will snap back if they breach it.

What separates mean reversion from [value-investing](/value-investing/) is the holding period. A value investor might hold for years waiting for the market to recognize the company's worth. A mean reversion trader holds days or weeks, banking on statistical reversion within a near-term window.

## The edge and the pitfall

If historical distribution of prices is stable and regime shifts are rare, mean reversion works. A stock trading at 10% above its 200-day average is genuinely overbought if volatility is normal. The trader captures the inevitable pullback without waiting for a fundamental change.

But this strategy fails dramatically during [trend](/business-cycle/) shifts. If a company releases a breakthrough earnings report, its "normal" range jumps permanently higher. Selling into the early rally, expecting reversion, means fighting a new equilibrium. The 2008 financial crisis and COVID-era volatility saw mean reversion traders wiped out as what looked like 3-sigma moves became 6-sigma regime breaks. **Most economists** who study mean reversion emphasize that it works in stationary price regimes; some argue it's dangerously naive in periods of structural change.

## Pairs trading and statistical arbitrage

A related and more robust variant is **pairs trading**: identifying two correlated assets that have diverged. If Apple and Microsoft normally move together, but Apple has fallen 15% while Microsoft is flat, a trader might buy Apple and short Microsoft, betting on convergence. This approach is market-neutral—it doesn't bet on direction, only on the gap closing—and avoids the regime-shift trap by focusing on relative value rather than absolute thresholds.

[Hedge funds](/hedge-fund/) and proprietary trading desks use this heavily. It requires careful calibration: the correlation must be genuine, not spurious, and the divergence must be in the tail of the historical distribution.

## Speed and execution challenges

Mean reversion is a crowded trade. A stock hits an extreme, dozens of algorithmic traders fire sell orders simultaneously, and the reversion happens in seconds. Retail traders face delays: by the time you see the signal and place the order, the move has already partially reversed. [Bid-ask-spread](/bid-ask-spread/) widens at extremes, eating into tight profit margins.

Execution costs matter enormously. If you're trading a stock that swings 3% in a day expecting a 2% reversal, friction and slippage often consume the gain. Professional mean reversion traders lean on high-frequency infrastructure or trade liquid, low-spread instruments—major equity indices, [major currency pairs](/currency-risk/), or [futures-contracts](/futures-contract/).

## Blending with fundamental catalysts

The strongest mean reversion traders don't rely on statistics alone. They look for fundamental reasons the price has stretched. A company misses earnings and the stock drops 20%—extreme by statistical measures, but does the business model survive? Or a geopolitical shock spikes oil prices 15% in a day; is it likely to reverse within a week, or is that the new price floor?

Combining [technical analysis](/price-discovery/) signals (bands, RSI) with a lightweight fundamental check—earnings quality, balance-sheet health, industry dynamics—improves the odds. This hybrid approach sidesteps pure statistical reversion traps by asking whether the extreme is really irrational.

## See also

<div class="wiki-seealso">

### Closely related

- [Momentum Trading](/momentum-trading/) — the opposite bet: buying strength, not fighting it
- [Contrarian Trading](/contrarian-trading/) — fading consensus sentiment rather than chasing statistical extremes
- [News Trading](/news-trading/) — profiting from price gaps around scheduled events
- [Volatility Smile](/volatility-smile/) — why implied volatility at extremes doesn't match historical patterns
- [Value Investing](/value-investing/) — long-term reversion to fundamental value
- [Bid-Ask Spread](/bid-ask-spread/) — why execution costs are critical to short-horizon trading

### Wider context

- [Price Discovery](/price-discovery/) — how markets establish true value
- [Market Maker Trading](/market-maker-trading/) — who captures reversion profits at scale
- [Algorithmic Trading](/algorithmic-trading/) — automation of mean reversion strategies
- [Tail Risk](/tail-risk/) — why statistical tails can be thicker than normal-distribution models assume

</div>
