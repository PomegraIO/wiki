---
title: "Risk Aggregation Across Asset Classes"
description: "Risk aggregation combines VaR or factor exposures across equities, bonds, and derivatives into a firm-wide risk number. Learn the practical challenges."
keywords:
  - risk aggregation
  - var aggregation
  - asset class risk
  - factor risk
  - firm-wide risk
  - portfolio diversification
image: /svg/risk.svg
---

*Summing up [**risk aggregation**](/risk-aggregation-across-asset-classes/) across asset classes—adding VaR from equities to VaR from bonds to VaR from derivatives—looks straightforward on paper but stumbles on the real-world complications: different risk models, hidden correlations, liquidity mismatches, and the fact that diversification breakdowns exactly when you need it most.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk Aggregation — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk." />

<div class="wiki-infobox-caption">The holy grail of risk management—one number capturing all firm exposure—is elegant in theory and messy in practice.</div>

|   |   |
|---|---|
| **Definition** | Combining [VaR](/value-at-risk/), stress, or Greeks across all books |
| **Common metrics** | [VaR](/value-at-risk/), expected shortfall, sensitivity limits |
| **Challenge** | Different models for equities, bonds, derivatives, FX |
| **Correlation assumption** | Historic or assumed; breaks in stress |
| **Pitfall** | Two assets uncorrelated in calm markets → 0.95 in a crisis |
| **Governance** | Enterprise risk committee; daily or weekly review |
| **Regulators** | [Dodd-Frank](/dodd-frank-act/), Basel III demand firm-wide VaR |

</aside>

## Why Firms Need Aggregation

A mid-sized financial institution might run ten trading desks: equities, fixed income, foreign exchange, commodities, derivatives, structured products, and more. Each desk has its own risk models and daily [VaR](/value-at-risk/) numbers. The equity desk reports a $2M VaR; the bond desk reports $1.8M; the derivatives desk reports $0.9M. The chief risk officer needs to know: What is the firm's total risk exposure?

The simplest answer—$2M + $1.8M + $0.9M = $4.7M—is wrong. It assumes every desk's loss happens simultaneously. In reality, some assets move together; others move in opposition. [Diversification](/diversification/) means the firm's VaR is lower than the sum of the parts. The real answer might be $3.2M, reflecting that equity, bond, and commodity moves are not perfectly correlated.

But here's the catch: that $3.2M number is only as good as the correlation assumptions, and those assumptions explode in a crisis.

## The Aggregation Methods

**Simple summation (worst-case stacking).** Add all desk [VaRs](/value-at-risk/) without any correlation adjustments. Used only for gross exposure limits and as a conservative sanity check. Overstates true risk but ensures no hidden leverage.

**Correlation-based VaR aggregation.** The standard method: treat each desk's P&L as a variable, estimate the correlation matrix between desks (or between asset classes), then compute the firm-wide VaR using portfolio theory.

Formula (simplified):
**Firm VaR² = Σ(VaR_i²) + 2 × Σ(ρ_ij × VaR_i × VaR_j)**

The first term is the sum of squared individual VaRs. The second term captures correlations: positive correlation increases firm VaR; negative correlation reduces it (hedging effect). Estimate ρ_ij from daily returns over the past year or two, and you get an aggregate number.

**Factor model aggregation.** Instead of correlating desks, decompose each desk's P&L into common factors (equity beta, interest rate duration, credit spread, volatility). Then aggregate the factor exposures.

Example:
- Equity desk: $5M exposure to market beta, $0.5M to small-cap factor
- Bond desk: $(3)M (short) to interest rate factor, $1.2M to credit factor
- Commodity desk: $2M to oil price, $(0.3)M to agricultural prices

A central risk function can then compute the firm's total exposure to each factor, and apply a single sensitivity model across the firm. This is more transparent but requires each desk to break down its risk in a consistent taxonomy.

**Stress-based aggregation.** Instead of relying on [VaR](/value-at-risk/) or correlations, apply a scenario (e.g., "equities fall 20%, credit spreads widen 200bp, implied volatility spikes to 50%") and compute the firm's loss. Aggregate across multiple scenarios. Stress testing avoids correlation assumptions but is labor-intensive.

## Core Challenges

**Different asset class models.** Equity models use beta and volatility; bond models use duration and convexity; derivatives models use [Greeks](/delta/) and [volatility surface](/volatility-smile/) assumptions. There is no single "VaR" methodology that applies cleanly to all. An equity desk might use a historical [VaR](/value-at-risk/) model; a bond desk uses a duration/convexity model; a derivatives desk uses a full revaluation (Monte Carlo). Aggregating these numbers is mixing apples and oranges.

**Correlation instability.** Historic correlations are reliable in calm markets. Equities and bonds are often negatively correlated over a year—a classic diversifier. Then a crisis hits, yields spike, and both equities and bonds fall together. Correlations spike to 0.7 or 0.8. The firm thought it was diversified; suddenly it is not. Regulatory stress tests try to account for this (assuming spike scenarios), but static correlation matrices do not capture the regime shift in real time.

**Hidden leverage.** Desk-level [VaR](/value-at-risk/) can hide leverage. A derivatives desk might hold a large short volatility position that carries low delta and duration exposure (thus low desk-level VaR) but enormous [vega](/vega/) and tail risk. When [implied volatility](/implied-volatility/) explodes, the desk loses a fortune. If no one is aggregating vega across desks (checking that the firm's overall short volatility is not too large), the risk goes undetected.

**Cross-desk correlations and netting.** A major challenge is determining what correlations matter between desks. If the equity desk is long cyclicals and the commodities desk is short oil, there is a natural hedge (recessions hit both). But this hedge is hidden if you are aggregating desk-level VaR numbers. Only detailed factor models surface these cross-desk offsets. Many firms discover (too late) that they have large correlated exposures in seemingly unrelated desks.

**Liquidity mismatches.** [VaR](/value-at-risk/) assumes you can exit a position at yesterday's prices. But in a stress, bid-ask spreads widen, and some assets become illiquid. A bond desk's $1.8M VaR is worthless if the bonds cannot be sold quickly. Equity desks can often exit quickly; some structured product desks cannot. A firm-wide VaR that ignores liquidity differences is misleading.

**Non-linear exposures.** [VaR](/value-at-risk/) is linear: it assumes P&L moves proportionally with market moves. But options, [credit default swaps](/credit-default-swap/), and mortgages are non-linear. A large market move can push a position from low-risk to high-risk (or vice versa). A linear aggregation model misses these threshold effects.

## Practical Governance

Most financial institutions run a three-layer risk review:

**Daily desk limits.** Each desk has a [VaR](/value-at-risk/) limit (e.g., $2M equity desk, $1.8M bond desk). Desk-level reports are automated and checked continuously.

**Weekly enterprise risk review.** Risk aggregation is computed by correlating desks or using a factor model. The enterprise risk committee reviews the firm-wide [VaR](/value-at-risk/), stress scenarios, and exposure to key factors. If firm-wide VaR breaches a threshold or a single factor exposure exceeds a limit, the committee escalates.

**Quarterly stress testing.** The firm runs scenarios: equity crash, credit spread widening, yield curve inversion, volatility spike, etc. Each desk's P&L is modeled under each scenario, then summed. The goal is to identify concentrated bets and correlation fragilities that daily [VaR](/value-at-risk/) might miss.

## Regulatory Requirements

Post-[Dodd-Frank](/dodd-frank-act/), [Basel III](/capital-adequacy/), and Volcker Rule, financial institutions must calculate and report firm-wide [VaR](/value-at-risk/) and stress losses to regulators (the Federal Reserve, CFTC, etc.). The regulations require:

- Daily [VaR](/value-at-risk/) at 99% confidence level (1% tail loss)
- Stress testing under historical scenarios (2008, 1987, etc.)
- Incremental risk capital (IRC) for credit-sensitive instruments
- Comprehensive risk measure (CRM) for correlation and basis risk

These mandates have driven firms to invest in centralized risk infrastructure, though the systems remain imperfect.

## The Enduring Paradox

A well-aggregated [VaR](/value-at-risk/) model says "the firm can lose up to $3M on a bad day." That is useful until the bad day comes and the firm loses $8M. The gap usually reflects either:
- A correlation or exposure that was omitted (a desk held an unmodeled position)
- A tail event outside the historical distribution (a new correlation regime emerged)
- A liquidity crisis (the model assumed exit prices; markets froze)

The best firms handle this by using [VaR](/value-at-risk/) as a baseline and stress testing as a check. They also cultivate a culture where desk heads know that "the [VaR](/value-at-risk/) model said it was okay" is not a defense after a blowup.

## See also

<div class="wiki-seealso">

### Closely related

- [Value-at-Risk](/value-at-risk/) — the core metric being aggregated across desks
- [Delta](/delta/), [Gamma](/gamma/), [Vega](/vega/) — Greeks used in derivatives aggregation
- [Diversification](/diversification/) — the principle underlying risk aggregation math
- Correlation — the hidden assumption that breaks down in crises
- [Counterparty Risk](/counterparty-risk/) — another risk layer affecting aggregation
- [Stress Testing](/stress-testing/) — scenario-based aggregation that complements VaR

### Wider context

- [Dodd-Frank Act](/dodd-frank-act/) — post-2008 regulation driving firm-wide risk reporting
- [Basel III](/capital-adequacy/) — capital rules that depend on aggregated risk measures
- [Market Risk](/market-risk/) — the main risk type being aggregated
- [Operational Risk](/operational-risk/) — separate aggregation challenge not covered here

</div>
