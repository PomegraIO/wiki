---
title: "Weighted Average Spread in a CLO"
description: "A CLO's weighted average spread sets a floor on portfolio yield and is tested as a covenant to ensure adequate compensation for credit risk."
keywords:
  - weighted average spread clo
  - clo weighted average spread test
  - collateralized loan obligation spread
  - clo covenant
image: /svg/fixed-income.svg
---

*The **weighted average spread in a CLO** is a covenant test that measures whether the debt instruments in the portfolio are yielding enough to support the cost of the CLO's [debt financing](/debt-financing/) and equity returns, protecting investors and lenders alike.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Weighted Average Spread in a CLO — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income securities." />

<div class="wiki-infobox-caption">The threshold yield test that ensures CLO collateral generates adequate returns.</div>

|   |   |
|---|---|
| **Definition** | Sum of each loan's spread × its portfolio weight / total portfolio |
| **Spread component** | Typically SOFR or LIBOR plus a margin (e.g., +300 basis points) |
| **Minimum threshold** | Usually 200–250 basis points; set at issuance |
| **Test trigger** | Monthly or quarterly, during collateral monitoring |
| **Consequence of breach** | Funds diverted to repay debt; equity gets no distributions |
| **Why it matters** | Ensures manager cannot load portfolio with weak-credit, low-yield loans |
| **Weighted calculation** | Each loan's spread weighted by its principal balance in the pool |

</aside>

## What the weighted average spread measures

A [collateralized loan obligation (CLO)](/real-estate-investment-trust/) is a [securitization](/securitization/) of a pool of loans. The manager assembles perhaps 100–200 loans with varying [credit ratings](/credit-rating/), maturities, and [spread](/credit-spread/) above the floating-rate benchmark (typically [SOFR](/sofr/) or [LIBOR](/libor/)). Each loan pays its coupon—say, SOFR + 300 bps—and those coupons are paid waterfall-style: first to senior debt holders, then to [mezzanine investors](/), and finally to equity holders.

The **weighted average spread** (WAS) is simply the average spread of all loans in the portfolio, weighted by their principal amounts. If the portfolio has $100 million in total loans and the weighted sum of spreads is $2.5 million per year, the WAS is 250 basis points. That 250 bps is the margin the portfolio collects above the floating-rate index.

## Why the covenant is critical

The WAS covenant exists to prevent the collateral pool from degrading. Without it, a manager could theoretically buy junk-rated loans yielding only SOFR + 150 bps (low spread due to elevated risk or distress), pocketing the management fee and leaving CLO investors with insufficient yield to cover their [cost of capital](/cost-of-debt/).

By setting a minimum WAS—say, 225 bps at issuance—the CLO's trust indenture forces the manager to maintain a portfolio of loans with average quality. If the WAS falls below the threshold, the test is "breached," and cash flow is redirected: instead of distributing excess cash to the equity class, those dollars are used to repay the most senior debt tranches. This is called a "cash flow waterfall gate."

The minimum WAS is negotiated at issuance and reflects the cost structure of the CLO. For example:

- Senior debt may cost 200 bps (SOFR + 100 bps) = $2 million per year on a $100 million tranche.
- Mezzanine debt may cost 400 bps (SOFR + 300 bps) = $1.2 million on a $30 million tranche.
- Equity expects to earn 10–15% = $4–6 million on its $10 million investment.
- Total cost: $7.2–9.2 million annually.
- To cover these costs plus the manager fee, the portfolio must yield at least, say, 260 bps.

The WAS covenant sets this threshold and monitors it continuously.

## How the test works in practice

Each month or quarter, the collateral manager or trustee calculates the WAS on the outstanding loans in the pool:

**Worked example:**

Portfolio composition:

| Loan | Principal | Spread (bps) | Contribution ($ mm) |
|------|-----------|--------------|---------------------|
| Loan A (BB-rated) | $30 mm | 325 bps | 97.5 |
| Loan B (B-rated) | $25 mm | 400 bps | 100 |
| Loan C (BB-rated) | $20 mm | 300 bps | 60 |
| Loan D (CCC-rated) | $15 mm | 500 bps | 75 |
| Loan E (BB-rated) | $10 mm | 325 bps | 32.5 |

Total portfolio principal: $100 mm
Sum of spread contributions: $365 mm bps = 365,000 bps
Weighted average spread: 365,000 / 100,000 = 365 bps

Assuming the minimum WAS threshold is 225 bps, the test is comfortably passed. The portfolio is generating 365 bps of spread, well above the covenant floor. Equity receives distributions as scheduled.

**Breach scenario:**

Suppose Loan D (the CCC-rated loan) defaults. The manager purchases a replacement loan at a lower spread due to tighter [credit conditions](/credit-rating/):

| Loan | Principal | Spread (bps) | Contribution ($ mm) |
|------|-----------|--------------|---------------------|
| Loan A (BB-rated) | $30 mm | 325 bps | 97.5 |
| Loan B (B-rated) | $25 mm | 400 bps | 100 |
| Loan C (BB-rated) | $20 mm | 300 bps | 60 |
| Loan D-replacement (B-rated) | $15 mm | 275 bps | 41.25 |
| Loan E (BB-rated) | $10 mm | 325 bps | 32.5 |

New total spread contribution: $331.25 mm bps
New WAS: 331.25 bps

The WAS is still above the 225 bps threshold, so the test is passed. However, if credit conditions deteriorate further and loan spreads compress (because the floating benchmark rises or the manager is forced to buy lower-credit loans), the WAS might drift to 220 bps, and the covenant would be breached.

## Consequences of a breach

When the WAS test is breached:

1. **Cash flow diversion begins.** Instead of distributing excess cash to equity holders, the trustee applies it to reduce the senior debt tranches. This ensures senior investors recover principal and do not suffer further mark-to-market losses.

2. **Equity distributions cease.** The equity class is last in the waterfall; if WAS is breached and cash is limited, equity gets nothing. Over time, this forces the manager to rebuild the portfolio and restore the WAS above the threshold.

3. **Pressure on the manager.** The manager's own fee may be deferred or reduced during a breach, creating incentive to restore the WAS quickly. The manager might sell weaker loans (at a loss) and buy higher-spread loans to improve the portfolio quality and test result.

4. **Duration of the breach.** Most CLOs specify that the breach can last 12–24 months before it triggers other remedies (e.g., manager removal or acceleration of principal repayment). This gives the manager time to rebalance the portfolio and recover the WAS above the threshold.

## WAS vs. other CLO covenants

CLOs have multiple covenants, of which WAS is just one:

- **Weighted average rating factor (WARF):** Measures the average credit quality of the portfolio. A higher WARF means weaker credit, triggering a breach if the portfolio deteriorates too much.
- **Weighted average life (WAL):** Ensures loans do not mature too quickly; sudden maturity cliffs create reinvestment risk.
- **Diversity score:** Limits concentration; no single industry or borrower can be too large a share of the portfolio.
- **Interest coverage ratios:** Ensure there is enough excess cash flow to meet obligations at each level of the waterfall.

The WAS covenant is unique in that it directly ties portfolio yield to the cost of financing. If spreads are tight (credit is expensive, risk is perceived as high), a minimum WAS of 250 bps becomes harder to hit. If spreads are wide (credit is cheap, risk is perceived as low), hitting 250 bps is easy. This countercyclical feature means WAS tests tighten just when managers need more flexibility—during credit downturns.

## Practical implications for CLO investors

For CLO debt holders (senior and mezzanine), a strong WAS buffer (say, 350 bps when the threshold is 225 bps) is a comfort signal: the portfolio has room for spread compression or defaults. A thin buffer is a warning sign.

For equity investors, the WAS covenant is a double-edged sword. It protects equity from a deteriorating portfolio (because defaults or spread compression will trigger cash diversion, forcing repair), but it also cuts off equity distributions during market stress—precisely when equity is already underwater. Understanding the WAS cushion is critical to assessing the risk of a CLO equity tranche.

## See also

<div class="wiki-seealso">

### Closely related

- [Securitization](/securitization/) — pooling and tranching of loans
- [Credit Spread](/credit-spread/) — yield premium above the risk-free rate
- [SOFR](/sofr/) — the floating-rate benchmark used in most modern CLOs
- [Credit Rating](/credit-rating/) — assessments of borrower creditworthiness
- [Collateralized Loan Obligation](/real-estate-investment-trust/) — the CLO structure itself
- [Tranche](/tranche/) — priority levels in a securitized pool

### Wider context

- [Mortgage Backed Security](/mortgage-backed-security/) — similar securitization structure for mortgages
- [Bond](/bond/) — general fixed-income instruments
- [Cost of Debt](/cost-of-debt/) — the yield required to compensate lenders
- [Counterparty Risk](/counterparty-risk/) — risk that a loan issuer defaults
- [Interest Coverage Ratio](/interest-coverage-ratio/) — ability to meet debt service obligations

</div>
