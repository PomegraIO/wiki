---
title: "Time Spread"
description: "An options strategy that buys and sells options at the same strike but different expirations to profit from time decay differences."
---

*A time spread (also called calendar spread) sells a near-term option and buys a longer-term option at the same strike, profiting when time decay shrinks the short option faster than the long option.*

## The mechanics of time spreads

A time spread is often called a **calendar spread** and pairs a short near-term option with a long longer-term option. Both use the same strike and underlying, but different expirations.

For example: sell a 30-day call at the $100 strike for $2, and buy a 90-day call at the $100 strike for $4. You pay a $2 net debit. As time passes, the 30-day call loses value faster (theta decay accelerates as expiration approaches) while the 90-day call loses value more slowly. If both remain at-the-money, the spread widens and you gain profit.

The position's P&L depends on both time decay (theta) and price movement. If the underlying moves sharply, the short option's delta changes faster than the long option's, creating gamma risk. If the underlying stays near the strike, time decay works entirely in your favor.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Time Spread — key facts</div>
  <table>
    <tr><th>Type</th><td>Time decay-focused strategy</td></tr>
    <tr><th>Legs</th><td>Short near-term + long far-term (same strike)</td></tr>
    <tr><th>Max loss</th><td>Net debit paid (if held to expiration)</td></tr>
    <tr><th>Max profit</th><td>Modest, typically smaller than net debit</td></tr>
    <tr><th>Time decay</th><td>Beneficial; more profit in quiet markets</td></tr>
    <tr><th>Typical use</th><td>Neutral outlook; harvesting theta for income</td></tr>
  </table>
</aside>

## Why traders use time spreads

Time spreads are ideal for traders who expect low volatility or range-bound trading. You're betting that the underlying stays near the strike as time passes. The market rewards you with theta decay differential.

They're also used by income-focused traders. Unlike [covered calls](/wiki/covered-call/), which require owning stock, time spreads use only options. You can run them on stocks you don't hold, making them flexible for directional and volatility views.

Professionals often roll time spreads forward: when the short option expires, they sell another short-term option at the same or adjusted strike, creating a recurring theta harvest.

## Rolling and adjustments

When the short option approaches expiration, you can:

1. **Let it expire**: Close the position and book profit or loss.
2. **Roll forward**: Buy back the short call, sell a new short call at a further expiration. This extends the theta harvest.
3. **Roll up and forward**: Sell a new short call at a higher strike, collecting more premium if implied volatility rises.
4. **Adjust if needed**: If the underlying moves sharply, close the entire position to prevent losses from expanding gamma.

Rolling is how professionals turn time spreads into recurring income streams. A systematic time spread trader might roll every month, harvesting 0.5–1% premium per month on the same stock.

<div class="wiki-hatnote">See <a href="/wiki/calendar-spread/">calendar spreads</a> for the detailed treatment of this strategy's variants.</div>

## Greeks and sensitivities

A long time spread is:

- **Long [vega](/wiki/vega/)**: If implied volatility rises, the longer-term option gains more than the shorter-term option loses, so you profit.
- **Long [theta](/wiki/theta/)**: Time decay is your friend; every day that passes in quiet markets, you gain money.
- **Short [gamma](/wiki/gamma/)**: If the underlying moves significantly, the short option's delta increases faster than the long option's, creating losses. This is the cost of collecting theta.

The position is most profitable when implied volatility is high (you collect a premium), and the market is quiet (you harvest theta without gamma losses).

## Compared to calendar spreads

This entry uses "time spread" and "calendar spread" interchangeably. Both refer to the same strategy: different expirations, same strike. Some traders distinguish by saying "calendar spread" is the general concept and "time spread" emphasizes the time decay focus, but the structures are identical.

A **diagonal spread** adds a second difference: different expirations AND different strikes, creating a more flexible but more complex position.

## When time spreads don't work

Time spreads fail when implied volatility collapses. You enter collecting elevated premiums, expecting calm markets. Then market stress hits, implied volatility spikes, both options lose value, but the short option (closer to expiration) loses proportionally more. Your intended profit vanishes.

They also fail if the underlying gaps sharply. A gap removes the time decay benefit; the short option can move in-the-money or far out-of-the-money in seconds, and gamma losses can exceed accumulated theta gains.

Transaction costs matter too. Buying the long option and selling the short option costs commissions on both sides. Closing the position and rolling forward compounds costs. On small spreads (narrow strikes, low premiums), total costs can exceed 30% of intended profit.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/calendar-spread/">Calendar spread</a> — the foundational version of this strategy.</li>
  <li><a href="/wiki/diagonal-spread/">Diagonal spread</a> — uses different strikes too.</li>
  <li><a href="/wiki/theta/">Theta</a> — the profit driver of time spreads.</li>
  <li><a href="/wiki/gamma/">Gamma</a> — the risk when prices move.</li>
  <li><a href="/wiki/implied-volatility/">Implied volatility</a> — affects premium collected.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational contract.</li>
  <li>Derivatives — asset class overview.</li>
  <li><a href="/wiki/expiration-date/">Expiration date</a> — defines the spread expirations.</li>
</ul>
</div>
