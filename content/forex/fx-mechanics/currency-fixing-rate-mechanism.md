---
title: "How Daily Currency Fixing Rates Are Set"
description: "How daily currency fixing rates are set: sampling, calculation windows, and why corporations use benchmark fixes for revaluation and settlement."
keywords:
  - currency fixing rate
  - daily currency fix
  - wm/reuters fix
  - benchmark exchange rate
  - spot fixing
  - fx fixing methodology
---

*The **daily currency fixing rate** is a standardized exchange rate, typically calculated once or twice per day, that banks, corporations, and custodians use to revalue foreign-currency balances and settle cross-border payments. The most widely used fix is the WM/Reuters 4 p.m. London fix, which samples actual trades and indicative prices over a fixed window and publishes the resulting benchmark — a single rate that brings certainty and comparability to how trillions of dollars in assets are marked.*

## Why a Single Daily Rate Matters

Foreign exchange trades 24 hours a day across time zones, with no central exchange. A dollar might trade at 1.0950 EUR/USD at 8 a.m. in Tokyo and 1.0945 at 4 p.m. in London the same day. Without an agreed-upon benchmark, each bank would value the same currency position differently, creating audit and reporting chaos.

Daily currency fixes solve this: they define a single "official" rate that applies to all participants during a defined accounting period (usually a calendar day). A multinational corporation that holds €10 million can report a consistent USD equivalent across all its subsidiaries. Pension funds revalue their foreign holdings at the same rate. Settlement systems can execute transactions using a known, published benchmark instead of a disputed rate.

## The WM/Reuters 4 p.m. London Fix: The Global Standard

The WM/Reuters fix, now operated by Refinitiv (following acquisition of Reuters), is the most quoted daily rate globally for major pairs like EUR/USD, GBP/USD, and JPY/USD. It is published once at 4 p.m. London time each business day.

**The calculation window**: The fix is based on a **one-minute sampling window** — usually 4:00 to 4:01 p.m. London time — during which the algorithm captures:

- **Actual spot trades** executed on major electronic venues (EBS, Refinitiv Matching, and over-the-counter dealer platforms)
- **Indicative quotes** (bid and offer prices) from top-tier banks

Within that one-minute window, the algorithm ranks trades and quotes by time and price, then applies a weighting method that reflects market depth and participant creditworthiness. The result is a single midpoint rate that is published within 10–15 seconds of the window close.

## Why a One-Minute Window?

A longer window would dilute the benchmark by averaging across different market conditions; a shorter one might miss sufficient volume. One minute has proven to strike a balance: it is tight enough to capture a genuine snapshot of market consensus, yet wide enough to gather meaningful data even on days with lighter trading. The algorithm is transparent: Refinitiv publishes the methodology and weights, and independent auditors verify execution annually.

## How Corporations and Banks Use the Fix

On any given day, a corporate treasury department that receives a large EUR-denominated payment will use the WM/Reuters 4 p.m. fix (or a close variant, such as the ECB's 1 p.m. Frankfurt fix) to convert that payment into USD for book purposes. If a company's accounting cutoff is 4:30 p.m. London time, using the 4 p.m. fix ensures that foreign-exchange gains and losses are marked consistently.

Large institutional investors also rely on the fix: a pension fund's custodian bank will use the fix to revalue its foreign-currency positions at month-end, and the fund reports those valuations to its clients. The fix removes ambiguity about which rate was used — and disputes over whether a particular rate was fair.

## Other Fixing Benchmarks

While WM/Reuters dominates, other fixes serve specific markets or regions:

- **ECB Fix (1 p.m. Frankfurt time)**: The European Central Bank publishes daily rates for EUR pairs, used in eurozone financial reporting and some European corporate practices.
- **Hong Kong Fixing (9:30 a.m. HKD time)**: The Hong Kong Association of Banks publishes USD/HKD, used in Hong Kong settlement systems.
- **Bank of Japan Fixing (Tokyo Fix)**: Applied for JPY pairs.
- **SONIA/SOFR-based forwards**: For outright forwards, some institutions now use overnight rate benchmarks rather than traditional spot fixes.

## The Concern: Manipulation and Its Remedy

In the years after the 2008 financial crisis, large banks were found to have attempted to manipulate the WM/Reuters fix to profit on positions held during the fixing window. A subset of dealers would coordinate to push the 4 p.m. rate in a favorable direction. The discovery led to hundreds of millions in fines and regulatory overhaul.

Today, the fixing process includes:
- **Audit trails**: Every trade and quote used in the calculation is recorded with timestamps.
- **Algorithmic transparency**: Refinitiv's weighting rules are public and non-discretionary.
- **Surveillance**: Regulators in the UK (FCA) and US (CFTC) monitor for collusion.
- **Contributor code of conduct**: Banks must attest to fair-dealing protocols when providing quotes.

These safeguards have made manipulation harder, though occasional enforcement actions remind participants that scrutiny continues.

## Time-of-Day and Your Bottom Line

The timing of the fix is not arbitrary. The 4 p.m. London fix occurs during a window when London, New York, and Tokyo markets all have meaningful overlap or active participation. A fix timed at 3 a.m. Sydney time would miss most Australian and Asian participants. The 4 p.m. choice ensures that the largest liquidity pool — the presence of both European and US market makers — is captured, yielding a robust and representative rate.

For any organization that must value foreign assets or settle international payments, understanding which fix applies and when it is published prevents settlement delays and avoids unpleasant surprises when a payment is converted at an unexpected rate.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the difference between buy and sell prices that shrinks at the published fix
- [Spot exchange rate](/spot-exchange-rate/) — the rate for immediate delivery, which the fixing rate approximates
- [Market maker](/market-maker-trading/) — dealers who quote during the fixing window
- [Currency volatility](/currency-volatility/) — why fixing windows are prone to intraday moves
- [Over-the-counter market](/over-the-counter-market/) — where most spot trades that feed the fix occur

### Wider context

- [Exchange rate](/stock-exchange/) — how rates relate to broader exchange mechanics
- [Settlement](/secondary-market/) — the use of fixes in payment settlement
- [Regulatory framework](/finra/) — how fixing conduct is now overseen

</div>
