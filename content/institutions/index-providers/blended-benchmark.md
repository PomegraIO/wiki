---
title: "Blended Benchmark"
description: "A composite index created by combining two or more separate indexes at fixed weights to match a portfolio's target asset allocation."
keywords:
  - composite benchmark
  - benchmark allocation
  - multi-asset index
  - portfolio benchmark
  - tactical allocation
  - index weighting
image: "/svg/institutions.svg"
---

*A **blended benchmark** is a [benchmark](/wiki/sp-500-index/) constructed by combining two or more existing indexes at fixed weights, designed to reflect a portfolio's intended [asset allocation](/wiki/asset-allocation/). For example, a "60/40" portfolio might blend 60% of a domestic [stock index](/wiki/stock-market/) with 40% of a [bond index](/wiki/bond/), creating a single composite benchmark against which to measure the portfolio's returns and risks.*

## Why blend indexes instead of building one from scratch

A single monolithic index (like the [S&P 500](/wiki/sp-500-index/)) gives you broad [diversification](/wiki/diversification/) within one asset class, but [portfolio managers](/wiki/asset-allocation/) need to measure performance across multiple asset classes—equities, fixed income, real estate, maybe commodities. Rather than ask index providers to design a custom all-in-one index for every combination, the industry uses pre-built indexes and mixes them.

A blended benchmark formalizes this mix. It answers the question: "If I hold exactly this portfolio with these [allocations](/wiki/asset-allocation/), how should it perform?" By locking weights in advance, it becomes a stable measuring stick for manager performance, unambiguous for reporting, and transparent to clients and regulators.

## How blending works in practice

The construction is straightforward: select your component indexes, fix their weights (usually summing to 100%), and calculate the blended return as a weighted average.

A simple two-asset example:
- 60% [S&P 500](/wiki/sp-500-index/) (a broad US equity index)
- 40% Bloomberg Aggregate Bond Index (US [investment-grade bonds](/wiki/investment-grade-bond/))

The monthly return of the blended benchmark is 0.60 × (equity return) + 0.40 × (fixed income return).

Real institutional portfolios may blend five or more indexes:
- 45% US large-cap equity index
- 15% US small-cap equity index
- 10% international developed-market equity index
- 20% US [investment-grade bond](/wiki/investment-grade-bond/) index
- 10% emerging-market [bond](/wiki/bond/) index

Each component serves a specific purpose in the portfolio; the fixed weights embody the [asset allocation](/wiki/asset-allocation/) decision. When the portfolio drifts—perhaps equities rally and now represent 50% instead of 60%—the [fund manager](/wiki/actively-managed-fund/) uses the blended benchmark to identify that drift and decide whether to rebalance back to target.

## Where blended benchmarks fit in the fund industry

[Index funds](/wiki/index-fund/) and [ETFs](/wiki/etf/) use blended benchmarks to set and communicate expectations. A target-date retirement fund, for instance, typically promises "a 60/40 blend of stocks and bonds" or, more granularly, "weighted 80% equities (60% US, 20% international) and 20% fixed income." The blended benchmark operationalizes that promise.

[Actively managed funds](/wiki/actively-managed-fund/) use blended benchmarks as their primary performance hurdle. A multi-asset [hedge fund](/wiki/hedge-fund/) might target "outperformance of 60/40 equities/bonds," meaning the fund's returns are compared monthly to that exact blend. This makes performance measurable and client expectations concrete.

Institutional investors—pension funds, university endowments, insurance companies—construct custom blended benchmarks tailored to their exact investment policy and liability schedules. A pension fund with long-term obligations might use a benchmark that over-weights long-duration bonds; an endowment might include real-estate and private-equity allocations alongside public markets.

## Blended benchmarks versus tactical tilts

A blended benchmark fixes weights by policy. But markets move: equities rally and become overweight, or bonds fall and become underweight. When actual portfolio weights drift too far from the benchmark (often a 5% threshold), rebalancing brings them back in line. This mechanical rebalancing is often called "buy low, sell high"—it systematically profits from mean reversion when markets oscillate.

This differs from [tactical allocation](/wiki/asset-allocation/), where a manager deliberately tilts away from the benchmark—underweighting equities they believe are overvalued, overweighting bonds when yields spike—trying to outperform through market timing. A blended benchmark is a strategic, long-term statement; tactical tilts are short-term bets against it.

## Pitfalls and hidden complexity

**Index gaps:** A blended benchmark is only as good as its component indexes. If you blend a US equity index with an international bond index, you have a gap: US bonds and international equities are missing entirely. A naive investor might think the blend provides "total market exposure" when it actually has blind spots.

**Correlation changes:** The blended benchmark's risk profile depends partly on how its components move together. In normal times, stocks and bonds are negatively correlated—when equities fall, bonds often rise—which makes a 60/40 blend relatively stable. During financial crises, correlations often spike, and the blend becomes much more volatile than historical [volatility](/wiki/historical-volatility/) suggested. Index providers disclose this; investors often overlook it.

**Rebalancing drag:** Constant rebalancing to maintain the blend generates [trading costs](/wiki/bid-ask-spread/) and potential [capital gains tax](/wiki/capital-gains-tax-investor/) in taxable accounts. Very frequent rebalancing can hurt net returns, especially in sideways markets where the portfolio crosses thresholds repeatedly without making meaningful gains.

**Basis risk:** If a [fund](/wiki/mutual-fund/) is benchmarked to a blended index but holds slightly different securities (to reduce costs or for operational reasons), the fund's returns may drift from the benchmark even if the fund's managers are competent. This drift is called basis risk.

## Practical use by [asset managers](/wiki/asset-allocation/)

In investment management, the blended benchmark is a scorecard. If a 60/40 fund delivers a 7% annual return and its blended benchmark returned 6%, the manager earned a 1% "alpha"—value added above the benchmark. If the fund returned 5%, it delivered –1% alpha—an underperformance fee.

Clients pay close attention to this measurement. Institutional investors and fiduciaries are legally required to disclose and justify any fees; a manager underperforming the blended benchmark may lose assets to competitors using lower-cost [index funds](/wiki/index-fund/) that simply replicate the blend passively.

## See also

<div class="wiki-seealso">

### Closely related

- [Index Fund](/wiki/index-fund/) — fund that tracks a published index's methodology and constituents
- [Asset Allocation](/wiki/asset-allocation/) — portfolio construction balancing return and risk across asset classes
- [Stock Index](/wiki/stock-market/) — published index of equities used as benchmark or fund track
- [Bond](/wiki/bond/) — fixed-income security; indexes combine many bonds into a benchmark
- [Index Committee](/wiki/index-committee/) — governance body that oversees component index methodology

### Wider context

- [ETF](/wiki/etf/) — exchange-traded fund often structured to track a blended benchmark
- [Diversification](/wiki/diversification/) — spreading capital across uncorrelated securities to reduce risk
- Rebalancing — periodic adjustment of portfolio weights back to target allocation
- [Actively Managed Fund](/wiki/actively-managed-fund/) — fund measured against a blended benchmark; manager seeks outperformance

</div>
