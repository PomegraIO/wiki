---
title: "Ratio Put Spread"
description: "A credit-generating strategy that sells multiple puts at a lower strike against a single long put, designed to collect income from neutral to mildly bullish markets."
---

*A ratio put spread sells multiple puts below your long put, generating net credit while accepting capped but substantial downside loss risk. It's a put-based income strategy with defined maximum loss.*

## What a ratio put spread is

You buy one put at $100 and sell two puts at $95 (for example). If the two short puts generate $4 total premium and your long put costs $6, your net debit is $2. If the stock stays above $95, all puts expire worthless and you lose your $2 debit. If the stock crashes below $95, the short puts are at risk—you're naked one put below $95.

This is a variant of a [put ratio spread](/wiki/put-ratio-spread/) with tighter spacing and better risk control.

## Why to use a ratio put spread

The primary reason is **credit income with defined risk**. You're not naked short puts; the long put provides a floor on losses.

A second reason is **suitable for moderate bullish or neutral outlooks**. You're collecting income without betting directionally, as long as the stock stays above your short strike.

Ratio put spreads suit **systematic income strategies** where you're willing to accept occasional losses for steady monthly income.

## When a ratio put spread works

Ratio put spreads thrive in **bull markets or consolidation**. The stock stays above your short puts; all decay to zero; you keep the credit.

They also work in **elevated implied volatility**. Fat premiums mean the short puts generate substantial credit.

The strategy is ideal when you're **neutral to bullish and want income**. You're not betting the stock will crash; you're betting it won't.

## When a ratio put spread loses money

If the stock crashes below the short puts, losses escalate. The long put provides some protection, but losses below the short strike can be substantial.

Ratio put spreads also suffer from **IV spikes in down markets**. The short puts (OTM) remain safe, but losses can accelerate unexpectedly.

The strategy requires active management. If the stock approaches the short strike, you must roll or close to avoid naked exposure.

## Mechanics and adjustment

You typically receive a net credit—$200–$500. Maximum profit is the credit received. Maximum loss is `(short strike – long strike) – (credit received)` per share, typically $300–$600.

**Adjustment** is essential:
- **Rolling the shorts down**: If the stock falls toward the short strike, buy back the short puts and sell new ones lower.
- **Closing at profit**: If the stock rallies and your max profit is reached, close early.

## Ratio put spread vs. simple bull put spread

A [bull put spread](/wiki/bull-put-spread/) is safer; a ratio put spread generates more income but with higher complexity. Choose bull put spreads for straightforward income; choose ratio spreads for aggressive income portfolios.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/put-ratio-spread/">Put Ratio Spread</a> — the wider-spacing variant with more naked exposure.</li>
<li><a href="/wiki/bull-put-spread/">Bull Put Spread</a> — the safer two-leg alternative.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits ratio spreads.</li>
<li><a href="/wiki/put-option/">Put Option</a> — the contract type.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects spread credit.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying spreads.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring spread risk.</li>
<li>Naked Short — the risk component below the short strike.</li>
</ul>
</div>
