---
title: "Interest Coverage Test"
description: "Trigger in CLOs and CDOs comparing interest collected to senior notes' interest obligations; breach redirects cash to deleverage."
keywords:
  - structured credit
  - clo
  - cdo
  - interest shortfall
  - senior protection
image: "/svg/fixed-income.svg"
---

*The **interest coverage test** (or IC test) is a numerical trigger in collateralised loan obligations and collateralised debt obligations that measures whether the interest collected from the collateral pool is sufficient to pay the [coupon](/coupon-payment/) on all outstanding senior notes. If interest income falls short of senior obligations, a cash diversion automatically kicks in—subordinated tranches stop receiving payments, and available funds flow instead to cover the shortfall or pay down senior principal.*

<div class="wiki-hatnote">

For the comparable measure on asset values rather than income, see [Overcollateralization Test](/over-collateralization-test/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Coverage Test — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income and structured products." />

<div class="wiki-infobox-caption">A flow-based safety net: when interest dries up, junior distributions stop.</div>

|   |   |
|---|---|
| **What it is** | Ratio of collateral interest income to senior interest due |
| **Also called** | IC test, interest coverage ratio, interest shortfall test |
| **Typical trigger level** | 100%–115% (varies by deal) |
| **Breach consequence** | [Equity](/stock/) and [subordinated tranches](/junk-bond/) lose distributions; cash diverts to pay senior coupons |
| **Covers** | Scheduled interest payments from loans, net of defaults and recoveries |
| **When tested** | Monthly, quarterly, or at each [coupon](/coupon-payment/) date |
| **Who monitors** | [Trustee](/), [collateral manager](/collateral-manager/), note servicer |

</aside>

## Why income coverage matters separately from asset value

A CLO's cash waterfall has two distinct pillars: **assets** (the collateral pool's total value) and **income** (the interest and principal flowing in each period). The [overcollateralization test](/over-collateralization-test/) guards the first; the interest coverage test guards the second.

The distinction is crucial. A portfolio can be adequately overcollateralized on par value—the loans are still worth enough to cover senior debt—yet produce insufficient interest income to pay senior coupons on time. This happens when borrowers downgrade, [credit spreads](/credit-spread/) spike, or [floating-rate loans](/interest-rate/) reset downward in a lower-[interest-rate](/interest-rate/) environment. The underlying assets haven't defaulted, but the cash they generate has thinned.

The IC test asks: "Is the portfolio generating enough interest to keep senior noteholders whole every period?" It is a **cash-flow test**, not a balance-sheet test. Where the OC test measures solvency (do we have enough collateral?), the IC test measures liquidity (do we have enough income?).

## The calculation and threshold

The standard IC test formula is:

$$\text{IC Ratio} = \frac{\text{Interest Collected from Collateral}}{\text{Senior Notes' Interest Due}}$$

Interest collected includes [coupon payments](/coupon-payment/) and principal recovery from the loan portfolio, minus [defaults](/default-rate/) and write-downs. Senior notes' interest due is the sum of all [coupons](/coupon-rate/) owed to the senior and, sometimes, mezzanine tranches.

A deal might specify "IC test of 110%"—meaning collateral interest must be at least 110% of senior interest due. The extra margin is a buffer. If borrowers struggle or [spreads](/credit-spread/) compress, there is headroom before the ratio falls below 100% and the test breaches.

The test is typically **recalculated monthly or quarterly**, aligned with the periodic [coupon](/coupon-payment/) dates. Some deals allow for rolling adjustments: if one month is weak, the test might average the last three months' interest collections. This smoothing prevents a single bad month from triggering a permanent diversion.

## Breach mechanics: the cascade

When the IC ratio falls below the trigger—say, to 108% in a 110% deal—the immediate consequence is a **cash redirect**. Distributions that would have gone to [equity](/stock/) holders (and sometimes to [subordinated noteholders](/junk-bond/)) are instead applied to pay senior coupons in full.

If the shortfall is large, the redirect may not be enough. The next step is that available cash—instead of going to junior distributions—goes to **paying down senior principal**. This accelerates the [deleveraging](/leverage-ratio-forex/) of the fund and reduces the senior notes' outstanding balance, lowering future coupon obligations.

In a severe stress scenario, the IC breach can persist across multiple quarters. Junior distributions remain suspended until collateral interest recovers and the IC ratio climbs back above the threshold. This forces equity investors to wait, sometimes for months or years, while the [collateral manager](/collateral-manager/) works to improve the portfolio.

## How managers prevent breaches

A [collateral manager](/collateral-manager/) monitoring the IC ratio constantly asks: "Will next quarter's interest collections exceed senior obligations?" If the answer is no, the manager has several levers:

1. **Sell weak-performing loans** and [redeploy](/reinvestment-period/) proceeds into higher-[yielding](/yield-to-maturity/) credits. Swapping a 2% [coupon](/coupon-rate/) loan for a 5% coupon loan directly raises the portfolio's interest output.

2. **Accelerate principal paydowns** from performing borrowers. When a [leveraged buyout](/leveraged-buyout/) borrower refinances or repays early, the manager can redeploy that principal into higher-yielding loans (during the [reinvestment period](/reinvestment-period/)), rather than letting it sit in cash.

3. **Manage [floating-rate](/interest-rate/) exposure**. Many CLO loans have [floating-rate](/interest-rate/) coupons tied to [SOFR](/sofr/) or other benchmarks. In a falling-rate environment, the manager may hedge or shorten duration to preserve income. Conversely, in a rising-rate environment, floating-rate collateral becomes more valuable.

4. **Monitor [credit quality](/credit-rating/)**. If the collateral's [credit ratings](/credit-rating/) slip, [default rates](/default-rate/) may rise and interest collections may shrink. Proactive position-trimming and early distressed selling can prevent wholesale portfolio deterioration.

The [collateral manager](/collateral-manager/)'s fee is often tied to fund [net asset value](/net-asset-value/) or performance, so breaches hurt the manager's bottom line. This aligns incentives: the manager is motivated to keep the IC and OC ratios healthy.

## The interplay with overcollateralization

The IC test and OC test work in tandem but measure different dimensions of safety. A deal can breach its OC test (collateral value has eroded) while passing its IC test (current income still covers coupons). Conversely, a deal can breach its IC test (income has dried up) while passing its OC test (assets are still worth enough).

In practice, a deteriorating portfolio usually breaches both over time. Defaults reduce collateral value (triggering OC breach) and also eliminate interest collections (triggering IC breach). A manager who spots an IC breach knows that an OC breach may follow, and the urgency of portfolio repair increases.

Some indentures include a "remedy period"—a brief window after an IC breach during which the manager can cure the test without triggering a full distribution diversion. Others allow the manager to rebalance the collateral during the [reinvestment period](/reinvestment-period/) to shore up interest generation. These provisions give managers a fighting chance to avoid cascading breaches.

## Why investors care about IC

For [senior noteholders](/corporate-bond/), the IC test is a direct promise: "You will receive your coupon every period, or cash will be diverted to ensure you do." A breach signals portfolio stress, but the waterfall kicks in automatically to protect senior payments.

For [subordinated](/junk-bond/) and [equity investors](/stock/), an IC breach is a stoplight: distributions vanish, and returns evaporate until the breach is cured. An equity holder in a CLO that has just breached its IC test faces the grim realization that reinvestment and compound growth have been cut off, and the fund may take years to recover.

For [collateral managers](/collateral-manager/), the IC test is an ever-present operational constraint. Unlike a corporate [bond indenture](/bond/) that might trigger a default only after months of non-payment, the IC test is **mechanical and unforgiving**. Miss it once, and junior distributions stop immediately. The test is therefore a powerful forcing function for disciplined portfolio management.

## See also

<div class="wiki-seealso">

### Closely related

- [Overcollateralization Test](/over-collateralization-test/) — asset-value trigger paired with the IC test for dual-layer protection
- [Collateral Manager](/collateral-manager/) — portfolio steward responsible for maintaining both IC and OC ratios
- [Reinvestment Period](/reinvestment-period/) — window when manager can swap positions to improve income generation
- [Coupon Payment](/coupon-payment/) — senior obligations that the IC test measures against
- [Credit Rating](/credit-rating/) — portfolio credit quality drives interest collections and default rates
- Cash Waterfall — payment sequence through tranches; IC breach redirects flows to senior notes
- [Floating-Rate Loan](/interest-rate/) — collateral exposure that managers hedge to protect interest income

### Wider context

- Collateralised Loan Obligation — the primary vehicle using IC tests
- Collateralised Debt Obligation — similar cash flow-dependent structures
- [Bond](/bond/) — senior notes whose coupons the IC test protects
- [Subordinated Tranche](/junk-bond/) — junior noteholders first to lose distributions on IC breach
- Risk Management — structural safeguards in securitized finance

</div>
