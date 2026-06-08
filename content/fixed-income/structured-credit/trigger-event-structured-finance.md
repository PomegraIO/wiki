---
title: "Trigger Events in Structured Finance"
description: "Trigger events in structured finance are performance thresholds that automatically redirect cash flows or accelerate bond repayment when collateral deteriorates."
keywords:
  - trigger events structured finance
  - overcollateralization trigger
  - coverage ratio test
  - delinquency trigger
  - cash flow diversion securitization
  - performance-based event
---

*A **trigger event** in structured finance is a contractual threshold—such as a rise in delinquencies, a drop in [overcollateralization](/overcollateralization/), or a breach of an interest-coverage ratio—that automatically reorders the securitization's payment waterfall to protect senior noteholders. When a trigger is breached, cash that would normally flow to equity or servicer spread is diverted into loss reserves or accelerated repayment of bonds, giving investors an extra cushion before things get worse.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trigger Events in Structured Finance — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income and structured products." />

<div class="wiki-infobox-caption">Automatic circuit-breakers that shift risk when deals start to slip.</div>

|   |   |
|---|---|
| **Definition** | Objective metric breach that changes the payment waterfall |
| **Common types** | Delinquency %, overcollateralization ratio, loss severity, interest-coverage ratio |
| **Who monitors** | [Trustee](/trustee-role-in-securitization/); noteholders are notified |
| **Effect when breached** | Cash diverted from equity/spread to reserves or senior bond paydown |
| **Purpose** | Protect senior bonds by hardening cash flow priority when risk rises |
| **Reversibility** | Some triggers are one-way (irreversible once breached); others reset monthly |

</aside>

## Why Trigger Events Matter

In a healthy securitization, the originator or equity sponsor owns the "first loss" tranche and benefits from excess spread (the difference between what borrowers pay and what noteholders earn). This incentive—equity takes the first hit if the deal goes bad—aligns the sponsor's interests with investors'. But markets can move fast. A pool of mortgages can shift from performing to troubled in months, and collateral value can evaporate before anyone notices.

Trigger events are the securitization's insurance policy. They are automatic rules, written into the indenture, that force a protective response without needing a vote or waiting for the servicer's next report. When delinquencies spike, when overcollateralization crumbles, or when loss severity runs high, the waterfall reconfigures in real time, shifting cash away from the equity sponsor and locking it in reserves.

This protects senior noteholders. It also has a mild disciplinary effect on the originator: if the deal's performance falters, the equity sponsor is punished immediately by seeing its cash flows diverted.

## Overcollateralization (OC) Triggers

The most common trigger type is an overcollateralization breach. **Overcollateralization** is the ratio of the collateral's par (face) value to the par value of the bonds outstanding. If a pool of $100 million in mortgages backs $90 million in bonds, the deal has 11% overcollateralization (or an OC ratio of 1.11).

As loans default and are written down, the collateral pool shrinks. If the collateral drops to $98 million, the OC ratio falls to 1.09. The indenture sets a threshold—say, OC cannot fall below 1.05. If it does, a trigger is breached.

When an OC trigger is hit:

1. **The waterfall changes.** Normal waterfall might pay equity after all bonds. Triggered waterfall diverts all excess collections (principal prepayments, loss recoveries) to a reserve account or to senior bond paydown, bypassing the equity tranche entirely.
2. **The equity sponsor loses cash.** Instead of receiving its share of prepayments, those funds are locked away, reducing the equity sponsor's potential return.
3. **Senior noteholders get an extra principal paydown.** By paying down senior bonds faster, the deal's liability shrinks, and the remaining overcollateralization improves.

Once the OC ratio is restored above the threshold, the trigger often resets, and normal waterfall resumes. (Some indentures use "sticky" triggers that reset at a slightly higher level, to prevent constant flipping.)

## Delinquency Triggers

Another frequent trigger is a **cumulative delinquency threshold**. For example:

- If loans 30+ days late exceed 3% of the pool, a trigger is breached.
- If loans 60+ days late exceed 2%, an even stricter condition is met.
- If losses (charge-offs) exceed 5% cumulative, the deal enters "loss mitigation" mode.

Delinquency triggers are forward-looking: rising delinquencies signal that losses are likely to follow. By triggering on delinquency before the losses hit, the securitization forces a defensive stance earlier.

When a delinquency trigger is breached, the [trustee](/trustee-role-in-securitization/) steps up monitoring, may require more frequent reports, and may redirect cash to loss reserves. Some indentures allow the trustee to replace the servicer or freeze new cash distributions to equity if delinquencies stay high for long.

## Interest-Coverage Ratio (ICR) Triggers

In securitizations backed by floating-rate assets (adjustable mortgages, bank loans), an **interest-coverage ratio** trigger is common. This ratio compares the interest collected from the collateral to the interest owed on the bonds.

An ICR of 1.10 means that the collateral generates 10% more interest than the bonds require. If rates drop, the collateral's interest income falls (if it resets downward) but the bonds' coupon may stay fixed, compressing the ratio. If the ICR breaches a threshold (e.g., below 1.05), the waterfall changes to prioritize interest reserve accumulation over equity or servicer fees.

ICR triggers protect against a slow-motion squeeze where collateral coupons fall but liabilities remain constant.

## Loss Severity and Recovery Triggers

Some securitizations—particularly those backed by corporate loans or distressed assets—use **loss severity** triggers. These track what percentage of defaulted loans are recovered through sale, restructuring, or workout.

If the average loss severity exceeds an indenture threshold (e.g., more than 50% of par is lost on each default), a trigger may be breached, signaling that the collateral is worse than underwritten. This forces a shift to loss mitigation and may restrict the servicer's discretion in loan modifications.

## One-Way vs. Reversible Triggers

Most triggers reset monthly or quarterly if the condition improves. Delinquency and OC triggers often fall into this category: the waterfall changes this month, but if delinquencies fall next month, normal waterfall may resume.

However, some triggers are **one-way**: once breached, they remain in effect for the remainder of the deal's life. An example might be a "weighted-average maturity" trigger: if the [weighted average life](/weighted-average-life-abs/) of the collateral pool extends beyond a stated limit (due to lower-than-expected prepayments), the deal enters a "portfolio rebalancing" mode for the rest of its term.

One-way triggers are more punitive but provide unambiguous protection to noteholders. They also simplify the indenture: there is no ambiguity about when a condition is "cured."

## Trigger Levels and Deal Design

The indenture specifies exact trigger thresholds, and these are typically calibrated during deal structuring:

| Collateral type | Typical OC trigger | Typical delinquency trigger |
|---|---|---|
| Prime residential mortgages | 1.03–1.05 | 3–4% (30+ days late) |
| Subprime mortgages | 1.08–1.15 | 2–3% (30+ days late) |
| Auto loans | 1.02–1.04 | 2–3% (30+ days late) |
| Credit card receivables | 1.10–1.15 | 1–2% (60+ days late) |
| Commercial real estate loans | 1.05–1.10 | 1–2% (60+ days late) |

Riskier collateral gets higher (more conservative) trigger thresholds, because the risk of rapid deterioration is higher. A subprime-mortgage securitization might trigger at 8% OC, while a prime deal triggers at 3%, reflecting the difference in expected loss.

## Triggers in Practice: Enforcement and Disputes

In principle, triggers operate automatically. The trustee monitors collateral metrics monthly, detects a breach, and notifies noteholders. The waterfall changes accordingly.

In practice, disputes arise:

- **Calculation disagreements.** Did the servicer measure delinquency correctly? Are loss recoveries properly reflected in the OC calculation? Indentures define these methodologies carefully, but gray areas persist.
- **Timing.** Some triggers require two months of breach before activating (a "stability" feature to avoid whipsaw). Others activate immediately. Investors disagreed with trustees over when to count the breach as "real."
- **Remediation pressure.** Equity sponsors have incentives to avoid trigger breaches and may pressure servicers to be lenient on modifications, deferrals, or loss recognition. Noteholders and trustees must police this.

During the 2008–2009 mortgage crisis, trigger disputes were common. Many servicers disputed whether delinquencies had actually breached thresholds; some trustees were criticized for accepting servicer certifications without verification. Post-crisis regulation tightened trustee verification, but resource constraints remain.

## See also

<div class="wiki-seealso">

### Closely related

- [Trustee Role in Securitization](/trustee-role-in-securitization/) — The entity that monitors triggers and enforces waterfall changes
- [Overcollateralization](/overcollateralization/) — The protective cushion most commonly used as a trigger metric
- [Weighted Average Life in Asset-Backed Securities](/weighted-average-life-abs/) — A structural metric that can itself be a one-way trigger
- [Conditional Prepayment Rate (CPR) Explained](/conditional-prepayment-rate-explained/) — Prepayment assumptions affect overcollateralization and may trigger circuit-breakers

### Wider context

- [Mortgage-Backed Security](/mortgage-backed-security/) — Trigger events are especially important in residential mortgage pools
- [Securitization](/securitization/) — The parent structure within which triggers operate
- Asset-Backed Security — General framework for collateral-backed bonds with trigger protection
- [Cash Flow Statement](/cash-flow-statement/) — The trustee uses cash-flow data to monitor triggers

</div>
