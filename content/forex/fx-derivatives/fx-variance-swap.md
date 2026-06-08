---
title: "FX Variance Swap"
description: "An OTC derivative that transfers realised FX volatility risk from one party to another, settling on the difference between realised and implied variance."
keywords:
  - variance swap
  - fx volatility
  - otc derivatives
  - volatility trading
  - realised variance
image: /svg/forex.svg
---

*A **variance swap** is an over-the-counter derivative contract in which one counterparty agrees to pay a fixed notional amount times the difference between realised and implied variance of an FX rate, measured over a set period. The buyer pays the strike (implied variance) upfront; if spot volatility runs higher than the fixed strike, the buyer profits. Unlike straddles or options, variance swaps offer pure exposure to realised volatility with no directional drift risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Variance Swap — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for FX instruments." />

<div class="wiki-infobox-caption">Pure volatility exposure settled on realised variance over the swap tenor.</div>

|   |   |
|---|---|
| **What it is** | OTC contract transferring realised volatility risk |
| **Payoff driver** | Realised variance minus variance strike |
| **Settlement** | Cash, typically at expiry; quarterly or at maturity |
| **Notional** | On variance points, not spot levels |
| **Volatility measure** | Usually daily close-to-close log returns, squared and annualised |
| **Typical tenor** | 3 months to 2 years |
| **Counterparty** | Banks, hedge funds, corporate treasury desk |

</aside>

## Mechanics and settlement

The variance strike (the fixed rate paid by the buyer) is quoted at deal time, usually in units of "variance points"—essentially annualised variance expressed as a percentage squared. For example, a strike of 8 per cent means 0.08 annualised. Once the swap is live, both sides mark the contract daily based on spot movements; the bank samples the exchange rate (often the daily close or midpoint) and accumulates squared daily returns.

At expiry—or on scheduled reset dates for longer trades—the realised variance is computed from the path of daily log returns, annualised and squared. The buyer then receives (or pays) the difference:

**Payoff = Vega notional × (Realised variance − Strike)**

A vega notional scales the profit or loss; for instance, a €1 million vega notional with 2 percentage points of realised variance above strike yields a €20,000 profit to the long buyer. This design offers [linear exposure](/equity-etf/) to volatility itself, independent of spot drift.

## Why use them

Variance swaps sidestep the gamma and theta costs embedded in options. A [straddle](/option/) or risk reversal on an FX pair profits (or loses) not only from volatility moves but also from time decay and directional gamma. A variance swap isolates realised volatility: if an investor believes spot will bounce around (either up or down), but is agnostic on direction, variance swaps offer cleaner execution than buying multiple option strikes.

Banks use them to hedge customer option flow. When a corporate client buys a large [FX call option](/option/), the bank becomes long gamma and short vega. Selling variance swaps against that book locks in the volatility hedge cost, separating the directional hedge (via forwards or spot trading) from the volatility risk.

## Pricing and the volatility smile

The strike is set using the implied variance derived from the [Black-Scholes model](/black-scholes-model/) or similar frameworks, averaged across strikes and expiries. However, currency markets exhibit a volatility smile: implied variance is higher for far out-of-the-money (OTM) and at-the-money (ATM) options, and lower for slightly in-the-money legs. A variance swap strike that ignores this smile and uses only ATM volatility will be systematically mis-priced relative to a model that accounts for the full smile.

Market makers typically adjust the strike upward to compensate for the [convexity](/call-option/) of the smile—a skew adjustment. The more pronounced the smile, the higher the variance swap strike quoted to the buyer.

## Realisation and mark-to-market

During the life of the swap, realised variance is typically recomputed and compared to the running variance swap strike. Banks mark positions daily using either realised variance accumulated to date or implied variance from the market term structure of volatility. A trader long a variance swap will see profit if spot bounces more than expected, even if spot ends the period flat.

One critical detail: the choice of sampling frequency (daily close, intra-day high-low, or continuous) and the treatment of overnight gaps can materially shift realised variance. Conventions in FX are generally standardised around daily close-to-close log returns, but terms should always be specified in the term sheet.

## Risk and counterparty considerations

Variance swaps are pure OTC products, so [counterparty risk](/counterparty-risk/) is substantial. The buyer is exposed to the seller's default before payoff is settled. Major dealers like JPMorgan, Goldman Sachs, and regional FX specialists are primary liquidity providers; entering a variance swap with a weaker counterparty commands a [credit spread](/credit-spread/) premium.

Realised variance can spike sharply on large spot moves or overnight data releases. A currency that is calm for months can gap 2–3 per cent on a central bank announcement, instantly inflating realised variance and shifting the mark against the short position. Unlike short options, there is no natural gamma hedge; hedging variance swap short positions is complex and often done through dynamic delta hedging or buying ATM straddles.

Liquidity in FX variance swaps is concentrated in the major currency pairs—EUR/USD, USD/JPY, GBP/USD—and even there, the market is thin compared to options. Bid-ask spreads can be 0.5–2 per cent of the strike on liquid tenors, wider on exotics.

## Applications and market participants

Volatility hedge funds and quantitative traders actively trade variance swaps to exploit perceived mispricings between realised and implied volatility. A fund that expects spot to remain calm longer than markets price in will sell variance swaps (receive the fixed strike, benefit if realised comes in below).

Corporate treasurers sometimes buy variance swaps to cap volatility costs during extended periods of balance-sheet translation exposure. Insurance companies and other long-gamma investors use them to monetise expected tranquility.

The variance swap market is also a testing ground for newer pricing models that account for [jumps](/equity-etf/), stochastic volatility, and term-structure dynamics. Simple Black-Scholes pricing has given way to approaches like Heston or local-volatility models that better capture the behaviour of realised variance under stress.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — derivative contract giving the right but not obligation to buy or sell at a fixed price
- [Volatility Smile](/equity-etf/) — pattern of implied volatility varying across strikes
- [Black-Scholes Model](/black-scholes-model/) — foundational framework for pricing European options
- [Straddle](/option/) — simultaneous long call and put at the same strike, long volatility
- [Risk Reversal](/equity-etf/) — paired call and put positions offsetting direction while trading volatility skew
- [Vanna-Volga Pricing](/vanna-volga-pricing/) — market-standard adjustment for volatility smile in FX options
- [FX Forward Extra](/fx-forward-extra/) — structured product combining forward with embedded optionality
- [Counterparty Risk](/counterparty-risk/) — risk that a derivatives counterparty defaults before settlement

### Wider context

- [Currency Volatility](/currency-volatility/) — fluctuations in FX spot rates
- [Currency Risk](/currency-risk/) — exposure to adverse FX movements
- [Over-the-Counter Market](/over-the-counter-market/) — decentralised derivatives trading between counterparties
- [Interest Rate Risk](/interest-rate-risk/) — parallel concept in fixed income
- [Price Discovery](/price-discovery/) — mechanism by which derivative prices aggregate market views

</div>
