---
title: "Longevity Swap"
description: "A contract in which a pension fund swaps its mortality risk by exchanging fixed for actual survivor-linked benefit payments, isolating longevity exposure."
keywords:
  - longevity swap
  - mortality derivatives
  - longevity risk transfer
  - pension risk swap
  - survivor-linked swap
image: "/svg/derivatives.svg"
---

*A **longevity swap** transfers pension plan mortality and longevity risk from a sponsoring company or pension fund to a counterparty (typically a reinsurer or specialized investment firm). The fund agrees to pay a fixed annuity stream—calculated on traditional [actuarial-tables](/investment-grade-bond/) assumptions—while the counterparty pays the actual benefits owed as plan members live longer or die earlier than expected. The swap isolates demographic risk from investment risk, letting pension funds hedge the uncertainty of how long beneficiaries will live.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Longevity Swap — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract mark representing derivatives and structured contracts." />

<div class="wiki-infobox-caption">A pension risk derivative isolating longevity exposure from market and credit risk.</div>

|   |   |
|---|---|
| **What it is** | Transfer of mortality/longevity risk from pension fund to counterparty |
| **Also called** | Mortality swap, survivor-linked swap, pension risk swap |
| **Leg 1 (fixed)** | Annuity stream on standardized mortality assumptions |
| **Leg 2 (floating)** | Actual benefit payments based on realized survivor rates |
| **Primary users** | Large defined-benefit pension funds, pension de-risking groups |
| **Key risk** | Basis risk: realized mortality may differ from model |

</aside>

## The problem longevity swaps solve

Pension funds face a silent but enormous risk: they must pay benefits to members who live longer than expected. In 1950, life expectancy for a 65-year-old was roughly 80 years; today it is often 85 or beyond, and improving. A fund that set aside assets in 1990 for members expected to live to 80 now discovers members are living to 85 or 87. The shortfall is the fund's to bear.

This risk is not diversifiable. Unlike market risk—where buying stocks or bonds lets you trade up or down—mortality risk is [idiosyncratic-risk](/idiosyncratic-risk/). A pension fund cannot hedge it by holding different stocks or [bonds](/bond/). Longevity swaps exist precisely because longevity risk is real, material (often amounting to millions of dollars for large funds), and difficult to shed without a specialized counterparty.

A longevity swap lets a pension fund convert an unknown longevity liability into a known, hedged one. Instead of guessing how many of its members will be alive in 20 years, the fund pays a fixed stream and lets the swap counterparty bear the guess. If members live longer, the counterparty pays the extra; if they die earlier, the fund keeps the savings.

## How payments work

The swap has two legs, exchanged on a regular schedule (usually quarterly or annually):

**Leg 1 (pension fund pays):** A fixed annuity amount per plan member (or per surviving member at each payment date), calculated using a baseline mortality table—often a standard cohort such as "UK males born 1960" or "US females born 1955."

**Leg 2 (counterparty pays):** The actual pension benefit payments owed to surviving plan members, plus lump-sum payments to estates of deceased members (if applicable).

At each payment date, the counterparty observes how many plan members have died since inception. If fewer have died than the mortality table predicted, the counterparty owes the fund the extra benefit. If more have died, the fund owes the counterparty. The net settlement is often netted and paid by the party owing the larger amount.

Example: A pension fund has 10,000 retirees. The baseline mortality assumption (from a standard table) predicts 100 deaths per year. Leg 1 is set at a fixed annual payment of 100 × (average benefit per deceased member) = $500,000. If only 90 die in year one, the counterparty owes the fund 10 × (average benefit) = $50,000. If 110 die, the fund owes the counterparty $50,000.

## Pricing and basis risk

Longevity swaps are priced using [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) of the expected payment streams under both the pension fund's mortality assumptions and the counterparty's (typically slightly more conservative). The spread is the longevity swap's "price"—the margin the counterparty demands for bearing the risk.

The key pricing input is the **basis risk** between the mortality table used in the swap and the actual mortality of the pension fund's members. A table might assume 10% annual mortality for males aged 75; the pension fund's specific male members aged 75 might have 8% actual mortality (because they are higher-income, healthier, or from a region with lower mortality). This mismatch is basis risk. The counterparty prices it in; the wider the expected basis, the wider the swap spread.

[Duration](/duration/) is the primary sensitivity metric. A longevity swap's duration is tied to the average remaining life expectancy of the plan members. A fund with members age 65 has much longer duration (and thus more risk) than a fund with members age 85. A 10-year bond duration is typical; some pension funds have swaps with 20+ year effective duration.

[Convexity](/interest-rate-risk/) also matters. If mortality improvements are non-linear (accelerating or decelerating), the cash flows become unpredictable, raising the counterparty's pricing.

## Who provides longevity swaps

**Reinsurance companies** are the largest counterparties. Munich Re, Swiss Re, and other mega-reinsurers hold vast databases of mortality experience across many populations and can absorb longevity risk more cheaply than a single pension fund can hedge it. They lay off residual risk via [securitization](/securitization/) or reinsurance treaties.

**Specialized mortality fund managers** and pension de-risking platforms (like Pension Insurance Group, PIC) have grown to absorb longevity risk. These firms raise capital from institutional investors (pension funds, endowments, insurers) and enter multiple swaps to diversify mortality exposure.

**Investment banks** (Goldman Sachs, JP Morgan, Morgan Stanley) sometimes intermediate longevity swaps, though direct capital deployment is less common than arranging the transaction.

**Mortality-linked bond issuers** use securitization to raise capital against longevity risk, creating marketable securities backed by pension liabilities.

## Hedging effectiveness and real-world challenges

A well-designed longevity swap can reduce a pension fund's balance-sheet volatility by half or more. For accounting purposes, it is a perfect hedge: the fund's liability is fixed, and the swap's value moves inversely with changes in actuarial assumptions.

But longevity swaps are not frictionless. Several challenges arise:

**Basis risk:** As mentioned, the mortality table's assumptions may not match the fund's actual members. A table assumes a population-average mortality; the fund's members might be wealthier, healthier, or concentrated in urban areas with better longevity. If realized mortality diverges from the table by 10%, the hedge fails to offset the fund's actual loss.

**Causality and feedback:** If a pension fund cuts benefits or stops enrolling new members, the remaining cohort becomes older and unhealthier (negative selection). Realized mortality can worsen unexpectedly, defeating the swap's hedge precisely when the fund is most stressed.

**Counterparty credit:** A longevity swap is a long-term bilateral agreement. If the counterparty fails (as some reinsurers have), the pension fund loses its hedge and is back to bearing full mortality risk. [Counterparty-risk](/counterparty-risk/) is real and typically mitigated via collateral, credit triggers, or diversification across multiple counterparties.

**Accounting and regulatory:** Longevity swaps must satisfy [generally-accepted-accounting-principles](/generally-accepted-accounting-principles/) hedge accounting rules to be treated as an offset to the liability. Documenting the hedge relationship, testing effectiveness, and reporting mark-to-market can be expensive and complex. Some jurisdictions have carve-outs or special rules for pension de-risking, but this is still in flux.

**Illiquidity:** Longevity swaps are bespoke. If a pension fund needs to unwind a swap early, there may be no liquid secondary market. The counterparty will quote an exit price that reflects mark-to-market losses, which can be steep if mortality assumptions have shifted.

## Size and market evolution

Longevity swaps are a relatively young market—the first trades occurred in the early 2000s. As of the 2020s, over $500 billion notional of longevity risk has been transferred via swaps and securitization globally, mostly among UK, European, and US pension funds. The market is growing as defined-benefit pensions struggle with funding ratios and plan sponsors seek to de-risk.

The typical hedge covers only a portion of the fund's longevity exposure (a "partial hedge"), reducing cost. A full hedge would be expensive and might not be cost-justified if the fund expects strong returns or improved funding over time.

## Variants and related structures

**Survivor indices:** Instead of bilateral swaps, some funds buy standardized survivor-linked bonds or indexes. The iBoxx Longevity index, for example, tracks a standardized population; funds can hedge against divergence from the index at lower cost than bespoke swaps.

**Mortality-linked securities (MLS):** Bonds backed by pools of mortality risk, often issued by reinsurers or de-risking platforms. These are publicly traded and allow distributed investment in longevity risk.

**Pension buy-ins and buyouts:** Rather than a swap, some funds purchase an insurance company annuity for a subset of their liabilities, transferring both mortality risk and payment obligation. This is more costly than a swap but eliminates counterparty risk (the insurer is typically AA-rated).

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-Rate Swap](/interest-rate-swap/) — the swap mechanism longevity swaps are built on
- [Securitization](/securitization/) — the capital markets technique for distributing longevity risk
- [Duration](/duration/) — key metric for longevity swap sensitivity
- Risk Transfer — the core purpose of longevity swaps
- [Counterparty Risk](/counterparty-risk/) — a primary concern in long-dated swaps
- [Range-Accrual-Swap](/range-accrual-swap/) — another specialized derivative variant

### Wider context

- [Fair Value](/fair-value/) — accounting standard for pension liabilities and hedges
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — methodology for pricing longevity swaps
- [Credit Rating](/credit-rating/) — important for evaluating counterparty safety
- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — framework for hedge accounting
- Defined-Benefit Pension Plans — the primary user of longevity swaps
- Actuarial Risk — the demographic basis of longevity derivatives

</div>
