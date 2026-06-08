---
title: "Netting Agreement"
description: "A contractual provision that offsets multiple derivative exposures between counterparties into a single net payment upon default or termination."
keywords:
  - close-out netting
  - multilateral netting
  - credit exposure
  - counterparty risk
  - ISDA
  - default
image: "/svg/derivatives.svg"
---

*A **netting agreement** is a legal clause that allows two counterparties to combine the value of all their derivative trades into one net payment obligation, rather than settling each position separately. Upon default or early termination, only the net amount changes hands—a mechanism that dramatically reduces credit exposure and administrative friction in derivatives markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Netting Agreement — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and risk." />

<div class="wiki-infobox-caption">Netting collapses multiple exposures into a single net obligation.</div>

|   |   |
|---|---|
| **What it is** | A contractual mechanism that offsets all derivative positions between two parties into one net amount |
| **Also called** | Close-out netting; multilateral netting (if more than two parties) |
| **Key benefit** | Reduces [credit risk](/credit-risk/) and legal complexity when a counterparty defaults |
| **Standard vehicle** | [ISDA Master Agreement](/isda-master-agreement/) |
| **Typical use** | OTC derivatives (swaps, forwards, options) |
| **Regulatory role** | Recognized under [Dodd-Frank](/dodd-frank-act/) and EMIR; essential for [collateral](/collateral-management-derivatives/) posting |

</aside>

## How netting collapses exposures into one obligation

Imagine Bank A and Bank B have entered into five separate [interest-rate swaps](/interest-rate-swap/). On one swap, Bank A owes Bank B $10 million. On another, Bank B owes Bank A $8 million. Without netting, both parties would pay each other the full amounts, moving $18 million in total liquidity. With a netting clause, the two banks calculate one net position: Bank A pays Bank B $2 million. The same economic outcome—A's loss, B's gain—occurs, but with less cash flow, less settlement risk, and simpler accounting.

Close-out netting applies this principle at the moment of default. If Bank B becomes insolvent, Bank A does not have to pay B on in-the-money trades while watching B's insolvency administrator seize A's payments on out-of-the-money trades. Instead, a netting clause allows A to stop all payments, mark all positions to market, and collect only the net amount owed. This is powerful protection: it cuts credit exposure in half or more, depending on portfolio composition.

## The legal and regulatory foundation

Netting agreements derive their force from contract law and rely on carefully drafted language that survives the insolvency of one counterparty. The [ISDA Master Agreement](/isda-master-agreement/) is the global standard; it embeds detailed netting mechanics that have been tested (and refined) through multiple financial crises. Courts in most jurisdictions recognize netting clauses as binding, though the enforceability varies by country and the type of contract.

Regulators explicitly support netting because it reduces systemic risk. Under [Dodd-Frank](/dodd-frank-act/), netting agreements reduce capital and margin requirements for derivatives dealers. The [Federal Reserve](/federal-reserve/) and international standard-setters recognize netting as a credit-risk mitigation technique, allowing banks to calculate [counterparty risk](/counterparty-risk/) net of netting benefits. Without this recognition, derivatives markets would require roughly twice as much capital and margin.

## Two forms: bilateral and multilateral

**Bilateral netting** involves two counterparties and a single netting agreement. This is the default in OTC markets. Bank A and Bank B agree: when either party defaults, all trades between them are marked to market, cash flows are netted, and one payment settles the lot.

**Multilateral netting** extends the concept to three or more parties, typically through a central counterparty (CCP). An exchange or clearinghouse becomes the counterparty to every trader; it nets all buy and sell orders into a single position per member. This is standard on organized exchanges and is now mandatory for standardized derivatives under post-2008 regulation. A CCP can net thousands of trades across hundreds of members, collapsing exposures far more efficiently than bilateral arrangements.

## Margin and collateral implications

Netting directly influences how [collateral](/collateral-management-derivatives/) is posted. If Bank A has a large in-the-money swap with Bank B, it can demand [initial margin](/collateral-management-derivatives/). But a netting clause means A only posts margin on the net exposure—the sum of all positions with B—not on each trade individually. This can cut margin requirements by 30–60%, freeing capital for other uses.

In practice, dealers and their counterparties negotiate [variation margin](/variation-margin/) daily. The netting agreement specifies the net mark-to-market value of the entire portfolio, and the losing party posts cash or securities equal to the daily gain or loss. If the agreeing parties have not signed a netting clause, each position would need separate margin calculations, a bureaucratic nightmare.

## What netting does not do

Netting reduces credit risk but does not eliminate it. If Bank A is holding a $50 million in-the-money position with Bank B, and Bank B defaults overnight, the netting clause protects A's net exposure. But A still risks that the margin already posted by B is insufficient, or that B's insolvency administrator will contest the netting clause (a rare but real event). This remaining credit risk is why dealers also use other tools: [credit derivatives](/credit-event-sovereign/), [CDS](/credit-default-swap/) hedges, and [diversification](/diversification/).

Netting also does not affect the economic value of trades. A $10 million loss is a $10 million loss, whether settled in one payment or split across ten. Netting is purely a risk-mitigation and settlement mechanism, not a way to avoid losses or hide them.

## The post-2008 regulatory shift

Before the financial crisis, netting was common in bilateral OTC markets but less systematized. Lehman Brothers' 2008 collapse exposed weaknesses: the bank had thousands of netting agreements with different counterparties, each with slightly different terms. Resolving these agreements consumed months and billions in legal fees. Regulators responded by standardizing netting practices within the ISDA framework and, more radically, by mandating that standardized derivatives move to CCPs, where multilateral netting happens automatically.

Today, most [interest-rate swaps](/interest-rate-swap/), [currency swaps](/currency-risk/), and [credit-default swaps](/credit-default-swap/) are cleared through a CCP and subject to multilateral netting. Custom derivatives remain bilateral but rely on ISDA Master Agreements with robust netting clauses. The result is a derivatives market with far lower systemic credit risk than it carried in 2007.

## See also

<div class="wiki-seealso">

### Closely related

- [ISDA Master Agreement](/isda-master-agreement/) — the standard legal template embedding netting clauses for OTC derivatives
- [Collateral Management in Derivatives](/collateral-management-derivatives/) — how netting affects margin posting and credit exposure
- [Counterparty Risk](/counterparty-risk/) — the credit risk that netting helps mitigate
- [Credit Default Swap](/credit-default-swap/) — a hedge often paired with netting agreements
- [Derivatives Market Regulation](/derivatives-market-regulation/) — how Dodd-Frank and EMIR mandate clearing and netting
- Central Counterparty — the hub of multilateral netting on regulated exchanges

### Wider context

- [Forward Contract](/forward-contract/) — bilateral derivatives that depend on netting
- [Interest-Rate Risk](/interest-rate-risk/) — the underlying exposure managed by swaps using netting
- [Credit Risk](/credit-risk/) — the fundamental risk that netting is designed to reduce
- [Default Rate](/default-rate/) — the probability event that triggers close-out netting

</div>
