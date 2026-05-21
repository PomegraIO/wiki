---
title: "Stress Testing"
description: "Stress testing is a risk assessment method that measures portfolio losses under severe but plausible market conditions, explicitly exploring tail scenarios and model breakdowns."
keywords:
  - stress testing
  - risk scenario
  - adverse scenario
  - portfolio loss
  - tail risk
image: "https://picsum.photos/seed/stress-testing/900/600"
---

*Stress testing is the practice of assessing portfolio losses under extreme market scenarios — scenarios that are severe and plausible but may not have occurred in recent history. Unlike [value-at-risk](/value-at-risk), which relies on historical distributions, stress testing explicitly imagines catastrophic but foreseeable conditions and calculates the damage.*

<div class="wiki-hatnote">

This entry covers stress testing methodology. For structured, named scenarios, see [scenario-analysis](/scenario-analysis); for measurement of typical losses, see [value-at-risk](/value-at-risk).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stress Testing — key facts</div>

<img src="https://picsum.photos/seed/stress-testing/900/600" alt="A stress gauge showing the needle pushed to the red zone" />

<div class="wiki-infobox-caption">Stress testing asks: how bad could it get?</div>

|   |   |
|---|---|
| **What it is** | Assessment of losses under extreme but plausible scenarios |
| **Time period** | Usually short-term (1-10 days) for market stress |
| **Scenarios** | Historical crises, constructed extremes, or hypothetical shocks |
| **Purpose** | Find exposures to tail risks; test limits of [value-at-risk](/value-at-risk) models |
| **Regulatory requirement** | Mandatory for banks; increasingly required for hedge funds, asset managers |
| **Advantage** | Captures risks models miss; no distributional assumptions |
| **Limitation** | Scenarios are subjective; no clear probability attached |

</aside>

## How stress testing works

**Step 1: Define stress scenarios.**
Choose severe but plausible conditions. Examples:
- Stock market falls 30% in one month.
- Bond yields rise 2% in one week.
- Credit spreads widen 500 basis points.
- A major geopolitical crisis erupts.
- A key central bank cuts rates unexpectedly.

**Step 2: Shock the portfolio.**
Apply the scenario to the portfolio. Calculate new prices for all holdings and the portfolio's new value.

**Step 3: Measure the loss.**
Loss = Original value - Value under stress scenario.

**Step 4: Assess damage.**
Compare to risk limits, capital available, and acceptable loss tolerance.

## Historical stress tests

Real market crises serve as templates for stress scenarios:

- **October 1987 ("Black Monday").** Stock markets fell 22% in a single day. Stress scenario: "What if that happened again?"
- **1998 Russian crisis / LTCM.** Credit spreads blew out. Stress scenario: "What if EM spreads widen 500 bps?"
- **2008 financial crisis.** Stocks fell 50%, credit spreads spiked 300+ bps, correlations jumped to 1. Stress scenario: "2008 revisited."
- **March 2020 ("COVID crash").** Stocks fell 34% in 23 days, volatility spiked, liquidity dried up. Stress scenario: "Pandemic shock."

Post-crisis, regulators usually mandate stress tests based on that crisis. The 2008 crisis prompted the US Federal Reserve to require major banks to conduct annual stress tests.

## Types of stress tests

**Historical scenario stress testing:**
Use an actual crisis. "Replay the 2008 crisis with today's portfolio." This is concrete and grounded in reality.

**Hypothetical scenario stress testing:**
Create an extreme but plausible scenario that might not have occurred. "What if rates rose 300 bps in one month?" or "What if crude oil fell to $20 per barrel?"

**Sensitivity analysis / parameter shock:**
Vary one parameter and see the effect. "If volatility increases 50%, how much do we lose?" This is simpler but less integrated than full scenario stress testing.

**Reverse stress testing:**
Work backwards from an unacceptable loss. "A $1 billion loss would wipe out our capital. What scenarios cause it?" This identifies vulnerabilities.

## Regulatory stress testing

Regulators use stress testing to ensure banks can survive severe crises. The US Federal Reserve conducts the Comprehensive Capital Analysis and Review (CCAR), which stress-tests major banks annually using adverse scenarios like:
- Unemployment rises 5 percentage points.
- Stock market falls 50%.
- Credit spreads widen sharply.
- Interest rates change (rise or fall) by various amounts.

Banks must prove they would remain solvent and profitable in these scenarios. This is [capital adequacy](/capital-adequacy) stress testing.

## Stress testing versus [value-at-risk](/value-at-risk)

**VaR:**
- Based on historical distributions.
- Estimates the 99% or 95% loss.
- Assumes the future is like the past.
- Fast to calculate.
- Misses scenarios outside historical experience.

**Stress testing:**
- Based on explicit scenarios.
- Assesses loss under a specific extreme event.
- Does not require distributional assumptions.
- Slower (requires scenario construction and manual calculation).
- Can explore [tail-risk](/tail-risk) scenarios not in history.

They are complementary. Use VaR for typical risk management and limit-setting. Use stress testing to explore tail risks and ensure preparedness.

## Building a stress test

1. **Identify key risks.** What factors drive portfolio value? Rates? Spreads? Stock prices? FX?

2. **Choose scenarios.** Pick scenarios that stress your key risks. If you hold long-duration [bonds](/bond), stress a rate rise. If you hold corporate bonds, stress a credit crisis.

3. **Determine relationships.** How do holdings respond to the scenario? A 30% stock decline does what to volatility, spreads, and correlations?

4. **Calculate losses.** Apply the scenario to the portfolio and measure the loss.

5. **Set limits.** Decide: is this loss acceptable? Does it exceed capital? Does it trigger risk limits?

6. **Iterate.** If losses are too high, either reduce exposures or increase capital.

## Limitations of stress testing

**Subjectivity.** Who chooses the scenarios? A stress test is only as good as the scenarios selected. If you miss the real tail risk, stress testing does not help.

**No probability.** Stress tests don't assign probabilities. A scenario has a loss, but you don't know if it is 1-in-100-year or 1-in-10,000-year.

**Assumption of static holdings.** During a real crisis, portfolio managers might reduce positions, hedge, or rebalance. Stress tests usually assume holdings are static.

**Liquidity illusion.** Stress tests assume you can sell at stressed prices. In reality, during extreme stress, liquidity evaporates and you cannot sell at any price.

Despite these, stress testing is essential for risk management, especially for exposures to [tail-risk](/tail-risk) and tail-risk scenarios not in historical data.

## See also

<div class="wiki-seealso">

### Closely related

- [Scenario-analysis](/scenario-analysis) — structured assessment of named scenarios
- [Reverse-stress-test](/reverse-stress-test) — work backwards from unacceptable loss
- [Value-at-risk](/value-at-risk) — complements stress testing
- [Expected-shortfall](/expected-shortfall) — alternative risk metric
- [Tail-risk](/tail-risk) — what stress testing aims to assess

### Regulatory context

- [Capital-adequacy](/capital-adequacy) — stress testing ensures capital is sufficient
- [Basel-capital](/basel-capital) — regulatory framework that mandates stress testing
- [Federal Reserve](/federal-reserve) — conducts CCAR stress tests
- Risk-weighted-assets — stress testing informs capital requirements
- Liquidity-coverage-ratio — another regulatory metric stress-tested

### Scenario examples

- [Black-swan](/black-swan) — unpredictable extreme events
- [Gray-swan](/gray-swan) — foreseeable but hard-to-model catastrophic risks
- [Fat-tail-risk](/fat-tail-risk) — distributions have fatter tails than normal

</div>
