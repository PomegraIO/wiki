---
title: "Static vs Managed CLO: Key Differences"
description: "Understand static vs managed CLOs: static vehicles hold fixed loan pools from closing, while managed CLOs allow active trading during reinvestment periods."
keywords:
  - static vs managed clo
  - clo collateral manager
  - reinvestment period clo
  - clo structure comparison
  - loan pool management
---

*A **static CLO** holds a fixed pool of loans from closing until maturity, while a **managed CLO** allows the collateral manager to trade loans during a designated reinvestment period. The choice affects risk, manager skill exposure, and the stability of cash flows to investors.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Static vs Managed CLO — structure essentials</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Static CLOs lock in collateral at closing; managed CLOs trade loans to optimize portfolio performance.</div>

|   |   |
|---|---|
| **Static CLO** | Fixed loan pool from closing to maturity |
| **Managed CLO** | Active trading during reinvestment period |
| **Collateral manager role** | Passive (static) or active (managed) |
| **Reinvestment period** | Absent (static) or typically 3–8 years |
| **Investor control** | Covenants govern loan amortization; manager has limited discretion |
| **Risk profile** | Static: predictable defaults; Managed: exposed to manager skill and timing risk |
| **Fee structure** | Management fees higher on managed CLOs due to active oversight |

</aside>

## How static CLOs work

In a **static CLO**, the collateral manager sources and purchases a portfolio of loans before the legal closing. Once the securitization closes, the loan pool is locked in. Investors know exactly which loans back their tranches. The manager has no discretion to swap loans or add new names to the portfolio. Cash flows—principal repayments, prepayments, and default losses—flow through the structure as they occur, but the underlying collateral is unchanged for the life of the deal.

Static CLOs were the dominant structure in the early stages of the CLO market, particularly during the 1990s and 2000s. Because the portfolio is fixed, there are no ongoing decisions for the manager to make. The manager's job is largely to service the loans (monitor covenants, track obligor credit quality) and ensure the structure complies with its legal constraints. Investors in static CLOs benefit from transparency: they can model future cash flows based on observed default rates and prepayment speeds of the fixed collateral pool.

However, static CLOs also lock in the initial loan selection. If the manager made errors in picking credits, or if market conditions shift sharply after closing, the investor has no recourse to portfolio adjustments. The collateral ages, and the manager cannot refresh it with new loans to maintain credit quality.

## How managed CLOs work

A **managed CLO** grants the collateral manager explicit authority to trade loans during a defined **reinvestment period**, typically lasting 3 to 8 years from closing. During this window, the manager may sell loans from the portfolio and use the proceeds (and new principal repayments) to buy replacement loans. The manager is expected to optimize the portfolio—rotating out deteriorating credits, capturing price dislocations, and adjusting sector or exposure concentrations to maintain or improve credit quality and portfolio yield.

The reinvestment period is crucial. During it, principal proceeds from loan amortization and unscheduled payoffs can be reinvested in new loans. After the reinvestment period ends, the CLO typically enters an **amortization period**, where principal is returned to investors rather than reinvested. This discipline prevents the manager from holding the collateral indefinitely and forces a wind-down.

Active management introduces skill—the manager can identify improving credits to buy at a discount, rotate away from deteriorating obligors, and rebalance the portfolio in response to economic cycles or sector shocks. This flexibility is a significant advantage in volatile credit environments. However, it also introduces **manager risk**: the skill level varies, and managers may make poor trading decisions or become overconfident in their market timing.

## The reinvestment period and call windows

Both static and managed CLOs may have call options, but reinvestment periods are the defining feature of managed deals. During the reinvestment period, a managed CLO is said to be in an "**active period**." The manager continually buys and sells loans to fine-tune the portfolio.

Once the reinvestment period expires, the CLO enters amortization. Principal is returned to investors in order of seniority. If the manager is not actively trading, the CLO drifts toward static behavior as the collateral pool shrinks through payoffs and defaults.

Some CLOs have a **hard maturity date** (typically 12–15 years from closing) at which point any remaining collateral is liquidated and investors receive principal. Others have a **legal final maturity** tied to the slowest-paying loan in the pool, but in practice they pay down much faster.

## Risk profiles and investor implications

**Static CLOs** offer clarity but limit upside potential. Investors know their collateral and can run stress tests on a fixed set of obligors. The tradeoff is that portfolio aging and lack of refresh can pressure credit quality over time. A static CLO is well-suited to conservative investors who want to understand and model the exact cash-flow dynamics.

**Managed CLOs** introduce manager alpha (or error). A skilled manager can materially improve returns by rotating out troubled credits before losses occur and capitalizing on temporary mispricings. However, a poor manager—or a competent one caught in a severe market downturn—can underperform. Investors in managed CLOs are implicitly betting on the manager's skill and discipline.

The fee structure reflects this. Managed CLOs charge higher management fees (often 0.25% to 0.50% of collateral par annually, versus lower or flat fees for static deals) to compensate the manager for ongoing work. Some managed CLOs also include incentive or performance fees tied to excess returns above a hurdle rate.

## Practical market context

In recent years (roughly 2010–2024), **managed CLOs have dominated** new issuance. The market learned from defaults during the 2008 financial crisis that fixed loan pools can deteriorate rapidly. Active managers provide a cushion. Moreover, strong collateral managers have built track records demonstrating that active trading improves recovery rates and reduces default clustering.

That said, static CLOs still exist, particularly in the form of **single-asset CLOs** (which finance one large loan or a small group of similar loans) or in niche markets where simplicity and transparency are valued.

## Monitoring and covenants

Both static and managed CLOs include detailed deal documents with covenants that protect investors. These include:

- **Overcollateralization tests** (the par value of collateral must exceed the outstanding notional of each tranche)
- **Interest coverage tests** (available interest must cover all expenses and senior tranches)
- **Minimum weighted-average rating tests** (WART)
- **Minimum weighted-average spread tests** (WARS)

For managed CLOs, covenants are tighter on the manager's trading freedom. If the CLO fails a test, the manager's reinvestment rights may be curtailed or suspended, forcing amortization to begin early.

## See also

<div class="wiki-seealso">

### Closely related

- [CLO structure and tranches](/collateralized-loan-obligation/) — overview of how CLOs allocate risk across investor classes
- [Credit-card ABS mechanics](/credit-card-abs-mechanics/) — example of active portfolio management in a different securitization context
- [Subordination levels](/subordination-level-sizing/) — how credit enhancement thickness is set across tranches
- [Tail risk in structured credit](/tail-risk-structured-credit/) — why manager-driven portfolio shifts can amplify tail losses

### Wider context

- [Securitization](/securitization/) — foundational concept for all structured credit
- [Hedge fund](/hedge-fund/) — parallels with active collateral management
- [Credit default swap](/credit-default-swap/) — tools managers use to hedge or express views
- [Covenant](/corporate-bond/) — protections embedded in CLO loan agreements
- [Concentration risk](/concentration-risk/) — key consideration when evaluating static loan pools

</div>
