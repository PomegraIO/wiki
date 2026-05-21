---
title: "Scenario Valuation"
description: "A valuation approach that explicitly models discrete, named scenarios (bear, base, bull) with different assumptions and probabilities, rather than relying on single-point estimates."
keywords:
  - scenario analysis
  - scenario valuation
  - bear case
  - base case
  - bull case
image: "/svg/valuation.svg"
---

*A **scenario valuation** avoids the false precision of a single intrinsic value by explicitly modeling 3–5 named scenarios (pessimistic, base, optimistic) with different assumptions and assigned probabilities. The result is a weighted expected value and, more importantly, transparency about the range of outcomes and the key drivers of that range. It is a practical, honest alternative to [DCF](/discounted-cash-flow-valuation/) point estimates or [Monte Carlo](/monte-carlo-valuation/) simulations.*

## The structure

**Bear case.** Pessimistic scenario. Company grows slowly, faces competitive pressure, margins compress. This case is not "default the company will be bankrupt." It is "growth is 2% instead of 5%, margins are 18% instead of 22%."

**Base case.** Most likely. Company executes as planned, industry grows at expected rate, execution is on track.

**Bull case.** Optimistic. Company wins market share, adjacent markets open up, margins expand.

Occasionally, a fourth case—a disaster case—is added for very high-risk scenarios.

Each scenario gets explicit assumptions: revenue growth, margins, capex, terminal growth, cost of capital. Some assumptions (cost of capital) might be the same across scenarios; others (growth, margins) differ significantly.

## Example

A biotech company with a drug in late-stage trials:

**Bear case (20% probability):**
- Drug fails clinical trial. Company pivots to pipeline programs but loses 2 years.
- Intrinsic value: 500 million (much lower, as the immediate growth opportunity evaporates)

**Base case (60% probability):**
- Drug is approved on schedule. Company gains market share over 5 years.
- Intrinsic value: 2 billion

**Bull case (20% probability):**
- Drug approved early, broader indication approved, becomes blockbuster.
- Intrinsic value: 5 billion

**Expected value:** 0.20 × 500M + 0.60 × 2B + 0.20 × 5B = 100M + 1.2B + 1B = 2.3 billion

The company's expected intrinsic value is 2.3 billion, with a wide range (500M to 5B) reflecting the major binary event (drug approval).

## Advantages over DCF

**Explicit about uncertainty.** A DCF might estimate intrinsic value at 2 billion, hiding the fact that there is a 20% chance of 500 million. Scenario analysis is transparent: the range is 500M to 5B.

**Easier to communicate.** Boards and investors understand "bear, base, bull." They understand the probabilistic framework. A single DCF with perpetual growth assumptions is abstract.

**Accounts for bimodal outcomes.** For binary events (drug approval, regulatory approval, bankruptcy), discrete scenarios are more honest than continuous distributions.

**Highlights key decision points.** What is the value if the drug fails? If it gets approved early? This forces clarity on what matters.

## Disadvantages

**Requires explicit probabilities.** How likely is the bear case? 20% or 30%? Picking probability is subjective.

**Missing outcomes.** If there are more than three or four plausible outcomes, you are omitting some. Monte Carlo is better if there are dozens of possible outcomes.

**No guidance on decision-making.** A scenario valuation tells you the value is 2.3 billion on average, with 500M to 5B range. But does that mean buy, hold, or sell? You need to decide your required return.

**Assumed independence.** Scenarios often assume outcomes are discrete, but in reality, they might be correlated. A bear case might involve both failed drug trial and margin pressure. Scenario analysis doesn't easily capture this.

## Building the scenarios

**Identify key decision points or uncertainties.**
- Will the drug be approved?
- Will the company win this major contract?
- Will the regulatory environment become hostile?
- Will a competitor disrupt the market?

**Build discrete scenarios around these.**
- Drug approval vs. failure (two scenarios)
- Contract win vs. loss (two scenarios)
- Combine to get four scenarios, assign probabilities

**For each scenario, forecast financials.**
- Revenue: what is the growth rate in this scenario?
- Margins: are they higher or lower?
- Capex: does the scenario change capex needs?
- Cost of capital: is the company riskier or safer in this scenario?

**DCF each scenario.**
- Calculate intrinsic value in bear, base, bull
- Verify that valuations align with scenario assumptions

**Assign probabilities.**
- Sum to 100%
- Be explicit and defensible: "Drug approval is 70% based on phase 3 data and typical approval rates"

**Calculate expected value.**
- Weighted average of scenario values

## When scenario valuation is most useful

**Binary outcomes.** Drug approval, regulatory decision, contract win/loss. Discrete scenarios are ideal.

**Early-stage or distressed companies.** Value depends heavily on one or two key events. Scenario analysis captures this.

**Strategic options.** "If we acquire Company X, value is Y. If we don't, value is Z." Scenarios model this.

**Turbulent environments.** In recession, geopolitical crisis, or sector disruption, discrete scenarios (recession vs. recovery, trade war vs. resolution) are more realistic than a smooth DCF.

## When DCF is better

**Mature, stable businesses.** A utility or grocery chain has slow, predictable evolution. Continuous distribution is appropriate.

**When you have many drivers.** If value depends on dozens of inputs (market share, pricing power, cost structure, capex policy), Monte Carlo or DCF with sensitivity is better than three scenarios.

## Combining scenarios with DCF

Many practitioners use both: build 3–5 scenarios, DCF each, then calculate expected value. This is scenario-based DCF—powerful and credible.

It avoids the false precision of a single DCF while capturing complexity through detailed scenario analysis.

## See also

<div class="wiki-seealso">

### Closely related

- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — underlying method per scenario
- Expected value — probability-weighted outcome
- Decision tree — structuring scenarios
- Probability — assigning to scenarios

### Uncertainty and sensitivity

- [Sensitivity analysis](/sensitivity-analysis-valuation/) — which variables drive value
- [Monte-Carlo valuation](/monte-carlo-valuation/) — continuous uncertainty
- [Football field valuation](/football-field-valuation/) — visualizing ranges

### Application areas

- Risk assessment — identifying key risks
- Strategic options — valuing decision choices
- Merger integration — valuing combined company scenarios

</div>
