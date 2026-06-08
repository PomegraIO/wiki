---
title: "Counterparty Risk in Derivatives Contracts"
description: "Counterparty risk in derivatives: how bilateral exposure arises in swaps and forwards, netting mechanisms, and why OTC derivatives differ from exchange-traded contracts."
keywords:
  - counterparty risk
  - counterparty risk derivatives
  - swap counterparty exposure
  - bilateral default risk
  - netting agreements derivatives
image: "/svg/risk.svg"
---

*When two parties enter a [swap](/swap/) or [forward contract](/forward-contract/), neither side can eliminate the risk that the other defaults before settlement. **Counterparty risk in derivatives** is the exposure that your trading partner will fail to deliver payments due under the contract, leaving you holding a loss if rates have moved in your favor. This bilateral default risk is the defining structural difference between over-the-counter derivatives and exchange-traded contracts.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Counterparty Risk in Derivatives — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">Derivatives dealers manage default exposure through collateral, netting, and central clearing.</div>

|   |   |
|---|---|
| **Definition** | Default risk borne by both parties in OTC derivatives |
| **Mark-to-market exposure** | Positive (in-the-money) leg bears counterparty risk |
| **Netting benefit** | Reduces gross exposure by offsetting positions with same counterparty |
| **Central clearing** | Eliminates bilateral risk by replacing counterparty with clearinghouse |
| **Collateral** | Pledged as insurance; ISDA Credit Support Annexes standardize terms |
| **Pre-2008 gap** | Most interest-rate swaps unsecured; now majority collateralized |

</aside>

## Why Derivatives Carry Bilateral Default Risk

In a bond or stock transaction, [counterparty risk](/counterparty-risk/) is one-way: the seller's obligation to deliver the security ends after settlement. With derivatives, the exposure is two-way and persists over the life of the contract. A [call option](/call-option/) seller is exposed to the buyer defaulting on the premium; the buyer is exposed to the seller failing to deliver the underlying at [exercise](/exercise-price/). More commonly, the risk lives in mark-to-market gains and losses over time.

Consider a plain-vanilla [interest-rate swap](/interest-rate-swap/): Party A pays fixed; Party B pays floating. On day one, each party is solvent and liquid, so no one owes anything. Three months later, rates have risen sharply. The floating-rate leg is now worth more; Party B owes Party A a net payment. But if Party B defaults before paying, Party A is left with an unrealized loss—the value it *would have* received. Party B also bears the opposite risk: if rates fall, Party A owes Party B, and Party A might default. Both sides are exposed.

The magnitude of this exposure is unknown at inception because it depends on future price movements. A 10-year [interest-rate swap](/interest-rate-swap/) might have mark-to-market value near zero at the start, but by year three it could be worth 2% or 5% of the notional amount, representing real default risk. This *contingent exposure* is the core challenge: you cannot simply look at nominal values to measure risk; you must stress-test future rates, spreads, and volatilities to estimate how much your counterparty might owe you at various horizons.

## Netting: Reducing Gross to Net Exposure

Without netting, a derivatives dealer with hundreds of clients would face the sum of mark-to-market values of all positions—an unwieldy and expensive risk. **Bilateral netting** lets two counterparties offset gains and losses across all contracts between them. If Party A owes Party B $10 million on a swap and Party B owes Party A $8 million on a forward, netting reduces the obligation to a single $2 million payment from Party A to Party B. The dealer now faces only the net position for default risk purposes.

Netting requires a legal agreement—typically the [ISDA](/isda-master-agreement/) Master Agreement—that explicitly states the netting intent and is enforceable in the counterparty's jurisdiction. During the 2008 financial crisis, Lehman Brothers' bankruptcy revealed gaps: some counterparties had contracts with Lehman under agreements not governed by jurisdictions that recognize close-out netting, leaving them unable to quickly unwind positions and offset gains and losses. Modern ISDA documentation includes netting language, but cross-border and emerging-market derivatives sometimes lack robust netting protection.

Netting is potent. A large dealer might have $50 billion in gross mark-to-market exposures across all clients, but after netting, the net credit exposure might be only $5 billion—a tenfold reduction in the required collateral and capital reserves.

## Collateral and Credit Support

To limit counterparty default risk, derivatives counterparties post collateral. The **Credit Support Annex** (CSA) to the ISDA agreement specifies: which assets are acceptable (usually cash, Treasuries, or high-grade corporate bonds), how often collateral is marked to market and rebalanced (typically daily or weekly), and what threshold triggers a margin call. If your counterparty owes you $2 million and only has posted $1 million in collateral, it must post an additional $1 million to comply with the CSA.

Before the 2008 financial crisis, most interest-rate swaps—the largest segment of the derivatives market—were unsecured. A AAA-rated bank was trusted not to default, so collateral was rare. Post-crisis, regulatory reforms (including [Dodd-Frank](/dodd-frank-act/) in the United States) pushed most new derivatives into central clearing or mandated collateral for non-cleared positions. By the 2020s, the majority of interest-rate swaps are bilaterally collateralized. This shift dramatically reduced counterparty credit risk in the derivatives market, but at the cost of collateral demand and operational complexity.

Collateral arrangements also introduce **substitution risk**: if your counterparty posts lower-quality collateral (e.g., emerging-market bonds instead of Treasuries), you bear the risk that this collateral loses value if your counterparty defaults. CSAs manage this via haircuts—if Treasury collateral is worth 100 cents on the dollar, lower-grade corporate might be marked at 98 cents, and equities at 90 cents, to account for liquidation friction.

## Central Clearing and the Elimination of Bilateral Risk

**Central clearing** outsources counterparty risk to a clearinghouse. Instead of Party A owing Party B directly, Party A owes the clearinghouse, and the clearinghouse owes Party B. The clearinghouse is typically a heavily capitalized, well-regulated entity with a default fund (paid for by clearing members) to absorb any member's failure. From Party A's perspective, the counterparty risk becomes the risk of the clearinghouse itself—which is orders of magnitude lower because clearinghouses do not trade, they only guarantee.

Most standardized futures and options trade on exchanges with central clearing. Most plain-vanilla interest-rate and FX swaps can now be cleared; mandatory clearing rules push new contracts toward clearinghouses. However, bespoke (customized) derivatives—like a tailored [commodity swap](/commodity-swap/) or an exotic [currency option](/currency-option/)—often cannot be cleared and remain bilateral OTC contracts, requiring credit management.

The trade-off is cost: clearing requires the posting of initial margin (collateral against potential future losses) and variation margin (daily settlement of gains and losses), raising funding costs. Bilateral OTC derivatives can sometimes be traded with lower collateral requirements, making them cheaper for certain players, though riskier.

## Measuring Counterparty Exposure

Risk managers use several metrics to estimate bilateral counterparty exposure:

- **Current Exposure (CE)**: The mark-to-market value of all contracts with a counterparty if it defaulted today.
- **Potential Future Exposure (PFE)**: An estimate of how much you might owe at a future date under a stress scenario (e.g., a 2-standard-deviation move in rates or FX). Used to size collateral thresholds.
- **Expected Positive Exposure (EPE)**: The probability-weighted average of PFE over the life of the contract, used in regulatory capital calculations.

A derivatives dealer might estimate that with a major corporate client, current exposure is $5 million (favorable), but potential future exposure at a 95% confidence level is $15 million. It would post collateral or reduce notional size to keep the net position manageable.

## Counterparty Risk in Different Derivative Types

**Swaps** and **forwards** are symmetric: both parties have bilateral risk. **Options** are asymmetric: the buyer of the option has negligible counterparty risk (the premium is paid upfront), while the seller bears all the risk. A dealer writing a large [put option](/put-option/) must be monitored for credit quality because the buyer has no collateral at stake and will exercise the option only if it is in-the-money (i.e., when the seller has incurred a loss).

**Futures** and **exchange-traded options** transfer counterparty risk to the clearinghouse. A retail trader buying a stock-index futures contract faces minimal counterparty risk because the exchange member and clearinghouse guarantee it.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty risk](/counterparty-risk/) — default risk in any transaction with a trading partner
- [Credit default swap](/credit-default-swap/) — derivative used to hedge or speculate on default risk
- [Swap](/swap/) — general template for bilateral derivative contracts
- [Interest-rate swap](/interest-rate-swap/) — most common swap type; bilateral exposure example
- [Forward contract](/forward-contract/) — bilateral customized derivative with structural counterparty risk

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — using derivatives to reduce other risks
- [Credit risk](/credit-risk/) — broader framework for default and credit exposure
- [Risk weighted assets](/risk-weighted-assets/) — regulatory measure of default risk
- [Dodd-Frank Act](/dodd-frank-act/) — post-2008 regulation mandating clearing and collateral
- [Systemic risk](/systemic-risk/) — how derivatives interconnectedness threatens financial stability

</div>
