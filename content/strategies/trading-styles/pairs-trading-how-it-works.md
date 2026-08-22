---
title: "Pairs Trading: How It Works"
description: "Pairs trading exploits temporary mispricings between two correlated securities by shorting one while going long the other, aiming to profit from spread convergence."
keywords:
  - pairs trading
  - statistical arbitrage
  - market neutral strategy
  - spread convergence
  - correlated securities
  - long-short trading
---

*Pairs trading is a **market-neutral strategy** where a trader simultaneously buys one security and sells a correlated one, betting that their temporary price divergence will narrow. The profit comes from that convergence, not from overall market direction—making it indifferent to bull or bear markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Pairs Trading — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for trading strategies." />

<div class="wiki-infobox-caption">A hedge that isolates relative value from market swings.</div>

|   |   |
|---|---|
| **Core idea** | Long one security, short its correlated peer; profit from spread mean reversion |
| **Setup cost** | Margin account required; borrowing fees on short leg reduce profit |
| **Profit driver** | Spread narrowing, not directional moves |
| **Typical holding** | Days to months |
| **Skill required** | Identifying correlated pairs, quantifying valuation gaps, managing execution slippage |
| **Primary risk** | Pairs diverge further; correlation breaks down; borrow cost spikes |

</aside>

## The Core Mechanic

A pairs trade rests on a simple observation: two similar securities—say, Apple and Microsoft, or Coca-Cola and PepsiCo—often move in tandem. Traders measure this relationship using correlation. When the pair drifts out of sync, one becomes relatively expensive and the other cheap. The pairs trader bets that this gap closes.

The execution is blunt: buy the cheaper security (long), borrow and sell the expensive one (short). If the spread tightens—either because the long rises, the short falls, or both—you pocket the difference. You are indifferent to whether both stocks climb or both plummet; you care only that their relative gap narrows.

This structure makes pairs trading **market-neutral** in intent. A portfolio-level crash does not automatically kill your trade if both legs move down together at the same rate. That symmetry is why hedge funds and [statistical arbitrage](/statistical-arbitrage/) desks have favored this approach for decades.

## Identifying a Pair

The first task is finding two securities that genuinely move together. Common candidates are:

- **Competitors in the same industry**: Energy companies (ExxonMobil vs. Chevron), retailers (Target vs. Walmart), pharmaceutical makers.
- **Related asset classes**: Treasury bond future vs. Treasury ETF; a stock and its principal analyst-recommended ETF.
- **Cross-listed or identical underlyings**: The same company's shares on different exchanges, or a company and its depositary receipt.

The trader then calculates **historical correlation**—typically over 100 to 500 trading days. A correlation above 0.80 is usually the minimum threshold; many traders hunt for pairs above 0.90.

But past correlation is not a guarantee. Industries, business models, and leadership change. A pair that moved in lockstep for five years can diverge when one firm acquires a target or enters a new market. Successful pairs traders monitor the relationship continuously and exit trades when the correlation weakens beyond a pre-set tolerance.

## The Spread and Its Measurement

Once a pair is chosen, the trader calculates the **spread**—the quantitative gap between the two. This takes several forms:

- **Simple ratio**: If Stock A trades at $100 and Stock B at $50, the ratio is 2:1. A trader might track when this ratio deviates beyond, say, 1.95 or 2.05.
- **Standardized distance**: Using z-scores, the trader calculates how many standard deviations the current spread sits from its historical mean. A z-score beyond +2 or −2 signals an extreme divergence.
- **Regression-based model**: For sector-level pairs, traders regress one stock's returns against the other to quantify the baseline relationship, then trade when the residual swells.

When the spread is at an extreme (say, the short leg is unusually expensive relative to the long leg), the trader establishes the position, expecting the spread to revert toward its historical mean.

## Execution and Position Management

Pairs trades require precision in execution. The trader must:

1. **Enter both legs near simultaneously** to avoid directional exposure while waiting to fill the other leg.
2. **Calculate the hedge ratio**—how many shares of each to trade so the [delta](/delta/) is neutral. If Pair A has a beta of 1.2 and Pair B has a beta of 0.9, the trader might buy 90 shares of B for every 100 shares of A sold short.
3. **Manage borrow costs** on the short leg. Borrowing a heavily shorted security can be expensive; that cost eats into returns.
4. **Monitor the spread in real time**. Many traders use automated alerts to watch for widening (a sign the thesis is breaking down) or, conversely, for the convergence target being hit.

## Exiting the Trade

A trader exits when:

- **The spread converges** to its target level. If the goal was to close a 3% gap, the trader exits when that gap shrinks to, say, 0.5%.
- **The thesis breaks**: The pair's correlation deteriorates or fundamental news suggests one company has a major advantage over the other.
- **A stop-loss is hit**: If the spread widens beyond a pre-set threshold, the trade is closed to limit losses.
- **Time decay**: Some pairs traders use a calendar trigger—"hold for 30 days, then exit regardless." This caps tail-risk exposure.

## Why Pairs Trading Remains Attractive

The appeal is straightforward: pairs trading works in [bear markets](/bear-market/), [bull markets](/bull-market/), and sideways choppy conditions. It sidesteps the need to predict overall market direction. For a retail trader without conviction about the next Fed move or earnings season, a well-researched pairs trade offers a contained wager.

The downside is real. Borrow costs, bid-ask [spreads](/bid-ask-spread/), and slippage on entry and exit can eat 50–100 basis points. The pair can diverge further, not less, if sentiment toward one company shifts. And identifying a truly mispriced pair in liquid markets is harder than it sounds; if the gap is obvious, someone else has already traded it away.

## The Competition

Professional [algorithmic trading](/algorithmic-trading/) firms, quant hedge funds, and [market makers](/market-maker-trading/) run pairs strategies on a vast scale, using microsecond-level timing and real-time data feeds. The spreads available to them are tighter. Retail traders can still compete in less liquid pairs (small-cap stocks, international exchanges) or in pairs where the mispricing is driven by sector rotation or index rebalancing events that hit all traders at once.

## See also

<div class="wiki-seealso">

### Closely related

- Market-Neutral Strategies — the broader framework where pairs trading sits
- [Statistical Arbitrage](/statistical-arbitrage/) — the quant toolkit behind spread hunting
- [Short Selling](/short-selling/) — the mechanics of the short leg
- Correlation — measuring asset relationships
- [Trend Following vs Mean Reversion](/trend-following-vs-mean-reversion/) — contrasts mean-reversion pairs logic with trending systems
- [Algorithmic Trading for Retail Investors](/algorithmic-trading-for-retail-investors/) — how retail automation overlaps with pairs execution

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — using options and futures to hedge pairs risk
- [Market Maker Trading](/market-maker-trading/) — how professionals profit from spreads
- [Value Investing](/value-investing/) — the fundamental mindset behind spotting relative mispricings
- [Factor Investing](/factor-investing/) — systematic bets on asset characteristics

</div>
