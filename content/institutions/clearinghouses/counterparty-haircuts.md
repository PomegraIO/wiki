---
title: "Counterparty Haircuts"
description: "Margin discounts applied to collateral pledged to clearinghouses and central counterparties."
keywords:
  - haircut
  - collateral discount
  - counterparty risk
  - clearing margin
---

*A **haircut** is a percentage discount applied to the value of collateral pledged to a clearinghouse, central counterparty, or prime broker. If you deposit $100 million in Treasury bonds as collateral, a 2% haircut means the clearinghouse credits you only $98 million in purchasing power. The haircut absorbs potential losses from price declines and protects the clearinghouse and other participants if the pledging firm defaults. Haircuts vary by asset class, volatility, and liquidity risk.*

<aside class="wiki-infobox">

| Asset Class | Typical Haircut Range |
|---|---|
| **U.S. Treasuries (short-dated)** | 0.5% – 2% |
| **U.S. Treasuries (long-dated)** | 2% – 5% |
| **Investment-grade corporates** | 3% – 8% |
| **High-yield bonds** | 8% – 20% |
| **Equities** | 15% – 30% |
| **Emerging-market securities** | 10% – 25% |

</aside>

## Why clearinghouses impose haircuts

A clearinghouse stands between buyers and sellers, guaranteeing each side's obligation. If a seller defaults before delivery, the clearinghouse must cover the loss. Collateral—typically cash or securities—is the first line of defense. A haircut ensures that even if the collateral declines in value, it will cover the gap.

The haircut's magnitude reflects the risk of rapid price loss. U.S. Treasuries are highly liquid and rarely suffer large daily moves, so haircuts are small (0.5% to 2%). High-yield bonds are less liquid and more volatile, so haircuts are larger (10% to 20%). A sudden market dislocation can widen spreads and create forced selling; the haircut cushions this scenario.

## Haircut mechanics and margining

When you open a derivatives [futures](/wiki/futures-contract/) or cleared swap position with a clearinghouse, you post initial margin (collateral). The clearinghouse applies haircuts to reduce the credited value. If you post $1 million in AAA corporate bonds with a 5% haircut, you get $950,000 in margin buying power.

As your position gains or loses value, variation margin adjusts daily. If your [futures](/wiki/futures-contract/) position loses $10,000, the clearinghouse demands an additional $10,000 in collateral. If the posted collateral's market value falls (e.g., a bond declines 2% due to rising rates), the haircut adjusts upward to reflect the new discount needed. This dynamic margining prevents the clearinghouse from bearing losses.

## The 2008 crisis and haircut spikes

During the 2008 financial crisis, haircuts spiked dramatically. Securities that normally carried a 2% haircut suddenly faced 20% or more. This forced institutions to post far more collateral or liquidate positions. A prime broker lending money against MBS collateral at a 5% haircut suddenly demanded a 30% haircut—instantly shrinking the client's available leverage. Firms scrambled for cash, fueling fire sales. Haircut spikes became self-reinforcing: as assets sold off, haircuts rose further, forcing more liquidations.

This procyclical behavior—haircuts rising when they're most burdensome—is a key source of financial contagion. Regulators now pay close attention to haircut dynamics to prevent similar spirals.

## Regulatory framework and standardization

After 2008, regulators introduced rules requiring clearinghouses to set haircuts conservatively and update them frequently as volatility changes. The Securities and Exchange Commission and Commodity Futures Trading Commission oversee [central counterparty clearing](/wiki/central-counterparty-clearing/) firms. Under Dodd-Frank, new derivatives must be cleared through approved CCPs, making haircut policy a macroprudential tool.

Basel III regulations also set minimum haircuts for [repo](/wiki/repurchase-agreement/) transactions and securities lending, limiting the amount of leverage participants can obtain against any given asset. The goal is to ensure resilience: even in stress, haircuts don't spike so suddenly that forced liquidations cascade.

## Haircuts in repo and prime brokerage

A bank lending cash in a [repo](/wiki/repurchase-agreement/) transaction (purchasing securities with an agreement to repurchase) applies haircuts to securities provided as collateral. A dealer purchasing $100 million of corporate bonds via repo might require the bond seller to post $105 million in collateral, implying a -5% haircut (the bond seller can only borrow 95% of the bond's value). If the bond price falls 3%, the effective haircut rises to 8%, and the borrower must post additional collateral.

Prime brokers use haircuts to protect themselves from client defaults. If a hedge fund posts $10 million in collateral against which the prime broker allows $8 million in leverage (20% haircut), and the collateral loses 15% in value, the fund is nearly margin-called. The haircut provides breathing room.

## Collateral disputes and disputes resolution

During stress, disputes arise over haircuts. A client believes their collateral deserves a lower haircut; the counterparty disagrees. This friction can trigger [counterparty risk](/wiki/counterparty-risk/) concerns, especially if a large client is unable to access funds they believed were credit-available. Clearinghouses maintain dispute-resolution procedures and publish detailed haircut methodologies to minimize ambiguity.

Some institutions negotiate bespoke haircuts based on relationship and credit quality. A large, investment-grade bank posting securities might secure a lower haircut than a smaller or riskier counterparty posting identical assets. This adds complexity and potential for favoritism, which regulators monitor.

## Haircut models and volatility assumptions

Clearinghouses typically model haircuts using historical volatility and stress scenarios. The LCH, CME, and ICE each maintain haircut frameworks. A common approach: take the 99th percentile of daily price changes over a historical period, add a buffer, and apply that as the haircut. As volatility rises, haircuts mechanically increase. In low-volatility regimes, haircuts compress, providing more leverage. This is beneficial for normal markets but creates risk: haircuts that are too small for the actual tail risks present.

Regulators require clearinghouses to stress-test their haircut models against historical crises (2008, the 1998 LTCM collapse, March 2020) to ensure they would be adequate in stress.

<div class="wiki-seealso">

### Closely related
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — The CCP framework
- [Counterparty Risk](/wiki/counterparty-risk/) — The risk haircuts mitigate
- [Repurchase Agreement](/wiki/repurchase-agreement/) — Collateralized lending using haircuts

### Wider context
- [Initial Margin](/wiki/initial-margin/) — Collateral posted upfront
- [Variation Margin](/wiki/variation-margin-daily/) — Daily adjustments to margin
- [Financial Regulation](/wiki/financial-regulation-and-supervision/) — Oversight of haircut policy

</div>
