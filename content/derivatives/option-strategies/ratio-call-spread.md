---
title: "Ratio Call Spread"
description: "A credit-generating strategy that sells multiple calls at a higher strike against a single long call at a lower strike, generating income with defined risk."
---

*A ratio call spread sells multiple calls above your long call, collecting net credit while accepting capped but substantial upside loss risk. It's a refinement of [call ratio spreads](/wiki/call-ratio-spread/) with better risk management through tighter strike spacing.*

## What a ratio call spread is

You buy one call at $100 and sell two calls at $105 (for example). If the two short calls generate $3 total premium and your long call costs $5, your net debit is $2. If the stock stays below $100, both calls expire worthless and you lose $2. If the stock rallies above $105, the short calls are at risk—you're naked one call above $105.

This is a variant of a call ratio spread but using tighter spacing between long and short.

## Why to use a ratio call spread

The primary reason is **credit income with controlled risk**. You're not naked short calls; the long call provides a floor on losses.

A second reason is **capital efficiency**. By selling more options than you buy, you generate income that offsets your cost or even turns negative (a credit).

Ratio call spreads suit **income portfolios** where you're willing to cap upside for reliable premium collection.

## When a ratio call spread works

Ratio call spreads thrive in **consolidation or mild bull markets**. The stock rallies slowly; your short calls decay; you pocket income.

They also work in **elevated implied volatility**. Fat premiums mean the short calls generate substantial credit.

The strategy is ideal when you're **confident in an upside ceiling** but willing to be called away above that level.

## When a ratio call spread loses money

If the stock rallies sharply beyond the short calls, losses escalate. The long call provides some protection, but losses above the short strike can be substantial.

Ratio call spreads also suffer from **IV spikes**. The short calls (OTM) remain safe, but your cost structure doesn't benefit—losses can widen unexpectedly.

The strategy requires active management. If the stock approaches the short strike, you must roll or close to avoid naked exposure.

## Mechanics and adjustment

You typically receive a net credit—$100–$300. Maximum profit is the credit received. Maximum loss is `(short strike – long strike) – (credit received)` per share, typically $200–$500.

**Adjustment** is key:
- **Rolling the shorts up**: If the stock rallies, buy back the short calls and sell new ones higher.
- **Closing at profit**: If the stock consolidates and theta decay generates your max profit, close early.

## Ratio call spread vs. simple bull call spread

A bull call spread is safer; a ratio call spread generates more income but with higher complexity and risk. Choose bull call spreads for straightforward directional bets; choose ratio spreads for income portfolios willing to manage complexity.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/call-ratio-spread/">Call Ratio Spread</a> — the wider-spacing variant with more naked exposure.</li>
<li><a href="/wiki/bull-call-spread/">Bull Call Spread</a> — the safer two-leg alternative.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits ratio spreads.</li>
<li><a href="/wiki/call-option/">Call Option</a> — the contract type.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects spread credit.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying spreads.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring spread risk.</li>
<li>Naked Short — the risk component above the short strike.</li>
</ul>
</div>
