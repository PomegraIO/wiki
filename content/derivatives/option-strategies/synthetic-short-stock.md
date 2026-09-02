---
title: "Synthetic Short Stock"
description: "An option strategy that sells a call and buys a put at the same strike, replicating short stock payoff using options instead of a short sale."
---

*A synthetic short pairs a short [call](/wiki/call-option/) and long [put](/wiki/put-option/) at identical strikes, replicating the payoff of a short stock position. It profits from declines while avoiding borrow costs and settlement complications of naked short sales.*

## What a synthetic short stock is

You sell a call at strike $100 and buy a put at the same $100 strike, expiring the same period. If the stock falls to $90, the call expires worthless and the put is worth $10 (ITM by $10). Your net gain is $10—identical to owning a short position that rallied $10 (profit from decline).

If the stock rises to $110, the call is ITM by $10 and you're forced to sell stock at $100; the put is worthless. Your net loss is $10—identical to a short position that fell $10 (loss from rally).

The payoff mirrors short stock ownership, but avoids the complications of an actual short sale.

## Why to use a synthetic short stock

The primary reason is **avoiding short-sale complications**. Short selling requires stock borrow, which can be expensive or impossible for thinly traded names. A synthetic achieves short exposure without borrow costs.

A second reason is **leverage and capital efficiency**. A synthetic uses far less capital than being short stock. The margin required is minimal; your profit/loss is dollar-for-dollar with stock.

Synthetics also suit **bearish bets in accounts where naked short selling is restricted**. Some IRAs and 401ks allow options but prohibit short selling; a synthetic short provides the strategy's payoff within those constraints.

## When a synthetic short works

Synthetic shorts thrive when **you're bearish and want leveraged downside exposure**. You profit from declines like a short seller, but with less capital and no borrow costs.

They also work in **declining markets**. As the stock falls, your short call becomes safer (further OTM) and your long put becomes more valuable.

Synthetics are ideal for **tactical bearish bets**. You're not trying to be short long-term; you're capturing a 2–8 week decline before rolling or closing.

## When a synthetic short loses money

If the stock rallies sharply, you're forced to sell stock at your short call's strike, locking in losses. Unlike an actual short sale where you can cover and exit, a synthetic at expiration must settle—you're short stock or closed out.

Synthetic shorts also suffer from **implied volatility spikes**. The call you sold loses value if IV rises (good for you on the short side), but the put you bought gains value if IV rises (bad for you). Both legs work against you.

If the stock rallies and you're forced to sell at the strike, you can't participate in further gains. Upside loss is capped at the strike, but losses from being forced to sell at a lower price than the eventual stock price are real.

## Mechanics and adjustment

You receive a net credit or pay a net debit, depending on whether the call premium exceeds the put cost. If both legs are ATM, they typically offset, leaving a net zero.

Your maximum profit is the strike price minus the net cost paid (or plus the net credit received). Your maximum loss is theoretically unlimited (stock can't go below zero but losses accelerate as the stock falls).

**Adjustment** is optional. You hold to expiration and accept settlement, or roll the position: buy back the short call and long put expiring soon, sell a new call and buy a new put at the same or different strike for a later expiration.

## Synthetic short vs. actual short sale

An actual short sale requires stock borrow and pays you interest. A synthetic short uses options and costs commissions but avoids borrow costs. Choose synthetics to avoid borrow complexity; choose actual short sales for true short-equity exposure in the account's accounting.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/synthetic-long-stock/">Synthetic Long Stock</a> — the long-equivalent strategy.</li>
<li><a href="/wiki/short-selling/">Short Selling</a> — the traditional downside exposure method.</li>
<li><a href="/wiki/call-option/">Call Option</a> — the short leg of a synthetic.</li>
<li><a href="/wiki/put-option/">Put Option</a> — the long leg of a synthetic.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects synthetic entry cost.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying synthetics.</li>
<li>Leverage — the key advantage of synthetics.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring synthetic risk.</li>
</ul>
</div>
