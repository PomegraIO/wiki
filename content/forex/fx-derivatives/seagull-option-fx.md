---
title: "Seagull Option"
description: "A three-leg FX option structure that provides zero-cost protection by combining a bought call, sold put, and sold call to cap both upside and downside."
keywords:
  - seagull option
  - zero-cost collar fx
  - three-leg option structure
  - collar strategy
  - fx protection
image: "/svg/forex.svg"
---

*A **seagull option** is a three-legged FX option strategy that provides downside protection at zero or minimal cost by pairing a long call with a sold put and sold call — all at different strikes. It is also called a **zero-cost collar** because the [option premium](/option-premium/) collected from selling the two wings (put and call) funds the purchase of the protective upside call, leaving net premium near zero. The trade-off is asymmetric: the buyer gains protection below one level but caps gains above another, creating a corridor of profitable payoff.*

<div class="wiki-hatnote">

For the equity collar strategy, see [protective-put](/protective-put/). This article covers the foreign exchange variant.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Seagull Option — key facts</div>

<img src="/svg/forex.svg" alt="An editorial mark for foreign exchange instruments." />

<div class="wiki-infobox-caption">A three-leg structure that borrows cost from selling profit caps to fund downside protection.</div>

|   |   |
|---|---|
| **What it is** | Long call + short put + short call, creating a defined-risk, zero-cost protection collar |
| **Also called** | Zero-cost collar, seagull, three-way option, collar spread |
| **Structure** | Buy call at high strike, sell put at low strike, sell call at higher strike |
| **Net premium** | Near zero; sold premium offsets bought premium |
| **Payoff pattern** | Flat below put strike, diagonal between strikes, flat above call strike |
| **Typical notional** | 1–100 million in major pairs; OTC-structured |
| **Key users** | Corporates hedging earnings, [hedge funds](/hedge-fund/), risk managers |

</aside>

## The three legs and payoff diagram

Imagine a German exporter expecting to receive $10 million in six months. Today, EUR/USD is at 1.0900. The exporter fears a stronger euro (weaker dollar), which would reduce the hedging value of those dollars when converted back to euros.

The exporter structures a seagull:
1. **Buy a call** at 1.1000 (upside protection: if the dollar weakens beyond 1.10, the call kicks in and limits loss).
2. **Sell a put** at 1.0700 (collect premium: accept downside to 1.07 to offset call cost).
3. **Sell a call** at 1.1200 (cap upside: accept that if the dollar strengthens beyond 1.12, no further gain accrues).

The put sale (low strike) and call sale (high strike) generate premium that funds the call purchase (middle strike), leaving net premium at or near zero.

The payoff corridor is bounded: 
- Below 1.0700 (put strike), the exporter is obligated to buy EUR/USD at 1.0700 (downside loss capped).
- Between 1.0700 and 1.1000, profit or loss moves one-to-one with spot.
- Between 1.1000 and 1.1200, the bought call shields further loss, profit flattens.
- Above 1.1200 (sold call strike), the exporter's upside is capped; the sold call obliges the exporter to sell at 1.1200.

## Zero-cost mechanics and the cost-carry debate

The term "zero-cost" is slightly misleading. The premium collected from the short put and short call typically *exceeds* the cost of the long call, yielding a net **credit** — the exporter receives cash. This credit is the hidden cost: the exporter has given up upside (sold a call) and accepted downside (sold a put) to fund the protection.

Over time, as the option approaches expiration, [time value](/time-value/) decays and the credit shrinks. If the currency drifts to the middle of the corridor, the exporter's effective cost is the original credit received, amortized. If the currency stays in the middle (the desired scenario), the exporter has paid a net zero premium and earned a flat, known hedged return.

Some dealers also offer a "true" zero-cost seagull by adjusting strike distances — if the exporter wants wider protection, the cap gets higher (moving the short call farther out), effectively selling more premium to finance a cheaper protection level. The builder's goal is to make the structure attractive and easy to explain.

## Why corporates use seagulls over collars

A simple [protective put](/protective-put/) (long call, no additional legs) costs clear premium — the exporter must pay cash upfront. A seagull defers or eliminates that cost by capping upside. For budget-constrained treasuries, this is appealing: instead of spending cash on insurance, the exporter accepts a ceiling on profits and uses that acceptance to buy protection.

The seagull is also more intuitive to explain to CFOs and boards: "We've locked in a range. Below 1.07, we're protected. Above 1.12, we don't make more, but we don't lose either. In the middle, we're fully exposed." The visual — a range of safety — is easier to justify than abstract premium paid for an out-of-the-money option.

## Market conditions and seagull popularity

Seagulls are most popular in:

**High [implied volatility](/implied-volatility/) environments.** When options are expensive, selling premium (puts and calls) generates substantial income, making zero-cost hedges feasible. In low-volatility environments, selling premium yields little, so the seagull becomes less attractive.

**Structural trends.** When a currency is expected to depreciate slowly (a long-term trend), corporates using seagulls can accept a higher cap (short call at a richer level) because they don't expect to hit it anyway. This makes the seagull even cheaper or profitable.

**Earnings season.** Exporters expecting FX headwinds tier seagull orders in the weeks before earnings announcements. Banks hedge their aggregate flow and set prices accordingly.

## Risks and tail-event dangers

The seagull is not without hazards:

**Gap risk at expiration.** If the currency gaps past the call cap at expiration (due to a surprise data release or geopolitical event), the exporter is obligated to sell at the cap level. A currency that leaps from 1.1100 to 1.1500 overnight leaves the exporter short, unable to deliver the promised dollars at the pre-arranged rate without buying them at a loss in the spot market.

**[Counterparty risk](/counterparty-risk/).** The seagull is an OTC structure, meaning credit risk to the bank is present. The bank could default between now and expiration, leaving the exporter unhedged.

**Basis risk.** The notional amount, timing, or currency of actual cash flows may differ from the seagull terms, leaving residual exposure.

**Complexity.** Because it is a three-legged trade, pricing, execution, and unwinding are more complex than a simple option. Wider bid-ask spreads apply. If the exporter wants to exit early (not possible, then realized the amount is wrong), costs multiply.

## Comparison to alternative hedges

A forward contract is simpler and cheaper: the exporter simply locks in EUR/USD at 1.0900 (or some forward rate) and eliminates FX risk entirely. But it admits no upside, which some treasuries find unpalatable.

A simple long call gives full upside but costs cash upfront.

A seagull splits the difference: modest upside, downside protection, zero net cost. It is especially popular among exporters and importers with limited hedging budgets, or those whose boards demand "natural" profit sharing above a floor.

## Exotic variants and dealer innovation

Dealers have extended the seagull concept: **reverse seagull** (short call, long put, short put at a wider strike) provides zero-cost protection against currency appreciation for importers. **Participating seagulls** or **asymmetric seagulls** adjust the cap and floor to create a wider corridor with partial upside — if the structure is profitable enough, it can fund not just one protective leg but a partial free option higher up.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — the protective upside leg
- [Put option](/put-option/) — the sold downside leg funding the call
- [Option premium](/option-premium/) — the net credit (ideally zero) flowing to the buyer
- [Strike price](/strike-price/) — the three strike levels defining the corridor
- [Protective put](/protective-put/) — the simpler single-leg hedge alternative

### Wider context

- [Counterparty risk](/counterparty-risk/) — OTC credit exposure to the bank dealer
- [Implied volatility](/implied-volatility/) — the key pricing driver for the three legs
- [Hedge fund](/hedge-fund/) — sophisticated users of exotic seagull variants
- [Currency risk](/currency-risk/) — the underlying FX exposure the seagull hedges

</div>
