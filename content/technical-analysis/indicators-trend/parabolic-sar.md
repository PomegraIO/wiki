---
title: "Parabolic SAR"
description: "A trailing-stop indicator that accelerates toward price as a trend strengthens, flipping direction when price reverses, marking potential exhaustion points."
keywords:
  - Parabolic SAR
  - stop and reverse
  - trailing stop
  - trend exhaustion
  - entry and exit signals
  - technical trading
image: "/svg/technical-analysis.svg"
---

*A **Parabolic SAR** (stop and reverse) is a trailing-stop indicator that follows price in a trend, always sitting just behind where the market is moving. When price reverses and closes on the opposite side of the SAR, the position is reversed—you exit the old trade and enter the new one automatically. The indicator's parabolic curve accelerates toward price as a trend grows strong, then decelerates when conviction fades, making it one of the few tools that yields both entry and exit signals from a single ruleset.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Parabolic SAR — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">An intelligent, self-adjusting trailing stop that reverses when price turns.</div>

|   |   |
|---|---|
| **What it is** | A trailing stop that flips direction when price reverses, triggering a new trade |
| **Named after** | Its parabolic curve shape and "stop and reverse" mechanics |
| **Acceleration factor** | Starts at 0.02, increases by 0.02 each time a new extreme is made, caps at 0.20 |
| **SAR in uptrend** | Below price; moves up as price climbs; sits at the lowest low of the trend |
| **SAR in downtrend** | Above price; moves down as price falls; sits at the highest high of the trend |
| **Strengths** | Clear entry/exit rules, adapts to trend intensity, removes emotion |
| **Weaknesses** | Whipsaws in choppy markets, cannot predict reversals early |

</aside>

## How the parabolic curve builds as a trend strengthens

The Parabolic SAR begins conservatively. In an uptrend, the SAR starts at the lowest low seen so far and climbs slowly—0.02 times the difference between the highest high and the current SAR. As price extends higher and makes new highs, the acceleration factor increases by another 0.02, capping at 0.20 (20%). With each new high, the SAR jumps forward more aggressively, climbing at an accelerating rate toward price.

This mathematics mirrors real trend psychology. Early in a rally, price gains slowly; the SAR lingers far below, acting as a conservative stop. But as the move matures and price makes record highs, the SAR catches up, compressing the space between price and the stop. This acceleration is intentional: it forces you out of tired trends before they fully reverse.

The parabolic shape emerges from this acceleration formula. If you plot SAR values during an extended uptrend, they trace a curve that looks like a parabola—slow at first, then accelerating upward. This visual curvature is where the indicator gets its name.

## Using SAR as a dynamic trailing stop

In a long trade, you hold as long as price stays above the SAR. The moment price closes below the SAR, you exit and reverse short. The SAR then flips to above price and begins trailing downward, acting as a resistance level for the short. When price rallies and closes above the SAR, you exit the short and go long again.

This creates a mechanical, emotion-free system. You never wonder whether to hold or exit; the SAR tells you. For traders who struggle with discipline, this is invaluable. For traders with strong conviction in a trend, the automatic reversal can feel frustrating—you'll occasionally be whipsawed out of a winning trade just before it accelerates again.

The advantage is clarity. A [moving average](/exponential-moving-average/) is passive; it sits there and you decide when to exit. The SAR is active; it gives you a definitive line, and the rule is binary—price is on the correct side or it isn't.

## The acceleration factor as a volatility proxy

The acceleration factor is the SAR's admission that trends don't all grow at the same pace. In a volatile, convulsive rally, price makes new highs frequently; the SAR's acceleration factor maxes out at 0.20 (20%) quickly, and the SAR races upward aggressively. In a steady, grinding uptrend with few new highs, the acceleration factor stays low (0.02 or 0.04), and the SAR trails lazily.

This adaptability is the indicator's main edge. During quiet consolidations, the SAR's low acceleration keeps you from being shaken out on minor wiggles. During explosive breakouts, the high acceleration pulls you out early, protecting profits before the reversal fully takes hold.

Professional traders sometimes tweak these parameters. Instead of capping at 0.20, they might cap at 0.30 to be more aggressive; or they might set a lower cap (0.10) for choppy markets. The concept remains: make the SAR accelerate faster in violent trends and slower in calm ones.

## When SAR exits you from winners prematurely

The classic complaint about Parabolic SAR is that it exits winning trades before the full move is complete. You're long, price rallies 20%, the SAR catches up and you reverse short, then price continues rallying another 10% against your short position before you cover.

This happens because the SAR is a *trailing* stop designed for risk management, not a *leading* indicator designed to predict the full extent of a move. Its job is to keep you in the trend whilst the trend is healthy and boot you out quickly once it fails. Sometimes it boots you out a bar or two early.

Traders who want to ride longer moves often use a slower [exponential moving average](/exponential-moving-average/) or [moving average crossover](/moving-average-crossover/) for position management instead of, or alongside, the SAR. They use the SAR as a hard stop-loss level (only exit if breached decisively on the close), but they take some profits at the [moving average](/exponential-moving-average/) to harvest a portion of the move.

## Parabolic SAR in choppy, sideways markets

The SAR's biggest weakness surfaces in consolidation zones. Price oscillates back and forth; the SAR flips long, then short, then long again within days. Each flip exits the prior trade and enters the opposite position, and most of those trades hit the SAR stop almost immediately. A choppy sideways market can shred accounts using strict Parabolic SAR rules.

Smart traders avoid SAR systems during sideways phases. They might shift to a mean-reversion tool like [Bollinger Bands](/bollinger-bands/) or simply sit in cash until the SAR gives an unambiguous signal (e.g., a new extreme in the direction of the signal before the first reversal). Alternatively, they add a filter: only take SAR signals if price is also above a 50-period [moving average](/exponential-moving-average/), ensuring they trade in the direction of the longer-term trend.

## Layering SAR with other trend confirmations

Alone, Parabolic SAR can mislead in choppy markets. But combined with other trend tools, it becomes powerful. A common setup: trade SAR signals only when price is on the correct side of [exponential moving averages](/exponential-moving-average/) (e.g., price above a 20-period and 50-period EMA for long signals). This filters out many of the false reversals in choppy zones.

Another approach: use SAR for exit discipline but enter using [moving average crossovers](/moving-average-crossover/). Once the 12 EMA crosses above the 50 EMA, you go long and ride the SAR; you exit when the SAR flips. This ensures you're already in the trend before you risk capital, and the SAR manages your exit with precision.

## The SAR in intraday and multi-timeframe trading

Parabolic SAR works on any timeframe. A 5-minute chart SAR is perfect for day traders; a daily SAR suits swing traders; a weekly SAR is used by longer-term position traders. The mechanics don't change; only the holding period and risk per trade scale with the timeframe.

Many systematic traders use SAR on multiple timeframes simultaneously. They use a daily SAR to set their directional bias (are they long or short overall?), then use an hourly SAR to time intraday entries and exits. This layering keeps them trading in the direction of the dominant trend whilst harvesting intraday mean-reversion swings.

## Customising SAR for risk tolerance

The default parameters (AF start 0.02, increment 0.02, cap 0.20) suit most traders. But if you're in a very volatile market or you want to stay in trends longer, you might lower the cap to 0.10. If you're in a choppy market and you want to be more aggressively shaken out on first signs of weakness, you might raise it to 0.30.

The best practice is to backtest your preferred market and timeframe with a few parameter sets, measure the results, and stick with one. Tinkering mid-stream tempts you to curve-fit to recent performance—the kiss of death in trading. Once you've chosen your SAR parameters, treat them as sacred rules.

## See also

<div class="wiki-seealso">

### Closely related

- [Exponential Moving Average](/exponential-moving-average/) — Companion tool for trend confirmation and position management
- [Moving Average Crossover](/moving-average-crossover/) — An alternative signal for entering trends before SAR exits them
- [Bollinger Bands](/bollinger-bands/) — A volatility-adaptive tool for mean reversion when SAR exits in choppy zones
- [Market Timing](/market-timing/) — The core discipline that SAR automates

### Wider context

- [Bull Market](/bull-market/) — Sustained uptrends where SAR shines
- [Bear Market](/bear-market/) — Downtrends where SAR trailing stops protect profits
- [Price Discovery](/price-discovery/) — The underlying price mechanism that SAR follows
- [Algorithmic Trading](/algorithmic-trading/) — How SAR rules scale into systematic trading systems

</div>
