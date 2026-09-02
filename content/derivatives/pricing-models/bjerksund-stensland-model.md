---
title: "Bjerksund-Stensland Model"
description: "An analytic approximation formula for American option pricing that avoids the computational cost of binomial trees and full partial differential equations."
keywords:
  - American option
  - early exercise
  - approximation formula
  - option pricing
  - computational efficiency
image: /svg/derivatives.svg
---

*The **Bjerksund-Stensland model** is an analytical closed-form approximation for pricing American [call](/call-option/) and [put options](/put-option/) on dividend-paying equities. Instead of solving a full partial differential equation or building a binomial lattice, it uses a clever boundary approximation that treats early exercise as occurring whenever the stock price hits a certain optimal level. The result is fast, accurate to within 1–2 basis points, and widely adopted by practitioners who need [option](/option/) prices in real time.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bjerksund-Stensland Model — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives pricing." />

<div class="wiki-infobox-caption">Closed-form speed with near-analytic precision for American equity options.</div>

|   |   |
|---|---|
| **What it is** | A two-step approximation formula for American [option](/option/) value when dividends are present |
| **Also called** | B-S approximation, Bjerksund-Stensland formula |
| **Invented** | 1993 by Petter Bjerksund and Gunnar Stensland (academics, later practitioners) |
| **Key advantage** | Closed-form speed without binomial or tree lattice computation |
| **Key assumption** | Stock follows lognormal diffusion; [volatility](/historical-volatility/) and dividend yield are constant |
| **Typical error** | 1–2 basis points vs. numerical solutions; less accurate deep in the money |
| **Contrast** | [Black-Scholes-Merton](/black-scholes-model/) applies only to European options; Bjerksund-Stensland handles American early exercise |

</aside>

## The American [option](/option/) problem: why closed-form is hard

A European [option](/option/) can only be exercised at maturity, so the [Black-Scholes-Merton](/black-scholes-model/) formula applies: an integral under the risk-neutral measure, solvable in closed form. An American [option](/option/) can be exercised at any time before expiry, opening the door to early exercise. This *optimal stopping problem* has no known closed-form solution—the value at any point depends on whether immediate exercise is better than waiting, a recursive decision that typically demands numerical methods.

The standard approach is a binomial tree: at each node, you decide whether to exercise now or hold and optimize forward. For fine grids (thousands of steps), this becomes slow—problematic for a trader who needs prices for hundreds of [option](/option/) strikes in milliseconds. The Bjerksund-Stensland approximation offers a compromise: a formula that captures the essential logic of early exercise without building the tree.

## The key insight: approximating the exercise boundary

The crux is the **optimal early-exercise boundary**: a stock price *S*(t) as a function of time and parameters, such that you should exercise the American [option](/option/) if and only if *S* hits this boundary. Bjerksund and Stensland observe that for perpetual American [options](/option/) (infinitely long maturity), the boundary is constant: above that price, always exercise; below it, always hold. For finite maturity, the boundary is not constant but can be approximated.

Their trick: use the perpetual-[option](/option/) boundary as a first guess, then apply a correction for time-to-maturity and [dividend](/dividend/) yield. This yields a closed-form approximation for the boundary, which in turn gives a closed-form value.

## The formula in sketch (calls on dividend-paying stock)

For an American call on a stock paying continuous [dividend](/dividend/) yield *q*, with [strike-price](/strike-price/) *K*, stock price *S*, volatility *σ*, [interest-rate](/interest-rate/) *r*, and time to maturity *T*:

1. Compute a "trigger" price *S* (boundary) using the perpetual-[option](/option/) formula scaled by a time-dependent factor.
2. If the current stock price exceeds the trigger and early exercise is optimal, use the immediate [exercise-price](/exercise-price/) plus time value.
3. Otherwise, use a [Black-Scholes-Merton](/black-scholes-model/)-like integral adjusted for the boundary.

The full formula is a two-piece structure: one approximation for the value itself, and one for whether early exercise is in the money. The result is a function you can evaluate in microseconds—a handful of exponentials and square roots.

## Accuracy and when it fails

The Bjerksund-Stensland approximation is typically accurate to 1–2 basis points for [option](/option/) prices in the range of 0.5 to 1.5 times the [strike-price](/strike-price/), and less accurate (errors of 5–10 basis points) when deep in or out of the money. The error stems from the approximation of the true boundary: the real boundary is more nuanced than the simplified formula captures, especially near maturity (when the boundary is close to the [strike-price](/strike-price/)).

For portfolios with millions of [option](/option/) positions and tight [margin](/margin-call-forex/) constraints, traders sometimes prefer the [Barone-Adesi Whaley model](/barone-adesi-whaley-model/), which uses a quadratic approximation and can be even faster. For academic research or pricing where accuracy is paramount, a full binomial or finite-difference lattice is more reliable.

## Dividend yield and adjustments

The original Bjerksund-Stensland formula assumes a constant continuous [dividend](/dividend/) yield *q*. If dividends are discrete (e.g., a known dollar amount paid on a specific date), the formula becomes less accurate, though practitioners use adjustments or approximate the discrete stream as a continuous yield.

For stock [options](/option/) in markets with ex-dividend dates (essentially all real-world equity [option](/option/) markets), traders price American [option](/option/)s using Bjerksund-Stensland as a baseline and then adjust for discrete dividends via a shift in the stock price or a manual check on the optimal [exercise-price](/exercise-price/) around dividend dates.

## Comparison with other methods

- **Binomial trees**: Exact in the limit, but slow (thousands of nodes). Bjerksund-Stensland is much faster.
- **Finite-difference PDE solvers**: Also exact (given fine grids), but require specialized software and calibration. Bjerksund-Stensland is closed-form.
- **[Barone-Adesi Whaley model](/barone-adesi-whaley-model/)**: A competing approximation using quadratic terms instead of boundary approximation. Often slightly more accurate for deep in-the-money [option](/option/)s.
- **Monte Carlo**: Flexible for complex payoffs but slow for American [option](/option/)s (requires *Longstaff-Schwartz* regression or similar).

## See also

<div class="wiki-seealso">

### Closely related

- [Barone-Adesi Whaley Model](/barone-adesi-whaley-model/) — competing American [option](/option/) approximation with quadratic structure
- [Option](/option/) — derivative priced using Bjerksund-Stensland
- [Call Option](/call-option/) — typical application
- [Put Option](/put-option/) — American puts are frequently valued with this method
- [Black-Scholes Model](/black-scholes-model/) — foundational framework; Bjerksund-Stensland is an extension for early exercise
- [Exercise Price](/exercise-price/) — parameter determining when early exercise occurs
- [Volatility](/historical-volatility/) — critical input; misestimation directly affects the [option](/option/) value

### Wider context

- [Dividend](/dividend/) — affects early-exercise incentives
- [Interest-Rate](/interest-rate/) — discount factor in [option](/option/) value
- [Option Premium](/option-premium/) — what the [option](/option/) is worth in the market
- [Risk-Neutral Pricing](/risk-neutral-pricing/) — underlying principle

</div>
