---
title: "Semi-Variance"
description: "A downside-focused risk measure that squares only the returns below a target threshold, ignoring positive deviations and treating upside differently from downside."
keywords:
  - downside volatility
  - downside risk
  - target return
  - below-mean returns
  - risk asymmetry
image: "/svg/risk.svg"
---

*A **semi-variance** measures the squared deviations of returns only when they fall below a chosen threshold—typically the mean return or a target return—ignoring upside swings entirely. By isolating downside volatility, it treats losses and gains asymmetrically, reflecting the investor intuition that not all volatility is equally bad.*

## The case against ordinary variance

Standard variance treats every return deviation from the mean as equally risky, whether it swings above or below. A portfolio that jumps 20% above its mean return contributes as much to variance as a 20% plunge below it. This symmetry is convenient for mathematics but unrealistic: an investor who experiences an unexpected gain does not feel the same anxiety as one facing an equal loss. Prospect theory in behavioural economics codified this: losses hurt more than gains feel good.

Semi-variance corrects this. It says: calculate the squared deviations, but only for returns below your threshold. Everything above the threshold counts as zero. This produces a risk measure that literally cannot see the upside, capturing the intuition that a strategist cares about the bottom tail, not the top.

Mathematically, semi-variance to a target T is the mean of max(0, T − R)², where R is the return. If you use mean return as the target, you get downside semi-variance to the mean. If you use a personal or mandate-specified target return, you get downside semi-variance to that target. The latter is often more meaningful: a pension fund with a 7% liability yield cares about falling short of 7%, not about the statistical mean.

## Downside risk and investor behaviour

Why does semi-variance matter? Because real investors do not care symmetrically about volatility. A portfolio that oscillates ±10% feels safer than one that reliably gains 12% then crashes 20%. The second exhibits the same variance, but the semi-variance is much larger. Semi-variance ranks it as riskier, aligning with intuition.

This is not merely psychological. It has practical consequences. An investor with capital commitments (a pension fund with fixed liabilities, a retiree with spending needs) cares about the probability of shortfall far more than about upside surprise. Semi-variance captures this: it penalizes the likelihood and magnitude of falling short of requirements.

Semi-variance also decouples risk from mean return in a useful way. Two portfolios with the same mean but different distributions—one smooth, one choppy—might have equal variance but very different semi-variances. The smooth one, with fewer downside swings, shows lower semi-variance. Practitioners prefer it. Semi-variance explains why; variance does not.

## Relationship to downside risk and lower partial moments

Semi-variance is a special case of a broader concept called [lower partial moment](/lower-partial-moment/) (LPM). An LPM raises downside deviations to an arbitrary power n: LPM(n, T) is the mean of max(0, T − R)^n. Semi-variance is LPM with n = 2. When n = 1, you get mean below-target shortfall. When n = 0, you get the frequency of misses.

This hierarchy is useful: n = 0 ignores magnitude (does not matter how bad the fall); n = 1 is a linear penalty (losses are bad, but not disproportionately); n = 2 (semi-variance) heavily penalizes large downside swings; n > 2 penalizes extreme tail losses even more sharply.

Different portfolio problems call for different n. A hedge fund manager worried about blow-ups might choose n = 3 or higher; a conservative endowment might accept n = 2. Semi-variance, at n = 2, sits in the middle, balancing responsiveness to tail size with computational simplicity.

## Asymmetry and the limits of mean-variance optimization

The mean-variance framework, which dominates portfolio theory and practice, assumes that [variance](/market-risk/) fully describes risk. Under mean-variance logic, two assets with the same mean and variance are equally risky, even if one delivers positive surprises and the other delivers negative ones. This breaks down when preferences are asymmetric.

When you replace [variance](/market-risk/) with semi-variance in optimization, you can get radically different portfolios. An asset that occasionally spikes upward (high positive skew) might be valued more highly under semi-variance than under variance, because its downside is tame. An asset with silent, steady declines punctuated by rare crashes (negative skew) might be rated much worse.

For real portfolios, this matters. A technology stock with a history of quick recoveries and occasional spectacular rallies shows different semi-variance than traditional variance suggests. A mortgage-backed security with steady income and rare but severe credit losses looks much worse through the semi-variance lens. Semi-variance forces the optimizer to weight tail risk explicitly.

However, semi-variance also introduces a choice: what is the target threshold? There is no universally correct answer. Using the mean captures volatility around the long-run outcome; using a specific return (a liability, a mandate minimum) captures shortfall risk. Different choices will optimize to different allocations. This flexibility is powerful but demands discipline.

## Calculation and data requirements

Semi-variance is straightforward to calculate. For a time series of returns, identify the threshold, subtract it from each return, set all positive differences to zero, square the negatives, and take the mean. Annualized semi-variance is the time-aggregated version: if you have monthly returns, calculate monthly semi-variance and multiply by 12 to annualize (approximately; exact treatment depends on whether returns are log or simple).

One practical advantage: semi-variance demands less data history than [value at risk](/value-at-risk/) or [expected shortfall](/expected-shortfall/). Because it does not focus on a narrow tail quantile, it is less sensitive to the handful of worst outcomes. A 10-year history of monthly returns (120 points) is often sufficient. VaR at 95% or tighter confidence, by contrast, might require 20 years or more to avoid noise in the 5% tail.

On the flip side, semi-variance does not directly tell you: what is the worst I could lose? Unlike [value at risk](/value-at-risk/), which answers "there is a 5% chance of losing more than X", semi-variance only answers "my downside volatility is Y". The two are related but not interchangeable. A comprehensive risk framework often uses both.

## Strengths and limitations

Semi-variance excels at capturing intuitive downside sensitivity in a way [variance](/market-risk/) misses. For investors with asymmetric loss aversion, it is philosophically cleaner. It also fares better in optimization: portfolios built on semi-variance tend to show lower realized shortfalls in backtests than mean-variance portfolios, precisely because the model was built to avoid downside.

Yet semi-variance has trade-offs. First, it is not a [coherent risk measure](/coherent-risk-measure/): it violates positive homogeneity. Double the portfolio size, and semi-variance does not simply double if the threshold is absolute (like a dollar amount) rather than relative (like a percentage return). This can cause unexpected behaviour in scaling problems.

Second, semi-variance can be unstable if the target threshold is close to the mean. With most returns near the target, small swings in the data drive large changes in semi-variance. Practitioners often smooth over rolling windows or Bayesian priors to avoid noise.

Third, it requires choosing a target. For some mandates (a liability-driven portfolio), the choice is clear. For others (an absolute-return hedge fund), it is arbitrary. The measure's strength—its ability to encode a specific investor preference—also makes it less universal than [variance](/market-risk/).

## See also

<div class="wiki-seealso">

### Closely related

- [Lower Partial Moment](/lower-partial-moment/) — Generalized downside metric; semi-variance is LPM(2, target)
- [Coherent Risk Measure](/coherent-risk-measure/) — Axiomatic framework; semi-variance does not satisfy homogeneity
- [Distortion Risk Measure](/distortion-risk-measure/) — Alternative downside-focused approach via probability transformation
- [Value at Risk](/value-at-risk/) — Threshold-based percentile; complements semi-variance
- [Expected Shortfall](/expected-shortfall/) — Coherent tail-average; different downside philosophy

### Wider context

- [Market Risk](/market-risk/) — Portfolio risk from price and volatility
- [Loss Aversion](/loss-aversion/) — Behavioural foundation for asymmetric risk preferences
- [Asset Allocation](/asset-allocation/) — Portfolio construction framework that can use semi-variance
- [Volatility](/historical-volatility/) — Related dispersion metric; treats upside and downside equally
- [Standard Deviation](/market-risk/) — Square root of variance; same symmetry issue as variance

</div>
