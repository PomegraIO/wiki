---
title: "Long Put Ladder"
description: "A multi-leg option strategy that buys puts at multiple strikes, designed to profit from moderate declines while limiting cost through the sales of lower-strike puts."
---

*A long put ladder buys a higher-strike put and an at-the-money put, then sells a lower-strike put, combining [bear put spread](/wiki/bear-put-spread/) and ladder characteristics. It profits from downside moves while capping maximum loss.*

## What a long put ladder is

You buy a $110 put, buy a $100 put, and sell a $90 put—all same expiration. You typically pay a small net debit (the long puts cost more than the short put generates).

The payoff has multiple zones:
- Stock above $110: all puts expire worthless, you lose your debit.
- Stock $100–$110: the $110 put gains value, you profit.
- Stock $90–$100: both long puts gain value, profit continues.
- Stock below $90: the short $90 put caps maximum loss.

## Why to use a long put ladder

The primary reason is **cost-efficient bearish exposure**. Selling the $90 put generates premium, offsetting much of the cost of buying two puts.

A second reason is **flexible downside profit**. Unlike a simple [bear put spread](/wiki/bear-put-spread/), a ladder spans multiple strikes, capturing a wider profit zone.

Long put ladders also suit **bearish traders with limited capital**. The short put premium helps fund the position.

## When a long put ladder wins

Long put ladders thrive when the **stock declines modestly to a specific zone**. If you expect a 5–15% decline, a ladder capturing that zone is ideal.

They also work when **implied volatility is elevated**. The sale of the $90 put generates fat premium, offsetting much of your cost.

Ladders profit from **time decay and directional declines**, making them more forgiving than naked puts.

## When a long put ladder loses money

If the stock rallies, all three puts expire worthless and you lose your debit paid.

Ladders also suffer if the **stock declines sharply below your short put strike**. Downside is capped at a loss, and you miss further gains from the crash.

If **implied volatility collapses**, the long puts you bought lose value faster than the short put you sold appreciates—net loss.

## Mechanics and adjustment

You typically pay a small net debit—$50–$200. Maximum profit is `($110 strike – $90 strike) – (net debit)`, typically $15–$20 per share. Maximum loss is `($100 strike – $90 strike) – (net debit)` if the stock falls below the short put strike.

Break-even is the $110 strike minus the debit paid per share.

**Adjustment** is optional:
- **Rolling the short strike down**: If the stock declines and breaks through your short put, buy it back and sell a lower-strike put for a later month.
- **Closing early**: If the stock hits your profit zone, close and redeploy.

## Long put ladder vs. bear put spread

A bear put spread uses two strikes and caps profit at the width of those strikes. A long put ladder uses three strikes, offering more flexibility. Choose spreads for simplicity; choose ladders for nuanced bearish positions.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/bear-put-spread/">Bear Put Spread</a> — a simpler two-leg alternative.</li>
<li><a href="/wiki/put-option/">Put Option</a> — the contract type underlying ladders.</li>
<li><a href="/wiki/butterfly-spread/">Butterfly Spread</a> — similar three-strike structure.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits ladders.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects entry cost and payoff.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying ladders.</li>
<li><a href="/wiki/strike-price/">Strike Price</a> — defines the ladder's structure.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring ladder risk.</li>
</ul>
</div>
