---
title: "Pairs Trading Strategy Basics"
description: "Pairs trading strategy basics: simultaneously going long one asset and short a historically correlated counterpart when their price spread diverges. A market-neutral, statistical approach."
keywords:
  - pairs trading strategy
  - pairs trading basics
  - market neutral strategy
  - statistical arbitrage
  - long short pairs trading
---

*A **pairs trading strategy** involves simultaneously taking a long position in one asset and a short position in a historically correlated asset when their price relationship deviates from its historical norm by a statistical threshold. The approach is market-neutral, profiting from mean reversion—the assumption that the spread between correlated assets will eventually revert to its average.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Pairs Trading Strategy — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Bet on convergence between correlated assets, not market direction.</div>

|   |   |
|---|---|
| **Core premise** | Two historically correlated assets drift apart; spread mean-reverts |
| **Entry signal** | Spread exceeds mean by 1–3 standard deviations (typically) |
| **Position structure** | Long one asset; short the other in ratio preserving correlation |
| **Exit condition** | Spread converges back to mean, or stop-loss is hit |
| **Risk exposure** | Market-neutral on index; sensitive to divergence widening further |
| **Time horizon** | Days to weeks (momentum-based pairs) or months (mean-reversion) |
| **Primary users** | Quantitative hedge funds, stat-arb desks, algorithmic traders |

</aside>

## The Core Logic: Correlation and Divergence

Pairs trading rests on a simple observation: some pairs of assets move together historically. Apple and the Nasdaq-100 index rise and fall in tandem. Gold and the US Dollar often move inversely. Two competing retailers, or two banks in the same region, frequently track together because they are exposed to similar business cycles and macro shocks.

When two correlated assets trade at a spread (price difference or ratio) that deviates sharply from its historical average, a pairs trader hypothesizes that the spread is temporary—driven by temporary liquidity, sentiment, or news—and will eventually revert. The trade is designed to profit from that convergence.

**The key insight:** Pairs trading is not a directional bet on either asset alone. It is a *relative value* bet. The trader does not need the stock market to rise or fall; they just need the spread between the two assets to shrink. This market-neutral structure removes broad market risk and focuses profit purely on the relative mispricing.

## How to Construct a Pairs Trade

**Step 1: Select a correlated pair.** This can be done through historical data analysis (computing the correlation coefficient over a rolling window, typically 1–3 years) or through economic logic (two utilities in the same region, two oil producers, two e-commerce retailers). The correlation must be strong—ideally above 0.7—and, crucially, it must be *economically stable*. If two assets were correlated in the past but the fundamental relationship has changed, the pair is no longer useful.

**Step 2: Define the spread metric.** For stocks, this could be the price ratio (Stock A / Stock B), the price difference (Stock A - Stock B), or a regression-based residual (the actual price minus the predicted price based on historical correlation). For more sophisticated traders, it might be a Z-score: how many standard deviations the current spread is from its mean.

**Step 3: Establish a statistical threshold.** A trader decides that if the spread deviates by, say, two or three standard deviations, it is worth trading. A two-sigma threshold triggers roughly 5% of days (in a normal distribution); a three-sigma event is rare (0.3% of days), suggesting a large mispricing. Tighter thresholds (one sigma) increase trade frequency but accept smaller mispricings; wider thresholds are pickier about entry but require larger deviations.

**Step 4: Enter the trade.** If Asset A has outperformed and is now expensive relative to its historical spread with Asset B, the trader shorts A and longs B. If Asset B is now expensive, the trade reverses. Position sizes are often determined by the historical regression: if A is twice as volatile as B, the trade might be short 200 units of A and long 100 units of B to keep dollar exposure balanced (or to match the regression coefficient).

**Step 5: Exit when the spread converges.** Once the price relationship reverts to its historical mean, the trade is profitable and can be closed. Alternatively, if the spread widens further (confirming the divergence is not temporary), the trade is stopped out at a pre-set loss level to prevent catastrophic drawdowns.

## An Example

Suppose XYZ Airlines and ABC Airlines have historically traded at a price ratio of 1.2 (XYZ is 20% more expensive per share). Over a three-year history, this ratio has fluctuated between 1.0 and 1.4, with a mean of 1.2 and a standard deviation of 0.1.

Today, XYZ trades at $50 and ABC at $50. The ratio is now 1.0, two standard deviations *below* the mean. This is rare and suggests that XYZ is undervalued relative to ABC.

A pairs trader would:
- **Long** 100 shares of XYZ at $50 (cost: $5,000)
- **Short** 120 shares of ABC at $50 (proceeds: $6,000)

Net cash outlay: -$1,000 (the short raises cash). The position is hedged: if the sector crashes, both fall, and the short gain offsets the long loss. If the sector rallies, both rise, and the losses offset. The profit comes only if the spread narrows—i.e., if XYZ outperforms ABC.

Within weeks, XYZ announces a strong earnings beat. ABC reports a mixed quarter. XYZ rises to $55; ABC falls to $48. The ratio is now 1.15, close to the mean. The trader closes the long (sell 100 shares at $55, gaining $500) and covers the short (buy 120 shares at $48, losing $240 from the short sale proceeds of $6,000). Net profit: roughly $260 before commissions.

## Market-Neutral and Risk Implications

A pairs trade removes *systematic risk*—the broad market direction. If the overall stock market crashes, both assets in a correlated pair are likely to fall, and the long/short structure cushions the blow. This is valuable in volatile markets: the strategy profits from relative mispricings regardless of bull or bear conditions.

However, pairs trading is not risk-free. Several risks remain:

**Correlation breakdown:** The historical relationship can deteriorate. If economic conditions change—a regulatory shift, a technological disruption, a merger—two assets that were once correlated may diverge permanently. A trader holding a pairs trade sees the spread widen and widen, triggering a stop loss.

**Event risk:** A company-specific shock (fraud, accident, management change) can disrupt the correlation. The short position may suffer a short squeeze (if the shorted company is acquired at a premium) while the long position recovers modestly, creating losses despite the spread still being mean-reverting.

**Liquidity:** If either leg of the pair becomes illiquid, the trader may struggle to exit at favorable prices. In a crisis, liquidity evaporates, and the mark-to-market loss can be severe.

**Leverage:** Pairs traders often use leverage to amplify returns from small spreads. Leverage magnifies losses if the trade moves against them.

## Why Pairs Trading Works (and When It Doesn't)

Pairs trading exploits mean reversion, a documented feature of relative prices across many asset classes. Over long enough time horizons, correlated assets do tend to revert to their historical relationship. The strategy is strongest in:

- **Efficient, liquid markets** with tight bid-ask spreads (equities, major currency pairs, index futures)
- **Structural relationships** (e.g., a parent company and its subsidiary; two major competitors in the same industry)
- **Periods of high volatility**, when mispricings widen, offering larger profit potential

The strategy is weakest when:

- **The correlation is changing** (e.g., two industries decoupling as a sector rotates)
- **Spreads are already tight**, leaving little room for profit after commissions
- **Leverage is high**, turning small losses into portfolio-threatening events
- **The assets are illiquid**, making entry and exit costly

## Historical Context and Modern Practice

Pairs trading grew popular in the 1980s and 1990s, particularly in academic finance and among quant funds. The 1998 collapse of Long-Term Capital Management, which relied heavily on statistical arbitrage (pairs trading's cousin), exposed the strategy's vulnerabilities: during market dislocations, correlations can break and liquidity evaporates, creating simultaneous losses on multiple fronts.

Today, pairs trading remains popular among algorithmic traders, hedge funds, and quantitative asset managers, but it is more sophisticated. Traders now:

- **Monitor correlation stability** in real-time, triggering exit if it deteriorates
- **Combine pairs trading with other signals**, using machine learning to identify the most robust pairs
- **Scale positions** based on volatility and liquidity conditions
- **Use options** to hedge event risk on the short leg

## See also

<div class="wiki-seealso">

### Closely related

- [Market Neutral](/market-risk/) — the strategy's objective of removing market-level direction risk
- [Short Selling](/short-selling/) — how the short leg of a pairs trade is executed
- [Hedging](/derivatives-hedging/) — the principle underlying pairs trading
- [Statistical Arbitrage](/algorithmic-trading/) — pairs trading is a subset of stat-arb
- [Mean Reversion](/momentum-investing/) — the core assumption that spreads revert to average
- [Beta](/beta/) — pairs trades aim for low or zero portfolio beta

### Wider context

- [Algorithmic Trading](/algorithmic-trading/) — the execution method for most modern pairs trades
- [Hedge Fund](/hedge-fund/) — the typical institutional user of pairs trading
- [Correlation](/market-cycle/) — the statistical foundation of pair selection
- [Leverage](/leverage-ratio-forex/) — risk amplification in pairs trading
- [Liquidity Risk](/liquidity-risk/) — a major danger in unwinding pairs trades during stress

</div>
