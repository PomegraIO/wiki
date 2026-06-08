---
title: "Leveraged ETF Decay: How Daily Rebalancing Erodes Returns"
description: "Leveraged ETF decay refers to volatility drag that causes 2x and 3x leveraged funds to underperform their target index multiplier over holding periods longer than one day due to daily rebalancing."
keywords:
  - leveraged etf decay
  - volatility drag leveraged etf
  - daily rebalancing decay
  - leveraged etf long-term performance
  - beta slippage decay
  - 2x 3x etf underperformance
---

*Leveraged ETF decay, also called volatility drag or beta slippage, is the mathematical erosion of returns that causes a 2x or 3x leveraged exchange-traded fund to fall short of twice or three times the index return over periods longer than one day. The culprit is daily rebalancing: by resetting leverage each day to maintain a constant multiplier, the fund locks in losses during downturns and forfeits outsized gains during sharp rallies, a friction that compounds into significant underperformance over weeks, months, or years.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Leveraged ETF Decay — the mechanics</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Daily rebalancing is necessary for funds to stay on target, but it has a real cost.</div>

|   |   |
|---|---|
| **What it is** | Underperformance of a 2x or 3x leveraged fund relative to its stated multiple of index return |
| **Root cause** | Daily rebalancing forces selling after losses, buying after gains (rebalancing at unfavorable points) |
| **Magnitude** | Grows with volatility; 20% annualized volatility + 2x leverage can decay 10–15% annually |
| **Time horizon** | Negligible over 1 day, material over 1–3 months, severe over years |
| **Volatility sensitive** | High-volatility indices and assets suffer far worse decay than stable ones |
| **Inverse decay** | Inverse leveraged funds (-1x, -2x) decay identically, eroding short-bet returns |
| **Mitigation** | Short holding periods; tactical trading, not buy-and-hold; [inverse-etf](/inverse-etf/) alternatives |

</aside>

## The Daily Rebalancing Treadmill

To understand decay, imagine a 2x leveraged ETF tracking the [S&P 500 index](/sp-500-index/). The fund holds a mix of stocks and futures or swaps to deliver twice the daily return of the S&P 500. If the S&P rises 1%, the fund target is a 2% gain. If the S&P falls 1%, the fund target is a 2% loss.

Here is the problem: the fund must rebalance daily to maintain this leverage ratio. Each evening, it resets its exposure so that the next day's exposure is again exactly 2x the index. This daily reset is essential for the fund to stay on track—without it, leverage would drift unpredictably. But the reset creates a cost, especially in volatile markets.

Consider a concrete scenario:

| Day | S&P 500 Move | Fund Target (2x) | Fund Actual (if no rebalance) |
|-----|--------------|-----------------|-------------------------------|
| 1 | +10% | +20% | +20% |
| 2 | -9% | -18% | -18% (off target, becomes -13.4% of NAV) |
| End of Day 2, rebalance | — | —Fund resets to 2x | — |
| Cumulative over 2 days | +1% return | Target: +2% return | Actual: ~+3.2% (by coincidence, outperforms) |

But now reverse the scenario:

| Day | S&P 500 Move | Fund Target (2x) | Fund Actual (if no rebalance) |
|-----|--------------|-----------------|-------------------------------|
| 1 | -10% | -20% | -20% |
| 2 | +11% | +22% | Fund has shrunk; +11% on smaller base = less recovery |
| End of Day 2 | — | Fund resets | — |
| Cumulative over 2 days | +0% return | Target: 0% return | Actual: -2.4% loss (underperformance) |

In the second scenario, the fund lost 20% of its value on day 1, then gained 11% on a smaller base on day 2. To rebalance back to 2x leverage after the loss, it had to shrink its position further, locking in losses. The rebalancing process forces the fund to *sell low* (after day 1's drop) and *buy high* (at the rebalanced level). Over repeated cycles, this compounds into significant drag.

## Why Volatility Is the Real Enemy

Decay is not primarily a function of whether the index rises or falls—it is a function of volatility. An index that rises 10% in a straight line with zero interim volatility will be tracked perfectly by a 2x leveraged fund. The fund gains 20%, and there are no rebalancing losses because there are no reversals.

The killer is volatility: the up-and-down oscillations, however small, that force repeated rebalancing. A highly volatile index that ends at the same level as a stable index will underperform dramatically in a 2x leveraged fund.

Consider two indices, both ending at +20% after one year:

- **Index A (stable)**: Rises 1.67% every month with zero interim volatility
  - 2x leveraged return: 40% (perfect tracking)

- **Index B (volatile)**: Swings ±8% monthly but ends at +20% annually
  - Monthly volatility forces daily rebalancing; 2x leveraged return: 25–30% (underperformance)

The decay formula, simplified, is approximately:

**Decay ≈ Leverage Ratio × Daily Volatility Squared × Number of Days**

A 2x leveraged fund on an index with 20% annualized volatility (1.25% daily volatility) decays roughly 2 × (0.0125)² × 252 trading days ≈ 0.08 or 8% annually. With a 3x fund, decay tripled to 24% annually, which can swamp the fund's outperformance in moderate uptrends.

## Concrete Historical Examples

In 2008, volatility spiked above 80% annualized, and leveraged ETFs suffered catastrophic decay. A 2x ETF on the S&P 500 underperformed 2x the index return by 30–50% over the year, despite the S&P's eventual loss. The fund was perpetually rebalancing into losses; each down day forced the sale of an outsized position, locking in additional losses on the subsequent recovery.

Conversely, in stable 2012–2013 (volatility around 10%), a 2x S&P 500 leveraged ETF tracked quite closely to 2x the index return, because there were fewer rebalancing cycles and less whipsaw.

The effect is even more pronounced in inverse and ultra-short positions. A 3x inverse ETF (betting against the market) decays identically: in a rising market, decay erodes short returns; in a volatile, sideways market, it erodes them even faster.

## Who Suffers Most from Decay

**Buy-and-hold investors** suffer most. Anyone holding a leveraged ETF for more than a few days is fighting decay, especially if they are holding through cyclical volatility. A retail investor who buys a 3x leveraged ETF expecting it to triple the index return over five years will be severely disappointed—decay will likely reduce actual returns by 50% or more versus the target.

**Day traders and tactical traders** often escape the worst of decay. They hold positions for hours or days, during which decay is negligible. Their profits or losses are driven by short-term price moves, not by multi-week volatility patterns.

**Covered call traders** and options-based strategies sometimes use leveraged ETFs as underlying assets, accepting decay as a cost of leverage. They typically offset decay via option income.

## Measuring and Mitigating Decay

The most direct way to see decay is to compare the 2x or 3x leveraged ETF's cumulative return to twice or three times the index return over a given period. Most fund factsheets now disclose this explicitly.

Investors can also calculate expected decay using historical [volatility](/historical-volatility/). An index or asset class with 25% annualized volatility will decay a 3x fund roughly 3 × 0.25² ≈ 19% annually, before fees. Add [expense ratios](/expense-ratio/) (typically 0.45–1.0% for leveraged ETFs), and total drag approaches 20–25% annually.

To mitigate decay:

1. **Keep holding periods short**: days or weeks, not months or years.
2. **Use in tactical trades**: rotate in and out based on directional conviction, not as core holdings.
3. **Monitor realized volatility**: if volatility spikes, expect increased decay; consider closing positions.
4. **Avoid ultra-leveraged funds in choppy markets**: a 3x fund in a 40%+ volatility environment will decay catastrophically.
5. **Consider alternatives**: unleveraged positions with [margin](/margin-call-forex/) or longer-dated [options](/option/) (which experience time decay differently) sometimes outperform leveraged ETFs in sideways or volatile markets.

## Inverse Leveraged Decay

Inverse and [inverse-etf](/inverse-etf/) funds (shorting the market) suffer identical decay mathematics. A -3x inverse fund decays by the same formula and is equally unsuitable for buy-and-hold strategies. In a bull market, the decay is particularly harsh because the fund is positioned to lose as the market rises, and volatility amplifies those losses further.

## See also

<div class="wiki-seealso">

### Closely related

- [Inverse ETF](/inverse-etf/) — funds designed to profit from market declines; suffer identical decay
- [Daily rebalancing](/etf/) — the mechanism that drives decay in leveraged funds
- [Expense ratio](/expense-ratio/) — fund fee that compounds decay over time
- [Volatility smile](/volatility-smile/) — related options pricing concept reflecting non-linear risk
- [Time decay theta](/time-decay-theta/) — options analogue to leveraged ETF decay

### Wider context

- [Exchange-traded fund](/etf/) — the fund structure underlying leveraged ETFs
- [Margin call forex](/margin-call-forex/) — alternative leverage mechanism with different risks
- [Derivatives hedging](/derivatives-hedging/) — how funds implement leverage internally via futures
- [Value at risk](/value-at-risk/) — risk metric that reflects tail volatility exposures

</div>
