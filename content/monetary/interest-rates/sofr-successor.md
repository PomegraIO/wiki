---
title: "SOFR Successor"
description: "The Secured Overnight Financing Rate, the Federal Reserve's replacement for LIBOR—a transaction-based benchmark for overnight secured lending that underpins trillions in derivatives and floating-rate bonds."
keywords:
  - SOFR
  - interest rate benchmark
  - LIBOR replacement
  - overnight rate
---

*The **SOFR Successor** (properly called the Secured Overnight Financing Rate, though commonly referred to as the successor to [LIBOR](/wiki/libor/)) is the Federal Reserve's preferred [interest rate](/wiki/interest-rate/) benchmark for unsecured and secured overnight lending in US dollar markets. It replaced LIBOR on January 1, 2022, as the primary reference rate for new [floating-rate bonds](/wiki/floating-rate-bond/), [interest-rate swaps](/wiki/interest-rate-swap/), and [derivatives](/wiki/derivative-accounting-hedging/). SOFR is computed from actual transactions in the [repurchase market](/wiki/repurchase-agreement/) (the "repo" market, where banks borrow and lend using [Treasury](/wiki/treasury-bond/) securities as collateral) and is therefore more resilient to manipulation and credit shocks than the defunct LIBOR, which relied partly on panel bank submissions.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Full name** | Secured Overnight Financing Rate |
| **Launched** | April 2018 (SOFR publication began); full transition from LIBOR by Jan 1, 2022 |
| **Computation** | Weighted median of actual overnight repo trades; compiled from FR2 data and DTCC repo records |
| **Secured vs. unsecured** | SOFR is a secured rate (backed by Treasury collateral); LIBOR was unsecured, reflecting credit risk |
| **Publication time** | Released daily at 8:00 AM ET by the Federal Reserve |
| **Term rates** | SOFR 1M, 3M, 6M, 12M derived via SOFR averages (not real transactions) |
| **Spread to SOFR** | Floating-rate bonds and swaps now quote as "SOFR + 200 bps" (basis points) |

</aside>

## Why LIBOR was broken and SOFR was needed

LIBOR (London Interbank Offered Rate) was historically the most widely used [interest rate benchmark](/wiki/federal-funds-rate/), with trillions of dollars of loans, bonds, and derivatives referencing it daily. But LIBOR was computed from voluntary submissions by a panel of banks estimating the rate at which they could borrow unsecured overnight. In practice, these submissions were not based on actual transactions; they were estimates. During the 2008 financial crisis, these estimates became farcical: banks inflated LIBOR estimates to hide their own credit stress, and the published rate ceased to reflect reality.

Multiple scandals (LIBOR manipulation, the RATE Setting fraud) revealed that traders were offering small payments to panel banks to move submissions in their favor. A rate that was supposed to be a market truth had become a [consensus fiction](/wiki/consensus-layer-security/). Regulators worldwide (the SEC, CFTC, and UK Financial Conduct Authority) fined banks tens of billions of dollars. By 2017, the consensus was clear: LIBOR had to go.

## SOFR is transaction-based, not opinion-based

SOFR's core strength is that it is calculated from *real transactions* in the repo market, not estimates. Every morning, the Federal Reserve gathers data on all overnight repo trades reported to the DTCC (Depository Trust and Clearing Corporation) and dealer submission pools, sorts them by size, and publishes the weighted median. There is no room for manipulation because there is no subjective estimate; the number is mechanical. If a bank tried to induce a trader to report a fake repo trade, it would be fraud against the Federal Reserve and the DTCC, with criminal consequences.

SOFR is secured because the borrowers (banks, dealers, hedge funds) pledge Treasury securities as collateral. If a repo counterparty defaults, the lender can seize and auction the collateral immediately. Unsecured LIBOR, by contrast, exposed lenders to the full credit risk of the borrowing bank. This fundamental difference is why SOFR is typically 20–50 basis points *lower* than [LIBOR was](/wiki/libor/), all else equal. A bank's credit risk costs extra; Treasuries don't.

## The big transition: how markets switched from LIBOR to SOFR

The December 31, 2021 LIBOR discontinuation deadline loomed over global finance for years. Banks, hedge funds, asset managers, and mortgage originators had to reprice trillions in exposure:

- **Floating-rate bonds**: Each bond's coupon changed from "LIBOR + spread" to "SOFR + spread." The spread was typically 25–50 bps higher to compensate for the difference between unsecured (LIBOR) and secured (SOFR) rates.
- **Interest-rate swaps**: Dealers created a new SOFR swap curve starting from zero and bootstrapped it from futures, term SOFR quotes, and dealer submissions.
- **Mortgages and loans**: Consumer mortgages switched to "SOFR-based" rates at next reset, though home loans had 2–3 years to migrate. Corporate loans either switched earlier or negotiated synthetic LIBOR arrangements (banks publish a "synthetic LIBOR" computed from SOFR + an add-on) as a bridge.
- **Fallback language**: Existing contracts that matured during the transition often included fallback language saying "if LIBOR ceases, use SOFR + 26.161 basis points," a number chosen to represent the average LIBOR-SOFR spread historically.

## Term SOFR and the lack of a real 3-month rate

LIBOR was published in seven maturities (overnight, 1-week, 1-month, 2-month, 3-month, 6-month, 12-month). SOFR publishes only the overnight rate from transaction data; there is no real 3-month repo market large or liquid enough to support a term rate the way the unsecured lending market supported 3-month LIBOR.

Instead, regulators and traders created "term SOFR" rates, computed as the average of overnight SOFR over a historical window (e.g., the 3-month term rate is the average SOFR over the past 90 days). This is a fallback, not a market rate. CME Eurodollar futures contracts, which had been LIBOR-linked for 30 years, were rebased to use daily SOFR rates, forcing traders to manage a fundamentally different contract (daily compounding rather than a quarterly reset).

## SOFR's path to adoption and lingering resistance

The Federal Reserve and regulators gave market participants until January 2023 to cease *writing new* LIBOR contracts. Hundreds of billions in legacy LIBOR exposure remained outstanding for years (mortgages, loans, bonds issued before the deadline). Regulators permitted "synthetic LIBOR" publication for U.S. dollar rates through June 2023 and for some other currencies (GBP, JPY, CHF) through 2024, as a bridge for contracts without fallback language.

Some holdouts—Australian banks, Asian insurers, others in jurisdictions with weaker regulatory oversight—continued using LIBOR impliedly (or switched only reluctantly). The UK's Financial Conduct Authority published a formal statement that LIBOR would be discontinued after June 2023, forcing the hand of even recalcitrant lenders.

By 2024, SOFR-based markets dominated new issuance and trading in USD interest-rate derivatives. The shift also accelerated the adoption of other regional equivalents: SONIA in the UK, EONIA (replaced by €STR) in Europe, TONA in Japan, and CORRA in Canada.

## SOFR term curve and the forward rate agreement replacement

The lack of a real 3-month or 6-month SOFR market posed challenges for [hedging](/wiki/interest-rate-hedging/). Dealers solved this by offering "term SOFR forwards"—agreements to lend at a rate based on the compounded daily SOFR for a future 3-month window. These forward SOFR rates embed expectations of future overnight [monetary policy](/wiki/monetary-policy/) but are often more volatile than the historical LIBOR term rates were, because they reflect daily repricing rather than a quarterly snapshot.

This daily compounding feature is both a strength and a weakness: it is more responsive to changes in central bank policy (the [Fed funds rate](/wiki/federal-funds-rate/)), but it introduces more variance into hedging strategies. A corporate treasurer hedging a variable-rate [loan](/wiki/debt-financing/) backed by quarterly SOFR averages now sees the hedge ratio change daily, increasing operational complexity.

## SOFR spreads in floating-rate bonds and loans

When a company issues a [floating-rate bond](/wiki/floating-rate-bond/), it now quotes as "3-month SOFR + 150 bps" (for example). The 150 basis point spread compensates investors for:
- Credit risk of the issuer
- Optionality (call risk if rates fall sharply)
- Liquidity premium relative to Treasuries

Interestingly, SOFR-based bonds often trade with wider spreads than old LIBOR bonds, because investors demand compensation for the daily compounding and the higher basis-point volatility of SOFR relative to LIBOR. A 3-month SOFR-based bond backed by a 90-day average has a different risk profile than a quarterly-reset LIBOR bond.

## The Fed's role and the repo market anchor

SOFR's credibility rests entirely on the health and size of the U.S. repo market, which is roughly $1–1.5 trillion in daily turnover. The Federal Reserve has backstopped this market multiple times (2008 crisis, 2019 repo spike, COVID-19 March 2020). If the repo market seized completely, SOFR would become meaningless. The Fed has acknowledged this by establishing the [Standing Repo Facility](/wiki/standing-repo-facility/) in 2021, a permanent backstop allowing banks to repo Treasuries to the Fed at a fixed rate, ensuring SOFR never spikes dangerously again.

<div class="wiki-seealso">

### Closely related
- [LIBOR](/wiki/libor/) — The predecessor benchmark SOFR replaced
- [Interest Rate Swap](/wiki/interest-rate-swap/) — Floating-rate contracts now benchmarked to SOFR
- [Floating-Rate Bond](/wiki/floating-rate-bond/) — Bonds whose coupons reset to SOFR + spread
- [Federal Funds Rate](/wiki/federal-funds-rate/) — The overnight rate the Fed targets; SOFR tracks near it

### Wider context
- [Repurchase Agreement](/wiki/repurchase-agreement/) — The collateralized overnight lending market that generates SOFR
- [Monetary Policy](/wiki/monetary-policy/) — The Fed's tools, now transmitted via SOFR-based markets
- [Interest Rate Risk](/wiki/interest-rate-risk/) — How borrowers hedge SOFR exposure
- [Derivatives Clearing](/wiki/central-counterparty-clearing/) — How SOFR swaps are cleared and collateralized

</div>
