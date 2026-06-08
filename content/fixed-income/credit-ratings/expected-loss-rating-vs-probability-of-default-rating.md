---
title: "Expected Loss Rating vs Probability of Default Rating"
description: "How Moody's expected loss rating differs from probability-of-default ratings by S&P and Fitch, and why it matters for structured products."
keywords:
  - expected loss rating
  - probability of default rating
  - moody's ratings
  - credit ratings methodology
  - structured product ratings
  - loss severity
---

*The main rating agencies use fundamentally different frameworks to assess credit risk. **Expected loss ratings** incorporate both the chance of default and the size of the loss if default happens, while **probability-of-default ratings** focus only on the likelihood of default itself—a distinction that produces meaningfully different conclusions, especially for products where recovery varies widely.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rating Approaches — Key Differences</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income and credit." />

<div class="wiki-infobox-caption">Three major agencies employ two distinct philosophies for rating debt instruments.</div>

|   |   |
|---|---|
| **Moody's approach** | Expected loss (default probability × loss severity) |
| **S&P and Fitch** | Probability of default only |
| **Key implication** | Same default odds can earn different ratings depending on recovery assumptions |
| **Structured products** | Expected loss ratings often appear more lenient on subordinated tranches |
| **Recovery rate assumption** | Critical in Moody's model; ranges 20–100% depending on collateral and seniority |
| **Practical impact** | Investors may find equivalent risk levels rated differently across agencies |

</aside>

## The Two Philosophies

Rating agencies began with a single mission: predict whether a borrower will fail to pay. That mission still guides S&P and Fitch, which assign ratings based on the [probability](/credit-rating/) of default in a given time horizon. An A-rated bond means roughly a 0.1% chance of default within a year, a BBB bond roughly 0.2%, and so on. The rating tells you the odds, not the consequences.

Moody's broke ranks in the late 1980s and reformulated ratings to capture expected loss—the dollar or percentage impact you'd see if the loan goes bad. Expected loss multiplies two numbers: (1) the [probability of default](/credit-rating/) and (2) the loss given default (one minus the recovery rate). A borrower with a 5% chance of default but 90% recovery is far less damaging than one with a 1% chance of default but only 10% recovery. Moody's ratings fold both into a single number; S&P and Fitch do not.

This philosophical divide rarely matters for plain-vanilla corporate or government bonds, where recovery assumptions are stable and well-understood. But in [structured products](/structured-product/)—mortgage-backed securities, collateralized debt obligations, and other tranched instruments—the difference becomes acute. Senior tranches recover first and almost always get paid in full; junior tranches absorb losses and may recover nothing. Moody's expected-loss framework naturally accommodates this tiering; the probability-of-default approach does not.

## How Moody's Builds an Expected Loss Rating

Moody's assigns a rating to each [tranche](/structured-product/) of a structured deal based on the expected loss to that specific piece of the capital stack.

First, it models the pool of underlying loans or bonds and estimates a loss distribution—how much principal could be lost in a range of default scenarios. This distribution depends on the characteristics of the collateral: mortgage default rates in a housing downturn, corporate default rates in a recession, and the correlation between individual defaults.

Next, it models how losses flow through the deal's waterfall. The most senior tranche absorbs nothing unless losses exceed, say, 20% of the pool. A mezzanine tranche might absorb losses between 15% and 35%. Moody's calculates the probability that losses in each scenario will reach and exceed each tranche's attachment point.

Finally, it multiplies that probability by the loss severity for that tranche. If a mezzanine tranche faces a 4% probability of any loss, and if loss does occur, investors recover an average of 30 cents on the dollar, the expected loss is 4% × 70% = 2.8%, which Moody's might map to an A or A2 rating depending on the scale.

## Why S&P and Fitch Stay with Probability of Default

S&P and Fitch argue that expected loss collapses two independent questions—can it fail, and how much will it hurt?—into one opaque metric. They contend that investors are better served by a clean probability number and a separate recovery assumption they can adjust themselves if they disagree with the agency's loss forecast.

From a rating-stability perspective, the probability-of-default approach also makes sense. Recovery assumptions are forward-looking guesses; default probabilities, though uncertain, rest on historical data. If recovery assumptions shift in a credit cycle (e.g., real-estate values fall and collateral recoveries drop), an expected-loss rating would swing sharply even if the probability of default stays flat. A probability-of-default rating would not. This can be seen as either a feature (ratings capture real changes) or a bug (ratings bounce around too much).

For [high-yield bonds](/high-yield-bond/) and corporate instruments, the difference is typically small: recovery rates are often in a narrow range, and the agency methodologies converge. But S&P and Fitch still publish expected recovery assumptions alongside their ratings, so sophisticated investors can compute an expected loss themselves.

## Impact on Structured Products

In mortgage-backed securities and collateralized debt obligations, the gap widens considerably.

Consider a hypothetical MBS with 1,000 mortgages. Moody's might estimate a 5% probability that defaults reach a point where the BBB tranche (the third loss-bearing layer) takes a hit, and assumes a 40% recovery rate. Expected loss is 5% × 60% = 3%, which might merit an A-rated designation. S&P, using the same default model but only rating on probability, might see the same 5% risk to the tranche and rate it BBB, because it doesn't fold the 40% recovery into the rating number itself.

The ratings look contradictory, but they're answering slightly different questions. Moody's says "expected loss is low"; S&P says "default probability is moderate, recovery is uncertain." An investor holding both agencies' reports can synthesize the truth. An investor relying on one can be misled.

In post-2008 analysis, Moody's expected-loss approach faced criticism for assigning ratings that didn't fully account for the extreme tail risk—the possibility of 80% losses when most of the collateral defaulted. Expected loss assumes recoveries at historical or modeled averages; it does not capture the worst-case path. [Stress testing](/stress-testing/) and [value at risk](/value-at-risk/) models now complement ratings at most institutions to capture this gap.

## Practical Consequences for Bond Investors

If you're comparing two structured tranches, one rated by Moody's and one by S&P, the ratings may not be directly comparable. You should ask:

1. **What recovery is each agency assuming?** This is disclosed in the rating report.
2. **What's my own estimate of recovery?** If you believe recovery will be 20%, not 40%, the expected-loss rating may overstate safety.
3. **Do I agree with the default probability?** Both agencies estimate this, though using different models. If you are more bearish, adjust downward.
4. **Am I buying for safety or yield?** Conservative investors should focus on probability of default and be conservative on recovery. Yield-hunting investors need to understand the full loss spectrum.

The key insight: a rating is not a truth statement; it's a model output. Different models can be valid without being identical. Expected loss and probability of default both have merit; they are complementary views of risk, not competitors.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit Rating](/credit-rating/) — the core concept and how agencies assign letter grades
- [Credit Risk](/credit-risk/) — the broader category encompassing default probability and recovery
- [Structured Product](/structured-product/) — how tranches are created and how they differ in risk
- [Tranche](/structured-product/) — the layered pieces of a CDO or MBS
- [Mortgage-Backed Security](/mortgage-backed-security/) — a major category of structured debt
- [Loss Given Default](/credit-risk/) — the complement to probability of default in expected loss calculations
- [Stress Testing](/stress-testing/) — methods to evaluate ratings under extreme scenarios

### Wider context

- [Bond Rating Agencies](/credit-rating/) — background on S&P, Moody's, and Fitch
- [Collateralized Debt Obligation](/structured-product/) — the structured product that brought expected loss into focus
- [Credit Rating](/credit-rating/) — foundational essay on how ratings are assigned
- [Value at Risk](/value-at-risk/) — an alternative risk metric capturing tail risk

</div>
