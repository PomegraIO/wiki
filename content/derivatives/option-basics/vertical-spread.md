---
title: "Vertical Spread"
description: "An option strategy of buying one option and selling another at different strikes but same expiration, limiting both risk and reward."
---

*A vertical spread combines two options of the same type (both calls or both puts) at different [strike prices](/wiki/strike-price/) and the same [expiration date](/wiki/expiration-date/). The name comes from the vertical arrangement of strikes on an [option chain](/wiki/option-chain/). By pairing a long option with a short option, you cap both max profit and max loss, making vertical spreads popular for traders who want defined-risk positions.*

<aside class="wiki-infobox">
<div class="wiki-infobox-title">Vertical Spread — key facts</div>
<table>
<tr><th>Types</th><td>Bull call, bear call, bull put, bear put</td></tr>
<tr><th>Max gain</th><td>Fixed (difference between strikes minus net premium)</td></tr>
<tr><th>Max loss</th><td>Fixed (net premium paid for long leg)</td></tr>
<tr><th>Complexity</th><td>Two commissions, margin, assignment risk</td></tr>
</table>
</aside>

## Bull call spreads: bullish with defined risk

Buy a [call option](/wiki/call-option/) at a lower strike and sell a call at a higher strike. You're bullish on the stock but willing to cap your upside in exchange for lower net cost. Example: buy a $95 call for $5, sell a $100 call for $2, net cost $3. Max profit is $5 − $3 = $2 per share ($200 total). Max loss is the $3 net cost. The short call's premium offsets the long call's cost, making this cheaper than buying a call outright but also capping the gain.

## Bear call spreads: bearish income play

Reverse the structure: sell a call at a lower strike, buy a call at a higher strike. You're bearish and collect net premium upfront. If the stock stays below the short strike, you keep the full premium. The long call caps your loss if the stock rallies unexpectedly. This is a common income strategy for investors who believe a stock will decline or trade sideways.

## Bull put and bear put spreads

Put spreads follow the same logic but with puts. A bull put spread sells a put at a higher strike and buys a put at a lower strike—you're bullish and generating income, with defined max loss. A bear put spread buys a put at a higher strike and sells a put at a lower strike—you're bearish on the stock and on volatility, betting the stock will fall more than the market is pricing in.

## Why traders love defined risk

Vertical spreads appeal to disciplined traders because risk and reward are locked in from inception. You always know the worst-case loss before entering the trade. This makes position sizing and portfolio risk management much cleaner than unlimited-risk naked options. For brokers, spreads require less margin than naked short calls, encouraging their use.

## Assignment complexity and multi-legged mechanics

If your short call is assigned, you're forced to deliver shares or cover it in the market. If you're holding the long call, that assignment happens independently—there's no automatic pairing. You could be assigned on the short call at $95 and still own the long $100 call that expires worthless days later. Professional traders track assignment risk carefully and adjust spreads as expiration nears.

## Greeks and the spread's behavior

The spread's delta is smaller than the long call alone—the short call dampens directional sensitivity. Theta decay can work for or against you depending on which side is winning. A bull call spread with time decay eats into the short call's value faster than the long call's, which is good. A bear put spread experiences theta decay on both legs negatively if the stock falls sharply, reducing the put values and narrowing your profit zone.

## Costs and efficiency

Two commissions (one for entry, one for exit) and two separate Greeks to monitor make spreads more work than directional bets. But the defined risk and lower capital requirement often justify the friction, especially for retail traders operating with fixed account sizes and position limits.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/bull-call-spread/">Bull call spread</a> — bullish vertical spread using calls.</li>
<li><a href="/wiki/bear-call-spread/">Bear call spread</a> — bearish vertical spread using calls.</li>
<li><a href="/wiki/call-option/">Call option</a> — the components of call spreads.</li>
<li><a href="/wiki/put-option/">Put option</a> — the components of put spreads.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/strike-price/">Strike price</a> — the differentiator between legs.</li>
<li><a href="/wiki/option-chain/">Option chain</a> — where vertical spreads are visualized.</li>
<li><a href="/wiki/delta/">Delta</a> — directional sensitivity of the spread.</li>
</ul>
</div>
