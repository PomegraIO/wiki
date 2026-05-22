---
title: "CCP Default Waterfall"
description: "Hierarchical loss-absorption mechanism triggered when a central counterparty member defaults"
keywords:
  - central counterparty
  - default management
  - loss absorption
  - clearing member
  - financial stability
---

*The **CCP default waterfall** is a layered fund-raising and loss-allocation framework that a [central counterparty clearinghouse](/wiki/central-counterparty-clearing/) activates when a member fails. It ranks claims in priority order: first the defaulted member's own collateral (margin), then the CCP's guarantee fund, then the CCP's own capital, and finally—in the most extreme scenario—surviving members' contributions. The waterfall's design is meant to ring-fence losses while preserving market integrity.*

<aside class="wiki-infobox">

| Layer | Source | Order |
|---|---|---|
| **1st** | Defaulted member's margin | Applied immediately |
| **2nd** | Defaulted member's default fund contribution | Before CCP capital |
| **3rd** | CCP guarantee fund (mutually funded) | Multi-member pool |
| **4th** | CCP's own capital | Institutions stake |
| **5th** | Surviving members' assessment | Pro-rata charge, capped |
| **6th** | Liquidity facilities / public backstop | Emergency lever only |
| **Waterfall principle** | Mutualized risk above layer 2 | Spreads cost across market |

</aside>

## Why a waterfall exists: contagion prevention

Before the 2008 financial crisis, most clearinghouses had modest default-management rules. When [Lehman Brothers collapsed](/wiki/lehman-brothers-collapse/) in 2008, its clearinghouses faced enormous open positions across derivatives and repo. One clearinghouse, LCH.Clearnet, suffered a $71 million loss when Lehman's positions could not be hedged cleanly; the clearinghouse absorbed it from its own capital. The Dodd-Frank Act and subsequent international agreements (Basel III, EMIR) mandated that CCPs pre-fund a waterfall architecture so that a single member's default would not deplete the clearinghouse's reserves or cascade losses onto other members without warning.

The waterfall's purpose is twofold. *First,* it ensures sufficient liquidity and capital are pre-positioned to manage a default without market-disruptive fire sales of collateral. *Second,* it distributes losses predictably so surviving members (who are also CCP shareholders) know their maximum exposure before a crisis hits. This transparency is meant to reduce panic and maintain confidence in the clearinghouse.

## Layer 1: The defaulted member's own margin

When a member fails to meet a margin call or declares bankruptcy, the CCP immediately seizes all collateral (margin) posted by that member. For futures and options traded at exchanges like the CME, this includes initial margin and variation margin. For derivatives cleared at ICE or LCH, this is both initial and variation margin across all products.

Margin is sized to cover typical daily volatility plus a confidence interval (usually 99% over a 1-day horizon for futures, longer for OTC). In a slow-moving market, the defaulted member's margin is often sufficient to cover losses from unwinding their open positions. But in a flash crash or fast gap move, margin will not be enough. That is when layer 2 activates.

## Layer 2: The defaulted member's default fund contribution

Each member contributes to a default fund (also called a guarantee fund or guarantee bond fund). The size of each member's contribution is computed by the CCP using a risk-based model, often tied to that member's average notional open interest or gross margin. A large dealer might contribute $500 million; a regional broker, $50 million.

When a member defaults, the CCP draws on *only that member's* default fund contribution first—not the pool. This two-tiered approach gives members whose contributions are highest a small advantage: their own capital is burned before they start paying for the defaulter's losses mutualized across all members. In practice, this distinction is often moot because a large default exhausts the individual contribution immediately.

## Layer 3: The default fund pool (mutualized contributions)

Once the defaulted member's own contribution is exhausted, the CCP draws on the shared default fund pool. This is the core of mutualization: all surviving members' contributions become available pro-rata or per the CCP's rules. If the pool is $5 billion and a default loss exceeds the member's $100 million contribution, the CCP may assess the remaining $4.9 billion pool. Surviving members do not have a choice about this assessment; it is binding in their membership agreement.

The default fund pool is the primary cushion. At major CCPs like [LCH.Clearnet](/wiki/lch-clearnet/), CME Clearing, and ICE Clear Credit, the pool typically ranges from $10 billion to $50 billion, depending on business volume and historical stress tests. The CCP conducts annual stress tests (usually covering historical scenarios like the 2008 crisis or 1987 [Black Monday](/wiki/black-monday-1987/)) to size the pool adequately.

## Layer 4: The CCP's own capital

If the default fund is depleted, the CCP begins burning its own capital. This is a pivotal moment: the clearinghouse has moved from "mutualized member contributions" to "institutional insurance." Most CCPs maintain capital equal to 25% of their default fund, or about $2–10 billion for systemically important ones. This is a financial incentive for the CCP to manage risk conservatively—the institution itself is at stake.

Drawing on own capital also signals to markets that the CCP is capable of absorbing extraordinary loss. This is why regulators scrutinize a CCP's capital ratio. If a CCP has only 5% capital relative to its default fund, it signals under-capitalization and may trigger rating downgrades or restrictions on new clearing memberships.

## Layer 5: Survivor member assessment (loss mutualization extended)

Once the CCP's capital is exhausted (a scenario that has never occurred at a major CCP), the waterfall enters the final stage: the CCP assesses surviving members for additional contributions. This is the "nuclear option" for a clearinghouse. Members face an open-ended liability to cover losses beyond the CCP's capital.

Jurisdictions differ on assessment mechanics:

- **U.S. (Dodd-Frank rules):** The CCP may assess surviving members up to 25% of their average default fund contribution, capped at some absolute total. This cap (often called a "assessment cap") prevents a single member from bearing an unlimited burden.
- **EU (EMIR rules):** Similar structure, but the cap is typically 25% of the member's contributions over a rolling period.
- **Japan (JSCC rules):** Assessment can extend further, reflecting a philosophy that clearinghouses are financial utilities that must be backstopped by members collectively.

When a member is hit with an assessment, they typically have 30–90 days to settle in cash. Failure to do so can result in immediate default, creating a cascade risk. This is why members monitor CCP solvency closely and maintain dedicated assessment reserves.

## Layer 6: Liquidity facilities and public backstops

In an unprecedented crisis where the waterfall is wholly insufficient, a CCP may activate emergency liquidity facilities backed by central banks. The Bank of England's Loan Facility for Insolvent Clearing Members (a tool introduced in the 2008 crisis) and equivalent arrangements at the Fed allow CCPs to borrow against the CCP's own capital or default fund. These are last-resort measures and have not been formally tapped in modern times.

Some jurisdictions empower governments to inject capital directly. The EU's Resolution Directive grants powers to national authorities to recapitalize a CCP if it becomes critical to financial stability. This is controversial because it amounts to taxpayer insurance for the derivatives market.

## How the waterfall affects member behavior

Knowing they face potential assessments, large dealers and investment firms allocate internal capital to cover maximum plausible CCP assessments. A systematic default at a major CCP could require a surviving member with $500 million in default-fund contributions to pay an additional $100+ million in assessments. Large dealers routinely model "CCP default scenarios" as part of [counterparty risk](/wiki/counterparty-credit-risk/) management, similar to [stress testing](/wiki/stress-testing/) for their own firms.

This creates a second-order effect: members adjust leverage and position sizes partly on the basis of CCP risk. If a CCP's default fund shrinks due to member withdrawals (fewer clearing members post-crisis consolidation), surviving members' exposure to assessment increases, which can drive some members away. This is why CCPs are cautious about member churn.

## Gaps and critiques

**Procyclicality:** Default fund contributions are often sized based on recent volatility and open interest. In a boom, low volatility means lower contributions; in a crash, contributions rise sharply. This creates a pro-cyclical effect: the fund is smallest when risk is highest.

**Opacity of loss allocation:** While the waterfall structure is public, the precise rules for allocating losses within the default fund—especially if a partial default exhausts only part of the pool—can be ambiguous. Different CCPs use different methodologies (pro-rata contributions, notional exposure, initial margin charged).

**Interconnection risk:** CCPs are themselves counterparties to each other. When a member posts collateral across multiple CCPs (a large bank might clear at CME, LCH, Eurex, and ICE simultaneously), a major member default can trigger waterfall draws at multiple institutions simultaneously, creating system-wide stress.

<div class="wiki-seealso">

### Closely related
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — CCP core functions and governance
- [Counterparty Credit Risk](/wiki/counterparty-credit-risk/) — Risk of member default
- [Margin and Initial Margin](/wiki/initial-margin/) — Collateral underpinning the waterfall
- [Default Fund](/wiki/hedge-fund-lock-up-redemption/) — Member guarantee contributions

### Wider context
- [Clearing Member Risk](/wiki/clearing-member-risk/) — Systemic exposure of CCPs
- [Financial Stability](/wiki/financial-stability-oversight-council/) — CCP role in broader market stability
- [2008 Financial Crisis](/wiki/lehman-brothers-collapse/) — Event that motivated modern waterfall rules
- [Basel III](/wiki/basel-iii/) — Post-crisis regulatory framework for CCPs

</div>
