---
title: "Credit Event (Sovereign)"
description: "Technical trigger of credit default swap payouts on sovereign bonds, defining when insurance on government debt pays off."
keywords:
  - credit default swap
  - sovereign bonds
  - distressed government debt
  - insurance mechanics
---

*A **credit event (sovereign)** is a contractually defined event that triggers payment on a [credit default swap](/wiki/credit-default-swap/) protecting against government debt default. Unlike corporate CDS, which have standardized triggers, sovereign CDS are negotiated bilaterally or defined by clearinghouse standards. The event typically includes failure to pay interest or principal, covenant breach, or restructuring of debt terms.*

<aside class="wiki-infobox">

| Event Type | Trigger | Recent Example |
|---|---|---|
| **Failure to pay** | Missing coupon or principal payment | Ukraine (2022) partial default on Eurobonds |
| **Acceleration** | Debt maturity accelerated by creditors | None common in sovereigns recently |
| **Repudiation** | Government explicitly rejects debt obligation | Greece (pre-2012, threatened) |
| **Restructuring** | Terms changed; creditors forced to accept less favorable terms | Greece (2012), Ukraine (2015) |
| **Moratorium** | Government imposes payment pause or capital controls | Argentina (2001), Cyprus (2013) |

</aside>

## Why CDS triggers matter: the payout race

A [credit default swap](/wiki/credit-default-swap/) is insurance on debt. If you own a Greek bond and buy CDS protection, you pay a premium (the "spread," often 1–5% annually). If Greece defaults, the CDS seller pays you the loss (100% of notional minus recovery value). But what counts as default? This is critical: if CDS protection does not pay when the government stops paying interest, the insurance is worthless.

The Dodd-Frank Act and ISDA standardized these definitions for corporate CDS in 2014, but sovereign CDS definitions vary. Most trades reference the "ISDA 2003 Definitions" with sovereign amendments, but interpretation disputes have occurred.

## Failure to pay: the clearest trigger

**Failure to pay** is the most straightforward trigger: the sovereign misses an interest coupon or principal payment. But there are nuances:

1. **Grace periods.** Many sovereign bonds have a grace period (typically 14–30 days) for late payment. CDS may or may not apply during grace periods, depending on contract language.

2. **Currency of payment.** If a government pays in local currency when the bond is denominated in USD, does it count as failure to pay? Argentina faced this ambiguity: it paid coupons in pesos when bonds were in dollars, and disputes erupted over whether CDS should pay.

3. **Selective default.** A government might default on some bonds but honor others. When Russia defaulted in 1998, it honored some foreign-currency debt while defaulting on ruble debt. CDS sellers argued there was no credit event because they held the honored bonds; CDS buyers disagreed.

## Restructuring: the most contentious trigger

**Restructuring** is the hardest to define. If a government offers creditors a choice—take 90 cents on the dollar today, or wait 10 more years for full repayment—is that a credit event? If creditors vote to accept the offer, is there a default?

Most sovereign CDS define restructuring narrowly: a *material* change in debt terms due to deteriorating credit. If the government voluntarily offers better terms (e.g., lower interest rate when credit improves), that is not restructuring. But if creditors are forced to accept worse terms, it is.

Greece's 2012 restructuring triggered intense CDS payout disputes. Creditors holding the bulk of Greek debt voted to accept a "haircut"—taking 50% losses. But some CDS sellers argued the restructuring was "voluntary" (creditors voted for it) and therefore not a credit event. The European authorities pushed for this interpretation to minimize systemic contagion from CDS payouts. Eventually, the ISDA rules committee ruled it was a credit event, but the dispute exposed fragility in the system.

## Repudiation and moratorium

**Repudiation** occurs when a government explicitly states it will not pay debt. This is rare in modern times; governments usually prefer to default de facto (stop paying) rather than de jure (declare repudiation), to preserve some negotiation room. Argentina in 2001 de facto defaulted but avoided explicit repudiation.

**Moratorium** is a government-imposed delay in payment—creditors are barred from drawing on accounts, or the government imposes capital controls. Cyprus in 2013 implemented capital controls and a moratorium on large payments, but this did not trigger CDS payouts because the government eventually resumed payment within weeks. The technical definition matters: CDS usually requires a prolonged moratorium (often 30+ days) to trigger.

## The sovereign CDS basis: pricing mispricing

Because triggering a credit event is ambiguous for sovereigns, CDS spreads often diverge from actual bond spreads. If the market thinks default is unlikely but CDS definition is narrow (low probability of payout), CDS spreads will be lower than the yields offered by the bonds. This is the **CDS basis**.

During the Euro crisis, Greek CDS spreads sometimes were *lower* than Greek bond yields, even though both were pricing default risk. The reason: investors feared CDS sellers would be bailed out or would dispute payouts, making CDS protection unreliable.

## Settlement: physical delivery vs. cash

When a credit event is ruled to have occurred, CDS settles. Most modern sovereign CDS settle in cash: the CDS seller pays the difference between par (100) and the "recovery value" (determined by auction of the underlying bonds). Older contracts allowed physical delivery—the CDS buyer delivers bonds and receives 100 cents on the dollar.

Ukraine's 2022 partial default illustrates the settlement challenge: some bondholders accepted losses; others held out. What is the "recovery value"? The auction process determines it, but the auction can be gamed or disputed.

## The systemic question: who bears the risk?

Because sovereign CDS can be used to speculate on default (buying protection without owning the debt), large CDS positions can create systemic risk. If a major financial institution writes billions in Greek CDS protection and Greece defaults, that institution faces massive losses that could trigger a cascade.

This is why regulators scrutinize sovereign CDS positioning and why central banks have sometimes intervened in CDS markets (e.g., the ECB's Outright Monetary Transactions program was partly designed to suppress Greek CDS spreads). The question remains unresolved: should CDS be allowed on sovereigns where the speculative component could destabilize the entire system?

<div class="wiki-seealso">

### Closely related
- [Credit Default Swap](/wiki/credit-default-swap/) — The insurance being triggered
- [Sovereign Default](/wiki/sovereign-default/) — The event being insured
- [Distressed Market](/wiki/distressed-market/) — Where CDS payouts are settled

### Wider context
- [Bond Covenants](/wiki/bond-covenants/) — Terms that govern default definitions
- [Debt Restructuring](/wiki/debt-restructuring/) — The negotiation post-default
- [Central Bank](/wiki/central-bank/) — Regulator of systemic CDS risk
- [Credit Risk](/wiki/credit-risk/) — The fundamental risk being priced

</div>
