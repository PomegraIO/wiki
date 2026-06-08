---
title: "How to Calculate the Hurdle Rate in a PE Fund"
description: "Calculate hurdle rate in a PE fund using preferred return and waterfall structure. American vs European waterfalls create different accrual mechanics."
keywords:
  - hurdle rate private equity calculation
  - pe hurdle rate example
  - preferred return calculation
  - private equity waterfall
  - american vs european waterfall
---

*The **hurdle rate calculation** in a private equity fund works through the fund's distribution waterfall, which determines when and how much profits flow to the general partner (the fund manager) versus the limited partners (the investors). A typical hurdle rate — often 8%, 10%, or 12% annually — is the minimum annual return that must be achieved before the GP can earn a disproportionate share of profits. Understanding how to calculate whether a fund clears its hurdle requires tracing cash flows through either an American or European waterfall structure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Hurdle rate calculation — waterfall mechanics</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A hurdle rate is a performance threshold. Which capital bears it depends on the waterfall structure.</div>

|   |   |
|---|---|
| **Typical hurdle rate** | 8%, 10%, or 12% per annum; negotiated upfront in the partnership agreement |
| **American waterfall** | LPs receive capital + preferred return on contributed capital only; GP catches up before sharing carry |
| **European waterfall** | LPs receive capital + preferred return on committed capital (including uncalled); different accrual base |
| **Preferred return** | Annual return threshold (often equal to hurdle rate); accrues until cashed out or waterfall triggered |
| **General partner catch-up** | Clause allowing GP to take a disproportionate share until hurdle is satisfied, after which normal carry applies |
| **Carry split** | After hurdle is met, typical split is 70–80% to LPs, 20–30% to GP (the GP's "carry" or "promoted interest") |

</aside>

## The Purpose of a Hurdle Rate

A **hurdle rate** is the performance threshold that a private equity fund must meet before the general partner (the manager) earns its disproportionate profit share. In a typical fund deal, the GP contributes perhaps 1–3% of capital and receives 20–30% of profits above the hurdle. Below the hurdle, profits are paid preferentially to limited partners.

The hurdle rate compensates LPs for illiquidity, risk, and the time they lock up capital. A 10% hurdle means the fund must generate 10% annual returns on LP capital before the GP earns its carried interest (its share of excess profits). If the fund achieves 12% annual returns, the hurdle is cleared and the GP participates in the upside above that threshold. If it achieves only 8%, the GP earns no carry; LPs get all returns until the 10% threshold is satisfied.

## American Waterfall: Contributed Capital Base

In an American waterfall (also called a "traditional" or "GP-aligned" waterfall), the hurdle rate typically accrues on **contributed capital only** — the cash that LPs have actually handed over to the fund. Committed capital that has not yet been drawn does not count toward the hurdle.

**Worked example: American waterfall with 10% hurdle**

- Fund size: $1 billion commitment (committed capital)
- Year 1: GP calls $200 million from LPs (contributed capital); remaining $800 million not drawn
- Investment generates $10 million in distributions (a 5% return on the $200 million contributed)
- Preferred return calculation: 10% of $200 million = $20 million
- Since LPs received only $10 million in distributions, the preferred return is short by $10 million
- Distributions to LPs: $10 million (all of the distribution; no carry to GP yet)
- Preferred return "overhang" or accrued: $10 million (the shortfall from 10% on contributed capital)

In year 2, if the fund contributes another $250 million and generates $35 million in proceeds:
- Preferred return owed on contributed capital: 10% × ($200M from Y1 + $250M from Y2) = $45 million
- Cumulative preferred return so far: $55 million (the $20M from Y1 + $35M from Y2, less the $10M paid out)
- Actually, let's recalculate: LPs received $10M in Y1. In Y2, they are owed 10% on $450M = $45M. Cumulative distributions: $10M + $35M = $45M.
- Preferred return is now satisfied through Y2.
- GP catch-up: The GP can now take a catch-up allocation equal to the GP's normal carry percentage (say 20%) on all distributions since inception until the hurdle was satisfied, to compensate the GP for the below-hurdle distributions it did not participate in.
- After catch-up, future distributions split per the fund agreement (often 80% LP, 20% GP).

## European Waterfall: Committed Capital Base

In a European waterfall, the hurdle often accrues on **committed capital** — the total amount LPs have promised to the fund, whether drawn or not. This is a more LP-favorable structure because the hurdle is calculated on a larger base, making it easier for the fund to "clear" the hurdle and reach carry-splitting.

**Worked example: European waterfall with 10% hurdle**

- Fund size: $1 billion commitment
- Year 1: GP calls $200 million; remaining $800 million uncalled
- Preferred return calculation (European): 10% of $1 billion = $100 million annually
- Distributions in Year 1: $10 million
- Preferred return owed: $100 million
- Shortfall: $90 million accrues

In Year 2, the GP calls another $250 million (cumulative $450 million drawn) and generates $35 million in proceeds:
- Preferred return owed in Year 2 (on committed capital): 10% of $1 billion = $100 million
- Cumulative preferred return over 2 years: $200 million
- Cumulative distributions to LPs so far: $10M + $35M = $45 million
- Cumulative shortfall: $200M − $45M = $155 million

In Year 3, if the fund realizes a large exit and distributes $150 million:
- Preferred return owed in Year 3: 10% of $1 billion = $100 million
- Cumulative distributions to LPs: $45M + $150M = $195 million
- Cumulative preferred return owed: $300 million
- Hurdle is still not fully satisfied. The $150 million in Year 3 proceeds goes first to LPs until cumulative preferred return is paid.
- Remaining after preferred return: $195M paid − $300M owed = −$105 million (still short)
- LPs receive the full $150 million in Year 3.
- Preferred return overhang: $105 million

The European structure is more favorable to LPs because the committed capital base is larger, so the hurdle amount is large and takes longer to clear, delaying carry to the GP.

## Preferred Return, Distributions, and Accrual

The "preferred return" is the annual target return, equal to the hurdle rate. It is called "preferred" because LPs receive it before the GP participates in profits. A preferred return can be:

- **Cash-on-cash**: Paid from available distributions only, whenever the fund distributes cash
- **Accruing**: Compounds annually, even if no cash is distributed, creating a cumulative overhang that must be satisfied before carry kicks in

Most PE fund agreements use accruing preferred returns. This means if Year 1 produces no distributions, the 10% preferred return compounds and must be satisfied in future years before the GP earns anything above the hurdle.

The accrual mechanism can create a long carry waterfall. If a fund is illiquid and does not distribute for years, the preferred return overhang becomes very large. When the fund finally exits an investment and distributes $500 million, the first several hundred million may still go to preferred return before any GP carry is triggered.

## Catch-Up and Multiple Investments

A **catch-up** clause allows the GP to take a disproportionate share of distributions until the hurdle is met, to compensate for having received below-market returns during the accumulation phase. Without catch-up, the GP would be perpetually disadvantaged if the fund took years to clear the hurdle.

Example of catch-up:
- Normal split is 80% LP, 20% GP
- Fund clears hurdle; next $10 million in distributions is subject to catch-up
- GP's catch-up share: 20% / (1 − 0.20) = 25% on the catch-up (until caught up)
- LPs receive: $10M × 0.80 = $8 million
- GP catch-up: $10M × 0.25 = $2.5 million
- After catch-up is satisfied, the 80/20 split resumes

## Hurdle Rates Across Fund Strategies

Hurdle rates vary by fund stage and strategy. An early-stage venture fund might have a 0% hurdle (no preferred return; carry splits immediately) because the risk is very high and GP–LP interests are closely aligned. A leveraged buyout fund might have an 8% hurdle, reflecting lower risk. A distressed or turnaround fund might have a 12% hurdle, pricing in higher complexity.

Larger, more established GPs can sometimes negotiate lower hurdles (8% instead of 12%) because they have proven track records and LPs are willing to align earlier. Smaller or first-time GPs might need higher hurdles (12%+) to compensate LPs for execution risk.

## Tax and Timing Issues

The timing of when the hurdle is measured can affect outcomes. Some funds measure preferred return on a fiscal-year basis; others use a rolling anniversary from initial capital call. A fund might clear the hurdle in Year 3 but fall back below it in Year 4 if investments underperform, resetting the accrual.

Tax implications also matter. In the US, carry is typically taxed as short-term capital gains or as ordinary income to the GP, while LPs' preferred return is their share of capital gains (long-term) plus interest. The preferred return structure does not change the tax character of the returns, but it does determine timing of when the GP is taxed on its profit share.

## See also

<div class="wiki-seealso">

### Closely related

- [Private Equity Fund](/private-equity-fund/) — the fund vehicle structure and LP/GP roles
- [Carried Interest Compensation](/carried-interest-compensation/) — the GP's profit share above the hurdle
- [Return on Invested Capital](/return-on-invested-capital/) — how to measure fund returns in the real world
- [Leveraged Buyout](/leveraged-buyout/) — a major PE strategy with typical 8% hurdle rates
- [Dividend Payout Ratio](/dividend-payout-ratio/) — similar waterfall logic in dividend payments
- [Fair Value](/fair-value/) — how funds mark interim valuations of portfolio companies

### Wider context

- [Enterprise Value](/enterprise-value/) — the metric GPs use to value portfolio companies
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — how PE models project returns to clear hurdles
- [Deal Economics](/carried-interest-compensation/) — how GPs model returns on acquisition investments
- [Capital Gains Tax](/capital-gains-tax-investor/) — the tax treatment of carry distributions to the GP

</div>