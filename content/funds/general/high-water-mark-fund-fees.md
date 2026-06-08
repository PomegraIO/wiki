---
title: "High-Water Mark in Fund Fee Structures"
description: "Understand how high-water mark provisions protect investors from paying performance fees twice on the same gains."
keywords:
  - high water mark
  - performance fee
  - fund fee structure
  - hurdle rate
image: /svg/funds.svg
---

*A **high-water mark** is a threshold that prevents a fund manager from collecting [performance fees](/performance-fee/) until the fund recovers all past losses. Once the fund hits a new peak in value, the manager begins earning performance fees again—but only on gains above that highest previous net asset value. This rule protects investors from paying twice for the same returns.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">High-Water Mark — Key Facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A gatekeeping mechanism that ties manager compensation to genuine new wealth creation.</div>

|   |   |
|---|---|
| **Definition** | The highest net asset value per share the fund has ever reached |
| **Effect** | Manager earns performance fees only on gains above the prior peak |
| **Investor benefit** | Avoids double-charging for the same returns; aligns incentives |
| **Calculation** | Performance fee triggered only when fund NAV exceeds previous high-water mark |
| **Common in** | [Hedge funds](/hedge-fund/), [private equity](/private-equity-fund/), [mutual funds](/mutual-fund/) with performance fees |
| **Duration** | Persists across redemptions; typically resets only at fund termination or explicit amendment |

</aside>

## The problem it solves: double-charging for recovery

Imagine a fund with $100 per share net asset value in year one. In year two, poor performance cuts the NAV to $80. In year three, strong performance restores it to $100. Without a high-water mark, the manager could claim a 20% performance fee on the $20 recovery—effectively charging investors for profits that merely restored losses they had already suffered.

A high-water mark prevents this inequity. The manager earns no performance fee during year three's recovery because the fund has only returned to its prior peak; no new wealth has been created yet. Only when the fund exceeds $100 per share does the manager's incentive fee kick in, applying only to gains above that waterline.

## How it's calculated in practice

The high-water mark is tied to [net asset value](/net-asset-value/) per share, computed after the deduction of all fees and realized and unrealized losses. The calculation unfolds simply:

1. **Establish the baseline**: The highest closing NAV per share the fund has ever achieved (often called the "prior peak").
2. **Calculate current NAV**: Determine the fund's current NAV per share after all costs.
3. **Assess the incentive trigger**: If current NAV > prior peak NAV, the manager earns a performance fee only on the excess (current NAV minus prior peak NAV, multiplied by the number of outstanding shares and the performance fee percentage).
4. **Update the mark**: If the fund sets a new record NAV, that becomes the new high-water mark for the next period.

## Example walkthrough

Suppose a [hedge fund](/hedge-fund/) with 1 million shares outstanding has a high-water mark of $50 per share (the fund's all-time peak NAV). The current NAV stands at $48, down from the prior peak due to recent losses. The manager charges a 20% performance fee.

| Scenario | Current NAV | Mark status | Performance fee earned |
|----------|-------------|-------------|------------------------|
| Fund at $48/share | $48 | Below mark | $0 (no new gains to reward) |
| Fund recovers to $50/share | $50 | At mark | $0 (only recovered losses) |
| Fund rises to $52/share | $52 | Above mark | 20% × ($52 − $50) × 1M shares = $400,000 |
| Fund surges to $55/share | $55 | New high-water mark | 20% × ($55 − $50) × 1M shares = $1,000,000; new mark = $55 |

In the last scenario, the fund's new peak becomes $55 per share, and that is the floor for all future performance fee calculations.

## Protecting investors from the recovery trap

The high-water mark's greatest strength is preventing managers from extracting fees during periods of reversion to prior levels. Without it, a manager could engineer a boom-and-bust cycle, pocketing fees on each rebound while leaving shareholders to bear the losses.

Consider a realistic multi-year scenario: a $100M fund suffers a 30% loss (down to $70M) in a bear market. The manager's compensation is already diminished because [management fees](/management-fee/) are typically assessed on current AUM. In the recovery year, the fund climbs back to $100M—a 43% return. Without a high-water mark, the manager would claim a performance fee (say, 20%) on that entire $30M gain, even though shareholders have only recouped their losses, not achieved new profits.

With the high-water mark, the manager earns nothing during recovery, creating a period in which the manager has aligned incentives—both must wait for true new gains. This dynamic often motivates managers to accelerate recoveries and can even raise governance questions: should a manager taking an extended period to climb back to the high-water mark be retained?

## When high-water marks don't apply

Not all funds use high-water marks. Many [mutual funds](/mutual-fund/) without explicit performance fees have no need for one. [Index funds](/index-fund/) and passively managed funds typically charge only a [management fee](/management-fee/), which accrues whether the fund is up or down.

Some [private equity funds](/private-equity-fund/) and [hedge funds](/hedge-fund/) negotiate contracts that omit high-water marks in exchange for lower performance fees, though this is the exception. [Business development companies](/business-development-company/), which operate under specific regulatory structures, may have idiosyncratic fee mechanics.

In jurisdictions or fund structures where performance fees reset annually (rare and controversial), a high-water mark offers less protection because the manager can claim fees on annual gains even if the multi-year track record is underwater. Investors should always ask whether their fund uses a high-water mark and, if not, why.

## Interaction with redemptions and share classes

A high-water mark persists across [redemptions](/fund-redemption-queue-mechanics/). If an investor redeems at $50 per share while the mark is still $60, the mark doesn't adjust for that departing capital. The fund maintains the $60 waterline, and the manager continues to await new gains above that level.

In funds with multiple share classes, each class may have its own high-water mark or may share a single mark. The structure varies by fund and is specified in the [fund prospectus](/fund-prospectus/). Shared marks are simpler but create cross-subsidization dynamics: if Class A (the "premium" class) has recent inflows while Class B is underwater, Class A shares' recovery may unlock fees that benefit all shareholders equally, irrespective of their historical performance.

## Interaction with hurdle rates and clawback mechanics

Some funds combine a high-water mark with a [hurdle rate](/hurdle-rate-private-fund/)—a minimum return the fund must achieve before the manager earns any [carried interest](/carried-interest/) (in private funds) or performance fees. The hurdle rate and high-water mark operate on different timelines and logics.

- **High-water mark**: Prevents fees on gains that merely recover prior losses (multi-year or perpetual baseline).
- **Hurdle rate**: Sets a minimum annual or measurement-period return (often a benchmark plus a spread) before the manager's fee kicks in for that period.

A fund might require the NAV to exceed the high-water mark *and* the portfolio to achieve a 8% annual hurdle rate before performance fees are triggered. Both must be satisfied.

In [private equity](/private-equity-fund/) and [hedge funds](/hedge-fund/), high-water marks are often paired with clawback provisions: if the manager's total compensation over the fund's life exceeds a certain threshold relative to the fund's actual gains, the manager must return the excess. The high-water mark reduces the need for clawbacks but doesn't eliminate it.

## See also

<div class="wiki-seealso">

### Closely related

- [Hurdle Rate in Private Funds](/hurdle-rate-private-fund/) — The minimum return threshold before performance fees or carried interest applies
- [Soft Close vs Hard Close in a Fund](/soft-close-vs-hard-close-fund/) — Capacity management tools that interact with fund economics
- [Fund Redemption Queue Mechanics](/fund-redemption-queue-mechanics/) — How redemptions process while the high-water mark persists
- [Performance Fee](/performance-fee/) — The incentive fee structure the high-water mark constrains
- [Net Asset Value](/net-asset-value/) — The metric on which the high-water mark is based

### Wider context

- [Hedge Fund](/hedge-fund/) — Structures that commonly employ high-water marks to align manager and investor incentives
- [Private Equity Fund](/private-equity-fund/) — Another vehicle type where high-water marks and clawback mechanics are standard
- [Management Fee](/management-fee/) — The baseline fee that applies regardless of high-water mark status
- [Fund Prospectus](/fund-prospectus/) — The disclosure document that details fee mechanics and high-water mark terms

</div>
