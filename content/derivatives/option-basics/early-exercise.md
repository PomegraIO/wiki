---
title: "Early Exercise"
description: "The exercise of an option before its expiration date, allowed for American-style options but not for European-style ones."
---

*Early exercise occurs when a holder of an [American option](/wiki/american-option/) invokes the right to buy or sell the underlying asset before the [expiration date](/wiki/expiration-date/)—a privilege unique to American-style contracts. Whether early exercise makes economic sense depends on the underlying's behavior, [dividend](/wiki/dividend/) schedules, and the [time value](/wiki/time-value/) remaining in the option.*

<div class="wiki-hatnote">For European options, exercise is not permitted until expiration; early exercise is exclusively a feature of American contracts.</div>

## When early exercise makes sense for calls

For a [call option](/wiki/call-option/), early exercise on a non-dividend-paying stock is economically irrational. The call's price includes time value—the possibility of further upside—which you forfeit if you exercise early and buy the stock. You're better off selling the call and keeping the time value. However, when the underlying pays a large [dividend](/wiki/dividend/), the calculus flips. If the dividend exceeds the remaining time value, a rational call holder exercises before the ex-dividend date to capture that income. The earlier the ex-date, the sooner this becomes optimal.

## Put holders and downside capture

For a [put option](/wiki/put-option/), early exercise is more common and sometimes necessary. If the underlying has crashed and is still falling, an owner of deep-in-the-money puts might exercise to lock in a gain, redeploy the capital, and exit a position that no longer needs downside protection. The time value remaining in the put may be thin, and the certainty of capturing the [intrinsic value](/wiki/intrinsic-value/) may outweigh waiting for further upside. American puts, especially on volatile stocks, are frequently exercised well before expiration.

## The assignment hazard for writers

From the short side, early exercise is a nuisance. A writer of a covered call that is assigned early must hand over shares, sometimes weeks before expiration, disrupting a carefully planned hedge. The short put seller must take delivery of shares earlier than expected, tying up capital sooner. This is why professional traders and market makers prefer [European options](/wiki/european-option/) on indexes and currencies—the exercise timeline is fixed and predictable.

## Why it happens in practice

Early exercise also occurs by accident. Some retail investors exercise winners automatically at expiration without understanding the economics. Brokers may exercise in-the-money options by default if the holder doesn't cancel the instruction. In most cases, early exercise is suboptimal for the exerciser compared to selling the option in the secondary market—but transaction costs and human error mean it still happens regularly.

## Pricing the early-exercise premium

The possibility of early exercise adds value to an American option compared to an otherwise identical [European option](/wiki/european-option/). Pricing American options requires numerical methods (binomial trees, Monte Carlo simulation) to model the holder's optimal exercise decision at each point in time. The [Black-Scholes model](/wiki/black-scholes-model/), while elegant, cannot capture this early-exercise feature and is only appropriate for European contracts.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/american-option/">American option</a> — permits exercise at any time before expiration.</li>
<li><a href="/wiki/european-option/">European option</a> — exercise only at expiration.</li>
<li><a href="/wiki/exercise/">Exercise</a> — the act of using the right in an option contract.</li>
<li><a href="/wiki/in-the-money/">In-the-money</a> — when exercise would be profitable.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/call-option/">Call option</a> — the right to buy.</li>
<li><a href="/wiki/put-option/">Put option</a> — the right to sell.</li>
<li><a href="/wiki/time-value/">Time value</a> — value from potential future moves before expiration.</li>
</ul>
</div>
