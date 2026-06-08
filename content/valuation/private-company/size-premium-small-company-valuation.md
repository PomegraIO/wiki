---
title: "Size Premium in Small Company Valuation"
description: "How the size premium adjusts discount rates for micro-cap and private firms; empirical magnitude and academic debates about its validity."
keywords:
  - size premium small company valuation
  - small stock premium capm
  - micro-cap discount rate
  - private company discount rate adjustment
  - fama-french size factor
image: /svg/valuation.svg
---

*The **size premium** in small company valuation is an additional return premium historically demanded by investors for holding stocks of micro-cap and small-cap firms, reflecting their greater risk and liquidity constraints. When valuing a private company or micro-cap using CAPM, analysts add a size premium to the equity risk premium to justify a higher discount rate than large-cap peers.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Size Premium — key facts</div>

<img src="/svg/valuation.svg" alt="An abstract editorial mark for valuation." />

<div class="wiki-infobox-caption">Small-company stocks have historically traded at lower multiples than large-caps, justifying a higher required return.</div>

|   |   |
|---|---|
| **What it reflects** | Illiquidity, earnings volatility, and financial distress risk in smaller firms |
| **Typical range** | 2–6% annual premium, depending on market cap decile and data period |
| **Where it appears** | [CAPM](/capital-asset-pricing-model/) discount rate calculations for micro-cap and private valuation |
| **Decile breakdown** | Largest premium at 10th decile (smallest stocks); fades by 5th decile |
| **Academic dispute** | Academics debate whether historical premium persists or reflects measurement error |
| **Practical use** | Nearly universal in private equity and business appraisal; magnitude varies sharply by method |

</aside>

## Historical evidence for the size premium

From 1926 to 2024, small stocks have delivered higher average returns than large stocks. The Fama-French research team, studying U.S. equity returns across size deciles, found that the bottom decile (smallest 10% of firms by market cap) outperformed the top decile by roughly 2–6% annually, depending on the measurement period and methodology.

This outperformance was not smooth. The premium peaked in the 1980s and early 1990s, when small caps experienced a dramatic rally. It has been far less pronounced in the post-2000 era, especially after 2010. A practitioner valuing a private company in 2026 cannot assume that historical 1926–2024 averages still apply; the forward-looking premium is hotly contested.

The size premium appears across multiple geographies. Japanese, UK, and European exchanges have shown similar patterns—smaller stocks outperform large ones over decades, though the magnitude and consistency vary by country and period.

## Why smaller companies command a higher discount rate

Four factors explain why investors demand more return from small firms:

**Liquidity risk.** A small-cap stock trades less frequently, with wider bid-ask spreads. If you own a private company stake worth $10 million, you may wait months or years for a buyer, or face a steep haircut to close a deal quickly. Large-cap equity holders can exit within seconds. This illiquidity carries a real economic cost.

**Earnings volatility and business risk.** Smaller companies have less diversified revenue streams, fewer resources to weather downturns, and higher bankruptcy probabilities. A large firm like [JPMorgan Chase](/jpmorgan-chase/) can absorb a drop in one business line; a five-person software startup cannot. Higher earnings volatility requires a higher discount rate.

**Financial distress.** Small firms have less access to capital markets, higher borrowing costs, and tighter covenant constraints. A cash-flow shortfall forces more drastic action—layoffs, asset sales, default.

**Information asymmetry.** Public small caps file fewer materials than large firms; private companies disclose almost nothing. Valuation relies on unaudited financials, management interviews, and gut calls. This uncertainty commands a premium.

## Measuring the size premium: decile analysis

The Fama-French size factor breaks the market into ten deciles by market capitalization. The most granular empirical picture comes from the Fama-French data library, which tracks average returns and factors at decile level.

| Decile | Typical market cap range | Historical size premium vs. CAPM |
|--------|--------------------------|----------------------------------|
| 1 (largest) | $10B–$1T+ | Baseline (0% adjustment) |
| 2–3 | $5B–$10B | 0.2–0.5% |
| 4–6 | $500M–$5B | 1–2% |
| 7–8 | $100M–$500M | 2.5–4% |
| 9–10 (smallest) | <$100M | 4–6%+ |

Private companies below $50 million in revenue are often treated as decile 10, or even beyond it. Valuators then add a further "private company discount" of 20–35% (a separate adjustment capturing illiquidity, key-person risk, and lack of diversification).

The decile approach is empirically cleaner than a single "small-cap premium" number, but it requires judgment about which decile a private firm falls into. A $20 million revenue SaaS company might sit in decile 9, or valuators might argue it belongs even further out.

## Building a discount rate with the size premium

A standard CAPM discount rate looks like:

$$\text{Required Return} = R_f + \beta(R_m - R_f) + \text{Size Premium} + \text{Private Co. Risk Adjustment}$$

where:
- *R*_f is the risk-free rate (typically the 10-year Treasury)
- β is the firm's systematic risk (often assumed to match its industry or the market average if unleveraged)
- (*R*_m − *R*_f) is the historical [equity risk premium](/equity-risk-premium/), conventionally 5–6%
- Size premium is the decile adjustment (0–6%)
- The private-company risk adjustment is an additional illiquidity/key-person haircut (15–35%)

Example: Valuing a $30 million revenue consulting firm.
- Risk-free rate: 4.5%
- Market risk premium: 6%
- Beta: 1.2 (industry average)
- Size premium: 3.5% (decile 8–9)
- Private company adjustment: 25%

Discount rate = 4.5% + 1.2(6%) + 3.5% + 25% = **39.7%**

A 40% discount rate is severe but not unusual for early-stage or high-risk private firms. It reflects genuine economic risk.

## The academic challenge to the size premium

Since the early 2000s, researchers have questioned whether the historical size premium is real or statistical artifact.

**Survivorship bias.** The Fama-French database includes only stocks that survived to the present. Bankrupt small-cap firms are dropped. This overstates the returns of small-stock investors, who bore the full cost of failures. The true forward-looking premium may be lower.

**Data mining and factor drift.** Once Fama and French published the size factor, trading strategies were built around it. Capital chased the anomaly, bid up the smallest stocks, and compressed returns. What looked like a 4% annual premium in 1980–2000 might now yield 1% or less.

**Market structure changes.** Commission costs have collapsed, ETFs have made small-cap investing cheap, and information asymmetry has narrowed. Some argue these trends have eroded the economic rationale for a large premium.

**Empirical instability.** The size premium in Japan, Europe, and emerging markets is often negligible or even negative in recent decades. International data weakens the case for a universal, forward-looking premium.

Practitioners acknowledge these critiques but still apply a size premium in almost every private-company valuation. The reasoning: even if the historical premium has shrunk, the economic risk of small-cap and private firms remains real. A 1–2% premium on top of CAPM may be more defensible than a 4–6%, but abandoning the concept entirely seems to ignore the genuine illiquidity and volatility small-cap investors bear.

## Practical approaches to sizing the premium

**Historical decile approach.** Plug in the observed size premium for the relevant market-cap decile from Fama-French or similar databases. Transparent but backward-looking.

**Build-up method.** Estimate component risks—liquidity, earnings volatility, financial distress—independently, then sum them. More judgment-heavy but allows forward-looking adjustment.

**Comparable company analysis.** Look at earnings multiples paid for recent private acquisitions in the peer group, back out an implied discount rate, and see if the size premium implied by CAPM matches market practice. Often the two diverge.

**Venture-backed benchmarks.** If the firm has raised venture capital, use the valuation multiples from those rounds as a reality check. A Series A valuation at a 35% discount rate may be more credible than a theoretical CAPM calculation.

Many valuators blend these methods, starting with CAPM and then stress-testing against recent comps and transaction data.

## When to adjust the size premium

The baseline size premium can be modified for company-specific factors:

- **Exceptional competitive moat.** A small firm with durable pricing power and limited competition may deserve a lower premium than peers.
- **Concentrated customer base.** If the firm derives 50% of revenue from one customer, add a further concentration-risk adjustment on top of the size premium.
- **Strong management team.** Proven founders who have built profitable businesses before reduce key-person risk.
- **Leverage.** A small company with high debt faces more refinancing and default risk; increase the premium.

Size premium is a starting point, not a law of nature. The final discount rate reflects the analyst's credible judgment about the company's specific risk profile.

## See also

<div class="wiki-seealso">

### Closely related

- [Capital Asset Pricing Model](/capital-asset-pricing-model/) — Framework anchoring discount rate calculations with risk-free rate, beta, and equity risk premium
- [Equity Risk Premium](/equity-risk-premium/) — Historical and forward-looking return spread of stocks over bonds
- Fama-French Factor Models — Academic framework separating size, value, and profitability effects
- [Cost of Equity](/cost-of-equity/) — Systematic approach to estimating discount rate for valuation
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Method that applies discount rates to project future cash flows
- [Private Company Valuation](/private-equity-fund/) — Broader context for illiquidity adjustments and key-person risk

### Wider context

- [Business Valuation](/enterprise-value/) — Overall framework for assigning value to firms
- [Risk-Weighted Assets](/risk-weighted-assets/) — Alternative way of calibrating risk in financial institutions
- [Venture Capital Returns](/initial-public-offering/) — Market practice for sizing discount rates in early-stage equity
- [Merger and Acquisition Pricing](/acquisition/) — Comparable transaction data
- [Small-Cap Stock Investing](/stock/) — Investor perspective on small-stock returns and volatility

</div>
