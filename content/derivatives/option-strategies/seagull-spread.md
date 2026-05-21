---
title: "Seagull Spread"
description: "A three-leg option strategy that buys protection at one strike and sells two options at higher strikes, designed to reduce hedging cost in bullish markets."
---

*A seagull spread buys a protective [put](/wiki/put-option/) and sells a short call and a higher call at different strikes, with the sales offsetting much of the put's cost. It's a cost-efficient collar variant for those willing to cap upside.*

## What a seagull spread is

You buy a $95 put for $2, sell a $105 call for $1, and sell a $110 call for $0.50. You receive net credit: 1.50 per share. This credit can fully offset the put cost or even generate a small gain.

If the stock stays between the put and the first short call, you keep the credit and are protected. If it rises above the first short call, it gets called away. If it falls below the put, the put protects you.

## Why to use a seagull spread

The primary reason is **downside insurance with zero or negative cost**. You get a protective put funded entirely by the options you sell, creating true leverage.

A second reason is **suited to moderately bullish outlooks with downside worry**. You're not betting on a crash; you're protecting against it while staying bullish.

Seagull spreads also appeal to **yield-seeking investors**. The credit you collect generates return while you own stock.

## When a seagull spread wins

Seagull spreads thrive in **moderate bull markets where the stock rallies steadily but modestly**. You're protected downside, profiting from the rally up to the first short call.

They also excel when **implied volatility is elevated**. Fat short call premiums allow you to fully offset the put cost or even generate credit upfront.

The strategy works best when you're **bullish but willing to be called away at a profitable level**. If you're happy to sell at $105, a seagull lets you own stock and generate income.

## When a seagull spread loses money

If the stock crashes hard below the put strike, your loss is capped but real. The protection is expensive (you paid for it via opportunity cost of lost calls).

Seagull spreads also suffer if **the stock gaps down hard between the put strike and your short strikes**. A gap down could hurt despite the put protection if the put strike is close to the short calls.

If **implied volatility collapses**, the credit you received evaporates, and you're locked into lower cash flow than you expected.

## Mechanics and adjustment

You typically receive a net credit—$50–$200. Maximum profit is the credit received (if the stock stays between your short calls and put). Maximum loss is `(stock price – put strike)`, capped to a defined downside.

**Adjustment** is optional:
- **Rolling the short calls**: If the stock rallies through the first short call, buy it back and sell a new higher call.
- **Closing early**: If the stock hits your profit zone, close and redeploy.

## Seagull spread vs. regular collar

A regular collar buys one put and sells one call. A seagull spreads the short-call premium across two calls at different strikes, allowing cost optimization and better control of assignment risk.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/collar-strategy/">Collar Strategy</a> — the two-leg variant.</li>
<li><a href="/wiki/zero-cost-collar/">Zero Cost Collar</a> — collar designed to have zero net cost.</li>
<li><a href="/wiki/protective-put/">Protective Put</a> — the put component of a seagull.</li>
<li><a href="/wiki/covered-call/">Covered Call</a> — the call component of a seagull.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — determines seagull credit.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying seagulls.</li>
<li><a href="/wiki/strike-price/">Strike Price</a> — defines seagull zones.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring seagull risk.</li>
</ul>
</div>
