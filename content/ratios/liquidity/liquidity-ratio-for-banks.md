---
title: "Liquidity Ratios for Banks: LCR and Beyond"
description: "Explore bank-specific liquidity ratios including the Liquidity Coverage Ratio (LCR), Net Stable Funding Ratio (NSFR), and regulatory stress-test metrics that assess banking system resilience."
keywords:
  - liquidity ratios for banks
  - LCR NSFR
  - banking regulation
  - liquidity coverage ratio
  - net stable funding ratio
image: /svg/ratios.svg
---

*Bank **liquidity ratios for banks** differ fundamentally from corporate metrics because banks are inherently leveraged institutions that must convert short-term deposits into long-term loans. The **Liquidity Coverage Ratio (LCR)** and **Net Stable Funding Ratio (NSFR)** are the regulatory linchpins, designed to ensure banks survive stress periods without firesales or government rescue.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bank Liquidity Ratios — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for financial ratios." />

<div class="wiki-infobox-caption">Regulators mandate minimum thresholds to prevent bank runs and systemic crises.</div>

|   |   |
|---|---|
| **LCR (Liquidity Coverage Ratio)** | High-quality liquid assets ÷ Net 30-day cash outflows; minimum 100%. |
| **NSFR (Net Stable Funding Ratio)** | Available stable funding ÷ Required stable funding; minimum 100%. |
| **Time horizon** | LCR = 30 days (immediate stress); NSFR = one-year (structural stability). |
| **Who enforces** | [Federal Reserve](/federal-reserve/), SEC, FDIC (US); Basel Committee (global). |
| **Purpose** | Prevent fire-sales of assets; ensure deposits stay on bank books. |
| **Stress test** | Regulators run annual scenarios (recession, deposit flight, credit spreads). |

</aside>

## Why banks need different metrics

A typical bank borrows short (deposits, money-market funding) and lends long (mortgages, business loans). That maturity mismatch—borrowing for 30 days, lending for 30 years—is the business model. But it creates acute liquidity risk. If depositors panic and withdraw funds all at once, the bank can't instantly convert illiquid loans to cash. Before Basel III and post-2008 reforms, this risk was under-monitored. Bank runs happened; financial crises cascaded.

Corporate liquidity ratios like the current ratio (current assets ÷ current liabilities) don't work for banks. A bank's "current liabilities" include all deposits, some of which don't leave for years. A bank's assets are mostly loans, which are illiquid. A simple current ratio would make every bank look dangerously underleveraged, yet banks operate sustainably because deposits are sticky and loans generate stable cash flow.

Enter the **Liquidity Coverage Ratio** and **Net Stable Funding Ratio**, designed to isolate the precise liquidity stress that threatens a bank's solvency.

## Liquidity Coverage Ratio (LCR): 30-day survival

The LCR answers the question: *Can the bank survive a severe 30-day funding shock?*

In a stress scenario, deposits flee. Creditors refuse to roll over short-term borrowing. Asset sales become harder, and bid-ask spreads widen. The LCR measures whether the bank holds enough liquid assets to weather 30 days of this chaos:

**LCR = High-Quality Liquid Assets (HQLA) ÷ Total Net Cash Outflows (30-day scenario)**

**High-Quality Liquid Assets (HQLA)** are defined tightly:
- **Level 1:** Cash, central-bank reserves, sovereigns of the highest credit grade (US Treasuries, German bunds). No haircut; these are money.
- **Level 2A:** High-grade corporate bonds, covered mortgages; 15% haircut (haircut = what you lose if you firesale quickly).
- **Level 2B:** Lower-grade corporates, equity, mutual funds; 25–50% haircut.

For example, a bank holding $10 billion in US Treasuries and $5 billion in high-grade corporate bonds would report:
- Level 1: $10 billion
- Level 2A: $5 billion × 85% = $4.25 billion
- Total HQLA: $14.25 billion

**Total Net Cash Outflows** is the sum of stressed withdrawals and funding outflows over 30 days. Regulators prescribe withdrawal rates for each liability category:
- Insured deposits (FDIC-protected): 3% withdrawal rate
- Uninsured retail deposits: 10% withdrawal rate
- Wholesale funding (money-market, interbank): 75% withdrawal rate
- Credit lines drawn: 50% of committed lines not yet used

A bank with $100 billion in insured deposits, $50 billion in uninsured retail deposits, $30 billion in wholesale borrowing, and $20 billion in committed credit lines faces:
- Insured outflows: $100B × 3% = $3B
- Retail outflows: $50B × 10% = $5B
- Wholesale outflows: $30B × 75% = $22.5B
- Credit-line outflows: $20B × 50% = $10B
- **Total net outflows: $40.5 billion**

An LCR of 100% means HQLA = Net outflows. A bank with $40.5 billion in HQLA just barely survives 30 days. Regulators prefer LCR > 100% (comfort margin); the rule requires minimum 100% and is phased in to 100% by 2019.

High LCR (120%+) means the bank is conservative, holding excess liquid assets. Low LCR (just above 100%) means the bank is optimized for profit but vulnerable to worse-than-stressed scenarios.

## Net Stable Funding Ratio (NSFR): structural stability over a year

The LCR is a short-term shock test. The **NSFR** asks a deeper question: *Can the bank sustain current assets and liabilities over a full year of market stress?*

**NSFR = Available Stable Funding ÷ Required Stable Funding**

**Available Stable Funding (ASF)** is money the bank can expect to keep or refinance over a year:
- Equity: 100% of ASF (it won't leave)
- Insured deposits: 90% (sticky; mostly won't flee)
- Uninsured retail deposits: 70% (some will leave in stress)
- Wholesale funding (short-term): 0–50% (much will run; depends on credit quality)
- Lending to other banks: 0% (counterparties won't lend back in stress)

**Required Stable Funding (RSF)** is the amount the bank must hold or stabilize:
- Cash and equivalents: 0% RSF (already liquid)
- Government securities: 0–5% RSF (easy to sell)
- High-quality corporates: 15% RSF
- Mortgages (unencumbered): 25% RSF
- Business loans: 50% RSF
- Illiquid assets: 85–100% RSF

A bank's NSFR tells a longer story. High NSFR (120%+) means the bank's deposits and equity can cover long-term assets with a cushion. A bank heavily reliant on short-term wholesale funding (bond issuance, repo) with illiquid assets (mortgages, business loans) will have a lower NSFR and faces refinancing risk.

## Regulatory expectations and stress testing

The [Federal Reserve](/federal-reserve/) and Office of the Comptroller of the Currency (OCC) require US banks above a size threshold to submit annual [stress tests](/stress-testing/). Regulators run scenarios (recession, market crash, credit event) and calculate what happens to capital and liquidity ratios.

A typical stress scenario might assume:
- Unemployment rises 2% (economic shock)
- House prices fall 20% (housing crisis)
- Stock markets drop 30% (equity crash)
- Credit spreads widen (borrowing costs rise)

Under these conditions, what happens to the bank's LCR and NSFR? Does it stay above 100%, or does it fall below the regulatory minimum?

If it falls below, the bank must hold more capital, reduce risky assets, or adjust liability structure. The test is public, so investors and regulators see the bank's vulnerabilities.

## Inter-bank differences and contagion risk

Not all banks face the same liquidity stress. 

**Community banks** with mostly insured deposits and mortgage portfolios face lower wholesale-funding risk but higher interest-rate risk on long-duration assets. Their LCR is often comfortable; NSFR depends on lending-to-deposits ratio.

**Large money-center banks** with huge wholesale operations (repo, commercial paper, foreign exchange) face volatile funding. A spike in credit spreads or a flight to quality can blow through LCR quickly. These banks typically hold higher HQLA buffers.

**Global banks** with multiple currencies and countries face additional stress: currency risk (a weakening home currency makes foreign liabilities more expensive) and cross-border funding shocks.

During the 2008 crisis, wholesale funding froze almost overnight. Banks with LCR < 50% (common before regulation) faced existential crisis. Post-Basel III, banks with LCR near 150% and NSFR > 110% can weather the same scenario. That shift in the regulatory framework dramatically reduced systemic risk.

## Beyond LCR and NSFR: deposit intelligence

Regulators also monitor **deposit concentration** (what percentage of deposits come from one customer or sector?) and **wholesale-funding maturity profile** (how much short-term debt rolls over daily?).

A bank with 10% of deposits from a single corporate customer faces idiosyncratic risk; if that customer fails or moves its account, the bank loses material funding. A bank with $5 billion in commercial paper rolling over every 90 days faces refinancing risk; if credit spreads spike, the cost of rolling that debt balloons.

Some banks disclose **liquidity coverage by currency** and **liquidity maturity ladders**—how much funding they need to refinance each day, week, and month. A bank needing to refinance $2 billion daily faces higher refinancing risk than one refinancing $200 million daily.

## The post-2008 world

Before 2008, banks routinely operated with LCR < 50% and NSFR < 80%. Regulators didn't mandate minimums. The theory was that markets would enforce discipline—a bank with poor liquidity would face higher borrowing costs. It didn't work. When Lehman Brothers collapsed, credit froze regardless of individual bank quality. Fear and contagion dominated.

Post-Basel III, the floor is LCR ≥ 100% and NSFR ≥ 100%, enforced by US regulators. The rule applies to bank holding companies with > $250 billion in assets and is calibrated for smaller banks. Banks discovered that hitting the minimums was feasible: raise more deposits, hold more Treasuries, manage the liability mix. The trade-off is lower yields on Treasuries and higher deposit-insurance costs; the benefit is systemic stability.

## See also

<div class="wiki-seealso">

### Closely related

- [Liquidity Ratio vs Solvency Ratio](/liquidity-ratio-vs-solvency-ratio/) — How banks' LCR and NSFR fit into the broader liquidity vs. solvency framework.
- [Federal Reserve](/federal-reserve/) — The primary regulator of bank liquidity and stress-testing compliance.
- [Stress Testing](/stress-testing/) — The regulatory scenario analysis underpinning LCR and NSFR adequacy.
- [Capital Adequacy](/capital-adequacy/) — The related regulatory ratio; liquidity and capital are both enforced.
- [Counterparty Risk](/counterparty-risk/) — Why banks worry about who else they lend to and refinance from.

### Wider context

- Commercial Bank — The business model that creates liquidity risk; maturity mismatch.
- [Federal Deposit Insurance Corporation](/federal-deposit-insurance-corporation/) — Protects insured deposits, which lowers deposit-run risk and raises ASF in NSFR.
- [Systemic Risk](/systemic-risk/) — Why bank liquidity crises threaten the broader financial system.
- Treasury Market — The main source of HQLA; bank demand for Treasuries is driven by LCR rules.

</div>
