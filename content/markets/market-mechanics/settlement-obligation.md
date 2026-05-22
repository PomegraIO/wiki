---
title: "Settlement Obligation"
description: "The legal and operational requirement to deliver securities or funds to counterparties on the contractual settlement date."
keywords:
  - settlement obligation
  - trade settlement
  - delivery requirement
  - market mechanics
---

*A **settlement obligation** is the binding commitment to deliver [securities](/wiki/shares-of-stock/) or funds to a counterparty on the agreed settlement date. In equities and bonds, this occurs [T+2](/wiki/settlement-t2/) (two business days after trade execution), [T+1](/wiki/settlement-t2/), or same-day for certain derivatives. Failure to meet this obligation triggers [fails](/wiki/fail-to-deliver-market-impact/), penalties, and potential [forced liquidation](/wiki/liquidation/) by the counterparty.*

<aside class="wiki-infobox">

| Key Fact | Value |
|---|---|
| **Standard Equity Settlement** | T+2 (North America, Europe, Asia) |
| **Government Bond Settlement** | T+1 or T+0 (varies by country) |
| **Derivative Settlement** | Cash, physical delivery, or T-day |
| **Governing Body** | Depository Trust Company ([DTC](/wiki/dtcc/)) (U.S.) |
| **Failure Penalty** | Buy-in forced, daily fees assessed |
| **Failing-to-Deliver Exposure** | [Counterparty risk](/wiki/counterparty-risk/) |

</aside>

## How settlement obligations work in practice

When you buy 100 shares of Apple for $15,000, the trade settles in two calendar days. On [T+2](/wiki/settlement-t2/):

- You must deliver $15,000 to the seller's [custodian](/wiki/custodian/).
- The seller must deliver 100 shares to your custodian.

This mutual obligation is simultaneous ("delivery versus payment," or DVP). If you don't have $15,000 in your account by settlement, your broker cannot deliver the shares—and you've violated your settlement obligation. Likewise, if the seller lacks the shares (perhaps they [shorted](/wiki/short-selling/) them), they cannot deliver.

The [clearing](/wiki/central-counterparty-clearing/) system (e.g., the [Depository Trust Company](/wiki/dtcc/)) stands as a [central counterparty](/wiki/central-counterparty-clearing/), netting all trades between thousands of brokers. This reduces bilateral risk but does not eliminate settlement obligations—it shifts them to the central clearer.

## Consequences of failing to settle

A "fail" occurs when one party does not deliver by the deadline. In equities:

1. The receiving party can force a buy-in—purchasing the shares in the open market and billing the failing party for any loss.
2. Daily penalty fees (typically 100 bps per annum, sometimes higher) accrue on the fail amount.
3. Extended fails trigger [regulatory](/wiki/sec-enforcement/) investigation, especially in [short-selling](/wiki/short-selling/) scenarios.

In fixed income, fails are more common because settlement occurs faster (T+1 or T+0) and bond market infrastructure is less standardized. A fail in government bonds can cascade, freezing [repo](/wiki/repurchase-agreement/) markets and credit channels. The 2008 financial crisis saw widespread fails as broker-dealers and banks struggled to locate collateral.

## Fails and naked short-selling

A settlement obligation is the enforcement mechanism against [naked short selling](/wiki/short-selling/) (selling shares you don't own and haven't borrowed). Under [Regulation SHO](/wiki/regulation-sho/), short sellers must "locate" shares they intend to sell—confirm a borrow exists. If no borrow is available, the seller cannot execute the short, and if they do anyway, they have breached their settlement obligation. Regulators can impose fines and bar traders.

[Fail-to-deliver](/wiki/fail-to-deliver-market-impact/) data is published weekly by the [SEC](/wiki/securities-and-exchange-commission/). Stocks with persistent fails (especially meme stocks during the GameStop saga) attract scrutiny.

## Settlement cycles and future shortenings

Historically, settlement took five business days (T+5). In 1993, it moved to T+3; in 2015, to T+2. Many industry participants want to move to T+1 or T+0 (same-day) to reduce [counterparty risk](/wiki/counterparty-risk/).

T+1 is technically feasible for equities—central clearing and electronic systems can process trades overnight. T+0 is harder because it requires instantaneous confirmation, payment, and delivery, which is impractical for global markets spanning time zones. However, crypto exchanges settle instantly (often in minutes or seconds) because blockchain settlement is atomic.

The [European Securities and Markets Authority](/wiki/european-banking-authority/) (ESMA) mandates T+2 for most securities but has explored T+1 pilots. The U.S. [SEC](/wiki/securities-and-exchange-commission/) has proposed T+1 but has not enforced it.

## Settlement risk and central clearing

Before [central counterparty clearing](/wiki/central-counterparty-clearing/) became universal, settlement risk was enormous. If Broker A failed to deliver shares to Broker B, Broker B simultaneously failed to pay and could face a [liquidity crisis](/wiki/liquidity-crisis/). The 1987 [Black Monday](/wiki/black-monday-1987/) crash nearly broke settlement systems because trading volume overwhelmed infrastructure.

The [CCP](/wiki/central-counterparty-clearing/) model (Broker A settles with CCP, CCP settles with Broker B) isolates bilateral risk. But the CCP now concentrates counterparty risk; if the CCP fails, all members fail. To mitigate this, [CCPs](/wiki/central-counterparty-clearing/) maintain:

- Multi-billion-dollar default funds
- Daily [mark-to-market](/wiki/mark-to-market/) and [margin](/wiki/maintenance-margin/) calls
- Strict [capital adequacy](/wiki/capital-adequacy/) rules

## Settlement in derivatives markets

[Derivatives](/wiki/derivative-accounting-hedging/) settlement is more varied:

- **Futures** settle daily (mark-to-market) at 4:00 pm CT, then the next day at open.
- **Options** on equities settle T+1 (American [options](/wiki/option/)) but can be exercised on last trading day.
- **Interest rate swaps** and [credit default swaps](/wiki/credit-default-swap/) settle via [novation](/wiki/novation-central-counterparty/)—the CCP interposes itself after trade initiation.

## Settlement obligation and international bonds

A U.S. Treasury bond settles T+1; a German Bund settles T+2. When a foreign investor buys a U.S. Treasury overseas (say, on an Asian electronic communication network), settlement may occur in New York [clearing](/wiki/central-counterparty-clearing/) or London [Euroclear](/wiki/euroclear/), creating [Herstatt risk](/wiki/herstatt-risk/)—the danger that payment and delivery occur in different time zones and one side fails. Modern [settlement](/wiki/settlement-procedures/) infrastructure (Continuous Linked Settlement, or CLS, for forex) has reduced this, but it persists in exotic currencies and off-the-run bonds.

<div class="wiki-seealso">

### Closely related
- [T+2 Settlement](/wiki/settlement-t2/) — Standard two-day settlement cycle for equities
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — The infrastructure that enforces settlement obligations
- [Fail-to-Deliver](/wiki/fail-to-deliver-market-impact/) — When settlement obligations are breached
- [Regulation SHO](/wiki/regulation-sho/) — Rules governing short-selling and locates

### Wider context
- [Counterparty Risk](/wiki/counterparty-risk/) — The risk of bilateral settlement failure
- [Depository Trust Company](/wiki/dtcc/) — The central custodian for U.S. securities
- [Repo Market](/wiki/repurchase-agreement/) — Short-term borrowing secured by settlement obligations

</div>
