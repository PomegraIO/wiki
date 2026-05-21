---
title: "Zero Cost Collar"
description: "A hedging strategy that protects long stock by combining a protective put and covered call at strikes chosen so the put cost is fully offset by call premium."
---

*A zero cost collar pairs a long [put](/wiki/put-option/) and short [call](/wiki/call-option/) on stock you own, with strikes chosen such that the put's cost exactly equals the call's premium generated. It provides downside insurance for free.*

## What a zero cost collar is

You own 100 shares at $100. You buy a $95 put for $2 and sell a $105 call for $2. The costs offset; you're hedged for zero net cost. Below $95, the put protects you; above $105, the call caps your gains. Between these strikes, you're exposed.

This is identical to a [collar strategy](/wiki/collar-strategy/) where the strikes are chosen specifically to make the put cost zero.

## Why to use a zero cost collar

The primary reason is **free insurance**. You get downside protection without paying for it—a powerful appeal for executives, founders, or concentrated-position holders.

A second reason is **psychological comfort**. Knowing your worst case is defined costs nothing. The floor can make a volatile position psychologically tolerable.

Zero cost collars also suit **earnings periods**. Before announcing results, buy a protective put at zero cost and keep upside capped. If the news is bad, you're hedged; if good, you've capped upside but at least you're flat.

## When a zero cost collar works

Zero cost collars work when the **volatility environment makes put and call premiums symmetrical**. This happens frequently; find a put strike where the cost equals a call strike's premium.

They also work when you're **willing to sacrifice upside for downside certainty**. The trade-off is explicit and fair when costs are zero.

Zero cost collars are ideal for **concentrated holdings** where downside insurance has high value.

## When a zero cost collar constrains returns

If the stock rallies sharply, you don't participate beyond the call strike. Leaving 10–20% on the table (the distance between current and call strike) feels like a loss, especially if the stock soars further.

Zero cost collars also require **precise execution**. You must find two strikes where premiums exactly match. If the call premium is $1.95 and the put cost is $2.05, there's a small cost; you're not truly at zero.

The strategy is also less flexible. Once you've locked in the collar, adjusting is costly. Rolling the collar to a new set of strikes requires new commissions.

## Mechanics and adjustment

You pay zero net debit at entry (or a small credit if you're lucky on pricing).

Maximum loss is `(stock price – put strike)`. Maximum gain is `(call strike – stock price)`.

Return on risk is `(call strike – stock price) / (stock price – put strike)`. If this ratio is favorable (e.g., 3:1), the collar is attractive.

**Adjustment** is rare. Most collars are held to expiration or near-term (3–6 months) and then replaced with a new one.

Some traders **roll the collar up and out**: buy back the short call, extend the put to a later month, sell a new higher-strike call. This resets the collar upward.

## Zero cost collar vs. buying puts outright

Buying a protective put alone gives unlimited upside but costs cash. A zero cost collar gives bounded upside but costs nothing. Choose zero cost collars for cheap insurance on a specific time frame; choose naked puts if you're confident in unlimited upside potential.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/collar-strategy/">Collar Strategy</a> — the general strategy; zero cost is a special case.</li>
<li><a href="/wiki/protective-put/">Protective Put</a> — the put component of a zero cost collar.</li>
<li><a href="/wiki/covered-call/">Covered Call</a> — the call component of a zero cost collar.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — determines whether a zero cost collar is achievable.</li>
<li><a href="/wiki/put-option/">Put Option</a> — the protection leg.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/stock/">Stock</a> — the underlying asset being hedged.</li>
<li><a href="/wiki/option/">Option</a> — contract type underlying collars.</li>
<li><a href="/wiki/hedge-fund/">Hedge Fund</a> — institutional context for collars.</li>
</ul>
</div>
