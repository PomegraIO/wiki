---
title: "Spread Option"
description: "An option whose payoff depends on the difference between two underlying prices or rates, useful for hedging relative price movements."
---

*A spread option is a derivative where the payoff is based on the difference between two underlying values—two stocks, two commodity prices, two currencies, or two interest rates. It's especially useful for hedging basis risk and relative price changes.*

## How spread options work

A **spread call** has a positive payoff when the price difference exceeds a strike. For example, a call on the spread between crude oil and natural gas: if crude is $80 and natural gas is $4 per MMBtu, the spread is $76. If the spread call has a strike of $70, the payoff at expiration is max(76 − 70, 0) = $6.

The payoff is the absolute difference between the two underlyings minus the strike (or plus the strike for spread puts). Spread options are powerful for traders whose P&L depends on relative prices, not absolute prices.

A **spread put** has positive payoff when the spread is below the strike. A refiner might buy a spread put on crude-to-gasoline. If the spread narrows (gasoline stays stable while crude rallies), the put protects against margin compression.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Spread Option — key facts</div>
  <table>
    <tr><th>Type</th><td>Exotic option on two underlyings</td></tr>
    <tr><th>Payoff</th><td>Call: max(S1 − S2 − K, 0); Put: max(K − (S1 − S2), 0)</td></tr>
    <tr><th>Risk</th><td>Delta on both legs; correlation risk</td></tr>
    <tr><th>Liquidity</th><td>OTC; illiquid; wide spreads</td></tr>
    <tr><th>Valuation</th><td>Requires correlation between underlyings</td></tr>
    <tr><th>Typical use</th><td>Hedging basis risk, margin risk, relative price risk</td></tr>
  </table>
</aside>

## Why spread options exist

Many businesses have profits that depend on spreads, not absolute prices. A crude-to-gasoline spread reflects refining margins. A stock-index-to-bond spread reflects relative risk appetite. A currency basis spread reflects funding costs.

For example, a power plant that burns natural gas to generate electricity profits when gas is cheap and electricity is expensive. Its P&L depends on the spread (electricity price minus gas cost), not on either price independently. A spread option on this commodity pair lets the plant hedge that specific risk.

Similarly, a bond trader who is long bonds financed at LIBOR is exposed to the spread between long rates and LIBOR. A spread option on this rate pair provides targeted hedge.

## Valuation and correlation

Spread options are harder to price than vanilla options because their payoff depends on two assets. If you assume the assets move independently, you can use [Monte Carlo simulation](/wiki/monte-carlo-options-pricing/) to price them. But if the assets are correlated, the correlation itself is a parameter in the pricing model, and correlation risk emerges.

**Correlation risk** is often underestimated. If you price a spread option assuming 50% correlation between two stock prices, but correlation jumps to 80% during a crisis, the option's value can move sharply. This is why many traders treat spread options as "low probability of ever using" hedges—they're purchased as insurance against tail events.

## Spread options in commodities

Spread options are common in commodities. Energy spreads (crude to heating oil, crude to gasoline) are widely traded. Agricultural spreads (corn to soy, corn to wheat) are liquid. Metal spreads (copper to iron ore) are used for hedging.

The liquidity varies. Crude-to-product spreads are fairly liquid (many oil refiners hedge). Agricultural spreads are decent but less liquid than commodity futures. Exotic spreads (two small-cap commodities) might have no liquid options market.

## Spread options in financial markets

In foreign exchange, spread options are used to hedge basis risk: the difference between spot and forward rates, or between two currency pairs. A currency trader might buy a spread call to hedge a funding mismatch.

In equities, spread options can hedge sector spreads, market-neutral long-short exposures, or correlation risk. A long-short equity fund might buy a spread option to hedge the spread between long and short positions.

## Compared to calendar spreads and other multi-leg strategies

A **calendar spread** (sell near-term, buy long-term options) is a different concept: both legs reference the same underlying but different expirations. A **spread option** is a single option whose payoff is defined on two underlyings.

They serve different purposes. Calendar spreads capture time decay differences. Spread options capture relative price movements.

<div class="wiki-hatnote">For options on a single underlying, see <a href="/wiki/vanilla-option/">vanilla options</a>. For multi-leg strategies, see <a href="/wiki/call-spread/">call spreads</a> or <a href="/wiki/iron-condor/">iron condors</a>.</div>

## Risks and limitations

Spread options have several risks:

1. **Basis risk**: The hedge is imperfect if the two underlyings don't move in lockstep.
2. **Correlation risk**: If correlation changes, the option's value changes unexpectedly.
3. **Model risk**: Valuation depends on assumptions (distribution, correlation, volatility) that may not hold.
4. **Counterparty risk**: Spread options are OTC, so you're exposed to the dealer's credit.
5. **Liquidity risk**: If you need to exit early, bid-ask spreads can be 5–10% of the option value.

Most professional hedgers treat spread options as long-term hedges they don't intend to sell. Buying early exit or dynamic rebalancing is usually not feasible.

## When spread options disappoint

If the spread stays stable, the spread option loses its entire premium like any out-of-the-money option. But unlike vanilla options, which are easier to price and understand, spread options often involve complicated correlations that are hard to estimate.

A refiner might buy a crude-to-gasoline spread put expecting margin compression. But if gasoline rallies along with crude (correlation near 1), the spread stays wide and the put expires worthless. The refiner paid for protection they didn't need.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/call-option/">Call option</a> — single-underlying reference.</li>
  <li><a href="/wiki/put-option/">Put option</a> — single-underlying reference.</li>
  <li><a href="/wiki/basket-option/">Basket option</a> — payoff depends on multiple underlyings.</li>
  <li><a href="/wiki/exchange-option/">Exchange option</a> — close relative, payoff on price difference.</li>
  <li><a href="/wiki/implied-volatility/">Implied volatility</a> — affects spread option pricing.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational concept.</li>
  <li>Derivatives — asset class overview.</li>
  <li><a href="/wiki/monte-carlo-options-pricing/">Monte Carlo options pricing</a> — common valuation method.</li>
</ul>
</div>
