---
title: "Put Ratio Spread"
description: "An advanced option strategy that buys one put and sells multiple puts at a lower strike, generating credit while exposing traders to naked short-put risk below the short puts."
---

*A put ratio spread buys a put and sells two or more puts at a lower strike, creating a net credit. It profits from stagnation and time decay but carries unlimited loss risk below the short puts.*

## What a put ratio spread is

A standard put ratio (typically 1x2) buys one higher-strike put and sells two lower-strike puts, all the same expiration. If structured correctly, the credit from the two short puts partially or fully offsets the cost of the long put.

The payoff has three zones: above the short puts (small loss), between short and long puts (profit), and below the short puts (escalating loss—theoretically unlimited).

## Why to use a put ratio spread

The primary reason is **enhanced credit collection with cost control**. Selling two puts generates substantial income; buying one put reduces max loss if the stock crashes through both short strikes.

A second reason is **cheap bullish entry**. If the credit from selling two puts exceeds the cost of the long put, the position is free—you own downside protection for nothing.

Put ratio spreads also suit **stocks after sharp declines**. If a stock has fallen 30% and you expect consolidation, selling two puts below the current price while owning a protective put below those creates income while capping loss.

## When a put ratio spread wins

Put ratio spreads thrive when the **stock stays near or above the short put strikes**. All three puts expire worthless (or with minimal value) and you keep the credit—maximum profit.

They also excel when **implied volatility contracts after entry**. The short puts lose value faster than the long put, tightening the spread and locking in profit.

Put ratio spreads work well when you're **bullish or neutral, confident in a downside floor**. If you believe the stock won't drop below $80, selling two $80 puts and owning one $70 put generates income while managing tail risk.

## When a put ratio spread loses money

If the stock crashes below the short puts, you're exposed to escalating losses. You're naked short one put—your losses grow dollar-for-dollar as the stock declines further.

Put ratio spreads also suffer from **implied volatility spikes**. A sharp IV increase widens spreads and can turn a winning position into a loss, especially if the stock moves sharply downward.

Time decay hurts early in the spread's life. You're long one put, short two; theta works in your favor on the short puts but against you on the long put (which is less exposed to time decay early on). The math is asymmetric against you initially.

## Mechanics and adjustment

You typically receive a net credit—$200–$500 for a 1x2 ratio. Maximum profit is the credit received (if the stock stays above both short puts). Maximum loss is `(short put strike – long put strike – credit received)` at the long put strike, and escalates below it.

Break-even below the short strike is the short strike minus the credit received per share; you lose $1 for every $1 the stock falls below that point.

**Adjustment** is essential:
- **Buying back the shorts early**: If the stock approaches the short put strikes, close the short puts to prevent naked exposure.
- **Rolling the shorts lower**: If the stock declines, buy back the short puts at a loss and sell new ones lower.
- **Closing the entire spread**: If losses mount, exit all legs to cut exposure.

## Put ratio spread risk

This strategy carries **naked short-put risk** below the short strike. A sharply declining stock forces the short puts deep ITM, creating substantial losses. Most brokers restrict this to advanced accounts.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/call-ratio-spread/">Call Ratio Spread</a> — the call equivalent using calls.</li>
<li><a href="/wiki/bull-put-spread/">Bull Put Spread</a> — a safer two-leg alternative.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits these spreads.</li>
<li><a href="/wiki/put-option/">Put Option</a> — the contract type underlying ratio spreads.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects spread credit and payoff.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying spreads.</li>
<li><a href="/wiki/naked-short/">Naked Short</a> — the risk component below the short puts.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring ratio spread risk.</li>
</ul>
</div>
