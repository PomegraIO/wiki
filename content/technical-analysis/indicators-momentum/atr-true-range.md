---
title: "ATR True Range"
description: "Average True Range measures volatility based on the largest of intraday moves and gaps, widely used for position sizing and stop placement."
keywords:
  - ATR volatility
  - true range
  - technical indicators
  - volatility measure
  - position sizing
---

*The **Average True Range (ATR)** is a technical indicator that quantifies volatility by averaging the "true range"—the largest of the intraday high-low span, gap-open distance, or gap-close distance. ATR is used by traders to size positions, set stop-loss levels, and identify regime shifts without making directional bets.*

<div class="wiki-hatnote">For broader volatility measures, see [Historical Volatility](/wiki/historical-volatility/) and [Implied Volatility](/wiki/implied-volatility/).</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| Definition | Average of true range over N periods |
| True range | Max(high − low, |high − prior close|, |low − prior close|) |
| Default period | 14 days (for daily charts) |
| Interpretation | Higher ATR = higher volatility |
| Use | Position sizing, stop-loss placement, volatility regime |
| Scaling | Absolute (dollar amount) and percentage-based |
| Lag | Lags current volatility due to averaging |

</aside>

## What true range captures

The **true range** for a single bar is the largest of three measurements:

1. **Intraday range**: High − Low (the bar's trading span).
2. **Gap up**: |High − Prior Close| (how far the bar opened above yesterday's close).
3. **Gap down**: |Low − Prior Close| (how far the bar opened below yesterday's close).

Example: Suppose XYZ stock closed yesterday at $100, opens today at $102, trades between $101 and $105, then closes at $103.

- Intraday range: $105 − $101 = $4
- Gap up: |$105 − $100| = $5
- Gap down: not applicable (it gapped up, not down)

**True range = $5** (the largest).

Without the gap component, you'd only measure intraday volatility. By including gaps, true range captures the market's overnight sentiment shifts—news, earnings, geopolitical events. This is why ATR is more useful than simple high-low ranges for traders.

## Calculating ATR

**Step 1**: Calculate true range for each of the past N periods (usually 14 days).

**Step 2**: Average the true ranges.

$$\text{ATR} = \frac{\sum_{i=1}^{N} \text{TrueRange}_i}{N}$$

Some traders use an **exponential moving average** (EMA) instead of a simple average, to weight recent volatility more heavily:

$$\text{ATR}_{EMA} = \alpha \times \text{TrueRange} + (1-\alpha) \times \text{ATR}_{EMA,prev}$$

Where α = 2/(N+1).

## ATR as a volatility signal

ATR can be used to measure regime changes:

- **Rising ATR**: Volatility is expanding. This often signals the start of a [trend](/wiki/trend-following/) (uptrend or downtrend) or the approach of a significant event (earnings, Fed decision).
- **Declining ATR**: Volatility is contracting. Markets are in a "quiet" period; breakouts are less likely, and support/resistance lines are tighter.
- **Extreme high ATR**: Panic or euphoria; reversal may follow as participants exhaust themselves.
- **Extreme low ATR**: Boredom; likely to end in volatility expansion.

A trader watching a 14-period ATR might use a historical percentile approach: "ATR is in the 90th percentile of the past year = extreme volatility; I'll size smaller positions." Or conversely, "ATR in 10th percentile; unusual for this stock; big move coming."

## Position sizing with ATR

Many professional traders use ATR for **risk-based position sizing**. The idea:

$$\text{Position Size} = \frac{\text{Account Risk Tolerance}}{\text{ATR} \times \text{Dollar Value per Unit}}$$

Example:
- You're willing to risk $500 on this trade (1% of a $50k account).
- ATR on stock XYZ is $2.50 (14-day average true range).
- Each share is worth $100.
- Position size = $500 / ($2.50 × 100) = 2 shares.

This ensures that if price moves against you by one ATR, you lose exactly your target amount. If price moves two ATRs, you lose 2× target. This is rational: in a low-volatility stock, you can hold larger positions; in a high-volatility stock, you hold smaller positions for the same risk.

## Setting stop losses with ATR

A trader using ATR-based stops might place stops **N × ATR away from entry**. If ATR is $2 and you enter long at $100, you might place a stop at:

- $100 − (2 × $2) = $96 (two ATRs below entry), or
- $100 − (1 × $2) = $98 (one ATR below entry).

The advantage: stops are dynamic. In a volatile period, ATR rises, and stops widen automatically. In a calm period, ATR falls, and stops tighten. This avoids being whipsawed by false breakouts but also avoids stops that are too tight to give the trade room to breathe.

## ATR drawbacks

1. **Lag**: ATR is an average; it lags the current volatility. If volatility spikes suddenly, ATR hasn't caught up yet.
2. **Non-directional**: ATR doesn't tell you *which way* price will move, only that volatility is high. You need other tools for direction.
3. **Period sensitivity**: A 14-period ATR might miss longer-term volatility patterns. Traders often look at multiple ATR periods (14, 30, 60-day) simultaneously.
4. **Gap insensitivity in quiet markets**: If a stock never gaps, ATR becomes just the average high-low range, losing its edge.

## ATR in different markets

**Equities**: ATR works well; gaps and earnings moves are common, so the gap component is meaningful.

**Forex**: ATR is useful, but forex trades 24 hours, so "daily" gaps are less dramatic. Traders often use hourly ATR for intraday moves.

**Futures**: ATR is essential; futures gap on open regularly due to overnight news and global events.

**Cryptocurrencies**: 24/7 trading, but gaps occur between exchange settlement periods. ATR is useful but must account for exchange-specific schedules.

## ATR and mean reversion vs. trend following

**Trend followers** use rising ATR as a signal that a trend is beginning and size up. **Mean-reversion traders** use rising ATR as a signal that price has moved too far and is about to snap back; they bet on reversal.

The same indicator, opposite interpretation. This is why ATR is a volatility measure, not a directional signal—you supply the directional hypothesis.

## Combining ATR with other indicators

Traders often pair ATR with:

- **[RSI](/wiki/rsi-relative-strength/)**: High ATR + RSI > 70 = volatile uptrend (risky); high ATR + RSI < 30 = capitulation (potential reversal).
- **[Moving averages](/wiki/moving-average/)**: Low ATR + price near 50-day moving average = low-risk entry; high ATR + price far from moving average = overextended.
- **[Bollinger Bands](/wiki/bollinger-bands/)** (which are based on standard deviation, not ATR, but conceptually similar): Narrow bands + rising ATR = breakout imminent.

<div class="wiki-seealso">

### Closely related
- [Historical Volatility](/wiki/historical-volatility/) — statistical volatility measure
- [Implied Volatility](/wiki/implied-volatility/) — option market volatility
- [Moving Average](/wiki/moving-average/) — trend component
- [RSI Relative Strength](/wiki/rsi-relative-strength/) — momentum indicator
- [Support and Resistance](/wiki/support-and-resistance/) — level placement

### Wider context
- [Technical Analysis](/wiki/technical-analysis/) — discipline
- [Trend Following](/wiki/trend-following/) — strategy type
- [Mean Reversion Investing](/wiki/mean-reversion-investing/) — opposing strategy
- [Risk Management](/wiki/position-limit-regulations/) — position sizing

</div>
