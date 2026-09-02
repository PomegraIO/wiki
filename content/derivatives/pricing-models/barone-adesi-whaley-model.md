---
title: "Barone-Adesi Whaley Model"
description: "A quadratic approximation for American option pricing that decomposes value into European and early-exercise components, widely used by practitioners."
keywords:
  - American option
  - early-exercise premium
  - quadratic approximation
  - option pricing
  - practitioner standard
image: /svg/derivatives.svg
---

*The **Barone-Adesi Whaley** (BAW) **model** is a fast closed-form approximation for American [option](/option/) prices that decomposes the value into a European [option](/option/) component plus an early-exercise premium. Using a quadratic approximation, it solves for the optimal exercise boundary analytically and is computationally efficient enough for real-time market-making and portfolio risk. It is the industry standard in derivatives trading desks and is often more accurate than [Bjerksund-Stensland](/bjerksund-stensland-model/) for deep in-the-money [option](/option/)s.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Barone-Adesi Whaley Model — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives pricing." />

<div class="wiki-infobox-caption">The practitioner's choice: accurate, fast, and handles both calls and puts cleanly.</div>

|   |   |
|---|---|
| **What it is** | A closed-form approximation combining [Black-Scholes-Merton](/black-scholes-model/) with an analytic early-exercise premium |
| **Also called** | BAW model, Barone-Adesi-Whaley formula |
| **Invented** | 1987 by Giancarlo Barone-Adesi and Robert Whaley |
| **Key advantage** | Higher accuracy than [Bjerksund-Stensland](/bjerksund-stensland-model/) for in-the-money [option](/option/)s; handles both calls and puts symmetrically |
| **Key assumption** | Stock follows lognormal diffusion; constant [volatility](/historical-volatility/) and [dividend](/dividend/) yield |
| **Typical error** | < 1 basis point for most strikes; slightly higher out-of-the-money |
| **Contrast** | [Bjerksund-Stensland](/bjerksund-stensland-model/) uses boundary approximation; BAW uses quadratic adjustment |

</aside>

## The decomposition: European plus early exercise

All American [option](/option/) pricing rests on a decomposition:

**American [Option](/option/) Value = European [Option](/option/) Value + Early-Exercise Premium**

The European part is easy: apply [Black-Scholes-Merton](/black-scholes-model/). The hard part is the early-exercise premium—how much extra is the American [option](/option/) worth simply because you *can* exercise before maturity? Barone-Adesi and Whaley solve this by approximating the early-exercise premium using a quadratic term, rather than solving the full optimal-stopping problem.

The insight is that the optimal [exercise-price](/exercise-price/) boundary near maturity behaves smoothly; a quadratic function (a parabola) captures its shape well. This allows them to express the early-exercise premium in closed form, avoiding both binomial trees and numerical PDE solvers.

## The mechanics: solving for the boundary

The American [option](/option/) satisfies a free-boundary problem: the value function and its derivative must be continuous at the optimal exercise boundary, and at the boundary, exercising immediately yields the [intrinsic-value](/intrinsic-value/). Barone-Adesi and Whaley linearize around the [Black-Scholes-Merton](/black-scholes-model/) solution by assuming the boundary is a quadratic function of the remaining time to maturity.

Under this assumption, the early-exercise premium M(S, T) (the extra value over European) satisfies a partial differential equation that they solve analytically. The result is a compact formula:

**American Call ≈ European Call + M**

where M depends on a quadratic approximation involving the [strike-price](/strike-price/), stock price, [volatility](/historical-volatility/), [dividend](/dividend/) yield, [interest-rate](/interest-rate/), and time to maturity. You compute M once (a few exponentials and polynomials), add it to the [Black-Scholes-Merton](/black-scholes-model/) call, and you have the American call price.

## Accuracy: when and why it shines

The BAW model typically delivers errors under 1 basis point for at-the-money and slightly in-the-money [option](/option/)s. It remains accurate even for [option](/option/)s deep in the money, where the approximation of the exercise boundary becomes especially important—this is a weakness of [Bjerksund-Stensland](/bjerksund-stensland-model/), which uses a constant perpetual boundary adjusted by time decay.

For out-of-the-money [option](/option/)s, where early exercise is rarely optimal anyway, both BAW and Bjerksund-Stensland converge to the European value, and error is negligible.

The formula is symmetric in calls and puts (with appropriate adjustment of the boundary), whereas [Bjerksund-Stensland](/bjerksund-stensland-model/) requires separate formulation. Traders appreciate this elegance and consistency.

## Dividend handling and practical implementation

Like Bjerksund-Stensland, BAW assumes a continuous [dividend](/dividend/) yield. For discrete dividends, practitioners either:

1. Approximate the stream as continuous.
2. Use BAW as a baseline and apply manual adjustments around ex-dividend dates.
3. Fall back to a binomial tree for accuracy on dividend-heavy [option](/option/)s.

Many proprietary trading systems (especially interest-rate derivatives desks) use BAW as the default [option](/option/) pricer for quick quotes, then refine with full methods when needed for large positions or hedging.

## Speed and computational cost

BAW is a closed-form formula: a few square roots, exponentials, and a root-finding step (often Newton-Raphson for the boundary coefficient). Evaluation takes microseconds per [option](/option/), making it ideal for pricing thousands of [option](/option/)s across a portfolio or at every [market-tick](/). By contrast, a 100-step binomial tree is 100+ times slower; a finite-difference PDE solver is slower still.

This speed advantage has solidified BAW as the industry standard for real-time risk management and trading systems. Quants run BAW during the day and reserve more expensive methods (full recalibration of the [volatility](/historical-volatility/) surface, binomial backtest) for end-of-day and stress-testing.

## Comparison with [Bjerksund-Stensland](/bjerksund-stensland-model/)

| | BAW | Bjerksund-Stensland |
|---|---|---|
| **Accuracy (ATM)** | < 1 bp | 1–2 bp |
| **Accuracy (ITM)** | < 1 bp | 5–10 bp |
| **Speed** | Fastest | Very fast |
| **Calls vs. Puts** | Symmetric | Separate formulas |
| **Dividend complexity** | Continuous yield | Continuous yield |

BAW is generally preferred for production trading; [Bjerksund-Stensland](/bjerksund-stensland-model/) is useful as a sanity check or when a slightly faster approximation suffices.

## Limitations and when to use binomial

BAW breaks down at the extremes: when an [option](/option/) is so far out of the money that its value is dominated by tail risk, or when dividend dates fall within days of the [exercise-price](/exercise-price/). Also, like all continuous-model approaches, it assumes no jumps or overnight gaps—assumptions violated in real markets during earnings announcements or central-bank shocks.

For mission-critical pricing (e.g., pricing a single large [option](/option/) for a bespoke [swap](/)), traders often run both BAW and a binomial tree to cross-check. The binomial is the "ground truth"; BAW is the fast workhorse.

## See also

<div class="wiki-seealso">

### Closely related

- [Bjerksund-Stensland Model](/bjerksund-stensland-model/) — competing American [option](/option/) approximation; generally less accurate ITM
- [Black-Scholes Model](/black-scholes-model/) — the European [option](/option/) baseline that BAW augments
- [Option](/option/) — the derivative BAW prices
- [Call Option](/call-option/) — typical application
- [Put Option](/put-option/) — American puts priced with BAW symmetrically
- [Intrinsic Value](/intrinsic-value/) — the immediate [exercise-price](/exercise-price/) value
- [Volatility](/historical-volatility/) — critical input; surface changes drive [hedging](/hedge-fund/) decisions

### Wider context

- [Dividend](/dividend/) — affects early-exercise incentives
- [Interest-Rate](/interest-rate/) — discount rate in the formula
- [Exercise Price](/exercise-price/) — strike at which early exercise occurs
- [Risk-Neutral Pricing](/risk-neutral-pricing/) — the underlying valuation principle
- [Market Maker Trading](/market-maker-trading/) — practitioners who use BAW in real time

</div>
