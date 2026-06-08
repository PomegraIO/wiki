---
title: "Cumulative Volume Delta Explained"
description: "Cumulative volume delta explained: the running sum of buying minus selling volume, used to detect absorption, supply, and hidden institutional order flow."
keywords:
  - cumulative volume delta explained
  - cvd indicator
  - buying volume selling volume
  - volume delta trading
  - institutional absorption
  - order flow analysis
image: "/svg/technical-analysis.svg"
---

*A **cumulative volume delta** (CVD) is a running total of the difference between buying and selling volume at each price level, revealing whether institutions are absorbing supply or aggressively pushing price higher. Traders use it to spot conviction behind price moves and to anticipate reversals when absorption reaches extremes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cumulative Volume Delta — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A measure of institutional accumulation or distribution hiding beneath headline price action.</div>

|   |   |
|---|---|
| **What it is** | Running sum of (buy volume − sell volume) |
| **Time frame** | Intraday to daily; most sensitive on shorter bars |
| **Key signal** | Rising CVD = absorption; falling CVD = distribution |
| **Extreme readings** | Mark potential reversals when CVD diverges from price |
| **Limitation** | Requires reliable buy/sell volume data; unreliable on venues without tick data |

</aside>

## How Cumulative Volume Delta Is Calculated

Every candlestick or time-based bar has two components: the price move and the volume. Traders trying to infer intent from volume ask: did more volume trade on up-ticks or down-ticks?

A **buy volume** estimate counts every tick where price moved up; **sell volume** counts down-ticks. If a bar closes higher with more volume on up-ticks, the net delta is positive. Over time, adding each bar's delta to the previous total creates the running CVD line.

In practical terms, if a stock trades from $100.00 to $100.50 on the day with 2 million shares up and 1.2 million down, the day's delta is +800,000. If the next day adds another +600,000, the cumulative delta is now +1.4 million.

The arithmetic is straightforward; the insight is harder. A rising CVD tells you that despite any pullbacks, more volume is flowing in on strength than out on weakness—a sign of institutional buying interest.

## Why Volume Delta Matters More Than Price Alone

Price tells you where the market closed; volume delta tells you *how much conviction* was behind it. A stock rallying 2% can happen two ways:

- **Weak rally**: small lots of buyers push price up; the stock reverses on the first serious selling
- **Strong rally**: large blocks accumulate on dips, absorbing supply; price barely pulls back because buy interest is relentless

The CVD favors the second scenario. When cumulative volume delta rises steadily during a rally, it signals institutional buyers stepping in and soaking up every offer. When CVD stalls or reverses while price keeps climbing, it's a warning—the move is getting ahead of actual buying interest.

## Absorption and the Hunt for Hidden Orders

Institutions often split large orders into smaller parcels to avoid signaling their intent. A pension fund wanting to buy $50 million of stock will break it into dozens of smaller lots distributed over minutes or hours.

Cumulative volume delta reveals this absorption. While price action might look choppy—moving sideways or even drifting lower—a rising CVD shows that every dip is being bought. This is the textbook definition of absorption: aggressive buying underneath the surface.

The opposite happens during distribution. Price rallies but CVD plateaus or falls, meaning selling is matching or outweighing buying interest. Large holders are unloading while others are still bullish on the move.

## CVD Divergence as a Reversal Signal

The most actionable setup in CVD analysis is **divergence**. If price is making new highs but CVD is rolling over or failing to confirm, it's a yellow flag. The rally is losing its institutional fuel.

Conversely, when price dips to new lows but CVD is rising (or at least not falling as sharply), it suggests panic selling is drying up and smart buyers are stepping in.

A common real-world example: a stock gaps down on earnings and trades lower throughout the morning. Price touches a new low, but the CVD begins climbing as large buyers sense value. By afternoon, the gap is completely filled and the stock rallies hard—reward for traders who read the divergence.

These setups work best on intraday timeframes (5- to 60-minute bars) where institutional flow is most visible. On daily charts, CVD can take days or weeks to fully develop, and the signal is less timely.

## Data Quality and Practical Limits

CVD effectiveness depends entirely on the accuracy of buy/sell volume estimates. Most charting platforms infer buys from up-ticks and sells from down-ticks, but this is imperfect. Some large orders execute at the ask (buys) and some at the bid (sells) without moving price, and these get missed.

Additionally, many market venues don't publish true buyer/seller data—they report only total volume. Retail traders working with aggregated data from exchanges that do this lose resolution. Professional traders often subscribe to expensive data feeds with proper order flow or use venues like futures exchanges that publish tick data more transparently.

On illiquid assets or during slow trading periods, CVD can whipsaw—small market orders swing the indicator sharply. It's most reliable on high-volume, liquid symbols where order flow is constant and easier to pattern-match.

## Combining CVD With Price Structure

CVD is strongest not as a standalone indicator, but paired with price action. A trader might use CVD to confirm a bounce off a support level: if price holds and CVD climbs, it's a genuine accumulation zone. If price holds but CVD doesn't improve, it's just technical demand, fragile.

Similarly, CVD can warn of exhaustion near resistance. If price approaches a major high but CVD has already topped weeks earlier, the move may be running on momentum alone, not buying conviction.

Volume delta also integrates naturally with order flow analysis and [market microstructure](/market-microstructure/), where professionals dissect who is buying and selling and in what size. For longer-term investors, CVD is less relevant; for day traders and short-term swing traders reading intraday bars, it's a critical lens into institutional intent.

## See also

<div class="wiki-seealso">

### Closely related

- [Volume-Weighted RSI](/volume-weighted-rsi/) — momentum refined by volume strength
- [Volume at Price Levels](/volume-at-price-levels/) — how traders use historic volume clusters for support and resistance
- [Low-Volume Pullback as a Bullish Signal](/low-volume-pullback-signal/) — why shrinking volume during retracements is constructive
- [Market Microstructure](/market-microstructure/) — the mechanics of how orders execute and interact
- [Bid-Ask Spread](/bid-ask-spread/) — the cost of immediacy in order flow

### Wider context

- [Algorithmic Trading](/algorithmic-trading/) — how systems exploit volume patterns
- [Price Discovery](/price-discovery/) — the role of volume and flow in determining fair value
- [Market-Maker Trading](/market-maker-trading/) — how dealers manage inventory and flow
- [Over-the-Counter Market](/over-the-counter-market/) — venues with less transparent order data

</div>
