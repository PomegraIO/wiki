---
title: "Scenario Analysis"
description: "Scenario analysis is a structured method of assessing portfolio losses under specific, named market conditions by explicitly defining key variables and calculating outcomes across different scenarios."
keywords:
  - scenario analysis
  - scenario planning
  - what-if analysis
  - case analysis
  - conditional loss
image: "/svg/risk.svg"
---

*Scenario analysis is a systematic method for assessing portfolio risk by constructing and evaluating multiple named scenarios — specific, internally consistent descriptions of future states — and calculating portfolio losses in each. It is more structured than open-ended [stress-testing](/stress-testing/) and complements quantitative risk measures like [value-at-risk](/value-at-risk/).*

<div class="wiki-hatnote">

This entry covers structured scenario analysis. For exploratory stress testing without specific scenarios, see [stress-testing](/stress-testing/); for the measurement of typical losses, see [value-at-risk](/value-at-risk/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Scenario Analysis — key facts</div>

<img src="/svg/risk.svg" alt="Three branching paths from a starting point, each labeled with a different future state" />

<div class="wiki-infobox-caption">Scenario analysis defines multiple plausible futures and their implications.</div>

|   |   |
|---|---|
| **What it is** | Structured analysis of portfolio under named, consistent scenarios |
| **Number of scenarios** | Typically 3-5; "Base," "Bull," "Bear," etc. |
| **Components** | Each scenario specifies key variables (rates, spreads, FX, growth) |
| **Time horizon** | Medium-term (months to years) or short-term (days to weeks) |
| **Outcome** | Loss or gain in each scenario; sensitivity to key variables |
| **Use** | Strategic allocation decisions; risk limits; hedge design |
| **Advantage** | Explicit about assumptions; easy to communicate |

</aside>

## How scenario analysis works

**Step 1: Define scenarios.**
Create 3-5 named scenarios representing plausible futures. Example:
- **Base case:** Interest rates stable; growth continues; no major shocks.
- **Bull case:** Rates fall; growth accelerates; risk appetite increases.
- **Bear case:** Recession; rates fall sharply; credit spreads widen.
- **Inflation scenario:** Rates rise; growth slows; inflation persists.
- **Crisis scenario:** Financial shock; credit spreads spike; correlations jump to 1.

**Step 2: Specify key variables in each scenario.**
For each scenario, define the values of key drivers:

| Variable | Base | Bull | Bear | Inflation | Crisis |
|---|---|---|---|---|---|
| Stock return | 8% | 15% | -20% | -10% | -30% |
| Rate change | 0 bps | -50 bps | -200 bps | +150 bps | -100 bps |
| Credit spread | 0 | -50 bps | +200 bps | +50 bps | +300 bps |
| VIX | 15 | 10 | 40 | 25 | 60 |

**Step 3: Calculate portfolio loss in each scenario.**
Apply each scenario's variables to the portfolio. Calculate new values and losses.

**Step 4: Assess outcomes.**
Compare losses across scenarios. Identify which scenarios hurt most and why. Adjust portfolio if needed.

## Example: Scenario analysis for a balanced portfolio

**Portfolio:** 60% stocks, 40% bonds, 5% hedge fund.

**Scenarios and outcomes:**

| Scenario | Stock loss | Bond gain/loss | HF return | Portfolio return |
|---|---|---|---|---|
| Base (stable) | +8% | +2% | +5% | +5.5% |
| Bull (growth) | +15% | -1% (duration) | +8% | +8.3% |
| Bear (recession) | -20% | +8% (flight to quality) | -5% | -5.0% |
| Inflation (rising rates) | -10% | -5% | 0% | -6.5% |
| Crisis (systemic) | -30% | -2% (spread widening) | -15% | -18.0% |

**Insights:**
- Worst case: Crisis scenario, -18%.
- Best case: Bull scenario, +8.3%.
- Inflation scenario hurts despite bonds gaining (bonds fall due to rate rise).
- HF provides modest diversification in base and bull; loses in tail.

**Decision:** The portfolio can lose 18% in a crisis. Is that acceptable? If not, increase bonds/cash or buy [tail hedges](/tail-risk/).

## Scenario analysis in practice

**Strategic asset allocation.** Investors use scenarios to decide how much to allocate to stocks, bonds, alternatives. "In a bull scenario, I want to capture upside; in a bear scenario, I want downside protection. What allocation balances these?" Scenarios help answer this.

**Derivative hedging.** A corporation with foreign currency exposure uses scenarios to determine how many currency [forwards](/currency-risk/) to buy. "In a depreciation scenario, I lose $X; the hedge protects me for cost Y. Is Y worth it?"

**Credit decisions.** A lender to a company assesses creditworthiness by scenario. "In base case, the borrower is fine. In recession scenario, do they default?" If recession risk is high, require a higher interest rate.

**Risk limits.** Risk managers set limits based on scenarios. "We will not hold any position where the worst-case scenario (crisis) loss exceeds 5% of capital." This operationalizes risk tolerance.

## Advantages of scenario analysis

**Explicit and communicable.** Scenarios are concrete and easy to explain to boards, clients, and risk committees. "Here is what happens in a bear market."

**Flexible.** Can be customized to a specific portfolio and risks. Tailor scenarios to your exposures.

**No distributional assumption.** Unlike [value-at-risk](/value-at-risk/), scenario analysis does not assume returns follow a normal distribution.

**Captures tail risks.** By including explicit tail scenarios (crisis, crash), you address [tail-risk](/tail-risk/) that models often miss.

**Addresses unknowns.** Scenarios can be updated as new information arrives. If geopolitical risk rises, add a "war scenario."

## Limitations of scenario analysis

**Subjectivity.** Scenarios are chosen by humans. If you miss a plausible scenario (as happened before [black swans](/black-swan/)), analysis is incomplete.

**No probability.** Scenarios do not have assigned probabilities. You know the loss in each but not the odds of each occurring.

**Static holdings.** Analysis assumes holdings do not change. In reality, during a crisis, positions are sold, hedges are exercised, [correlations](/stock-market/) change.

**Labor-intensive.** Scenario analysis requires significant manual work. Easy for simple portfolios; painful for complex ones.

## Scenario analysis versus stress testing

**Scenario analysis:**
- Named scenarios with consistent variable values.
- Structured and repeatable.
- Good for communicating risk.

**Stress testing:**
- Open-ended; can be any extreme scenario.
- More exploratory.
- Good for discovering vulnerabilities.

Use both: scenario analysis for regular risk reporting; stress testing to explore edge cases.

## See also

<div class="wiki-seealso">

### Closely related

- [Stress-testing](/stress-testing/) — complementary approach to scenario analysis
- [Value-at-risk](/value-at-risk/) — quantitative alternative
- [Expected-shortfall](/expected-shortfall/) — tail-loss measure
- [Reverse-stress-test](/reverse-stress-test/) — work backwards from unacceptable loss
- [Tail-risk](/tail-risk/) — what scenarios aim to assess

### Application areas

- [Asset allocation](/asset-allocation/) — decisions informed by scenarios
- Hedging — sizing hedges based on scenarios
- [Capital adequacy](/capital-adequacy/) — regulatory stress tests use scenarios
- [Black-swan](/black-swan/) — scenarios explore extreme events
- [Gray-swan](/gray-swan/) — foreseeable catastrophic scenarios

### Strategic use

- [Risk management](/value-at-risk/) — scenarios inform limits and controls
- [Portfolio management](/asset-allocation/) — scenarios guide allocation decisions
- [Corporate risk](/operational-risk/) — scenarios assess business impacts

</div>
