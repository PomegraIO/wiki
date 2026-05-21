---
title: "SOFR"
description: "SOFR is the Secured Overnight Financing Rate, a risk-free benchmark interest rate based on actual overnight repo transactions, replacing USD LIBOR."
keywords:
  - SOFR
  - secured overnight financing rate
  - benchmark rate
  - repo
  - LIBOR replacement
image: "/svg/monetary.svg"
---

*The **SOFR** (Secured Overnight Financing Rate) is a benchmark [interest rate](/interest-rate) based on the volume-weighted median rate of secured overnight repo transactions in the US Treasury market. Published daily by the Federal Reserve, SOFR is designed to be a reliable, transaction-based replacement for [LIBOR](/libor) and is rapidly becoming the standard reference rate for USD-denominated financial contracts.*

<div class="wiki-hatnote">

This entry covers SOFR's mechanics and role. For its international counterparts, see [sonia](/sonia), [euribor](/euribor), [tonar](/tonar), and [ester](/ester). For the market it's based on, see [temporary-open-market-operations](/temporary-open-market-operations).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">SOFR — key facts</div>

<img src="/svg/monetary.svg" alt="SOFR rate calculation based on Treasury repo trades" />

<div class="wiki-infobox-caption">SOFR measures the actual cost of borrowing against Treasury collateral overnight.</div>

|   |   |
|---|---|
| **What it is** | Median rate of secured overnight repo transactions |
| **Published by** | Federal Reserve (based on DTCC/FICC data) |
| **Frequency** | Daily |
| **Based on** | Observable, actual market transactions |
| **Applies to** | Floating-rate notes, derivatives, mortgages, loans |
| **Launched** | June 2018 (publication); widespread adoption from 2021 |
| **Why created** | To replace LIBOR, which is based on estimates |

</aside>

## The advantage: real transactions

LIBOR was based on the guesses of a panel of [banks](/broker). A [bank](/broker) submitting LIBOR was saying "I think I could borrow at this rate," but it was not actually borrowing. SOFR is different: it is the median of *actual, observed* transactions in the overnight Treasury repo market.

Every day, major financial institutions lend Treasury securities and borrow cash against them. The Federal Reserve collects data on those transactions (via the Depository Trust & Clearing Corporation, which runs the main automated repo market). The Fed calculates the volume-weighted median rate and publishes it as SOFR. No guessing, no estimation, no room for manipulation.

This transaction-based approach makes SOFR far more reliable and harder to game than LIBOR ever was. A [bank](/broker) cannot move SOFR by submitting a false rate; SOFR is what it is, determined by the millions of dollars in real trades that happen overnight.

## How SOFR is calculated

The Federal Reserve collects data on Treasury repo transactions from the FICC (Fixed Income Clearing Corporation) tri-party repo platform and other sources. For each overnight transaction, the Fed records the amount and the rate. At the end of the day:

1. The Fed identifies all eligible overnight Treasury repo transactions.
2. It calculates the volume-weighted median rate (the midpoint rate where 50% of the dollar volume traded above and below).
3. It publishes SOFR the next morning.

The rate is published for overnight maturities. The Fed also publishes average rates for longer periods (30-day, 90-day, 180-day averages), which are derived from rolling SOFR data and used for floating-rate [bonds](/bond) and long-term contracts.

## The "secured" element

The "S" in SOFR stands for "Secured," meaning that the borrowers in these overnight repo transactions are pledging Treasury securities as collateral. This is important: a Treasury repo is safer than unsecured borrowing, because if the borrower defaults, the lender has securities to seize and liquidate.

This secured nature makes SOFR lower than [LIBOR](/libor) would be for the same maturity. LIBOR was (theoretically) for unsecured borrowing, so it carried a credit premium. SOFR, being backed by Treasuries, is nearly risk-free. The spread between SOFR and LIBOR (which were both published side-by-side during the transition) captured this credit risk, and that spread has been substantial.

## The transition from LIBOR to SOFR

For decades, [LIBOR](/libor) was the default reference rate in USD contracts. The 2011–2012 LIBOR manipulation scandal and the realization that LIBOR no longer reflected real borrowing costs made a transition urgent. In 2017, US regulators designated SOFR as LIBOR's successor.

The transition has been complex. New contracts are now being written in SOFR. Old contracts written in LIBOR are being amended, often with complex conversion rules (sometimes a simple spread adjustment, sometimes more elaborate formulas). The Financial Conduct Authority set the end of LIBOR publication (for most currencies and tenors) as December 31, 2021, though some LIBOR rates were extended to 2023 to ease the transition.

## SOFR term rates

Initially, SOFR was only published as an overnight rate (the actual overnight repo rate). But many financial contracts—mortgages, bonds, derivatives—need longer-term reference rates (3-month, 6-month). The Fed and private providers have created SOFR term rates by averaging overnight SOFR over rolling periods. These term rates allow longer-dated financial instruments to reference SOFR.

## See also

<div class="wiki-seealso">

### Closely related

- [LIBOR](/libor) — the rate SOFR replaces
- [SONIA](/sonia) — GBP equivalent
- [ESTER](/ester) — EUR equivalent
- [TONAR](/tonar) — JPY equivalent

### Wider context

- [Interest rate](/interest-rate) — what SOFR measures
- [Temporary open-market operations](/temporary-open-market-operations) — the repo market SOFR is based on
- [Federal Reserve](/federal-reserve) — the publisher
- [Bond](/bond) — instruments often priced off SOFR
- [Monetary policy](/monetary-policy) — context for interest rates

</div>
