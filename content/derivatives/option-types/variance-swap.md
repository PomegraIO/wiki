---
title: "Variance Swap"
description: "A derivative that exchanges actual realized volatility for an agreed-upon volatility level, used to trade volatility itself as an asset."
---

*A variance swap is an over-the-counter derivative where one party pays fixed implied volatility and receives realized volatility. It's a pure volatility bet: you profit if actual price swings exceed expectations, regardless of price direction.*

## How variance swaps work

In a variance swap, two parties agree on a "strike volatility" at inception. Over the contract's life, actual volatility is calculated from daily price changes. At maturity, if actual volatility exceeds strike volatility, the long variance position pays the difference × notional volatility amount. If actual volatility is lower, the long variance position receives payment.

For example, you might agree to a variance swap with a strike of 20% volatility on a stock with $1 million notional volatility. If actual realized volatility is 25%, you pay 5% × (notional) = an amount dependent on vega notional. The payoff is purely volatility-based: the stock could rally 30% or fall 15%; if actual volatility was 25%, you owe money.

Variance swaps are "variance" because they depend on the square of returns (variance), not the returns themselves. This gives them unique convexity: they become more profitable when volatility spikes and losses accelerate when volatility collapses.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Variance Swap — key facts</div>
  <table>
    <tr><th>Type</th><td>Pure volatility derivative</td></tr>
    <tr><th>Payoff</th><td>Notional × (Realized variance − Strike variance)</td></tr>
    <tr><th>Risk</th><td>Directional (realized volatility), not directional in price</td></tr>
    <tr><th>Liquidity</th><td>OTC; moderate liquidity on major indexes</td></tr>
    <tr><th>Typical notional</th><td>Often $100K to $10M vega notional</td></tr>
    <tr><th>Typical use</th><td>Trading volatility; hedging event risk</td></tr>
  </table>
</aside>

## Why trade variance swaps

Variance swaps appeal to volatility specialists: traders who believe implied volatility is mispriced relative to future realized volatility. If implied volatility is 20% but you expect realized volatility to be 30%, you're long the variance swap (paying strike, receiving realized).

Professionals also use them to hedge volatility. A long volatility position (long straddles, long calls) loses value if realized volatility falls below implied. A long variance swap offsets some of that loss because variance swaps gain value as volatility increases.

Variance swaps are also more efficient than buying options. Instead of buying many call and put options across multiple strikes (to create a synthetic volatility position), you can buy one variance swap with defined notional. The cost is lower and the exposure is cleaner.

On major indexes like the [S&P 500](/wiki/sp-500-index/), variance swaps are commonly traded because realized and implied volatility often diverge. The VIX (implied volatility index) might be 20, but traders might expect realized volatility to be 25. They can trade that view via variance swaps.

## Realized vs. implied volatility

**Implied volatility** is the market's expectation of future volatility, reflected in option prices. The VIX, for example, is the implied volatility of S&P 500 index options.

**Realized volatility** is the actual volatility that occurred, calculated from historical returns. It's the standard deviation of daily returns over the swap's lifetime.

Variance swaps directly bet on the gap. If implied is 20% and realized is 25%, long variance profitable. If implied is 20% and realized is 15%, long variance loses.

This gap can persist for months or years. During calm markets, realized volatility tends to fall below implied (because option sellers have priced in uncertainty that doesn't materialize). During crises, realized spikes above implied (because fear overwhelms models).

<div class="wiki-hatnote">For traded volatility indexes, see <a href="/wiki/implied-volatility/">implied volatility</a>. For volatility products, see <a href="/wiki/volatility-swap/">volatility swaps</a>.</div>

## Variance swap vs. volatility swap

Variance swaps pay based on variance (σ²). **Volatility swaps** pay based on volatility (σ). The difference is subtle but important:

- A variance swap is convex: it pays based on σ², so volatility spikes create outsized payoffs.
- A volatility swap is linear: it pays based on σ directly.

Variance swaps are riskier and more valuable when volatility is expected to be volatile. Volatility swaps are more stable.

Most traders refer to both as "variance swaps" colloquially, but the distinction matters for pricing and risk.

## Valuation and Greeks

Variance swaps are priced using the [volatility smile](/wiki/volatility-smile/) and skew. A fair variance strike is computed by integrating option prices across all strikes:

Strike variance = (2 / T) × integral of [OTM call prices / strike²] + [OTM put prices / strike²]

This shows that variance swaps are related to options but are not simple options themselves. The strike is implicit in the options market, not directly quoted.

Variance swaps have one primary Greek: **vega**, which measures sensitivity to changes in implied volatility. A long variance swap gains value if implied volatility increases.

## Risks and constraints

Variance swaps have several risks:

1. **Realized volatility risk**: If realized volatility comes in lower than strike, you lose money.
2. **Event risk**: A gap (sudden price jump) contributes outsized variance and can create losses.
3. **Liquidity risk**: Variance swaps are OTC; exiting early can be difficult and costly.
4. **Counterparty risk**: The dealer can default; there's no exchange clearing.
5. **Model risk**: Fair variance strikes depend on option market models; mispricing is possible.

The biggest constraint is leverage. A variance swap on $1 million vega notional might require $100K–$500K margin, and if volatility spikes, margin calls can cascade.

## Institutional use

Asset managers use variance swaps to:

1. **Hedge volatility risk**: A long equity position loses value when volatility spikes (flight to safety). A long variance swap gains value, offsetting some loss.
2. **Trade volatility views**: A fund might be bullish on equities but bearish on realized volatility, so it goes long equities and long variance to express both views.
3. **Reduce tail risk**: Buying variance swaps is insurance against volatility spikes, similar to buying puts.

Hedge funds also run systematic variance trading strategies: buying variance when implied is high and selling when implied is low, capturing the volatility risk premium.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/volatility-swap/">Volatility swap</a> — linear version of variance swap.</li>
  <li><a href="/wiki/implied-volatility/">Implied volatility</a> — strike of the variance swap.</li>
  <li><a href="/wiki/straddle/">Straddle</a> — options strategy for volatility betting.</li>
  <li><a href="/wiki/vega/">Vega</a> — Greeks sensitivity to volatility.</li>
  <li><a href="/wiki/volatility-smile/">Volatility smile</a> — shapes variance swap strikes.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/derivatives/">Derivatives</a> — asset class overview.</li>
  <li><a href="/wiki/option/">Option</a> — related vanilla contract.</li>
  <li><a href="/wiki/swap/">Swap</a> — the broader swap framework.</li>
</ul>
</div>
