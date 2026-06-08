---
title: "Sovereign Credit Default Swap"
description: "A derivative contract that transfers default risk on government debt, with CDS spreads often diverging from bond-implied yields during market stress."
keywords:
  - credit default swap
  - sovereign CDS
  - default risk
  - government bonds
  - cds-bond basis
image: /svg/fixed-income.svg
---

*A **sovereign credit default swap (CDS)** is a derivative contract in which one party pays a periodic fee to another in exchange for protection against default by a government borrower. If the government defaults, the protection buyer receives a lump sum. CDS spreads on government debt are market prices for [default risk](/credit-risk/), but they frequently diverge from the spreads embedded in [bonds](/bond/) themselves—a gap that reveals liquidity imbalances, regulatory constraints, and speculative positioning.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sovereign CDS — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for government debt and fixed income." />

<div class="wiki-infobox-caption">A price signal for government default risk that diverges from bonds during crises.</div>

|   |   |
|---|---|
| **What it is** | Derivative providing insurance against government default or credit event |
| **Also called** | Sovereign credit default swap, government CDS, CDS on [sovereign debt](/sovereign-debt/) |
| **Premium paid** | Periodic fee, quoted in basis points per year |
| **Payout trigger** | Defined credit event—default, restructuring, or specified covenant breach |
| **Key advantage** | Pure default risk exposure, unburdened by [bond](/bond/) carrying costs or liquidity constraints |
| **CDS-bond basis** | Difference between CDS spread and bond [credit spread](/credit-spread/); often widens in stress |

</aside>

## How a sovereign CDS contract works

A sovereign CDS is a customized bilateral agreement between two parties. The protection buyer (often a hedge fund, insurance company, or [hedge fund](/hedge-fund/) positioning for a sovereign default) pays an annual fee—called the CDS spread—expressed in basis points on a notional amount. A CDS spread of 100 basis points means the buyer pays 1% of the notional principal per year.

In exchange, the protection seller (typically a large dealer or financial institution) agrees that if a defined credit event occurs before the contract matures, it will compensate the buyer. The compensation is usually cash equal to the loss on the underlying bond, calculated as the difference between par (100) and the market value of the bond after the event.

Credit events are precisely defined in the contract, typically including:
- Non-payment of principal or coupons when due
- Restructuring (forced reduction of debt, maturity extension, or coupon cut)
- Repudiation of debt
- Moratorium (suspension of payments)

For sovereigns, the definition of "restructuring" is contentious. Some CDS use a narrow definition requiring explicit government action; others include any economic loss to bondholders. This ambiguity has created disputes—the Greek CDS settlement in 2012 is a famous example—because whether a particular debt exchange triggers a payout depends on which contract terms apply.

## Why CDS spreads diverge from bond spreads

In a frictionless market, the CDS spread should equal the [credit spread](/credit-spread/) on the government's bonds. Both measure default risk over the same horizon. But in reality, they diverge—sometimes by tens of basis points—due to several structural factors.

**Liquidity imbalance**: CDS on deeply traded sovereigns (like the U.S. or Germany) are more liquid than the cash bond market itself. If investors want exposure to default risk with minimal price movement, they prefer CDS. Demand for CDS can push spreads lower than bond spreads. Conversely, if cash-bond investors are forced sellers (due to leverage, margin calls, or redemptions), bond spreads widen while CDS may lag, creating a positive basis.

**Regulatory constraints**: Insurance companies and banks hold large quantities of government bonds for capital and liquidity purposes. They often buy CDS as hedges, creating one-way demand. Regulations that exempt government bonds from certain prudential requirements may also skew the supply-demand balance.

**Carry and funding costs**: Bond holders incur repo financing costs and custodial fees. CDS buyers pay only the periodic spread, with no carry costs. If funding is cheap, bond holders profit from the carry (the accrual of coupon minus financing cost) and tolerate a wider bond spread than the CDS spread. If funding becomes expensive (during stress), that advantage reverses and bond spreads tighten relative to CDS.

**Speculation and positioning**: Hedge funds and proprietary traders use CDS to make leveraged directional bets on sovereign default risk. Concentrated large positions can push CDS spreads away from fair value. During crises, when balance-sheet constraints bind, dealers may resist taking CDS risk and quotes widen sharply—widening the basis.

## The CDS-bond basis during stress periods

The gap between CDS and bond spreads—the "basis"—is tightest in calm markets and widens dramatically during crises. When fear spikes, CDS spreads typically move first and wider because derivatives are more liquid and faster to price than cash bonds. A big dealer can quote a CDS 1 basis point tighter than the last traded bond, triggering rapid repricing.

During the 2011 European sovereign crisis, the bases on Greek, Irish, and Portuguese debt blew out. CDS spreads spiked 500+ basis points while bond spreads lagged, creating arbitrage opportunities: traders shorted bonds and bought CDS protection, betting the basis would converge. When it did, they locked in profit.

The 2020 COVID crash saw a violent but brief basis widening. Dealers were flooded with selling in both markets but repriced CDS faster because inventory management is faster in derivatives than in cash bonds. Within weeks, liquidity returned and the basis normalized.

## Using CDS to price default probability

The CDS spread is a market price for default risk, but it is not a direct probability. A 100-basis-point spread does not mean a 1% annual default probability; it reflects the premium to insure against default over a multi-year horizon, accounting for recovery value after default, convexity, and term structure.

Quantitative analysts extract implied default probabilities from CDS spreads using calibrated models, but the relationship is complex. A spike in CDS spreads on a government that has not missed a coupon indicates market stress, repricing of tail risk, or speculative positioning—not an immediate solvency crisis. Conversely, extremely low CDS spreads can reflect complacency or regulatory-driven demand that masks underlying risk.

For investors, CDS spreads are most useful as a relative gauge: comparing spreads across sovereigns to identify which governments are perceived as relatively riskier; tracking spreads over time to detect deterioration; and spotting basis anomalies that signal market dislocations.

## The role of CDS in sovereign restructuring

When a government defaults and must restructure its debt, CDS holders can be either beneficiaries or victims depending on how the credit event is defined and triggered. Greece's 2012 restructuring, for example, was contentious because the country implemented a debt exchange via a domestic legal mechanism rather than an outright default. Many CDS contracts did not trigger a payout because they required an explicit non-payment event, not a restructuring. Buyers who thought CDS would protect them were left uncompensated while bondholders took haircuts.

This ambiguity has made sovereign CDS less useful as a pure hedging tool. Governments can be creative in structuring debt relief in ways that avoid triggering CDS technical definitions. As a result, market participants increasingly view sovereign CDS as a speculative instrument or relative-value trade rather than a reliable insurance mechanism.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit Default Swap](/credit-default-swap/) — derivative transferring credit risk on corporate or government debt
- [Credit Risk](/credit-risk/) — the risk that a borrower will default or fail to pay on time
- [Credit Spread](/credit-spread/) — the yield premium demanded for riskier debt versus safe [Treasury debt](/treasury-bond/)
- [Sovereign Debt](/sovereign-debt/) — borrowing issued by national governments
- [Bond](/bond/) — a fixed-income security with coupon payments and maturity date
- [Counterparty Risk](/counterparty-risk/) — risk that a CDS protection seller fails to pay if a credit event occurs

### Wider context

- [Derivative](/option/) — a financial instrument whose value derives from an underlying asset
- [Hedge Fund](/hedge-fund/) — investment partnerships deploying leveraged strategies across markets
- [Default Rate](/default-rate/) — the proportion of borrowers who fail to repay debt
- [Financial Crisis](/recession/) — severe market dislocations and credit contractions

</div>
