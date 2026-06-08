---
title: "CCP Skin-in-the-Game: How Clearinghouses Share Default Losses"
description: "How CCP skin-in-the-game requirements force clearinghouses to commit capital before tapping clearing members' default funds."
keywords:
  - ccp skin in the game
  - clearing
  - clearinghouse
  - default fund
  - financial stability
  - risk management
---

*A **CCP skin-in-the-game** requirement mandates that a clearinghouse (CCP) commit a portion of its own capital to cover losses from clearing-member defaults, before accessing the mutualized default fund contributed by members. This aligns the CCP's incentives with member safety and reduces moral hazard.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CCP Skin-in-the-Game — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A clearinghouse's own capital absorbs initial losses, creating accountability.</div>

|   |   |
|---|---|
| **Purpose** | Align CCP incentives with member and market stability |
| **Amount** | Typically 25–50% of default-fund size |
| **Loss order** | CCP capital first, then member default fund, then wind-down |
| **Regulatory basis** | EMIR (EU), Dodd-Frank (US), FSB-CPMI principles |
| **Benefit** | CCP has financial reason to manage member risk strictly |
| **Risk** | If CCP capital is exhausted, member funds bear full subsequent loss |

</aside>

## The clearinghouse model and moral hazard

A clearinghouse (central counterparty, or CCP) sits between buyers and sellers in derivatives and securities markets. It becomes the buyer to every seller and the seller to every buyer, netting positions and collateralizing risk. If a member defaults—cannot post margin or meet settlement obligations—the CCP must cover losses immediately to prevent contagion.

Historically, CCPs were funded via a mutualized default fund (a pool of cash and securities contributed by clearing members). Each member put in capital based on their market activity, and the fund sat as a buffer against member failure. But a moral hazard arose: because the default fund was mutualized, no individual CCP had a direct financial incentive to scrutinize members' risk-taking tightly. The CCP's revenue came from membership fees and margin collected; if a member blew up, the loss fell on the pool, not the CCP itself.

After the 2008 crisis, regulators worldwide (especially the Financial Stability Board, EMIR in Europe, and the Dodd-Frank Act in the US) imposed skin-in-the-game rules to close that gap. A CCP now must commit its own capital to the loss-absorption waterfall.

## The loss waterfall: order and scale

The modern loss-absorption hierarchy works as follows:

1. **Member margins** cover routine daily variation in positions. Collateral is posted upfront.
2. **CCP capital** (skin-in-the-game) is the first loss layer when a default occurs. The CCP draws on retained earnings or dedicated capital reserves.
3. **Default fund** (member contributions) is tapped only after the CCP's capital is exhausted.
4. **Surviving members** may be assessed additional contributions if the default fund is depleted.
5. **CCP recovery or wind-down** occurs if losses exceed available resources.

The CCP's capital typically represents 25 to 50 percent of the default fund's size. For a major exchange's CCP with a $1 billion default fund, the CCP might commit $300–500 million of its own capital.

## Why it changes behavior: incentive alignment

With skin-in-the-game, the CCP's management has a direct financial stake in member solvency. If a member takes excessive risk and fails, the CCP absorbs the initial hit. This creates powerful incentives to:

- **Monitor members closely.** The CCP now has reason to audit trading behavior, enforce position limits rigorously, and demand frequent margin updates.
- **Set stricter margin models.** A CCP wants sufficient collateral upfront to avoid drawing on its capital. This raises the cost of leverage for all members.
- **Exclude or delever risky members.** A CCP can justify kicking out or forcing deleveraging of a member whose risk profile threatens the CCP's capital.
- **Invest conservatively.** The CCP's own capital (typically invested in short-term, liquid assets) is protected, reducing the temptation to chase yield.

Before skin-in-the-game rules, a CCP had weak incentives to do any of this. The default fund was the members' problem. After the rules, the CCP became a steward of systemic stability.

## Regulatory rationale: financial stability

Regulators imposed skin-in-the-game rules because CCPs had become critical infrastructure. By 2008, most derivatives trades were cleared through CCPs, not bilateral credit. A CCP failure would cascade through the entire financial system. If a CCP lacked a financial reason to manage member risk, the potential for systemic failure rose dramatically.

The skin-in-the-game rule is a simple mechanism: make the gatekeeper a stakeholder. A CCP that owns capital in the default waterfall cannot claim neutrality or hide behind member contributions. Regulators can also demand that a CCP meet minimum capital ratios relative to the default fund, enforcing the rule numerically.

## Practical impact: margin and deleveraging

In practice, skin-in-the-game has tightened clearing standards. CCPs have raised margin requirements and shortened margin collection cycles (from daily to intra-day). They monitor positions more granularly. Members face higher costs to clear trades, which in turn raises trading costs for end investors (hedgers and speculators alike).

Some say this is appropriate: markets were under-collateralized before 2008, and skin-in-the-game makes them safer. Others argue that the burden has shifted from CCPs to members and ultimately to end users, and that clearing costs have risen too high.

In moments of market stress, a CCP may call extraordinary margin or impose position limits on members to protect its capital. This can amplify volatility. For example, if a member faces losses, the CCP demands more margin; the member is forced to sell positions; other members see losses from those sales and face margin calls; a cascade occurs. Skin-in-the-game does not eliminate this; it only ensures the CCP has tried to prevent it by being strict upfront.

## Risk of capital exhaustion

Skin-in-the-game is only as good as the CCP's capital. If a single default is large enough to exhaust the CCP's contribution, the default fund bears the full remaining loss. If a second default follows while the default fund is depleted, surviving members face assessment calls—demands for additional capital.

This creates a perverse incentive at the margin: a member close to the edge of the default fund might pressure the CCP to move quickly to wind down the failed member and recover collateral, even if faster recovery is costlier. The surviving members want to preserve what is left of the default fund for their own potential benefit.

Some CCPs have addressed this by maintaining a two-tier default fund structure, with a larger first tier funded by all members and a smaller second tier funded only by the largest members. This reduces the probability that any single default exhausts the CCP's capital alone.

## Real-world examples and testing

After the 2008 crisis, most major CCPs (CME, Eurex, LCH, ICE) adopted skin-in-the-game rules. The COVID-19 market crash of March 2020 tested the system. Volatility spiked, margin calls surged, and some members faced stress—but no CCPs drew significantly on their capital, and no defaults propagated. Observers credited strict margin practices and skin-in-the-game as stabilizing.

However, some argue that 2020 would have been worse without massive central-bank support (rate cuts, quantitative easing, reverse-repo facilities). A true test may never come if central banks intervene early and aggressively.

## Tensions with profitability

Skin-in-the-game also reduces CCP profitability. A clearinghouse that ties up 25–50% of the default-fund size in capital earns lower returns on assets. CCPs have thus consolidated; the number of major CCPs globally has shrunk, creating concentration risk. A few large, well-capitalized CCPs now dominate each asset class, reducing competition and leaving smaller venues stranded.

Regulators tolerate this consolidation as a trade-off for safety. A large, well-funded CCP is better positioned to absorb a member default than a small CCP with thin capital. But the concentration raises systemic importance—if a major CCP fails, the impact is immense.

## See also

<div class="wiki-seealso">

### Closely related

- Clearinghouse — The institutional structure that skin-in-the-game rules apply to
- Central counterparty — The role and regulatory framework for CCPs
- [Default fund](/default-fund/) — The mutualized loss-absorption pool that follows CCP capital
- [Margin call](/margin-call-forex/) — The daily mechanism that protects against member default
- [Counterparty risk](/counterparty-risk/) — The risk a CCP manages and must incentivize itself to control

### Wider context

- [Systemic risk](/systemic-risk/) — Why CCP stability is a financial-stability issue
- [Financial Stability Board](/financial-stability-board/) — The international body that drove skin-in-the-game rules
- [Dodd-Frank Act](/dodd-frank-act/) — The US legislation that formalized CCP skin-in-the-game
- [Risk-weighted assets](/risk-weighted-assets/) — How regulators measure CCP capital adequacy

</div>