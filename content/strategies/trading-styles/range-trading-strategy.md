---
title: "Range Trading Strategy"
description: "Range trading strategy buys near support and sells near resistance within a horizontal price band, repeating the cycle until a breakout occurs."
keywords:
  - range trading strategy
  - support and resistance
  - mean reversion
  - horizontal trading
  - intraday trading
  - price channel
image: /svg/strategies.svg
---

*A **range trading strategy** identifies a horizontal price band where a stock, commodity, or currency has repeatedly bounced off the same floor and ceiling. The trader buys near support (the floor), sells near resistance (the ceiling), and repeats the cycle, profiting on small reversals within the band. Success depends on correctly identifying the range, managing the risk of a breakout, and exiting when the range breaks.*

## How Range Trading Works

A stock trades between $48 and $52 for three weeks. It bounces off $48 five times and off $52 three times. A range trader identifies this band and deploys a mechanical rule:
- Buy at or near $48 (support).
- Sell at or near $52 (resistance).
- Pocket the $4 spread as profit.
- Repeat until the range breaks.

This is simple in theory. The trader is not betting on a direction, but on *reversion to the mean within known bounds*. The range is the mean; every move away from it is expected to snap back.

Range trading works because markets spend significant time consolidating—gathering strength or shaking out weak hands—before the next directional move. During consolidation, support and resistance become observable and tradeable.

## Identifying a Valid Range

Not every price band is a tradeable range. A valid range has:

**Multiple touches at boundaries:** A price level tested only once is not support or resistance. Support and resistance are confirmed by at least two touches (ideally three or more) where price bounced rather than closed below (support) or above (resistance).

**Horizontal shape:** The support level should be roughly flat, not sloping. A downward-sloping support is less reliable—it suggests weakness, not equilibrium. Similarly, a resistance that slopes down suggests the market is slowly surrendering to selling.

**Time duration:** A range that has held for a few hours or one trading day may break on the next data point. Ranges that persist for days or weeks are more reliable. Professional range traders often focus on intraday ranges (opening hour to 3 p.m.) because they're easier to predict than multiday ranges.

**Adequate liquidity:** Thin ranges in low-volume stocks are easily broken by a small order. A trader needs enough daily volume and [bid-ask spread](/bid-ask-spread/) stability to enter and exit multiple times without excessive slippage.

## An Intraday Example

A stock opens at $100, rallies to $102 in the first hour, then settles into a $99–$102 range for the next six hours.

A range trader identifies the range:
- Support: $99 (buyers appeared here three times).
- Resistance: $102 (sellers appeared here twice).

The trader's plan:
- Buy 500 shares at $99.20 (just above support to confirm a bounce).
- Sell at $101.80 (just below resistance to avoid being pinned).
- Repeat three or four times, pocketing $1.60 per cycle.
- If price closes above $102.50, exit all positions (range broken on upside).
- If price closes below $98.50, exit all positions (range broken on downside).

Over the course of a trading day, if the range holds and the trader successfully buys three times and sells three times, they lock in $2,400 profit on a $50,000 position.

## The Breakout Problem

The biggest risk in range trading is **breakout:** the price escapes the band, leaving the range trader holding a losing position or forced to exit at a loss.

A trader who bought $99 support is vulnerable if price closes at $98. The support has broken. If they're holding shares, they face a loss. If they exited at their stop ($98.50), they took a $0.50 loss and are out of the trade.

This is why range traders use **stop losses** (always). A typical stop in a $99–$102 range might be set at $98.50 (below support) and $102.50 (above resistance). When price touches the stop, the range trader exits, accepting a small loss as the cost of being wrong.

Breakouts can be false. Price may spike above resistance to $103, triggering stops, then collapse back into the range at $101. The trader has just been shaken out. This is why some range traders use wider stops or confirm breakouts with volume before exiting.

## Distinguishing Range Trading from Related Strategies

**Range trading** focuses on horizontal bands and profit from repeatedly trading the same boundaries.

**[Fade trading strategy](/fade-trading-strategy-explained/)** also bets on mean reversion but does not require a defined range. A fader may bet on reversion after a sharp 4% move, using support and resistance loosely. A range trader uses the range itself as the bet.

**[Breakout trading strategy explained](/breakout-trading-strategy-explained/)** is the opposite: the trader *anticipates* or *trades* the escape from the range. When price breaks above $102 on volume, the breakout trader enters long, expecting the move to continue.

**[Momentum investing](/momentum-investing/)** follows trends that develop after breakouts. A momentum trader might ride the stock from $102 to $110 after the range breaks up.

## How Professional Range Traders Adapt

Experienced range traders add filters to improve accuracy:

**Volume profile:** Buy support levels where large volume has historically accumulated; avoid support levels formed on light volume.

**Volatility context:** In low-volatility periods, ranges are tight and reliable. In high-volatility periods, false breakouts are common; widen stops or reduce trade frequency.

**Economic calendar:** Major data releases (jobs, CPI, Fed minutes) can spike price outside the range. Many range traders reduce size or close trades before such events.

**Intraday time windows:** Some range traders only trade the 10–15 minute bands after the open or in the final hour. They avoid the middle hours when news or algorithmic flows can disrupt the range.

**Confirmation of touches:** Instead of buying at exactly $99, buy only when the tape shows aggressive buying at $99 ([tape reading trading technique](/tape-reading-trading-technique/)). This increases the odds that the bounce is real.

## Range Trading in Different Market Conditions

Range trading thrives in **consolidation and low-volatility regimes**—the quiet periods between big moves.

It struggles in **trending markets**. A stock in a strong uptrend may eventually break its range to the upside; a range trader short at the old resistance suffers. Similarly, a stock in a downtrend breaks ranges downward, and range traders long at support are caught.

In **choppy or mean-reverting markets** (where price oscillates without clear direction), range trading can be the highest-probability strategy.

## See also

<div class="wiki-seealso">

### Closely related

- [Support and resistance levels](/price-discovery/) — the foundation of range trading; without clear levels, there is no range.
- [Breakout trading strategy explained](/breakout-trading-strategy-explained/) — the flip side: trading the escape from the range rather than the boundaries.
- [Fade trading strategy](/fade-trading-strategy-explained/) — also profitable on mean reversion but less dependent on a defined range.
- [Tape reading trading technique](/tape-reading-trading-technique/) — confirms entry and exit points within the range by observing order flow.
- [Volatility smile](/volatility-smile/) — understanding when a range is likely to widen or break.

### Wider context

- [Market maker trading](/market-maker-trading/) — market makers also profit from range-bound oscillation.
- [Momentum investing](/momentum-investing/) — the dominant strategy when ranges break into trends.
- [Risk management and stop losses](/market-order/) — essential discipline in range trading to cap losses on breakouts.
- [Consolidated market](/business-cycle/) — the broader environment where consolidation and ranges emerge.

</div>
