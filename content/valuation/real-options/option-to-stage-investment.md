---
title: "Option to Stage an Investment: Phased Capital Commitment"
description: "How breaking a large capital project into sequential phases creates an embedded option to proceed or halt, and how the staging premium is calculated."
keywords:
  - option to stage investment
  - phased capital commitment
  - staged development value
  - wait-and-see investment option
  - option to abandon phased investment
image: /svg/valuation.svg
---

*Most large capital projects are not bets that land all at once. Instead, they unfold in phases. A pharmaceutical company spends $50 million on Phase II trials, and only if results are promising does it commit $150 million to Phase III. A real estate developer builds and leases a first building, and only if it performs does it build phase two. A mining company runs a pilot extraction plant, and only if engineering works out does it commit to full-scale mining. This structure is not just a practical quirk—it is a **real option**. By breaking the project into sequential phases, management retains the **option to stage an investment**, a choice right that adds value. Ignoring this optionality leads to systematic undervaluation of phased projects.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Staging Options — key drivers</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Breaking investment into phases creates decision gates where management can proceed, pause, or abandon.</div>

|   |   |
|---|---|
| **Phase 1 cost** | $C_1$; reveals some information; success rate $p_1$ |
| **Phase 2 cost** (contingent) | $C_2$; only incurred if Phase 1 succeeds; success rate $p_2$ |
| **Phase N cost** (contingent) | $C_N$; final phase; completion success $p_N$ |
| **Terminal value** | $V$ if all phases succeed; $0$ if any phase fails |
| **Option premium** | Value of staging *minus* value of committing to all phases upfront |

</aside>

## The Intuition: Why Staging Reduces Risk

Imagine you are considering a $500 million capital project. A naïve approach is to estimate all costs and benefits, run a [discounted cash flow](/discounted-cash-flow-valuation/) calculation, and decide immediately: full commit or walk away.

But suppose there is material uncertainty in the project's feasibility. Perhaps the underlying technology is unproven, or the market size is unclear. Sinking $500 million in a single lump sum exposes you to the risk that $400 million in capital is already spent *before* you discover the project will not work.

Now consider an alternative: break the investment into two phases:

- **Phase 1** ($100 million, 1 year): Build a prototype, run pilots, de-risk the technology. Success rate: 60%.
- **Phase 2** ($400 million, 2 years): Full-scale production and deployment. Contingent on Phase 1 success; success rate if Phase 1 works: 80%.

If Phase 1 fails (40% chance), you lose $100 million but avoid losing the remaining $400 million. If Phase 1 succeeds, you then *decide* whether to commit Phase 2 based on new information gained. This staged approach has asymmetric payoff: you keep your downside capped while retaining upside if conditions evolve favorably.

That asymmetry is the essence of an embedded [option](/option/).

## Calculating the Option Value

Let's work a numerical example. Assume:

- **Terminal value** if successful: $2,000 million (NPV of future cash flows if project succeeds).
- **Phase 1**: Cost $100M, success probability 60%.
- **Phase 2** (if Phase 1 succeeds): Cost $400M, success probability 75%.

### Scenario A: All-or-Nothing (Lump Sum)

Commit $500M upfront. Probability of overall success: 0.6 × 0.75 = 0.45.

Expected value:
- (0.45 × $2,000M) + (0.55 × $0) - $500M = $900M - $500M = **$400M**

### Scenario B: Staged Investment (Phase 1, then decide)

Pay $100M for Phase 1 immediately.

- If Phase 1 succeeds (60% probability): 
  - You *then* decide whether to invest $400M in Phase 2.
  - If you proceed and succeed (75% chance): Terminal value is $2,000M.
  - Expected value of Phase 2 *conditional on Phase 1 success*: (0.75 × $2,000M) - $400M = $900M.
  - So if Phase 1 succeeds and you rationally proceed with Phase 2, the payoff is $900M (before subtracting Phase 1 cost).

- If Phase 1 fails (40% probability):
  - You stop and invest nothing further.
  - Payoff: -$100M.

Expected value of the staged approach:
- (0.60 × $900M) + (0.40 × -$100M) - $100M = $540M - $40M - $100M = **$400M**.

Wait—both approaches yield $400M? That's because in this simplified example, the decision to stage is *automatic*: Phase 2 is always pursued if Phase 1 succeeds (since $900M is positive). There is no real option to abandon; only the option to find out about Phase 1 before spending Phase 2 money.

Now let's add realistic uncertainty: suppose after Phase 1 completes, you learn more about market size and cost overruns, and there is a 30% chance Phase 2's terminal value drops to $1,000M (from $2,000M) if market risk materializes.

### Scenario B-revised: Uncertainty revealed by Phase 1

If Phase 1 succeeds, you learn whether the terminal value is $2,000M (70% chance) or $1,000M (30% chance).

**If terminal value is $2,000M:**
- Proceed with Phase 2. Expected value: $900M (as before).

**If terminal value is $1,000M:**
- Expected value of Phase 2: (0.75 × $1,000M) - $400M = $350M.
- Still positive, so you proceed.

Expected value of staged approach:
- Phase 1 cost: $100M.
- If Phase 1 succeeds (60%):
  - 70% chance terminal value is $2,000M → proceed Phase 2 → payoff $900M.
  - 30% chance terminal value is $1,000M → proceed Phase 2 → payoff $350M.
  - Expected payoff conditional on Phase 1 success: (0.70 × $900M) + (0.30 × $350M) = $735M.
- If Phase 1 fails (40%): payoff is -$100M.

Overall expected value:
- (0.60 × $735M) + (0.40 × -$100M) - $100M = $441M - $40M - $100M = **$301M**.

### All-or-Nothing under Uncertainty:

Commit $500M upfront. You do not learn from Phase 1; you must assume the 70%/30% split applies *ex-ante* across all outcomes.

- 60% × 70% = 42% chance: Phase 1 succeeds, terminal value $2,000M. Phase 2 succeeds (75%). Payoff: $2,000M × 0.75 - $500M = $1,000M.
- 60% × 30% = 18% chance: Phase 1 succeeds, terminal value $1,000M. Phase 2 succeeds (75%). Payoff: $1,000M × 0.75 - $500M = $250M.
- 40% chance: Phase 1 fails. Payoff: -$500M.

Expected value:
- (0.42 × $1,000M) + (0.18 × $250M) + (0.40 × -$500M) = $420M + $45M - $200M = **$265M**.

**The staging premium**: $301M - $265M = **$36M**. By phasing, you add $36M in value through the ability to observe and respond before committing the bulk of capital.

## The Abandonment Option at Each Gate

The real power of staging emerges when abandonment is rational. Revise the example: suppose after Phase 1, there is a 20% chance the terminal value is only $200M (catastrophically bad news).

**If terminal value is only $200M:**
- Expected value of Phase 2: (0.75 × $200M) - $400M = $150M - $400M = -$250M.
- Rational choice: **Abandon**. Do not invest $400M.
- Payoff: -$100M (Phase 1 sunk cost).

This is the critical difference. In the all-or-nothing approach, you *cannot* abandon mid-project; capital is already committed. In the staged approach, if Phase 1 reveals bad news, you stop.

With 20% chance of this catastrophic outcome:

Expected value of staged approach:
- Phase 1 cost: $100M.
- If Phase 1 succeeds and market is strong (60% × 70% = 42%): Payoff $900M.
- If Phase 1 succeeds and market is medium (60% × 10% = 6%): Payoff $350M.
- If Phase 1 succeeds and market is catastrophic (60% × 20% = 12%): Payoff -$100M (abandon Phase 2).
- If Phase 1 fails (40%): Payoff -$100M.

Overall expected value:
- (0.42 × $900M) + (0.06 × $350M) + (0.12 × -$100M) + (0.40 × -$100M) - $100M
- = $378M + $21M - $12M - $40M - $100M = **$247M**.

All-or-nothing would still commit $500M and suffer -$200M on the catastrophic scenario, reducing its expected value further.

The staging premium is now much larger: ~**$100M** added through the ability to exit when bad information emerges.

## Factors That Increase the Staging Option's Value

The option to stage is more valuable when:

1. **High uncertainty about success**: Unproven technology, new market, novel business model. More chance that Phase 1 reveals game-changing information.
2. **Large later-phase costs**: A massive Phase 2 means the option to abandon is protecting a lot of capital.
3. **High volatility in success rates**: If success is either very likely or very unlikely (not 50-50), later phases should be more contingent on Phase 1 validation.
4. **Information-rich early phases**: Phase 1 learning is material (not just "move forward regardless").
5. **Ability to defer**: If you can wait without losing the option (no competitive preemption), the value of waiting and learning increases.

## Implementation and Pitfalls

In practice, staging adds complexity:

- **Costs more**: Phasing often means running pilot plants, building prototypes, or conducting preliminary studies that would be skipped in a monolithic project. Phase 1 "inefficiency" is the price of the option.
- **Delays value capture**: Terminal payoff comes later, extending the discount period and reducing NPV.
- **Invites scope creep**: Each phase can expand; estimated costs can balloon.
- **Requires discipline**: If managers are emotionally committed to success after Phase 1, they may proceed with Phase 2 even if the option to abandon would be rational.

Despite these costs, real-options logic strongly favors staging for projects with high technical or market uncertainty. The pharmaceutical, biotech, mining, and real estate development industries all use phased approaches because the option value is so large.

## See also

<div class="wiki-seealso">

### Closely related

- [Real Options in Pharmaceutical R&D Valuation](/real-options-in-pharmaceutical-rd/) — Stages of drug development as sequential options
- [Real Options in Mining Project Valuation](/real-options-mining-project-valuation/) — Phased mine development (pilot → full scale)
- [How to Estimate Volatility for a Real Options Model](/volatility-estimate-real-options/) — Volatility drives option value at each gate
- [Call Option](/call-option/) — The right to proceed (exercise) at each gate
- Option to Abandon — Cease investment; stop losses

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Static method that often misses phasing benefits
- [Sensitivity Analysis in Valuation](/sensitivity-analysis-valuation/) — Stress-test project value across uncertainty ranges
- Decision Trees — Framework for visualizing staged investment decisions
- [Scenario Analysis](/scenario-analysis/) — Alternative to real-options for handling uncertainty

</div>
