---
title: "Option Pin Risk at Expiration"
description: "Option pin risk occurs when the underlying closes near a strike at expiration, creating uncertainty about assignment and leaving position managers unable to act decisively."
keywords:
  - option pin risk
  - pin risk expiration
  - strike price at expiration
  - option assignment uncertainty
  - short option assignment risk
  - expiration week trading
---

*When an underlying stock closes near the strike price of an expiring option, both option holders and short sellers face a problem: nobody knows whether [exercise](/option/) will happen. **Option pin risk** describes this uncertainty and the trading restrictions it creates in the final hours before expiration.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Pin Risk — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">When expiration meets ambiguity, hedges and positions become unmanageable.</div>

|   |   |
|---|---|
| **What it is** | Uncertainty about [option assignment](/option/) when the underlying trades within one [strike](/strike-price/) of expiration |
| **When it appears** | Last trading day or hour before [expiration](/expiration-date/) |
| **Who feels it** | Short call/put holders (fear forced exercise); long holders (unsure whether to sell or hold) |
| **Main risk** | Sudden whipsaw if stock moves decisively after you've locked in your position |
| **Mitigation** | Close or roll positions before expiration week; avoid holding short options near-the-money |

</aside>

## Why Pin Risk Exists

At [expiration](/expiration-date/), an [option](/option/) either will or will not be exercised. That decision depends entirely on whether the underlying finishes in-the-money or out-of-the-money. But in the hours before expiration, no one knows the final closing price—and that uncertainty is the root of pin risk.

If you are short a call, and the stock is trading exactly at or just below the [strike price](/strike-price/), you have no idea whether you will be forced to deliver shares at expiration. If you are long a call in the same spot, you cannot decide whether to exercise, sell the option for its remaining [time value](/time-value/), or let it expire worthless. The closer the stock trades to the strike, the more acute the paralysis becomes.

This is called "pinning" because the stock appears to cluster at or very near the strike price as expiration nears—as if pinned there by the options market itself.

## The Mechanics of Assignment

To understand why pin risk matters, you need to know how assignment works. When an option is exercised, the [clearing house](/counterparty-risk/) steps in and randomly assigns the exercise notice to short holders. If you sold a call at 50 and the stock closes at 50.50, the call is in-the-money by 50 cents, but whether *your* short call is assigned is a lottery. You might owe 100 shares, or you might walk away free.

Short put holders face the same ambiguity. A stock trading at 49.99 when you sold the 50 put could be assigned instantly, or could snap back to 51.00 and you escape.

Long holders confront a different problem: should I exercise now and lock in my profit, sell the option and pocket whatever time value remains, or hold and hope for a bigger move? That hesitation costs real money if the stock jumps $2 or $3 in the final minutes.

## Real-World Consequences

Pin risk becomes costly for four reasons:

**Hedge blindness.** If you sold a call as a covered hedge against a stock you own, but you do not know whether the call will be assigned, you cannot finalize your hedge math. Your effective short position is undefined.

**Rollover gridlock.** Traders wanting to roll an expiring short call to the next month find that the stock's position near the strike makes it pointless to close the current call and open the new one simultaneously. Both might move together, wasting commissions.

**Cash management failure.** Short put sellers who do not know whether they will be assigned cannot tell their accounting systems whether to reserve cash for a stock purchase or mark the position as closed.

**Gamma traps.** As expiration approaches, [gamma](/gamma/) explodes near the strike. A $0.20 move can flip an option from $0.05 to $0.25 [intrinsic value](/intrinsic-value/). If you are short and caught flat-footed, the gap move bankrupts you.

## How Market Makers Exploit Pin Risk

[Market makers](/market-maker-trading/) and sophisticated traders weaponize pin risk. If a stock drifts to exactly the strike of a widely-held short call or short put position, big institutions can suddenly buy or sell the stock in size, triggering a whipsaw that extracts profits from trapped retail traders. A coordinated push above or below the strike in the final seconds can force a wave of assignments or expirations, creating the illusion of gamma-driven "pinning."

Retail traders holding short positions near expiration are most vulnerable because they usually cannot rebalance fast enough.

## Strategies to Avoid or Manage Pin Risk

**Close early.** The most reliable defense is to exit short options before expiration week. A short call that is in-the-money with one or two weeks left still carries a few cents of time value; selling it then avoids the expiration-day lottery entirely.

**Roll forward.** Instead of closing, roll the short call or put to the next month. This keeps you long-volatility and short-delta, but eliminates the binary assignment outcome.

**Use alerts.** Set a price alert at the strike price. If the stock is trading within $0.20 of your strike on the last trading day, close the position or roll it immediately.

**Accept assignment.** If you have sold a covered call and the stock is in-the-money at expiration, assignment is often the intended outcome. Fight it only if the stock's momentum suggests a post-expiration pop that would have let you keep your shares.

**Avoid selling puts near support.** Put sellers should avoid strikes that align with key support levels or round numbers, where stocks often hold or bounce. The temptation to sell a 50-strike put is high, but so is the likelihood of a pin-risk trap.

## Pin Risk and Volatility Surface Effects

As expiration nears, the [volatility smile](/volatility-smile/) flattens and then inverts near the strike. This means a stock trading exactly at the strike has nearly identical implied volatility whether the stock is 1% up or 1% down. That makes options near the strike appear cheaper than they are, and traps sellers.

Conversely, deep in-the-money or out-of-the-money options do not suffer pin risk, because exercise is nearly certain or certain not to happen.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the contract whose assignment creates pin risk
- [Strike Price](/strike-price/) — the level where pin risk clusters
- [Expiration Date](/expiration-date/) — the moment when risk resolves
- [Intrinsic Value](/intrinsic-value/) — what determines whether exercise is profitable
- [Time Value](/time-value/) — what vanishes as expiration approaches
- [Gamma](/gamma/) — the acceleration of delta that makes pin-risk moves violent
- [Covered Call](/covered-call/) — the hedging strategy most exposed to pin risk
- [Protective Put](/protective-put/) — the defense strategy confused by pin risk

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — why options are used for risk management
- [Market Maker Trading](/market-maker-trading/) — who profits from option trader paralysis
- [Call Option](/call-option/) — the instrument that creates upside pin risk
- [Put Option](/put-option/) — the instrument that creates downside pin risk
- [Execution Risk](/execution-risk/) — how indecision costs money
- [Volatility Smile](/volatility-smile/) — why options near the strike trade differently

</div>
