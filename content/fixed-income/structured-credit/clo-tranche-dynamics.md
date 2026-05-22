---
title: "CLO Tranche Dynamics"
description: "Waterfall payment priority and credit enhancement across tiers in collateralized loan obligation tranches."
keywords:
  - CLO
  - collateralized loan obligation
  - tranches
  - waterfall
---

*A **CLO (Collateralized Loan Obligation)** is a structured investment backed by a portfolio of corporate loans. The collateral is divided into **tranches** with different risk and return profiles—senior tranches have priority on payments, junior tranches absorb losses first, creating a waterfall structure that allocates cash flow by seniority.*

<aside class="wiki-infobox">

| Tranche | Seniority | Typical Coupon | Attachment Point |
|---------|-----------|---|---|
| **Senior AAA** | 1st priority | SOFR + 100 bps | 0–2% loss |
| **AA** | 2nd priority | SOFR + 150 bps | 2–4% loss |
| **A** | 3rd priority | SOFR + 250 bps | 4–7% loss |
| **BBB** | 4th priority | SOFR + 400 bps | 7–10% loss |
| **Equity** | Last priority | Residual | 10%+ loss |

</aside>

## The waterfall: how cash flows cascade through tranches

A CLO with $500 million in loans is carved into tranches: $400M senior AAA, $50M AA, $30M A, $15M BBB, $5M equity. Each month, the loans pay interest and principal. The **waterfall** directs cash as follows:

1. **Cover expenses**: Management fees, servicing fees, trustee fees (~1% of portfolio annually).
2. **Senior AAA interest**: $400M × (SOFR + 100 bps) / 12 ≈ $400K per month.
3. **AA interest**: $50M × (SOFR + 150 bps) / 12 ≈ $65K per month.
4. **A interest**: $30M × (SOFR + 250 bps) / 12 ≈ $63K per month.
5. **BBB interest**: $15M × (SOFR + 400 bps) / 12 ≈ $50K per month.
6. **Principal paydown**: Senior AAA principal (quarterly or monthly).
7. **Reserve account funding**: Holding cash for future defaults.
8. **Equity distributions**: Anything left over goes to equity holders.

If loan defaults increase and the portfolio recovers only $420M (20% loss), the waterfall triggers **diversion**: principal that would go to senior tranches is diverted to reserves instead, protecting junior tranches first. Once losses exceed the equity tranche cushion (>5% of portfolio), losses begin to "consume" the BBB tranche. A $75M loss (15% portfolio loss) wipes out equity ($5M), BBB ($15M), and A ($30M), leaving $25M loss to penetrate the AA tranche.

## Credit enhancement: subordination and overcollateralization

Each tranche is **protected** by the subordinated tranches below it. The equity tranche absorbs the first 5% of losses; the BBB absorbs 6–7%; the A absorbs the next 3%; and so forth. This subordination is the **credit enhancement**—the mechanism that keeps senior tranches rated AAA despite backing leveraged loans (typically rated BB or lower). A senior AAA can suffer 10%+ portfolio loss and still not take a loss because junior tranches have $130M of cushion (BBB + A + AA + equity).

**Overcollateralization (OC)** is a second form of enhancement. The $500M in loans might not be worth exactly $500M; some are trading at $95 per $100 par (due to credit deterioration). The CLO's actual collateral is valued at $480M. The OC ratio is $480M / $400M senior tranche = 1.2x. If the portfolio declines 5%, the collateral value drops to $456M, and the OC ratio falls to $456M / $400M = 1.14x. Once the OC ratio breaches a threshold (often 1.15x for AAA), the waterfall shifts: principal diversion increases, senior interest is suspended, and cash flows divert to rebuild OC and protect junior tranches. This mechanism **forces deleveraging** once credit stress hits, protecting senior investors.

## Attachment and detachment points: loss severity

Each tranche is defined by **attachment and detachment points**—the cumulative loss thresholds. The AAA tranche attaches at 0% (it's first in line) and detaches at 10% (after 10% cumulative loss, it starts taking losses). The AA attaches at 10% and detaches at 15%. The BBB attaches at 15% and detaches at 20%. These points directly correspond to the tranche sizes and subordination. A wider attachment point (equity is often 20–25% attachment) means deeper loss cushion; wider detachment (less common for CLOs, but exists for high-risk portfolios) means higher loss potential.

Investors buy tranches based on risk appetite: an asset manager seeking AAA safety buys senior AAA (attachment 0%, detachment 10%); a [hedge fund](/wiki/hedge-fund-credit/) seeking yield buys BBB or equity (attachment 15–20%, higher coupon); an insurer matching liabilities buys AA or A (moderate risk, moderate yield).

## Interest coverage and triggers: protective covenants

CLOs have **interest coverage (IC) and overcollateralization (OC) tests**. Failing these tests triggers "step-down"—removing the manager's ability to reinvest principal in new loans (they must pay it down). The IC test: aggregate interest from loans must cover interest due to all tranches at a 1.5x–2.0x ratio. If defaults rise and loan interest falls below 1.5x the coupon due, IC fails, and deleveraging is forced. The OC test: collateral value must exceed the outstanding principal of tranches. Failing OC forces the same outcome. These tests are **self-healing**: if the CLO's loan portfolio recovers (defaults cease, recoveries arrive), tests can re-pass within months, allowing reinvestment to resume.

## Default and recovery cascade

When a loan in the portfolio defaults, the impact depends on recovery. A $10M loan defaulting with 60% recovery (the manager recovers $6M, loses $4M) immediately reduces portfolio value by $4M. This depletes the equity tranche first; if the $5M equity cushion is breached, BBB takes losses next. In a severe stress scenario (2008, post-COVID), a CLO with 15% portfolio losses wipes out equity and BBB tranches entirely, A tranches take 5% loss, and senior tranches (AA, AAA) remain whole. Because defaults are uncertain and recoveries unpredictable, junior tranches are highly risky—they might return 20%+ per year in good times or 0% (wiped out) in crises.

## Equity tranches and residual value

The equity (or "first loss") tranche in a CLO receives no coupon—it's **paid last** in the waterfall, after all senior tranches are satisfied. But it can be lucrative: in a healthy CLO with 2% average loan defaults and 65% recoveries, there's enough cash left over each year to pay equity investors 15–20% IRR. However, in a stressed CLO (2008, 2015 energy crisis), equity gets $0 while tranches above it get cut, devastating equity investors. Equity holders are the **true risk-takers**; they're compensated with upside only if the portfolio performs. This aligns incentives—the CLO manager owns much of the equity and is incentivized to maintain loan quality. However, perverse incentives can emerge if the manager is paid only on closing new CLOs (origination volume), not performance.

## Secondary market trading and bid-ask dynamics

CLO tranches trade in the secondary market, but liquidity varies. Senior AAA tranches are liquid (institutional demand, low risk); bid-ask spreads are 5–10 basis points. BBB and A tranches are illiquid (fewer buyers), with spreads 20–50 basis points. Equity tranches barely trade—secondary market bids are often 50%+ below par, and many equity positions are held to maturity. A CLO that was well-regarded at issuance might tank in secondary trading if loan defaults rise faster than expected (e.g., a 2020 COVID shock could drop a BBB tranche 20% in value even if no actual losses occur, because investors demand higher yield on higher perceived risk). This creates opportunities for contrarian buyers but is treacherous for those caught holding into stress events.

## CLO managers' incentives and conflicts

The **CLO manager** selects loans, reinvests principal, and manages the portfolio. The manager is typically paid a fixed fee (~0.50% of assets) plus incentive fee (profit participation if equity exceeds a threshold). This alignment is theoretically strong—the manager's profit depends on good loan selection. However, conflicts exist: (1) the manager is paid even if the portfolio performs poorly (fixed fee), so moral hazard tempts aggressive leverage; (2) managers who close large CLOs earn large origination fees, incentivizing large issuances over quality; (3) secondary trading bids/offers from the manager's own trading desk can be opaque. Post-2008, regulators tightened CLO manager requirements, including stress-testing and higher capital standards for managers.

---

<div class="wiki-seealso">

### Closely related
- [Collateralized Debt Obligation](/wiki/collateralized-debt-obligation/) — Securitizations of credit instruments
- [Collateralized Loan Obligation](/wiki/collateralized-loan-obligation/) — CLOs backing corporate loans
- [Tranche](/wiki/tranche/) — Tiered security with priority to cash flows
- [Waterfall (Payment Priority)](/wiki/ccp-default-waterfall/) — Cascade of distributions in structured securities

### Wider context
- [Credit Rating](/wiki/credit-rating/) — How tranches are rated AAA, BBB, etc.
- [Structured Finance](/wiki/structured-finance/) — Design of securitized products
- [Mortgage-Backed Security](/wiki/mortgage-backed-security/) — MBS as a similar waterfall structure
- [Default Waterfall](/wiki/ccp-default-waterfall/) — Priority allocation in clearing defaults

</div>
