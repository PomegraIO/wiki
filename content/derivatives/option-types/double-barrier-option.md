---
title: "Double Barrier Option"
description: "An option with both an upper and lower barrier level, knocked out or activated if either barrier is breached."
keywords:
  - double barrier
  - two-way barrier
  - exotic option
  - range option
  - dual barrier
  - option derivatives
image: /svg/derivatives.svg
---

*A **double barrier option** is a [barrier option](/barrier-option/) with both an upper and a lower boundary. If the underlying asset breaches either barrier during the option's life, the option is either terminated (knockout) or activated (knock-in), depending on the contract's design. The option remains alive only while the underlying stays between the two levels.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Double Barrier Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and options." />

<div class="wiki-infobox-caption">Controlled by bounds: both up and down breaches matter equally.</div>

|   |   |
|---|---|
| **What it is** | A [barrier option](/barrier-option/) with symmetric or asymmetric upper and lower thresholds |
| **Also called** | Two-way barrier, double-knock option, corridor option |
| **Barrier structure** | Upper barrier (cap) and lower barrier (floor) |
| **Knockout form** | Option dies if either barrier is touched |
| **Knock-in form** | Option activates only if either barrier is touched |
| **Primary use** | Range-bound strategies; volatility play on confined movement |
| **Pricing factor** | Probability of breaching either boundary; path-dependent |

</aside>

## The bounded universe

In a standard [barrier option](/barrier-option/), a single threshold divides possibility from extinction. A double barrier option imposes two thresholds, confining the option's lifetime to a corridor between them. The width of that corridor—the gap between upper and lower barriers—directly shapes the option's value.

Consider a three-month [call option](/call-option/) on a stock trading at $100. A typical single-barrier knockout [call](/call-option/) might die if the stock rises above $120. A double barrier [call](/call-option/), by contrast, might live only as long as the stock stays between $80 and $120. Now both tails threaten termination. If the stock collapses to $75, the option dies just as surely as if it had rocketed to $125. The option's entire value depends on the underlying staying in that corridor until expiry.

This confinement makes double barriers significantly cheaper than vanilla [options](/option/). A trader paying $5 for a standard [call](/call-option/) might pay $1.50 for a double barrier equivalent, because the corridor constraint dramatically raises the probability of knockout before [intrinsic value](/intrinsic-value/) can be harvested. Conversely, this discount creates opportunity: if you believe the underlying will stay in a range, you capture the insurance benefit of the [option](/option/) at a fraction of traditional cost.

## Symmetric versus asymmetric barriers

**Symmetric barriers** place equal distances above and below the current price. A stock at $100 might have barriers at $95 (floor) and $105 (cap). The corridor is tight and symmetric, reflecting equal downside and upside risk.

**Asymmetric barriers** are the more common design in practice. An investor might set a tight cap ($110) to protect against runaway gains, while allowing a wider floor ($70) to tolerate moderate downside. This asymmetry aligns with the trader's actual risk tolerance: they care less about the stock rallying than about a crash.

Pricing is sensitive to this asymmetry. The further apart the barriers, the higher the option's value, all else equal. A barrier pair ($80, $120) prices higher than ($90, $110) because the wider corridor means a lower probability of knockout. Traders adjust barrier spacing to hit a target premium or probability-of-survival threshold.

## Knockout versus knock-in mechanics

A **double-knockout barrier** option dies the moment either barrier is touched. This is the more intuitive form: you're buying a range-bound bet. A double-knockout [call](/call-option/) between $80 and $120 is like saying, "I win if the stock stays in this corridor and finishes above my strike; I lose if it breaks either boundary or finishes below my strike." The corridor constraint is a penalty, not a feature. These options are sold by traders betting the underlying will break out, making them sellers of "range confidence."

A **double knock-in barrier** option springs to life—becomes a live, in-the-money [put](/put-option/) or [call](/call-option/)—only if the underlying breaches one of the two barriers. This is a speculative structure: you're betting on a breakout in either direction, and only if that breakout happens do you gain a live payoff. Before the barrier touch, the option is inert. If expiry arrives with both barriers untouched, the option expires worthless. Double knock-ins are cheap precisely because breakouts are rare events in stable, range-bound markets.

## Pricing and probability challenges

Valuing a double barrier option is notably harder than pricing a single-barrier [option](/barrier-option/) because the pricing engine must account for the probability of breaching two distinct levels independently. If the barriers are at $80 and $120, the valuation must weight:
- The probability of staying within [$80, $120] to expiry.
- The probability of touching $80 before touching $120 (and vice versa).
- The timing of any breach and its effect on the remaining time value.

These probabilities are path-dependent—they hinge on how the underlying moves, not just where it lands. Monte Carlo simulation is the standard computational tool because it can naturally incorporate the sequence of prices along each path, checking whether either barrier is crossed at any step.

Closed-form solutions exist for simplified cases (constant volatility, log-normal distribution), but they become unwieldy and require numerical approximation for realistic parameter sets. The Greeks—[delta](/delta/), [gamma](/gamma/), [vega](/vega/)—are highly sensitive to position within the corridor; an underlying near one barrier exhibits much higher [gamma](/gamma/) than one in the middle, because a small price move changes the probability of knockout substantially.

## Real-world applications

**Forex carry strategies** frequently use double barrier options. A trader holding a high-interest-rate currency [call](/call-option/) against a low-rate currency might add a double barrier structure: the option lives if the pair stays within an expected trading range, but expires if it breaks either way, capping the trader's exposure in a sudden currency crisis or correction.

**Commodity trading** uses double barriers on crude oil, natural gas, and agricultural [futures](/futures-contract/). A producer hedging output might use a double-knockout [put](/put-option/) with a floor (protection below a minimum price) and a cap (acceptable upside at some reasonable price). This structure lowers the hedge cost while maintaining protection in the trader's target price band.

**Equity index strategies** employ double barriers in emerging market [options](/option/). An index option on Indian stocks might have barriers at 15% below and 20% above the current level, reflecting the trader's tolerance for volatility. Outside that corridor, the option's value is minimal anyway due to transaction costs and basis drift.

**Convertible bond hedging** sometimes embeds double barriers: conversion rights activate only if the stock price stays within a defined band, discouraging sudden moves that would disrupt the bond issuer's capital structure.

## The correlation between barriers

Double barrier dynamics introduce a concept absent in single-barrier products: correlation between barrier outcomes. If the underlying is highly volatile, it's more likely to breach *either* barrier. If it's calm, both barriers might survive to expiry undisturbed. This correlation drives the smile/skew in [implied volatility](/implied-volatility/) for double barriers: [volatility](/volatility-smile/) traders who see spikes in realized volatility prefer to sell double-knockout barriers (betting volatility won't spike further), while those expecting calm prefer to buy them.

## See also

<div class="wiki-seealso">

### Closely related

- [Barrier option](/barrier-option/) — the parent class; single-barrier forerunner
- [Window barrier option](/window-barrier-option/) — barriers active only in a time window
- [Knock-out option](/barrier-option/) — simple one-sided knockout structure
- [Knock-in option](/barrier-option/) — simple one-sided activation structure
- [Range option](/barrier-option/) — pays off based on whether underlying stays in band
- Exotic option — the broader universe of custom-payoff derivatives

### Wider context

- [Option](/option/) — the fundamental derivative contract underlying all barrier variants
- [Implied volatility](/implied-volatility/) — critical pricing input for path-dependent structures
- Path dependence — why the route matters, not just the destination
- [Volatility smile](/volatility-smile/) — smile steepens for double barriers as correlation between barriers rises

</div>
