---
title: "Portfolio of Real Options: Why Project Values Are Not Simply Additive"
description: "A portfolio of real options values nonlinearly because options interact through correlation and timing effects. Learn why simple summing overstates value."
keywords:
  - portfolio of real options
  - real options correlation
  - real options interaction effects
  - option value nonlinearity
  - multiple projects valuation
  - real options timing
image: "/svg/valuation.svg"
---

*When a firm owns multiple real options—expansion, abandonment, or flexibility in production—the total value is not the sum of the individual option values. Options interact through correlation and timing effects: exercising one option can reduce or eliminate the value of another, or it can accelerate or delay exercise of a third. A portfolio of real options requires modeling these interactions, not just adding up the pieces.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Portfolio of Real Options — Why Values Don't Add</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Interaction effects mean a firm's real option value is less than the sum of standalone values.</div>

|   |   |
|---|---|
| **Value if options were independent** | Sum of individual option values |
| **Actual portfolio value** | Lower, due to interaction effects |
| **Key interaction sources** | Competition between options, shared cash flows, mutually exclusive choices, capacity constraints |
| **Correlation effect** | Options on the same underlying variable are correlated; joint value depends on joint distribution, not individual distributions |
| **Timing interaction** | Exercising one option can trigger or prevent exercise of another (path dependency) |
| **Intuition** | Options are valuable because they provide flexibility; using flexibility in one direction often forecloses it in others |

</aside>

## The Aggregation Problem

Suppose a pharmaceutical firm owns three real options: (1) expand a manufacturing facility, (2) enter a new geographic market, and (3) abandon a low-margin product line if competitor drugs arrive. An analyst values each option using [Black-Scholes](/black-scholes-model/) or a binomial tree and concludes the three options are worth 50 million, 30 million, and 20 million euros, respectively. Total = 100 million euros.

But this sum almost certainly **overstates the true value** of the portfolio. Why? Because the options interact. If the firm exercises the expansion option early, it consumes cash that would otherwise be available to fund the geographic entry. If competitors arrive faster than expected, the abandon option's value spikes, but the geographic entry option becomes worthless. Options on correlated assets do not behave like independent financial instruments.

This is the portfolio of real options problem: recognizing and quantifying how multiple strategic flexibilities interact.

## The Sources of Interaction: Correlation

**Correlation** is the primary source of interaction. In financial options, two independent call options on unrelated stocks can be valued separately and summed. Their payoffs are uncorrelated. But real options rarely operate on uncorrelated underlying variables.

Consider a mining firm with two real options:
1. **Expand production** if commodity prices rise.
2. **Abandon the mine** if commodity prices fall.

Both options depend on the same underlying variable—commodity price. They are perfectly negatively correlated: when the expand option is in-the-money (price is high), the abandon option is out-of-the-money (price is not low). The value of the portfolio is not the sum of the two individual values; it is the value of a single option to choose between expansion and abandonment, conditional on a single price path.

The portfolio value is **subadditive**: the whole is less than the sum of the parts.

More generally:
- **Positively correlated options**: Both options benefit if the underlying variable moves in the same direction (e.g., two expansion options, each triggered by rising demand). Their joint value is less than the sum because exercising one can saturate demand, making the second less valuable. They compete for the same upside.
- **Negatively correlated options**: Options that benefit from opposite movements (e.g., expand and abandon). They are mutually exclusive in effect. Only one is worth exercising, so the portfolio behaves like a single option.

## The Sources of Interaction: Mutually Exclusive Choices

Many real options are mutually exclusive by nature. A firm cannot simultaneously operate a plant in Germany and operate the same plant in Poland; it must choose one. The options are not independent choices but a decision tree.

A pharmaceutical company pursuing R&D for two drugs faces a similar constraint if it has limited testing resources or regulatory bandwidth. Pushing Drug A forward faster may delay Drug B. The value of the portfolio (Drug A option + Drug B option) is less than the sum because the constraints are binding.

In formal option terms, the portfolio value is determined by the optimal stopping rule: the firm exercises the option that is most valuable at each moment, conditional on the state of the world at that moment. The total value is not the sum of values in isolation; it is the value of the optimal strategy over the entire portfolio.

## The Sources of Interaction: Shared Cash Flows and Capacity

Real options in a firm often share cash flows and capacities. If the firm has a budget of 100 million euros, it can expand the factory (costs 60 million, NPV[+50 million) or enter a new market (costs 70 million, NPV 40 million), but not both. The option to do both is worth less than the sum because of the constraint.

Similarly, if both options generate future cash flows that contribute to the same budget, the firm's ability to exercise subsequent options (like a second-stage expansion or a hedge) is constrained. The option to do all three things is less valuable than the sum of three independent options because cash and management attention are limited.

## Quantifying the Interaction: A Stylized Example

A manufacturing firm owns two real options:

**Option 1: Expand capacity** if demand grows.
- Standalone value (using binomial): 40 million euros.

**Option 2: Pursue a new product line** if demand also grows.
- Standalone value (using binomial): 30 million euros.

Naïve sum: 70 million euros.

Both options depend on the same demand growth variable. In the model:
- Demand grows with probability 60 % (high state) and stays flat with probability 40 % (low state).
- In high state, expansion is worth 50 million and new product is worth 35 million.
- In low state, both are worth near zero.

If evaluated separately:
- Expansion option value ≈ 0.6 × 50 million + 0.4 × 0 = 30 million (before discounting and early exercise).
- New product value ≈ 0.6 × 35 million + 0.4 × 0 = 21 million (before discounting and early exercise).

But the firm does not get both. If demand grows, the firm can pursue expansion, which requires 60 million investment and yields 50 million payoff, for a net 10 million gain. Or it can pursue new product, which requires 40 million and yields 35 million, for a net 5 million gain. The firm will choose expansion (higher net gain). The firm cannot do both because cash is constrained.

**Portfolio value** = value of optimal strategy = approximately 0.6 × 50 million (expansion) + 0.4 × 0 (low state) = 30 million, **not 51 million**.

The interaction effect subtracts roughly 20 million from the naïve sum, reflecting the constraint that only one option can be exercised in full.

## Timing and Path Dependency

Interactions also arise through **path dependency**. The value of exercising an option today depends on what the future looks like. And what the future looks like is shaped by what options have already been exercised.

Suppose a tech company owns:
1. An option to acquire a startup (option expires in 2 years).
2. An option to build an internal team to develop the same technology (can start any time).

If the market booms and the company acquires the startup, the internal team option vanishes (there is no longer a strategic need). But in the binomial model, these look like independent options: (1) acquire at some future exercise price, (2) build internally at some future cost. The portfolio value that treats them as independent ignores that acquisition makes the internal build redundant.

More subtly, exercising option 1 early (acquiring the startup quickly) may change the decision rule for option 2 (there is less need to ever build internally). The timing of option 1 affects the timing and value of option 2. These path dependencies cannot be captured by separately valuing each option in isolation.

## Methods for Valuing a Portfolio

**Binomial trees and decision trees** remain the most practical approach. The analyst models the evolution of the underlying variable (commodity price, demand, technology state) and at each node decides which option is optimal to exercise, given all remaining options. The tree is solved backward from the terminal nodes, and the resulting value captures all interaction effects.

**Monte Carlo simulation** can also be used for complex portfolios. For each simulated path of the underlying variable, the analyst determines the optimal sequence of option exercises and calculates the resulting cash flows. The average across many paths gives the portfolio value. This approach is flexible and can handle path dependency and multiple underlying variables, but it is computationally intensive and requires careful calibration of decision rules (when exactly should option X be exercised?).

**Simplified analytical approaches** exist for special cases. If all options depend on a single underlying variable and there are no cash flow constraints, some interactions can be modeled semi-analytically. But in general, portfolio effects require simulation or tree-based models.

## Why This Matters in Practice

Naive summing of option values leads to overvaluation of projects and strategies. A firm that overstates the value of a portfolio of options may overinvest, committing resources to projects that do not actually create value when interactions are accounted for.

Conversely, recognizing interactions can reveal hidden value. If the firm owns a set of options that are well-coordinated (each option makes other options more valuable), the actual portfolio value can exceed the sum. This is less common than subadditivity, but it happens when options are complementary—for example, an option to expand production and an option to access new markets (both expand value if pursued together).

For strategic planning, understanding portfolio interactions clarifies which options to pursue and in what order. The optimal strategy is not to sum the values and exercise the highest-value option; it is to consider the entire decision tree and choose the path that maximizes total firm value.

## See also

<div class="wiki-seealso">

### Closely related

- Real Options — Overview of real option valuation
- [Option Premium](/option-premium/) — What drives the value of optionality
- Binomial Tree Valuation — Practical method for multi-stage decisions
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — The baseline method that real options extend
- [Sensitivity Analysis (Valuation)](/sensitivity-analysis-valuation/) — How to test robustness of option values

### Wider context

- Capital Budgeting — Framework for project selection and investment
- [Scenario Analysis](/scenario-analysis/) — Modeling future states of the world
- Correlation in Portfolios — How correlation reduces diversification benefits
- [Black-Scholes Model](/black-scholes-model/) — Financial option pricing foundations

</div>
