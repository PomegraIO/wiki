---
title: "McClellan Oscillator"
description: "Exponential moving average of breadth indicator showing market momentum via advance-decline divergence."
keywords:
  - McClellan oscillator
  - breadth momentum
  - advance-decline line
  - market internals
  - technical indicator
---

*The McClellan Oscillator is a technical indicator derived from market breadth data—the difference between the number of advancing and declining stocks. It applies exponential moving averages to this difference to smooth noise and signal market momentum. Divergences between the oscillator and price indices (e.g., S&P 500 rising while oscillator falls) warn of weakening market participation and potential reversals.*

<aside class="wiki-infobox">

| Item | Details |
|------|---------|
| **Data source** | Daily advances minus declines (NYSE or NASDAQ) |
| **Calculation** | EMA(19 days) minus EMA(39 days) of advance-decline difference |
| **Interpretation** | Positive: breadth gaining; negative: breadth deteriorating |
| **Signal** | Divergences with price index warn of trend reversals |
| **Timeframe** | Intraday to weeks |
| **Complementary metric** | [Advance-decline line](/wiki/market-breadth-advances-declines/); [breadth thrust](/wiki/breadth-thrust-indicator/) |

</aside>

## Market breadth and the advance-decline difference

Market breadth measures how many individual stocks are advancing (price up) versus declining (price down) on a given day. If the S&P 500 rises but only 60% of NYSE stocks advance, breadth is weak. If 90% advance, breadth is strong. The advance-decline difference (advances minus declines) quantifies this imbalance.

A healthy bull market sees broad participation: indices rise, and a large percentage of individual stocks rise too. A weak bull market sees narrow participation: indices rise but driven by a handful of mega-cap stocks (e.g., the "Magnificent Seven" tech names in 2023), while the broader market stagnates. The McClellan Oscillator captures this distinction by converting breadth data into a momentum signal.

## Calculation and interpretation

The McClellan Oscillator applies a 19-day exponential moving average (EMA) and a 39-day EMA to the daily advance-decline difference. The oscillator = EMA(19) – EMA(39). The 19 and 39-day periods are arbitrary but standard; some traders use different periods for shorter or longer time horizons.

Positive values indicate upside momentum in breadth; the short-term (19-day) trend is above the longer-term (39-day) trend, signaling accelerating breadth. Negative values indicate downside momentum in breadth; breadth is deteriorating.

Extreme positive values (oscillator > 500 or so) can signal overbought breadth—participation is so strong that a pullback may occur. Extreme negative values (oscillator < -500) can signal oversold breadth—participation is so weak that a reversal may be imminent.

## Divergence as a warning signal

The power of the McClellan Oscillator lies in detecting divergences between price and breadth. If the S&P 500 reaches new highs while the McClellan Oscillator is falling or at lower levels than prior peaks, breadth is deteriorating even as the index rises. This divergence warns that the rally is narrowing and vulnerable to reversal.

Historically, major market peaks are often preceded by breadth deterioration. As the final leg of a bull run plays out, a handful of expensive mega-cap stocks chase the index higher while the broader market lags. The McClellan Oscillator declines, flagging this weakness to observant traders.

Similarly, at market bottoms, the oscillator may find a low while the index is still falling. This positive divergence—breadth improving while price is still declining—can signal an imminent reversal and a buying opportunity.

## Breadth thrust indicator

Closely related is the [Breadth Thrust Indicator](/wiki/breadth-thrust-indicator/), which flags when the oscillator rises from negative to positive territory rapidly. A breadth thrust signals that the market is transitioning from breadth deterioration to acceleration, and often precedes sustained rallies. Historical data shows breadth thrusts are followed by outsized gains over the subsequent months.

## Market internals and technical analysis

The McClellan Oscillator is one of several [breadth indicators](/wiki/market-breadth-advances-declines/) used in technical analysis. Others include the [advance-decline line](/wiki/market-breadth-advances-declines/) (cumulative sum of advances minus declines), [new highs/new lows](/wiki/new-highs-new-lows/) counts, and [volume-based indicators](/wiki/accumulation-distribution-line/). Together, these "market internals" provide texture to price movements and help assess the authenticity of rallies or declines.

A strong uptrend backed by positive market internals (improving breadth, rising new highs, rising volume) is more likely to be durable. A price rally accompanied by deteriorating breadth and declining volume is fragile.

## Application in trading and portfolio management

Retail traders use the McClellan Oscillator to time entries and exits. A positive divergence at a market bottom (price low, oscillator high and rising) can trigger a buy. A negative divergence at a price high (price high, oscillator rolling over) can trigger a sell or reduction.

Institutional portfolio managers monitor breadth as a macro signal. If breadth is deteriorating despite price strength, they may reduce exposure or hedge. If breadth is improving, they may increase exposure or reduce hedges, confident in market participation.

## Limitations and cyclicality

The McClellan Oscillator is backward-looking, like all technical indicators. It identifies trends already in motion, not reversals before they occur. False signals are common; the oscillator can oscillate between positive and negative for weeks without a clear trend emerging.

Also, the indicator depends on advance-decline data, which varies by index. NYSE-based calculations differ from NASDAQ-based ones (NASDAQ is technology-heavy and shows different breadth dynamics). Traders must choose consistently.

## Relationship to market cycles and sentiment

Breadth weakening is often correlated with rising [volatility](/wiki/fear-index/) and declining investor sentiment. As uncertainty increases, institutional investors reduce position sizes and rotate into defensive stocks, narrowing the breadth of participation. The McClellan Oscillator picks up these rotations before price indices reflect them fully.

During [regime changes](/wiki/market-regime-momentum/) — transitions from bull to bear or vice versa — the oscillator often leads. It deteriorates before price declines (warning) and improves before price rebounds (opportunity).

## Integration with other indicators

The McClellan Oscillator is most powerful when used alongside other indicators. Combining it with [momentum indicators](/wiki/momentum-investing/) (MACD, RSI), [support and resistance](/wiki/support-and-resistance/) levels, and [volume analysis](/wiki/accumulation-distribution/) creates a more robust decision framework. A divergence flagged by the oscillator is more credible if supported by divergence in other indicators.

<div class="wiki-seealso">

### Closely related
- [Market Breadth](/wiki/market-breadth-advances-declines/) — Advancing vs. declining stocks
- [Breadth Thrust Indicator](/wiki/breadth-thrust-indicator/) — Signal of breadth acceleration
- [Advance-Decline Line](/wiki/market-breadth-advances-declines/) — Cumulative breadth metric
- [New Highs/New Lows](/wiki/new-highs-new-lows/) — Participation signal

### Wider context
- Technical Analysis — Price and volume-based analysis
- [Momentum Investing](/wiki/momentum-investing/) — Trend-following approach
- [Market Regime](/wiki/market-regime-momentum/) — Shifts in market character
- [Volatility Index](/wiki/fear-index/) — Fear and sentiment gauge

</div>