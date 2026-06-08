---
title: "Monte Carlo DCF Simulation"
description: "Using probability distributions instead of point estimates to calculate a valuation range with confidence intervals."
keywords:
  - monte carlo simulation
  - probabilistic valuation
  - sensitivity analysis
  - confidence intervals
  - dcf probability distribution
  - valuation uncertainty
image: "/svg/valuation.svg"
---

*A **Monte Carlo DCF simulation** replaces fixed assumptions with probability distributions for revenue, margins, growth, and discount rates, then runs thousands of iterations to produce a range of possible valuations rather than a single point estimate. This approach reveals the distribution of outcomes and quantifies valuation uncertainty.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Monte Carlo DCF — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Turning deterministic models into probability distributions.</div>

|   |   |
|---|---|
| **What it is** | Stochastic valuation method using iterative sampling |
| **Also called** | Probabilistic DCF, stochastic valuation, Monte Carlo analysis |
| **Replaces** | Point estimates with probability distributions across inputs |
| **Typical iterations** | 5,000–10,000+ per valuation |
| **Output** | Valuation range with percentiles and confidence bounds |
| **Best for** | High-uncertainty businesses or novel ventures |

</aside>

## How Monte Carlo overcomes false precision

A traditional [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) model plugs fixed numbers into a formula and returns a tidy number—say, $150 per share. In reality, nearly every assumption carries uncertainty. Revenue could grow at 5% or 12%. Operating margins might compress from regulation. The [discount-rate](/discount-rate/) shifts with interest rates. A point estimate masks this scatter.

Monte Carlo simulation acknowledges that unknowns are unknowns. Instead of assuming "revenue grows at 8%," you define a distribution: perhaps 60% probability of 6–10%, 30% of 10–14%, 10% of under 6%. You do the same for margins, capex ratios, terminal growth, and the discount rate. The algorithm then randomly samples from each distribution thousands of times, recalculating the valuation each iteration. The result is not "$150" but a probability distribution: "40% chance valuation exceeds $160; 50% chance it lands between $130 and $170."

This is honest. It shows what you know and what you don't.

## The mechanics of random sampling

The simulation engine works in a loop:

1. **Define distributions.** For each input (revenue growth, EBITDA margin, capex-to-revenue, [terminal-growth](/yield-to-maturity/), [discount-rate](/discount-rate/)), specify the shape: normal (bell curve), triangular, uniform, or empirical (historical percentiles). Include correlations if some variables move together—higher growth often pairs with margin pressure.

2. **Sample once.** Draw one random value from each distribution. Not cherry-picked; genuinely random, respecting the shape you specified.

3. **Run one full DCF.** Feed these sampled values through your [cash-flow-statement](/cash-flow-statement/) forecast, terminal-value calculation, and [net-present-value](/discounted-cash-flow-valuation/) computation. Write down the result.

4. **Repeat.** Go back to step 2. Do this 5,000, 10,000, or 50,000 times.

5. **Analyze the distribution.** Examine the sorted results. What percentile lands where? Plot a histogram. The shape tells you whether outcomes cluster or spread.

A 5,000-iteration run takes seconds on modern hardware; each passes through the same financial logic once, then discards its intermediate values.

## Interpreting the output: ranges and tails

When the run finishes, you have a list of 5,000 valuation numbers. The arithmetic mean is one "fair value," but the median, 25th percentile, and 75th percentile are often more useful. If the 25th percentile is $120 and the 75th is $180, half of your plausible scenarios fall in that band.

The shape of the distribution reveals risk. If it's symmetric—bell-shaped—the mean and median align, and the business is "normally" uncertain. If it's skewed left, the downside tail is long; a few bad scenarios crater the valuation dramatically. If skewed right, the upside is open-ended. This tail behaviour matters more than the central estimate if you're a risk manager or contrarian investor.

The _tails_ themselves are instructive. The 5th percentile tells you "barely one scenario in twenty falls below this." The 95th, vice versa. Some practitioners widen these to 1st and 99th for stress-testing. If a 1st-percentile outcome is still solvent and profitable, the business is resilient.

## When to use Monte Carlo, and when not to

Monte Carlo excels when assumptions carry material, quantifiable uncertainty and the distribution shapes are defensible. A biotech valuing a drug pipeline with success probabilities? Perfect. A mature utility projecting stable cash flows? Overkill.

The method also shines for screening. If a valuation is sensitive to only three variables—say, revenue growth, margin, and the discount rate—Monte Carlo quickly reveals which of your 5,000 scenarios survive a given hurdle price. That informs how tight your margin of safety needs to be.

The catch: garbage in, garbage out. If you define distributions carelessly—pulling percentiles from thin air rather than historical data or expert consensus—the output looks rigorous but is just random noise dressed as science. You must justify each distribution shape and parameter. A triangular distribution (most-likely, upside, downside) forces you to pick three points explicitly; a normal curve with a standard deviation requires thought about what "one standard deviation" means for your business.

Correlation assumptions matter too. Ignoring that revenue growth and margin often move together—or move _opposite_—can understate or overstate volatility. Professional simulations often include a correlation matrix to capture these linkages.

## Practicalities: spreadsheets and dedicated tools

You can build a Monte Carlo model in Excel using RAND() and NORM.INV() functions to draw random samples, but 5,000 iterations become tedious. Most practitioners use dedicated software: @Risk, Crystal Ball, SimVoi, or Python libraries like scipy.stats and numpy. These let you define distributions with a few clicks, specify correlations, run iterations in parallel, and export percentile charts instantly.

The output—a valuation range with confidence intervals—then feeds into portfolio decisions. If you're building a [short-selling](/short-selling/) case, you care about the downside tail. If you're a long-term compounder buying with a margin of safety, the median and 25th percentile might be your frame.

## See also

<div class="wiki-seealso">

### Closely related

- [Scenario Analysis DCF](/scenario-analysis-dcf/) — constructing discrete bull, base, and bear cases with probability weights
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the foundation model that Monte Carlo refines
- [Sensitivity Analysis](/sensitivity-analysis-valuation/) — testing how outputs shift with single-variable changes
- [Discount Rate](/discount-rate/) — a key input and often a significant source of valuation uncertainty
- [Free Cash Flow](/free-cash-flow/) — the core input to any DCF, including Monte Carlo

### Wider context

- Valuation — broad overview of pricing approaches
- Risk — conceptual foundation for understanding why distributions matter
- [Value Investing](/value-investing/) — philosophical approach that often pairs with probabilistic thinking
- Margin of Safety — why knowing your distribution tail matters to investors

</div>
