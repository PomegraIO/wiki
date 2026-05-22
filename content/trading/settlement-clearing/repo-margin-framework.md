---
title: "Repo Margin Framework"
description: "How haircuts and collateral valuation work in repurchase agreements, protecting the cash lender against collateral value fluctuations."
keywords:
  - repo margin
  - haircut
  - collateral valuation
  - repurchase agreement
  - margin framework
---

***The repo margin framework** governs how much collateral a borrower must post (and at what haircut) when securing a short-term loan via [repurchase agreement](/wiki/repurchase-agreement/). A **haircut** is the gap between the collateral's market value and the loan amount, protecting the cash lender against price declines and counterparty default.*

<div class="wiki-hatnote">
For the instrument itself, see [Repurchase agreement](/wiki/repurchase-agreement/). For the broader clearing mechanism, see [Central counterparty clearing](/wiki/central-counterparty-clearing/).
</div>

<aside class="wiki-infobox">

| Attribute | Detail |
|-----------|--------|
| **Haircut range** | 0.5% to 10%+ depending on collateral type |
| **Collateral types** | Government bonds, agencies, high-grade corporates, MBS |
| **Valuation method** | Market price + repo margin adjustment |
| **Frequency** | Daily or intraday adjustments in volatile markets |
| **Regulatory change** | Basel III, LCR, NSFR rules tightened in 2008+ |
| **Cyclicality** | Haircuts widen in stress periods, tighten in calm |

</aside>

## The haircut concept

In a repo, the **cash lender** is unsecured. If the borrower defaults, the lender must liquidate the collateral to recover the loan. If collateral prices fall before liquidation, the lender absorbs the loss. The **haircut** is an insulator:

**Example:**
- A dealer holds $100 million in Treasury bonds.
- They repo those bonds overnight to raise $99 million in cash.
- The 1% gap ($1 million) is the haircut.
- If bond prices fall 2% overnight ($2 million), the lender loses only $1 million; the dealer absorbs the other $1 million as owner of the collateral.

Haircuts are asymmetric. On Treasury bonds, haircuts are minimal (0.5–1.5%) because they are liquid and low-credit-risk. On mortgage-backed securities or lower-grade corporates, haircuts reach 5–10% or more.

## Collateral-specific haircut schedules

Different collateral classes incur different haircuts:

| Collateral | Typical Haircut | Rationale |
|-----------|-----------------|-----------|
| **U.S. Treasury (< 5yr)** | 0.5–1% | Most liquid, credit-free |
| **U.S. Treasury (5–10yr)** | 1–2% | Still liquid but duration risk |
| **U.S. Treasury (>10yr)** | 2–3% | Rising interest-rate risk |
| **Agency MBS** | 2–4% | Extension/prepayment risk |
| **Investment-grade corporate** | 3–7% | Credit and liquidity risk |
| **High-yield bond** | 8–15% | High default risk |
| **Stock** | 10–20%+ | Volatility and liquidity concerns |

A dealer's collateral basket is typically weighted by these haircuts. If they post $100M in Treasuries and $10M in corporate bonds, the effective haircut is roughly 1.2% (weighted average).

## Variation margin and mark-to-market

Repos typically reset daily (or even intraday in volatile periods). The lender marks the collateral to market daily. If collateral prices decline:

1. **Initial margin call**: The collateral's value drops, narrowing the cushion.
2. **Variation margin adjustment**: The borrower must post additional collateral to restore the cushion.

Conversely, if collateral prices rise, the lender refunds excess collateral to the borrower.

This daily settlement prevents small drifts from accumulating. Without it, a 5% price move over a month could render collateral underwater.

## Central clearing and standardized haircuts

Bilateral (uncleared) repos allow negotiated haircuts. A Wall Street bank and a pension fund might agree on a 1.5% haircut for Treasury collateral because they trust each other. But when trades are cleared through a central counterparty (like LCH, Eurex Repo Clearing), standardized schedules apply.

Central counterparties publish **standardized haircut tables** daily, updated based on:
- Historical volatility of each asset.
- Bid-ask spreads (wider spreads = higher haircuts).
- Counterparty concentration (if many parties repo the same collateral, haircuts tighten).

This transparency reduces counterparty-specific negotiation and lowers systemic risk—everyone uses the same haircut for the same collateral.

## Haircut cyclicality: calm vs. stress

During calm markets, haircuts are tight (0.5% on Treasuries). Lenders are confident that collateral is liquid and prices are stable.

During stress (like March 2020 COVID crash):
- Treasury haircuts spike from 1% to 3–5% as liquidity evaporates.
- Corporate and MBS haircuts may jump from 5% to 10%+.
- Less-liquid collateral (junk bonds, equity) becomes unacceptable in many venues.

This procyclicality is a double-edged sword. A dealer leveraged at normal haircuts suddenly faces massive variation margin calls when haircuts widen, forcing asset fire sales. The 2008 financial crisis saw this spiral: haircuts widened, margin calls cascaded, asset prices fell further, haircuts widened more.

## Collateral valuation methodologies

Haircuts are applied on top of **collateral valuation**, which is not always straightforward:

1. **Mark-to-market**: Use the last traded price. Standard for liquid securities.
2. **Model-based**: When no recent trade exists (illiquid collateral), use a pricing model (discounted cash flow, comparable securities).
3. **Haircut adjustment**: Some frameworks apply a separate haircut to the model price to account for model risk.

A mortgage-backed security with no traded price in the past hour might be valued at a model price of $98, then a 3% haircut reduces the collateral's repo value to $95.06.

## Regulatory developments post-2008

Basel III and Dodd-Frank changed the landscape:

1. **LCR (Liquidity Coverage Ratio)**: Banks must hold "high-quality liquid assets" sufficient to survive a 30-day stress scenario. This pressures banks to reduce leverage and hold safer collateral, tightening haircuts.
2. **NSFR (Net Stable Funding Ratio)**: Penalizes short-term, unsecured funding, benefiting repo (which is stable) over unsecured interbank lending.
3. **Clearinghouse capital requirements**: Central counterparties must hold more capital if haircuts are tight (incentivizing wider haircuts).

The net effect: haircuts are generally wider post-2008 than pre-crisis, increasing funding costs for dealers.

## Haircut grading and exceptions

Some frameworks use **haircut grading scales** (AAA, AA, A, BBB, BB, B, etc.) applied to bonds based on credit rating. A AAA-rated corporate might get a 2.5% haircut; a BBB-rated bond might get 5%. This simplifies administration and reduces model risk.

Exceptions exist for:
- **Eligible central bank collateral**: Central banks (Federal Reserve, ECB) maintain lists of collateral eligible in their refinancing operations. These receive favorable haircuts (sometimes zero) because the central bank is willing to absorb risk.
- **Negotiated relief**: A large, reputable counterparty may request a haircut below the standard schedule if they have excess collateral or strong relationships.

## Impact on financing costs and leverage

Haircuts directly affect dealer profitability. Tighter haircuts require more collateral, reducing achievable leverage. A dealer might finance $100M in bonds at 95% loan-to-value (5% haircut) in calm times, but only at 90% LTV (10% haircut) in stress. The wider haircut means the dealer must fund $10M of the $100M position from equity capital rather than borrowed funds, reducing return on equity.

Over time, haircuts have tightened, particularly for less-liquid assets, reducing dealers' ability to leverage and compress net interest margins.

<div class="wiki-seealso">

### Closely related

- [Repurchase agreement](/wiki/repurchase-agreement/) — The underlying instrument.
- [Central counterparty clearing](/wiki/central-counterparty-clearing/) — How standardized haircuts are administered.
- [Collateral ratio](/wiki/collateral-ratio/) — The broader concept of collateralization.
- [Counterparty credit risk](/wiki/counterparty-credit-risk/) — Why haircuts protect lenders.
- [Variation margin](/wiki/variation-margin-daily/) — Daily mark-to-market adjustments.

### Wider context

- [Credit risk](/wiki/credit-risk/) — The risk haircuts mitigate.
- [Liquidity risk](/wiki/liquidity-risk/) — Asset illiquidity increases haircuts.
- [Basel capital](/wiki/basel-iii/) — Regulatory framework shaping haircut policies.
- [Interest-rate risk](/wiki/interest-rate-risk/) — Duration risk factored into bond haircuts.

</div>
