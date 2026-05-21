---
title: "Reverse Iron Condor"
description: "A four-leg option strategy that buys puts and calls around the current price, designed to profit from large moves in either direction."
---

*A reverse iron condor (also called a long iron condor or strangle spread) buys both a put and call spread, profiting from directional moves while capping maximum loss. It's the inverse payoff of a standard iron condor.*

## What a reverse iron condor is

Instead of selling spreads for credit, a reverse iron condor buys spreads for a debit. You buy a put at a low strike, sell a put at a higher strike, buy a call at a high strike, and sell a call at a lower strike. The two short options don't fully offset the cost of the two long options; you pay a net debit.

You profit if the stock moves sharply in either direction beyond the short strikes. You lose if the stock stays between the short strikes—opposite of a standard [iron condor](/wiki/iron-condor/).

## Why to use a reverse iron condor

The primary reason is **long volatility with defined risk**. You're betting the stock will move far, but you've capped maximum loss by selling out-of-the-money options on both sides.

A second reason is **event-driven hedging**. If you own a stock and expect a volatile catalyst (earnings, lawsuit decision, regulatory ruling), a reverse iron condor lets you profit from the anticipated move while capping loss if nothing happens.

Reverse iron condors also suit **mean-reversion trades**. After a quiet period, stocks often break out sharply. You're buying the move and profiting from its magnitude.

## When a reverse iron condor wins

Reverse iron condors thrive when **implied volatility is depressed** before a catalyst. You're buying cheap options expecting realized volatility to exceed implied—a classic vol bet.

They also profit when **the stock moves sharply in either direction**. Unlike straddles, reverse iron condors cap loss, so a 50% move is just as good as a 30% move—you've hit max profit either way.

Reverse condors work best when you're **willing to be wrong on direction**. You don't care which way the stock moves as long as it moves far.

## When a reverse iron condor loses money

If the stock stays between the two short strike levels—your worst-case scenario—both spreads expire worthless and you've lost your full debit paid.

Reverse condors also lose if **implied volatility collapses post-entry**. A stock move that would normally be profitable can be erased by IV crush. A 30% rally is a loss if IV collapses 40%.

Time decay is your enemy until the stock moves. Early in the trade, theta decay slowly erodes your long options without compensating move in the stock. You need movement soon after entry to justify the cost.

## Mechanics and adjustment

You pay a net debit at entry—typically $200–$500. Maximum loss is the debit paid. Maximum profit is `(difference between short strikes) – (net debit)`, often a similar dollar amount as max loss.

Break-even points are the short strike minus the debit (downside) and the short strike plus the debit (upside). If you paid $300 debit for short strikes at $95 put and $105 call, you break even at $92.70 and $108.30—a ~15% move in either direction.

**Adjustment** is optional:
- **Closing early**: If the stock moves, close the profitable side early and let the other side expire or take a loss.
- **Rolling toward the move**: If the stock rallies, buy back the short calls and sell new ones higher, rolling in the direction of the move.
- **Letting it expire**: Some traders let both sides expire, accepting max loss if the stock stalled.

## Reverse iron condor vs. standard iron condor

A standard iron condor profits from stagnation; a reverse iron condor profits from volatility. Choose standard condors when you're neutral and want income; choose reverse condors when you expect a big move but aren't sure of direction.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/iron-condor/">Iron Condor</a> — the opposite payoff structure.</li>
<li><a href="/wiki/straddle/">Straddle</a> — alternative long-volatility strategy.</li>
<li><a href="/wiki/strangle/">Strangle</a> — another long-volatility approach.</li>
<li><a href="/wiki/bull-put-spread/">Bull Put Spread</a> — the put half of a reverse condor.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — key to reverse condor profitability.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying reverse condors.</li>
<li><a href="/wiki/vega/">Vega</a> — the Greek measuring volatility sensitivity.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for managing condor risk.</li>
</ul>
</div>
