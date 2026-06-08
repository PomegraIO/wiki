---
title: "How to Calculate IRR in an LBO"
description: "Step-by-step calculation of internal rate of return (IRR) in leveraged buyouts: entry equity, exit proceeds, holding period, and return drivers."
keywords:
  - irr calculation lbo
  - how to calculate irr
  - internal rate of return leveraged buyout
  - lbo returns
  - equity return calculation
image: /svg/corporate.svg
---

*The **internal rate of return** (IRR) in a leveraged buyout measures the annualized percentage return on the sponsor's equity investment, accounting for the timing and size of all cash flows from entry to exit. It is calculated by finding the discount rate that makes the present value of all outflows equal to the present value of all inflows.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">LBO IRR — Core Return Metric</div>

<img src="/svg/corporate.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">IRR is the annualized return on equity capital; IRR = discount rate where PV of equity outflows equals PV of equity inflows.</div>

|   |   |
|---|---|
| **Entry equity invested** | Purchase price minus debt financing at close |
| **Cash outflows** | Initial equity check; any follow-on capital injections |
| **Cash inflows** | Distributions from operations; exit proceeds from sale or refinance |
| **Exit value** | Enterprise value at sale (or refinanced value) minus remaining debt |
| **Hold period** | Years from close to exit or refinance; typically 5–7 years |
| **Target IRR** | Sponsor aspiration; 20–30% for mature LBOs; higher for distressed/turnaround |

</aside>

## The IRR Formula and Logic

The **internal rate of return** is the discount rate that solves this equation:

```
0 = −Equity₀ + Cash Flow₁/(1+IRR) + Cash Flow₂/(1+IRR)² + ... + Exit Equity/(1+IRR)ⁿ
```

In words:
- The initial equity check (negative, an outflow) plus
- All distributions and interim equity injections (positive inflows or negative outflows)
- Plus the exit equity value (positive inflow)
- All discounted at IRR
- Must sum to zero.

Solving for IRR yields the annualized return. Unlike a simple percentage gain (exit value ÷ entry value), IRR accounts for the timing of cash flows and the duration of the hold.

## Building an LBO IRR Model: Step by Step

### 1. Entry Equity

Start with the **purchase price** and the **leverage ratio** at close (typically 4–6x EBITDA for mature companies).

| Metric | Value |
|--------|-------|
| Enterprise Value (Purchase Price) | $500M |
| Target Leverage | 5.0x |
| EBITDA | $100M |
| Total Debt | $500M |
| Equity = EV − Debt | $0M |

Wait — this example shows zero equity, which illustrates the point: in a pure-debt buyout, the sponsor contributes minimal equity. But deals usually include $50–150M from the sponsor and coinvestors. Let's revise:

| Metric | Value |
|--------|-------|
| Enterprise Value | $500M |
| Bank Debt (Term Loan B) | $350M |
| Subordinated Debt (Mezz/PIK toggle) | $50M |
| Sponsor Equity Contribution | $100M |
| Other equity (management rollover, co-invest) | $0M |
| **Entry equity to sponsor** | **$100M** |

The sponsor is writing a $100M equity check at close. This is the starting cash outflow for the IRR model.

### 2. Annual Cash Flows During the Hold

Each year, the company generates free cash flow (after tax, capex, and working capital). Most or all of this cash is used to pay down debt and/or fund distributions.

Assume the portfolio company generates $20M in free cash flow per year, and the sponsor uses it to pay down debt (rather than take distributions). This is a **debt paydown** of $20M annually.

| Year | FCF | Debt Paydown | Distributions to Sponsor | Equity Injection |
|------|-----|-------------|-------------------------|------------------|
| 1 | $20M | $20M | — | — |
| 2 | $25M | $25M | — | — |
| 3 | $30M | $30M | — | — |
| 4 | $32M | $32M | — | — |
| 5 | $35M | $35M | — | — |

In this scenario, there are no interim distributions, only debt paydown. The sponsor's equity investment is not generating cash until exit.

However, in some LBOs the sponsor takes modest distributions (e.g., 2–3% dividend) once debt reaches a lower threshold. And the sponsor may inject additional equity if the company hits a [covenant breach](/portco-covenant-breach-lbo/) and needs a cure.

### 3. Exit Proceeds and Equity Value

At year 5 (or whenever the sponsor exits), assume the company is sold for an enterprise value of **$750M**.

| Metric | Value |
|--------|-------|
| Exit Enterprise Value | $750M |
| Less: Remaining Debt | $280M |
| **Exit Equity Value** | **$470M** |

The sponsor's equity stake was originally $100M, and the exit generates $470M. But the IRR depends on the timing.

### 4. Putting It Together: The IRR Calculation

The cash flow timeline is:

| Period | Cash Flow | Description |
|--------|-----------|-------------|
| Year 0 (Close) | −$100M | Sponsor equity check |
| Year 1–5 | $0 | No interim distributions in this model |
| Year 5 (Exit) | +$470M | Exit equity proceeds |

**IRR formula:**

```
0 = −100 + 0/(1+IRR) + ... + 0/(1+IRR)⁴ + 470/(1+IRR)⁵
```

Solving: `100 = 470 / (1+IRR)⁵`

`(1+IRR)⁵ = 4.7`

`1+IRR = 4.7^(1/5) = 1.378`

`IRR = 37.8%`

This is a **gross IRR** (before sponsor management fees and carried interest splits). A 37.8% return over 5 years is strong.

## Adjusting for Interim Distributions and Equity Injections

In real LBOs, the cash flow picture is more complex:

**Interim distributions.** After year 3, assume the company reaches a lower leverage level (3.0x) and the sponsor takes a dividend of $15M.

**Equity injection for covenant cure.** In year 3, the company misses a covenant, and the sponsor injects $10M equity to cure.

| Period | Cash Flow | Description |
|--------|-----------|-------------|
| Year 0 | −$100M | Initial equity |
| Year 2 (middle) | +$5M | Small dividend |
| Year 3 (middle) | −$10M | Equity cure injection |
| Year 3 (late) | +$15M | Dividend post-cure |
| Year 5 | +$470M | Exit equity |

Solving the IRR equation with these flows yields a lower IRR than 37.8%, because some equity went in at year 3 at a lower valuation (the covenant breach depressed the company), and interim distributions reduce the equity base growing to exit.

## Gross vs. Net IRR

- **Gross IRR:** Return on equity before sponsor fees (management fees, monitoring fees) and before carried interest claws or holdbacks.
- **Net IRR:** Return to a typical LP after sponsor fees and carry splits. Net IRR is usually 2–5 percentage points below gross IRR.

A deal promising a 25% gross IRR might deliver 18–22% net to LPs, depending on fee tiers.

## Benchmarking and Target Returns

Sponsors target different IRR ranges depending on deal profile:

| Profile | Target IRR |
|---------|-----------|
| Mature, stable buyout (Fortune 500 carve-out) | 18–22% |
| Mid-market buyout (leveraged recapitalization) | 22–28% |
| Distressed or turnaround | 30–50% |
| Growth equity (lower leverage) | 15–20% |

Target IRRs of 20–30% are standard for institutional sponsors. Lower leverage or more stable cash flows mean lower targets. Higher leverage or turnaround risk mean higher targets.

## Common IRR Pitfalls

**Unrealistic exit multiple.** If the model assumes an exit at 12x EBITDA but the market exits at 9x, IRR will disappoint.

**Leverage reduction underestimated.** If debt paydown is slower than modeled, equity growth is slower, reducing IRR.

**Interim cash leakage.** Sponsor fees, advisor costs, and management bonuses reduce free cash flow available for debt paydown, lowering IRR.

**Timing mismatch.** An equity cure or recapitalization in year 3 introduces a large outflow at a lower valuation, dragging down the overall return.

## The Equity Bridge as IRR Proof

Some sponsors compute an **equity bridge** to decompose where IRR came from: debt paydown, EBITDA growth, and multiple expansion. This shows whether the IRR relied on optimistic operational improvement or more conservative assumptions. Bridges with returns driven by debt paydown are more defensible than those betting entirely on multiple expansion.

## See also

<div class="wiki-seealso">

### Closely related

- [Leveraged Buyout (LBO)](/leveraged-buyout/) — Core concept; IRR is the primary return metric.
- [LBO Equity Bridge: Tracking Value Creation from Entry to Exit](/lbo-equity-bridge/) — Decomposition of IRR into EBITDA growth, multiple expansion, and debt paydown.
- [Covenant Breach at an LBO Portfolio Company](/portco-covenant-breach-lbo/) — Unplanned equity injections reduce realized IRR.
- [Private Equity Fund](/private-equity-fund/) — IRR benchmarks and LP return expectations.
- [Carried Interest](/carried-interest/) — Sponsor share of the gross IRR, typically 20%.

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — NPV method; IRR is a special case.
- [Cost of Debt](/cost-of-debt/) — Lower cost of debt raises IRR by reducing interest burden.
- [Return on Equity](/return-on-equity/) — Company-level metric; IRR is equity-sponsor return.
- Time Value of Money — Principle underlying IRR discount rates.

</div>
