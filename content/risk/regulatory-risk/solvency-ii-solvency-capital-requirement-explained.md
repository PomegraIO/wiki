---
title: "Solvency II Solvency Capital Requirement Explained"
description: "Solvency II's Solvency Capital Requirement (SCR) sets a minimum capital buffer for EU insurers, calculated via standard formula or internal models, to cover unexpected losses."
keywords:
  - solvency ii solvency capital requirement explained
  - solvency capital requirement scr
  - solvency ii standard formula
  - insurance regulatory capital
  - solvency ii internal model
image: "/svg/risk.svg"
---

*The **Solvency Capital Requirement (SCR)** under the European Union's Solvency II Directive is the minimum amount of capital (the financial cushion) an insurer must hold to withstand an unexpected adverse event over a one-year horizon with a 99.5% confidence level. Put plainly: an insurer must hold enough capital so that in only 1 out of 200 bad scenarios would it run out of money. The SCR can be calculated using a standardized regulatory formula or, for larger or more complex insurers, through an internally developed [risk model](/risk-weighted-assets/). Failure to maintain the SCR triggers immediate regulatory intervention.*

<div class="wiki-hatnote">

Not to be confused with the Minimum Capital Requirement (MCR), a lower floor below which an insurer faces automatic license suspension or closure; Solvency II also defines this double-floor system.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Solvency Capital Requirement — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for insurance and regulatory risk." />

<div class="wiki-infobox-caption">Solvency II translates risk quantitatively into a capital mandate; the SCR is the main pillar of the framework.</div>

|   |   |
|---|---|
| **Confidence level** | 99.5% (loss coverage in 1 in 200 bad years) |
| **Horizon** | 12 months |
| **Calculation methods** | Standard formula (regulatory prescription) or internal model (firm-specific) |
| **Coverage** | [Counterparty risk](/counterparty-risk/), underwriting risk (life, health, property), market risk, operational risk |
| **Breach consequence** | Regulatory capital add-ons, profit restrictions, business plan mandates, ultimatum to recapitalize |
| **Comparison** | Replaces Solvency I (1973 rules based on premium volume/reserves) |
| **Softer floor** | Minimum Capital Requirement (MCR) is about 25–45% of SCR; breach triggers closure threat |

</aside>

## The Solvency II Architecture

Solvency II, adopted across the European Economic Area in 2016, replaced Solvency I, which was crude: it required an insurer to hold capital proportional to written premiums or claims reserves, with no differentiation for risk. An insurer writing auto insurance (moderate risk) faced the same capital regime as one writing catastrophe reinsurance (extreme risk). Solvency II corrected this by moving to a **risk-sensitive, probability-based** framework.

The SCR sits as the middle pillar of Solvency II's three-pillar architecture. Pillar 1 covers technical capital rules (the SCR). Pillar 2 establishes governance and supervisory review—regulators scrutinize whether the insurer's own risk assessment is sound. Pillar 3 mandates transparency: public and regulatory reporting so market participants and authorities can assess solvency.

## The Standard Formula Approach

Most insurers, particularly smaller ones, use the **standard formula**—a regulatory recipe that breaks risk into modules and calculates capital as a multiple of each. The main modules are:

- **Market risk** (interest rate risk, equity risk, currency risk, real estate risk, spread risk): an insurer holds bonds and equities; if interest rates spike or equity markets tank, asset values fall. The SCR must cover this [market risk](/market-risk/).
- **Underwriting risk** (life, health, non-life): if an insurer underestimated claim frequencies or severity, reserves prove insufficient. The formula imposes capital buffers proportional to premiums written and reserves held.
- **Counterparty risk**: if a reinsurer or derivative counterparty defaults, the insurer loses the hedging benefit. SCR must cover that [counterparty risk](/counterparty-risk/).
- **Operational risk**: a simple formula ties this to premium and claims volumes, capturing the reality that a bigger book has more operational loss exposure.

The regulator sums these modules (with some diversification offset, reflecting that not all risks hit simultaneously), and multiplies by a supervisory constant to reach a final capital charge.

## The Internal Model Route

Larger or more sophisticated insurers can use an **internal model** approved by their national regulator. Instead of a one-size-fits-all formula, the insurer builds a probabilistic model of its own loss distribution, typically using stochastic simulation or econometric techniques. The model projects what portfolio losses would look like in adverse scenarios, derives the 99.5th percentile (the threshold loss that occurs in 1 out of 200 bad years), and that percentile is the SCR.

An internal model is more granular—it can reflect an insurer's actual underwriting mix, hedging strategy, and [asset allocation](/asset-allocation/). But it requires substantial data and expertise. Regulators must pre-approve the model and conduct ongoing validation. Misspecification—e.g., underestimating [tail risk](/tail-risk/) or correlation in a stress—can lead to insufficient capital and regulatory censure.

## A Worked Example

Suppose a mid-sized property insurer writes €500 million of annual premiums across building, auto, and general liability. Its standard formula SCR calculation might proceed as:

**Non-life underwriting risk**: The formula may require 10% of premiums (calibrated to historical premium-to-loss ratios), yielding €50 million. Separately, 10% of reserves (if reserves are €300 million), adding €30 million.

**Market risk**: The insurer holds €200 million of bonds and €100 million of equities. Interest rate shock might hit bonds by €8 million; equity stress might hit equities by €20 million. Market risk module = €28 million.

**Counterparty risk**: The insurer buys reinsurance; if a reinsurer defaults, the insurer loses recovery. Counterparty risk charge = €5 million.

**Operational risk**: Roughly 10% of premiums and incurred claims (€500M + €450M incurred), yielding €10 million.

**Sum before diversification**: €50 + €30 + €28 + €5 + €10 = €123 million. A diversification adjustment (reducing this by, say, 15%) gives a final SCR of ~€104 million. The insurer must hold €104 million in capital (equity, retained earnings) over its claims reserves.

## Regulatory Intervention

If an insurer breaches the SCR—capital falls below the requirement—the national regulator does not immediately shut it down but enters supervisory dialogue. The regulator may:

- Demand a capital restoration plan with quarterly milestones.
- Restrict new business underwriting.
- Forbid dividend payments or share buybacks.
- Require higher prices or stricter underwriting to rebuild capital faster.

If the insurer falls below the MCR (roughly 25–45% of the SCR depending on the country), the regulator can withdraw the license, initiating insolvency proceedings. The MCR is a legal floor; breaching it is a capital event.

## Challenges and Critiques

The standard formula imposes a one-size-fits-all regime that may over-capitalize safe, conservative insurers and under-capitalize aggressive risk-takers. Internal models offer escape but require regulatory approval and generate debate over model validity. During the 2008 financial crisis, many internal models failed to predict losses, exposing the limits of even sophisticated [value-at-risk](/value-at-risk/) approaches.

Some critics argue that Solvency II, by focusing on one-year [tail risk](/tail-risk/) at a 99.5% level, may miss very-low-probability catastrophes. A 1-in-200-year flood scenario is captured; a 1-in-500-year event is not. Severe tail events (earthquakes, pandemics, geopolitical shocks) have hit insurers beyond what Solvency II alone would mandate.

Additionally, Solvency II is EU-specific, creating regulatory arbitrage: non-EU insurers writing EU business face Solvency II; EU insurers operating in the U.S. face NAIC capital rules (different formulas, different confidence levels), complicating global insurance groups' capital planning.

## Post-COVID and Refinements

After COVID-19, regulators have tightened scrutiny on pandemic risk modeling and liquidity stress. A 2024 review of Solvency II may shift some capital charges—particularly around equity risk and long-duration liability risk—to reflect post-pandemic economic realities. Dynamic interest rate environments have also prompted reassessment of interest-rate shock calibrations, as the 2023 banking crisis exposed hidden [duration risk](/duration/) in fixed-income portfolios.

## See also

<div class="wiki-seealso">

### Closely related

- [Risk-Weighted Assets](/risk-weighted-assets/) — similar concept for banks; solvency regimes differ across sectors
- [Counterparty Risk](/counterparty-risk/) — one major risk pillar in the SCR
- [Market Risk](/market-risk/) — the interest rate and equity risk component
- [Tail Risk](/tail-risk/) — the extreme-loss scenario captured at the 99.5th percentile
- [Capital Adequacy](/capital-adequacy/) — the overarching principle of holding sufficient capital buffers

### Wider context

- [Derivative Hedging](/derivatives-hedging/) — how insurers manage SCR through risk transfer
- Reinsurance — the market mechanism for externalizing underwriting risk
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — in the U.S., coordinates with NAIC on insurer oversight
- [Operational Risk](/operational-risk/) — the fourth risk pillar in Solvency II

</div>
