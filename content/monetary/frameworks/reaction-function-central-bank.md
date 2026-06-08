---
title: "Central Bank Reaction Function"
description: "How a central bank reaction function maps economic conditions to policy rate decisions, and why analysts estimate it to anticipate future monetary policy moves."
keywords:
  - central bank reaction function
  - policy rate rule
  - taylor rule monetary policy
  - reaction function estimation
  - federal reserve policy rules
  - inflation targeting
---

*A **central bank reaction function** is a mathematical relationship that maps economic conditions—inflation, unemployment, output growth—to the central bank's setting of the policy interest rate. Analysts estimate these functions to understand how a central bank has behaved historically and to forecast how it will likely respond to future economic shocks. The most famous example is the Taylor rule, which prescribes the fed funds rate as a function of inflation and the output gap.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reaction Function — key facts</div>

<img src="/svg/monetary.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A central bank reaction function is the policy rule linking economic data to rate decisions.</div>

|   |   |
|---|---|
| **Basic form** | Policy rate = f(inflation, unemployment, output gap, lagged rate) |
| **Most cited rule** | Taylor rule: specifies inflation and output gap weights |
| **Purpose of estimation** | Forecast policy moves, understand historical consistency |
| **Key variables** | Inflation target, neutral rate, current output gap |
| **Typical lag** | Central banks often smooth rates; previous rate is a variable |
| **Policy framework** | Used by [Federal Reserve](/federal-reserve/), ECB, and emerging-market central banks |

</aside>

## The concept: mapping data to decisions

A reaction function is a shorthand for the systematic way a central bank sets policy. Rather than treating each rate decision as idiosyncratic or opaque, economists model the bank as responding predictably to the economic data it observes or forecasts. When inflation rises, the bank raises the policy rate; when unemployment climbs, the bank may cut rates. The strength of these responses—how much the rate moves per unit of inflation or unemployment change—defines the bank's "stance" or "reaction intensity."

Economists value reaction functions for two reasons. First, they can forecast policy. If you estimate that the Federal Reserve follows a Taylor rule, and you forecast that inflation will rise 50 basis points next quarter, you can predict that the Fed will raise rates by roughly 75 basis points (if the Taylor rule's inflation coefficient is 1.5). Second, they provide a discipline check: if the central bank's actual decisions deviate significantly from its estimated reaction function, something has changed—either the bank has shifted priorities, or the shock is so large that normal rules no longer apply. The 2008 financial crisis, for instance, revealed that the Fed's reaction function temporarily broke down as the zero lower bound on interest rates was hit.

## The Taylor rule: the canonical example

The **Taylor rule**, proposed by economist John Taylor in 1993, is the most widely studied reaction function. It states:

**Policy rate = (Neutral rate) + (Inflation − Inflation target) × (Inflation weight) + (Output gap) × (Output weight)**

Using typical parameters:
- Neutral rate: 2 percent
- Inflation weight: 1.5
- Output gap weight: 0.5
- Inflation target: 2 percent

If inflation is 3 percent (1 percentage point above target) and the output gap is +2 percent (the economy is 2 percent above potential), the rule suggests: 2% + 1 × 1.5 + 2 × 0.5 = **5.0% policy rate**.

The elegance of the Taylor rule is that it is simple, transparent, and grounded in monetary theory. The inflation weight exceeds one, meaning the central bank raises rates more than proportionally to inflation; this ensures that real interest rates (nominal rate minus inflation) rise, cooling demand. The output gap weight is positive but smaller, reflecting the assumption that the bank prioritizes price stability over full employment, though it still cares about the output gap.

Central banks do not explicitly follow the Taylor rule, but when economists estimate what rule best fits a central bank's historical behavior, they often find that the Taylor rule or variants of it perform well. This does not mean the bank consciously uses the rule; rather, the rule captures the systematic patterns in the bank's decisions.

## Estimating reaction functions from historical data

Economists estimate reaction functions by regressing the central bank's actual policy rate on the economic variables the bank is presumed to respond to. A simple version is:

**Policy rate(t) = α + β₁ × Inflation(t) + β₂ × Unemployment(t) + β₃ × Policy rate(t-1) + error**

The coefficients β₁, β₂, β₃ are estimated from decades of monthly or quarterly data. The lagged policy rate term captures **interest rate smoothing**: central banks typically move rates gradually rather than jumping to the optimal rate all at once. A lagged-rate coefficient of 0.7 means that if the "target" rate is 3 percent but the current rate is 2 percent, the bank will move only 30 percent of the way to the target in one period, reaching 2.3 percent.

Challenges abound in estimation. First, the choice of variables and lags matters; different specifications yield different coefficients. Second, central banks' priorities and targets change over time. The Fed's inflation target was implicit (roughly 2 percent) in the 1990s but became explicit in 2012. Third, structural breaks occur; the 2008 crisis and 2020 pandemic shifted the relationship between unemployment and inflation (the Phillips curve), so reaction functions estimated before and after the break differ. Fourth, the concept of the "neutral rate" or "natural rate of unemployment" is unobservable and must be estimated, introducing measurement error.

Despite these challenges, estimated reaction functions are remarkably consistent across different studies and time periods. Most estimates confirm that the Fed has a stronger response to inflation than to unemployment, and that the Fed smooths rates over time.

## Why analysts use reaction functions to forecast policy

Central banks are reluctant to pre-commit to mechanical rules; they preserve discretion to handle crises and adapt to structural change. Yet discretion creates uncertainty for markets and investors. By estimating a central bank's historical reaction function, analysts create a baseline forecast of what the bank "should" do given current economic conditions. When the bank deviates, the deviation is noteworthy and signals new priorities or unforeseen constraints.

For instance, in 2023–2024, the Fed kept raising rates despite a sharp inversion of the yield curve (usually a recession signal) and signs of financial stress. Analysts who had estimated the Fed's reaction function expected rate cuts by late 2023. The Fed's deviation from the estimated function alerted markets that the Fed was prioritizing inflation control over financial stability—a change in weights, not a breakdown of the rule.

Investors use these forecasts to position portfolios. If you forecast that the Fed will cut rates 50 basis points in the next year based on your reaction function estimate, you buy long-duration bonds (which appreciate when rates fall). If the Fed surprises by raising instead, your positioning is wrong and you lose. Central banks understand this and sometimes signal (via speeches and forward guidance) what they expect inflation and unemployment to do, and thus what the reaction function predicts they will do. This transparency helps manage expectations.

## Non-linear and regime-switching reaction functions

The classic Taylor rule assumes a linear relationship: each additional point of inflation always produces the same policy response. But central banks may behave nonlinearly. For example, when rates approach the zero lower bound, the bank cannot cut further and must rely on unconventional tools like [quantitative easing](/quantitative-easing/). The reaction function "switches" regimes.

Similarly, central banks may respond more aggressively to large inflation surprises than to small ones, or may react differently depending on whether inflation expectations are anchored. Advanced estimates use machine-learning and regime-switching models to capture these nonlinearities. However, the more parameters a model has, the more data is needed to estimate it reliably, and history sometimes runs out before a crisis repeats.

## Central bank forward guidance and implied reaction functions

Modern central banks publish "dot plots" (projections of future policy rates) and issue forward guidance ("we expect to keep rates on hold through 2025"). These communications reveal the bank's implicit reaction function: the rate path it expects to follow given its forecasts of inflation and unemployment. Market participants extract the reaction function from the guidance, then challenge it when economic data surprises.

When the [Federal Reserve](/federal-reserve/) projects three rate cuts in 2024 but inflation remains sticky and unemployment low, markets infer that the Fed's reaction function is loosening—the bank is placing less weight on inflation and more on growth, or is targeting a lower neutral rate. These inferences affect asset prices immediately.

## See also

<div class="wiki-seealso">

### Closely related

- [Taylor Rule](/taylor-rule/) — Canonical monetary policy rule framework
- [Federal Reserve](/federal-reserve/) — Primary implementer of U.S. monetary policy
- [Monetary Policy](/monetary-policy/) — Broader framework for rate setting
- [Inflation Expectations](/inflation-expectations/) — Key variable in reaction function models
- [Forward Guidance](/forward-guidance/) — How central banks communicate future policy intentions

### Wider context

- [Interest Rate](/interest-rate/) — Core policy instrument modeled by reaction functions
- [Central Bank](/central-bank/) — Institutional context
- [Business Cycle](/business-cycle/) — Economic backdrop for policy responses
- [Phillips Curve](/phillips-curve/) — Relationship between unemployment and inflation that informs reaction functions

</div>
