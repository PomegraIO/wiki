---
title: "SOFR vs LIBOR: Why the Benchmark Rate Changed"
description: "Why LIBOR was retired, how SOFR differs in construction and credit risk, and what the transition means for floating-rate bonds and derivatives."
keywords:
  - sofr vs libor transition explained
  - sofr benchmark rate why
  - libor retirement
  - sofr libor difference
image: "/svg/fixed-income.svg"
---

*The **SOFR transition from LIBOR** is the largest plumbing change in global finance in decades. LIBOR, the 32-year-old reference rate that priced trillions in loans and derivatives, is gone. In its place: SOFR, a rate built on actual overnight repurchase transactions rather than surveyed quotes. Understanding this shift matters because it reshapes credit-risk pricing and touches every floating-rate instrument.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">SOFR vs LIBOR — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income analysis." />

<div class="wiki-infobox-caption">LIBOR was estimated; SOFR is measured from real transactions.</div>

|   |   |
|---|---|
| **LIBOR construction** | Panel banks submitted estimated borrowing costs; averaged daily |
| **SOFR construction** | Actual overnight repo borrowing rates; observed in real money-market trades |
| **Credit risk embedded** | LIBOR included bank credit premium; SOFR is credit-risk-free |
| **Scope of change** | ~$200 trillion in contracts linked to LIBOR; most now reference SOFR |
| **Liquidity** | SOFR is overnight-only; term SOFR added for loans with longer reset periods |
| **Spread adjustment** | Fixed "basis spread" added to SOFR to approximate historical LIBOR levels |

</aside>

## Why LIBOR failed and had to go

**LIBOR** (London Interbank Offered Rate) was born in 1986 as a simple solution: ask major banks what they would pay to borrow from each other overnight, average the quotes, and publish that as the benchmark. For 30 years, it worked.

Then, during the 2008 financial crisis, it broke. Banks stopped trusting each other. Lending froze. But LIBOR panels kept submitting quotes as if everything were normal, because "normal" was their instructions. The rate no longer reflected reality.

After the crisis, investigations revealed something darker: some banks had deliberately lowballed their LIBOR submissions to make their own borrowing costs look cheaper. Traders at major institutions had colluded to push LIBOR in directions that fattened their derivatives positions. Fines totaled billions. Reputations burned.

Regulators concluded that a rate based on estimates from a small panel of banks, with no anchor in actual trades, was not fit for a global financial system. They ordered LIBOR's retirement. By end of 2021 (extended to mid-2023 for legacy contracts), LIBOR was gone.

## The fundamental difference: observed vs estimated

The core flaw of LIBOR was that it was a survey. "What rate would you borrow at?" is an estimate. No actual transaction had to happen at that rate. Under stress, estimates drift from reality—either because banks are guessing badly or, in darker episodes, because they are guessing on purpose.

**SOFR** (Secured Overnight Financing Rate) flips this model. It is built from real transactions. Every day, the Federal Reserve observes repurchase (repo) trades—the bread-and-butter of money-market funding. Banks and investors lend cash overnight to each other, backed by Treasury collateral. The Fed collects data on millions of these trades, calculates a volume-weighted average, and publishes SOFR.

Because the data comes from actual transactions in a liquid, transparent market, SOFR cannot be easily gamed. A bank cannot push SOFR by submitting a false estimate; it would have to execute billions of dollars in actual repo trades, which other market participants would spot and offset.

SOFR is therefore more robust. But this robustness comes with a trade-off: SOFR is an overnight rate only. LIBOR came in 1-month, 3-month, 6-month, and 12-month flavors, allowing loans to reset at staggered intervals. SOFR does not naturally exist for longer periods because longer-term repo markets are less liquid. To fill this gap, the Fed created "term SOFR"—statistical estimates of what overnight SOFR might average over the next 1, 3, 6, or 12 months, based on futures prices. It is an estimate, but anchored in traded futures contracts, not panel submissions.

## Credit risk: the invisible component

Here is a subtle but crucial difference: **LIBOR embedded credit risk**. When a bank said "I would borrow at 3-month LIBOR + 0.50%," it was saying "my cost to borrow unsecured for three months is this level." The rate reflected the bank's creditworthiness. In good times, all panel banks had nearly the same credit quality, so LIBOR moved tightly. But in a crisis, when one bank was perceived as riskier than another, their LIBOR submission diverged—and LIBOR as an average became a muddy signal.

**SOFR is credit-risk-free**. Every SOFR transaction is backed by Treasury collateral. The lender is protected; if the borrower defaults, the lender seizes the Treasuries. Because of this collateral, SOFR is typically 50–100 basis points *lower* than 3-month LIBOR in normal times, and the gap widens in stress.

This difference has huge implications for loan pricing. A floating-rate corporate loan that used to price as "LIBOR + 200 bps" meant the borrower paid LIBOR (which included bank credit risk) plus a credit spread. Under SOFR, the same loan might be "SOFR + 220 bps"—the extra 20 bps compensates for the credit-risk premium that was embedded in LIBOR but is missing from SOFR.

Setting these "spread adjustments" was contentious. The industry eventually agreed on fixed spreads—a one-time adjustment locked into each contract—rather than dynamic spreads that would shift daily. But not all contracts have been amended cleanly, and disputes linger.

## The mechanics of the transition

Trillions of dollars in contracts had to migrate or be rewritten. The process unfolded in waves.

For new loans and derivatives issued after 2018, dealers and lenders simply started using SOFR or term SOFR from day one. For many corporate loans, the switch was fast. Banks stopped offering LIBOR-linked products and issued SOFR-linked alternatives.

For existing contracts—legacy loans, mortgages, bonds, swaps—the transition was messier. Some had "fallback language" that specified what would happen if LIBOR died (use SOFR plus a spread, or use a replacement rate if available). Others had no fallback and technically became unenforceable at the end of 2021. Regulators stepped in with rules requiring derivatives dealers to convert LIBOR derivatives to SOFR-based equivalents. Loan amendments required borrower consent, which dragged out the timeline.

The biggest gap is in syndicated loans. Thousands of legacy syndicated facilities still reference LIBOR (especially USD LIBOR), and many borrowers have resisted the switch because SOFR-based loans cost more (due to the spread adjustment). Regulators have pushed hard but cannot force amendment without cooperation.

By mid-2023, the vast majority of new volume was SOFR-based. Legacy LIBOR exposure shrunk sharply. But pockets remain—particularly in private loans, insurance contracts, and some older mortgages.

## Practical differences for investors and borrowers

For a corporate borrower, the **SOFR transition** is not invisible. A SOFR-linked loan resets daily at overnight SOFR plus a fixed spread. This means the borrower pays SOFR + 220 bps (or whatever the agreed spread is). If SOFR is 5.5%, the borrower pays 7.7% that day; if SOFR falls to 4.5%, the borrower pays 6.7% the next day.

LIBOR-linked loans reset less frequently (monthly, quarterly) and reference a longer-dated LIBOR (e.g., 3-month LIBOR). The effective borrowing cost moved less frequently and reflected longer-term bank credit conditions.

For investors holding SOFR-linked bonds or loans, the daily reset to SOFR means less interest-rate risk (short duration) but more day-to-day payment volatility. Investors in longer-duration instruments prefer term SOFR resets (quarterly, semi-annual) to smooth out daily noise.

For derivatives traders, the change requires new valuation models. LIBOR and SOFR curves behave differently under stress. Basis risk—the risk that SOFR and LIBOR diverge—was a major hedge during the transition. That trade is now mostly historical.

## The remaining pockets and complications

As of 2026, nearly all active new borrowing uses SOFR or other risk-free rates (sterling borrowing has moved to SONIA, euro to €STR). But legacy LIBOR lingers.

Some bilateral loans, often at smaller banks or in specialized lending (real estate, M&A), still reference USD LIBOR as of June 2023 and have not been amended. These are technically in default of LIBOR's discontinuation but operate under regulatory forbearance.

Insurance contracts present another snag. Some variable annuities and structured notes were issued with LIBOR guarantees that are now unenforceable. Insurers are renegotiating or buying out these obligations, a slow and expensive process.

The transition also exposed arbitrage opportunities. For a period, the spread between SOFR and LIBOR remained wide, rewarding those who could trade the basis. That trade has largely evaporated as the rate structures have aligned.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate](/interest-rate/) — the benchmark rate system and why it matters to global pricing
- [Repurchase Agreement](/repurchase-agreement/) — the overnight collateral lending market that SOFR measures
- [Central Bank](/central-bank/) — the Federal Reserve's role in publishing SOFR
- [Money Market Fund](/money-market-fund/) — funds holding short-dated instruments tied to SOFR
- [Corporate Bond](/corporate-bond/) — floating-rate bonds often linked to LIBOR or SOFR
- [Treasury Bill](/treasury-bill/) — the collateral underlying SOFR repo trades

### Wider context

- [Credit Rating](/credit-rating/) — how credit quality affected LIBOR but not SOFR
- [Derivative](/derivatives-hedging/) — the largest volume of LIBOR-linked contracts, now converted
- [Basis Risk](/basis-risk/) — the risk that SOFR and LIBOR diverge, relevant during transition
- [Federal Reserve](/federal-reserve/) — the institution that publishes and administers SOFR

</div>
