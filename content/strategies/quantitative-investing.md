---
title: "Quantitative investing"
description: "Quantitative investing is a strategy of using mathematical models and statistical analysis to select stocks, rather than relying on qualitative judgment or fundamental research."
keywords:
  - quantitative investing
  - quant investing
  - statistical models
  - algorithmic trading
  - factor models
  - data-driven investing
image: "/svg/strategies.svg"
---

*Quantitative investing is an approach to [stock](/stock/) selection that relies on mathematical models, statistical analysis, and computational power to identify opportunities, rather than on qualitative judgment, research calls, or analyst reports. The core bet is that systematic, rules-based selection will outperform discretionary human judgment.*

<div class="wiki-hatnote">

For factor-based systematic approaches, see [factor investing](/factor-investing/) or [systematic investing](/systematic-investing/). For individual stock analysis, see [fundamental investing](/fundamental-investing/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Quantitative investing — key facts</div>

<img src="/svg/strategies.svg" alt="A computer screen showing stock selection model outputs" />

<div class="wiki-infobox-caption">Quant investors build models to remove emotion and codify repeatable patterns.</div>

|   |   |
|---|---|
| **Core idea** | Mathematical models outperform human judgment |
| **Tools** | Regression, machine learning, Monte Carlo, backtesting |
| **Data** | Price, volume, fundamentals, alternatives |
| **Scale** | Typically large (100s–1000s of stocks) |
| **Holding period** | Ranges from days to years |
| **Rebalancing** | Frequent and mechanical |
| **Alpha source** | Factor exposure, mispricings, behavioral biases |

</aside>

## The quant philosophy

Quantitative investors believe that:

1. **Patterns exist in data.** Historical stock returns contain exploitable patterns — [value](/value-factor/), [momentum](/momentum-factor/), [quality](/quality-factor/) — that can be modeled.
2. **Human judgment is biased.** Analysts and managers are subject to anchoring, overconfidence, herding, and other biases that quantitative models can avoid.
3. **Scale beats discretion.** A model can systematically evaluate thousands of [stocks](/stock/) and dimensions simultaneously; a human analyst cannot.
4. **Discipline matters.** A rules-based system forces consistent execution; humans often abandon strategies at the wrong time.

## How quant models work

A typical quantitative model:

1. **Defines signals.** Identifies measurable characteristics that historically correlate with future returns — e.g., low P/E, high earnings growth, high return on capital.
2. **Ranks stocks.** Scores each [stock](/stock/) by these signals, producing a ranking or predicted return.
3. **Constructs portfolio.** Selects and weights stocks based on the scores, often applying risk constraints.
4. **Backtests.** Tests the model against historical data to evaluate expected returns, volatility, and drawdowns.
5. **Rebalances mechanically.** Executes trades on a fixed schedule (monthly, quarterly) regardless of market conditions.

## Types of quant models

- **Factor models** target specific factors ([value](/value-factor/), momentum, quality) systematically.
- **Statistical arbitrage** models hunt for pairs or baskets that are mean-reverting.
- **Machine learning models** use neural networks or gradient boosting to predict returns from complex feature sets.
- **Sentiment models** extract signals from news, social media, or alternative data (credit card swipes, satellite imagery).
- **High-frequency models** exploit microsecond trading advantages and liquidity provision.

## Risks and limitations

- **Backtesting bias.** A model fit to historical data may be overfit, working great in backtest but failing forward.
- **Data mining.** With enough variables tested, some will show spurious correlation by chance alone.
- **Crowding.** As more capital chases the same factors, mispricings can disappear.
- **Fat tails.** Models trained on normal historical returns often underestimate crash risk.
- **Black boxes.** Complex models that work in backtest but whose logic is opaque are dangerous — the crash will be mysterious.

## See also

<div class="wiki-seealso">

### Closely related

- [Systematic investing](/systematic-investing/) — rules-based approaches
- [Factor investing](/factor-investing/) — systematic factor exposure
- [Smart-beta](/smart-beta/) — quantitative index weighting
- [Statistical arbitrage](/statistical-arbitrage/) — quantitative pair trading
- [Algorithmic trading](/trend-following/) — execution via algorithms

### Wider context

- [Stock](/stock/) — the underlying instruments
- [Stock market](/stock-market/) — the venue
- [Diversification](/diversification/) — model risk management
- [Alpha](/alpha/) — model return sources

</div>
