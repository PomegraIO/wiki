---
title: "Money Flow Index: How It Is Calculated and Used"
description: "The Money Flow Index calculation uses typical price and volume to create an oscillator measuring buying and selling pressure, flagging overbought and oversold zones."
keywords:
  - money flow index calculation
  - mfi indicator
  - overbought oversold
  - volume indicator
  - price momentum
  - technical analysis
  - money flow
image: /svg/technical-analysis.svg
---

*The **Money Flow Index calculation** transforms price and volume into a single oscillator that swings between 0 and 100, signaling when a stock or commodity is overbought, oversold, or balanced. Unlike indicators that ignore volume, the MFI measures the actual force of buyers and sellers, making it a favorite tool for quantifying institutional conviction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Money Flow Index — key facts</div>

<img src="/svg/technical-analysis.svg" alt="An abstract editorial mark for technical analysis." />

<div class="wiki-infobox-caption">The only oscillator that weights price movement by the volume behind it.</div>

|   |   |
|---|---|
| **Reading range** | 0–100 (oscillator, bounded) |
| **Overbought threshold** | Typically 70–80, meaning buying pressure is extreme |
| **Oversold threshold** | Typically 20–30, meaning selling pressure is extreme |
| **Standard period** | 14 bars (days, hours, or minutes depending on chart timeframe) |
| **Divergence signal** | When price makes a new high but MFI does not, weakness is indicated |
| **Calculation method** | Typical price × volume → positive/negative money flow → money ratio → oscillator |
| **Reliability** | Strongest in range-bound markets; less reliable in strong trending markets |

</aside>

## The Three-Step Formula

The Money Flow Index calculation rests on three linked steps: calculating typical price, computing raw money flow, and then deriving the money ratio. Understanding each step reveals how volume is woven into the signal.

**Step 1: Typical Price.** For each bar, calculate the average of the high, low, and close:

$$\text{Typical Price} = \frac{\text{High} + \text{Low} + \text{Close}}{3}$$

This single number represents the "center of gravity" of the bar's price range and is more reliable than using only the close when assessing where the bar traded on balance.

**Step 2: Raw Money Flow.** Multiply the typical price by the volume for that bar:

$$\text{Raw Money Flow} = \text{Typical Price} \times \text{Volume}$$

Raw money flow is an absolute measure. A large volume bar with a high price produces a large positive number. A small volume bar produces a small number. This is the sense in which the MFI "weights" price movement by volume—high-volume moves carry more weight in the calculation.

**Step 3: Positive and Negative Money Flow.** The calculation then separates positive from negative money flow:

- If today's typical price is *higher* than yesterday's, all of today's raw money flow is labeled "positive money flow" (accumulation).
- If today's typical price is *lower* than yesterday's, all of today's raw money flow is labeled "negative money flow" (distribution).
- If today's typical price is *equal* to yesterday's, raw money flow is typically excluded or counted as neutral.

## The Money Ratio and the Oscillator

The next step sums the positive and negative money flows over a period (typically 14 bars):

$$\text{Money Ratio} = \frac{\text{Sum of Positive Money Flow (14 bars)}}{\text{Sum of Negative Money Flow (14 bars)}}$$

A money ratio above 1.0 indicates that positive money flow (buying pressure) has dominated the period. A ratio below 1.0 indicates that negative money flow (selling pressure) has dominated.

Finally, the oscillator is derived:

$$\text{Money Flow Index} = 100 - \frac{100}{1 + \text{Money Ratio}}$$

This formula bounds the MFI between 0 and 100. As the money ratio grows larger (more buying), the MFI approaches 100. As the money ratio shrinks (more selling), the MFI approaches 0. When positive and negative money flows are equal, the MFI reads 50.

## Interpreting Overbought and Oversold

An MFI reading above 70–80 is considered overbought. It means that over the last 14 bars, buyers have been so forceful that negative money flow is dwarfed. This is a warning: such extreme buying pressure often leads to pullbacks or consolidation as the early buyers take profits and new sellers arrive.

An MFI reading below 20–30 is considered oversold. Sellers have been so dominant that buying pressure has evaporated. This often precedes bounces or reversals as bargain hunters step in and short-sellers cover.

However, overbought does not mean "sell immediately" and oversold does not mean "buy immediately." These extremes can persist during strong trending moves. A stock in a [bull-market](/bull-market/) rally may spend days above MFI 80 and still keep rising. Treating MFI extremes as automatic reversal signals is a common mistake.

## Divergence: The Signal That Matters Most

The most powerful use of the MFI is divergence. When price makes a new high but the MFI fails to make a new high (or makes a lower high), institutional buying is weakening even as price rises. This is a classic warning that the move is losing conviction.

Similarly, when price makes a new low but the MFI fails to make a new low, selling pressure is weakening even as price falls. This often precedes a bottom and reversal.

Divergence is a form of hidden weakness. The price chart shows optimism, but the MFI reveals that the volume behind the move is insufficient. Smart traders treat MFI divergence as a warning to scale back position size, tighten stops, or prepare for a reversal.

## MFI in Ranges Versus Trends

The MFI is most reliable in range-bound, sideways-moving markets where mean reversion is the expected behavior. A stock oscillating between $100 and $120 with MFI bouncing between 30 and 80 becomes highly predictable: buy near 30, sell near 80.

During strong trends, the MFI is less useful as a reversal signal. A powerful uptrend may keep MFI above 70 for weeks, giving false reversal signals to traders who blindly sell overbought conditions. In these situations, the MFI is better used to identify *pullbacks*: MFI may spike to 80, pull back to 50, and then spike again to new highs. The pullback to 50 offers a better entry than the overbought 80 reading.

## Combining MFI With Other Volume Tools

The MFI works well alongside other [volume](/stock-market/) indicators. Compare it to [Volume Confirmation of a Breakout](/volume-confirmation-breakout/): if price breaks resistance and the MFI surges simultaneously, conviction is high. If price breaks but MFI stays flat or falls, the breakout is suspect.

Similarly, if a stock exhibits [High Volume With Low Price Movement](/high-volume-low-price-movement/), the MFI will read near 50 (balanced positive and negative flow), even as raw volume is extreme. This combination tells you that the market is contested—neither buyers nor sellers are dominating—which often precedes a large directional move.

## Practical Reading Examples

**Example 1: Overbought Bounce.** A stock rallies from $50 to $58 over 5 days on strong volume. The MFI swings from 30 to 85. On day 6, price stalls at $57.50 as MFI rolls over to 75. This is a normal correction within an uptrend. On day 7, price climbs to $59 and MFI surges back to 80. The trend is intact.

**Example 2: Divergence Warning.** A stock rallies to a 52-week high of $120 on strong volume, and MFI reaches 82. Over the next week, price continues to creep higher, reaching $121. But MFI fails to reach above 78, instead falling to 72. This divergence warns that buying interest is drying up. A pullback follows within days.

**Example 3: Oversold Bottom.** A stock falls from $50 to $45 over two days on heavy selling volume. MFI crashes to 15. On the third day, price ticks down to $44.80, but MFI bounces to 25 on light volume. This divergence—lower price but higher MFI—suggests selling is exhausted. A reversal often follows within hours.

## Limitations and Adjustments

The standard 14-period MFI works well for daily charts. Shorter-term traders (using 5-minute or 1-hour charts) may use 9-period or 5-period MFI to reduce lag. Longer-term swing traders may use 21-period or 28-period MFI to smooth out noise.

The MFI also lags. It is a lagging indicator by design—it summarizes the past 14 bars. It is not predictive. It is best used in combination with current price action, [support and resistance](/price-discovery/) levels, and broader market context.

Additionally, the MFI assumes that price movement and volume are the only relevant data. It ignores gaps, news, earnings, and liquidity changes. On earnings days or during market-wide crashes, the MFI may read extreme without being predictive of immediate reversals.

## See also

<div class="wiki-seealso">

### Closely related

- [High Volume With Low Price Movement: What It Means](/high-volume-low-price-movement/) — Understanding when the MFI reads near 50 despite heavy volume, revealing market equilibrium.
- [Volume Confirmation of a Breakout](/volume-confirmation-breakout/) — Using MFI to validate whether breakouts have buying or selling conviction.
- [Volume Dry-Up Pattern in Technical Analysis](/volume-dry-up-pattern/) — Detecting when MFI and volume contract together before explosive moves.
- [Moving Average](/moving-average/) — Support and resistance levels where MFI extremes often reverse.
- [Trend Following](/trend-following/) — Using MFI to identify pullbacks within trends rather than relying on overbought/oversold alone.
- [Momentum Investing](/momentum-investing/) — Leveraging MFI to confirm that price momentum is backed by institutional volume.
- [Price Discovery](/price-discovery/) — How volume and price converge to establish fair value, the core principle behind the MFI.

### Wider context

- Technical Analysis — Broader framework for reading price, volume, and momentum signals.
- [Options](/option/) — Derivatives that respond to the same overbought and oversold conditions the MFI measures.
- [Volatility Smile](/volatility-smile/) — When MFI extremes coincide with volatility spikes, reversals are often more violent.

</div>
