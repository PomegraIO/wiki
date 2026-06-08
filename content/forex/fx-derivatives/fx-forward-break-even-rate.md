---
title: "FX Forward Break-Even Rate Explained"
description: "The FX forward break-even rate is the future exchange rate at which a currency hedge neither gains nor loses. How to calculate it using interest rate parity."
keywords:
  - fx forward break even rate
  - forward exchange rate calculation
  - interest rate parity
  - currency hedge math
  - forex break even
  - forward contract valuation
---

*The **FX forward break-even rate** is the exchange rate at the [forward contract](/forward-contract/) maturity date where a hedge realizes neither a gain nor a loss relative to the [spot rate](/spot-rate/) at the time the hedge was entered. It is calculated using [interest rate parity](/interest-rate-parity/), which ties forward rates to the interest rate differential between two currencies.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Forward Break-Even Rate — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex and currencies." />

<div class="wiki-infobox-caption">The forward rate implied by interest rate parity.</div>

|   |   |
|---|---|
| **Formula** | F = S × (1 + r₂) / (1 + r₁) |
| **F** | Forward rate (domestic currency per foreign currency) |
| **S** | Spot rate today |
| **r₁** | Interest rate on domestic currency |
| **r₂** | Interest rate on foreign currency |
| **Break-even occurs at** | Forward rate = interest rate parity rate |
| **Result if actual forward < parity** | Hedging locks in a gain if spot drifts down |
| **Result if actual forward > parity** | Hedging locks in a loss if spot drifts down |

</aside>

## The Concept: No Free Lunch in Currency Markets

When you enter a [forward contract](/forward-contract/) to buy or sell currency at a future date, you are locking in an exchange rate. The **break-even rate** is the level at which you would have been indifferent to entering the forward—the forward pays off exactly what you would have gotten by investing in the foreign currency at spot rates and earning the local [interest rate](/interest-rate/).

The intuition is simple: if the dollar [interest rate](/interest-rate/) is higher than the [euro](/european-central-bank/) rate, the dollar is expected to weaken. A forward contract should price in that weakness; if it doesn't, there would be an arbitrage opportunity. The break-even rate is where no arbitrage exists—the forward is "fairly valued."

## The Interest Rate Parity Formula

The break-even forward rate is derived from the [interest rate parity](/interest-rate-parity/) relationship:

> **F = S × (1 + r₂) / (1 + r₁)**

Where:
- **F** = the forward rate (domestic per foreign)
- **S** = the spot rate today
- **r₁** = the annual interest rate in the domestic currency (as a decimal)
- **r₂** = the annual interest rate in the foreign currency

Imagine you are a US exporter who will receive €1 million in one year and wants to hedge the [currency risk](/currency-risk/). The spot rate is 1.10 $/€ (one euro costs 1.10 dollars). The one-year US dollar rate is 5% and the euro rate is 3%.

The break-even forward rate is:

> F = 1.10 × (1.03) / (1.05) = 1.10 × 0.9810 = 1.0791 $/€

If the forward contract is offered at exactly 1.0791, you are indifferent between hedging and not hedging (assuming no transaction costs). Your expected cash flow is the same either way.

## What If the Forward Rate Differs from Break-Even?

In practice, the forward rate quoted by a [broker](/broker/) may differ slightly from the parity rate due to bid-ask spreads, [counterparty risk](/counterparty-risk/) premia, and market friction. But large deviations would trigger arbitrage.

Suppose the forward is quoted at 1.0750 $/€, **lower** than the parity rate of 1.0791. This is a favorable forward for the exporter: you lock in 1.0750 instead of 1.10 spot (a gain) and better than the parity rate (another gain). The forward is said to be "tight" or "in the money" for the hedger.

Conversely, if the forward is 1.0850 $/€, **higher** than parity, the forward is "out of the money." You lock in more dollars per euro than parity would suggest, but it's still a weakness hedge relative to the current spot.

## Arbitrage and Market Equilibrium

If the forward deviates significantly from the parity rate, an arbitrageur can profit. Suppose the forward is 1.0750 and parity says 1.0791:

1. Borrow dollars at 5%.
2. Exchange dollars for euros at spot 1.10, receiving euros.
3. Lend euros at 3%.
4. Sell euros forward at 1.0750 $/€.
5. In one year, collect euro principal + interest, sell at forward, and repay dollar loan + interest.

The locked-in profit is tiny but positive. Thousands of arbitrageurs pursuing this trade drive the forward back up to parity. When the forward rate equals the interest rate parity rate, the arbitrage is eliminated and the break-even is in equilibrium.

## Practical Calculation Over Shorter Periods

For a short-term forward (e.g., 90 days), use a simplified version. If the dollar rate is 5% annually (0.05 / 4 = 0.0125 per quarter) and the euro rate is 3% annually (0.03 / 4 = 0.0075 per quarter):

> F = 1.10 × (1.0075) / (1.0125) = 1.10 × 0.9951 = 1.0946 $/€

Over 90 days, the forward weakens by just 0.54% (1.0946 vs. 1.1 spot). Over a full year, the weakening is 1.91%, reflecting the interest rate differential.

## Hedging and Lock-In Mechanics

Once you enter a forward at the agreed rate, that rate is your **break-even**—the cost of your hedge is crystallized. If the euro appreciates beyond the forward rate (say, to 1.15 $/€), you are glad you hedged: you locked in 1.0791 instead of paying 1.15. Conversely, if the euro depreciates (say, to 1.05 $/€), you wish you hadn't hedged; you could have sold euros at the higher spot rate.

But that regret is built into forward pricing. The interest rate differential already bakes in the expected depreciation; if you enter at parity, you have paid for that protection in advance via the rate differential.

## Real-World Factors Affecting Actual Forward Rates

The interest rate parity formula assumes:
- No [transaction costs](/bid-ask-spread/)
- Ability to borrow and lend at quoted rates
- No [credit risk](/credit-risk/) or [basis risk](/basis-risk/)
- Frictionless markets

In reality, forwards deviate slightly from parity due to:
- **Bid-ask spreads** on both currency spot and interest rate instruments
- **Counterparty credit spreads**: a forward with riskier banks costs more
- **Hedging demand imbalances**: if many exporters are selling euros forward, the forward may be pushed lower as brokers seek offsetting buyers
- **Regulatory constraints**: limitations on [leverage](/leverage-ratio-forex/) or position sizes

These frictions are usually small (0.01–0.05%), but they add up and are why no two traders quote the exact same forward rate.

## Break-Even vs. Payoff Diagram

A payoff diagram shows profit or loss as the spot rate moves at maturity. A forward contract is a horizontal line—flat payoff regardless of spot. The forward **break-even** is the vertical axis intercept: the spot rate at which profit is zero.

For a 1-million-euro forward bought at 1.0791 $/€:
- If spot at maturity is 1.05 $/€, loss = (1.05 − 1.0791) × 1m = −$29,100
- If spot at maturity is 1.10 $/€, gain = (1.10 − 1.0791) × 1m = +$20,900
- If spot at maturity is 1.0791 $/€, gain/loss = $0 (break-even)

## Multi-Period and Rolling Forwards

Long-dated forwards (2+ years) are less liquid and often involve rolling shorter-dated forwards to extend the hedge. Each roll resets the forward rate to a new parity level based on the prevailing [yield curve](/yield-curve/). The mechanics remain the same: the new forward equals spot multiplied by the interest rate ratio for the new period.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward contract](/forward-contract/) — the legal mechanics and settlement of FX forwards
- [Interest rate parity](/interest-rate-parity/) — the foundational principle linking spot, forward, and interest rates
- [Spot rate](/spot-rate/) — the exchange rate for immediate delivery
- [Currency risk](/currency-risk/) — exposure to unexpected currency moves
- [Currency volatility](/currency-volatility/) — the standard deviation of exchange rate moves

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — using forward, option, and swap instruments to reduce risk
- [Counterparty risk](/counterparty-risk/) — the risk that the other party in a forward defaults
- [Basis risk](/basis-risk/) — mismatch between the hedge instrument and the underlying exposure
- [Exchange rate](/spot-exchange-rate/) — factors driving long-term currency direction

</div>