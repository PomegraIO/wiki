---
title: "Hedging Currency Risk with a Forward Contract"
description: "Learn how exporters use forward contracts to lock in exchange rates and eliminate currency risk on future foreign-currency receivables."
keywords:
  - hedging currency risk with forward contract
  - forward contract currency hedge
  - exporter currency risk
  - fx forward hedging
  - exchange rate lock
  - currency exposure management
image: /svg/forex.svg
---

*A **forward contract** lets a business lock in a fixed exchange rate for a future currency transaction, removing the uncertainty of whether the dollar will rise or fall before payment arrives. An exporter owed money in euros six months out can use a forward to guarantee what those euros are worth today — the most direct way to eliminate [currency risk](/currency-risk/).*

<div class="wiki-hatnote">

This article covers operational currency hedging for businesses. For [portfolio hedging](/currency-risk/) of investment positions, see currency overlays and [options](/option/) strategies.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forward Contract Hedge — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for FX mechanics." />

<div class="wiki-infobox-caption">The simplest tool to lock in an exchange rate and eliminate currency uncertainty.</div>

|   |   |
|---|---|
| **What it does** | Fixes the [spot rate](/spot-exchange-rate/) for a future payment, eliminating [exchange-rate](/interest-rate/) moves |
| **Who uses it** | Exporters, importers, multinational corporations with future foreign-currency flows |
| **When to deploy** | Once you know the amount, timing, and currency of a future cash flow |
| **Cost structure** | No upfront premium; locked rate may be worse than today's spot |
| **Profit/loss mechanism** | Gain if spot moves in your favor; loss if it moves against you (hedged, so both are locked) |
| **Unwinding** | Sell the forward in the [secondary market](/secondary-market/) at current forward rates (may net gain or loss) |

</aside>

## A worked example: the exporter's hedge

An American electronics maker sells $2 million worth of components to a German customer, to be paid in euros six months from now. The contract is signed at today's [spot rate](/spot-exchange-rate/) of 1.10 dollars per euro — meaning the exporter expects to receive €1.82 million.

But the dollar has been volatile. If the euro weakens to 1.00 by the time payment arrives, those euros convert to only $1.82 million instead of the expected $2 million. The exporter's margin just compressed by 9%, entirely from currency movement, not the business itself.

The exporter approaches a bank and enters a **six-month forward contract** to sell euros at a fixed rate of 1.0950 dollars per euro. This rate is slightly below the current spot (1.10) — that's normal, a reflection of [interest rate differentials](/interest-rate/) between the US and the eurozone. Once locked in, the exporter knows with certainty:

- In six months, €1.82 million converts to exactly $1,994,900.
- No matter what the euro does in the meantime, the cash receivable is protected.

The trade-off: if the euro surges to 1.20, the exporter is stuck selling at 1.0950 instead of the then-current spot. The hedge eliminated downside risk but also capped upside.

## How the forward rate is set

Banks don't quote forward rates randomly. The **forward rate** is derived from the current [spot rate](/spot-exchange-rate/) and the interest-rate differential between the two currencies. If US dollar rates are 5% and euro rates are 2%, the dollar is worth more in terms of its time value, so the forward euro is bid lower to compensate — this is called **interest rate parity**.

The formula is rough, but the intuition is solid:

**Forward Rate ≈ Spot Rate × (1 + Domestic Rate) / (1 + Foreign Rate)**

In the example: 1.10 × (1.05 / 1.02) ≈ 1.0950. The forward is slightly weaker than spot because US rates are higher. This is not a forecast of where the euro "will go" — it's pure arbitrage pricing, ensuring neither the bank nor the customer can profit from a [carry trade](/carry-trade/) between the two rates.

## The profit-and-loss profile of a hedge

The exporter is short euros (will receive them); the forward contract is short euros (will sell them at a fixed rate). The positions perfectly offset.

- **If euro rises to 1.15 by maturity**: The exporter could have sold at spot and received an extra $46,000. The forward locks them out — it's a cost of the hedge.
- **If euro falls to 1.00 by maturity**: The exporter still sells at 1.0950 and avoids a $149,000 loss. The hedge protected them.

This is the essence of hedging: you pay the cost of protection (forgone upside) to eliminate downside. [Value at risk](/value-at-risk/) is cut to zero on the hedged amount.

## Unwinding the hedge early

Business rarely goes to plan. Suppose three months in, the customer delays payment another three months. The exporter now has a forward contract that no longer matches the actual cash flow. They can:

1. **Let it mature and simultaneously enter a new forward** for the actual payment date. This creates a synthetic [carry trade](/carry-trade/).
2. **Sell the forward in the [over-the-counter](/over-the-counter-market/) market** to another dealer or investor. The value of the forward is now determined by where the forward rate has moved since the trade was entered.

If rates have moved in the exporter's favor — say, the six-month forward rate is now 1.10 instead of 1.0950 — they can sell the forward at a profit. The opposite is also true. The unwinding price is driven by market [forward rates](/spot-rate/), which change continuously with interest-rate expectations and spot movement.

## Who else uses this structure

- **Importers**: Buy goods priced in foreign currency; forward locks in the home-currency cost.
- **Multinationals**: Hedge subsidiary dividends, intercompany loans, and expected tax payments in foreign currencies.
- **Project finance**: When revenue is in one currency and debt is in another, forwards lock in the [cost of debt](/cost-of-debt/) in home-currency terms.
- **Sovereign funds**: Hedge foreign-currency investment returns to manage [currency risk](/currency-risk/).

The forward is bilateral and customizable — any amount, any date, any pair of currencies that trade liquid forwards.

## Forwards vs. alternatives

A [call option](/call-option/) on euros gives the exporter the choice to sell at a fixed rate or walk away if the spot moves favorably. But options carry an upfront premium and are typically more expensive for routine hedging. A forward is cheaper because it removes the optionality — both parties are committed.

Futures contracts are standardized, exchange-traded versions of forwards, with daily [mark-to-market](/mark-to-market/) and collateral requirements. They're ideal for large flows and passive hedgers; forwards are the standard for bespoke corporate flows.

[Interest rate swaps](/interest-rate-swap/) and [currency swaps](/swap/) address longer-dated exposures and are common in project and sovereign debt. A forward is the tool for a single, discrete cash event.

## The accounting treatment

Under [ASC 606](/asc-606/) and similar standards, a designated cash-flow hedge is marked to [fair value](/fair-value/) each period, with changes flowing through equity (not the [income statement](/income-statement/)), preventing artificial P&L volatility. Operationally, the forward is a derivative and subject to reporting rules, but the hedge designation mutes earnings noise from the accounting perspective.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward Contract](/forward-contract/) — the general mechanics and pricing of forward derivatives
- [Spot Rate and Forward Rate](/spot-rate/) — the relationship between today's rate and locked-in future rates
- [Interest Rate Parity](/interest-rate/) — the economic principle linking forward rates to interest differentials
- [Currency Risk](/currency-risk/) — the broader context of FX exposure and why businesses hedge
- [Carry Trade](/carry-trade/) — how traders profit from interest-rate differentials without hedging
- [Over-the-Counter Market](/over-the-counter-market/) — where forwards are customized and traded

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — the general framework of using derivatives to manage risk
- [Mark-to-Market](/mark-to-market/) — how forwards are valued and reported
- [Counterparty Risk](/counterparty-risk/) — the bank that sells you a forward could default
- [Capital Flows](/capital-flows/) — the macroeconomic driver of currency movements

</div>
