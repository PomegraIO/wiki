---
title: "Settlement Discipline Regime Cash Penalties"
description: "How EU CSDR settlement discipline regime penalties work: daily cash charges for late trades, calculation methods, and redistribution between failing and receiving parties."
keywords:
  - settlement discipline regime
  - csdr settlement penalties
  - settlement discipline cash penalties
  - trade settlement discipline
  - settlement discipline framework
  - settlement failure penalties
---

*The **settlement discipline regime** imposes automatic daily cash penalties on trading parties whose securities fail to settle on time within the EU and EEA. These charges are calculated based on the trade's notional value and the number of days late, then split between the failing party (who pays) and the receiving party (who benefits), creating financial incentives to resolve settlement failures quickly.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Settlement Discipline Regime — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for settlement and clearing." />

<div class="wiki-infobox-caption">Regulatory cash penalties enforce on-time settlement across EU/EEA markets.</div>

|   |   |
|---|---|
| **Framework** | EU CSDR (Central Securities Depository Regulation), effective 2015 |
| **Jurisdiction** | EU and EEA member states |
| **Penalty accrual** | Daily: starts day after settlement date, continues until delivery |
| **Calculation basis** | Trade value × accrued rate (0.40% annually, applies pro rata) |
| **Split** | 50% to receiving party, 50% to central securities depository or competent authority |
| **Settlement type** | Applies to [equity](/stock/) and debt trades in CSD-eligible instruments |

</aside>

## Why settlement discipline penalties exist

Before penalties were introduced, the cost of late settlement—processing delays, operational friction, temporary funding mismatches—fell only on the receiving party or spread across the market. Failing parties had no direct financial penalty and little urgency to resolve failures. The **settlement discipline regime** inverts that: it creates a daily accrual cost borne directly by the failing party, making on-time settlement financially rational rather than optional.

The framework applies across all central securities depository networks in EU member states and cooperating EEA jurisdictions. It is one of the few post-2008 regulations that reaches directly into trade operations—not just bank solvency or risk reporting—and forces settlement discipline through pain, not persuasion.

## How the daily cash penalty is calculated

The penalty rate is **0.40% per annum** of the trade's notional value. This rate is fixed in the regulation; it does not vary by settlement window (T+2, T+3, etc.) or by market conditions.

**Worked example:**
- Trade notional value: €1,000,000
- Settlement date: Tuesday, 10 January
- Securities delivered: Thursday, 12 January (2 days late)
- Daily charge: €1,000,000 × 0.40% ÷ 365 = €10.96 per day
- Total penalty accrued: €10.96 × 2 = €21.92

The calculation begins on the day *after* the contractual settlement date and continues daily until the securities are fully delivered and cash exchanged. On the day settlement finally occurs, no additional penalty accrues.

For partial deliveries (settlement of quantity X on day 1, quantity Y on day 3), penalties apply separately to each tranche based on the quantity and days it remains unsettled.

## Who pays and who receives the cash penalty

The regulation splits the accrued penalty 50–50:

1. **50% to the receiving party.** The party entitled to receive the securities receives half the total penalty. This compensates for the delay and the cost of carrying an incomplete or delayed settlement.

2. **50% to the CSD or competent authority.** The remaining half goes to the central securities depository or the national competent authority overseeing settlement. This half typically funds surveillance, enforcement, or operational improvements to reduce future failures.

In a buy-sell transaction, the buyer is the receiving party (awaits securities delivery) and the seller is the failing party (owes delivery). The buyer receives 50% of the penalty; the CSD takes 50%.

## When penalties are waived or suspended

Not all settlement delays trigger penalties:

- **Instruction failures before settlement date:** If a party cannot settle because the other side never sent valid settlement instructions, no penalty accrues. The onus is on both parties to ensure instructions are in place by the day before settlement.
- **Force majeure or CSD closure:** Penalties are suspended if the CSD itself is closed, a [counterparty](/credit-risk/) fails (e.g., bankruptcy), or a documented force majeure event (exchange failure, national emergency) prevents settlement.
- **Mutual agreement:** In rare cases, trading parties may agree in writing to extend the settlement date. This agreement must be notified to the CSD and executed before the settlement date; a retroactive waiver is not permitted.

Penalties do accrue for ordinary delays—processing backlogs, operational error, liquidity shortages, or deliberate withholding. The intent is that failing parties bear the cost and accelerate resolution.

## Impact on market participants

For **buy-side institutions** (asset managers, pension funds), settlement discipline creates an incentive to monitor their custodians and brokers. A custodian with a pattern of late settlements will cost the asset manager real money; this drives better vendor selection and contract terms.

For **custodians and settlement service providers**, the penalties—especially the cost to reputation and the 50% windfall to the receiving party—are a direct operational charge. Leading CSDs invest in real-time settlement, exception management, and matching automation partly to avoid incurring these penalties on behalf of clients.

For **brokers**, penalties make it costly to defer final settlement ("rolling" trades from day to day) or to manage fails passively. This has contributed to faster settlement—many trades now settle same-day or T+1 in practice, well before penalties begin to accrue.

## Interaction with netting and multi-leg settlement

Settlement discipline applies per trade, not per netting cycle. If a party is net short securities after netting, the shortfall (the failing quantity) incurs penalties daily. Conversely, a party receiving more than it delivers does not "offset" the penalties from other trades.

For structured or multi-leg trades (e.g., a repo transaction with multiple legs, a stock-bond package), each leg's settlement is tracked independently for penalty purposes. A delay in one leg does not excuse the others.

## Reporting and transparency

CSDs report settlement discipline penalties to financial regulators and, in some cases, publish aggregated failure statistics. Individual transactions and the parties involved are typically confidential between the trading parties and the CSD, but aggregate failure rates and penalty data are used by regulators to identify systemic settlement risk.

The existence of penalties is also reflected in settlement risk disclosures. Institutions managing significant settlement volumes must disclose their exposure to penalties and settlement failures in governance and risk reports.

## See also

<div class="wiki-seealso">

### Closely related

- Settlement Clearing — core processes and timeline
- [Counterparty Risk](/counterparty-risk/) — credit exposure during settlement failure
- [Dodd-Frank Act](/dodd-frank-act/) — related post-2008 settlement regulation in the US
- [Price Discovery](/price-discovery/) — settlement certainty affects pricing
- [Forward Contract](/forward-contract/) — settlement terms embedded in pricing

### Wider context

- [Stock Exchange](/stock-exchange/) — venue where settlement is initiated
- [Broker](/broker/) — intermediary managing settlement on behalf of clients
- [Custodian](/custodian/) — institution responsible for safekeeping and settlement
- [Credit Risk](/credit-risk/) — broader operational and financial risk framework

</div>
