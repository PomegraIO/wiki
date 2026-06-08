---
title: "Early Exercise Premium for American Options"
description: "Early exercise premium explains why American options cost more than European: the value of choosing when to exercise, quantified and when it matters."
keywords:
  - early exercise premium
  - american options
  - american call options
  - american put options
  - american option pricing
  - early exercise value
---

*An **early exercise premium** is the extra value built into an [American option](/american-option/) compared to its [European counterpart](/european-option/), purely because the American option can be exercised at any time before expiration, while the European option can only be exercised at expiration. The premium is not a constant; it depends on the stock price, time to expiration, [interest rates](/interest-rate/), and dividends.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Early Exercise Premium — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">The difference between American and European option values; large for puts, often zero for calls without dividends.</div>

|   |   |
|---|---|
| **Definition** | American value minus European value, same strike and underlying |
| **For calls** | Usually small or zero if no dividends; positive if dividends are large |
| **For puts** | Often substantial; increases with time to expiration and interest rates |
| **Driven by** | [Interest rates](/interest-rate/), [dividends](/dividend/), [volatility](/volatility-smile/), [time value](/time-value/) |
| **Quantified by** | Binomial trees, finite-difference methods, or simulation |
| **Never zero for puts** | Because early exercise is sometimes optimal |

</aside>

## The Economic Intuition

When you own a [European call option](/call-option/), you must wait until expiration to exercise. If the call is deep in-the-money and dividend payments are imminent, you cannot exercise early to capture the dividend—you simply lose it. An [American call option](/call-option/) lets you exercise right before the ex-dividend date and receive the cash, even though you are sacrificing the remaining time value.

Similarly, if you own a [European put option](/put-option/) and the stock crashes, you want to exercise and lock in the gain. An American put lets you do that immediately; a European put forces you to wait. If the stock rallies again before expiration, your European put suffers, but the American put owner has already cashed out.

The early exercise premium measures the value of this optionality. It is always non-negative (an American option is worth at least as much as a European option with the same terms) but can be zero in some cases.

## Why Early Exercise is Optimal: Calls

A call is worth more held alive than exercised (when out-of-the-money) because of the [time value](/time-value/) — the stock could surge and reward the call holder for waiting. The only reason to exercise a call early is to capture a dividend.

**With no dividends:**

A [risk-free rate](/interest-rate/) of 5% means money grows faster in your pocket than a stock that pays no cash return. Intuitively, you might think: exercise early and invest the proceeds in a risk-free bond. But this logic is wrong. The intrinsic value you receive on early exercise is less than the current call price (which includes time value). Exercising early means selling a valuable asset at a discount. You are better off selling the call to someone else for its full price, including time value.

Formally, the value of a call is always at least its intrinsic value, and the call holder's optimal policy is to hold (not exercise) until either expiration or a dividend event.

Result: **American and European calls have equal value if there are no dividends or if dividends are very small.**

**With large dividends:**

Now suppose the stock pays a 5% dividend in one week, and the call is $10 in-the-money. A European call holder cannot exercise and thus forfeits the dividend. An American call holder can exercise one day before the ex-dividend date, collect the stock, and receive the dividend.

The dividend received is tangible value. If the dividend is large enough to outweigh the time value sacrificed by early exercise, the American call holder will exercise.

The early exercise premium for calls is therefore:

$$\text{Call premium} \approx \text{(present value of dividend)}$$

when the option is in-the-money and the dividend is imminent. The deeper in-the-money, the more likely early exercise is optimal.

## Why Early Exercise is Optimal: Puts

Puts are different. A put holder profits from the stock *falling*, so interest rates and dividends both push toward early exercise.

**Interest rate effect:**

If you exercise a put and receive strike price $K$ in cash, you can invest that cash at the risk-free rate. The longer you wait, the more interest you miss. A European put holder cannot lock in this gain until expiration.

Result: American puts are worth more than European puts, even with no dividends.

**Dividend effect:**

A dividend lowers the stock price on the ex-dividend date. A put holder benefits from this price decline. An American put holder can wait for the ex-dividend date and then exercise at a more favorable (lower) stock price. A European put holder cannot time the exercise.

**Deep in-the-money:**

A put that is far in-the-money has high [intrinsic value](/intrinsic-value/) and low time value. Exercise and lock in the gain. Waiting provides little upside (the stock is already well below the strike) but costs interest on the cash proceeds. The optimal policy is to exercise immediately.

Result: **The early exercise premium is largest for deep in-the-money American puts, and can be substantial (many percentage points of the call price).**

## Quantifying the Premium: A Binomial Example

Consider a six-month put option on a $100 stock, strike $100, risk-free rate 5%, volatility 20%, and no dividends. 

Using Black-Scholes (European):

$$P_{\text{European}} \approx \$5.57$$

Using a binomial tree that allows early exercise (American):

$$P_{\text{American}} \approx \$5.89$$

$$\text{Premium} = 5.89 - 5.57 = \$0.32$$

The premium here is modest (about 6% of the European value) because the option is at-the-money, interest rates are moderate, and there are no dividends.

Now suppose the stock is at $90 (put is $10 in-the-money):

$$P_{\text{European}} \approx \$10.50$$

$$P_{\text{American}} \approx \$10.89$$

$$\text{Premium} = \$0.39$$

Still small because the put's time value (the benefit of waiting) is already low when deep in-the-money.

But if you raise the risk-free rate to 20% (an extreme scenario):

$$P_{\text{European}} \approx \$9.89$$

$$P_{\text{American}} \approx \$10.50$$

$$\text{Premium} = \$0.61$$

The premium widens because early exercise (and investment of the strike price) becomes more attractive.

## When Does the Premium Matter in Practice?

**For calls:**

The premium is rarely material unless:
- The stock is in-the-money.
- Large dividends are imminent.
- The option is near expiration.

Otherwise, call premiums are small, and American and European calls trade at nearly identical prices.

**For puts:**

The premium is always positive but is most visible when:
- The put is deep in-the-money (intrinsic value dominates).
- Interest rates are high (investment opportunity is attractive).
- Time to expiration is long (more opportunity to exercise and earn interest).

For out-of-the-money or at-the-money puts with normal interest rates and plenty of time remaining, the premium is usually single-digit percentage points.

## How Traders Price American Options

Because American option values do not have a closed-form solution like [Black-Scholes](/black-scholes-model/), traders use:

1. **Binomial trees:** Build a lattice of possible stock prices, compute the payoff at expiration, then work backward. At each node, compare the exercise payoff (intrinsic value) to the hold value (expected discounted next-period value). If exercise is better, use that. Otherwise, use the hold value. The early exercise premium emerges naturally.

2. **Finite-difference methods:** Solve the option-pricing PDE with a boundary condition that enforces the early-exercise decision at each point.

3. **Monte Carlo with least-squares regression:** Simulate paths forward, then regress to estimate the optimal exercise boundary.

For liquid American options (e.g., S&P 500 index puts), the market price incorporates the premium, and traders use the market price as a reference. For less liquid options, traders rely on their chosen computational method.

## The Role of Volatility

[Volatility](/volatility-smile/) works against early exercise. High volatility means the stock could swing dramatically in either direction, so the time value of waiting is large. Conversely, low volatility means the future is more predictable, and time value shrinks, making early exercise more attractive.

Result: The early exercise premium **decreases** as volatility increases. A highly volatile stock has a smaller American-vs-European gap.

## See also

<div class="wiki-seealso">

### Closely related

- [American Option](/american-option/) — Definition and general properties
- [European Option](/european-option/) — The baseline for comparison
- [Black-Scholes Model](/black-scholes-model/) — Formula for European options (no early exercise)
- [Binomial Option Pricing](/binomial-option-pricing/) — Computational tool that naturally values early exercise
- [Intrinsic Value](/intrinsic-value/) — The payoff from immediate exercise
- [Time Value](/time-value/) — The value of waiting, competing with exercise opportunity

### Wider context

- [Dividend Adjustment in Options Pricing](/dividend-adjustment-options-pricing/) — Dividends drive call early exercise
- [Volatility Smile](/volatility-smile/) — Market volatility and moneyness effects on option prices
- [Interest Rate](/interest-rate/) — Drives the benefit of early exercise for puts
- [Call Option](/call-option/) — Why calls rarely have an early-exercise premium
- [Put Option](/put-option/) — Why puts often have a material early-exercise premium

</div>
