---
title: "Call Spread"
description: "A multi-leg options strategy combining a long call and short call to define risk and reward boundaries."
---

*A call spread is an options strategy where you simultaneously buy one call option and sell another call with the same expiration but a higher strike price. The combination limits both your maximum loss and maximum profit, making it a defined-risk trade.*

## The structure of a call spread

A call spread uses two call options on the same underlying and expiration date. You buy a call at a lower strike (say $100) and sell a call at a higher strike (say $110). Each leg reduces the net cost: the premium you pay for the long call is partially offset by the premium you collect from the short call. This net debit is your maximum loss.

The strategy caps your profit at the difference between the two strike prices minus the net premium paid. If the underlying settles above the higher strike at expiration, both calls are in-the-money, but the short call prevents you from capturing gains beyond $110. This trade-off—lower cost, lower reward—suits traders who expect moderate upside and want to reduce entry friction.

## When call spreads make sense

Call spreads are most attractive when implied volatility is high. Selling the upper call captures elevated premiums, bringing down the cost of the long call. Traders use them in mildly bullish conditions: you expect the price to rise, but not explosively. If you were highly bullish, you'd buy an uncapped call outright; if you were neutral, you'd avoid directional bets.

The strategy is also popular for income: sell wide call spreads on indexes or major stocks and collect the net premium as profit if the price stays below both strikes. Many professional traders run systematic call-spread programs on the S&P 500, rolling them weekly or monthly.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Call Spread — key facts</div>
  <table>
    <tr><th>Type</th><td>Multi-leg options strategy</td></tr>
    <tr><th>Legs</th><td>Long call + short call (same expiration, different strikes)</td></tr>
    <tr><th>Max loss</th><td>Net premium paid</td></tr>
    <tr><th>Max profit</th><td>Strike width minus net premium</td></tr>
    <tr><th>Typical use</th><td>Mildly bullish directional or income strategy</td></tr>
    <tr><th>Volatility preference</th><td>High implied volatility at entry</td></tr>
  </table>
</aside>

## The mechanics of profit and loss

Suppose the underlying is at $100. You pay $5 for a $100 call and sell the $110 call for $2, netting a $3 debit. Your maximum loss is $3 (if the stock falls and both calls expire worthless). Your maximum profit is $7 (the $10 spread minus the $3 you paid). Break-even is $103.

If the stock rallies to $108 at expiration, the $100 call is worth $8, the $110 call is worthless, and you keep your $2 credit, netting a $5 gain ($8 long minus $3 net paid). The profit curve is linear between the two strikes.

<div class="wiki-hatnote">For strategies that omit the short leg and cap upside differently, see <a href="/wiki/protective-put/">protective puts</a> (downside hedge) or <a href="/wiki/collar/">collars</a> (two-sided hedge).</div>

## Adjustments and roll-forwards

If the underlying moves against you—rallying past the short strike before expiration—your loss is capped. But if it rallies significantly, you may choose to close the position early to lock in the max loss and redeploy capital. Many traders roll the short call higher (sell a new short call, buy back the original) to extend the position and capture more premium.

The inverse strategy, a [put spread](/wiki/put-spread/), works identically but is bearish instead. Both are credit spreads when you sell the higher-strike option for more than you pay for the lower-strike option.

## When call spreads disappoint

If you underestimate volatility or the market crashes, the underlying can settle below the long strike, and you lose the full net debit with no profit. Call spreads also suffer when implied volatility collapses at expiration: you collect less premium than you paid to open the trade.

Transaction costs matter too. You pay commissions on all four sides (buy the call, sell the call, buy to close, sell to close at expiration). On small spreads, costs can consume 20–30% of the intended profit, so most professionals run call spreads on liquid underlyings like index options or near-the-money strikes where the spreads themselves are wide.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/put-spread/">Put spread</a> — the bearish mirror of a call spread.</li>
  <li><a href="/wiki/option/">Option</a> — foundational derivatives contract.</li>
  <li><a href="/wiki/call-option/">Call option</a> — the long leg of a call spread.</li>
  <li>Butterfly spread — another multi-leg defined-risk strategy.</li>
  <li><a href="/wiki/implied-volatility/">Implied volatility</a> — key input to spread premiums.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li>Derivatives — category overview.</li>
  <li><a href="/wiki/option-premium/">Option premium</a> — what you pay and collect on each leg.</li>
  <li><a href="/wiki/strike-price/">Strike price</a> — defines the boundary between profit and loss.</li>
</ul>
</div>
