---
title: "Conversion Strategy"
description: "An arbitrage strategy that pairs a short stock position with a long call and short put at the same strike, exploiting pricing inefficiencies between stock and options."
---

*A conversion pairs a short stock position with a long [call](/wiki/call-option/) and short [put](/wiki/put-option/) at identical strikes. It's a market-neutral arbitrage designed to lock in profit if options are overpriced relative to stock.*

## What a conversion is

You short 100 shares of stock at $100, simultaneously buy a $100 call, and sell a $100 put, all expiring the same period. At expiration:

- Stock below $100: the put forces you to buy stock at $100 (offsetting your short). The call expires worthless. You buy high, sold high—neutral payoff.
- Stock above $100: you exercise the call to buy stock at $100 (covering your short). The put expires worthless. You sell high, buy high—neutral payoff.

In all cases, your payoff is deterministic: the cost/credit difference between the options and the short stock. If options are overpriced, you profit.

## Why to use a conversion

The primary reason is **volatility arbitrage**. If options are expensive relative to stock (implied volatility too high), a conversion lets you sell that expensive volatility while hedging away the directional risk via the short stock.

A second reason is **dividend harvesting**. When a stock is about to pay a dividend, options don't adjust for it. A conversion allows you to collect the dividend while remaining fully hedged.

Conversions also suit **merger arbitrage**. If a stock is announcing an acquisition, implied volatility often spikes. A conversion locks in the over-priced premium.

## When a conversion works

Conversions work when **implied volatility is abnormally high**. You're selling expensive protection (short call, short put) while shorting stock.

They also work when **there are arbitrage opportunities** between stock lending rates, dividend payments, and option prices. Professional traders routinely scan for these.

Conversions excel in **high-volatility events**: earnings announcements, FDA decisions, merger news. Options typically overprice the move; conversions capitalize on that overpricing.

## When a conversion loses money

If you overpay for the options relative to the stock short (if options are actually fairly priced or cheap), you lock in a loss from day one.

Conversions also suffer if **you can't borrow stock**. Short selling requires borrow; in tight borrows, the cost eats into your arbitrage edge.

Conversions also create dividend complications. You're short stock, so you owe dividends to the person who lent you shares. Options don't pay dividends; you're exposed to that cash flow differential.

## Mechanics and adjustment

You typically receive a net credit or pay a net debit, depending on whether the short stock credit plus short put premium exceeds the long call cost.

Your payoff is deterministic: maximum profit is the net credit received or the difference between the box value and your entry cost. Maximum loss is the net debit paid.

**Adjustment** is not needed. You hold to expiration, where the payoff is locked in. The put forces you to buy at the strike (covering your short) or you exercise the call to buy at the strike.

## Reversal strategy (the inverse)

A reversal is the inverse: long stock, short call, long put at the same strikes. It profits when options are cheap relative to stock. Conversions and reversals are mirror-image arbitrage strategies.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li>Reversal Merger — the inverse arbitrage strategy.</li>
<li><a href="/wiki/short-selling/">Short Selling</a> — the short stock component.</li>
<li><a href="/wiki/call-option/">Call Option</a> — the long leg of a conversion.</li>
<li><a href="/wiki/put-option/">Put Option</a> — the short leg of a conversion.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — key to conversion profitability.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying conversions.</li>
<li>Arbitrage — the principle underlying conversions.</li>
<li><a href="/wiki/dividend/">Dividend</a> — complicates conversion payoff.</li>
</ul>
</div>
