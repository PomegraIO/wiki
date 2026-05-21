---
title: "Call Ratio Spread"
description: "An advanced option strategy that buys one call and sells multiple calls at a higher strike, designed to enhance returns in sideways markets but with unlimited loss risk above the short calls."
---

*A call ratio spread buys a call and sells two or more calls at a higher strike, creating a net credit if structured properly. It profits from stagnation and time decay but exposes traders to naked short-call risk beyond the short strike.*

## What a call ratio spread is

A standard call ratio (typically 1x2) buys one lower-strike call and sells two higher-strike calls, all the same expiration. The two short calls may or may not fully offset the cost of the long call, depending on strike spacing and implied volatility.

The payoff has three zones: below the long call (small loss), between long and short strikes (profit), and above the short strikes (escalating loss—capped at the profit taken if you manage early, but theoretically unlimited if you don't).

## Why to use a call ratio spread

The primary reason is **enhanced income in sideways markets**. Selling two calls generates substantial premium; one long call provides partial protection. It's a way to amplify credit-collection strategies.

A second reason is **cheap or free entry**. If the two short calls generate enough premium, the position is free—you own a call for nothing. The upside is capped by the short calls, but you're long with no cost.

Call ratio spreads also suit **range-bound consolidation**. If you're confident the stock won't break above a certain level, selling two calls above that ceiling while owning a call below it can generate 1–3% monthly returns.

## When a call ratio spread wins

Call ratio spreads thrive when **the stock consolidates tight**. If the stock doesn't move, all three calls decay to zero (if OTM) and you keep the credit. Maximum profit occurs when the stock closes between the long and short strikes on expiration.

They also excel when **implied volatility expands at entry then contracts**. The short calls shrink in value faster than the long call, tightening the spread and locking in profit.

Call ratio spreads work well when you're **confident in an upside ceiling**. If you own a stock and expect it to rally to $110 but not $120, selling two $120 calls and owning one $110 call provides income while capping risk.

## When a call ratio spread loses money

If the stock rallies above the short strikes, you're exposed to escalating losses. Unlike a vertical spread where losses cap at the strike width, a call ratio spread's losses can grow indefinitely—you're naked short one call.

Call ratio spreads also suffer from **implied volatility spikes**. A sharp IV increase can widen the spread and turn a winning position into a loss, especially if the stock moves near one of your strike levels.

Time decay works against you early in the spread's life. You're long one call and short two; theta decay accelerates on the shorts, but asymmetrically—you're losing money every day the stock consolidates early on.

## Mechanics and adjustment

You typically receive a net credit—$100–$400 for a 1x2 ratio. Maximum profit is theoretically the credit received. Maximum loss is `(short call strike – long call strike – credit received)` if the stock stays at the short strike, and unlimited above.

Break-even above the short strike is the short strike plus the credit received per share; you lose $1 for every $1 the stock rallies above that point.

**Adjustment** is critical:
- **Buying back the shorts early**: If the stock approaches the short strike, close the short calls to prevent naked exposure.
- **Rolling the shorts higher**: If the stock rallies, buy back the short calls at a loss and sell new ones higher.
- **Closing the entire spread**: If the trade isn't working, exit all legs to cut losses.

## Call ratio spread risk

This strategy carries **naked short-call risk** above the short strike. Many brokers require significant margin or restrict this trade to advanced accounts. Understand your broker's requirements before deploying a call ratio spread.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/put-ratio-spread/">Put Ratio Spread</a> — the put equivalent using puts.</li>
<li><a href="/wiki/bull-call-spread/">Bull Call Spread</a> — a safer two-leg alternative.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits these spreads.</li>
<li><a href="/wiki/call-option/">Call Option</a> — the contract type underlying ratio spreads.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects spread credit and payoff.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — the contract type.</li>
<li><a href="/wiki/naked-short/">Naked Short</a> — the risk component above the short strikes.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring ratio spread risk.</li>
</ul>
</div>
