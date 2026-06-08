---
title: "How to Size a Position in a Portfolio"
description: "Position-sizing frameworks—equal weight, volatility-scaled, conviction-based—and how each balances concentration risk with diversification."
keywords:
  - how to size a position in a portfolio
  - position sizing framework
  - portfolio concentration
  - diversification strategy
image: "/svg/strategies.svg"
---

*The size of each **position in a portfolio** determines how much the holding can move the overall returns and how much portfolio risk concentrates in any single bet. Different **position-sizing frameworks** make different trade-offs: equal weighting spreads risk evenly but can overweight volatile assets, volatility scaling adjusts for risk, and conviction sizing aligns position size with confidence in the thesis.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Position Sizing — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The art of deciding how much to own of each holding.</div>

|   |   |
|---|---|
| **Equal weight** | Same dollar amount in each position; simple but ignores risk |
| **Volatility-scaled** | Larger positions in low-volatility assets, smaller in volatile ones |
| **Conviction-based** | Size matches confidence in the thesis; highest conviction gets largest position |
| **Risk-parity** | Weight by inverse volatility to equalize risk contribution per position |
| **Key trade-off** | Concentration vs. diversification |

</aside>

## The core problem: How much is enough?

Before investing, a portfolio manager must answer a deceptively simple question: If I believe in this opportunity, how much of my capital should I actually deploy?

The answer determines two things: the portfolio's exposure to that single bet, and the overall portfolio's risk and return profile. Sizing too small means the position barely moves the needle. Sizing too large means one bad thesis can crater the entire portfolio. Most portfolios sprawl somewhere in the middle, with position sizes that feel reasonable but are rarely thought through systematically.

**Position sizing** is the discipline of making this choice explicit. It is the answer to "how much" — and it must be consistent with both the portfolio's total risk budget and the manager's conviction in each holding.

## Equal weighting: The simplest approach

The most intuitive position-sizing method is equal weighting. If you own five stocks, put 20% of capital in each. If you own ten, put 10% in each.

Equal weighting has clear advantages: it is easy to execute, easy to explain, and it enforces [diversification](/diversification/) by design. No single holding can dominate. It requires no estimates of volatility or future returns — you simply divide the capital equally among your holdings.

But equal weighting ignores risk. Consider a portfolio of two assets: a stable utility stock with 8% annual volatility, and a biotech stock with 40% volatility. Equal weighting (50/50) means the biotech position can swing the portfolio far more than the utility position, even though they occupy the same dollar amount. The portfolio behaves much more like the volatile asset than its 50/50 composition suggests.

Equal weighting also creates an implicit bet that all positions are equally attractive. In reality, a manager often has stronger conviction in some holdings than others. Equal weighting forces you to ignore this information.

## Volatility-scaled sizing: Adjusting for risk

A better framework accounts for the risk profile of each holding. **Volatility-scaled position sizing** allocates more capital to lower-volatility assets and less to higher-volatility ones. The principle is that a given position should contribute roughly equally to the portfolio's risk, regardless of its absolute volatility.

Here is a simplified approach:

- Estimate the [historical volatility](/historical-volatility/) of each holding (usually the standard deviation of returns over the past 12–24 months).
- Allocate capital inversely to volatility. A stock with 10% volatility gets twice as much capital as a stock with 20% volatility.
- Normalize so allocations sum to 100%.

Example: A portfolio of three holdings with volatilities of 10%, 15%, and 30%.

| Holding | Volatility | Inverse (1/vol) | Allocation |
|---------|-----------|-----------------|-----------|
| A       | 10%       | 0.10            | 55%       |
| B       | 15%       | 0.067           | 37%       |
| C       | 30%       | 0.033           | 18%       |

This ensures that if all three holdings decline by their historical average volatility, they contribute roughly the same magnitude of loss to the portfolio. The stable holding supports a larger position; the risky holding is restrained.

Volatility scaling is more sophisticated than equal weighting, but it still treats all holdings as equally *important* to the strategy. It only adjusts for risk.

## Conviction-based sizing: Aligning size with thesis strength

Many professional investors size positions according to **conviction** — how confident they are in the thesis and how well-researched the holding is.

A conviction-based framework might look like this:

- **Core conviction** (50% allocation): Holdings the manager knows deeply, with extensive research and a high-conviction thesis. Each might be 8–15% of the portfolio.
- **Secondary conviction** (30% allocation): Solid ideas with good fundamentals but less depth of research. Each might be 3–5%.
- **Exploration** (20% allocation): Smaller bets on less-proven ideas or emerging opportunities. Each might be 1–2%.

The logic is straightforward: concentrate capital where you have the most edge. A manager who has spent six months building a model of a company's [cash flow](/cash-flow-statement/) should size that position larger than one she heard about last week.

Conviction sizing requires discipline: you must regularly reassess your conviction as new information arrives. When a thesis breaks down, you cut the position. When conviction deepens, you size up. The framework stays honest about what you actually know.

## Risk-parity sizing: Equal risk contribution

A more technical approach is **risk-parity sizing**, often used in hedge funds and quant strategies. The goal is to weight each position so it contributes equally to portfolio risk, accounting not only for [volatility](/historical-volatility/) but also for correlations between holdings.

In a simple case with uncorrelated assets, risk-parity allocation is similar to volatility-scaled allocation: allocate inversely to volatility. But when holdings are correlated — say, two tech stocks that move together — risk-parity adjusts by reducing the size of one to avoid concentration of risk.

Calculating true risk-parity requires a [covariance matrix](/beta/) of all holdings and is typically done with optimization software. The reward is a portfolio where each holding poses roughly the same threat to overall performance, regardless of its volatility. This appeals to investors who want risk to be explicit and balanced.

## Comparing the frameworks

| Framework | Pros | Cons |
|-----------|------|------|
| **Equal weight** | Simple, enforces diversification | Ignores risk and conviction |
| **Volatility-scaled** | Accounts for risk, easy to compute | Treats all holdings as equally important |
| **Conviction-based** | Aligns capital with edge | Requires honest self-assessment |
| **Risk-parity** | Technically rigorous, risk-balanced | Complex; requires covariance estimates |

Most professional portfolios blend these ideas. A manager might start with volatility-scaled positions, then adjust upward for high-conviction ideas and downward for exploratory bets. The key is being intentional: you should be able to explain why each position is its particular size.

## Maximum position size and concentration limits

Most portfolios set rules about how large any single position can grow. These limits serve two purposes: they prevent unintended concentration if a holding performs spectacularly, and they enforce discipline around position sizing.

Common limits include:

- No position larger than 10% of the portfolio at initiation.
- No position larger than 15% after [appreciation](/accumulated-depreciation/).
- Core positions capped at 8%, exploration positions at 2%.

These limits are arbitrary but useful. They force the portfolio to hold enough holdings to survive if one thesis fails catastrophically. A portfolio with four 25% positions is not diversified; a portfolio with 20 positions averaging 5% is far more resilient.

## Adjusting positions over time

Position size should not be static. As holdings appreciate or depreciate, their weight in the portfolio drifts. A position that was 5% of capital and tripled is now 15%. This requires a rebalancing decision: do you trim it back to 5% (locking in gains, reducing concentration), or let it run?

Similarly, when conviction changes, position size should adjust. If your thesis breaks down, you should cut the position, not hold it for the sake of a formula.

The best position-sizing frameworks are guidelines, not dogma. They keep you thinking systematically about risk and allocation, and they prevent lazy decisions like "hold it because I bought it" or "buy more because it's falling."

## See also

<div class="wiki-seealso">

### Closely related

- [Diversification](/diversification/) — Why spreading across holdings reduces portfolio risk.
- [Historical Volatility](/historical-volatility/) — How to measure past price swings as a guide to future risk.
- [Beta](/beta/) — How much a holding tends to move with the broader market.
- [Concentration Risk](/concentration-risk/) — The danger of having too much capital in too few holdings.
- [Portfolio Construction](/asset-allocation/) — The broader framework for assembling a portfolio.

### Wider context

- [Risk-Weighted Assets](/risk-weighted-assets/) — How banks measure risk concentration.
- [Value Investing](/value-investing/) — One conviction-based approach.
- [Reputational Risk](/reputational-risk/) — Why overconcentrated positions expose you to single-firm risk.

</div>