---
title: "Stop-Out Level"
description: "The margin threshold at which a broker automatically closes all open positions to prevent account equity from going negative."
keywords:
  - stop out
  - margin requirement
  - forced liquidation
  - leverage risk
  - account equity
image: /svg/forex.svg
---

*A **stop-out level** is the margin-based trigger at which a [broker](/broker/) forcibly closes all remaining open positions in a trading account, regardless of the trader's wishes. Once account equity falls below this threshold—typically 20–50% of the margin requirement, depending on the broker—the system liquidates positions to prevent the account balance from turning negative. It's a hard line, not a warning.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stop-Out Level — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for currency trading mechanics." />

<div class="wiki-infobox-caption">The point of no return: when a broker ends your trading session.</div>

|   |   |
|---|---|
| **What it is** | Account equity threshold triggering automatic position closure |
| **Trigger** | Equity drops below broker's stop-out level (often 20–50% of required margin) |
| **Who sets it** | The broker, embedded in trading terms |
| **Effect** | All open positions liquidated instantly at market rates |
| **Why it exists** | Protects broker from trader negative equity; prevents cascading losses |
| **Contrast** | Margin call: a warning; stop-out is execution |

</aside>

## The mechanics of forced closure

When you leverage your trading account—say, controlling $100,000 in currency with only $2,000 of your own capital—the broker holds a lien on your positions. If the market moves against you hard enough, your equity shrinks. Most brokers issue a margin call at, say, 50% of required margin to warn you. But if you don't deposit more funds or close trades voluntarily, and equity slides further, the broker's stop-out logic kicks in.

At that point, the system doesn't wait for your response. It liquidates all open positions, usually starting with the most underwater trades and working toward breakeven ones. Execution happens within milliseconds, at whatever bid or ask price the market is offering at that instant. You have no say. The math is simple from the broker's perspective: better to realize a known loss and close the account than risk the trader losing more money than exists in the account, leaving the broker holding the deficit.

## Why brokers enforce it

The regulatory framework in most jurisdictions prohibits negative equity accounts—at least, the broker cannot force a trader to pay back money lost beyond the account balance. So the stop-out level is the broker's only practical way to cap its own exposure. If the account hits zero and the market keeps moving, without force-closing positions, the broker itself would be the counterparty to an underwater trade, and the client couldn't—or wouldn't—cover the shortfall.

Different brokers set different stop-out levels. A conservative operation might trigger at 50% of margin; an aggressive bucket shop might allow 10%, tempting traders with the illusion of more trading freedom. That extra rope, of course, is exactly what makes a 10%-stop-out account more dangerous: a sudden volatility spike can liquidate you with almost no warning.

## Timing and market conditions

Stop-out triggers are particularly brutal during [weekend gap](/weekend-gap-forex/) scenarios or during news releases. If the market opens Monday with a massive gap, your position might go from healthy to liquidated before you've had a chance to react. Certain brokers, especially those operating in less-regulated jurisdictions, have been known to trigger stop-outs at suspiciously convenient levels—just above resistance, for instance—raising questions about execution integrity.

Likewise, during a [forex session overlap](/forex-session-overlap/), when liquidity is highest and volatility can spike, stop-outs flow in volume. A cluster of stop-outs across multiple accounts can itself create a feedback loop, as forced selling presses the market further, triggering more stops.

## The psychology and the protection

For many retail traders, the stop-out level represents the point where risk becomes real and irreversible. Knowing a stop-out exists should inform position sizing and stop-loss placement from the outset. A trader who sizes carefully and places a manual stop loss well before the broker's stop-out level regains control of the outcome; the trade closes at the level they chose, not at the level the market is offered after a cascade of liquidations.

Most risk-aware traders set their own stops closer to entry than the broker's stop-out level. This transforms the stop-out from an execution event into a safety net—something that exists but is never reached. That distinction matters. A trader who treats the stop-out level as a target ("I can trade up to 50% margin") is not managing risk; they're gambling on the market not moving enough, which is a poor trade on its own terms.

## Regulatory evolution

Regulators in Europe and some other jurisdictions have tightened rules around negative equity, requiring brokers to close accounts at or before the stop-out level reaches zero margin. This means a trader in a well-regulated environment faces a harder ceiling: you cannot run an account to actual negative equity. But in less-regulated markets, stop-outs remain broker discretion, and margins of safety are thinner.

## See also

<div class="wiki-seealso">

### Closely related

- Margin call — the warning before the stop-out is triggered
- [Leverage ratio (forex)](/leverage-ratio-forex/) — controls how far equity can erode before stop-out
- Margin requirement — the baseline equity percentage that defines the stop-out threshold
- [Liquidation](/liquidation/) — the forced sale of positions
- [Broker](/broker/) — the entity enforcing the stop-out
- [Weekend gap (forex)](/weekend-gap-forex/) — a common trigger for sudden stop-outs

### Wider context

- [Requote](/requote-forex/) — another broker risk control mechanism
- [FX session overlap](/forex-session-overlap/) — high-volatility windows when stops cluster
- Volatility — the risk factor that moves equity fastest
- Risk management — the discipline that prevents reaching stop-out

</div>
