---
title: "How CCP Clearing Fund Contributions Are Calculated"
description: "Central clearinghouses calculate each member's clearing fund contribution using stress tests and risk-based formulas to mutualize default risk beyond initial margin."
keywords:
  - clearing fund contribution calculation
  - CCP default fund
  - central counterparty risk
  - stress testing methodology
  - mutualized loss allocation
  - clearing member assessment
---

*A **clearing fund contribution** is the amount a clearing member must post to a central clearinghouse (CCP) to help cover losses if another member defaults. Unlike [initial-margin](/initial-margin/), which is purely customer-specific, the clearing fund is mutualized and risk-weighted across all members. Clearinghouses calculate each member's share using stress tests and historical loss scenarios.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clearing Fund Contribution — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">CCPs size the collective default fund to absorb the biggest plausible single-member loss; members share the cost on a risk-adjusted basis.</div>

|   |   |
|---|---|
| **Mutualized risk** | All members share the cost of any member's default |
| **Stress scenarios** | Historical and hypothetical market shocks applied to positions |
| **Risk metrics** | Notional, delta-adjusted, value-at-risk multipliers |
| **Tiered pricing** | Larger or riskier members pay proportionally more |
| **Waterfall** | Margin, then default fund, then CCP capital cover losses |
| **Mark-to-market** | Daily revaluation adjusts exposure estimates |
| **Procyclicality** | Contributions may rise during stress, adding liquidity pressure |
| **Portfolio concentration** | Risk weights may penalize members with correlated exposures |

</aside>

## The role of the clearing fund in the waterfall

When a clearing member defaults, the CCP must cover the losses from the defaulted member's positions. The financial waterfall works like this:

1. **Initial margin** on the defaulted member's account covers the first layer of loss.
2. **Clearing fund contributions** (also called the default fund) cover losses above initial margin.
3. **CCP capital** and insurance backstop any loss exceeding the default fund.

The initial margin is customer-specific and sized to cover a one- or two-day market move under normal conditions. The clearing fund, by contrast, is sized to absorb a far larger shock: the default of the single largest or most volatile member in a tail scenario. The CCP's goal is to keep the clearing fund large enough that it rarely needs to draw on CCP capital (which would trigger losses to shareholders or, in extremis, create solvency risk).

Because the clearing fund is mutualized, every member's contribution goes into a collective pot. If Member A defaults and leaves a €50 million loss, all members share that cost proportionally—not based on any direct exposure to Member A, but on their contribution to the fund. This creates an incentive problem (a member has less skin in the game if it doesn't contribute) but also a pooling benefit (no single member bears the full tail risk of any other).

## Stress testing methodology

CCPs size the clearing fund by running extensive stress tests on the portfolio of positions each member holds at the CCP. The methodology typically includes:

**Historical stress scenarios**: The CCP applies major past market shocks (e.g., the 2008 financial crisis, the 2020 COVID crash, the 2022 energy crisis) to today's portfolio. If a derivatives dealer holds a large swaption or credit portfolio, the CCP applies 2008's yield-curve moves, default rates, and volatility spikes to that portfolio to compute the mark-to-market loss.

**Hypothetical scenarios**: CCPs also construct forward-looking shocks (e.g., a 300 basis point parallel yield-curve shock, a 30% equity decline, a 50% drop in commodity prices) and revalue each member's positions under those moves. The loss under the worst single scenario becomes a measure of that member's exposure.

**Correlation stress**: A common assumption in normal risk models is that correlations are stable. Stress testing relaxes this: correlations go to one (everything falls together) or to negative extremes, which can flip hedges on their head. A member hedged against equity moves using bonds might face massive losses if equities and bonds both decline (as happened in 2022).

**Collateral haircuts**: The CCP also assumes that haircuts on collateral worsen during stress (e.g., corporate bonds decline in value, liquidity premia widen). A member that is "hedged" by posting low-haircut collateral may find that collateral is worth far less in a stress scenario.

The CCP runs these tests daily or weekly and computes the maximum loss (or a high percentile, e.g., 99th percentile) across all scenarios. This peak loss, summed across all members, defines the target clearing fund size.

## Risk-based contribution formulas

Not all members pose the same risk to the CCP. A large derivatives dealer with billions in notional exposure, high leverage, and concentrated positions in illiquid assets is riskier than a small broker with simple vanilla swaps and strong collateral. CCPs price this risk difference into contributions.

**Notional-based formula**: The simplest approach divides the clearing fund proportionally to each member's notional exposure. If Member A holds $100 billion notional and total member notional is $1 trillion, Member A pays 10% of the fund. This is transparent but crude—it ignores the risk profile of the positions.

**Value-at-risk (VaR) multiplier**: Many CCPs use each member's VaR (an estimate of the maximum loss under normal conditions, at a confidence level like 99%) as the risk metric, then multiply by a stress factor (often 1.5 to 3) to account for tail scenarios. A member with high VaR pays more. This better reflects risk but still misses tail correlations and basis risk.

**Stress-loss contribution**: The most rigorous approach computes each member's maximum loss across all stress scenarios and assigns contribution based on that loss. If Member A's peak loss across scenarios is $500 million and the sum of all members' peak losses is $5 billion, Member A contributes 10% of the target fund. This fully accounts for member-specific risk but is computationally intensive and can fluctuate daily.

**Tiered and capped contributions**: CCPs often layer these approaches. A base contribution might be notional-based (ensuring every member has "skin in the game"), an adjustment layer based on VaR accounts for volatility, and a cap prevents any single member from dominating the fund. Some CCPs also exempt very small members from the fund entirely, imposing only a minimum fixed fee.

## Procyclicality and liquidity concerns

A major criticism of risk-based clearing funds is procyclicality: during market stress (when volatility spikes, defaults rise, and correlations rise), members' VaR and stress losses explode. The CCP then demands higher contributions precisely when members are under liquidity pressure. A dealer facing large mark-to-market losses and margin calls on its own customer positions is also asked to pay more to the clearing fund—forcing it to raise liquidity or sell assets, which can amplify the market stress.

Regulators have encouraged CCPs to smooth or lag the calculation (e.g., use a rolling average of recent VaR rather than spot VaR, or cap quarter-to-quarter increases). Some jurisdictions require that any increase in contributions be phased in over time. These measures aim to decouple the fund from the short-term cycle, though they also mean the fund may be undersized during the exact moment a default occurs.

## Portfolio concentration and systemic risk

A more subtle issue is concentration. If the CCP's membership is dominated by a few large dealers who all have correlated positions (e.g., all long credit, all short volatility, all exposed to the same commodities), the stress loss across the group is not the sum of individual losses but potentially much larger. A scenario that triggers a default in one mega-dealer often triggers stress in all of them. Some CCPs apply concentration adjustments or increase the stress factors (e.g., multiplying by 4 instead of 2.5) for scenarios in which multiple large members are simultaneously distressed.

Another consideration is whether the member base itself is procyclical. During booms, a CCP attracts high-leverage dealers trading risky products. During downturns, the risky members default or reduce activity, and the safer members remain. The fund was sized for the boom composition but must cover losses from the bust composition.

## Clearing fund governance and adjustments

CCPs typically review clearing fund levels quarterly or annually. If market conditions have changed materially (e.g., interest rates have fallen, volatility has risen, major sector defaults have occurred), the CCP recomputes the stress scenarios and may increase the target level. Members are notified, and additional contributions are collected or older contributions released.

Some CCPs have established separate "resilience funds" or multiple tranches: a base fund that covers most single-member defaults, and a second-layer fund for tail scenarios. This allows for more granular risk pricing and clearer disclosure of who bears which tranches of loss.

## Regulatory requirements

Regulations like EMIR (Europe) and Dodd-Frank Title VII (US) impose minimum requirements on CCPs: the clearing fund must be sized to cover the default of the single largest member under a stress scenario specified by the regulator. In practice, this stress is severe: e.g., a 99.5% confidence interval move in market prices combined with a 20% haircut on collateral. The regulator also requires that CCPs cover this loss without drawing on general revenue, though CCP capital can be tapped after the fund is exhausted.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty risk](/counterparty-risk/) — The risk the clearing fund is designed to absorb
- [Central bank](/central-bank/) — Often serves as the backstop lender during clearing crises
- [Reserve requirements](/reserve-requirements/) — Similar mutualized prudential safeguards in banking
- [Credit risk](/credit-risk/) — The core risk being pooled and priced
- [Stress testing](/stress-testing/) — The methodology underlying fund sizing
- [Systemic risk](/systemic-risk/) — A clearing fund default could trigger wider contagion

### Wider context

- [Financial futures](/futures-contract/) — Most futures exchanges operate similar default funds
- [Credit default swap](/credit-default-swap/) — CCPs also clear CDS and use similar waterfall structures
- [Derivatives hedging](/derivatives-hedging/) — Users benefit from CCP guarantees but share the fund cost
- [Secured lending](/repurchase-agreement/) — Repos and other secured instruments also cleared through CCPs with similar safeguards

</div>
