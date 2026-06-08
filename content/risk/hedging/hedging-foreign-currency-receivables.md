---
title: "Hedging Foreign Currency Receivables"
description: "How to lock in the domestic-currency value of a foreign-currency payment using forwards and options before the money arrives."
keywords:
  - how to hedge foreign currency receivables
  - foreign currency receivables
  - forward contract hedge
  - currency options
image: "/svg/risk.svg"
---

*When a company expects to receive money in a foreign currency, **hedging foreign currency receivables** means locking in today's exchange rate so that currency fluctuations do not erode the value of the payment. The two main tools are [forward contracts](/forward-contract/) (which lock in a rate) and [options](/option/) (which protect against adverse moves while allowing upside).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hedging FX Receivables — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Lock in value before the payment arrives.</div>

|   |   |
|---|---|
| **Problem** | Currency fluctuations erode the domestic value of foreign cash |
| **Forward contract** | Lock rate today; mandatory delivery at maturity |
| **Option contract** | Pay a premium; choose to exchange at maturity if favorable |
| **Timing** | Hedge when receivable is committed (invoice issued, contract signed) |
| **Cost** | Forward: none upfront; option: premium paid today |

</aside>

## Why hedging matters for receivables

Imagine a U.S. company with a customer in Europe. The contract is for €100,000 due in 90 days. If the euro is worth $1.10 today, the company expects $110,000.

But currency markets are volatile. In 90 days, the euro might trade at $1.05 or $1.15. If it falls to $1.05, the receivable is worth only $105,000 — a $5,000 loss from currency movement alone. That loss is unrelated to whether the customer paid on time or whether the business was profitable. It is pure [currency risk](/currency-risk/).

For many companies, that variance is unacceptable. The business has already earned the profit from the sale; the remaining uncertainty is purely about exchange rates, a variable the company does not control and that does not reflect its operational performance.

**Hedging foreign currency receivables** means using financial instruments to lock in the rate and eliminate that uncertainty. Once hedged, the company knows exactly how much domestic currency it will receive, regardless of where the exchange rate moves.

## Forward contracts: The straightforward tool

A **forward contract** is an agreement to exchange a fixed amount of foreign currency for domestic currency at a rate locked in today, with settlement 90 days in the future.

Here is how it works:

1. **Company commits a forward.** The company agrees with a bank or counterparty to exchange €100,000 for U.S. dollars at a rate locked in today. Suppose the 90-day forward rate is $1.09 per euro.

2. **No money changes hands today.** The contract is an obligation, not a cash transaction. The company pays nothing upfront.

3. **At maturity (90 days).** The company receives €100,000 from its customer and delivers it to the counterparty. In exchange, it receives 100,000 × $1.09 = $109,000, regardless of the spot rate at that moment.

If the spot rate at maturity is $1.15, the company forgoes the €7,500 windfall ($1.15 − $1.09). If the spot rate is $1.03, the company avoids a €6,000 loss ($1.09 − $1.03). The forward locks in the middle.

### Forward contract mechanics and pricing

The forward rate is not the same as today's spot rate. It incorporates the interest-rate differential between the two currencies, a principle called **interest-rate parity**.

If U.S. dollar interest rates are 5% and euro rates are 2%, the dollar is "more expensive" to borrow. The forward rate adjusts so that a trader cannot arbitrage: borrowing cheap euros, swapping for dollars at a locked-in rate, and earning 5% interest. The forward rate on the euro is higher than the spot rate to offset the interest-rate advantage.

In practice, the company does not calculate this. The bank quotes a forward rate; the company accepts or shops around. The rate is typically very close to the spot rate, with the difference a few hundredths of a percentage point.

### Advantages and constraints of forwards

Forwards are simple and have no upfront cost. The company knows with certainty the amount of domestic currency it will receive.

But forwards are inflexible. If the customer pays early, the company might not receive the foreign currency on the forward date and must close the contract (buying it back or letting it expire unexercised, incurring a cost). If the company ends up with less foreign currency than expected, it might have to deliver domestic currency to settle the shortfall. The forward is a binding obligation.

In volatile markets, this certainty is exactly the point. In calmer markets, the company might prefer the option to benefit from favorable moves.

## Options: Flexibility at a cost

A **put option** on the foreign currency gives the company the right (but not the obligation) to exchange foreign currency for domestic currency at a locked-in rate, called the [strike price](/strike-price/).

Here is how it works:

1. **Company buys a put option.** The company pays a premium (say, $0.02 per euro) to buy a 90-day put option on the euro with a strike of $1.09. Total cost: 100,000 × $0.02 = $2,000.

2. **No obligation to exercise.** If the spot rate at maturity is $1.15, the company lets the option expire and exchanges its €100,000 at the market rate: $115,000.

3. **Insurance if rates move down.** If the spot rate falls to $1.03, the company exercises the put and exchanges at the strike of $1.09: $109,000. The put prevents a loss.

The company's net proceeds are the spot rate minus the premium, unless the option is in-the-money:

- Spot rate $1.15: Exercise value = $1.15 − $0.02 premium = $1.13 per euro. Proceeds: $113,000.
- Spot rate $1.03: Exercise value = $1.09 (strike) − $0.02 premium = $1.07 per euro. Proceeds: $107,000.

The put option ensures the company never receives less than about $1.07 per euro (the strike minus premium), while allowing upside if the currency appreciates.

### Forward vs. option: The trade-off

| Instrument | Cost | Benefit | Downside |
|-----------|------|--------|----------|
| **Forward** | $0 upfront | Locks rate; no uncertainty | Must settle at locked rate; no upside |
| **Put option** | Premium paid today (e.g., 2%) | Protects against downside; keeps upside | Premium reduces net proceeds even if option unused |

The forward is cheaper and simpler. The option costs money but allows the company to benefit if the currency strengthens. Choosing between them depends on:

- **Conviction about the rate.** If the company believes the currency will stay stable or strengthen, an option is attractive. If it fears a sharp depreciation, a forward offers certainty without doubt.
- **Budget.** The premium for options can be material for large exposures. A 2% premium on €100,000 is $2,000, which might be acceptable or might seem expensive.
- **Operational certainty.** If the company needs to forecast domestic-currency cash flow exactly, a forward is easier. If some flexibility around the timing or amount of receivable is acceptable, an option makes sense.

## Timing and structuring the hedge

A company should hedge when it has committed to the foreign-currency receivable — typically when the contract is signed or the invoice is issued. Waiting introduces unnecessary [currency risk](/currency-risk/).

For recurring receivables, a company might hedge a rolling window: hedge the next 90 days' expected foreign revenue with forwards or options, and roll the hedge forward as new invoices arrive. This is called a **rolling hedge**.

For one-off large receivables, a single forward or option is simplest.

The amount hedged should match the expected foreign-currency inflow. If the company hedges more or less than it actually receives, it is speculating on the currency, not hedging. This is called **basis risk** when the amount of hedge does not match the underlying exposure.

## Operational risks and adjustments

Not all receivables settle exactly on the expected date. A company that hedges 100% of a projected €100,000 receivable but actually collects only €90,000 will have a €10,000 short position under its forward contract. It must buy €10,000 at the market rate to settle, potentially at an unfavorable price.

To mitigate this, companies often hedge 80–90% of expected receivables, leaving some exposure unhedged to account for shortfalls. Alternatively, they use options so they can exercise only the amount they actually collect.

For companies with uncertain timing, options are superior because they can choose to exercise only if and when the foreign currency is received.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward Contract](/forward-contract/) — An obligation to exchange at a locked-in rate.
- [Option](/option/) — The right (not obligation) to exchange at a fixed rate.
- [Currency Risk](/currency-risk/) — The cost of exchange-rate movements.
- [Currency Volatility](/currency-volatility/) — How much exchange rates fluctuate.
- [Interest-Rate Swap](/interest-rate-swap/) — How interest-rate differentials affect forward pricing.

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — The broader framework for using contracts to offset risk.
- [Counterparty Risk](/counterparty-risk/) — Risk that the bank on the other side of the hedge defaults.
- [Operational Risk](/operational-risk/) — Risk from mismatches between hedge and actual receivables.

</div>