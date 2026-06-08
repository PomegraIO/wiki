---
title: "Second-Order Risk: Gamma and Convexity"
description: "Gamma and convexity measure how a position's value curve bends, revealing risk that linear (delta/duration) estimates miss—critical when volatility spikes or rates move sharply."
keywords:
  - second order risk gamma convexity
  - gamma risk options
  - convexity bond risk
  - non-linear risk
image: /svg/risk.svg
---

*Traders and portfolio managers use two main tools to measure sensitivity: **delta** (for options) and **duration** (for bonds) capture how much value changes with a 1% move in the underlying. But these are straight-line measures. **Gamma** and **convexity** measure the curvature—how much faster or slower that sensitivity itself changes. Ignoring curvature leads to massive underestimates of risk when volatility or rates shift sharply.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Second-Order Risk — Key Facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">Linear risk measures break down in turbulent markets; curvature catches what they miss.</div>

|   |   |
|---|---|
| **First-order (linear)** | Delta (options), duration (bonds) |
| **Second-order (curvature)** | Gamma (options), convexity (bonds) |
| **Why it matters** | Underestimates loss in stress scenarios |
| **Appears when** | Large moves, volatility spikes, rate shocks |
| **Metric** | Gamma often measured in dollars per 1% move in the underlying volatility |
| **Management** | Hedge, rebalance, or accept; often requires dynamic trading |

</aside>

## Why straight-line risk breaks down

Imagine you hold 100 shares of a stock at $50 (delta of 1.0). A simple linear assumption says: if the stock drops to $49, you lose $100. If it drops to $40, you lose $1,000. Straight math.

Now imagine you own a [call option](/call-option/) on that same stock, struck at $50, while the stock is also at $50. The option has a delta of around 0.5. Linear thinking says a $1 drop costs you $50. But options don't work that way. As the stock falls, the option becomes less likely to be exercised, so its delta *shrinks*—to 0.4, then 0.3. Each dollar drop now costs you less. The relationship between the option's value and the stock price is curved, not straight.

That curvature is gamma—and it can be your ally or enemy depending on which side of the option you sit.

## Gamma: The acceleration of delta

**Gamma** measures how much delta itself changes when the underlying moves by 1%. It is the second derivative of the option's value.

For the long call buyer:
- Gamma is always positive. As the stock rises, delta accelerates toward 1.0 (the option behaves more like owning the stock). As it falls, delta decelerates toward 0.
- This is favorable: in a big rally, you gain more than linear math predicts. In a crash, you lose less.

For the short call seller (the option writer):
- Gamma is negative. The curvature works against you. In a rally, the call accelerates in value faster than delta predicted. You bleed losses. In a crash, you don't benefit as much as delta suggested.

A high-gamma position in a volatile market is like holding an asymmetric bet: you win when volatility creates large moves, lose when moves are small. A low-gamma position is "sticky"—your P&L follows the linear prediction closely.

## Convexity: The same principle for bonds

[Bonds](/bond/) have duration, which measures how much their price falls (on average) when [interest rates](/interest-rate/) rise by 1%. A bond with 7-year duration loses roughly 7% in value if rates jump from 2% to 3%.

But bonds are also curved. When rates *rise*, the bond's duration shrinks—it becomes less sensitive to further rises. When rates *fall*, duration grows. This curve is **convexity**.

**Positive convexity** (the normal case for a regular bond):
- When rates rise, the bond loses value, but not as much as duration predicts, because duration is shrinking.
- When rates fall, the bond gains value faster than duration predicts, because duration is growing.
- This is beneficial to the bondholder: you gain more in rate rallies and lose less in rate selloffs.

**Negative convexity** (e.g., a [callable bond](/callable-bond/) where the issuer can refinance if rates fall):
- If rates fall sharply, the issuer may exercise the call, capping your upside.
- The bond's price doesn't rise as much as positive-convexity math suggests.
- You lose the asymmetric benefit of duration.

## Measuring second-order risk in practice

**For options:** Gamma is usually quoted in dollars per 1% change in volatility, or as a raw number per 1-point move in the underlying. A short call position with a gamma of -10 means each 1-point move in the stock costs you an additional $10 in gamma losses (on top of delta losses).

**For bonds:** Convexity is measured in basis points per 100 basis points of rate change, or sometimes per 1 basis point. A bond with a duration of 7 and convexity of 100 will lose approximately:
- Duration loss: 7 × 2 = 14 basis points
- Convexity gain: 0.5 × 100 × (2)² = 200 basis points
- Net: about 186 basis points, *not* 200

In a 200 basis point rate rise, the second-order effect cuts the loss by nearly 7%. In a crisis with a 400 basis point move, the difference is even larger.

## When second-order risk explodes

**Large, sudden moves trigger gamma losses:**
- A trader holding short puts on a stock expects a small loss if the stock drops 2–3%. If the market gaps down 15% overnight, gamma loss can dwarf the delta prediction.
- During the 2020 COVID crash, gamma losses on short call positions forced margin calls and cascade selling.

**Volatility spikes activate gamma risk:**
- A short call position that was comfortable on a quiet day becomes dangerous when [implied volatility](/implied-volatility/) jumps. The option premium suddenly extends further, amplifying losses.

**Rate shocks reveal bond convexity:**
- In March 2020, when the [Federal Reserve](/federal-reserve/) cut rates emergency-style from 1.5% to 0%, many duration-hedged portfolios still suffered losses because they hadn't accounted for the convexity flattening.
- In 2022, when rates rose from near-zero to 4%, positive-convexity bonds cushioned the fall better than duration models alone predicted.

## Managing second-order risk

**For option traders:**
- **Gamma-hedge:** Buy options to hedge short positions, or sell options to cap upside if you're long.
- **Rebalance:** Adjust delta exposure frequently as prices move, locking in gains.
- **Size limits:** Cap gross notional exposure if gamma is large, to prevent blowups in stress scenarios.

**For bond managers:**
- **Capture positive convexity:** Prefer callable-free bonds and avoid callable issues.
- **Match duration:** If a liability is due in 7 years, match it with 7-year duration assets; convexity is a bonus.
- **Stress test:** Model what happens if rates spike to levels not seen in the current data—convexity assumptions may break.

**For risk teams:**
- **Scenario analysis:** Test positions under large moves (e.g., ±300 basis points on rates, ±20% on equities), not just 1-standard-deviation moves.
- **Greeks monitoring:** Track gamma, theta, and vega in real time; set limits on [Value at Risk](/value-at-risk/) under stress.
- **Tail risk budget:** Acknowledge that rare, extreme moves will have second-order effects; build reserves accordingly.

## The hidden trap: model risk

[Black-Scholes](/black-scholes-model/) and other option-pricing models assume constant volatility and smooth markets. In reality, volatility spikes and gaps happen. When they do, gamma accelerates faster than the model predicts, and convexity assumptions can fail.

During the 1987 stock market crash, models grossly underestimated gamma losses because volatility jumped to levels the models had never "seen." During 2008, mortgage-backed securities suffered convexity loss when prepayment behavior inverted—homeowners stopped refinancing when rates rose (opposite of the normal pattern), flipping the sign of convexity.

Always test your assumptions under stressed conditions, and always assume that second-order effects will be *larger* than the model suggests, not smaller.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — The first-order sensitivity of an option's value to the underlying price
- [Theta](/theta/) — Time decay; another second-order risk for option sellers
- [Vega](/vega/) — Sensitivity to changes in implied volatility
- [Duration](/duration/) — The first-order sensitivity of a bond's price to interest rates
- [Black-Scholes Model](/black-scholes-model/) — The foundational (but limited) option-pricing framework
- [Implied Volatility](/implied-volatility/) — The volatility that makes the market price make sense under Black-Scholes

### Wider context

- [Value at Risk](/value-at-risk/) — A risk metric that captures tail losses but may underestimate second-order effects
- [Stress Testing](/stress-testing/) — The discipline that catches second-order surprises
- [Volatility Smile](/volatility-smile/) — Evidence that option models systematically misprice based on strike and maturity
- [Call Option](/call-option/) — The instrument where positive gamma helps the buyer
- [Bond](/bond/) — The instrument where positive convexity is a natural feature
- [Callable Bond](/callable-bond/) — A bond where negative convexity can bite

</div>
