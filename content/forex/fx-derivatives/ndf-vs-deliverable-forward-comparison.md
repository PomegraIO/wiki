---
title: "NDF vs Deliverable Forward: Key Differences"
description: "Non-deliverable forwards (NDFs) and deliverable forwards differ in settlement mechanics, credit structure, and which currencies require each type."
keywords:
  - ndf vs deliverable forward
  - non-deliverable forward
  - fx forwards
  - currency derivatives
  - offshore currency settlement
  - emerging market fx
image: /svg/forex.svg
---

*An **NDF** (non-deliverable forward) and a **deliverable forward** are both [forward contracts](/forward-contract/) on currency pairs, but they settle in fundamentally different ways. A deliverable forward obliges both parties to exchange the full notional amount of principal at maturity; an NDF settles only the difference in value, in cash, typically in a third currency like USD. NDFs arose to circumvent capital controls in emerging markets, where authorities restrict offshore delivery of the local currency.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">NDF vs Deliverable Forward — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex." />

<div class="wiki-infobox-caption">Two settlement models for FX forwards; NDF is suited to restricted currencies, deliverable to major pairs.</div>

|   |   |
|---|---|
| **Settlement type** | Deliverable: full principal exchange; NDF: cash difference only |
| **Settlement currency** | Deliverable: both contract currencies; NDF: usually USD (or agreed currency) |
| **Counterparty risk** | Deliverable: principal risk on both sides; NDF: only profit/loss exposure |
| **Capital requirements** | Deliverable: both parties need full notional in reserves; NDF: minimal notional required |
| **Common currencies** | Deliverable: EUR/USD, GBP/USD, JPY/USD; NDF: INR, CNY, KRW, SGD, PHP, etc. |
| **Pricing** | [Forward rate](/forward-contract/) in both; NDF premium/discount may reflect capital controls |
| **Offshore vs. onshore** | Deliverable: standard in free-floating currency pairs; NDF: standard in restricted pairs |

</aside>

## Mechanics of a Deliverable Forward

A deliverable forward is the classic structure. Two counterparties agree that Party A will pay Currency 1 and receive Currency 2 at a specified date and [forward rate](/forward-contract/). At maturity, Party A physically delivers the notional amount of Currency 1 (say, $10 million USD) and receives the agreed amount of Currency 2 (say, EUR 9 million at a 1.11 forward rate).

Both parties face full notional principal risk: if the counterparty defaults before settlement, the non-defaulting party loses the entire notional amount (or faces replacement-cost risk if they have to enter a new forward at a worse rate). Accordingly, both parties typically require credit lines and may post collateral for large forwards.

Deliverable forwards are standard for freely tradeable major currency pairs: EUR/USD, GBP/USD, JPY/USD, CAD/USD, AUD/USD, etc. Central banks do not restrict offshore delivery of euros, dollars, pounds, or yen, so there is no legal or regulatory incentive to avoid physical settlement.

## Mechanics of an NDF

An NDF (non-deliverable forward) is settled as a cash difference only. Party A and Party B agree to a forward rate on, say, USD/INR (the Indian rupee). The contract specifies a notional principal (say, $10 million USD).

At maturity, the parties do *not* exchange the full principal. Instead, they compare the agreed forward rate to the spot rate realized at maturity. The difference is calculated and paid in a single cash settlement—typically in USD or another freely convertible currency.

Example:
- Notional: $10 million USD / INR
- Agreed forward rate: 1 USD = 82 INR
- Spot rate at maturity: 1 USD = 84 INR

Party A (long USD) benefits: they locked in 82 INR per dollar, but the dollar strengthened to 84 INR. The difference of 2 INR per dollar on $10M is worth approximately $240,000 USD (10M × 2 ÷ 84). This is paid in cash to Party A in USD; no rupees change hands.

## Why NDFs Exist: Capital Controls

NDFs emerged in emerging markets where the local government restricts offshore movement of its currency. India, China, Korea, Singapore, and the Philippines have (or had) capital controls that make offshore delivery of local currency difficult or illegal for many transactions.

Banks in these countries need to hedge their own currency exposure but cannot deliver the local currency offshore. An NDF allows them to replicate the economic effect of a forward—locking in a future exchange rate—without ever attempting to deliver the currency, thereby sidestepping regulatory restrictions.

The NDF market is thus entirely offshore, conducted in international financial centers (London, New York, Singapore) via telephone and electronic communication. The "non-deliverable" feature is a legal necessity, not a convenience.

## Counterparty Risk: The Central Difference

Deliverable forwards expose both parties to the full notional principal amount. If Party A owes Party B $10 million at settlement, Party A must deliver that cash; Party B's loss, if Party A defaults, is the entire $10 million (less recovery from bankruptcy).

NDFs expose each party only to the profit-or-loss amount. In the rupee example above, Party A's exposure is the $240,000 difference, not the $10 million notional. This is a *massive* reduction in [counterparty risk](/counterparty-risk/).

From a balance-sheet perspective, an NDF is cheaper: a bank can enter into a large notional NDF with a modest (or no) collateral requirement, because the economic exposure (the P&L) is small relative to notional. A deliverable forward requires full collateral or credit line backing for the principal.

This credit efficiency is why NDFs are attractive for emerging-market hedges and why they have grown so large (the NDF market is now several trillion dollars notional outstanding).

## Pricing and the "NDF Premium"

The forward rate in a deliverable forward is derived from [interest rate parity](/interest-rate-parity/): the forward rate should reflect the interest-rate differential between the two currencies and the current [spot rate](/spot-exchange-rate/).

Forward Rate = Spot Rate × (1 + Interest Rate 1) ÷ (1 + Interest Rate 2)

For major currencies in efficient markets, this relationship holds tightly. The forward market price is the theoretical price.

In NDF markets, however, pricing may deviate from interest-rate parity if capital controls create artificial scarcity or if onshore and offshore interest rates diverge. An NDF on the Chinese yuan might trade at a forward rate that does not match the theoretical parity, because onshore yuan interest rates are administratively controlled and differ from offshore (non-deliverable) rates.

This "NDF premium" (or discount) relative to parity can be a tradeable signal: investors believe it reflects the market's embedded view of future capital-control shifts or devaluation risk.

## Redemption and Termination

Deliverable forwards are simple to unwind: the parties agree to reverse the forward (sell/buy the opposite direction for the remaining period) or physically settle early. The economic settlement is straightforward.

NDFs are slightly more complex. If a bank wants to exit an NDF early (say, it entered a USD/INR forward six months out and now wants to exit after three months), it must agree with the counterparty on a termination price—the present value of the profit or loss as of that early date. This is negotiated in the interbank market.

## Which Currencies Use Which Structure

**Deliverable forwards** are standard for:
- EUR, GBP, JPY, CHF (Swiss franc), AUD, CAD, NZD
- Any currency with no significant capital controls and offshore availability

**NDFs** are standard for:
- INR (Indian rupee)
- CNY (Chinese yuan, offshore)
- KRW (Korean won, historically)
- SGD (Singapore dollar, for some tenors)
- PHP (Philippine peso)
- THB (Thai baht)
- IDR (Indonesian rupiah)
- MXN (Mexican peso, historically for some institutions)
- Any restricted or thinly offshore-traded currency

The NDF/deliverable boundary is not static: as a country liberalizes its capital account, the currency may migrate from NDF dominance to deliverable dominance. Conversely, periods of capital-control tightening can shift currencies into the NDF market.

## Regulatory and Accounting Implications

From a regulatory standpoint, NDF notional is measured differently than deliverable forwards. Regulators (and banks' risk systems) often report NDF notional at face value but calculate [value-at-risk](/value-at-risk/) based on the *economic* exposure (the difference, not the principal).

For accounting purposes, both NDFs and deliverable forwards are marked to market under IFRS and GAAP, with changes in fair value flowing through profit and loss. The settlement mechanics affect *how* the fair value is calculated, but both types must be fair-valued.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward contract](/forward-contract/) — Generic FX forward; deliverable and NDF are variants
- [Spot exchange rate](/spot-exchange-rate/) — Current market rate; forward premium or discount reflects interest-rate and risk differentials
- [Interest rate parity](/interest-rate-parity/) — Relationship between interest rates and forward exchange rates; NDF deviations from parity signal capital-control risk
- [Counterparty risk](/counterparty-risk/) — Central distinction: deliverable forwards expose principal; NDFs expose only P&L
- [Currency risk](/currency-risk/) — Why firms and banks use forwards (deliverable or NDF) to hedge FX exposure

### Wider context

- Forex market — Spot and forward FX trading; NDFs are an offshore, restricted-currency segment
- Capital controls — Regulatory restrictions that make NDFs necessary in emerging markets
- Emerging market currency — NDFs are the dominant hedging vehicle for EM FX
- [Leverage ratio forex](/leverage-ratio-forex/) — Banks' leverage constraints affect NDF vs. deliverable forward choice
- Credit valuation adjustment — CVA is larger on deliverable forwards (principal exposure) than NDFs

</div>
