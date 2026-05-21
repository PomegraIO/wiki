---
title: "Iron Butterfly"
description: "A four-leg option strategy combining a bull put spread and bear call spread with a shared center strike, designed for high-probability income in sideways markets."
---

*An iron butterfly sells a put and call at the same strike, buying farther-OTM puts and calls for protection. It's a tighter, more capital-efficient version of an [iron condor](/wiki/iron-condor/) when conviction in stagnation is very high.*

## What an iron butterfly is

An iron butterfly stacks four options at three strikes: buy a put far OTM, sell a put at the middle strike, sell a call at the middle strike, and buy a call far OTM. All expire the same month. You collect net credit from the two short options, offsetting the cost of the two long.

The payoff forms a sharp "butterfly" peak: maximum profit occurs when the stock closes exactly at the middle strike on expiration. Any move away from that strike reduces profit; moves beyond the long strikes hit maximum loss.

## Why to use an iron butterfly

The primary reason is **higher probability with lower capital efficiency**. An iron butterfly requires less capital than an [iron condor](/wiki/iron-condor/) because both spreads collapse at the same center strike. Win rates can reach 80–90% if you sell the center strike near the current price.

A second reason is **income concentration**. You collect premium from two short options at the same strike; the benefit of theta decay is front-loaded and concentrated.

Iron butterflies also appeal to **mechanical traders** who want high-probability, repeatable trades. Sell the market price, earn 1–2% per month, and redeploy—it's a formula.

## When an iron butterfly wins

Iron butterflies thrive in **extremely tight consolidation**. If the stock doesn't budge for a month, both the short put and call decay to zero and you keep the full credit—a clean, maximum-profit scenario.

They also excel when **implied volatility is elevated**. Fat premiums mean bigger credits; tight spreads (OTM puts and calls far from the money) have high probability of expiration worthless.

Iron butterflies work best when **you're willing to accept very narrow profit zones**. You're trading width for probability and capital efficiency.

## When an iron butterfly loses money

If the stock moves sharply away from the center strike, you hit maximum loss fast. A 10% move in a quiet stock can turn a winner into a loser. Iron butterflies punish directional moves harshly.

They also suffer from **implied volatility spikes**. If IV jumps after entry, both the long and short options gain value, but the longs (far OTM) can appreciate faster, narrowing your profit margin.

Gamma risk is severe near expiration. If the stock drifts toward one wing in the final week, a 1% move can swing the position 30–50%. You're forced to manage actively.

## Mechanics and adjustment

You typically collect $200–$400 net credit. Maximum profit is the credit received. Maximum loss is the width of either spread minus the credit—often $400–$600 per butterfly.

Return on risk is typically 30–50%, but requires active management. Many traders don't let iron butterflies run to expiration; they manage winners aggressively.

**Adjustment** is essential:
- **Closing the threatened side early**: If the stock moves toward one wing, close that spread at 50% max loss and keep the other profitable side.
- **Rolling both sides**: If breached, buy back the short at a loss and sell a new short further from the current price for the next month.
- **Converting to a condor**: If threatened, roll one wing further away, restructuring into a wider iron condor.

## Iron butterfly vs. iron condor

An iron butterfly has tighter, higher-probability payoffs but harsher gamma risk and lower payoff width. An iron condor is wider, lower-probability, but more forgiving of adverse moves. Choose iron butterflies for very quiet, range-bound markets; choose iron condors for normal volatility.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/iron-condor/">Iron Condor</a> — similar structure with wider spreads.</li>
<li><a href="/wiki/butterfly-spread/">Butterfly Spread</a> — call-only version of an iron butterfly.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits iron butterflies.</li>
<li><a href="/wiki/gamma/">Gamma</a> — acceleration risk near expiration.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects butterfly premiums.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying iron butterflies.</li>
<li><a href="/wiki/volatility-smile/">Volatility Smile</a> — affects pricing of far-OTM options.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for managing butterfly risk.</li>
</ul>
</div>
