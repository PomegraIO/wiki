---
title: "Mean Reversion Strategy"
description: "A trading approach betting that asset prices or spreads will revert toward their historical average after deviating from it."
keywords:
  - mean reversion
  - statistical arbitrage
  - price reversion
  - trading strategy
  - market inefficiency
  - pairs trading
---

*A **mean reversion strategy** is a trading approach based on the statistical observation that asset prices, spreads, or volatility tend to drift back toward their historical average after moving sharply away from it. Traders bet against large moves, positioning themselves to profit when the market reverses.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Mean Reversion Strategy — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Profit from temporary departures from historical norms.</div>

|   |   |
|---|---|
| **Core principle** | Prices deviate from averages; reversion captures the return move |
| **Opposite view** | [Momentum investing](/value-investing/) — assumes trends continue |
| **Time horizon** | Days to months (short to intermediate) |
| **Key metrics** | Standard deviation, historical mean, z-score, Bollinger Bands |
| **Markets** | Stocks, [bonds](/bond/), forex, commodities, spreads |
| **Risk** | The asset may not revert; regime shifts break the pattern |

</aside>

## The logic behind reversion

Markets occasionally overshoot. Fear or euphoria drives a stock 30% above its justified value, or a commodity crashes on temporary supply news. Mean reversion strategies treat these extremes as opportunities: the trader identifies the historical range and places bets that prices will snap back.

The intuition is sound in many cases. If a stock's ten-year median price is £40, and it suddenly trades at £55 on irrational hype, statistical gravity suggests it will fall. The strength of this effect varies. In liquid, efficient markets like major [equity indices](/sp-500-index/), reversions are quick and modest. In less-traded securities or [illiquid spreads](/credit-spread/), departures from the mean persist longer, offering wider windows for trades.

## Standard tools: bands, z-scores, and pairs

Traders typically measure deviation using **Bollinger Bands** — upper and lower bands drawn two standard deviations above and below a moving average. When a price touches the upper band, it signals overextension; touching the lower band suggests underextension. The strategy is then to sell near the upper band and buy near the lower.

A **z-score** approach formalises this: calculate how many standard deviations the current price sits from its mean. A z-score of +3 suggests extreme overvaluation; −3 suggests extreme undervaluation. Positions are entered at extreme z-scores, betting on mean reversion.

**[Pairs trading](/merger/)** is a popular multi-asset variant. Find two historically correlated stocks — say a retailer and its supplier. When the spread between them widens beyond normal (one rallies while the other falls), short the outperformer and buy the underperformer, assuming their normal relationship will be restored. This approach reduces market [beta](/beta/) risk because long and short positions offset broad market moves.

## Why reversion works—and fails

Mean reversion works best when the deviation is driven by noise or temporary factors. A dividend announcement momentarily lifts a stock beyond its fundamentals; a seasonal shortage pushes oil higher; a liquidity crisis widens [credit spreads](/credit-spread/) beyond fair value. In each case, the deviation is self-correcting.

Reversion fails when the "mean" itself has shifted. What looks like an overshoot may actually be a new, justified level. A company improving its operations, a structural shortage of natural resources, or a [sector rotation](/sector-rotation/) away from technology can all look like temporary extremes but are in fact regime changes. The trader who bets on reversion into a broken old mean loses money.

Market regimes also matter. During [bull markets](/bull-market/), stocks overshoot to the upside more often and recover more slowly than to the downside. Mean reversion strategies can be whipsawed in trending markets, where a price "deviation" actually continues in the same direction. A trader shorting a stock climbing from £30 to £60 because £45 is the historical mean will suffer losses as the mean itself shifts upward.

## Risks and practical limits

**Regime risk** tops the list. If the market regime changes, the historical mean becomes irrelevant. A strategy that prospers in stable, mean-reverting conditions can collapse when [volatility](/implied-volatility/) spikes or when structural factors redefine fair value.

**Liquidity risk** arises when trying to scale. A reversion trade on an illiquid spread may require large positions to justify transaction costs; if the market moves against the trade before reversion occurs, exits become expensive or impossible.

**Timing risk** is the trader's constant torment. Even if you are right that a price will revert, you may be wrong about when. A stock may stay "overextended" for months before snapping back. Capital tied up in a losing position earns no [return](/return-on-assets/), and [opportunity cost](/cost-of-equity/) mounts.

**Correlation breakdown** threatens pairs trades. Two stocks that historically moved together can diverge for months or years if fundamentals diverge. The trader assumes reversion; instead, the divergence persists.

## Modern and classical versions

Classical mean reversion looks simple: identify a statistic (price, spread, volatility), measure its historical mean and variance, and trade when it deviates beyond a threshold. Modern variants layer in [machine learning](/algorithmic-trading/), regime-detection filters, and hedging overlays to reduce the chances of betting on a broken mean.

Some traders combine mean reversion with [momentum](/alpha/) signals—buying oversold assets that show signs of stabilisation, or selling overbought assets that show signs of rolling over. This hybrid approach tries to catch reversion early while filtering for cases where the old regime is likely to hold.

## When to use it

Mean reversion strategies thrive in low-[volatility](/historical-volatility/), range-bound markets where prices oscillate around a stable centre. They are natural fits for traders with short to intermediate time horizons—days to a few months. Retail traders favour simple Bollinger Band or z-score rules. Institutional traders scale them via [quantitative strategies](/factor-investing/) and leverage.

The strategy demands discipline: you must define your mean, your entry threshold, and your exit rule *before* you trade. Ad-hoc decision-making turns a statistical edge into a gamble.

## See also

<div class="wiki-seealso">

### Closely related

- [Alpha](/alpha/) — excess return driven by skill or an exploitable edge, the goal of mean reversion trades
- [Momentum investing](/value-investing/) — the opposing thesis that trends continue, not revert
- [Volatility smile](/volatility-smile/) — persistent deviations from option-pricing models; a target for mean-reversion arbitrage
- [Algorithmic trading](/algorithmic-trading/) — modern platforms where mean reversion rules are automated
- [Beta](/beta/) — systematic market risk; mean reversion trades often try to isolate specific assets or spreads from broad beta
- [Statistical arbitrage](/factor-investing/) — the broader field of trading price relationships using quantitative models

### Wider context

- [Market maker trading](/market-maker-trading/) — provides liquidity but may adjust spreads in anticipation of reversion
- [Sector rotation](/sector-rotation/) — shifts in which asset classes outperform; can trap mean-reversion traders who assume stable relationships
- [Business cycle](/business-cycle/) — economic expansions and contractions; regimes that shift what "mean" values look like
- [Leverage ratio forex](/leverage-ratio-forex/) — borrowed capital used to scale mean-reversion positions
- [Value investing](/value-investing/) — longer-term philosophy that undervalued assets revert upward over years

</div>
