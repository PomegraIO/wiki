---
title: "Nominal vs Real Cash Flows in DCF"
description: "Understand when to use nominal vs real cash flows in DCF models and how mixing them creates systematic valuation errors."
keywords:
  - nominal vs real cash flows in dcf
  - real cash flow valuation
  - inflation dcf
  - nominal discount rate
image: /svg/valuation.svg
---

*A discounted cash flow model requires internal consistency: if your cash flows are in future dollars (nominal), your discount rate must reflect expected nominal returns; if your cash flows are adjusted for inflation (real), your discount rate must too. Mixing nominal and real produces a systematic overvaluation or undervaluation—a difference that compounds across decades of projections.*

## Why the distinction matters

The question of **nominal vs real cash flows in DCF** turns on a single mechanical rule: the discount rate and the cash flows must measure the same thing. When you project revenues and costs forward, you can express them in two languages. Nominal cash flows include inflation. Real cash flows strip it out, showing what those flows are worth in today's dollars.

A retailer might forecast Year 10 revenue at $100 million nominal. Assuming 3% annual inflation over that decade, the same revenue in Year 10's purchasing power—its real value—would be roughly $74 million in today's money. The choice of which to project depends entirely on which discount rate you pair with it.

Most practitioners default to nominal. It mirrors how financial statements are reported, how analysts publish guidance, and how executives think about growth. But real cash flow models are equally valid and often clearer when inflation is a significant factor. The danger is not choosing one or the other—it is mixing them in the same spreadsheet.

## Nominal cash flows with nominal discount rate

Nominal cash flows are future dollars as they will actually appear in bank accounts or financial statements. If you forecast Year 10 revenue of $100 million nominal, that is the literal number a business will likely report. Similarly, a nominal discount rate (like a company's weighted average cost of capital) already prices in expected inflation. When you discount $100 million at a 10% nominal rate, you are implicitly asking: "What is a Year 10 dollar—which buys less than a today-dollar—worth today?"

This pairing is self-consistent. A 10% nominal discount rate assumes the investor requires 10% in an environment where, say, 3% is inflation and 7% is real return.

The advantage: fewer conversions. You work directly with the company's guidance, reported growth rates, and the analyst consensus that feeds into beta and cost-of-equity estimates. The disadvantage: over long projection periods (15+ years), compounding nominal inflation can obscure what is really happening to margins, capital intensity, and competitive position.

## Real cash flows with real discount rate

Real cash flows are expressed in purchasing power of the valuation date—today's dollars. If you believe Year 10 revenue will be $100 million nominal and you expect 3% average annual inflation, you project Year 10 real revenue as $100M ÷ 1.03^10 ≈ $74 million in today's money.

Pairing this with a real discount rate maintains consistency. A real discount rate is the return investors require above inflation. If nominal cost of equity is 10% and inflation is 3%, the real cost of equity is roughly (1.10 ÷ 1.03) − 1 ≈ 6.8%.

When you discount $74 million nominal revenue at 6.8% real, you are asking: "What is Year 10's purchasing power worth in today's purchasing power?"

The advantage: clarity. Margins measured in real terms reveal whether operational leverage is genuine or merely inflation-driven. Over a 30-year projection, you can visually see whether the company is becoming more or less efficient. The disadvantage: requires explicit inflation assumptions and more mental arithmetic.

## The systematic error of mixing

Suppose you project nominal cash flows but discount them at a real rate. You are saying: "These are Year 10 dollars, worth $100 million in nominal terms." Then you apply a 6.8% real discount rate, which assumes inflation is already stripped from the returns. This double-counts the erosion of purchasing power. The result: severe undervaluation.

Conversely, projecting real cash flows ($74 million) but discounting at the nominal rate (10%) overstates real purchasing power. It treats Year 10's already-deflated cashflow as if it were a full nominal dollar. Result: systematic overvaluation.

Neither scenario is a minor rounding error. In a 10-year valuation where inflation averages 3%, the difference between consistent pairs and a mixed pair can shift the enterprise value by 15–25%, depending on the rate and projection length.

## How to choose

**Start with the forecast.** If your base case revenue and margin assumptions come from management guidance or analyst consensus (which are intrinsically nominal), work in nominal terms. This is the typical path for most public-company valuations.

**Real is clearer for stress tests.** If you are asking "what if real margins decline?" or building a long-dated infrastructure or utility DCF where inflation-adjusted returns matter (because contracts often embed inflation escalators), real cash flows become easier to reason about.

**Be explicit about inflation.** The best practice is to state your long-term inflation assumption clearly—either in the nominal rate derivation (if you use nominal cash flows) or as an explicit deflator (if you use real). Avoid silently assuming zero inflation or treating nominal and real as interchangeable.

## Recovering from a mixed model

If you catch a mixed nominal/real error in an existing model, the fix depends on what you have. If the spreadsheet has nominal revenue/EBIT but has used a real discount rate, you must re-compute the discount rate in nominal terms (cost-of-equity, cost-of-debt, and WACC accounting for inflation expectations). If the cash flows have been deflated but the rates have not, normalize either the rates (convert to real) or the cash flows (convert to nominal).

The cleanest approach: keep one consistent model in nominal. Then, as a check, build a parallel real version using identical economic assumptions. If both are done correctly, they yield the same enterprise value. If they diverge, the error is in the inflation assumptions or the rate conversion.

## See also

<div class="wiki-seealso">

### Closely related

- WACC (Weighted Average Cost of Capital) — the discount rate used in nominal DCF models
- [Cost of Equity](/cost-of-equity/) — a component of WACC; estimated using beta and nominal risk-free rates
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the overarching framework for both nominal and real approaches
- [Inflation Risk](/inflation-risk/) — why inflation matters to valuation and how to model it
- [Interest Rate Risk](/interest-rate-risk/) — related to how discount rates change with inflation expectations
- [Adjusted Present Value vs WACC DCF](/adjusted-present-value-vs-wacc-dcf/) — alternative framing of leverage in DCF
- [Circular Reference Problem in DCF Models](/dcf-circular-reference-interest/) — a related structural issue in debt-heavy valuations

### Wider context

- Present Value — the foundational time-value concept
- [Gross Domestic Product](/gross-domestic-product/) — measures growth nominally and in real terms
- [Core Inflation](/core-inflation/) — how inflation is measured and forecasted
- [Monetary Policy](/monetary-policy/) — shapes inflation expectations and discount rates
- [Sensitivity Analysis in Valuation](/sensitivity-analysis-valuation/) — test how inflation assumption changes affect value

</div>
