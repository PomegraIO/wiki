---
title: "FX Digital Option"
description: "A binary currency option that pays a fixed lump sum if the exchange rate ends above or below a strike, or nothing if it doesn't."
keywords:
  - digital option
  - binary option
  - cash-or-nothing
  - asset-or-nothing
  - forex derivative
  - exotic option
  - discontinuous payoff
image: "/svg/forex.svg"
---

*A **digital option** (also called a **binary option**) is an [option](/option/) with a stark all-or-nothing payoff: if the spot exchange rate closes above (or below) a strike at expiry, the holder receives a pre-set amount of cash—perhaps $100,000—or nothing. Unlike standard [call](/call-option/) and [put](/put-option/) options, which pay the intrinsic difference, digital options pay a fixed sum, creating a discontinuous and dealer-hostile payoff that demands sophisticated hedging.*

## Two payoff structures: cash-or-nothing and asset-or-nothing

The most common form is a **cash-or-nothing** digital. An EUR/USD digital call struck at 1.10 with a $100,000 notional pays $100,000 if spot closes above 1.10 at expiry, or $0 if it closes at or below. No gradation—a close at 1.101 pays the full amount, the same as a close at 1.20. The optionality lies only in whether the barrier is breached. The premium reflects the probability of finishing in-the-money and the fixed payoff.

An **asset-or-nothing** digital takes the form of an even bet: if the option finishes in-the-money, the holder receives the asset itself—one unit of the foreign currency, typically. An asset-or-nothing EUR call struck at 1.10 pays 1 EUR if spot closes above 1.10, or nothing otherwise. The EUR has a varying value, so the payoff is less deterministic than cash-or-nothing, but the logic is identical: binary outcome, fixed if-in quantity.

Both types are structured as options, meaning the buyer pays an upfront premium that is far smaller than the potential payoff. A digital call with a 50% implied probability of finishing in-the-money and a $100,000 payout might trade for $40,000–$45,000 (accounting for [time-decay-theta](/time-decay-theta/) and the dealer's edge). That leverage—$40k premium for a $100k potential payout—is what attracts speculators and justifies the term "binary option" in popular usage.

## The hedging nightmare: discontinuous delta

Standard options have smooth, well-behaved [delta](/delta/) that increases gradually as spot moves in-the-money. A vanilla call becomes more valuable as spot rises, and its delta increases from near zero to near one as spot goes deeper in-the-money. Hedging is tractable: you sell underlying to offset your exposure.

Digital options have a delta that is nearly zero far away from the strike and then spikes to infinity (or discontinuity) at the strike itself. This discontinuity is the dealer's Achilles heel. A dealer short a digital call at 1.10 is essentially unhedged as long as spot is below, say, 1.08. But as spot approaches 1.10, the dealer's delta accelerates toward infinity—the dealer must suddenly hedge a huge amount of EUR exposure just before expiry. If spot closes at 1.0999, the delta collapses back to zero and the dealer has over-hedged, realizing a loss. If spot closes at 1.1001, the dealer has under-hedged catastrophically.

This discontinuous behaviour is hedged in practice by dealers selling further options at tighter strikes to create a replicating portfolio. To sell a digital call at 1.10 for $100,000, a dealer might sell a call spread: buy a vanilla call at 1.10 and sell a vanilla call at 1.101, then adjust the quantities so the spread replicates the digital's payoff. This replicating strategy works but ties up capital and introduces model risk—if the vanilla option markets gap or dislocate, the hedge breaks.

## Vega and volatility sensitivity

Digital options are exquisitely sensitive to [implied-volatility](/implied-volatility/). A digital call struck at-the-money (spot = strike) is at maximum [vega](/vega/) sensitivity; a small rise in volatility can swing the value significantly. A digital call struck well out-of-the-money but with spot still relatively close has negative vega—higher volatility makes the out-of-the-money outcome less likely on an expected-value basis. This vega risk is hard to hedge because the vanilla option market's vega varies smoothly with strike, while the digital's vega is concentration-based.

Dealers hedge vega by trading volatility swaps or selling variance products, but the leverage involved means digital options are capital-intensive to warehouse. A dealer might require a wider [bid-ask-spread](/bid-ask-spread/) on digitals than on vanillas to compensate for the hedging burden.

## Speculative and illicit uses

Digital options became notorious in retail markets during the 2010s. Platforms marketed them as short-duration, high-probability bets—"will EUR/USD close above 1.10 in one hour?"—essentially gambling on currency movements. Retail traders were often not educated on the odds and leverage; outcomes matched a casino more than a hedging instrument. Many regulatory jurisdictions have since banned or heavily restricted binary options for retail clients. Institutional trading of digitals continues over-the-counter, where both counterparties understand the discontinuous payoff and hedging costs.

## Replication and variance swaps

A digital call can be thought of as the limit of a call spread: buy a call at strike K, sell a call at K + dK, and let dK approach zero. The spread pays the intrinsic difference, capped at dK. In the limit, the payoff is one unit if spot > K, and zero otherwise. Dealers exploit this by constructing call spreads to replicate digitals. Conversely, digitals can be unbundled: a digital can be broken into a portfolio of vanilla options at progressively tighter strikes, mimicking the discontinuity.

Advanced pricing ties digital options to the variance of the spot rate. A digital call's value is related to the cumulative probability of the spot exceeding the strike, adjusted for the time-value of volatility. If [volatility-smile](/volatility-smile/) is steep—out-of-the-money options are priced at much higher implied volatility than at-the-money—a digital call's fair value shifts because the tail probability changes.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundation for all digital structures
- [Call Option](/call-option/) — a digital call pays a fixed sum if in-the-money
- [Put Option](/put-option/) — digital puts mirror the call logic with downside triggers
- [Delta](/delta/) — discontinuous and extreme for digital options near the strike
- [Vega](/vega/) — critical sensitivity factor for out-of-the-money digitals
- [Theta](/theta/) — time decay accelerates as expiry approaches for at-the-money digitals
- [Implied Volatility](/implied-volatility/) — drives digital pricing and replicating hedge costs

### Wider context

- Forex — the currency market where digitals are traded
- Exotic Option — digitals are a canonical exotic structure
- [Volatility Smile](/volatility-smile/) — empirical vol distribution across strikes affects digital value
- [Option Premium](/option-premium/) — the fixed upfront cost for the binary payoff
- [Over-the-Counter Market](/over-the-counter-market/) — where institutional digital trading occurs

</div>
