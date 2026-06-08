---
title: "Risk-Neutral Measure Explained With an Example"
description: "Learn how risk-neutral measure in options pricing changes probability distributions to simplify derivatives valuation via arbitrage."
keywords:
  - risk neutral measure
  - options pricing
  - binomial tree
  - martingale measure
  - derivatives valuation
  - arbitrage-free pricing
---

*The **risk-neutral measure** is a mathematical tool that lets traders and analysts price derivatives without knowing investors' actual risk preferences. Instead of modeling how real people trade stocks (which depends on their tastes), it models a hypothetical world where all investors are indifferent to risk — and uses that world to pin down prices.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk-Neutral Measure — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A probability measure that makes discounted price processes martingales, eliminating the need to estimate expected returns.</div>

|   |   |
|---|---|
| **Also called** | Equivalent martingale measure, Q-measure |
| **Purpose** | Simplify pricing by assuming investors require no risk premium |
| **Key insight** | Under this measure, all assets drift at the risk-free rate |
| **Connection** | Replaces the physical (real-world) measure with a synthetic one |
| **Use case** | [Binomial trees](/binomial-option-pricing/), [Black-Scholes](/black-scholes-model/), [Monte Carlo](/monte-carlo-valuation/) |

</aside>

## Why Risk-Neutral Pricing Works

When you build a mathematical model to price a [derivative](/derivatives-hedging/), you face an immediate problem: the future returns of the underlying asset depend on investor risk preferences, which are unknowable and change over time. If you try to forecast real stock returns and apply a [discount rate](/discount-rate/) that reflects genuine risk aversion, you get a circular problem — your price depends on an assumption you cannot verify.

The risk-neutral measure sidesteps this by asking a simpler question: *What probability distribution would make the expected (discounted) future value of the asset equal to its current market price?* Once you solve for that distribution, you can use it to price any derivative written on that asset, regardless of real-world risk appetite.

This works because of arbitrage. If the derivative price you compute differs from the market price, traders can construct a hedge that locks in a risk-free profit, which forces the market to adjust. The derivative price must therefore satisfy the risk-neutral pricing formula, or traders will exploit the gap.

## The Binomial Tree Intuition

A two-step binomial tree makes this concrete. Suppose a stock trades at $100 today, the risk-free rate is 5% per year, and in one year the stock is equally likely to be at $120 or $80 (in the real world).

You want to price a one-year call option with a strike of $100. At maturity:
- If the stock is $120, the call pays $20.
- If the stock is $80, the call pays $0.

The naive approach: estimate a drift µ for the stock, compute the real-world expected payoff, and discount. But µ is unobservable.

The risk-neutral approach: find the synthetic probability *q* such that the expected stock price (under *q*) discounted at the risk-free rate equals the current price.

$$E_q[S_1] / (1.05) = 100$$

$$q \cdot 120 + (1 - q) \cdot 80 = 105$$

$$100q + 80 = 105$$

$$q = 0.25$$

So under the risk-neutral measure, the stock goes up with probability 0.25 and down with probability 0.75. Note: this is *not* the real-world probability; it's a pure mathematical device.

Now price the call:

$$\text{Call price} = [0.25 \cdot 20 + 0.75 \cdot 0] / 1.05 = 5 / 1.05 \approx \$4.76$$

This price ensures no arbitrage. You could verify this by noting that if you buy the call and sell (delta-hedge with) a carefully weighted portfolio of stock and bonds, you lock in the risk-free rate.

## Real vs. Risk-Neutral Probabilities

The real-world probability might be that the stock goes up 60% of the time and down 40% of the time. Under the real measure:

$$E_{\text{real}}[S_1] = 0.6 \cdot 120 + 0.4 \cdot 80 = 104$$

The real expected return is 4% (below the risk-free rate), which makes sense: investors are willing to hold risky stock because they demand some premium beyond the risk-free rate, or perhaps they hold it for other reasons. The point is, the real-world probabilities *don't matter for pricing the option*.

What matters is that the market price of the stock is $100. That price already reflects the collective risk appetite of all traders. The risk-neutral measure extracts what that price implies about the future, without requiring you to estimate utility functions or risk preferences.

## How the Risk-Neutral Measure Changes with the Model

In a [Black-Scholes](/black-scholes-model/) world, the risk-neutral measure modifies the drift of the stock's logarithm. Under the physical measure, a stock drifts with its expected return µ. Under the risk-neutral measure, it drifts with the risk-free rate *r*:

**Physical measure (real world):**
$$d S = \mu S \, dt + \sigma S \, dW_{\text{physical}}$$

**Risk-neutral measure (pricing world):**
$$d S = r S \, dt + \sigma S \, dW_{\text{risk-neutral}}$$

The volatility σ stays the same under both measures (volatility is observable from the market and does not change), but the drift becomes the risk-free rate. This is the essence of risk-neutral pricing: equalize all expected returns to *r*, so the discount rate is always *r*, and arbitrage-free prices follow.

## When the Measure Matters Practically

Traders use risk-neutral pricing every day, often without saying the word. When you plug numbers into a [Black-Scholes calculator](/black-scholes-model/), you are implicitly using the risk-neutral measure. The formula assumes you know the current price (which you do), the risk-free rate (which you can observe), volatility (which you can estimate), and time to expiration. You do *not* need the drift µ.

For structured derivatives with multiple sources of [risk](/value-at-risk/), or for portfolios where real-world probabilities genuinely matter (e.g., credit [default](/sovereign-default/) scenarios), a trader might also compute the physical measure for risk management. But pricing always uses the risk-neutral measure.

## The Practical Limit: Basis Risk and Model Error

The risk-neutral approach assumes your model is correct and your [hedge](/derivatives-hedging/) is perfectly executable. In reality, the underlying asset might jump unexpectedly, you might have [transaction costs](/bid-ask-spread/), or the model might have missed a risk factor. These mismatches mean the hedged position is not truly risk-free, and the model price is only an approximation of what the market will bear.

For liquid options on major indices or currencies, the model price typically matches the market price closely. For less liquid or more exotic derivatives, model price and market price can diverge, and trader intuition and [vega](/vega/) or [gamma](/gamma/) judgments fill the gap.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes Model](/black-scholes-model/) — The canonical option pricing formula using risk-neutral valuation
- [Binomial Option Pricing](/binomial-option-pricing/) — A discrete-time framework for risk-neutral trees
- [Delta Hedging](/delta/) — The hedging strategy that makes risk-neutral pricing arbitrage-free
- [Option Premium](/option-premium/) — What the risk-neutral measure implies about price behavior
- Martingale Measure — The mathematical foundation for equivalent martingale measures
- Stochastic Volatility — How to extend risk-neutral pricing to dynamic volatility models

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — Why derivatives pricing is inseparable from hedging
- [Discount Rate](/discount-rate/) — How discounting works in the risk-neutral framework
- [Volatility Smile](/volatility-smile/) — Market prices that deviate from single-model risk-neutral prices
- [Monte Carlo Valuation](/monte-carlo-valuation/) — A computational method for risk-neutral pricing in complex models

</div>
