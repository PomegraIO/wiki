---
title: "How Subordination Levels Are Sized in Securitizations"
description: "Learn how subordination levels are sized: rating agencies and originators use loss models, rating curves, and credit enhancement math to protect each tranche."
keywords:
  - how subordination levels are sized securitization
  - credit enhancement securitization
  - subordination thickness
  - rating agency methodology
  - securitization tranche sizing
---

*Rating agencies and securitization originators use **expected loss models** and **rating curves** to determine how much junior debt (subordination) is needed to support a target rating for each senior tranche. Thicker subordination absorbs more losses; the math links default rates, recovery rates, and correlation assumptions to the credit enhancement required at each level.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Subordination Sizing — the rating framework</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Subordination thickness is built on loss assumptions and the probability that each tranche gets repaid in full.</div>

|   |   |
|---|---|
| **Input: default rate** | Historical or stressed assumption on obligor failure |
| **Input: recovery rate** | % of par recovered on defaulted loans (typically 40–70%) |
| **Input: correlation** | How likely defaults cluster together (systemic stress) |
| **Rating curve** | Maps expected loss to minimum subordination for a target rating |
| **Subordination level** | Par value of all junior tranches below a given level |
| **Overcollateralization (OC) test** | Par value of collateral must exceed outstanding tranches |
| **Interest coverage (IC) test** | Available cash must cover expenses and senior interest |
| **Target rating** | AAA, AA, A, BBB determine required credit enhancement |

</aside>

## The purpose of subordination

In a [securitization](/securitization/), **subordination** means that junior tranches absorb losses before senior tranches. A securitization might have four tranches:

- **Class A (Senior)**: AAA-rated, backed by ~85% of pool par
- **Class B (Mezzanine)**: A-rated, backed by next 8%
- **Class C (Lower mezzanine)**: BB-rated, backed by next 4%
- **Equity/First-loss**: Unrated, backed by bottom 3%

If the collateral pool experiences 5% losses, the equity tranche is wiped out first, then Class C, then Class B. Class A remains whole. This structure allows the originator to convert below-average collateral (say, loans with a 3% expected loss) into AAA-rated senior tranches with far lower risk.

The question is: **How much subordination does a Class A tranche actually need?** The answer depends on loss assumptions and the probability of exceeding them.

## Rating agency methodology

Rating agencies (Moody's, S&P, Fitch) use standardized models to determine subordination. The process has several steps:

**Step 1: Model expected loss.** The agency gathers data on the collateral pool: origination date, obligor credit quality, industry composition, geographic concentration, and loan terms. It then applies historical default and recovery rates to estimate expected losses. For example:

- Average default rate: 2% per year
- Average recovery rate: 50% of par
- Expected loss: 2% × (1 − 0.5) = 1% of par

**Step 2: Stress the model.** The agency doesn't just use expected loss; it applies stress scenarios. It might model a recessionary environment where default rates double to 4% and recovery falls to 35%. Or it models the 99th percentile of loss distributions—essentially, "what is the loss we'd see in a severe but plausible scenario?"

**Step 3: Apply a rating curve.** The agency has empirical or historical curves that link loss levels to ratings. For example, a curve might say: "A tranche is AAA-rated if losses stay below 2% of collateral par." The agency selects loss assumptions (often based on stressed scenarios) and determines the subordination cushion needed to keep each tranche above its loss floor.

**Step 4: Calculate subordination thickness.** If the stress scenario projects 3% losses, and Class A must have a 2% cushion to be AAA, then subordination (Class B + C + Equity) must be at least 5%. If the pool is $100 million, Class A can be $95 million and junior tranches are $5 million.

## Over-collateralization and interest coverage

Two mechanical tests enforce the subordination cushion after closing:

**Over-Collateralization (OC) Test**: The par value of the collateral pool must exceed the outstanding notional of all tranches. If the pool loses value (through defaults), the OC ratio declines. If it breaches a stated threshold, the manager is forced to begin paying down senior tranches immediately (instead of reinvesting cash), shrinking the structure and preserving the cushion.

Example: If collateral par is $100M and outstanding tranches total $98M, the OC ratio is 1.02 or 102%. If the ratio falls to 101%, an OC breach might occur, triggering amortization.

**Interest Coverage (IC) Test**: Available interest (net of losses and expenses) must cover all senior tranche coupon payments. If interest income drops (due to prepayments, defaults, or falling yields), and available interest falls below the required coupon, an IC breach occurs. This also forces amortization.

These tests operate like circuit breakers, automatically shifting the structure to safer mode if the collateral deteriorates.

## The role of correlation

A critical assumption in sizing subordination is **correlation**—how likely it is that multiple obligors default together. In a diversified pool, defaults are mostly independent: if one obligor fails, it doesn't materially increase the odds that others fail. But in a concentrated or correlated pool, failures cluster.

Consider two extreme scenarios:

**Low correlation**: Defaults are independent. A portfolio of 1,000 loans from different industries and geographies. If default rates are 2%, on average 20 loans fail each year, but outcomes cluster around that average. A 3% loss is fairly likely; a 10% loss is extremely rare. Modest subordination suffices.

**High correlation**: Obligors are all in the same sector (e.g., retail real estate) or all benefit from the same economic driver (employment in oil-dependent regions). In a downturn, most fail together. Losses could easily jump from 2% to 10% or higher. Massive subordination is needed to protect seniors.

Rating agencies model correlation using **copulas** or other statistical tools. A securitization with high correlation assumptions requires thicker subordination. This is one reason why concentrated [CLOs](/collateralized-loan-obligation/) are harder to rate (and require more subordination) than diversified consumer receivables securitizations.

## Relationship between expected loss and subordination

The math is straightforward:

**Subordination % = Expected Loss % + Stress Buffer %**

If a collateral pool has 1% expected loss and the rating agency wants a stress buffer of 1.5% (to cover the tail risk and give the tranche a AAA rating), then subordination must be at least 2.5% of par. Everything below that tranche absorbs the losses first.

Different tranches get different buffers:

- **AAA (senior)**: Highest buffer (e.g., 3% subordination)
- **AA**: Medium buffer (e.g., 1.5% subordination)
- **A**: Thinner buffer (e.g., 0.8% subordination)
- **BBB**: Minimal buffer (e.g., 0.2% subordination)

The gaps between these are the thickness of each tranche. If total subordination is 3% and is allocated AAA-1.5%, AA-0.5%, A-0.5%, BBB-0.5%, then:

- Class A (AAA): backed by bottom 1.5% + collateral surplus
- Class B (AA): backed by 0.5% subordination
- Class C (A): backed by 0.5% subordination
- Class D (BBB): backed by 0.5% subordination

## Real-world adjustments

In practice, subordination sizing is an art as much as science:

**Conservative originators** might size tranches with more subordination than agencies require, retaining or selling more junior pieces themselves to signal confidence in the collateral.

**Agency conservatism** increased after 2008. Post-financial crisis, rating agencies now stress scenarios more heavily and require thicker subordination for the same loss assumptions.

**Competitive pressure** can work in both directions. In tight credit markets, competition for underwriting business can push originators to ask agencies for lower subordination (thinner junior tranches, bigger senior tranches to appeal to more investors). Agencies may accommodate if they believe the collateral supports it.

**Collateral mix** matters enormously. A securitization backed by [prime mortgages](/residential-real-estate/) might need 5% subordination for a AAA tranche, while one backed by subprime auto loans might need 15%. The composition drives the stress assumptions.

## Subordination in different securitization types

**Mortgages**: Typically 20–30% subordination for AAA. High correlation in housing downturns justifies thick protection.

**Auto loans**: Typically 5–10% subordination for AAA. Lower correlation, better recovery rates (the car can be repossessed).

**Credit card receivables**: Typically 5–15% subordination for AAA. Large portfolio and geographic diversity reduce correlation; diversification allows thinner tranches.

**CLOs**: Typically 15–25% subordination for AAA. Loan defaults are highly correlated in recessions; sophisticated investors in CLOs accept thinner ratings but demand higher yields.

The differences reflect both the default and recovery characteristics of the collateral and the correlation profiles of the obligor base.

## See also

<div class="wiki-seealso">

### Closely related

- [Securitization](/securitization/) — foundational structure where subordination is embedded
- [Static vs managed CLO](/static-vs-managed-clo/) — collateral manager may adjust composition post-closing
- [Credit card ABS mechanics](/credit-card-abs-mechanics/) — example of credit enhancement in a revolving structure
- [Tail risk in structured credit](/tail-risk-structured-credit/) — why subordination can fail in extreme scenarios
- [Credit rating](/credit-rating/) — how agencies assign ratings tied to subordination levels

### Wider context

- [Concentration risk](/concentration-risk/) — affects correlation assumptions
- [Default rate](/default-rate/) — key input to loss models
- [Value-at-risk](/value-at-risk/) — statistical tool for modeling tail losses
- [Over-the-counter market](/over-the-counter-market/) — where many structured credit bonds trade
- [Stress testing](/stress-testing/) — methodology agencies use to size subordination

</div>
