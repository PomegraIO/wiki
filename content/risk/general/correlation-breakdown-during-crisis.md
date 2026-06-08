---
title: "Correlation Breakdown During a Market Crisis"
description: "Why asset correlations spike toward one during crises, undermining diversification assumptions and concentrating portfolio risk."
keywords:
  - correlation breakdown during market crisis
  - correlation spike crisis
  - diversification breakdown stress
  - portfolio risk concentration crisis
image: /svg/risk.svg
---

*A **correlation breakdown during a market crisis** occurs when asset prices that moved independently or even inversely during calm periods begin moving together toward one, eliminating the diversification benefit that investors expected. This spike in correlation concentrates portfolio risk precisely when losses are largest.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Correlation Breakdown During Crisis — Key Facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Crises expose that diversification works until it is needed most.</div>

|   |   |
|---|---|
| **Normal-market correlation** | Often low or negative (e.g., 0.2 to 0.5 between stocks and bonds) |
| **Crisis-period correlation** | Often jumps to 0.8, 0.9, or near 1.0 |
| **What triggers it** | Flight to safety, margin calls, liquidity squeezes, systemic fear |
| **Portfolio impact** | Diversification benefit evaporates; losses compound across holdings |
| **Time window** | Days to weeks during acute stress; can persist for months |
| **Risk measure affected** | [Value at risk](/value-at-risk/) (VaR) and other models become unreliable |

</aside>

## The Normal-Market Assumption

In standard portfolio theory, [diversification](/diversification/) reduces risk because assets do not move in perfect lockstep. A portfolio of stocks, bonds, and real estate might assume correlations of 0.3 between stocks and bonds, implying they move somewhat independently. When stocks fall, bonds might rise or hold steady, offsetting losses. The portfolio's overall [volatility](/historical-volatility/) is lower than the simple average of its component volatilities.

This assumption holds well in stable markets where each asset class responds to its own fundamentals: interest rates drive bond prices; earnings and growth drive stocks; rents and cap rates drive real estate. In these conditions, correlations can even turn negative—bonds often rise when stocks fall because central banks cut rates to combat recession.

## What Happens During a Crisis

In acute market stress—a systemic banking crisis, a sudden policy shock, a black swan event—correlations across asset classes often jump toward 1.0. Stocks plummet; bonds initially rally but then stumble as credit spreads blow out; real estate assets are repriced downward as yields spike; commodities whipsaw as macro uncertainty dominates; alternative strategies suffer as prime brokers demand collateral.

The intuition is that during a true crisis, the dominant force is risk aversion and forced deleveraging. Investors and institutions no longer care about the specific fundamentals of each asset; they simply want to raise cash and reduce exposure. They sell good assets and bad indiscriminately, compressing the differences in how assets behave.

## Mechanisms Behind the Breakdown

**Flight to safety.** When fear spikes, investors scramble for the safest assets—Treasury bonds, the dollar, gold—creating a vacuum everywhere else. This creates a "risk-off" episode where anything remotely risky sells first. Stocks, high-yield bonds, equities in emerging markets, and illiquid assets all fall together.

**Margin calls and forced liquidation.** Many institutional investors and hedge funds use leverage. When one asset falls sharply, brokers demand additional collateral. To meet those calls, investors liquidate their most liquid positions—often the largest, most correlated holdings. This creates a feedback loop: selling begets forced selling, pushing all correlated assets down together.

**Liquidity crises.** In normal times, a trader can sell a large position and move on. In a crisis, bid-ask spreads widen and market depth disappears. To exit, sellers must accept worse and worse prices. This liquidity crisis hits stocks and bonds alike, synchronizing losses across the portfolio.

**Systemic risk recognition.** Investors suddenly perceive that risks are not independent but linked through counterparty exposure, funding channels, or macro feedback loops. A financial crisis reveals interconnection; a pandemic does the same. Once the linkage is clear, correlation estimates jump immediately.

**Monetary and fiscal regime shifts.** Sudden policy changes—emergency rate cuts, bailouts, controls on capital—reshape expectations across all assets simultaneously, driving correlated repricing.

## Historical Examples

The 2008 financial crisis saw stock-bond correlations spike from near zero to 0.6–0.8 as credit markets froze and equities cratered. Real estate, commodities, and emerging-market assets all fell in tandem. A portfolio that expected 60% stocks and 40% bonds to diversify received almost no diversification benefit during the acute phase.

The 2020 COVID crash saw similar dynamics for a few weeks: stocks, high-yield bonds, and risk assets all fell sharply on March 16–19 before central bank intervention stabilized conditions. Again, correlation breakdowns were acute but brief.

Even the 2022 bond rout (driven by Federal Reserve tightening) saw unexpected correlations between Treasuries and stocks, as both repriced off higher rates simultaneously.

## Impact on Portfolio Risk Models

Standard portfolio risk models—including [value at risk](/value-at-risk/) (VaR) and [capital adequacy](/capital-adequacy/) frameworks—typically use historical correlations or assume constant correlations. When correlations spike during crises, the model's predicted risk underestimates actual losses. A portfolio that the model says has a 5% daily loss risk suddenly experiences 10–15% daily declines. This is why banks use [stress testing](/stress-testing/) and [tail risk](/tail-risk/) measures alongside VaR.

The [sharpe ratio](/sharpe-ratio/) and other risk-adjusted performance metrics also become unreliable in crises because they are built on historical volatility and correlation estimates that break down during stress.

## The Role of [Factor investing](/factor-investing/) and Systematic Strategies

Correlations breaking down are especially painful for factor-based and systematic strategies. An investor buying value stocks and momentum simultaneously because the factor correlations are low might experience both factors crashing at once during a crisis. Similarly, [momentum investing](/momentum-investing/) itself can amplify correlation breakdown—once a drawdown starts, trend-following positions liquidate together, driving all correlated assets lower.

## Quantitative Implications

If two assets have a correlation of 0.3 in normal times and that jumps to 0.8 during a crisis, the [portfolio volatility](/volatility-smile/) can easily double. A simplified example:

- Two assets, equal weight, each with 20% volatility, normal correlation 0.3: portfolio volatility ≈ 16%
- Same assets, crisis correlation 0.8: portfolio volatility ≈ 24%

During an actual crisis, the individual asset volatilities also expand, compounding the effect.

## Can Diversification Be Preserved?

True diversification during crises requires holdings that are structurally uncorrelated—holdings that benefit from or are insensitive to systemic shocks. Some investors use options or [protective puts](/protective-put/) to hedge tail risk, accepting the cost of those protective instruments. Others hold cash or very-short-duration debt, which avoids correlation issues but carries lower returns. Still others use [credit default swaps](/credit-default-swap/) or volatility hedges.

The sobering reality is that perfect diversification during a crisis is expensive. Holding enough dry powder or hedges to offset correlation breakdown reduces returns in normal times. The trade-off between steady-state diversification and crisis protection is fundamental.

## See also

<div class="wiki-seealso">

### Closely related

- [Diversification](/diversification/) — the principle that correlation breakdown undermines
- [Value at risk](/value-at-risk/) — risk measure that fails when correlations spike
- [Tail risk](/tail-risk/) — the extreme outcomes that correlation breakdown creates
- [Stress testing](/stress-testing/) — method to assess portfolio losses in crisis scenarios
- [Systemic risk](/systemic-risk/) — the interconnectedness that reveals itself during crises

### Wider context

- [Market cycle](/market-cycle/) — phases where correlation structures shift
- Flight to safety — behavior driving correlation breakdowns
- [Factor investing](/factor-investing/) — strategy vulnerable to correlation spikes
- [Credit cycle](/credit-cycle/) — when credit crises trigger correlation breakdowns

</div>
