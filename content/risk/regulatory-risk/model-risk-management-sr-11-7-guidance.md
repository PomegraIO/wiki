---
title: "Model Risk Management and the SR 11-7 Guidance"
description: "SR 11-7 supervisory letter outlines Federal Reserve requirements for model risk management, validation, and ongoing monitoring."
keywords:
  - model risk management sr 11-7 guidance
  - sr 11-7 federal reserve
  - model validation requirements
  - conceptual soundness
  - model governance
image: /svg/risk.svg
---

*The US Federal Reserve's **model risk management and the SR 11-7 guidance** sets the standard for how banks and financial institutions must validate, govern, and monitor the models they use for critical decisions—from pricing derivatives to setting [risk-weighted assets](/risk-weighted-assets/) to running stress tests. SR 11-7 is not law but a supervisory directive that shapes examination standards and regulatory expectations.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">SR 11-7 Guidance — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The Fed's benchmark for model governance across the financial system.</div>

|   |   |
|---|---|
| **Issued** | May 2011 (and reaffirmed through supervisory practice) |
| **Applies to** | Banks, large financial institutions, Fed-supervised entities |
| **Core requirement** | Independent model validation and governance |
| **Key framework** | Three pillars: development, validation, use and monitoring |
| **Real-world scope** | Credit risk, market risk, operational risk, ALM models |
| **Enforcement** | Through federal bank examinations and consent orders |
| **Red flag** | No independent validation, or models treated as black boxes |

</aside>

## What Is Model Risk?

Before diving into SR 11-7, the concept: **model risk** is the potential loss a bank faces when the mathematical or statistical model it relies on to make a decision is wrong, misused, or misunderstood. A bank may use a [credit-risk](/credit-risk/) model to decide how much capital to hold against a loan portfolio, a [value-at-risk](/value-at-risk/) (VAR) model to estimate daily trading losses, or a pricing model to value mortgage-backed securities. If the model is flawed, calibrated to old data, or applied outside its valid range, the bank can suffer large unexpected losses.

The 2008 financial crisis exposed massive model risk across the banking system. Banks used models that assumed housing prices never fell nationwide, models that underestimated correlation in a stress scenario, and models that treated complex structured products as low-risk because historical data was too short to capture a rare event. SR 11-7 emerged as the Federal Reserve's answer: banks must actively manage model risk, not just build models and assume they work.

## The Three Pillars: Development, Validation, and Monitoring

SR 11-7 organizes model governance into three overlapping domains.

**Development and implementation** is the first. A bank must document the model's purpose, assumptions, mathematical foundation, data sources, and limitations. Before deployment, the model's design must be sound—the underlying economic logic must hold. A credit model that ignores macroeconomic variables in a cyclical industry, or a pricing model built only on bull-market data, fails the conceptual soundness test before validation even starts.

**Validation** is the second pillar and the heart of SR 11-7. Validation is *independent* review—ideally carried out by a team separate from the model developers. Validators must check:
- Does the model perform as intended on historical data?
- Does it fail or degrade gracefully outside its normal operating range (stress scenarios)?
- Are the input data accurate and updated regularly?
- Have the model's outputs been backtested against actual outcomes?
- Are the assumptions still reasonable, or have market conditions changed?

Importantly, validation is not a one-time event. A model validated in 2018 but never retested after a regime shift (e.g., interest rate changes, new regulations) becomes a liability. SR 11-7 expects **ongoing monitoring and periodic revalidation**, especially after major business changes or market events.

**Independent model review** is critical here. The validator should report to an independent governance committee or chief risk officer, not to the business line that built and uses the model. This separation is meant to prevent conflicts of interest: the team that profits from a model is not the team that judges whether it's sound.

**Use and monitoring** is the third pillar. A bank must establish policies for:
- Who can use the model and under what conditions?
- What is the model's valid range (e.g., applicable only to prime mortgages under normal rate regimes)?
- What triggers a pause or recalibration (e.g., if error rates exceed a threshold)?
- How are model outputs fed into business decisions, and is there human oversight?
- How often is the model output compared to actual realized outcomes?

A model that predicts credit losses but is never compared to actual default rates is flying blind. Backtesting—comparing predicted vs. actual—is the feedback loop that keeps a model honest.

## Conceptual Soundness: The Foundation

SR 11-7 places heavy emphasis on **conceptual soundness**, the economic logic underlying a model. A technically sophisticated model with perfect statistics can still be conceptually unsound if it ignores a material factor or rests on a false premise.

Classic example: a [credit-default-swap](/credit-default-swap/) pricing model built on the assumption that default correlation among structured-finance tranches approaches zero in stress scenarios fails conceptual soundness. When stress actually occurs (2008), correlations spike to 1, defaults cluster, and the model is worthless.

A sound model must:
1. Capture the economic drivers that matter (for a credit model: borrower income, debt-to-income ratios, macroeconomic conditions, loan features).
2. Rest on assumptions defensible by theory or evidence.
3. Acknowledge its limits (e.g., "this model is valid for prime mortgages in normal rate regimes; not applicable to subprime or inverted yield curves").
4. Be transparent about tradeoffs (e.g., including too many variables overfits to historical data; too few and you miss real drivers).

When a bank uses a model as a black box—plugging in inputs without understanding the guts—it fails this test. SR 11-7 expects practitioners and validators to understand the model deeply enough to explain why it works and when it might fail.

## Data Quality and Governance

SR 11-7 demands rigorous data governance. A model is only as good as its inputs. If a [credit-risk](/credit-risk/) model is fed outdated portfolio composition data, or a market [VAR](/value-at-risk/) model uses stale correlation matrices, the output is unreliable.

Banks must:
- Define data lineage: where does each input come from, who maintains it, what checks ensure accuracy?
- Establish escalation procedures when data quality flags arise (e.g., if historical default rates are reported late or inconsistently).
- Track data changes and rerun models when material input shifts occur.
- Document data assumptions and limitations in model documentation.

For highly automated models or those fed real-time market data, monitoring data feeds becomes part of operational risk. A [value-at-risk](/value-at-risk/) model that breaks because a market data provider goes offline exemplifies operational fragility that SR 11-7 expects banks to identify and mitigate.

## Stress Testing and Model Boundaries

SR 11-7 implicitly requires that banks test models under stress—scenarios where the model's assumptions are violated. A credit model built on 20 years of low-default history is untested in a recession. A [duration](/duration/) model built on stable rates is untested in a rising-rate environment.

Banks are expected to:
- Run models through historical stress scenarios (e.g., 2008, 2020).
- Run hypothetical stress scenarios beyond historical experience (e.g., a 500-basis-point rate shock).
- Document when and why the model's output becomes unreliable (e.g., "this model is not valid if unemployment exceeds X%").
- Establish decision rules for when to pause reliance on a model or apply manual adjustments.

A model that produces an absurd output (e.g., suggesting a 99.9% loss in normal times) should trigger human review, not blind acceptance. SR 11-7 expects banks to build in sanity checks and escalation.

## The Exam Process and Compliance

Federal Reserve examiners look for SR 11-7 compliance through:
- **Model documentation**: Is there a current, detailed write-up of the model's purpose, method, data, and limits?
- **Validation records**: Is there evidence of independent validation, and was it recent?
- **Backtesting results**: Are model predictions compared to actual outcomes? What's the error rate?
- **Governance records**: Meeting minutes, validator sign-offs, model change approvals.
- **Monitoring dashboards**: Does management track model performance in real time?

Banks with weak model governance often face regulatory orders to overhaul their practices, hire validation specialists, or reduce reliance on inadequately governed models. In some cases, examiners require a bank to reprice its entire portfolio under a newly validated model—a costly and humbling exercise.

## Industry Evolution: Challenges and Emerging Practice

Since SR 11-7's 2011 release, model complexity has grown. Machine learning and artificial intelligence models pose new validation challenges. A neural network or random forest model may have high predictive accuracy but little interpretability—making "conceptual soundness" harder to demonstrate. Regulators have adapted, accepting that some modern models *are* opaque, but demanding that banks still validate their outputs, test them for bias, and monitor their drift over time.

Data-hungry models, once recalibrated frequently, can go stale if data pipeline assumptions shift. SR 11-7 does not prescribe a single governance approach, but the principle endures: models are not set-and-forget. They require independent oversight, regular revalidation, and honest backtesting.

## See also

<div class="wiki-seealso">

### Closely related

- [Risk-weighted assets](/risk-weighted-assets/) — how models assign capital requirements
- [Stress testing](/stress-testing/) — scenario analysis required by regulation
- [Counterparty risk](/counterparty-risk/) — a model-dependent measurement
- [Value-at-risk](/value-at-risk/) — a daily risk metric governed by SR 11-7
- [Credit risk](/credit-risk/) — the domain where model risk is most acute

### Wider context

- [Capital adequacy](/capital-adequacy/) — the regulatory framework that depends on models
- [Federal Reserve](/federal-reserve/) — the supervisor enforcing this guidance
- [Operational risk](/operational-risk/) — modeling and governance of non-credit losses

</div>
