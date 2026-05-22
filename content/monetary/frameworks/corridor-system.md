---
title: "Corridor System"
description: "Framework where market interest rates float within central bank-defined bounds, maintaining operational control without fixing rates."
keywords:
  - corridor system
  - interest rate corridor
  - central bank floor
  - central bank ceiling
  - monetary policy framework
---

*A **corridor system** is a monetary policy implementation framework where the central bank sets upper and lower bounds on market interest rates, rather than a single target. The market [interbank lending rate](/wiki/interbank-lending-rate/) (or policy rate) fluctuates within the corridor based on supply and demand, while central bank operations—offering loans at the ceiling and paying interest on deposits at the floor—keep rates from breaching the bounds.*

<div class="wiki-hatnote">
For the Fed's specific framework, see [Federal funds rate](/wiki/federal-funds-rate/) and [Discount window](/wiki/discount-window/). This entry covers the general corridor architecture used by many central banks.
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Central Ceiling** | Standing lending facility (e.g., Discount window) at penalty rate |
| **Central Floor** | Interest paid on excess reserves (IORR/IOER) |
| **Target Rate** | Usually the midpoint of the corridor |
| **Corridor Width** | Typically 50–100 bps (25 bps on each side of midpoint) |
| **Advantage** | Operational control without daily intervention |
| **Disadvantage** | Requires active reserve management by banks |
| **User Jurisdictions** | ECB, Bank of England, Bank of Canada, Swiss National Bank |

</aside>

## Core mechanics

The central bank announces a "standing facility corridor" consisting of two rates:

1. **Lending rate (ceiling)**: Banks can borrow unlimited amounts from the central bank at this rate, typically 25–50 bps *above* the target rate.
2. **Deposit rate (floor)**: Banks earn this rate on excess reserves held at the central bank, typically 25–50 bps *below* the target rate.

Between these bounds, the [interbank lending rate](/wiki/interbank-lending-rate/)—the rate at which banks lend to each other—fluctuates based on supply and demand for reserves. If banks are short of reserves and willing to pay high rates to borrow from each other, the interbank rate may rise toward the ceiling. If banks have excess reserves, the rate falls toward the floor.

The corridor constrains these moves: a bank that sees the interbank rate rise above the ceiling will prefer to borrow from the central bank at the fixed ceiling rate rather than pay more on the interbank market. Conversely, if the interbank rate falls below the floor, banks will prefer to deposit reserves at the central bank at the floor rate rather than lend them at lower rates to each other.

This *automatic* stabilization—without the central bank actively trading or managing the exact quantity of reserves—is the corridor system's key advantage.

## Historical context

The corridor system was formalized in the 1990s and 2000s, replacing earlier frameworks where central banks directly targeted a quantity of reserves and let the rate float. The shift reflected recognition that targeting quantity was unwieldy in modern, sophisticated banking systems.

The **European Central Bank (ECB)** adopted a corridor system from its inception in 1999. The [Bank of England](/wiki/bank-of-england/) switched to a corridor in 2006. The **Federal Reserve** operated a target range (a corridor with a 25 bp width) from 2009–2020 and again from 2022 onward, though for decades before 2009 the Fed used a point target (not a range).

## The Fed's framework

From 2009 to 2020, the Fed operated a **target range** for the [federal funds rate](/wiki/federal-funds-rate/), essentially a 25 bp corridor (e.g., 0.00%–0.25% in the zero-rate period). With rates at zero, the lower bound could not go lower, so the Fed relied more on [quantitative easing](/wiki/quantitative-easing/) (large-scale asset purchases) to inject liquidity.

In 2020, the Fed added an additional tool: it expanded [standing reverse repo facilities](/wiki/reverse-repo/) that allowed non-bank institutions (money market funds, securities dealers) to deposit funds with the Fed at a guaranteed rate. This extended the corridor to a wider set of market participants and helped stabilize short-term rates during market stress.

Since rates normalized in 2022, the Fed has operated a 25 bp corridor (e.g., 5.00%–5.25% when rates are higher), with the upper bound enforced by the [discount window](/wiki/discount-window/) and the lower bound by [interest on reserves](/wiki/interest-on-required-reserves/).

## Advantages of the corridor system

1. **Operational simplicity**: The central bank does not need to compute and trade the precise quantity of reserves daily. The corridor bounds are published, and markets self-correct.

2. **Flexibility**: If banks unexpectedly need more reserves, they can borrow from the central bank at the ceiling rate. If they have excess, they deposit at the floor rate. No artificial shortage or surplus.

3. **Transmission clarity**: Market participants understand that the central bank's policy is defined by the corridor bounds, not by quantity targets. Policy shifts (widening or narrowing the corridor, or moving the midpoint) are unambiguous.

4. **Risk management**: The corridor prevents extreme short-term rate spikes that might trigger financial instability (e.g., a money market fund unable to roll [commercial paper](/wiki/commercial-paper/) due to rate shock).

## Challenges and constraints

**Zero lower bound**: When target rates approach zero, the deposit rate (floor) cannot go lower without being negative (and even negative rates face political and operational resistance). The ECB and Swiss National Bank have experimented with negative rates (−0.5% to −0.75%), but this induces financial instability and asset-substitution effects.

**Reserve management complexity**: During periods of low rates and large central bank balance sheets (post-2008), banks accumulated vast reserves, and the spread between floor and ceiling became less binding. The Fed had to actively manage reserve supply via [quantitative tightening](/wiki/quantitative-tightening/) (gradually selling assets) to avoid oversupply.

**Corridor width precision**: Too narrow a corridor (5 bp) can amplify volatility if reserve supply is uncertain. Too wide (200 bp) gives little operational guidance. The optimal width depends on banking system liquidity and central bank asset size.

## Alternative frameworks

- **Quantity targeting**: The pre-1990s approach. The central bank fixes the quantity of reserves; the rate floats based on demand. Prone to volatility and harder to control.
- **Point target**: A single rate target with trading *around* it. The Fed used this before moving to ranges. Requires continuous central bank intervention.
- **Inflation targeting**: Many modern central banks (Reserve Bank of New Zealand, Norges Bank) use inflation as the ultimate target and let the policy rate float to hit that target. The corridor system is often embedded within an inflation-targeting regime.

## Modern adjustments

During the COVID-19 pandemic (2020) and subsequent [quantitative easing](/wiki/quantitative-easing/), central banks operated with massive balance sheets and overabundant reserves. The traditional corridor became less effective at controlling rates because the floor (IORR) was often the binding constraint.

The Fed responded by creating:

- **Standing reverse repo facility**: Banks and money market funds can place reserves with the Fed at a fixed rate (just below the IORR), extending the corridor to non-bank players.
- **Tiered IORR**: Different rates for different tranches of reserves, to encourage lending.

These adjustments reflect the reality that corridor systems must evolve as financial markets change.

<div class="wiki-seealso">

### Closely related

- [Federal funds rate](/wiki/federal-funds-rate/) — The US rate operating within a corridor.
- [Interest on excess reserves](/wiki/interest-on-excess-reserves/) — The floor of the corridor.
- [Discount window](/wiki/discount-window/) — The ceiling lending facility.

### Wider context

- [Monetary policy transmission](/wiki/monetary-transmission-mechanism/) — How corridor changes affect the economy.
- [Interest rate corridor](/wiki/interest-rate-corridor/) — Synonym and related concept.
- [Quantitative easing](/wiki/quantitative-easing/) — Alternative tool when corridor becomes less effective.

</div>
