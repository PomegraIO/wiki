---
title: "Jump Spread"
description: "A vertical spread strategy with wider-than-normal strike spacing, designed to reduce entry cost and increase profit potential at the expense of higher break-even requirements."
---

*A jump spread widens the distance between long and short strikes to 5–10+ points (vs. the typical 1–2 points in standard spreads). Wider spacing means lower entry cost but requires a larger move to profit.*

## What a jump spread is

Instead of a typical [bull call spread](/wiki/bull-call-spread/) using $100 and $105 strikes (5-point width), a jump spread might use $100 and $110 strikes (10-point width). The higher strike is further OTM, generating less short-call credit. Your net entry debit is lower, but you need a 10% move to capture full profit instead of 5%.

Jump spreads can use calls (bull or bear) or puts (bull or bear).

## Why to use a jump spread

The primary reason is **low entry cost**. For traders with minimal capital, a jump spread requires paying far less upfront than a standard spread.

A second reason is **capital efficiency on directional conviction**. If you're confident in a 15% rally, a jump spread with a 15-point width is ideal—cheaper entry, and the move justifies the width.

Jump spreads also appeal to **traders who want leverage**. You're betting a big move will happen; if it does, your capital is efficiently deployed.

## When a jump spread wins

Jump spreads thrive when the **stock makes large, swift moves in your expected direction**. The wider strike spacing is irrelevant if the stock gaps 15% overnight—you're maximally profitable.

They also work in **high implied volatility environments**. Fat option premiums mean even the far-OTM short option generates meaningful credit.

Jump spreads are ideal for **event-driven bets**: earnings, merger announcements, FDA decisions. You expect a big move; the wider spacing reduces cost and aligns with your conviction.

## When a jump spread loses money

If the stock doesn't move far enough to breach the long strike, you lose the full debit paid—even if it moves 5% in your direction.

Jump spreads also suffer from **implied volatility spikes favoring the short**. If IV explodes, the short strike (further OTM) remains safe, but your long option doesn't gain as much value as it would in a tighter spread.

Time decay is your enemy with jump spreads. You need a big move soon; if the stock stalls, time erodes value faster than in tighter spreads because the long option is further OTM.

## Mechanics and adjustment

Entry cost is lower—$50–$150 for a 10-point jump spread vs. $200–$300 for a standard spread.

Maximum loss is the debit paid. Maximum profit is `(width of spread) – (debit paid)`. For a 10-point spread costing $100, your max profit is $900 (a 9:1 return on capital—attractive if the stock moves).

Break-even is the long strike plus the debit paid.

**Adjustment** is rare. Jump spreads are binary: the stock either makes the big move or doesn't. If it doesn't, exiting early at a loss is often better than holding.

## Jump spread vs. standard spread

A standard spread has tighter strikes, easier break-evens, but higher cost. A jump spread has lower cost, harder break-evens, but better payoff if the big move happens. Choose standard spreads for moderate moves; choose jump spreads for conviction in large moves.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/bull-call-spread/">Bull Call Spread</a> — the standard variant with tighter spacing.</li>
<li><a href="/wiki/bear-call-spread/">Bear Call Spread</a> — bearish jump spread variant.</li>
<li><a href="/wiki/vertical-spread/">Vertical Spread</a> — the general class of spreads.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects jump spread cost and payoff.</li>
<li><a href="/wiki/strike-price/">Strike Price</a> — the wide spacing defines jumps.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying jump spreads.</li>
<li>Leverage — the key appeal of jump spreads.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring jump spread risk.</li>
</ul>
</div>
