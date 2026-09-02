---
title: "Synthetic Long Stock"
description: "An option strategy that buys a call and sells a put at the same strike, replicating the payoff of stock ownership without actually owning shares."
---

*A synthetic long pairs a long [call](/wiki/call-option/) and short [put](/wiki/put-option/) at identical strikes. It replicates stock payoff (dollar-for-dollar gain/loss above and below the strike) while using leverage and avoiding dividends or voting rights.*

## What a synthetic long stock is

You buy a call at strike $100 and sell a put at the same $100 strike, expiring the same period. If the stock rallies to $110, the call is worth $10 (ITM by $10); the put is worthless. Your net gain is $10—identical to owning stock that rallied $10.

If the stock declines to $90, the call is worthless; the put is ITM by $10, forcing you to buy stock at $100. Your net loss is $10—identical to owning stock that dropped $10.

The payoff is mathematically equivalent to owning stock, but requires options and leverage.

## Why to use a synthetic long stock

The primary reason is **leverage**. A synthetic long uses far less capital than buying stock outright. One $100 call costs $3–$5; one $100 put generates $2–$4 in credit. Your net cost is minimal, yet your profit/loss is dollar-for-dollar with stock. You've effectively borrowed capital.

A second reason is **tax treatment in some jurisdictions**. Synthetics may be treated differently than stock ownership for tax purposes—consult a tax professional.

Synthetics also suit **dividend avoidance**. If you're bullish but don't want dividend distributions (for tax or reinvestment reasons), a synthetic avoids them.

## When a synthetic long works

Synthetics thrive when **you're bullish and want leveraged exposure**. You get stock-like payoff with minimal capital and no margin interest (your capital isn't technically borrowed, just not fully deployed).

They also work in **low-interest-rate environments** where the interest cost of leveraging a long stock position would be high. A synthetic achieves the same leverage with options.

Synthetics are ideal for **tax-deferred accounts** (401ks, IRAs) where options are allowed but margin is restricted.

## When a synthetic long loses money

If the stock declines sharply, you're forced to own stock at your call strike, locking in losses. Unlike a stock owner who can hold and wait for recovery, a synthetic at expiration must settle—you own stock or don't.

Synthetics also suffer from **implied volatility collapse**. The call you bought loses value if IV drops; the put you sold gains value if IV drops. Both work against you.

Transaction costs (commissions on four legs: buy call, sell put, sell stock or exercise call, buy stock from put assignment) can be substantial. Over time, these costs erode the leverage advantage.

## Mechanics and adjustment

You pay a net debit or credit depending on whether the call costs more or less than the put generates. If call premium = put premium, the position is free.

Your maximum profit and loss are unlimited—identical to stock ownership. Break-even is the strike price minus the net debit paid (or plus the net credit received).

**Adjustment** is typically unnecessary. You hold to expiration and accept settlement (stock is assigned/exercised), then the position is closed.

Some traders "roll" synthetics: buy back both the call and put expiring soon, sell new call and put at a new strike for a later expiration. This adjusts the position as the stock moves.

## Synthetic long vs. stock ownership

Owning 100 shares costs $10,000 (at a $100 stock price) and generates dividends. A synthetic long costs $100–$500 and generates no dividends but offers leverage. Choose synthetics for leveraged bullish exposure with minimal capital; choose stock for dividend income and simplicity.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/synthetic-short-stock/">Synthetic Short Stock</a> — the short-equivalent strategy.</li>
<li><a href="/wiki/call-option/">Call Option</a> — the long leg of a synthetic.</li>
<li><a href="/wiki/put-option/">Put Option</a> — the short leg of a synthetic.</li>
<li><a href="/wiki/stock/">Stock</a> — the underlying asset replicated by a synthetic.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects synthetic entry cost.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying synthetics.</li>
<li>Leverage — the key advantage of synthetics.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring synthetic risk.</li>
</ul>
</div>
