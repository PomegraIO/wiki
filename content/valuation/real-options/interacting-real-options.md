---
title: "Interacting Real Options"
description: "How multiple options embedded in a single investment project interact such that their combined value is less than the sum of individual options, or sometimes more—a critical insight for valuing complex assets."
keywords:
  - real options
  - option interactions
  - portfolio of options
  - non-additive value
  - complex projects
image: "/svg/valuation.svg"
---

*A project rarely offers just one option—the choice to invest or wait. Instead, a single asset might embed an option to expand production, an option to switch to alternative inputs, an option to abandon, and an option to defer maintenance. These **interacting real options** do not add their values linearly. Instead, they interact, sometimes amplifying each other, sometimes cancelling out, creating valuation puzzles that simple sum-of-parts frameworks miss entirely.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interacting Real Options — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation concepts." />

<div class="wiki-infobox-caption">When multiple embedded options on one asset create non-additive value.</div>

|   |   |
|---|---|
| **What it is** | Co-existing options on the same asset whose combined value deviates from the sum of individual option values |
| **Also called** | Option interaction, compound options, correlated optionality |
| **Common pairing** | Option to expand + option to abandon |
| **Common pairing** | Option to defer + option to switch |
| **Typical outcome** | Subadditivity (whole < sum) when options compete for the same resource or scenario |
| **Less common outcome** | Superadditivity (whole > sum) when options complement and amplify |

</aside>

## Why options interact

Imagine a manufacturing plant. It offers an option to **expand capacity** (add a second production line if demand booms) and an option to **abandon** (exit the market if demand collapses). A naive valuation adds their individual option values. But the two options compete. In a boom scenario, both options seem "in-the-money": expand to capture upside *and* abandon to limit downside. But you cannot simultaneously expand and abandon the same asset—there is only one capital budget, one management team, one set of customers. In the boom state, management will choose to **expand, not abandon**. The value of the abandon option in that scenario is effectively zero.

This is **subadditivity**: the joint value of expand + abandon is less than the sum of their standalone values, because in many future states, only one option is economically rational to exercise. The other option is crowded out.

More broadly, option interactions arise from four mechanisms:

1. **Mutual exclusivity.** Expand and abandon are mutually exclusive within a single scenario; only one can be exercised at a time.
2. **Resource constraints.** If both options require the same scarce input (capital, management time, production capacity), exercising one limits the upside from the other.
3. **State-dependent payoffs.** The payoff from one option depends on whether another option has already been exercised. Once you've abandoned, you cannot expand.
4. **Volatility clustering.** If two options thrive in opposite volatility regimes (one gains from price spikes, another from price crashes), they may partially hedge each other, reducing joint value.

## Subadditivity: The typical case

Subadditivity is the default. A classic example is a mine or timber forest with:

- **Option to expand:** invest extra capital to increase extraction rate, boosting cash flows in a strong commodity cycle
- **Option to shrink:** cut production and harvest overhead to survive a price trough
- **Option to abandon:** walk away entirely if prices fall below salvage value

A commodity boom triggers the expand option; exercise it, and the abandon option becomes moot—you are thriving, not desperate to exit. A crash triggers the abandon option; exercise it, and the shrink option is irrelevant—you've already left. The three options rarely activate together. Summing their standalone values overstates the project's true optionality.

Quantitatively, if the three options are valued independently at $50M (expand), $30M (shrink), and $20M (abandon), a naive sum is $100M. The true joint value might be $60–75M, a discount of 25–40%. The gap is the cost of optionality interplay.

Some empirical evidence: projects with highly correlated embedded options (expand and contract, both sensitive to the same commodity price) see 20–50% subadditivity. Projects with uncorrelated options (abandon tied to regulatory risk, expand tied to demand shocks) see less discount—sometimes even modest superadditivity, as one option hedges the other.

## Superadditivity: Rare but real

Occasionally, options amplify. Consider a **startup with a product option** (invest in feature A) and a **pivot option** (shift the entire business model to target Y). In isolation, each option's value is modest—low probability of success, binary outcomes. But together, they create optionality on top of optionality. If feature A flops, the pivot option becomes more valuable: management can redirect effort toward Y without sunk losses in A. The existence of the pivot option increases the expected payoff of feature A (since failure is less catastrophic), raising its value. Simultaneously, the success of feature A refines the market signal, informing the pivot decision. The two options **compound**, sometimes yielding superadditivity.

This is rarest in mature, stable industries (mining, utilities, real estate), where options tend to be substitutes. It emerges in tech and biotech, where options are complements—each enhances the strategic optionality of the other.

## Valuation challenges

Pricing interacting options requires either:

1. **Monte Carlo simulation.** Model each future state, compute the optimal exercise decision in each state (considering all co-existing options), and discount back. This is computationally feasible but parameter-heavy and often opaque.
2. **Trinomial or lattice trees.** Discretize the state space and recursively solve for optimal policy at each node. More transparent, but can become intractable for many options or long horizons.
3. **Closed-form approximation.** For special cases (e.g., two correlated options, geometric dynamics), academic literature provides formulas. But these are rare and narrow.

In practice, most practitioners use simulation because it scales to messy real problems: phased funding, contractual constraints, management constraints, and multiple correlated uncertainties (commodity prices, interest rates, regulatory shifts, competitor actions).

A critical mistake: summing standalone option values and calling it done. This approach is simple but often wrong. A project with three $50M options is rarely worth $150M; it might be $90–110M, depending on correlation structure. Overlooking interaction can badly overvalue assets or leave value unidentified during negotiation.

## Implications for capital budgeting

Firms that recognize option interaction gain a strategic edge:

- **Valuation discipline.** Do not sum options; model the full state tree.
- **Portfolio rebalancing.** If options are subadditive, firms may choose to exercise early (sacrificing some option value) to reduce crowding and improve capital efficiency.
- **Staging and gates.** Multi-stage projects with stage-gate funding allow later stages to be tailored based on earlier option outcomes. This structure inherently reduces interaction costs.
- **Hedging.** If two options have opposite sensitivities (one gains when prices spike, another when they crash), natural hedges can be exploited.

The subtlest insight: in high-uncertainty environments with many embedded options (like biotech or venture capital), the traditional capital budgeting framework (sum the NPV plus the option values) is not just incomplete—it can be systematically misleading. A portfolio of 10 uncorrelated options, each worth $5M, does not sum to $50M; true joint value might be $20–30M. Conversely, a few strategically correlated options can create superadditivity, generating value greater than the sum of parts. Rigorous modeling of interaction is the only path to defensible valuations.

## See also

<div class="wiki-seealso">

### Closely related

- [Option Exercise Boundary](/option-exercise-boundary/) — the trigger point for optimally exercising any single option
- [Value of Waiting](/value-of-waiting/) — the optionality created by deferral and irreversibility
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the NPV baseline against which option value is measured
- [Sensitivity Analysis (Valuation)](/sensitivity-analysis-valuation/) — testing how project value responds to parameter uncertainty
- [Volatility Smile](/volatility-smile/) — how volatility itself varies, affecting option payoffs

### Wider context

- Capital Allocation — investment prioritization and portfolio construction
- Risk Management — hedging and diversification across multiple uncertain dimensions
- [Scenario Analysis](/scenario-analysis/) — exploring future states to understand option payoffs
- [Market Timing](/market-timing/) — decision timing under uncertainty in portfolio management

</div>
