---
title: "Derivative Clearing Requirements"
description: "Mandatory central clearing of standardized derivatives contracts by designated clearinghouses, a post-2008 regulatory reform to reduce systemic risk."
keywords:
  - derivative clearing
  - central counterparty
  - dodd frank
  - systemic risk
---

*Post-2008, regulators imposed **mandatory central clearing requirements** on standardized [derivatives](/wiki/derivative-accounting-hedging/) contracts. Swap dealers and major traders must submit eligible [interest rate swaps](/wiki/interest-rate-swap/), [credit default swaps](/wiki/credit-default-swap/), and [commodity derivatives](/wiki/commodity-swap/) to a [central counterparty clearing house (CCP)](/wiki/central-counterparty-clearing/). The CCP interposes itself as buyer to every seller and seller to every buyer, eliminating bilateral counterparty risk and improving market transparency.*

<aside class="wiki-infobox">

| Key Fact | Value |
|---|---|
| **Primary Mandate** | Dodd-Frank Act (U.S., 2010); EMIR (EU, 2012) |
| **Clearing Houses** | CME Clearing, LCH, ICE Clear, others |
| **Contract Types** | Interest rate swaps, CDS, commodity swaps, FX forwards |
| **Exemptions** | End-users with hedging intent; non-standard (bespoke) swaps |
| **Scope** | Standardized contracts meeting regulatory criteria |
| **Collateral Required** | Initial margin + variation margin (daily) |
| **Regulatory Bodies** | CFTC (U.S.), ESMA (EU), regulators worldwide |

</aside>

## Why mandatory clearing was imposed

Before 2008, the $600+ trillion [derivatives](/wiki/derivative-accounting-hedging/) market was largely bilateral and unregulated. Two counterparties would negotiate a [swap](/wiki/swap/) (e.g., interest rate swap) and hold it on their books until maturity, with no intermediary. When Lehman Brothers collapsed, its counterparties faced massive credit losses because Lehman owed them money on thousands of swaps and could not pay. The cascading defaults threatened the entire financial system.

Mandatory clearing aims to prevent this by:

1. **Eliminating counterparty risk:** The CCP is the counterparty to all trades, absorbing losses if a member defaults.
2. **Enforcing daily settlement:** [Mark-to-market](/wiki/mark-to-market/) and variation margin force loss recognition in real-time, not at maturity.
3. **Increasing transparency:** Regulators can see all cleared trades; systemic risk is easier to monitor.
4. **Mutualized default risk:** If a member defaults, the CCP's default fund (backed by all members) absorbs losses, spreading risk across the system.

## Which derivatives must be cleared

Regulators have established "Determinations of Substantial Equivalence" to designate which derivatives are standardized enough to clear:

**Must be cleared (U.S.):**
- Interest rate swaps (IRS) with major currencies (USD, EUR, GBP, JPY, CHF).
- [Credit default swaps](/wiki/credit-default-swap/) on major indices (CDX, iTraxx).
- [Commodity swaps](/wiki/commodity-swap/) on standardized products (crude oil, natural gas, metals).
- FX forwards with major currency pairs.

**Exempt from mandatory clearing:**
- Bespoke (non-standard) swaps tailored to specific risks.
- Swaps by "[end-users](/wiki/atomic-swap/)" (corporations, pension funds) engaging in genuine hedging, not speculation.
- Small- and mid-market firms below regulatory thresholds.

The exemptions are crucial: a manufacturing company hedging its European operations with a custom EUR/USD swap does not need to clear it; the swap is too specific and the company is not a systemic risk. But a [hedge fund](/wiki/hedge-fund/) or bank trading interest rate swaps for profit must clear.

## How clearing works: the mechanism

**Pre-clearing (bilateral):**
- Dealer A and Dealer B negotiate a 10-year interest rate swap: Dealer A pays fixed 4%, Dealer B pays floating SOFR.
- They agree on a price and execute.

**Post-clearing (tripartite):**
1. The trade is reported to the CCP (automated via electronic confirmation).
2. The CCP becomes the counterparty: Dealer A pays fixed 4% **to the CCP**, which pays floating SOFR; Dealer B pays floating SOFR **to the CCP**, which pays fixed 4%.
3. Daily mark-to-market: Each day, the swap is revalued. If rates move, the CCP calculates gains/losses and collects [variation margin](/wiki/variation-margin/) from the losing party.
4. At maturity (10 years), final cash flows are exchanged via the CCP.

The CCP risk-manages each member's account: if a member loses money, the CCP calls margin; if the member cannot pay, the CCP liquidates the member's positions and uses the default fund to cover losses.

## Collateral and margin requirements

Cleared swaps require two types of collateral:

### Initial Margin (IM)
Collected upfront to cover potential market moves over the default window (typically 2–5 days). Calculated using models (SPAN, SIMM) that estimate **Value at Risk**. For a $1 billion swap portfolio, IM might be $10–50 million.

### Variation Margin (VM)
Collected daily (or intraday for large moves). If a swap loses value by $100,000, the losing party deposits $100,000 immediately. This eliminates accrual of losses.

The collateral is held in segregated accounts; the CCP can access it to cover losses if the member defaults.

## Central counterparty risk concentration

Mandatory clearing solved bilateral counterparty risk but created a new risk: **CCP risk concentration**. All derivatives trades now funnel through 3–5 major CCPs (CME, LCH, ICE Clear, others). If a CCP fails, the entire derivatives market freezes.

To mitigate this:

- **Prudential requirements:** CCPs must maintain large capital buffers and regularly stress-test their default funds.
- **Regulatory oversight:** The CFTC (U.S.), ESMA (EU), and others supervise CCPs and set standards.
- **Interoperability:** Some regulators encourage multiple CCPs to compete, reducing concentration.
- **CCP default waterfalls:** If a CCP member defaults, the default is absorbed via: (1) member's collateral, (2) CCP's capital, (3) member default fund contributions, (4) CCP loss mutualization.

The 2023 financial turmoil (SVB collapse, Credit Suisse stress) tested CCP resilience; all major CCPs held firm.

## End-user exemptions and lobbying

"End-users" (non-financial corporates) are exempt from mandatory clearing if they:

1. Engage in genuine hedging of their business risks.
2. Stay below a $8 billion notional threshold (threshold varies by jurisdiction).
3. Provide hedging certification to their dealers.

This exemption was fiercely lobbied for by corporations fearing clearing costs and complexity. A wheat farmer hedging crop sales with [commodity futures](/wiki/commodity-swap/) would not need to clear; a farmer speculating on wheat prices might.

The line is blurry, and regulators are tightening the definition. Some hedge funds have claimed "end-user" status to escape clearing; regulators now scrutinize these claims.

## Global fragmentation: EMIR, Dodd-Frank, and beyond

The U.S. has Dodd-Frank; the EU has EMIR; other regions have similar rules. But they don't always align:

- The U.S. requires clearing for credit default swaps; the EU has different thresholds.
- Equivalence determinations (does EU clearing meet U.S. standards?) create operational complexity.
- Cross-border swaps must navigate multiple regulatory regimes.

This has created incentives for regulatory arbitrage: firms structure trades to minimize clearing obligations. The CFTC and ESMA continue negotiating "mutual recognition" agreements to streamline global derivatives regulation.

## Impact on market structure and costs

Mandatory clearing has:

1. **Increased transparency:** Regulators see all cleared trades via swap data repositories.
2. **Reduced leverage:** Higher margin requirements limit leverage in derivatives markets.
3. **Increased costs:** Clearing fees and initial margin requirements increase the cost of hedging, especially for corporates.
4. **Reduced liquidity in bespoke swaps:** Dealers less willing to trade non-standard derivatives, so custom hedges are rarer and more expensive.

Some argue clearing has reduced systemic risk; others argue it has just relocated it to CCPs without eliminating it.

<div class="wiki-seealso">

### Closely related
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — The CCP mechanism and risk management
- [Interest Rate Swap](/wiki/interest-rate-swap/) — A primary cleared derivative
- [Credit Default Swap](/wiki/credit-default-swap/) — Another major cleared instrument
- [Dodd-Frank Act](/wiki/dodd-frank-act/) — The U.S. law that mandated clearing

### Wider context
- [Derivative Accounting](/wiki/derivative-accounting-hedging/) — Accounting for cleared vs. uncleared swaps
- [Variation Margin](/wiki/variation-margin-daily/) — Daily collateral settlement
- [Systemic Risk](/wiki/systemic-risk/) — The problem clearing requirements aimed to solve

</div>
