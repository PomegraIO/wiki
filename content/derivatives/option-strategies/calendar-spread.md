---
title: "Calendar Spread"
description: "An option strategy that profits from time decay and volatility expansion by selling a near-term option and buying a longer-dated one at the same strike."
---

*A calendar spread pairs options at the same strike but different expirations, profiting when the near-term option decays faster than the long-term option. It's ideal for traders expecting stagnation with a later volatility catalyst.*

## What a calendar spread is

A calendar spread (also called a time spread or diagonal spread) sells an option (call or put) at one expiration and simultaneously buys the same type of option at a later expiration, both at the same or very similar strikes. You pay a net debit: the long option costs more than the short one generates.

The payoff is unique: you profit as the short-term option decays faster than the long-term option shrinks. If the stock stays near the strike, the short option expires worthless while your long option retains value, which you can close or roll into a new short.

## Why to use a calendar spread

The primary reason is **exploiting theta decay asymmetry**. Time decay accelerates exponentially as expiration approaches. An option decays 10% in the first 50 days, then 40% in the final 10 days. By selling the near-term and owning the long-term, you pocket the accelerated decay.

A second reason is **low directional risk**. Calendar spreads are theta-positive and relatively delta-neutral. You're not betting on direction; you're betting on stagnation and time passage.

Calendar spreads also suit **anticipated catalysts**. Sell the near-term option before earnings, own a longer-dated option that captures post-earnings volatility expansion. If the stock moves after near-term expiration, your long option is still valuable.

## When a calendar spread wins

Calendar spreads thrive when the **stock stays near the strike**. Each day of stagnation, your short decays faster than your long. Maximum profit occurs at the short's expiration with the stock at the strike price.

They also profit when **implied volatility expands**. If you enter at 15% IV and IV rises to 25%, your long option gains value faster than your short option loses. Even if the stock moves moderately, IV expansion offsets the directional loss.

The strategy is ideal for **consolidation before a known event**. Sell near-term while awaiting earnings or Fed decisions; own longer-dated to capture post-event moves.

## When a calendar spread loses money

If the stock moves sharply away from the strike, both options decline, but the short decays to zero while your long still has value. You can be hurt by an early move in the "wrong" direction.

Calendar spreads also suffer from **implied volatility collapse**. If IV contracts sharply (especially if the stock stays near the strike), both options shrink in value. Your short decays to zero, and your long drops 20–30%. Net loss.

The strategy also requires **active management**. When the near-term expires, you must decide: close the remaining long, or sell a new near-term option against it. Each decision resets the position.

## Mechanics and adjustment

You typically pay a small debit to enter—$100–$300 per spread. Maximum profit is the debit paid (achieved when the stock closes at the strike on short expiration). Maximum loss is theoretically large if the stock moves far away, but capped if you manage position size and close losing near-term legs.

**Adjustment** is routine:
- **Rolling the short forward**: When the near-term expires, immediately sell a new short one month out at the same strike. Repeat monthly.
- **Adjusting the strike**: If the stock has moved, sell the short at a new strike closer to the current price.
- **Closing at profit**: If the near-term is at 50% max loss and you've already realized 50% gain, close the position and redeploy.

## Calendar spread vs. diagonal spread

A diagonal spread shifts strikes between expirations (long a lower call, short a higher one, different expirations). This adds directional bias. A pure calendar keeps strikes the same. Diagonals are harder to manage but offer directional flexibility; calendars are mechanically simpler.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits calendar spreads.</li>
<li><a href="/wiki/vega/">Vega</a> — volatility sensitivity of calendar spreads.</li>
<li><a href="/wiki/call-option/">Call Option</a> — the legs of a call calendar.</li>
<li><a href="/wiki/put-option/">Put Option</a> — the legs of a put calendar.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects calendar spread payoff.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying calendars.</li>
<li><a href="/wiki/expiration-date/">Expiration Date</a> — defines calendar structure.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for managing calendar risk.</li>
</ul>
</div>
