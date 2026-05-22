---
title: "Overnight Rate Mechanism"
description: "The interest rate on unsecured overnight lending between banks, a fundamental rate that anchors short-term money market pricing."
keywords:
  - overnight lending
  - interbank rate
  - fed funds rate
  - money market
  - short-term borrowing
  - central bank policy
---

*The **overnight rate mechanism** governs the [interest rate](/wiki/interest-rate/) paid on unsecured loans between banks that mature the next business day, serving as the foundation for [central bank](/wiki/central-bank/) policy implementation and the anchor for broader [money market](/wiki/money-market-fund/) pricing.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Maturity** | Overnight (1 business day) |
| **Type** | Unsecured lending (no collateral) |
| **Key US rate** | [Federal funds rate](/wiki/federal-funds-rate/) (target 0–5.5% range as of 2024) |
| **Key euro rate** | EONIA (now linked to SOFR-like mechanisms) |
| **Key UK rate** | SONIA (Sterling Overnight Index Average) |
| **Key Japan rate** | TONAR (Tokyo Overnight Average Rate) |
| **Volatility** | Low in normal times; spikes in stress (2008, 2019) |
| **Central bank tool** | Directly influenced through [open market operations](/wiki/open-market-operations/) and corridor systems |

</aside>

## Why overnight lending exists

Banks need liquidity daily. A bank receiving deposits or selling securities gains cash; another bank faces unexpected outflows or needs to meet [reserve requirements](/wiki/reserve-requirements/). Rather than holding large idle cash buffers, banks lend to each other overnight, settling the next morning when one bank's inflows may balance another's outflows.

This overnight interbank lending market is huge—trillions of dollars turn over globally each day. The rate at which these loans trade becomes a signal of **financial system health** and **monetary policy stance**. When overnight rates are elevated, banks are nervous about counterparty risk or liquidity; when depressed, confidence is high and [excess reserves](/wiki/interest-on-excess-reserves/) are ample.

The overnight rate is the first and most direct channel through which central banks transmit policy. By controlling the rate banks charge each other overnight, the central bank influences the entire [yield curve](/wiki/yield-curve/) and credit conditions.

## Central bank targeting and corridor systems

The [Federal Reserve](/wiki/federal-reserve/) does not directly set the [federal funds rate](/wiki/federal-funds-rate/)—it targets a range (currently 4.5–5.5%, adjusted based on [inflation](/wiki/inflation/) and employment). Instead, the Fed uses two tools to keep the actual rate within its target band:

**1. [Interest on excess reserves (IONER)](/wiki/interest-on-excess-reserves/):** The Fed pays interest on reserves banks hold at the Fed. If the Fed pays 5.25% on reserves, banks are unlikely to lend to each other at lower rates; the **floor** on overnight rates is roughly IONER.

**2. [Reverse repo facility (RRP)](/wiki/reverse-repo-facility/):** The Fed offers a fixed-rate overnight repo facility (currently 5.3%). Banks and money market funds can park excess cash here; this acts as a **ceiling** on overnight rates (why lend to another bank at 5.5% when you can lend to the Fed at 5.3%?).

The spread between the floor (IONER) and ceiling (RRP) creates a narrow corridor. Actual fed funds trades settle within this band, anchored by the midpoint (the Fed's **target rate**).

Internationally, other central banks use similar mechanisms:
- **ECB:** Deposit rate (floor) and lending facility rate (ceiling) around its main refinancing rate.
- **Bank of England:** Bank rate with similar corridor structure using SONIA (Sterling Overnight Index Average).
- **Bank of Japan:** Policy rate corridor with unsecured overnight repo as anchor.

## How the overnight rate transmits to longer-term rates

The overnight rate directly impacts short-term rates (one week, one month, three months) because investors demand compensation for duration risk. A three-month rate is roughly the expected average of overnight rates over the next three months plus a [term premium](/wiki/term-premium/).

If the Fed raises overnight rates to 5%, market participants expect sustained tightness; three-month rates rise to 4.8–5.0%. Longer-term rates (10-year [Treasury yields](/wiki/yield-to-maturity/)) rise more modestly because they incorporate expectations that rates will eventually fall again. This creates a **[yield curve](/wiki/yield-curve/)** that slopes upward (longer rates higher) in normal times.

The overnight rate is also the input for pricing:
- **Floating-rate bonds** (coupons reset daily or weekly based on overnight or short-term rates)
- **[Interest rate swaps](/wiki/interest-rate-swap/)** (banks exchange fixed for floating SOFR/SONIA)
- **Derivatives** (options and futures on short-term rates)

A 0.25% change in overnight rates triggers repricing across trillions in derivatives positions, making central bank policy highly sensitive.

## Crisis behavior and rate spikes

In normal times, overnight rates trade in a tight band around the central bank's target. But during financial stress, the overnight rate can spike dramatically:

**2008 financial crisis:** The fed funds rate target was slashed to 0–0.25%, but actual overnight rates sometimes traded above the target as banks hoarded cash and refused to lend to each other (counterparty risk panic). The Fed had to intervene by expanding [reverse repo](/wiki/reverse-repo-facility/) and [discount window](/wiki/discount-window/) access to stabilize overnight lending.

**September 2019 repo crisis:** A technical shortage of collateral and a surprise surge in Treasury issuance strained the overnight repo market. Overnight rates spiked to 10% (far above the Fed's 2% target). The Fed flooded the market with liquidity through reverse repo and open market operations, calming the market within days.

**COVID-19 pandemic (March 2020):** Overnight rates again spiked temporarily as financial stress and forced selling of securities drained liquidity. The Fed's emergency [quantitative easing](/wiki/quantitative-easing/) and repo facility brought rates back to target.

These episodes show that **overnight rate control is not automatic**—it requires active central bank management and sufficient [liquid collateral](/wiki/liquidity-pool/) in the system.

## Transition from LIBOR to SOFR and similar benchmarks

Historically, the London Interbank Offered Rate ([LIBOR](/wiki/libor/)) served as the global benchmark for unsecured short-term lending. But LIBOR was based on estimates from a panel of banks and was manipulated during the 2008 crisis (fines exceeding $9 billion were levied). Regulators moved to **transaction-based** overnight rates:

- **US:** [SOFR (Secured Overnight Financing Rate)](/wiki/sofr/) — actual overnight repo transactions (secured by Treasury collateral)
- **UK:** SONIA — actual overnight unsecured interbank transactions
- **EU:** EONIA replaced by euro short-term rate (€STR)
- **Japan:** TONAR — actual overnight repo transactions

These new rates are more transparent and harder to manipulate because they are derived from actual market transactions, not estimates. However, [SOFR](/wiki/sofr/) is transaction-based rather than unsecured rate, creating a conceptual shift: it measures Treasury-secured rates rather than bank counterparty risk, which was what traditional LIBOR measured.

## Implications for borrowers and savers

For borrowers, the overnight rate matters indirectly:
- **Mortgage rates** reset based on short-term indices (SOFR, SOFR + spread)
- **Credit card rates** track prime rate, which moves with overnight rates
- **Auto loans** often float with short-term benchmarks

For savers:
- **Money market funds** yield roughly the overnight rate minus a small expense ratio
- **Savings accounts and CDs** track overnight/short-term rates loosely

A 0.5% move in the overnight rate eventually cascades into 0.4–0.5% changes in consumer lending and deposit rates over 3–6 months as banks adjust.

<div class="wiki-seealso">

### Closely related
- [Federal Funds Rate](/wiki/federal-funds-rate/) — US overnight rate target and mechanism
- [Interest on Excess Reserves](/wiki/interest-on-excess-reserves/) — floor on overnight lending
- [Reverse Repo Facility](/wiki/reverse-repo-facility/) — ceiling on overnight lending
- [SOFR](/wiki/sofr/) — replacement for LIBOR; transaction-based overnight rate

### Wider context
- [Central Bank Policy Tools](/wiki/central-bank-policy-tools/) — instruments for monetary control
- [Monetary Policy](/wiki/monetary-policy/) — control of money and credit
- [Interest Rate](/wiki/interest-rate/) — cost of borrowing
- [Yield Curve](/wiki/yield-curve/) — relationship between maturity and rate

</div>
