---
title: "Forward-Start Options: Pricing and Use Cases"
description: "How forward start option pricing works when the strike is set at a future date, using forward volatility and conditional pricing frameworks."
keywords:
  - forward start option pricing
  - strike-setting delay
  - forward volatility
  - cliquet options
  - employee stock options
image: "/svg/derivatives.svg"
---

*A **forward-start option** is an option whose strike price is set not today but at a specified future date, typically when the option enters the money or when an employee becomes vested. The pricing must account for the volatility between now and strike-setting day, and the contracts appear frequently in employee compensation and structured products like cliquet options.*

## Why Forward-Start Options Exist

Forward-start options solve a practical problem: sometimes the relevant economic strike should reflect future market conditions, not today's price. When a company grants options to an employee, for instance, it often wants the option to be neither too easy nor impossible to exercise. By deferring the strike to the vesting date, the grant committee can set a strike closer to the then-current stock price, making the incentive more meaningful.

The same logic applies to cliquet options (sometimes called ratchet or reset options), which reset their strike periodically — say, quarterly or annually — to lock in gains and start fresh. Each reset effectively creates a new forward-start option. A retail investor trading structured notes or warrants may also encounter these without realizing it.

## How Forward-Start Volatility Enters the Pricing

Standard [options](/option/) like [calls](/call-option/) or [puts](/put-option/) have a known strike and a known time to expiration, so pricing models (like Black-Scholes) need just one volatility input: the historical or implied volatility of the underlying until expiry. Forward-start options are trickier.

Suppose today is Day 0, the strike will be set on Day T, and the option expires on Day T + τ. The option's payoff depends on the stock price on Day T + τ relative to the Day T strike. Pricing requires:

1. **Forward volatility**: the volatility of the stock from Day 0 to Day T (when strike is set).
2. **Continuation volatility**: the volatility from Day T to Day T + τ (after strike is set).

In many models, these are assumed equal, but in practice they can differ. The valuation often uses the [Black-Scholes model](/black-scholes-model/) applied conditionally: the option is priced as if we freeze the stock price on Day T, then apply the standard formula for a τ-period option starting at that unknown future price.

## Pricing Mechanics: The Conditional Approach

The most intuitive approach treats the strike-setting date as creating two phases:

**Phase 1 (Day 0 to Day T):** Uncertainty about what the strike will be. If the strike is simply the stock price at Day T (an at-the-money-forward strike), the option owner faces no intrinsic value loss but gains all upside from Day T onward.

**Phase 2 (Day T to Day T + τ):** The strike is now known, and the option behaves like a standard option over the remaining τ periods.

Under this two-phase model:

- If the stock rises sharply by Day T, the strike rises too, resetting the option toward at-the-money.
- The longer the strike-setting delay, the more uncertain that strike becomes, and the more valuable the optionality (all else equal).
- An increase in volatility during Phase 1 *raises* the value of a long position, because the stock can move higher, pushing the future strike higher, while the option holder still captures all gains above that strike.

The option's theoretical value can be approximated by:

$$C = S_0 \exp(-r T) \left[ \mathbb{N}(d_1) - \mathbb{N}(d_2) \right]$$

where the parameters account for the Phase 1 and Phase 2 volatilities. Traders typically use a weighted or blended volatility if the two phases are likely to differ.

## Employee Stock Options and Cliquets

Forward-start structures are ubiquitous in employee compensation. A tech company might grant options with a strike set on the vesting date (say, four years hence). This achieves two goals:

1. It avoids granting deep-in-the-money or out-of-the-money options on the grant date.
2. It ties the strike to the employee's performance period, creating a more neutral incentive.

From a valuation standpoint, these forward-start grants are worth more than standard at-the-money options granted today, because they benefit from price appreciation between grant and vesting. However, they also carry [execution risk](/execution-risk/): if the company's stock tanks by vesting, the strike is set very low, making the option highly valuable but potentially at odds with shareholder interests.

Cliquet options (popular in structured products) apply the same logic repeatedly. Imagine a cliquet call that resets its strike quarterly. Each quarter, the strike snaps to the then-current spot price, locking in any gain. If the stock rises 5% in Q1, the Q2 strike is 5% higher than the Q1 strike. This creates a series of overlapping forward-start optionalities, all priced into a single product.

## Volatility Term Structure Matters

Because forward-start options depend on multiple volatility windows, traders must consider the [volatility smile](/volatility-smile/) and term structure carefully:

- **Steep term structure** (near-term volatility higher): The Phase 1 volatility is high, making strike uncertainty large, which increases the option's value.
- **Inverted structure**: Phase 1 volatility is low, so the strike is more predictable, reducing the option's value relative to a standard option.
- **Skew**: If the underlying has negative skew (e.g., equities tend to have downside skew), a forward-start call may be less attractive because the likely future strike could be pulled down by a crash.

Market participants price forward-start options by extracting the forward volatility curve from traded vanilla [options](/option/) and using those implied volatilities as inputs to pricing models. This practice can create arbitrage opportunities if the forward curve is mispriced.

## Applications Beyond Employee Compensation

Forward-start options appear in several financial contexts:

**Structured Products:** Insurers and investment banks embed cliquet calls and puts in index-linked notes, offering downside buffers and quarterly resets.

**Commodity Markets:** Forward-start options on crude oil or agricultural futures allow hedgers to lock in future strike prices without committing capital today.

**Currency Forwards:** Multinationals sometimes use forward-start FX options to hedge projected cash flows at uncertain future dates.

**Convertible Bonds:** Some convertibles allow the conversion price (strike) to be reset after a delay, creating a forward-start dynamic.

## Comparison to Standard Options

| Feature | Standard Option | Forward-Start Option |
|---------|-----------------|----------------------|
| **Strike** | Fixed at grant/issue | Set at future date |
| **Pricing input** | One volatility (now to expiry) | Forward volatility (now to strike-setting) |
| **Intrinsic value at inception** | Immediate if ITM | Zero until strike is set |
| **Price movement sensitivity** | Delta hedging straightforward | Delta changes at strike-setting date |
| **Use case** | Speculation, hedging | Incentive schemes, structured products |

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational contract whose payoff depends on a strike price and expiration date
- [Black-Scholes Model](/black-scholes-model/) — the canonical pricing framework for options with fixed strikes
- [Implied Volatility](/implied-volatility/) — the volatility backed out from traded option prices, essential input to forward-start valuation
- [Call Option](/call-option/) — the right to buy at a strike; forward-start variants reset that right at a future date
- [Exercise Price](/exercise-price/) — the strike; in forward-start options, determined later rather than today
- [Strike Price](/strike-price/) — the fixed level in standard options; the uncertain-but-critical input in forward-start structures

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — the broad context of using options to manage risk
- [Employee Stock Options](/employee-stock-options/) — compensation tool often structured as forward-start
- [Volatility Smile](/volatility-smile/) — the skew and term structure that shape forward volatility curves
- [Structured Products](/structured-product/) — consumer-facing investments embedding cliquet and other exotic options

</div>
