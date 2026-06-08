---
title: "Clearinghouse Default Fund Explained"
description: "A clearinghouse default fund pools member contributions to cover losses when a central counterparty member defaults. How sizing and draw mechanics work."
keywords:
  - clearinghouse default fund how it works
  - central counterparty default fund
  - clearing member default protection
  - ccp default fund
  - clearinghouse member contributions
  - systemic risk clearing
image: /svg/institutions.svg
---

*A **clearinghouse default fund** is a pool of cash and liquid securities contributed by clearing members to absorb losses if a member fails to meet its obligations to the central counterparty (CCP). The fund is sized based on member risk profiles and is drawn down sequentially: first the defaulting member's own collateral, then the default fund, then the CCP's own capital.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clearinghouse Default Fund — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions." />

<div class="wiki-infobox-caption">A shared safety net: members post capital to cover the tail risk of peer default.</div>

|   |   |
|---|---|
| **Who contributes** | All clearing members; size scaled by risk (notional exposure, margin) |
| **Size** | Typically $1B–$10B+ depending on asset class and CCP |
| **How it's drawn** | Member collateral first; then default fund pro rata; then CCP capital |
| **Replenishment** | Members rebuild contributions after a draw (over weeks to months) |
| **Investment** | Held in cash, T-bills, or other highly liquid instruments |
| **Testing** | CCPs stress-test scenarios (loss of largest or two largest members) |
| **Governance** | Set by CCP board; often approved by regulators (SEC, CFTC) |

</aside>

## The clearing landscape and member risk

A central counterparty (CCP) sits between buyer and seller in derivative and securities trades, guaranteeing both sides of the transaction. This reduces [counterparty risk](/counterparty-risk/) — the chance that a dealer will default — but concentrates it in the CCP itself. If a major clearing member (a bank or asset manager) fails and cannot post margin or settle its positions, the CCP absorbs the loss.

The default fund is the mechanism by which *non-defaulting members* absorb a defaulting member's losses, rather than the CCP or the broader financial system. It is, in effect, **mutualized loss-sharing** — a covenant among members that each will chip in to save the system from catastrophe.

## How the default fund is sized

Default fund sizing follows a regulatory and economic logic:

**Regulatory floor:** Global standards (CPMI-IOSCO principles) require CCPs to maintain a default fund large enough to cover the loss from the **two largest clearing members simultaneously failing and unable to post additional margin.** This is called the "Cover 2" or "Cover 1.5" standard (varying by jurisdiction). For equity and FX derivatives, "Cover 1" (largest member only) is sometimes acceptable.

**CCP internal model:** The CCP runs a stress test. It shocks the market (rates up 200bps, credit spreads widen, vol spikes, FX shifts), reprices all outstanding positions, and calculates the mark-to-market loss if the largest member cannot meet its margin call. That projected loss is the floor for the default fund.

**Member contributions:** Each member posts a contribution proportional to its risk. The CCP uses metrics like:
- **Notional exposure:** Gross value of derivatives outstanding.
- **Initial margin required:** The CCP's daily margin calculation already reflects member risk; high-margin members pay more.
- **Concentration:** A member with large positions in a single name or sector pays a premium.
- **Credit rating:** Lower-rated members may post higher contributions.

**Example:** A CCP for interest-rate swaps might have a $5B default fund. Bank A, a major user, posts $500M (10% of total). Bank B, a smaller participant, posts $100M (2% of total). A mid-sized regional bank posts $50M. Each is entitled to recover pro rata if the fund is drawn.

## The waterfall: who pays what and when

When a clearing member defaults, losses are absorbed in a defined sequence:

**1. Defaulting member's collateral.** The CCP first liquidates the member's posted margin (initial and variation) and any other unsecured claims against it (e.g., cash on deposit).

**2. Default fund draw (pro rata).** If the liquidation proceeds are insufficient, the CCP draws from the default fund. Non-defaulting members' capital is deployed **in proportion to their contributions**, not in proportion to their exposure.

**Example:** The default fund has $5B. Bank A posted $500M (10%); Bank B posted $1B (20%); others posted $3.5B (70%). A member defaults and liquidation yields $2B. The shortfall is $3B. The CCP draws from the default fund:
- Bank A pays: $3B × 10% = $300M
- Bank B pays: $3B × 20% = $600M
- Others pay: $3B × 70% = $2.1B

**3. CCP capital.** After the default fund is exhausted, the CCP uses its own capital (equity, insurance, or lines of credit from banks). Some CCPs maintain an explicit financial backstop (e.g., $10B in CCP equity reserved for this purpose).

**4. Clawback or member levies (in extremis).** If the CCP's own capital is exhausted, the exchange operator or parent company may inject capital, or members may be assessed an additional levy. This is rare but possible; it signals systemic stress.

## Replenishment and ongoing management

Once the default fund is drawn, the CCP replenishes it. Non-defaulting members are required to rebuild their contributions over a set period (days to weeks). This ensures the fund returns to its target level quickly, protecting against cascading defaults.

Replenishment can be controversial:
- **Fairness:** Should a member that posed no risk still pay to cover another's loss? The answer is yes — membership in the clearing system entails mutual responsibility.
- **Procyclicality:** In a crisis, requiring large capital calls on surviving members can strain their balance sheets and propagate stress. Some regulators now allow *graduated* replenishment, spreading the cost over months.

## Real-world examples

**2008 financial crisis:** No major CCP default occurred, but default funds were stress-tested. Clearinghouses expanded their funds significantly.

**Lehman Brothers (2008):** LCH.Clearnet (which cleared Lehman's repo transactions) and CME Clearing (which cleared its derivatives) drew on their default funds. The draws were absorbed by the waterfall; no member paid at the time, but the CCP's capital was used.

**Archegos Capital (March 2021):** Archegos' prime brokers (Goldman Sachs, Morgan Stanley, others) took losses on equity derivative positions they had not fully hedged. While Archegos was not a direct clearing member, the episode highlighted how prime-broker margin systems can differ from CCP default funds — and how important mutualized loss-sharing is when dealer networks face large, sudden shocks.

## Governance and regulatory oversight

**CCP Boards** decide default fund size in consultation with their risk committees. Board composition typically includes representatives of:
- Clearing members.
- The exchange operator.
- Independent risk experts.

**Regulatory approval:** In the U.S., the SEC (for securities CCPs like NSCC) and the CFTC (for derivatives CCPs like CME Clearing) approve default fund levels and changes. In the EU, ESMA oversees CCPs. This prevents a CCP from under-funding and shifting risk to the public sector.

**Stress testing:** CCPs are required to conduct *at least* monthly stress tests and disclose results to regulators. Members often conduct their own independent tests to model their exposure to a draw.

## The investment and yield question

Default funds are held in highly liquid, low-default-risk instruments: cash, Treasury bills, and repo. They are *not* invested in equities or credit; the point is safety and availability, not yield.

This creates a cost: members earn little or nothing on their contributed capital. Some have argued for allowing a small equity allocation or lending default funds to members against collateral (like Treasury repos) to generate modest returns. Regulators are cautious, fearing that yield-chasing will erode the fund's integrity.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty Risk](/counterparty-risk/) — the systemic risk a CCP default fund mitigates
- [Central Bank](/central-bank/) — often a backstop guarantor if a CCP fails
- [Securitization](/securitization/) — a process that relies on clearinghouse guarantees
- [Credit Default Swap](/credit-default-swap/) — a derivative product cleared through CCPs with default fund protection
- [Repurchase Agreement](/repurchase-agreement/) — a repo market transaction often cleared through CCPs
- [Systemic Risk](/systemic-risk/) — the broader financial stability issue default funds address

### Wider context

- [Derivative](/derivatives-hedging/) — the primary products cleared and covered by default funds
- [Federal Reserve](/federal-reserve/) — backstop provider and supervisor of systemically important CCPs
- [Over-the-Counter Market](/over-the-counter-market/) — the pre-clearinghouse derivatives market with higher counterparty risk
- [Market Maker](/market-maker-trading/) — clearing members who depend on CCP guarantees to operate

</div>
