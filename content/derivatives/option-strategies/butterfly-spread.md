---
title: "Butterfly Spread"
description: "A limited-risk option strategy using three different strikes, designed to profit from minimal price movement and high time decay."
---

*A butterfly spread pairs two spreads (a bull and bear) at overlapping strikes, creating a narrow profit zone near the middle strike. It's ideal for traders expecting stagnation with defined risk and profit.*

## What a butterfly spread is

A butterfly spread typically uses four options: buy a call at the lower strike, sell two calls at the middle strike, and buy a call at the higher strike (all same expiration). You pay a net debit or receive a net credit, depending on pricing.

The payoff forms a triangle or "butterfly" shape: maximum profit occurs if the stock closes exactly at the middle strike on expiration. Profit zones are narrow; maximum loss is the debit paid or the strike width minus credit received.

Butterfly spreads can be built with puts, or mixed (put butterfly), but call butterflies are most common.

## Why to use a butterfly spread

The primary reason is **low cost with defined risk**. Butterflies are cheap to enter—often $25–$100 debit—because the two short options offset the cost of the two longs. You can take 10 butterfly positions for the cost of one naked call.

A second reason is **high probability of profit**. The middle strike creates a wide profit zone at expiration. If you sell the middle strike near the current stock price, the stock has a large safe range.

Butterflies also appeal to **mechanical traders** and **portfolio overlay strategies**. You can deploy them in volume, manage by defined rules, and generate steady income from time decay in a range-bound market.

## When a butterfly wins

Butterflies thrive in **extremely tight consolidation**. If the stock doesn't budge for a month, time decay accelerates and both your short calls decay faster than your long calls, locking in profit.

They also excel in **high implied volatility that then contracts**. If IV drops, the middle strikes lose value faster, narrowing the gap between long and short. Your profit is locked in early.

Butterflies work best when **you have no edge on direction**. You're genuinely neutral and want to profit from passage of time and mean reversion to the middle strike.

## When a butterfly loses money

If the stock moves sharply away from the middle strike, you hit maximum loss. The stock closing at either extreme (both outer strikes) produces the worst payoff. A 10% move in a quiet stock can turn a winner into a loser.

Butterflies also suffer from **implied volatility spikes**. If IV explodes after entry, both long and short options gain value, but the longs (far from the money) appreciate faster than the shorts. Your profit margin shrinks.

Gamma risk is severe near expiration. As the stock approaches an outer strike, a 1% move can swing the position significantly. You're forced to manage actively in the final week or accept volatile swings.

## Mechanics and adjustment

You typically pay a small debit to enter—$25–$150. Maximum profit is `(middle strike – lower strike) – (debit paid)`, usually $100–$200 per spread. Maximum loss is the debit paid.

Break-even points are at the lower strike plus the debit, and the upper strike minus the debit. If you paid $50 for strikes at 95/100/105, your break-evens are 95.50 and 104.50—a 9% move in either direction hits max loss.

**Adjustment** is common if the stock drifts toward one wing:
- **Rolling the outer strike**: Buy back the outer call, sell one further out, regenerating the wings.
- **Converting to a strangle**: Close the outer call, keep the debit-spread core.
- **Taking profit early**: Close the spread at 50–75% of max profit and redeploy.

## Butterfly vs. simple bull/bear spread

A bull call spread profits from a 20% move and caps both risk and profit. A butterfly profits only from 0–5% moves and offers much tighter payoff. Choose spreads for directional conviction; butterflies for high confidence in stagnation.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/iron-butterfly/">Iron Butterfly</a> — put-and-call variant of a butterfly.</li>
<li><a href="/wiki/call-option/">Call Option</a> — legs of a call butterfly.</li>
<li><a href="/wiki/bull-call-spread/">Bull Call Spread</a> — one half of a butterfly structure.</li>
<li><a href="/wiki/bear-call-spread/">Bear Call Spread</a> — the other half of a butterfly structure.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits butterflies.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying butterflies.</li>
<li><a href="/wiki/gamma/">Gamma</a> — acceleration risk near expiration.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring butterfly risk.</li>
</ul>
</div>
