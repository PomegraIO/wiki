---
title: "Risk-Adjusted Return on Capital"
description: "A bank or business unit's profit scaled by the economic capital required to absorb potential losses."
keywords:
  - risk-adjusted return
  - economic capital
  - profitability
  - banking metrics
  - capital allocation
  - risk management
image: "/svg/risk.svg"
---

*Risk-adjusted return on capital (RAROC) divides a business line's profit by the economic capital allocated to it—the cushion of loss-absorbing funds required to meet a target [default probability](/default-rate/). It answers the question: how much profit does this unit earn per dollar of risk it carries? Banks use RAROC to decide whether a loan, trading desk, or product line generates enough return to justify the capital it ties up.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk-Adjusted Return on Capital — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk measurement." />

<div class="wiki-infobox-caption">Capital is cheap when return exceeds the cost of equity and reserves.</div>

|   |   |
|---|---|
| **What it is** | Net income divided by economic capital; measures return per unit of risk absorbed |
| **Also called** | RAROC, economic return on capital, risk-weighted return |
| **Formula** | (Expected profit) ÷ (Economic capital required) |
| **Interpretation** | Expressed as a percentage; compared against [cost of equity](/cost-of-equity/) or hurdle rate |
| **Used by** | Commercial banks, investment banks, insurance companies, large asset managers |
| **Competitor metrics** | [Return on equity](/return-on-equity/), [Return on invested capital](/return-on-invested-capital/), [Return on assets](/return-on-assets/) |

</aside>

## The gap between accounting and economic capital

Traditional [return on equity](/return-on-equity/) (net income divided by shareholder equity on the balance sheet) tells an incomplete story in banking. A commercial bank might hold $100 million of equity and earn $10 million, yielding a 10% ROE. But if a particular loan—say, a $10 million credit to a stressed borrower—could wipe out 50% of the bank's equity in a stress scenario, the true capital required to absorb that loan's risk is much larger than its nominal size on the balance sheet.

Economic capital is a forward-looking estimate of the loss buffer a bank needs to stay solvent if losses hit the projected worst case (typically defined as a 1-in-1,000-year event or a target probability of default). A retail mortgage portfolio and a leveraged buyout portfolio, each producing identical accounting profits, might require vastly different economic capital because of their risk profiles.

## How RAROC guides capital allocation

A bank's capital is finite. Management must decide whether to deploy it in mortgages (lower risk, modest margins), investment-grade [corporate bonds](/corporate-bond/) (moderate risk, moderate margins), or [leveraged buyouts](/leveraged-buyout/) (high risk, high expected returns). RAROC creates a common scorecard.

Suppose the bank's [cost of equity](/cost-of-equity/) is 10%. A mortgage desk earning 2% return on $50 million of economic capital yields RAROC of 2%—well below the hurdle rate, so that desk destroys value. A leveraged buyout desk earning 8% on $10 million of economic capital yields RAROC of 80%—well above the hurdle rate, so it should expand. All other things equal, the bank should shift capital from mortgages to leveraged deals, until marginal RAROC across units aligns with the cost of capital.

In practice, banks rarely reach perfect equilibrium because of regulatory [capital requirements](/capital-adequacy/), customer relationships, and competitive dynamics. But the RAROC framework at least forces transparent trade-offs.

## Calculating economic capital: the mechanics

Economic capital is typically computed using [value at risk](/value-at-risk/) or expected shortfall models. A bank specifies a confidence level (e.g., 99.9%) and a time horizon (e.g., one year), then asks: what loss level would we exceed with only 0.1% probability?

For a $10 million loan with a 5% probability of default, 60% loss-given-default, and assuming default events are mostly independent, the expected loss is $10M × 5% × 60% = $300,000. But there is volatility around that expectation; in a bad year, losses could spike to $2 million. The economic capital is roughly the difference between the worst-case loss (at the chosen percentile) and the expected loss, sometimes plus a buffer. The exact formula varies by institution and regulatory regime.

Credit derivatives and [securitization](/securitization/) markets have made economic capital more explicit: the capital tranche of a [mortgage-backed security](/mortgage-backed-security/) is the first to absorb losses, and its market price reveals what capital costs in that context.

## Adjusting profit for risk: the numerator

The numerator of RAROC is typically "risk-adjusted" profit, not raw accounting profit. For a loan, this might be:

> Loan interest income — expected loss — cost of funds — operating expenses = risk-adjusted profit

The expected loss is subtracted *even if no default has occurred yet*, because it is an implicit cost of bearing credit risk. A loan generating $100,000 in interest but carrying a $30,000 expected loss has risk-adjusted profit of only $70,000—much lower than accounting income.

For a trading desk, risk adjustment might account for [stressed loss estimates](/stress-testing/) or [value at risk](/value-at-risk/) limits breached during extreme moves.

## RAROC vs. Dodd-Frank stress testing

US banks subject to [Dodd-Frank Act](/dodd-frank-act/) supervision now run annual stress tests that forecast capital consumption under severe recession scenarios. These tests implicitly produce RAROC-like calculations at the portfolio level: the regulator asks whether the bank can absorb a hypothetical wave of defaults and market losses while maintaining minimum [capital adequacy](/capital-adequacy/) ratios.

The post-2008 regulatory framework has made RAROC more constraining. A business line that generates 12% RAROC might still be shut down if the stress test shows it would deplete capital too quickly in a crisis. Conversely, a low-RAROC but stable business (like deposit-taking) is often tolerated because it anchors the balance sheet.

## The assumption trap

RAROC is as good as the economic capital model underlying it. If the model assumes defaults are independent but they are actually correlated (as they are in recessions), the calculated capital is too low, and RAROC is overstated. A portfolio of loans to real estate developers looked profitable with high RAROC in 2006; the 2008 crisis revealed that the true economic capital was much larger.

Many banks now use Monte Carlo simulation and [scenario analysis](/sensitivity-analysis-valuation/) to stress-test RAROC assumptions. A business line must show not only high RAROC under the base-case economic capital estimate but also acceptable RAROC under plausible alternative capital models.

## See also

<div class="wiki-seealso">

### Closely related

- Economic capital — the loss-absorbing buffer allocated to a business line or [counterparty](/counterparty-risk/)
- [Cost of equity](/cost-of-equity/) — the hurdle rate against which RAROC is benchmarked
- [Return on equity](/return-on-equity/) — the accounting metric that RAROC refines by incorporating forward-looking risk
- [Value-at-risk](/value-at-risk/) — a statistical method for estimating worst-case losses that feed into economic capital
- [Default rate](/default-rate/) — the probability input to economic capital calculations

### Wider context

- [Capital adequacy](/capital-adequacy/) — regulatory minimum capital that complements economic capital
- [Stress testing](/stress-testing/) — forward-looking loss estimates that validate RAROC assumptions
- [Counterparty risk](/counterparty-risk/) — one of the largest capital consumers in investment banking
- [Securitization](/securitization/) — a mechanism that makes economic capital visible through market pricing

</div>
