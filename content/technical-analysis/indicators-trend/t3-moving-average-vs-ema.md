---
title: "T3 Moving Average vs EMA: Smoothness and Lag Trade-Off"
description: "Contrasts Tillson's T3 multiple-EMA construction against a standard EMA, examining lag reduction and overshoot, and which trend conditions favor each."
keywords:
  - t3 moving average
  - ema comparison
  - trend indicator
  - moving average smoothing
  - lag vs responsiveness
image: /svg/technical-analysis.svg
---

*The **T3 moving average**, invented by Tillson in the 1990s, applies multiple exponential smoothing passes to eliminate lag and reduce whipsaw. A standard **EMA** (exponential moving average) responds quickly but overshoots trend reversals. The T3 trades some responsiveness for smoother, more reliable signals in choppy and sideways markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">T3 vs EMA — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">T3 smooths out false breakouts at the cost of minor lag.</div>

|   |   |
|---|---|
| **EMA construction** | Single exponential moving average, one smoothing pass |
| **T3 construction** | Four nested EMAs applied sequentially (cascaded) |
| **T3 lag** | Slightly higher than standard EMA |
| **T3 smoothness** | Substantially lower noise and fewer whipsaws |
| **Best for EMA** | Trending markets; quick reversals; mean reversion |
| **Best for T3** | Range-bound markets; reducing false signals |

</aside>

## The Core Difference: Single vs. Multiple Smoothing

A standard exponential moving average weights recent prices more heavily than past prices. The EMA formula is simple:

**EMA = (Current Price × Alpha) + (Previous EMA × (1 – Alpha))**

Where Alpha = 2 / (N + 1), and N is the period (e.g., 14 for a 14-period EMA).

The T3, by contrast, runs this calculation four times in sequence. The output of the first EMA becomes the input of the second EMA, and so on. This cascading effect dramatically smooths the line and eliminates much of the noise that causes whipsaws in raw EMA signals.

Conceptually:

- **EMA**: One pass, direct price response  
- **T3**: Four passes, each one smoothing what came before

## Why Smoothing Reduces Lag (Counterintuitively)

This seems backwards—wouldn't more smoothing create more lag? In fact, the opposite is true in terms of signal quality. A noisy EMA oscillates erratically, causing traders to enter and exit on false breaks. The EMA *appears* responsive but is actually lagging behind the true trend because the noise drowns out the signal.

The T3 eliminates that noise, so when it finally crosses or breaks a level, the signal is far more likely to coincide with an actual trend shift. The T3 "waits" longer than the EMA to confirm, but when it moves, it moves with conviction. The EMA moves first but then retraces frequently. Over a full cycle, the T3 often has less real-world lag.

## The Trade-Off: Smoothness vs. Responsiveness

There is a genuine trade-off. In a fast, trending market where prices move in a sustained direction, an EMA will align with the trend sooner than a T3. If you are trading a strong uptrend, a 14-EMA might cross above price on day 2; a T3 might not cross until day 4 or 5. In that scenario, the EMA is ahead.

But in a choppy market with false breakouts, the EMA whips back and forth. A trader using the EMA exits on the first reversal, only to be stopped out before the real trend resumes. The T3, by filtering the noise, avoids those false signals. Over 100 trades, the T3 often wins despite being "slower" on individual moves.

The practical choice depends on market regime:

- **Strong trend (hourly, daily bars):** EMA is better for early entry. The cost of the occasional whipsaw is outweighed by catching the move sooner.
- **Range-bound / choppy (15-min, hourly bars):** T3 is better for filtering out noise. Fewer but higher-quality signals.
- **Swing trading (daily bars):** T3 often outperforms because noise in daily bars is reduced without much lag penalty.

## Practical Calculation: The Stacking Process

To calculate a T3 with period 14:

1. **EMA1** = 14-period EMA of closing prices  
2. **EMA2** = 14-period EMA of EMA1  
3. **EMA3** = 14-period EMA of EMA2  
4. **EMA4** = 14-period EMA of EMA3  
5. **T3** = EMA4

Some traders also apply a volume-weighted variant or adjust the intermediate period. The adjustment parameter *a* (typically 0.7) scales the lag:

**T3 = EMA1 – 3a×EMA2 + 3a²×EMA3 – a³×EMA4**

This adjustment formula reshapes the curve and can reduce lag further at the cost of introducing minor oscillation. Most trading platforms that offer T3 use a simplified cascade (EMA of EMA of EMA of EMA) without the adjustment.

## When Each Wins: Concrete Examples

**EMA in a trending market:**  
- Price: steady uptrend with no pullbacks  
- 14-EMA crosses above price on bar 3 → entry signal  
- T3 does not cross until bar 7  
- EMA catches more of the move  
- Outcome: EMA advantage

**T3 in a choppy market:**  
- Price: tight range, three breakout attempts, all false  
- 14-EMA crosses above the range on bars 3, 5, 9 → three whipsaw exits  
- T3 does not cross until bar 12 (final real breakout)  
- Outcome: T3 advantage (1 trade, no losses vs. 3 trades, 2 losses)

## Implementation Tips

Many charting platforms (TradingView, Thinkorswim, MetaTrader) offer T3 as a built-in indicator. If not, use a 4× cascade of standard EMA. Period selection works similarly to EMA: shorter periods (5–10) for scalpers, medium periods (14–21) for swing traders, longer periods (50–200) for position traders.

Some traders blend EMA and T3—using the T3 for primary trend and the EMA for entry timing. When both align, conviction is high. When they diverge, it signals a choppy or transitional market.

## Limitations of Both

Neither the EMA nor the T3 leads price consistently. Both are lagging indicators. In a sideways market with no trend, both generate whipsaws. A price that oscillates around the moving average is inherently difficult to trade; no amount of smoothing removes the fundamental lack of directional momentum.

Also, the T3's smoothing comes at a cost in fast, volatile intraday markets. If you are trading 5-minute bars, the T3 may be too slow to catch quick reversals. The EMA, despite its noise, may be more appropriate.

## See also

<div class="wiki-seealso">

### Closely related

- [Moving Average](/moving-average/) — foundation for both EMA and T3
- [Exponential Moving Average](/exponential-moving-average/) — the basic building block of T3
- [Trend Following](/trend-following/) — strategy that profits from moving average signals
- [Support and Resistance](/support-and-resistance/) — how moving averages act as dynamic levels
- Indicator — broader class of technical tools

### Wider context

- Technical Analysis — discipline in which moving averages are used
- [Price Discovery](/price-discovery/) — what moving averages reflect
- [Volatility Smile](/volatility-smile/) — related to price noise and smoothing
- Mean Reversion — contrasts with trending, affects indicator choice

</div>
