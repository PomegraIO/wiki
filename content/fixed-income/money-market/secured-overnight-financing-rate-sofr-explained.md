---
title: "SOFR Explained: The Secured Overnight Financing Rate"
description: "How the secured overnight financing rate works, why it replaced LIBOR, and its role in pricing short-term borrowing costs."
keywords:
  - secured overnight financing rate
  - sofr calculation
  - libor replacement
  - overnight repo market
  - short-term benchmark rate
image: "/svg/fixed-income.svg"
---

*The **secured overnight financing rate** (SOFR) is the interest rate at which banks lend cash to each other overnight, backed by U.S. Treasury collateral. It replaced LIBOR as the primary benchmark for short-term borrowing costs across trillions of dollars in loans, bonds, and derivatives.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">SOFR — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income securities." />

<div class="wiki-infobox-caption">The Federal Reserve's replacement for LIBOR, built on real overnight Treasury repo trades.</div>

|   |   |
|---|---|
| **What it measures** | Overnight interest rate on Treasury-collateralized loans between banks |
| **Calculation source** | Actual repo transactions reported to trade repositories |
| **Published daily by** | Federal Reserve Bank of New York |
| **Replaces** | LIBOR (as of 2021–2023 phaseout) |
| **Key advantage over LIBOR** | Based on observed transactions, not expert estimates |
| **Frequency** | Backward-looking; disclosed with a one-day lag |

</aside>

## Why SOFR replaced LIBOR

For decades, the **London Interbank Offered Rate** (LIBOR) was the global standard for pricing short-term borrowing. But LIBOR had a fatal flaw: it was calculated from banks' *estimates* of what they would pay to borrow, rather than actual trades. During the 2008 financial crisis, those estimates proved unreliable and sometimes manipulated. Regulators and the financial industry determined that a rate grounded in real market transactions was essential.

The Federal Reserve chose the overnight Treasury repo market as the foundation for SOFR. This market is enormous—trillions of dollars flow through it daily—and highly transparent. Every transaction is reported to data repositories, leaving a clear electronic trail. Unlike LIBOR, SOFR cannot be estimated or gamed; it simply reflects what banks actually paid on real loans.

## How SOFR is calculated

Each morning, the Federal Reserve Bank of New York collects overnight repo transaction data reported to the Financial Industry Regulatory Authority (FINRA), the Depository Trust & Clearing Corp (DTCC), and other repositories. These transactions cover loans made the previous business day.

The calculation works as follows:

1. Identify all eligible repo trades—overnight loans collateralized by Treasury securities.
2. Filter for transactions within the normal trading window and within acceptable price ranges.
3. Calculate a volume-weighted median of those rates.
4. Publish the result the following morning.

This approach ensures SOFR reflects genuine market activity, not opinions or forecasts. The volume-weighted median (rather than simple average) prevents a handful of large outlier trades from distorting the rate.

## Who uses SOFR and how

Banks, investors, and corporations reference SOFR for pricing:

- **Variable-rate loans**: Corporate borrowing lines often float at SOFR + a spread (e.g., SOFR + 150 basis points).
- **Floating-rate bonds and notes**: Issuers pay coupons tied to SOFR quarterly or semiannually.
- **Interest-rate derivatives**: Swaps, swaptions, and caps/floors use SOFR to settle payoffs.
- **Mortgages and consumer loans**: Adjustable-rate mortgages have begun moving to SOFR-based pricing.

The transition away from LIBOR was staggered and required years of preparation. U.S. dollar LIBOR ceased publication at the end of 2021 for most tenors (maturities), with sterling and yen LIBOR ending in 2022 and 2023. Any remaining LIBOR contracts were converted to SOFR using a statutory spread adjustment set by regulators.

## SOFR vs. other overnight rates

SOFR is the U.S. overnight Treasury repo rate. Other countries have equivalents:

| Jurisdiction | Rate | Collateral |
|---|---|---|
| **Eurozone** | ESTER | Euro-denominated bonds |
| **United Kingdom** | SONIA | Sterling bonds |
| **Japan** | TONA | Japanese government bonds |

All share the same principle: they measure actual overnight interbank lending against government securities. SOFR dominates global finance because the U.S. dollar is the world's reserve currency and U.S. Treasuries are the largest, most liquid asset class.

## Term SOFR and forward-looking alternatives

Standard SOFR is backward-looking: published one day after the rate accrues. For some products, this lag is inconvenient. The Federal Reserve and industry have therefore created:

- **Term SOFR**: A forward-looking rate for 1-, 3-, 6-, and 12-month tenors, published daily. Banks and brokers estimate the expected SOFR rate over those periods using swap data and market expectations.
- **Compounded SOFR**: A retrospective calculation that compounds daily SOFR over a period (e.g., a quarter). Used for floating-rate notes and adjustable mortgages.

Most loan contracts have gravitated toward compounded SOFR; term SOFR remains less common but is emerging for certain bond issuance and syndicated lending products.

## The Federal Reserve's role in daily SOFR management

Although SOFR is a market rate, not a target set by the Fed, the Federal Reserve influences it indirectly. The Fed sets a **target range** for the [federal funds rate](/effective-federal-funds-rate-vs-target-range/)—typically 25 basis points wide—and uses open market operations to keep overnight rates within that band.

When demand for overnight lending rises sharply (for example, during year-end or quarter-end pressures), SOFR can spike above the Fed's target range. To manage this, the Fed offers **standing repo facilities** that provide overnight funding at a fixed rate, essentially a ceiling. Similarly, the Fed maintains a reverse repo facility that absorbs excess cash from the system, acting as a floor.

This framework keeps SOFR stable most of the time, though it does fluctuate with market conditions—particularly during financial stress or operational disruptions to the Treasury market.

## See also

<div class="wiki-seealso">

### Closely related

- [Money-Market Fund Liquidity Fees and Redemption Gates](/money-market-fund-liquidity-fees-redemption-gates/) — How funds access safe overnight funding and cope with redemption pressure
- [Effective Federal Funds Rate vs the FOMC Target Range](/effective-federal-funds-rate-vs-target-range/) — How the Fed's target range relates to overnight rates
- [Treasury Bill](/treasury-bill-laddering-strategy/) — Competing safe short-term investment for cash
- [Repurchase Agreement](/repurchase-agreement/) — The underlying market transaction that generates SOFR
- [Federal Reserve](/federal-reserve/) — The agency that publishes SOFR and manages its corridor

### Wider context

- [Interest Rate](/interest-rate/) — The broader concept SOFR exemplifies
- [Monetary Policy](/monetary-policy/) — How the Fed uses overnight rates as a policy lever
- [Money Market Fund](/money-market-fund/) — The main investor counterparty to SOFR-linked instruments
- [Credit Risk](/credit-risk/) — Why repo is collateralized; SOFR is a secured rate
- [Derivatives Hedging](/derivatives-hedging/) — SOFR underpins trillions in interest-rate hedges

</div>
