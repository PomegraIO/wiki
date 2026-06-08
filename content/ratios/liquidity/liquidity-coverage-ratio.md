---
title: "Liquidity Coverage Ratio"
description: "Basel III regulatory metric requiring banks to hold high-quality liquid assets sufficient to cover 30-day net cash outflows."
keywords:
  - liquidity coverage ratio
  - LCR
  - Basel III
  - bank regulation
  - liquid assets
  - net cash outflows
image: /svg/ratios.svg
---

*The **Liquidity Coverage Ratio (LCR)** is the regulatory answer to a hard question that triggered the 2008 financial crisis: when depositors and creditors panic and demand their money all at once, does your bank have enough unencumbered liquid assets to survive 30 days without external funding? Mandated by [Basel III](/basel-iii/), it requires banks to hold high-quality liquid assets equal to at least 100% of projected net cash outflows over that horizon.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Liquidity Coverage Ratio — key facts</div>

<img src="/svg/ratios.svg" alt="An abstract editorial mark for financial metrics and balance sheet analysis." />

<div class="wiki-infobox-caption">A regulatory liquidity guardrail for systemically important banks.</div>

|   |   |
|---|---|
| **What it is** | High-Quality Liquid Assets ÷ Net Cash Outflows (30 days) |
| **Also called** | LCR, intra-day liquidity requirement |
| **Regulatory minimum** | 100% (as of 2019; phased in from 2015) |
| **Applies to** | Banks above certain size thresholds; varies by jurisdiction |
| **Related measures** | [Net Stable Funding Ratio](/net-stable-funding-ratio/), [Cash to current liabilities ratio](/cash-to-current-liabilities-ratio/), [Capital-adequacy ratio](/capital-adequacy/) |
| **Risk it mitigates** | Bank runs, contagion, fire sales, systemic collapse |

</aside>

## The Basel III genesis: learning from failure

Before the 2008 crisis, banks were never required to model a serious liquidity shock. Lehman Brothers had thousands of pages of sophisticated risk models, yet it suffocated on a 24-hour liquidity crunch. Counterparties fled, funding markets froze, and despite owning real assets worth tens of billions, the bank could not access cash.

Regulators and central banks learned a brutal lesson: capital adequacy alone does not prevent failure. A bank can be solvent on paper—assets exceed liabilities—and still collapse within hours if it cannot raise cash. The [Federal Reserve](/federal-reserve/), [Securities and Exchange Commission](/securities-and-exchange-commission/), and international bodies redesigned the rulebook around liquidity buffers.

The [Liquidity Coverage Ratio](/liquidity-coverage-ratio/) was born as a mandatory floor. It forces large banks to ask the hard question daily: if funding markets freeze and we cannot borrow, roll over [debt](/debt-financing/), or sell assets, can we operate for a month?

## High-quality liquid assets: the numerator

Not all assets are equally liquid in a true crisis. The LCR accepts only tightly defined "High-Quality Liquid Assets" (HQLA):

**Tier 1:** Cash, [central bank](/central-bank/) reserves, and government securities backed by sovereigns with zero or minimal risk weighting (US [Treasury bonds](/treasury-bond/), German Bunds, Japanese government bonds). These can be deployed instantly. Typically, a bank's HQLA is 60%+ Tier 1.

**Tier 2A:** Corporate [bonds](/bond/) rated AA– or higher, bonds issued by quasi-government agencies, municipal [securities](/securities-and-exchange-commission/) meeting strict criteria. Haircuts apply—a €100 bond counts as €85.

**Tier 2B:** Smaller amounts of lower-rated debt and equities. Strict quantitative caps and larger haircuts apply.

Notably absent: illiquid [mortgages](/mortgage-backed-security/), derivatives, non-qualified [corporate bonds](/corporate-bond/), [equity holdings](/equity-financing/), and any asset that requires time or market conditions to sell. A bank cannot count its vast portfolio of loans as HQLA. This is intentional—regulators want assets that can be converted to cash in hours, not months.

## Net cash outflows: the denominator and the 30-day stress scenario

The LCR defines a standardized 30-day stress scenario. It is not a worst-case—it is a *plausible crisis scenario*. It assumes:

- A sharp decline in unsecured funding (funding cost increases, some funding is not rolled over)
- Increased withdrawal of deposits from some categories (retail deposits decline 5–10%, depending on type; institutional deposits face higher run-off rates)
- Decreased inflows (some loan repayments are delayed)
- Contingent outflows triggered by credit events (backup credit lines that get drawn, derivative collateral calls if the bank's credit rating falls)

The scenario is granular. A retail deposit from a small depositor in a stable jurisdiction faces a 5% assumed withdrawal rate. A large institutional deposit from a financial firm in a jurisdiction with rising stress faces a 40% withdrawal rate. The logic: when panic hits, large, sophisticated depositors run first.

Banks compute inflows and outflows across thousands of positions, apply regulatory weights to each, and sum the net. The resulting number is the "Net Cash Outflows" denominator.

## The 100% standard and why it matters

The rule is simple: HQLA ÷ Net Cash Outflows ≥ 1.0.

If a bank's net cash outflows under the stress scenario are $1 billion, it must hold $1 billion in HQLA. If outflows are $10 billion, it must hold $10 billion—unencumbered and available.

This is a binding constraint. A bank cannot lend out every dollar. A portion of assets must sit idle, earning no return, ready for the day funding evaporates. The opportunity cost is real. It directly reduces profitability, which is why banks have argued loudly (and often) that the LCR should be set lower or that definitions of HQLA should expand.

Regulators have occasionally loosened the rules in emergencies. During the COVID-19 pandemic, central banks allowed temporary dips below 100% and expanded what counted as HQLA. But the intent is a hard floor: survive 30 days without outside help.

## Jurisdictional variations and regulatory arbitrage

The LCR is a [Basel III](/basel-iii/) standard, adopted across most major jurisdictions—the European Union, United Kingdom, Switzerland, Australia, Singapore—but with tweaks. Some regulators apply higher thresholds to systemically important banks (those deemed "too big to fail"). The European Union requires 100% as of 2019; the US and UK versions have minor differences in treatment of certain assets and outflows.

Banks naturally shop for regulatory arbitrage. A US bank might shift assets to jurisdictions with looser LCR rules. Regulators counter by requiring consolidated HQLA calculations and imposing additional buffers on consolidated entities.

## The relationship to net stable funding ratio

The LCR handles short-term shocks—30 days. The [Net Stable Funding Ratio](/net-stable-funding-ratio/) (NSFR) handles longer-term funding stability—a one-year horizon. NSFR requires banks to have stable funding sources equal to required stable funding amounts across a wider range of assets and liabilities.

Together, LCR and NSFR form a two-layer defense: survive a month of panic, and ensure one-year funding resilience even in normal times.

## The stress test linkage

The LCR is static at any given date. But regulators also run dynamic "stress tests" that model multi-quarter scenarios (recession, asset fire sales, defaults) and calculate how much capital and liquidity would erode. A bank that passes the LCR test but flunks a stress test gets targeted for capital raises or business divestitures.

The most famous stress test is the US Comprehensive Capital Analysis and Review (CCAR). A bank cannot increase dividends or repurchase stock if its projected capital ratios fall below minimums under the stress scenario. Over the past decade, this has forced major banks to retain capital rather than return it to shareholders.

## Limitations and debates

Critics argue the LCR is:

- **Too blunt:** The standardized 30-day scenario does not match any real bank's actual funding profile. A bank that funds itself largely through retail deposits faces different run-off dynamics than one relying on repo markets or capital markets. A one-size-fits-all rule misses subtlety.

- **Too generous with HQLA:** Government bonds are assumed to be perfectly liquid, but in a true systemic crisis, even [Treasury markets](/treasury-bond/) can seize up. A bank cannot be sure it can sell Treasuries without moving the market.

- **Too narrow on outflows:** The 30-day window may be too short. The 2008 crisis extended for months. A bank surviving 30 days but facing a 90-day solvency crisis is not meaningfully safer.

- **Procyclical:** In a downturn, when banks most need to raise capital, they face rising outflow assumptions and HQLA haircuts. This forces selling, which worsens the crisis.

Defenders counter that the LCR is a minimum, not a ceiling. Banks hold more HQLA in practice. And the rule has demonstrably reduced leverage and improved resilience; the 2020 pandemic shock was far less severe than 2008, partly because banks were better capitalized and more liquid.

## The 2008 versus 2020 lessons

Lehman Brothers collapsed because it could not access funding for 24 hours. Under the LCR, it would have been required to hold a month's worth of liquid assets, which would have bought time for negotiation, rescue, or orderly wind-down.

In March 2020, when COVID lockdowns triggered panic, large banks' LCRs fell to the low-to-mid-100s but never dipped below 1.0. Retail depositors did not withdraw en masse; institutions had confidence the banks would survive. The LCR did its job: it provided a credible floor, reducing panic.

## See also

<div class="wiki-seealso">

### Closely related

- [Cash to Current Liabilities Ratio](/cash-to-current-liabilities-ratio/) — the non-bank equivalent of immediate liquidity
- [Acid-Test Ratio](/acid-test-ratio/) — a stricter quick liquidity measure
- [Interval Measure](/interval-measure/) — days of operation fundable from liquid assets
- [Net Stable Funding Ratio](/net-stable-funding-ratio/) — one-year funding resilience standard
- [Capital-Adequacy Ratio](/capital-adequacy/) — minimum capital buffer for credit risk

### Wider context

- [Basel III](/basel-iii/) — international regulatory framework for bank capital and liquidity
- [Federal Reserve](/federal-reserve/) — US central bank and primary regulator
- Bank Run — panic withdrawal of deposits
- [Systemic Risk](/systemic-risk/) — contagion that threatens the entire financial system
- [Stress Testing](/stress-testing/) — regulatory scenarios for capital and liquidity

</div>