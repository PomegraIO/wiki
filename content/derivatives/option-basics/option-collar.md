---
title: "Option Collar"
description: "A strategy combining a protective put (long), held shares, and a covered call (short) to limit both downside loss and upside gain."
---

*A collar wraps a stock position in both protection and income. You own shares, buy a [put option](/wiki/put-option/) to establish a floor price, and sell a [call option](/wiki/call-option/) to cap the ceiling—all typically at the same expiration date. The premium from the short call often pays for or exceeds the cost of the long put, creating a hedge that is cheaper or free. The cost of this protection is foregoing upside above the short call's [strike price](/wiki/strike-price/).*

<aside class="wiki-infobox">
<div class="wiki-infobox-title">Option Collar — key facts</div>
<table>
<tr><th>Structure</th><td>Long stock + Long put + Short call</td></tr>
<tr><th>Cost</th><td>Usually zero or small net debit/credit</td></tr>
<tr><th>Max loss</th><td>Long put strike − stock cost − net premium</td></tr>
<tr><th>Max gain</th><td>Short call strike − stock cost + net premium</td></tr>
</table>
</aside>

## Choosing strikes to achieve zero cost

The elegance of a collar lies in strike selection. Suppose you own a stock at $100. You buy a $95 put for $2 and sell a $105 call for $2—the two premiums cancel, so the collar costs nothing. The downside is protected: if the stock crashes, you exercise the put and exit at $95, losing $5 per share (plus any dividends sacrificed). Upside is capped: if the stock soars to $150, your shares are called away at $105, capturing only $5 of gain. The zero-cost feature makes collars appealing to holders of concentrated positions who want downside protection but can't afford an outright [protective put](/wiki/protective-put/).

## Common use case: concentrated stock and tax deferral

Founders and executives with large positions in company stock often use collars to hedge without triggering capital gains. A founder holding appreciated shares can collar the position, locking in a floor without selling and incurring tax. Some founders hold the collar for years, occasionally rolling it (closing one and opening a new one at the same strikes). The IRS has specific rules about collars and loss-of-economic-substance doctrine, so tax advice is essential before implementing this strategy.

## Asymmetric cost collars and delta-neutral collars

Collars don't have to be zero-cost. A trader might buy an in-the-money put (expensive, more downside protection) and sell an out-of-the-money call (cheap, less upside lost). This results in a net debit—paying for downside protection out of pocket. Alternatively, a wide collar (put far out-of-the-money, call far in-the-money) might even generate a net credit, paying the holder to accept substantial downside risk in exchange for capturing almost all the upside.

## Rolling a collar

A collar expires at a fixed date. To extend the hedge, you close the current collar and open a new one at new strikes. Rolling is common for holders who want to maintain downside protection long-term. Rolling down (toward lower strikes) increases protection but reduces upside; rolling up (toward higher strikes) reduces protection but increases upside capture. The decision depends on the underlying's new level and the holder's views on forward returns.

## Dividend capture and assignment timing

A collar on a [dividend](/wiki/dividend/)-paying stock requires care around ex-dividend dates. If the short call is assigned early (on an American option), you lose the upcoming dividend. If not assigned, you capture the dividend but the long put's value erodes as the ex-date approaches (dividends reduce put value). Professional collars are often structured with quarterly rolling to time around dividend dates.

## Comparison to protective put and covered call

A [protective put](/wiki/protective-put/) alone leaves upside unlimited but costs premium. A [covered call](/wiki/covered-call/) alone captures premium but offers zero downside protection. A collar marries both: you get the downside floor of a protective put and the income of a covered call, ideally at zero net cost. The trade-off is capped upside, which is unacceptable to some investors but acceptable to those primarily concerned with protecting existing gains.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/protective-put/">Protective put</a> — the downside protection leg.</li>
<li><a href="/wiki/covered-call/">Covered call</a> — the income generation leg.</li>
<li><a href="/wiki/call-option/">Call option</a> — the upside cap.</li>
<li><a href="/wiki/put-option/">Put option</a> — the downside floor.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/strike-price/">Strike price</a> — the key to choosing collar levels.</li>
<li><a href="/wiki/option-premium/">Option premium</a> — the income and cost drivers.</li>
<li><a href="/wiki/american-option/">American option</a> — early assignment risk in collars.</li>
</ul>
</div>
