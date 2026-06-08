---
title: "Forward Start Option Explained"
description: "How forward start options defer activation to a future date with the strike price set relative to spot, commonly used in employee compensation and structured products."
keywords:
  - forward start option explained
  - forward start option strike price
  - cliquet options employee stock
  - deferred option activation
  - forward start derivatives
---

*A **forward start option** is a derivative contract that does not become active until a future date (the activation date), at which point its strike price is automatically set as a fixed percentage above or below the spot price on that date. Unlike a standard option purchased today with a known strike, a forward start option's strike is deferred and anchored to future spot—not today's price. This design makes it attractive for employee stock awards (where the employer wants to grant an option that starts in-the-money relative to a future baseline, not today's price) and for structured notes that reset periodically.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forward Start Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Strike is set later, at activation; useful when the reference price is unknown today.</div>

|   |   |
|---|---|
| **Strike-setting mechanism** | At activation date (future), strike = spot price × fixed percentage (e.g., 100% for at-the-money, 110% for 10% out-of-the-money call) |
| **Activation date** | The forward date when the option becomes live and the strike is locked in |
| **Exercise date** | Typically extends past activation (e.g., activate in 2 years, expire in 3 years); expiration is measured from activation, not from signing |
| **Common usage** | Employee equity grants, performance-linked notes, equity-linked swaps, structured products with step-up coupons |
| **Pricing** | Depends on volatility of the underlying stock/index and the time to activation; strike uncertainty adds complexity |
| **Tax implication (employee grants)** | Often treated as a grant of zero initial value (no immediate income tax) because strike equals future spot on activation |

</aside>

## Why strike is set at a future date, not today

In a standard equity call option purchased today, the strike is fixed immediately. The holder buys the right to purchase the stock at, say, \$100, regardless of what the stock does. An employee receiving such a grant faces an immediate tax decision: if the strike is below the current spot price, the IRS may deem it "in-the-money at grant" and assess ordinary income tax.

With a **forward start option**, the strike is not locked until the activation date arrives. At that future moment, the strike is set to a percentage of the then-current spot—typically 100% (at-the-money) or slightly higher. This design achieves two goals:

1. **Tax neutrality at grant**: Because the strike equals spot at activation, the option is at-the-money at that future point, so there is typically no ordinary income tax at grant. Taxation is deferred to exercise or vesting.
2. **Future-relative pricing**: The strike is always pegged to the then-current market price, not to the price when the option was promised. This is fairer in volatile markets. If a stock crashes between the promise date and the activation date, the employee's strike crashes with it (rather than remaining pinned to the old price).

## Typical structure: employment and equity compensation

A common scenario is a four-year employee equity grant with one-year cliff vesting:

1. **Day 1 (grant date)**: The company promises the employee a "forward start call option" that will activate in one year and expire in four years.
2. **Year 1 (activation date)**: The option becomes live. The company observes the stock price (say, \$50 at that moment). The strike is set to \$50 (i.e., at-the-money). The option now has a three-year life remaining.
3. **Year 4 (expiration)**: The employee can exercise the option if the stock is above \$50. If it trades at \$60, the employee exercises and nets \$10 per share.

The advantage to the employer is a tax-efficient grant structure. The advantage to the employee is that they do not bear downside risk from the grant date to the activation date (if the stock falls, the strike falls with it). However, they also don't benefit from an appreciation between grant and activation (the strike rises with the stock, so no "free" gains accrue during the deferral window).

## Cliquet options: chained forward starts

A **cliquet option** (or ratchet option) is a chain of forward start options, resetting repeatedly. Instead of activating once, the option resets—setting a new strike—every period (quarterly, yearly, etc.).

**Example: A five-year cliquet call on an equity index.**
- Year 1: Index is at 100. Strike is set to 100. At year-end, it's at 110, so the option has a \$10 gain so far. Strike locks in, and a new cliquet period begins.
- Year 2: A fresh forward start activates with strike = 110 (the closing price from Year 1). If the index ends at 130, the option gains another \$20.
- This repeats through five periods.

The key feature is that gains are **ratcheted** or locked in after each period. Even if the index crashes in Year 5, the employee keeps the gains from Years 1–4. This makes cliquets popular in deferred bonus plans and structured notes, where employers want to reward employees for outperformance each year without exposing them to later reversals.

## Pricing and valuation challenges

Standard option pricing (Black-Scholes) assumes the strike is known. With a forward start, the strike is random—it depends on future spot price, which is unknown. Valuation requires estimating the distribution of spot prices at the activation date.

For a simple forward start call with 100% moneyness (strike = spot at activation):
- The option is at-the-money at activation by construction.
- Its value at activation is the expected value of a one-year at-the-money option (or whatever remaining life is left).
- Today, we discount that expected future value.

The pricing formula involves the stock's volatility and the time to activation. **Higher volatility increases the forward start's value** because greater price swings make the at-the-money option more valuable at activation. **Longer time to activation also increases value** (more time for spot to move, making the eventual activation-date at-the-money option more valuable).

If the forward start is set to a non-100% moneyness (e.g., strike = 110% of future spot, making it 10% out-of-the-money at activation), the valuation is more complex, and pricing models (Monte Carlo simulation, trinomial trees) are often required.

## Forward starts vs. standard options: trade-offs

| Aspect | Forward Start | Standard Option |
|--------|---------------|-----------------|
| **Strike unknown today?** | Yes; set at activation | No; known at purchase |
| **Price impact of gap (grant to activation)** | Strike moves with stock; no "free" gain | Strike is fixed; benefit from gap gains |
| **Tax at grant (employee)** | Often zero ordinary income (at-the-money at activation) | Possible ordinary income if in-the-money at grant |
| **Valuation complexity** | Higher; strike is random | Standard; strike is deterministic |
| **Use case fit** | Employee grants, deferred compensation, structured notes | Standalone hedges, speculation, tactical positions |

## Structured products and forward-start mechanics

Investment banks embed forward starts into structured notes and indexed products. A "step-up coupon" note might promise:

> Annual coupons are set as follows: each year, we observe the index level. If it is higher than the prior year, you receive 50% of the gain (capped at 5% annually). The next year, the "prior year" resets.

This is effectively a chained series of forward start calls. The bank is short forward start calls to the investor. The bank hedges by holding the underlying index (dynamic rebalancing).

Another example: an autocallable note with forward-start knockouts. The note pays a coupon each year if the index stays above a barrier; the barrier is set relative to the barrier-setting date's spot price, not today's. This defers the barrier definition—a form of forward start—allowing the product designer to create fair, path-dependent exposures that reset.

## Greeks and hedging challenges

Forward start options have the usual Greeks (delta, gamma, theta, vega), but they evolve in a non-standard way. Before activation, the forward start has zero delta (the option is not active, so moves in spot price don't affect option value in a simple linear way). After activation, it behaves like a standard option.

Near the activation date, gamma spikes: a small move in spot price can significantly change the value of the soon-to-activate option, because the moneyness at activation depends on where spot closes on that date. Hedgers must be careful near activation, as gamma risk concentrates.

## Regulatory and accounting treatment

Under **ASC 718** (stock compensation, U.S. GAAP), forward start options are treated as variable-plan equity awards if the number of shares or strike is not fixed at grant. Compensation expense is remeasured each quarter until the strike is locked in (at activation). Once activation occurs and the strike is set, expense is typically fixed and amortized over the remaining service period.

This accounting treatment can create earnings volatility for the employer in the pre-activation window, because the grant's fair value must be recomputed as the stock price changes. Many employers prefer to accelerate the accounting or avoid forward starts for this reason.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational derivative contract of which forward starts are a variant
- [Call Option](/call-option/) — the long payoff structure commonly used in forward starts
- [Strike Price](/strike-price/) — the barrier price, set at activation rather than at grant
- [Exercise Price](/exercise-price/) — synonymous with strike; locked at activation
- [In the Money](/in-the-money/) — forward starts are typically designed to be at-the-money at activation

### Wider context

- [Black Scholes Model](/black-scholes-model/) — standard pricing framework, adapted for forward starts
- [Vega](/vega/) — the Greek measuring sensitivity to volatility; especially important for forward-start pricing
- Equity Option — the asset class most common for forward starts
- [Derivatives Hedging](/derivatives-hedging/) — how forward starts are hedged by issuers
- Structured Products — investment vehicles that frequently use forward-start mechanics

</div>
