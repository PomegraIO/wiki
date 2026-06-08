---
title: "Quanto Option"
description: "An option on a foreign asset that settles in domestic currency at a pre-fixed exchange rate, isolating currency risk from asset risk."
keywords:
  - quanto option
  - currency hedging
  - cross-currency derivatives
  - exchange rate lock
  - foreign asset option
image: /svg/derivatives.svg
---

*A **quanto option** is an [option](/option/) on an underlying asset denominated in a foreign currency, with the twist that it pays off in the holder's domestic currency at a fixed exchange rate agreed upfront. By locking the currency conversion rate, the quanto isolates the financial risk of the asset itself from currency fluctuation risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Quanto Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and exotic contracts." />

<div class="wiki-infobox-caption">A currency-locked option on a foreign asset.</div>

|   |   |
|---|---|
| **What it is** | An [option](/option/) on a foreign-currency asset that settles in domestic currency at a pre-fixed exchange rate |
| **Also called** | Guaranteed exchange-rate option, FX-hedged option |
| **Key benefit** | Isolates asset risk from currency risk |
| **Exchange rate** | Fixed at [option](/option/) inception |
| **Parties** | Investor, option seller, foreign asset issuer |
| **Common underlying** | Foreign [stock](/stock/), [bond](/bond/), [index](/sp-500-index/) |
| **Pricing factor** | [Interest rate](/interest-rate/) differential between currencies |

</aside>

## A simple example makes it concrete

Suppose an American investor wants to buy a [call option](/call-option/) on a Japanese company's [stock](/stock/) trading in yen. The stock costs ¥10,000; the option [strike price](/strike-price/) is ¥12,000. Normally, the investor would face two risks: the stock might fall (bad for the call holder), and the yen might weaken against the dollar, making the yen proceeds worth less when converted. 

A quanto [call option](/call-option/) eliminates the second risk. The parties agree upfront that any yen payoff will convert to dollars at, say, 100 yen per dollar, no matter what the actual exchange rate is when the option expires. If the stock rallies to ¥15,000, the option is in the money by ¥3,000; the investor receives $30 in domestic currency, not whatever the spot rate happens to be. The investor profits purely on the stock's movement.

## Why currency risk matters in derivatives

[Options](/option/) on foreign assets are popular with international investors and corporations. A US fund holds European bank [stocks](/stock/); a German exporter bids on a contract priced in US dollars. Both face [currency volatility](/currency-volatility/) on top of their core business risk. 

A straight foreign [option](/option/) exposes the holder to a multiplicative risk: the underlying asset's price *and* the exchange rate both move. That compounding can obscure whether the trade is making or losing money on the asset alone. Currencies are also notoriously difficult to forecast. A quanto separates the two bets, allowing the investor to make a pure play on the asset's fundamental value.

## How the pricing works

A quanto option's [premium](/option-premium/) reflects not only the asset's volatility and [interest rate](/interest-rate/) but also the correlation between the asset and the exchange rate, plus the interest-rate [differential](/interest-rate/) between the two currencies.

This is where it gets technical. If the foreign interest rate is higher than the domestic one, the forward exchange rate is already discounted in the market—the foreign currency is expected to weaken. A quanto [call option](/call-option/) on a foreign asset must account for this drift when setting the fixed exchange rate. Set the rate too generously, and the option seller is under water; too stingily, and the buyer refuses it. Most quanto options price the exchange rate as the [forward rate](/forward-contract/) at the option's expiration, adjusted for the correlation between the asset and currency.

In practice, investment banks use [Black-Scholes](/black-scholes-model/) variants adapted for two stochastic variables (asset price and exchange rate), plus calibration to implied [volatilities](/historical-volatility/) and interest-rate markets.

## Who uses quantos and why

**Multinational corporations** hedge foreign earnings. A Japanese automaker with a US subsidiary buys quanto [puts](/put-option/) on dollar-denominated [receivables](/accounts-receivable/) to cap downside in yen terms, without betting on the currency separately.

**International asset managers** buy quanto [calls](/call-option/) on foreign [stocks](/stock/) or [bonds](/bond/) when they are bullish on the asset but indifferent or cautious on the currency. This is cleaner than buying the asset outright and then hedging currency separately.

**Emerging-market investors** use quantos to invest in high-yielding [bonds](/bond/) or [stocks](/stock/) in volatile currencies. Instead of juggling [forex](/currency-volatility/) hedges constantly, a quanto locks in the conversion rate upfront.

**Structured-product desks** embed quantos into notes and funds aimed at retail investors who want exposure to, say, a Chinese tech [index](/sp-500-index/) but think the yuan will be choppy.

## Trade-offs and costs

The convenience of a fixed exchange rate comes at a price. The option [premium](/option-premium/) is typically higher than a plain vanilla option on the same asset because the seller is taking on additional hedging and basis risk. If the asset rallies *and* the foreign currency strengthens, the option seller has locked in a losing rate.

Liquidity also matters. Quanto options are less liquid than [standard options](/option/) on major [stocks](/stock/) or [indices](/sp-500-index/). Bid-ask [spreads](/bid-ask-spread/) are wider, especially for less-traded currency pairs or exotic underlying assets. Retail investors rarely encounter them directly; they are mainly sold by investment banks to institutional clients.

There is also no free lunch on [strike price](/strike-price/) selection. Because the option is already hedging one variable (the exchange rate), the [strike](/strike-price/) on the asset itself must be set independently. Investors cannot hide in the "sweet spot" between two risks—they must make an explicit choice on where they expect the foreign asset to move.

## Variants and related structures

**Reverse quantos** flip the setup: an option on a domestic asset that pays in foreign currency. Less common, but useful for exporters or investors seeking non-dollar returns.

**Quanto spread options** and **quanto basket options** extend the idea to [spreads](/credit-spread/) between two foreign assets or to portfolios, always settling in domestic currency.

**Equity-linked quantos** embed the feature into longer-term structured notes that tie coupons or payoff to both a foreign [stock](/stock/) and an exchange rate, but with the currency component hedged away.

## The arithmetic of correlation

The correlation between an asset and its currency is crucial. If a foreign [stock](/stock/) index tends to rise when its home currency strengthens, the correlation is positive—and the quanto [call](/call-option/) seller faces more risk, because both the asset and the implied forward rate work against them. Conversely, if the stock falls when the currency rises (negative correlation), the seller has a natural offset and will charge less premium.

Investment banks monitor these correlations closely. They fluctuate with macroeconomic conditions, central-bank policy, and capital flows. In times of [financial stress](/liquidity-risk/), correlations often flip, which is precisely when hedging is most valuable—and most expensive.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational derivative contract
- [Call Option](/call-option/) — the basic bullish option type
- [Put Option](/put-option/) — the basic bearish option type
- [Forward Contract](/forward-contract/) — a simpler currency-lock agreement
- [Strike Price](/strike-price/) — the agreed price in an option contract
- [Option Premium](/option-premium/) — the upfront cost of an option
- [Currency Volatility](/currency-volatility/) — the fluctuation in exchange rates
- [Interest Rate](/interest-rate/) — affects option pricing and forward rates

### Wider context

- Derivatives — the broader class of contracts
- [Hedge Fund](/hedge-fund/) — institutions that use exotic derivatives
- [Capital Flows](/capital-flows/) — the macroeconomic driver of currency movement
- [Currency Risk](/currency-risk/) — the broader concept of exchange-rate exposure

</div>
