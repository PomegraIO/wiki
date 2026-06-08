---
title: "Coppock Curve for Long-Term Trend Reversals"
description: "The Coppock Curve detects major bear-market bottoms using weighted rate-of-change momentum. Designed for monthly data, it struggles on short timeframes."
keywords:
  - coppock curve long term trend reversal
  - coppock curve indicator
  - buy signal bear market
  - rate of change momentum
  - long-term bottom detection
  - monthly oscillator
---

*The **Coppock Curve for long-term trend reversal** is a weighted rate-of-change oscillator originally designed to signal the end of bear markets and the start of new bull phases. It combines two ROC periods (typically 11 and 14 months) and applies a 10-period weighted moving average, producing a smooth oscillator that cycles from deeply negative (capitulation) to positive (conviction). It excels at identifying secular turning points but is nearly useless on intraday or short-term charts.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Coppock Curve — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">A long-period oscillator for major trend reversals, not short-term trades.</div>

|   |   |
|---|---|
| **Design timeframe** | Monthly bars (original); daily/weekly adaptations exist |
| **Formula** | Weighted MA of (ROC11 + ROC14) over 10 periods |
| **Optimal use** | Detecting end of bear markets, secular bottoms |
| **Lag** | 10+ bars on monthly, ~2–3 months in real time |
| **Key signal** | Curve crosses zero from negative = buy (bear ending) |
| **False-signal rate** | Low on monthly; very high on intraday |
| **Peak finding** | Can identify major trend exhaustion (negative extremes) |
| **Timeframe suitability** | Monthly, weekly; daily only with risk |

</aside>

## The history and design intent

The **Coppock Curve** was created by E.S. Coppock in the 1960s specifically to time the purchase of common stocks after a bear market. The original intent was to answer a single question: *When has selling pressure exhausted and the next bull market begun?*

Coppock observed that **major bear-market bottoms occur when fear is at its peak**—when the rate-of-change has turned deeply negative. At that inflection point, a trader could enter with confidence. The indicator was calibrated for monthly charts, where trend reversals are clear and whipsaws are rare.

The Coppock Curve has remained largely unchanged because it works well for its original purpose. It is not a general-purpose momentum indicator and should never be treated as one.

## The formula: weighted ROC with lagged smoothing

The **Coppock Curve calculation** is straightforward:

1. Calculate **ROC(11)** = 11-period rate of change = ((Close − Close 11 bars ago) / Close 11 bars ago) × 100
2. Calculate **ROC(14)** = 14-period rate of change
3. Sum: **ROC(11) + ROC(14)**
4. Apply **10-period weighted moving average** (WMA) to the sum

The WMA weights recent values more heavily than older ones, smoothing the raw ROC sum into a flowing curve. The result oscillates around zero, going deeply negative during sell-offs and positive during strong rallies.

On a monthly S&P 500 chart, the Coppock typically dips to −15% to −40% at major bottoms (March 2009, March 2020) and rises to +5% to +15% during sustained bulls. These extremes are roughly symmetrical, making the zero line a reliable pivot.

## Reading the Coppock: the key signals

### Zero crossing (buy signal)

The **classic Coppock buy signal** is when the curve **crosses zero from below** (from negative to positive). This marks the moment when the fear-driven selling has reversed and positive momentum is building.

On a monthly chart, this signal is remarkably reliable for identifying the start of new bull phases:
- **March 2009** (financial crisis bottom): Coppock crossed zero and a 10-year bull began.
- **March 2020** (COVID panic): Coppock crossed zero and the subsequent rally lasted years.
- **October 2002** (tech bubble bottom): Coppock zero cross preceded a major multi-year recovery.

The signal is delayed—the actual month-end bottom may occur 1–2 bars before the Coppock crosses zero—but it provides high confidence for long-term entry.

### Extreme negative values (capitulation flag)

When the Coppock dips deeply negative (below −20% on monthly data), it signals **capitulation**—exhaustion of selling pressure. Traders who recognize the pattern can begin scaling into positions even before the curve crosses zero. The extreme itself indicates that a reversal is likely within 1–3 months.

### Divergence with price

If price makes a new low but the Coppock is less negative than at a previous low, **bearish divergence** has formed. This often precedes a rally even before the zero cross. For example, price may drop 5% but the Coppock stays flat or improves—a signal that selling is running out of steam.

## Why Coppock fails on short timeframes

Applying the **Coppock Curve to intraday or hourly charts** is a common mistake. The formula's 11- and 14-period moving averages lose all their power on short timeframes:

- **5-minute chart with 11/14 bars:** That is only 55–70 minutes of history. The oscillator becomes noisy and uncorrelated with meaningful reversals.
- **Hourly chart with 11/14 bars:** That is 11–14 hours. Still too short to capture institutional positioning shifts.
- **Daily chart with 11/14 bars:** 11–14 days is closer to meaningful, but still short for a bear-market reversal signal.

The original 11- and 14-month periods were chosen because they approximated the market's business cycle frequency. Shrinking the timeframe without adjusting the periods breaks the indicator. Some traders attempt "daily Coppock" by using 11 and 14 days—an improvement, but still inferior to monthly versions.

## Adapting Coppock for weekly and daily use

If you must use Coppock on shorter timeframes, some traders adjust the periods:

- **Weekly Coppock:** Use ROC(8) + ROC(11) with 10-period WMA. Signals are more frequent and less reliable but occasionally useful for confirming multi-week trends.
- **Daily Coppock:** Use ROC(5) + ROC(7) with 10-period WMA. Whipsaws increase significantly, but can flag daily capitulation.

These adaptations produce faster signals but trade away the robustness that made the original monthly version famous. If you are using a 5/7 daily Coppock, you are using a different indicator than the original Coppock Curve and should test it thoroughly before deploying real capital.

## Coppock with other long-term indicators

**Coppock + Market regime:**
Many institutional traders combine Coppock zero crosses with other macro indicators. A Coppock zero cross is stronger if it coincides with:
- **Federal Reserve pivot** (shifting from tightening to easing).
- **Yield curve recovery** (from inverted to positive slope).
- **Credit spreads widening** (high-yield spreads contracting as fear subsides).

**Coppock + valuation:**
A Coppock zero cross at historically cheap valuations (P/E below 15, dividend yield above 3%) is more reliable than at expensive valuations. The signal says momentum is turning, but valuation context tells you if the reversal will stick.

**Coppock + sector leadership:**
If the Coppock crosses zero but defensive sectors are outperforming cyclicals, conviction is lower. True bull reversals see cyclical sectors (materials, energy, technology) outpace utilities and staples. Monitoring sector relative strength alongside Coppock confirms the reversal.

## Limitations and caveats

**Long lag in real-time trading:** On monthly data, a zero cross may not appear until 2–3 bars after the actual market bottom. For a day trader or swing trader, this lag is fatal. You have already made or lost significant capital by the time the signal appears.

**Crowded at bottoms:** Because Coppock is famous for bear-market timing, many institutions use it. This can create a "self-fulfilling prophecy" where the signal gets bought aggressively, driving up price. Conversely, false signals (Coppock crosses zero but price continues lower) can cause sharp reversals that stop out underprepared traders.

**No overbought signal:** The indicator excels at finding bottoms but does not reliably identify tops. A Coppock reading of +15% does not mean "sell"—rallies have run higher without mean-reverting. Some traders use the most recent extreme positive Coppock value as a ceiling, but this is ad hoc.

**Structural market changes:** The original Coppock was calibrated to 1960s equity markets. Algorithmic trading, index funds, and macroeconomic policy regimes have changed. Modern bottoms may look different than the extremes Coppock was designed for. Always cross-check with current market context.

## See also

<div class="wiki-seealso">

### Closely related

- Rate of change — Momentum foundation of Coppock formula
- [Moving average](/moving-average/) — Smoothing mechanism within the curve
- RSI indicator — Alternative momentum oscillator (but designed for overbought/oversold)
- MACD — Another trend-momentum hybrid

### Wider context

- [Trend-following](/trend-following/) — Long-term strategy Coppock supports
- [Bear market](/bear-market/) — Historical context for the indicator's design
- [Business cycle](/business-cycle/) — Macro rhythm Coppock's periods approximate
- [Volatility smile](/volatility-smile/) — Market regime context for major reversals
- [DMI Plus and Minus](/dmi-plus-minus-directional-movement/) — Complementary directional confirmation
- [TEMA vs EMA](/tema-vs-ema-lag-reduction/) — Lag trade-offs in smoothing

</div>
