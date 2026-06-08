---
title: "FX Butterfly Spread: Strategy and Mechanics"
description: "An FX butterfly spread uses long-dated options at the wings and short-dated at the body to trade limited spot movement or convexity at low cost."
keywords:
  - fx butterfly spread options strategy
  - butterfly spread forex
  - options butterfly structure
  - limited-range trading
  - convexity trading
  - currency options strategy
image: /svg/forex.svg
---

*An **FX butterfly spread** is an [options](/option/) strategy that combines two [call options](/call-option/) or two [put options](/put-option/) at outer strikes with one short option at the center strike, structured so that profit is realized if the spot [exchange rate](/spot-exchange-rate/) stays within a narrow band at expiration. The butterfly is cheap to establish (limited or zero upfront cost) and offers defined risk, making it popular for trading minor currency pairs or positioning for expected range-bound consolidation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Butterfly Spread — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex." />

<div class="wiki-infobox-caption">Long wings, short body; profits in the middle when spot is capped.</div>

|   |   |
|---|---|
| **Structure** | Long ATM call + Long OTM call + Short 2× ITM call (or puts) |
| **Cost** | Low or zero; short strike premium helps fund long strikes |
| **Max profit** | Width of one wing (e.g., $0.005 per unit) realized if spot ends at body strike |
| **Max loss** | Net debit paid upfront; usually 20–50% of max profit |
| **Profit zone** | Narrow band around body strike (e.g., EUR/USD 1.08–1.10) |
| **Expiration focus** | Profits depend on spot being within range at expiration, not before |
| **Vega exposure** | Short: butterfly benefits from declining [volatility](/implied-volatility/) |

</aside>

## The Butterfly Structure Explained

A standard FX butterfly spread is constructed with three strikes. Imagine trading EUR/USD spot at 1.0900:

- **Long call** at 1.0850 (out of the money, OTM; "wing")
- **Short two calls** at 1.0900 (at the money, ATM; "body")
- **Long call** at 1.0950 (OTM; other "wing")

The strikes are equally spaced (50 pips apart). You buy one call at the lower strike, sell two at the middle strike, and buy one at the upper strike. The width of each wing is 50 pips; the butterfly "span" is 100 pips.

Let's say the lower call (1.0850) costs $0.0030 per unit, the middle call (1.0900) costs $0.0050 per unit, and the upper call (1.0950) costs $0.0020 per unit. 

Cost: Buy 1.0850 call ($0.0030) + Buy 1.0950 call ($0.0020) − Short 2 × 1.0900 call ($0.0050 × 2) = $0.0050 − $0.0100 = −$0.0050. You receive $0.0050 per unit. A butterfly that receives money upfront is a credit butterfly; one where you pay a small debit is a debit butterfly. Either way, the cost is far lower than buying outright calls.

## How Payoff Works at Expiration

The butterfly's payoff diagram is the source of its name: a hump of profit in the middle.

**Scenario 1: Spot finishes at 1.0900 (body strike).**

- Long 1.0850 call: in-the-money by 50 pips, worth $0.005 per unit. Profit: $0.005 − $0.003 cost = $0.002.
- Short 2 × 1.0900 call: at-the-money, worth $0.00 each. Profit: $0.00 − 2 × $0.005 received = $0.00 (net).
- Long 1.0950 call: out-of-the-money, worthless. Loss: $0.00 − $0.002 cost = −$0.002.

Wait—let me recalculate more carefully. If spot finishes at 1.0900:
- Long 1.0850 call: worth $0.0050. You paid $0.0030, so profit is $0.0020.
- Short 1.0900 calls (×2): worth $0.00 each (ATM). You received $0.0050 × 2 = $0.0100, so you owe back $0.00. Profit on short is $0.0100.
- Long 1.0950 call: worth $0.00. You paid $0.0020, so loss is $0.0020.

Total: $0.0020 + $0.0100 − $0.0020 = $0.0100 net.

But wait—we received a net credit of $0.0050 upfront, so our max profit is higher. Let me re-examine the math:

Actually, the cleaner way: the butterfly's payoff at expiration is:

- If spot < 1.0850: all options expire worthless. Profit = net credit received upfront (if any) = $0.0050 per unit. Max loss capped.
- If spot is between 1.0850 and 1.0900: the lower wing is ITM, the short calls are ITM, the upper wing is OTM. Payoff rises.
- If spot = 1.0900: max profit, which is the width of one wing. Here, the width is 50 pips, so max profit is $0.0050 per unit.
- If spot is between 1.0900 and 1.0950: payoff declines symmetrically.
- If spot > 1.0950: all long calls are ITM, short calls (×2) are ITM; the short calls' larger size dominates, and payoff is negative. Max loss = (width of wing) − (net credit received) = $0.0050 − $0.0050 = $0.00.

If you *paid* a net debit to enter, the max loss equals that debit; max profit is reduced.

## Who Trades FX Butterflies and When

Traders use FX butterflies in several scenarios:

**Range-bound consolidation.** If analysis suggests EUR/USD will trade sideways (e.g., 1.0850–1.0950 over the next month), a butterfly defined by that range caps upside and downside losses while profiting if spot stays in the band. The trader is effectively saying, "I don't know direction, but I expect confinement."

**Volatility compression.** If implied [volatility](/implied-volatility/) is expected to fall after an event (central bank decision, data release), the butterfly, being short premium (short the two body calls), benefits from theta decay and vega decay. The butterfly becomes more profitable as volatility compresses.

**Cost-effective speculation.** Buying outright calls or puts on a minor currency pair (e.g., NZD/USD) is expensive because the pair is less liquid. A butterfly achieves similar directional exposure (if you tilt one wing wider than the other, it becomes mildly bullish or bearish) at far lower cost.

**Hedging a position.** A portfolio manager long GBP/USD is worried about a 2% downside but also worried the upside may be capped. A butterfly defined by the expected range allows profit if spot stays in that band and limits losses if it breaks out.

## Butterfly Variants: Skewed Butterflies

The textbook butterfly has equal wing widths (symmetric). A **skewed butterfly** shortens one wing (e.g., 30 pips) and lengthens the other (80 pips), biasing profit toward one direction.

A bullish skewed butterfly might have:
- Long call at 1.0850 (lower wing, 50 pips wide)
- Short 2 calls at 1.0900
- Long call at 1.0930 (upper wing, 30 pips wide)

This creates an asymmetric payoff: more profitable if spot finishes between 1.0900 and 1.0930 (slight bullish tilt) and takes less loss if spot drops. The trade-off is tighter profit zone and lower max profit in the upper region.

## Greeks and Risk Management

The butterfly is **net short vega**: the body (short calls) has higher vega than the wings (long calls), so if [implied volatility](/implied-volatility/) rises, the position loses money. This is a feature if you expect volatility to fall, a bug if volatility spikes.

The butterfly is **net long theta**: the decay of the short calls (body) benefits the position daily, while the long wings (which benefit from theta) are outweighed. The butterfly decays favorably as expiration approaches, assuming spot stays near the body strike.

[Delta](//) shifts gradually. Near the body strike, delta is near zero (the position is direction-neutral). Far from the body, delta approaches the wings' delta or becomes negative if spot overshoots.

Risk management involves monitoring:
- **Spot move beyond wings.** If spot exits the band, losses begin to accelerate. A stop-loss above the upper wing or below the lower wing is typical.
- **Volatility surge.** A spike in implied volatility can turn a profitable butterfly into a loss even if spot stays in range, because short vega dominates.
- **Time decay with spot movement.** As expiration nears, theta decay accelerates, but if spot drifts toward a wing, gamma (convexity) accelerates losses.

## Butterfly vs. Other Spreads

A **straddle** (long a call and a put at the same strike) profits from large moves in either direction; a butterfly profits from no move. Butterflies are cheaper to establish than straddles.

A **strangle** (long a call and a put at different, wider strikes) is similar to a straddle but farther OTM; it is even cheaper but requires a larger move to profit.

A **call spread** (long one call, short another at a higher strike) is directional and less expensive than a naked call. A butterfly is the next step: three strikes, neutral, and very cheap or even a credit.

## Practical Execution Notes

In FX options markets, butterflies are quoted by the width of the wings and the body strike. A trader might say, "I am a 25-pip butterfly on EUR/USD at 1.0900"—meaning long 1.0875, short 2 × 1.0900, long 1.0925.

Execution in thinly traded pairs (e.g., MXN/USD) can be challenging because bid-ask spreads on individual strikes widen, and the net cost of the butterfly can deteriorate. Traders in major pairs (EUR/USD, GBP/USD) often get tight prices.

Butterfly spreads are also available on [currency futures](/futures-contract/) and FX-linked structured products, allowing firms without direct OTC options access to participate.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — foundational call and put mechanics
- [Call Option](/call-option/) — the legs of the butterfly
- [Put Option](/put-option/) — butterfly can also be constructed with puts
- [Implied Volatility](/implied-volatility/) — crucial to butterfly pricing and P&L
- [Spot Exchange Rate](/spot-exchange-rate/) — the underlying that the butterfly constrains
- [Strike Price](/strike-price/) — the three strikes define the butterfly shape

### Wider context

- [Currency Risk](/currency-risk/) — what FX derivatives hedge
- [Derivatives, Hedging](/derivatives-hedging/) — the broader class of risk-management tools
- [Option Premium](/option-premium/) — what the butterfly aims to harvest via short vega
- [Carry Trade](/carry-trade/) — alternative FX strategy focusing on yield, not volatility

</div>
