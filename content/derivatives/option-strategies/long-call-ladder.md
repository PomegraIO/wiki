---
title: "Long Call Ladder"
description: "A multi-leg option strategy that buys calls at multiple strikes, designed to profit from moderate moves while limiting cost through the sales of higher-strike calls."
---

*A long call ladder buys a lower-strike call and an at-the-money call, then sells a higher-strike call, combining bull-call-spread and ladder payoff characteristics. It profits from modest upside while capping maximum loss.*

## What a long call ladder is

You buy a $90 call, buy a $100 call, and sell a $110 call—all same expiration. You typically pay a net small debit (the $90 and $100 calls cost more than the $110 call generates).

The payoff has multiple zones:
- Stock below $90: all three expire worthless, you lose your debit.
- Stock $90–$100: the $90 call gains value, you profit to the $100 strike.
- Stock $100–$110: the $90 and $100 calls gain value, profit continues.
- Stock above $110: the short $110 call caps profit.

## Why to use a long call ladder

The primary reason is **enhanced profit zone with limited cost**. By selling the $110 call, you offset the cost of buying two calls, reducing your entry debit.

A second reason is **flexible profit if the stock moves moderately**. Unlike a simple [bull call spread](/wiki/bull-call-spread/) capped at one level, a ladder has a wider profit zone.

Long call ladders also suit **bullish traders with limited capital**. The sale of the high-strike call partially funds the position.

## When a long call ladder wins

Long call ladders thrive when the **stock moves modestly to a specific zone**. If you expect the stock to rally 5–15%, a ladder capturing that zone is ideal.

They also work when **implied volatility is elevated**. The sale of the $110 call generates fat premium, offsetting much of your cost.

Ladders profit from both **time decay and directional moves**, making them more forgiving than naked calls.

## When a long call ladder loses money

If the stock doesn't move, all three calls expire worthless and you lose your debit paid.

Ladders also suffer if the **stock rallies beyond your short call strike**. Upside is capped, and you miss further gains.

If **implied volatility collapses**, the long calls you bought lose value faster than the short call you sold appreciates—net loss.

## Mechanics and adjustment

You typically pay a small net debit—$50–$200. Maximum profit is `($110 strike – $90 strike) – (net debit)`, typically $15–$20 per share. Maximum loss is the debit paid.

Break-even is the $90 strike plus the debit paid per share.

**Adjustment** is optional:
- **Rolling the short strike up**: If the stock rallies and breaks through your short call, buy it back and sell a higher-strike call for a later month.
- **Closing early**: If the stock hits your profit zone, close the position and redeploy.

## Long call ladder vs. bull call spread

A bull call spread uses two strikes and caps profit at the width of those strikes. A long call ladder uses three strikes, offering more flexibility. Choose spreads for simplicity; choose ladders for nuanced bull positions.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/bull-call-spread/">Bull Call Spread</a> — a simpler two-leg alternative.</li>
<li><a href="/wiki/call-option/">Call Option</a> — the contract type underlying ladders.</li>
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
