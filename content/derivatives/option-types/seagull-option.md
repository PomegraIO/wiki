---
title: "Seagull Option"
seo_title: "Seagull Option: Three-Leg Strategy With Near-Zero Cost"
description: "A seagull option pairs a call spread with a short put, often for zero net cost. Payoff zones, a EUR/USD example, and why forex hedgers use the structure."
---

*A seagull option buys one call spread and sells a put, creating a compound position that reduces cost by collecting put premium. It's a cost-reduced bull call spread, common in currency and emerging-market hedging.*

## Structure of a seagull option

A seagull option has three strikes. You buy a call at strike A, sell a call at strike B (creating a call spread), then sell a put at strike C below the current price.

For example, on EUR/USD at 1.10: buy a 1.11 call for 0.003, sell a 1.12 call for 0.001, and sell a 1.09 put for 0.002. Net cost: 0.003 − 0.001 − 0.002 = zero.

The payoff zones are:

- **Below 1.09**: Unlimited loss. The put is exercised; you're forced to buy EUR at 1.09, but EUR has fallen further.
- **Between 1.09 and 1.10**: The put is in-the-money, loss increases linearly.
- **Between 1.10 and 1.11**: Both calls and put are out-of-the-money; you own nothing.
- **Between 1.11 and 1.12**: The long call is in-the-money; profit increases.
- **Above 1.12**: The short call caps profit.

The seagull combines upside call spread (bullish) with a naked short put (bearish obligation). The put premium offsets call spread cost, often to zero.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Seagull Option — key facts</div>
  <table>
    <tr><th>Type</th><td>Compound options strategy</td></tr>
    <tr><th>Legs</th><td>Long call + short call + short put</td></tr>
    <tr><th>Net cost</th><td>Often zero or near zero</td></tr>
    <tr><th>Max gain</th><td>Capped at call spread width</td></tr>
    <tr><th>Max loss</th><td>Capped at put strike minus short call strike, or unlimited</td></tr>
    <tr><th>Typical use</th><td>Low-cost hedging in forex and emerging markets</td></tr>
  </table>
</aside>

## Why seagulls are used in forex

Seagull options are popular in forex because currency traders often want to hedge downside but don't want to pay for puts. A seagull lets them hedge downside (short put) while gaining upside (long call spread) at zero cost.

For example, an exporter receiving EUR in six months buys a seagull: buy EUR/USD calls, sell calls above, sell puts below. If EUR weakens, the put triggers and they're forced to buy—expensive, but they wanted to be hedged anyway. If EUR strengthens, the call spread caps gains but provides some upside. The zero cost is attractive.

Seagulls are also used by emerging-market investors. A portfolio manager buying EM assets wants to hedge currency risk but fears option costs. A seagull provides hedging at zero cost, albeit with capped upside.

## The name

"Seagull" is sometimes called a "seagull spread." The name is informal and suggests the profile looks like a seagull in flight: call spread (the wings) plus short put (the body). It's not a standard term, and various brokers use slightly different definitions. Some define seagull as a call spread alone (two legs), while others include the put.

## Cost reduction and the trade-off

The key attraction is cost reduction. A call spread costs net debit (you pay more than you collect). Adding a short put collects premium to offset the cost.

The trade-off: you accept downside risk. If the underlying crashes below the put strike, you face unlimited loss (if the put is naked) or large loss (if you have protection via an even lower put).

For investors with strong downside conviction, this is acceptable. For those uncertain about downside, it's unwise.

<div class="wiki-hatnote">For pure call spread profit, see <a href="/wiki/call-spread/">call spreads</a>. For defined-risk short put, see <a href="/wiki/put-spread/">put spreads</a>.</div>

## Variants

A **short seagull** (reverse seagull) uses short call spread + long put. The net position is bearish with hedged downside. It's less common because short call spreads are usually less attractive than short put spreads in income strategies.

Some traders define "seagull" more broadly as any three-leg option structure, but the classic seagull is call spread + short put.

## Risk and limitations

Seagull options create naked or semi-naked short put risk. If the underlying crashes, you're exposed to loss. Unlike call spreads, which have defined max loss, seagulls have undefined max loss unless you buy protection (a fourth leg, turning it into an iron condor).

They're also complicated to manage. If the put goes in-the-money, you must decide to close, roll, or accept assignment. This requires active monitoring.

Liquidity is also a constraint. Seagulls are OTC; you need a dealer who can price all three legs efficiently. Retail traders rarely have access.

## In practice

Seagull options appear primarily in:

1. **Currency hedging**: Exporters and importers use seagulls to hedge FX risk at zero cost.
2. **Emerging market hedging**: Portfolio managers hedging EM currency exposure.
3. **Commodity trading**: Traders hedging commodity price exposure.

They're rare in equity markets, where simpler spreads are more liquid. Most equity traders use call spreads or iron condors instead.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/call-spread/">Call spread</a> — the bullish component.</li>
  <li><a href="/wiki/put-spread/">Put spread</a> — the bearish component.</li>
  <li><a href="/wiki/iron-condor/">Iron condor</a> — a related four-leg structure.</li>
  <li><a href="/wiki/collar/">Collar</a> — another three-leg hedge.</li>
  <li><a href="/wiki/fx-option/">FX option</a> — underlying for currency seagulls.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational contract.</li>
  <li><a href="/wiki/derivatives/">Derivatives</a> — asset class overview.</li>
  <li><a href="/wiki/currency-option/">Currency option</a> — where seagulls commonly appear.</li>
</ul>
</div>
