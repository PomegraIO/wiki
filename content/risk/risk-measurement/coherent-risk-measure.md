---
title: "Coherent Risk Measure"
description: "A mathematically principled framework defining four axioms—monotonicity, subadditivity, positive homogeneity, and translation invariance—that a valid risk measure must satisfy."
keywords:
  - risk axioms
  - subadditivity
  - coherent risk framework
  - risk management principles
  - risk quantification
image: "/svg/risk.svg"
---

*A **coherent risk measure** is a function ρ that quantifies portfolio risk and satisfies four mathematical axioms: monotonicity (riskier portfolios score higher), subadditivity (diversification reduces risk), positive homogeneity (doubling the portfolio doubles the risk), and translation invariance (adding cash shifts risk downward by that amount). These properties formalize the intuition that a sound risk measure should reward hedging and not penalize diversification.*

<div class="wiki-hatnote">

For measures that satisfy only some coherence axioms, see [Distortion Risk Measure](/distortion-risk-measure/); for the most-used non-coherent standard, see [Value at Risk](/value-at-risk/).

</div>

## The four axioms

Coherent risk measures emerged in the late 1990s as a response to practical failures of [value at risk](/value-at-risk/). Before diving into the axioms, it helps to remember what they are trying to prevent: a risk measure that says a diversified portfolio is riskier than its isolated parts, or one that rewards the addition of toxic assets.

**Monotonicity** states that if one portfolio X always produces lower returns (under any scenario) than portfolio Y, then ρ(X) ≥ ρ(Y). In plain terms, a guaranteed loss is riskier than a possible gain. This seems obvious, yet it catches non-intuitive measures that might reverse orderings based on secondary properties like kurtosis.

**Subadditivity** says ρ(X + Y) ≤ ρ(X) + ρ(Y): the risk of a combined portfolio never exceeds the sum of individual risks. This is the cornerstone axiom. It encodes the diversification principle—when you merge two portfolios, their combined risk should not exceed the aggregate. Subadditivity fails for [value at risk](/value-at-risk/), the market standard, in many realistic scenarios: two portfolios each at the 95% confidence tail can, when merged, push both into the tail of the combined distribution, violating the inequality.

**Positive homogeneity** requires ρ(λX) = λρ(X) for any positive scalar λ. Scale the portfolio by 2, and the risk scales by 2. This rules out threshold effects where a small position is very risky but a large one, paradoxically, is less so per unit. Homogeneity also ensures that risk scales linearly—a property essential for linear optimization.

**Translation invariance** states ρ(X + r) = ρ(X) − r, where r is a safe, deterministic return. Adding cash (or cash equivalents) to a portfolio reduces measured risk by exactly that amount, with no surplus or deficit. This says that the risk measure is genuine: it is not influenced by accounting tricks or the asset mix, only by the true distribution of outcomes.

## Why these axioms matter

The coherence framework emerged because portfolio managers were making hedging decisions based on [value at risk](/value-at-risk/), not realizing that VaR could recommend against diversification. Imagine two portfolios, each exposing you to tail losses at exactly the 95% VaR threshold. When you combine them, the combined portfolio's loss distribution now has both tails active—meaning both old positions are now in the interior of the merged distribution, where VaR is blind. In mathematical terms, VaR violates subadditivity.

Coherence rules this out. A coherent measure must rank the combined portfolio as less risky than the sum of the parts, aligning with the practitioner's intuition. This alignment between math and intuition was the reform that Artzner, Delbaen, Eber, and Heath (the originators) championed.

## Standard coherent measures

**Expected Shortfall** (also called Conditional Value at Risk, or CVaR) is the best-known coherent alternative to [value at risk](/value-at-risk/). It averages the losses beyond the VaR threshold. If VaR95 is −10%, then CVaR95 is the mean loss on the worst 5% of outcomes. By averaging rather than picking a single threshold, it "sees" into the tail, capturing the magnitude of extreme events.

**Spectral risk measures** generalize expected shortfall by weighting losses at different quantiles. Instead of assigning equal weight to all tail outcomes (as CVaR does), a spectral measure assigns higher weight to worse outcomes. This is formalized by an increasing weighting function over the quantile range.

**Coherent distortion risk measures** apply [distortion functions](/distortion-risk-measure/) that are concave. When the distortion function curves upward (is concave), the resulting risk measure respects all four axioms. This gives practitioners another toolbox for embedding their intuitions about tail weighting into a mathematically sound framework.

## Limitations and trade-offs

Coherence is elegant but comes with costs. First, not all intuitively reasonable risk measures satisfy all four axioms. For instance, risk measures based on [variance](/market-risk/) or [semi-variance](/semi-variance/) violate homogeneity when losses are not symmetric around the mean. Some practitioners accept this trade-off in exchange for simplicity or interpretability.

Second, coherent measures are often harder to compute than [value at risk](/value-at-risk/). Expected shortfall requires sorting or integration over the tail; spectral measures require fitting a weighting function; distortion measures require choosing and calibrating a distortion function. For large portfolios updated in real time, the computational burden can be real.

Third, the axioms do not uniquely pin down a measure. There are infinitely many coherent risk measures, and they can produce very different rankings of the same portfolio. A bank using expected shortfall might approve a trade that a bank using a spectral measure would reject. The coherence framework guarantees logical consistency within a measure, not consensus across measures.

Finally, coherence assumes risks are portfolio-additive. In the presence of [liquidity risk](/liquidity-risk/), [operational risk](/operational-risk/), or counterparty correlation during crises, the real world is less modular than the math assumes. A coherent measure applied to illiquid assets can be a false comfort.

## Regulation and adoption

Regulators have moved toward coherence. The Basel III framework, which governs bank capital, moved from [value at risk](/value-at-risk/) to Expected Shortfall (a coherent measure) for the market-risk capital charge. This shift reflected a global recognition that subadditivity is not optional—it is a requirement for a risk measure to avoid perverse incentives.

Yet the market has been slower to abandon VaR. It remains the most-cited risk metric in public disclosures and internal dashboards. Part of this is inertia; part is institutional comfort with a measure that has decades of history; part is that VaR, while non-coherent, is intuitive and fast to compute. Moving the entire financial system to coherent measures remains a work in progress.

## See also

<div class="wiki-seealso">

### Closely related

- [Distortion Risk Measure](/distortion-risk-measure/) — Applies probability transformation; coherent if distortion is concave
- [Semi-Variance](/semi-variance/) — Downside-focused alternative; does not satisfy homogeneity
- [Lower Partial Moment](/lower-partial-moment/) — Generalizes semi-variance; foundation for coherent spectral measures
- [Value at Risk](/value-at-risk/) — Market standard; non-coherent; violates subadditivity
- [Expected Shortfall](/expected-shortfall/) — Coherent tail-average alternative; most-used coherent measure

### Wider context

- [Market Risk](/market-risk/) — Portfolio risk from price and rate moves
- [Diversification](/diversification/) — Core principle that coherence axioms protect
- [Liquidity Risk](/liquidity-risk/) — Risk not captured by coherence framework
- [Operational Risk](/operational-risk/) — Non-portfolio risk; requires different measures
- Risk Management — Broader discipline of measuring and hedging exposure

</div>
