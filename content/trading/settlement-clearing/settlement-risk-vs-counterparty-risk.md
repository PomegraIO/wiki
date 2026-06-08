---
title: "Settlement Risk vs Counterparty Risk: What Is the Difference"
description: "Settlement risk is exposure during trade finality; counterparty risk is credit risk before settlement closes. Timing and management strategy differ fundamentally."
keywords:
  - settlement risk
  - counterparty risk
  - settlement risk vs counterparty risk
  - credit exposure
  - trade finality
image: "/svg/trading.svg"
---

*The distinction between **settlement risk** and **counterparty risk** turns on timing: counterparty risk is the credit exposure that exists while a trade is pending, but settlement risk is the exposure that crystallizes only at the moment of final settlement. Understanding the difference is crucial for clearing [brokers](/broker/), banks, and [custodians](/custodian/), because the two risks demand different hedges and different collateral strategies.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Settlement Risk vs Counterparty Risk — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two exposures, two windows, two management playbooks.</div>

|   |   |
|---|---|
| **Counterparty risk** | Credit risk from the time of trade execution until settlement is final |
| **Settlement risk** | Exposure only at the moment both legs of the trade must finalize simultaneously |
| **Counterparty window** | Trade date to T+settlement date (days or weeks) |
| **Settlement window** | Minutes to hours: the moment one party delivers while the other has not yet confirmed receipt |
| **Usual magnitude** | Counterparty: entire notional trade value (in worst case) |
| **Settlement magnitude** | Settlement: often only the cash leg or the smaller of the two legs |
| **Mitigation** | Counterparty: collateral,[haircuts](/basis/), margin. Settlement: atomic delivery-vs-payment, clearing guarantees |
| **Frequency** | Both occur in every over-the-counter trade; settlement risk is largely eliminated in centrally cleared trades |

</aside>

## Counterparty Risk: Before Settlement Closes

**Counterparty risk** is the credit risk that the other party to your trade will default before the trade settles. It begins the moment you and your counterparty agree to terms, and it persists until both legs of the settlement are final.

Suppose you agree to buy 1,000 shares of Stock X from Dealer Y at $100 per share (notional value $100,000). You will pay $100,000 in cash, and Dealer Y will deliver 1,000 shares. But the trade will not settle until T+1 (the next business day).

Between T+0 (today, trade date) and T+1 (settlement date), you have a credit exposure to Dealer Y. If Dealer Y becomes insolvent overnight, you have already committed to pay $100,000. But there is no guarantee you will receive the shares. Your $100,000 is now an unsecured claim on a bankrupt counterparty.

This pre-settlement credit risk is counterparty risk. It affects the [balance sheet](/balance-sheet/) of the buyer (you have a credit-exposure liability to your clearing house or bank) and the seller (who must fund the trade and can only recover if you pay). The size of counterparty risk depends on the **market value** of the trade. If the stock fell to $95 overnight, the shares you are entitled to receive are now worth $95,000, and your counterparty's incentive to default (or to repudiate the trade) is much lower. But if the stock rose to $105, the counterparty may walk away, and you lose the economic benefit you were promised.

Counterparty risk is managed via **collateral**, **margin** (initial and variation), **netting agreements**, and **credit limits**. Banks and [brokers](/broker/) hold collateral from clients on margin accounts to cover potential loss if a counterparty fails. Clearing houses impose **capital** and [margin requirements](/margin-call-forex/) on all members to ensure they can cover a member's default.

## Settlement Risk: At the Moment of Delivery

**Settlement risk** is the credit exposure that emerges only at the instant one party has delivered its leg of the trade but the other party has not yet delivered theirs. It is also called **Herstatt risk**, named after the 1974 failure of Herstatt Bank, a German bank that received a [foreign exchange](/currency-risk/) payment in Deutsche Marks but failed before delivering U.S. dollars to its counterparties.

Settlement risk is much shorter in duration than counterparty risk—it lasts only minutes or a few hours—but it is also more acute. At the moment of settlement, the bank or dealer that has already paid has a total, unsecured claim on a counterparty that now possesses the asset but has not yet paid. There is no collateral, no netting, and no margin buffer. The payer is entirely dependent on the receiver's solvency and cooperation.

Example: You are a [currency](/currency-risk/) dealer. You sell $1 million USD and buy €900,000 EUR from a German counterparty. Settlement is scheduled for 2 PM New York time (9 PM Frankfurt time).

- At 1:55 PM, your U.S. dollar payment instruction goes out and is irrevocable.
- At 2:10 PM, you learn the German counterparty has collapsed.
- You have already sent $1 million, but the EUR payment never arrives.

Your bank is now $1 million poorer, and you have an unsecured claim on the receiver's estate.

Settlement risk is **atomic and binary**: either both legs settle, or neither does. There is no middle ground. The incentive structure is perverse: the party that receives first has every reason to confirm the receipt and then immediately fail, extracting the value of the asset without repayment.

## Why the Distinction Matters

### Risk Sizing

Counterparty risk grows as the market price of the underlying asset moves. A $100,000 trade is counterparty risk of up to $100,000 if the market moves sharply against the counterparty. But settlement risk is often much smaller: if the two legs of a $100,000 trade settle within seconds of each other (via a [repurchase-agreement](/repurchase-agreement/) or an [ETF](/etf/) redemption), the settlement risk window is almost zero. Settlement risk is really the credit risk of being **one leg ahead** at the moment of finality.

### Hedging and Mitigation

**Counterparty risk** is hedged by requiring collateral, posting margin, and diversifying across counterparties. A bank that trades with many dealers can cap its exposure to each dealer via a bilateral credit agreement.

**Settlement risk** cannot be hedged via collateral alone—by definition, the collateral has already been handed over. Settlement risk is mitigated by **delivery-versus-payment** (DVP) systems, in which both legs settle simultaneously through a central clearing system, or by **atomic delivery** on a distributed ledger (blockchain), where both legs either both clear or both fail. The only true hedge is to move settlement into a clearing house that guarantees both legs or to use real-time gross settlement (RTGS) systems that finalize both legs in the same instant.

### Regulations and Capital Rules

Regulators treat settlement risk and counterparty risk differently:

- **Counterparty risk** is monitored daily via mark-to-market, and capital is held against the potential loss. Banks must compute a [counterparty-risk](/counterparty-risk/) figure for every trade and must hold [capital](/capital-adequacy/) and collateral equal to (roughly) the expected positive exposure plus a buffer for unexpected moves.

- **Settlement risk** is managed via operational rules: same-day settlement is mandatory for many asset classes, and participation in settlement systems that eliminate settlement windows (such as real-time settlement) is required for systemically important counterparties. Regulators have pushed for the elimination of settlement risk by moving to T+0 settlement and by mandating clearing-house guarantees.

## Settlement Risk in Different Markets

### [Foreign exchange](/currency-risk/) (FX)

Settlement risk in FX is historically the largest and most acute. Because the U.S. dollar and EUR settle in different time zones (New York and Frankfurt), there is a many-hour window during which one currency has been paid but the other has not. During the Herstatt crisis, this window was nearly a full business day. Modern netting systems and **Continuous Linked Settlement** (CLS) have compressed this window to minutes, but settlement risk in FX remains material.

### Equities and Bonds

In [stock](/stock/) and [bond](/bond/) markets, settlement risk is much smaller because both legs (cash and securities) are often handled by the same clearing system (such as DTCC or Euroclear) and settle in the same instant. However, if a trade settles outside of the central clearinghouse (over-the-counter) or if one leg is in a different country, settlement risk can re-emerge.

### [Free-of-payment settlement](/free-of-payment-settlement-fop/) (FoP)

In **[free-of-payment-settlement-fop](/free-of-payment-settlement-fop/)** arrangements, settlement risk is deliberately extended. The securities leg settles, but the cash leg is delayed. This is common in [corporate-action-settlement-complications](/corporate-action-settlement-complications/) but is rare and risky in regular trades.

## Regulatory Evolution: From Herstatt to T+0

The 1974 Herstatt collapse exposed settlement risk as a systemic threat. Since then, regulations have aimed to **eliminate** settlement risk, not just manage it:

- **Mandatory clearing** of derivatives and certain securities shifts settlement risk to the clearing house, which guarantees both legs.
- **Real-time gross settlement** (RTGS) systems finalize both legs in the same instant, leaving no window for default.
- **T+1 and T+0 settlement cycles** reduce the counterparty-risk window (fewer days to wait for settlement).
- **Netting and offset** allow participants to reduce their gross settlement obligations, lowering the absolute value at risk.

The shift from T+3 (three business days) to T+2 (two business days) to T+1 (one business day) and eventually to T+0 (same day) is partly a reduction of counterparty risk (fewer days to hold the trade) and partly an elimination of settlement risk (no time for the counterparty to fail between legs).

## See also

<div class="wiki-seealso">

### Closely related

- [Free of payment settlement (FoP)](/free-of-payment-settlement-fop/) — When settlement risk is deliberately extended
- [Gross vs net settlement systems](/gross-vs-net-settlement-systems/) — How RTGS and netting reduce both types of risk
- Clearing — The infrastructure that guarantees settlement
- [Counterparty risk](/counterparty-risk/) — The broader credit-risk framework
- [Collateral and margin](/margin-call-forex/) — How credit exposures are backstopped
- [Custodian](/custodian/) — Third-party safeguards during the settlement window

### Wider context

- [Credit risk](/credit-risk/) — The full taxonomy of credit exposures
- [Operational risk](/operational-risk/) — Failures in settlement systems themselves
- [Liquidity risk](/liquidity-risk/) — The inability to raise cash or settle at all
- [Systemic risk](/systemic-risk/) — How settlement failures can cascade

</div>
