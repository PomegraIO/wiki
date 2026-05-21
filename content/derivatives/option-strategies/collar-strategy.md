---
title: "Collar Strategy"
description: "A hedging strategy that protects a long stock position by buying a put and selling a call at higher strikes, offsetting hedge costs."
---

*A collar pairs a long [put](/wiki/put-option/) and short [call](/wiki/call-option/) on the same underlying stock. The short call generates premium that partly or fully funds the protective put, creating a low-cost insurance policy with a capped upside.*

## What a collar is

If you own stock, you buy a put at a lower strike (floor) and sell a call at a higher strike (ceiling), both expiring in a few weeks or months. The call premium offsets or fully covers the put's cost. The result: you're insured against losses below the put strike, but gains are capped above the call strike.

Collars are used almost exclusively on positions you own. They answer the question: "I own stock I like, but I'm worried about a 10% correction. How do I hedge that without eliminating upside?"

## Why to use a collar

The primary reason is **cost-effective downside insurance**. Buying a naked put can cost 2–5% of stock value. Selling a call against it recovers 50–80% of that cost, making downside protection almost free.

A second reason is **simplicity**. Collars are conceptually cleaner than spreads or straddles. You own the stock; you're adding a floor and ceiling to your position.

Collars also suit **executives with concentrated holdings**. An exec who owns 10,000 shares of company stock can collar a meaningful position without raising insider-trading concerns (collars don't require selling the stock itself).

## When a collar works

Collars shine when **you're worried about short-term downside but bullish long-term**. You're not betting the stock will crash; you're protecting against a 15% correction while staying exposed to upside beyond that.

They also work well when the **short call strike is above your expected price target**. If you think the stock will rally to $110, selling a $115 call is painless—you're unlikely to be called away.

Collars are ideal for **elevated volatility environments** where put prices are inflated. Fat put premiums mean your short call covers more of the cost.

## When a collar constrains returns

If the stock rallies strongly above the call strike, you don't participate. Your position is capped at the call strike, creating opportunity cost. A 40% rally becomes a 20% gain because the short call forces you to sell.

Collars also lock you in psychologically. You've paid to hedge; you feel obligated to hold through expiration, even if your thesis changes and you want to exit or pivot.

If the stock declines sharply below the put strike, you're protected—but you've limited gains if it rebounds. Your payoff is bounded on both ends, which is sometimes exactly the point, but other times feels suffocating.

## Mechanics and adjustment

You typically pay a small net debit or break even at entry. A collar on $100 stock might cost: $2 to buy a $95 put, offset by $2 received from selling a $110 call. Cost: $0.

Maximum loss is `(stock price – put strike) = 5 percent` in this example. Maximum gain is `(call strike – original cost) = 10 percent`.

**Adjustment** is rare. You hold collars to expiration. If the stock breaches the put strike, you're protected—the put lets you sell at your floor. If the stock soars above the call strike, you accept the cap.

Some traders **roll the collar up and out**: buy back the short call at profit, sell a higher-strike call for the next month, and raise the put strike to maintain the collar's width. This resets the profit zone upward.

## Collar vs. naked stock ownership

Owning stock unhedged offers unlimited upside but unlimited downside risk. A collar caps downside but also caps upside. Choose a collar when you value downside insurance more than capturing every dollar of a rally. Choose naked stock when you're highly confident and can handle volatility.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/put-option/">Put Option</a> — the protective leg of a collar.</li>
<li><a href="/wiki/call-option/">Call Option</a> — the financed leg of a collar.</li>
<li><a href="/wiki/zero-cost-collar/">Zero Cost Collar</a> — variant where put cost exactly matches call premium.</li>
<li><a href="/wiki/protective-put/">Protective Put</a> — the put leg of a collar in isolation.</li>
<li><a href="/wiki/covered-call/">Covered Call</a> — the call leg of a collar in isolation.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying collars.</li>
<li><a href="/wiki/stock/">Stock</a> — the underlying asset in a collar.</li>
<li><a href="/wiki/hedge-fund/">Hedge Fund</a> — institutional context for collar strategies.</li>
</ul>
</div>
