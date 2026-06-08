---
title: "Soft Hurdle vs Hard Hurdle in Hedge Fund Fee Structures"
description: "Understand how soft and hard hurdles determine when hedge fund managers earn performance fees and how each aligns incentives differently."
keywords:
  - hedge fund soft hurdle vs hard hurdle
  - soft hurdle rate
  - hard hurdle rate
  - hedge fund fee structure
  - performance-based compensation
image: /svg/funds.svg
---

*A **soft hurdle** (or "soft gate") charges a [performance fee](/performance-fee/) on all gains once the fund exceeds a return threshold, while a **hard hurdle** charges the fee only on gains above the threshold itself. The difference determines how harshly managers are penalized for underperformance and how generously they are rewarded for beating the [benchmark](/index-provider/).*

<div class="wiki-hatnote">

This article focuses on the mechanics of the two hurdle structures. For the broader context of hedge fund compensation and [carried interest](/carried-interest-compensation/), see [hedge fund](/hedge-fund/) and fee structures overview.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Soft vs Hard Hurdle — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for funds." />

<div class="wiki-infobox-caption">Two ways to gate when a manager collects performance fees, with different payout implications.</div>

|   |   |
|---|---|
| **Soft hurdle** | Fee kicks in once fund return exceeds hurdle; fee applies to *all* gains from zero |
| **Hard hurdle** | Fee applies *only* to gains above the hurdle threshold |
| **Manager incentive** | Soft: aggressive (fee on all gains above hurdle); Hard: measured (no fee on below-hurdle gain) |
| **Investor cost** | Hard: cheaper if underperforming; Soft: more expensive if beating hurdle by small margin |
| **Typical hurdle rate** | 5–8% annualized; often tied to a benchmark like the [S&P 500](/sp-500-index/) or a fixed rate |
| **High-water mark** | Often paired with hurdles to prevent "double-dipping" after a loss year |
| **Disclosure** | Must be stated clearly in the fund [prospectus](/fund-prospectus/) |

</aside>

## A concrete example: soft hurdle

Suppose a hedge fund is structured as:
- **Management fee:** 2% of assets under management
- **Performance fee:** 20% of gains
- **Hurdle rate (soft):** 5% annually

The fund starts with $100 million in investor capital and generates a 12% return in year one.

- **Gains before fees:** $100M × 12% = $12M
- **Benchmark gain (hurdle):** $100M × 5% = $5M ✓ Hurdle exceeded by $7M
- **Taxable base for performance fee:** $12M (all gains, since hurdle is cleared)
- **Performance fee to manager:** 20% × $12M = $2.4M
- **Investor receives:** $100M × 12% − $2M mgmt fee − $2.4M perf fee = $107.6M (a 7.6% net return)

The manager collected a fee on the full $12M in gains, even though only $7M of it was "above the hurdle." The soft hurdle simply requires the fund to clear 5% before any performance fee is triggered; once it is, the fee applies to all gains.

## The same scenario: hard hurdle

Same fund, same 12% return, but a **hard hurdle** structure:

- **Gains before fees:** $12M
- **Gains *below* hurdle:** $5M (the hurdle amount)
- **Gains *above* hurdle:** $12M − $5M = $7M ✓ Only this portion is taxable for performance fee
- **Performance fee to manager:** 20% × $7M = $1.4M
- **Investor receives:** $100M × 12% − $2M mgmt fee − $1.4M perf fee = $108.6M (an 8.6% net return)

The manager earned $1M less in performance fees under the hard hurdle — a significant difference. The investor kept the extra dollar. In strong years, the hard hurdle is cheaper; in weak years, they're equivalent (no performance fee in either case if the hurdle is not met).

## Why the difference matters: a down year

Now suppose the fund returns −2% in year two.

**Soft hurdle:**
- Return: −2%
- Hurdle: +5%
- Has the hurdle been cleared? No.
- Performance fee: $0
- Investor net: −2% (the management fee is still paid)

**Hard hurdle:**
- Return: −2%
- Hurdle: +5%
- Has the hurdle been cleared? No.
- Performance fee: $0
- Investor net: −2%

In years where the fund underperforms, soft and hard hurdles are identical — no performance fee is charged in either case. The difference emerges only in **positive years above the hurdle**.

## When each hurdle aligns incentives

**Soft hurdles** are more common and incentivize **aggressive management**. Once the 5% hurdle is cleared (say, the fund hits 5.5%), the manager earns 20% performance fees on every dollar of additional gain — including that extra 0.5% cushion beyond the hurdle. Managers are motivated to shoot for big gains and run levered or concentrated positions. The fee structure rewards them generously for any outperformance.

**Hard hurdles** impose a **stricter incentive alignment**. The manager earns nothing until gains exceed the hurdle, and only on the excess. If the hurdle is 5% and the fund returns 6%, the manager gets 20% of only 1% — a measly performance fee. This structure discourages reckless risk-taking to chase a marginal hurdle clearance. Managers tend to be more disciplined and focus on **substantial** outperformance.

Sophisticated endowments and pension funds often negotiate hard hurdles to reduce fees in borderline years. Newer or less established funds may accept soft hurdles to attract capital by appearing to offer more generous returns.

## The high-water mark: a safeguard

Most hurdle clauses are paired with a **[high-water mark](/high-water-mark/)** — a running tally of the fund's peak value. After a down year, the fund must recover back to the previous high before any performance fees are charged again. This prevents managers from collecting performance fees on recovery gains after a loss.

Example:
- Year 1: Fund grows to $110M (starts at $100M). Manager collects performance fee.
- Year 2: Fund drops to $90M. No performance fee.
- Year 3: Fund recovers to $105M. **Has the high-water mark been exceeded?** No — the high-water mark is still $110M. So no performance fee is charged, even though the fund rose $15M. The manager must get the fund back above $110M to earn a performance fee on the new gains.

The high-water mark and the hurdle rate are independent. A fund can have a 5% soft hurdle *and* a high-water mark — the fund must both clear the hurdle *and* exceed the previous peak to trigger performance fees.

## Negotiating hurdle terms

In **large institutional relationships**, hurdle terms are customizable. Common negotiations include:

- **Hurdle tied to a benchmark:** Instead of a fixed 5%, the hurdle is S&P 500 return + 1% or LIBOR + 200 bps. This makes outperformance relative, not absolute.
- **Tiered performance fees:** 15% on gains up to 10% return; 20% on gains above 10%. Rewards outsized performance more.
- **Conditional hard hurdle:** Soft hurdle in year one (to attract capital); hard hurdle in years two and beyond.
- **Rebate clause:** If the hard hurdle is missed in year one, the manager rebates some management fees to offset the underperformance.

## Soft hurdle vs hard hurdle: investor perspective

From a dollar-and-cents view, hard hurdles are **always cheaper or equal** to soft hurdles on the same fund performance. Investors should prefer hard hurdles when they have negotiating power. However, hard hurdles might attract more conservative managers, which could mean lower returns but lower volatility. Soft hurdles attract return-hungry managers — higher upside, higher downside, and higher fees when they win.

The trade-off is implicit in manager selection and [alpha](/alpha/) generation philosophy, not just fee mechanics.

## See also

<div class="wiki-seealso">

### Closely related

- [Hedge Fund](/hedge-fund/) — the broader fund structure and compensation model
- [Performance Fee](/performance-fee/) — how managers are paid based on returns
- [Carried Interest Compensation](/carried-interest-compensation/) — the economic incentive structure for fund managers
- [High-Water Mark](/high-water-mark/) — the safeguard that prevents double-dipping after losses
- [Fee Structure and Expense Ratio](/expense-ratio/) — management fees and their impact on net returns
- [Alpha](/alpha/) — the outperformance a hedge fund claims to deliver to justify hurdles and fees

### Wider context

- [Mutual Fund](/mutual-fund/) — traditionally uses simpler fee structures without hurdles
- [Private Equity Fund](/private-equity-fund/) — related compensation model with carried interest
- Incentive Alignment — the broader principle of aligning manager and investor interests
- [Benchmark](/index-provider/) — the standard against which hurdles and outperformance are measured

</div>
