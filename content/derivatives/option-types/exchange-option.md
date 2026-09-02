---
title: "Exchange Option"
description: "An option that gives the holder the right to exchange one asset for another at a predetermined ratio or price."
---

*An exchange option is a derivative where the holder can swap one asset for another. For example, the right to exchange your stock in Company A for stock in Company B at a fixed ratio. It's useful in M&A, corporate restructurings, and relative value trades.*

## How exchange options work

An exchange option is also called an "option to exchange" or "swap option" in some contexts. The payoff is the difference between the value of the asset you receive and the value of the asset you give up, if positive.

For example, a call to exchange Microsoft for Apple at a 1:1 ratio. If Microsoft is worth $400 and Apple is worth $225, the option is worth zero (you wouldn't exchange). If Apple rallies to $450, the option is worth $50 (you exchange $400 of Microsoft for $450 of Apple).

More formally: payoff = max(Value of asset to receive − Value of asset to give × ratio, 0).

Exchange options are common in merger agreements. A target's shareholders might receive a fixed amount of acquirer stock (a cash-like deal) or a floating amount depending on the acquirer's stock price at closing. An exchange option captures that asymmetry: shareholders receive the upside if the acquirer rallies, but keep a floor if it declines.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Exchange Option — key facts</div>
  <table>
    <tr><th>Type</th><td>Exotic option on two assets</td></tr>
    <tr><th>Payoff</th><td>max(Asset A − Asset B × ratio, 0)</td></tr>
    <tr><th>Risk</th><td>Delta on both legs; correlation risk</td></tr>
    <tr><th>Liquidity</th><td>OTC; illiquid; typical in M&A</td></tr>
    <tr><th>Valuation</th><td>Requires correlation between assets</td></tr>
    <tr><th>Typical use</th><td>M&A deals, equity swaps, relative value hedges</td></tr>
  </table>
</aside>

## Why exchange options appear in M&A

In an all-stock merger, the target's shareholders receive a fixed number of acquirer shares per target share. This is economically equivalent to an exchange option.

Suppose Target shareholders get 1.5 Acquirer shares each. If Acquirer rallies from $100 to $120, Target shareholders gain (1.5 × 120 = $180 per target share). If Acquirer declines to $80, they receive only $120. They have upside but capped downside (no, actually, downside risk equals the decline in Acquirer stock).

Sometimes the deal includes a collar: Target shareholders get 1.5 Acquirer shares, but if Acquirer's stock declines below $95 or rallies above $110, the exchange ratio adjusts. This is equivalent to owning an exchange call spread.

## Valuation of exchange options

Exchange options are priced using the same methods as [spread options](/wiki/spread-option/): Monte Carlo simulation or closed-form models that assume log-normal asset distributions.

The key input is correlation between the two assets. If the two assets are highly correlated (both respond to the same market factors), the option is cheaper—the probability of a large payoff is low because they move together. If uncorrelated, the option is more expensive.

For example, an exchange option to swap General Electric for Berkshire Hathaway would be cheaper than an exchange option to swap GE for a healthcare stock, because GE and Berkshire are both industrials and move together more tightly.

## Exchange options in equity derivatives

Beyond M&A, exchange options appear in:

1. **Outperformance options**: An option to exchange one stock for another plus a fixed amount. Example: "Receive Apple if it outperforms the S&P 500 by more than 5%."
2. **Relative value trades**: A fund might buy an exchange option to swap an underperforming stock for an outperforming one if certain conditions are met.
3. **Corporate actions**: A company might offer shareholders an exchange option: receive new shares of a spinoff in exchange for old shares of the parent.

## Compared to spread options

**Spread options** have a payoff based on the difference between two prices: max(S1 − S2 − K, 0). **Exchange options** have a payoff based on the difference with a ratio: max(S1 − S2 × ratio, 0). If ratio = 1, they're equivalent. But exchange options allow flexible ratios.

They both depend on correlation, both are OTC, and both are used for relative value hedging.

<div class="wiki-hatnote">For spread options, see <a href="/wiki/spread-option/">spread options</a>. For multi-asset options, see <a href="/wiki/basket-option/">basket options</a>.</div>

## Risks and limitations

Exchange options face the same risks as spread options:

1. **Correlation risk**: Correlation between the two assets can change, affecting the option's value.
2. **Model risk**: Valuation assumes log-normal distributions, which may not hold in stress scenarios.
3. **Counterparty risk**: OTC trades expose you to the dealer's credit.
4. **Liquidity risk**: No secondary market; you typically hold to maturity.
5. **Basis risk**: The option is only as good as a hedge if the two assets are tightly linked (which they may not be).

## Legal and tax considerations

Exchange options in M&A agreements are complex legal documents. Terms like "adjustment for changes in Acquirer's capital structure," "anti-dilution provisions," and "walk-away conditions" are negotiated heavily. An exchange option that seems straightforward at signing can become contentious if corporate actions (dividends, splits, spinoffs) occur.

In some tax jurisdictions, exchange options in M&A are treated as constructive sales, triggering tax recognition. Shareholders should consult tax advisors before accepting exchange options in deals.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/spread-option/">Spread option</a> — similar but with fixed strike, not ratio.</li>
  <li><a href="/wiki/basket-option/">Basket option</a> — payoff on a basket of multiple assets.</li>
  <li><a href="/wiki/call-option/">Call option</a> — single-asset reference.</li>
  <li><a href="/wiki/put-option/">Put option</a> — single-asset downside reference.</li>
  <li><a href="/wiki/merger/">Merger</a> — where exchange options commonly appear.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational concept.</li>
  <li>Derivatives — asset class overview.</li>
  <li><a href="/wiki/monte-carlo-options-pricing/">Monte Carlo options pricing</a> — valuation method.</li>
</ul>
</div>
