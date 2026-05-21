---
title: "Monte Carlo Valuation"
description: "A probabilistic valuation method that simulates thousands of possible scenarios for key assumptions, generating a distribution of possible valuations rather than a single point estimate."
keywords:
  - Monte Carlo
  - simulation
  - probabilistic valuation
  - scenario analysis
  - uncertainty
image: "/svg/valuation.svg"
---

*A **Monte Carlo valuation** replaces the single point estimate of a standard [discounted cash flow](/discounted-cash-flow-valuation) model with a distribution of possible outcomes. Instead of assuming revenue grows at exactly 10%, you assume it is normally distributed with a 10% mean and 3% standard deviation. Then you run 10,000 simulations, each with different random draws of revenue, margins, and other variables. The result is a distribution of intrinsic values, not a single number.*

## How it works

**Step 1: Identify key uncertain variables.** Revenue growth, EBITDA margins, capex as a percentage of sales, working capital changes, discount rate, perpetual growth rate.

**Step 2: Specify probability distributions.** For each variable, choose a distribution. Revenue growth is normally distributed around 10% with 3% standard deviation. Perpetual growth is triangular, with low (1%), most likely (2.5%), and high (4%) values.

**Step 3: Run simulations.** A Monte Carlo engine generates 10,000 random scenarios. In scenario 1, revenue grows 9%, margins are 38%, capex is 4% of sales, etc. In scenario 2, different random values. In scenario 10,000, different again.

**Step 4: Calculate intrinsic value for each scenario.** For each of the 10,000 scenarios, build a DCF and calculate intrinsic value per share.

**Step 5: Analyze the distribution.** Look at the 5th percentile (pessimistic), 50th percentile (median), and 95th percentile (optimistic). Graph the distribution.

**Output.** Instead of "intrinsic value is 50 per share," you get "intrinsic value is likely between 35 and 75 per share, with a median of 52."

## Advantages

**Captures uncertainty honestly.** Instead of pretending one set of assumptions is correct, you acknowledge a range.

**Identifies key drivers.** A sensitivity analysis shows which variables most drive the valuation range. If the 5th-to-95th percentile spread is driven entirely by perpetual growth assumptions, you know the valuation is fragile.

**Handles correlations.** If you assume revenue growth and margins are correlated (when growth is high, margins are pressured), Monte Carlo can model this.

**Provides decision-relevant output.** A board asking "what is the value?" gets "it's probably between 35 and 75, most likely around 50." This guides decision-making better than a false precision of $50.23.

## Disadvantages

**False precision.** Running 10,000 simulations suggests high analytical rigor, but if your input distributions are guesses, the output is still a guess dressed up in false confidence.

**Garbage in, garbage out.** If you specify a normal distribution for revenue growth with 3% standard deviation, but in reality, growth could be anywhere from -20% to +50%, your distribution is wrong.

**Parameter uncertainty.** Monte Carlo handles uncertainty in variables (revenue growth might be 8–12%), but not uncertainty in the structure (is the company cyclical or not?). [Scenario analysis](/scenario-valuation) with discrete cases is better for that.

**Time and complexity.** Setting up a rigorous Monte Carlo model is more work than a simple DCF. Most teams won't bother.

## Distribution choices

**Normal distribution.** Suitable for most revenue and margin assumptions. Symmetric around the mean.

**Triangular distribution.** Useful for variables with clear bounds. Perpetual growth from 1% to 4%, most likely 2.5%—fit a triangle.

**Lognormal distribution.** Better for variables that cannot be negative (revenue, EBITDA) and are right-skewed (occasional big gains, but downside is bounded at zero).

**Uniform distribution.** Every value within the range is equally likely. Rarely realistic but sometimes used when you have no better information.

## Correlations matter

If you assume all good things happen together (high revenue growth, high margins, low cost of capital), you will overestimate upside and overestimate the probability of high valuations.

Most Monte Carlo models should include negative correlations: when growth is high, margins are often pressured by competition. When rates rise, discount rates rise. Specifying correlations makes the output more realistic.

## Sensitivity within Monte Carlo

Most Monte Carlo platforms allow you to extract sensitivity information: "which variable, when varied, most affects the output distribution?" This is more reliable than a traditional sensitivity table because it accounts for realistic ranges and correlations.

## Limitations and pitfalls

**Overconfidence from precision.** Seeing a distribution with percentiles (5th, 50th, 95th) makes it feel scientific. But if the 5th percentile is 35 because you didn't truly account for the 1-in-20 risk of company bankruptcy, the precision is false.

**Model risk.** A DCF model is always incomplete. Monte Carlo doesn't fix this; it just quantifies uncertainty within the model.

**Impossible scenarios.** With 10,000 scenarios, you will occasionally get scenarios that are unrealistic or contradictory (high growth, high margins, declining ROI). These noise outcomes contaminate the distribution.

## When Monte Carlo is worth doing

**Large, high-stakes decisions.** A 500 million acquisition or a 50 million capex decision justifies the modeling effort.

**Unknown but important variables.** If perpetual growth (which dominates valuation) is genuinely uncertain, Monte Carlo is better than single-point estimates.

**Hedging and risk management.** Understanding the distribution of outcomes is useful for hedging or insurance decisions.

**Academic or advisory work.** Consultants and academics often use Monte Carlo to show sophistication, though it is not always necessary.

## Simpler alternative: scenarios

For many situations, three scenarios (bear, base, bull) with explicit probability weights are more practical and often more honest:

- Bear case: 20% probability, 30 per share value
- Base case: 50% probability, 50 per share value
- Bull case: 30% probability, 70 per share value
- Expected value: 0.2 × 30 + 0.5 × 50 + 0.3 × 70 = 51 per share

This captures uncertainty and provides output similar to Monte Carlo without requiring probability distributions for dozens of variables.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation) — the base model
- [Scenario valuation](/scenario-valuation) — discrete outcomes
- [Sensitivity analysis](/sensitivity-analysis-valuation) — variable sensitivity
- Uncertainty — what Monte Carlo handles

### Probability and distributions

- Probability distribution — input to Monte Carlo
- Expected value — output concept
- Risk — captured by simulation

### Analysis and output

- [Football field valuation](/football-field-valuation) — visualizing ranges
- Decision analysis — using distributions for decisions
- [Value at risk](/value-at-risk) — related concept in finance

</div>
