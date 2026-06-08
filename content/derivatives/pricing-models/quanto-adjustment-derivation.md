---
title: "The Quanto Adjustment: Why Currency Correlation Affects Option Prices"
description: "Understand how quanto adjustment derivation in options accounts for correlation between the underlying asset and exchange rates when payoffs are in different currencies."
keywords:
  - quanto adjustment derivation
  - currency correlation options
  - quanto option pricing
  - foreign currency derivatives
  - exchange rate hedging
  - currency-adjusted payoff
image: "/svg/derivatives.svg"
---

*A **quanto adjustment** is a drift correction applied to option prices when the underlying asset and the option payout are denominated in different currencies. The size of the adjustment depends directly on the correlation between asset returns and exchange rates—a relationship that fundamentally alters how traders value these instruments.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Quanto Adjustment — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Currency correlation directly affects option pricing when domestic and foreign currencies diverge.</div>

|   |   |
|---|---|
| **What it is** | A drift term added to the risk-neutral rate of an underlying when pricing options in a foreign currency |
| **Why it exists** | Eliminates arbitrage when the payout currency differs from the asset currency |
| **What drives it** | Correlation between asset returns and the exchange rate |
| **Sign** | Positive when asset and currency are positively correlated; negative when negatively correlated |
| **Practical impact** | Can shift option prices by 5–20% or more in high-correlation scenarios |
| **Who applies it** | Traders pricing cross-border equity, index, and commodity options |

</aside>

## The Problem: Two Currencies, One Payoff

Suppose a U.S. investor buys a call option on a Japanese equity index. The index is denominated in yen, but the investor wants the option payout in dollars. Without hedging, the investor faces two risks: the index may fall (bad for the call), and the yen may weaken against the dollar (also bad, since the dollar payout shrinks). Conversely, if the yen strengthens, even a moderately-performing index becomes more valuable in dollar terms.

A standard [Black-Scholes-model](/black-scholes-model/) approach applies one asset volatility and one risk-free rate. But that ignores the correlation between the index and the exchange rate. If they move together, the combined risk is higher than a simple volatility adjustment captures. If they move opposite, risk is actually lower. The **quanto adjustment** explicitly models this interaction.

## Deriving the Quanto Drift Correction

Under the risk-neutral measure, the value of a forward contract on the foreign asset in domestic currency already includes a quanto drift. Start with two assets in their own currencies:

- The foreign asset price **S_f** grows at the foreign risk-free rate **r_f**.
- The spot exchange rate **X** (domestic currency per foreign currency unit) evolves with volatility **σ_x**.

The forward price of the asset in foreign currency is **S_f × exp(r_f × T)**. To convert to domestic currency, multiply by the forward exchange rate. But under the risk-neutral measure in the domestic currency, the relationship is not simply the product of the two forwards.

The key insight: apply Itô's lemma to the product **S_f × X**. The product has a drift that includes a **covariance term**:

**d(S_f × X) = (drift terms) + σ_S × σ_X × ρ(S_f, X) × S_f × X × dt**

where **ρ(S_f, X)** is the correlation between foreign asset returns and the exchange rate.

Rearranging, the risk-neutral rate applied to the foreign asset, when priced in domestic currency, is:

**r* = r_f + σ_S × σ_X × ρ(S_f, X)**

This **r* − r_f** term is the **quanto adjustment**. It is the extra drift (or drift reduction, if negative) that must be applied to option pricing formulas.

## Interpretation: Why Correlation Matters

If the foreign asset and the exchange rate are **positively correlated** (ρ > 0), the domestic investor benefits when the asset rises—the payout goes up both from the asset gain and from the currency strengthening. This extra benefit must be offset in pricing by raising the effective risk-free rate, which *lowers* call prices and *raises* put prices (the optionality is less valuable because the underlying is effectively "cheaper" on a risk-adjusted basis).

If they are **negatively correlated** (ρ < 0), the opposite occurs. When the asset rises, the currency weakens, dampening the domestic payout. This hedging-like behavior makes the option more valuable in domestic terms—the adjustment lowers the effective rate, raising call prices and lowering put prices.

If **ρ = 0** (uncorrelated), the adjustment vanishes entirely, and standard pricing applies.

## Size and Practical Examples

In liquid markets, the correlation is typically estimated from historical returns or implied from quanto [forwards](/forward-contract/) prices. A stock market index in a developed country (say, Germany) and the euro often show correlation in the range of −0.1 to +0.3 relative to the dollar. With index volatility around 15% and currency volatility around 10%, a correlation of +0.2 yields an adjustment of roughly:

**0.15 × 0.10 × 0.2 ≈ 0.003 or 30 basis points**

For a long-dated option, this can shift the effective strike or drift visibly. Commodity-linked options show much larger adjustments; a commodity priced in dollars but with a foreign-currency-denominated index—or vice versa—can exhibit correlations exceeding ±0.5, pushing adjustments above 1% of the spot rate.

## Practical Applications in Trading

Market makers pricing [quanto option](/option/) books apply this adjustment systematically. If a bank is short a euro-denominated call on an S&P 500 index (payout in euros), the quanto adjustment tells them to charge slightly less premium (because the positive correlation between the index and the dollar makes the payout less risky). Conversely, a positive correlation adjustment fattens their edge when they are long the option.

Traders also use the adjustment to detect mispricings. If a quanto forward is trading away from its no-arbitrage level, the implied correlation can be backed out. A divergence from historical or term-structure estimates may signal either a market dislocation or a shift in expected correlation—both of which drive trading decisions.

## Correlation Estimation and Model Risk

The practical challenge is estimating correlation accurately. Historical correlation can be noisy, especially over short horizons or during market stress when correlations shift. Many dealers use the implied correlation backed from quoted market prices as the "market price of correlation risk." For exotics and longer tenors, the correlation assumption can dominate [delta](/delta/) and [vega](/vega/), making the adjustment a first-order concern.

Some traders also apply a volatility smile to the correlation itself, pricing different correlation levels at different strikes or tenors. This adds a layer of complexity but better reflects the market's true risk premium for currency-linked optionality.

## Connection to Other Derivatives Adjustments

The quanto adjustment is one of several **convexity adjustments** in derivatives pricing. [Quanto swap](/swap/) rates, [equity-currency hybrids](/structured-product/), and leveraged products all use similar logic. The adjustment also appears in **variance swap** pricing when the index and currency are correlated, and in **spread option** valuation across asset classes with currency conversion.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes-Model](/black-scholes-model/) — Foundation for option pricing that the quanto adjustment modifies
- [Forward-Contract](/forward-contract/) — Currency forwards embed the quanto adjustment into their no-arbitrage price
- [Delta](/delta/) — How the adjustment affects the sensitivity of quanto options to the underlying
- [Vega](/vega/) — How currency volatility directly scales the size of the adjustment
- [Volatility-Smile](/volatility-smile/) — Correlation is often priced as part of implied vol surfaces
- [Currency-Risk](/currency-risk/) — The core economic force behind all quanto adjustments

### Wider context

- [Derivatives-Hedging](/derivatives-hedging/) — Why investors use quanto options to separate asset and currency risk
- [Option](/option/) — Broader category of tools that carry quanto adjustments
- [Structured-Product](/structured-product/) — Many exotic payoffs embed quanto logic
- [Exchange-Rate-Spot](/spot-exchange-rate/) — The underlying mechanism driving currency-correlated drift

</div>
