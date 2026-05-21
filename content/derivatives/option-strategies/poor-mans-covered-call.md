---
title: "Poor Man's Covered Call"
description: "A strategy that buys a longer-dated call and sells shorter-dated calls against it, replicating covered call returns with less capital than owning stock."
---

*A poor man's covered call (or call diagonal) buys a call expiring in 3–6 months and sells calls expiring in 1–3 months at higher strikes, mimicking a [covered call](/wiki/covered-call/) on 100 shares without actually owning the stock. It offers leverage and reduced capital requirement.*

## What a poor man's covered call is

You buy a call at $100 expiring in six months, then immediately sell a call at $105 expiring in one month. You pay a net debit—the long call costs more than the short call generates. As the short call expires, you roll it (close and sell a new one) monthly.

The payoff mirrors stock ownership plus covered calls, but uses far less capital—just the difference between the two call prices instead of the stock price.

## Why to use a poor man's covered call

The primary reason is **capital efficiency**. A long stock position requires $10,000; a poor man's covered call might cost $300–$500. You get similar exposure with 20x less capital.

A second reason is **leverage**. Your percentage return is magnified. If the stock appreciates $5 and you collect $2 in monthly option premium, a stock position returns 7%; a poor man's covered call returns 140% (on $500 cost basis).

Poor man's covered calls also suit **traders without large capital** who want stock-like returns but have limited funds.

## When a poor man's covered call works

Poor man's covered calls thrive in **bull markets where the stock rallies steadily**. Your long call appreciates while you harvest monthly premium from the shorts.

They also work in **elevated implied volatility**. Fat short call premiums create substantial monthly income.

The strategy is ideal when you're **bullish and willing to cap upside** in exchange for leveraged exposure.

## When a poor man's covered call loses money

If the stock crashes, your long call (the asset) decays toward zero. Unlike stock ownership (which can be held indefinitely), option decay accelerates as expiration nears. You lose the long call's value faster than a stock holder loses.

Poor man's covered calls also suffer from **implied volatility collapses**. The long call loses value if IV drops; the short calls you sell (which should regenerate income) generate less premium as IV falls.

Time decay is your enemy. Unlike stock (which doesn't decay), both your long and short calls bleed value. You're betting that short-term premium exceeds long-term decay—a race against the clock.

## Mechanics and adjustment

You pay a net debit at entry—typically $200–$500. Maximum profit is theoretically `(upper call strike – long call strike) – (net debit)` if the stock rallies past the upper call. Maximum loss is the net debit paid if the stock crashes and both calls expire worthless.

**Adjustment** is monthly:
- **Rolling the short**: Every month, close the expiring short call and sell a new one for the next month.
- **Rolling the long**: If the stock has appreciated significantly, you might buy back the long call and sell a new one at a higher strike, extending the position.

## Poor man's covered call vs. stock ownership

Stock offers unlimited holding period and dividend income. A poor man's covered call offers leverage but requires constant rolling and eventually expires. Choose poor man's covered calls for short-term, leveraged bullish bets; choose stock for long-term wealth building.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/covered-call/">Covered Call</a> — the stock-based strategy this replicates.</li>
<li><a href="/wiki/diagonal-spread/">Diagonal Spread</a> — the underlying structure (different expirations).</li>
<li><a href="/wiki/call-option/">Call Option</a> — both legs of a poor man's covered call.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay on the long call that erodes returns.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects both call prices.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying this strategy.</li>
<li><a href="/wiki/leverage/">Leverage</a> — the key advantage vs. stock ownership.</li>
<li><a href="/wiki/stock/">Stock</a> — the underlying asset.</li>
</ul>
</div>
