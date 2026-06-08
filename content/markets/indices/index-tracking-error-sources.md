---
title: "Sources of Index Tracking Error in Index Funds"
description: "Why index funds diverge from their benchmark: sampling, costs, dividend timing, and securities lending explain most tracking error."
keywords:
  - index tracking error
  - index fund tracking error
  - index fund underperformance
  - benchmark tracking error
  - passive fund expenses
image: /svg/markets.svg
---

*An **index fund** aims to match its benchmark (the S&P 500, Total Market, etc.) as closely as possible, but it never returns exactly what the index returns. **Tracking error**—the standard deviation of the fund's returns versus the benchmark—stems from transaction costs, sampling, dividend timing, securities lending revenue, and fees. Most index funds track their benchmarks to within 0.05–0.15% annually.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Index Tracking Error — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for markets." />

<div class="wiki-infobox-caption">Multiple small frictions prevent perfect index replication.</div>

|   |   |
|---|---|
| **Typical tracking error** | 0.05–0.15% annually (varies by fund) |
| **Largest driver** | Management fees and operating costs |
| **Transaction cost drag** | 0.01–0.05% (buying/selling, bid-ask spreads) |
| **Dividend timing slippage** | 0.01–0.03% (reinvestment timing mismatch) |
| **Securities lending benefit** | +0.01–0.05% (revenue offsets some costs) |
| **Sampling vs full replication** | 0.02–0.10% depending on strategy |
| **Market impact** | Minimal for large, liquid funds |
| **Measurable cost** | Compare fund's actual return to index return |

</aside>

## The Core Problem: Perfect Replication Is Impossible

A true index contains hundreds or thousands of holdings in precise weights. Holding every stock in exact index weight would require a fund's cash to be infinitesimally small, zero trading costs, zero cash drag, and no fees. In reality, index funds must reconcile:

- **Management and operating costs** — salaries, compliance, custody, audits
- **Trading frictions** — bid-ask spreads, market impact, commissions
- **Cash drag** — money sitting uninvested awaiting dividends, redemptions, or new contributions
- **Reinvestment timing** — when and where dividends are reinvested
- **Sampling decisions** — which stocks to hold and in what proportion

The cumulative effect is **tracking error**: the fund's actual returns drift from the index's theoretical returns. Investors should expect this and understand which sources matter most.

## Expense Ratios and Management Fees

The single largest source of tracking error is the **expense ratio**. If an index fund charges 0.04% annually and the index itself (with zero costs) returns 10%, the fund returns 9.96%. That 0.04% gap is guaranteed and locked in.

**Expense ratios vary widely:**
- Vanguard S&P 500 ETF (VOO): 0.03%
- SPDR S&P 500 ETF Trust (SPY): 0.09%
- Fidelity S&P 500 ETF (FXAIX): 0.025%
- iShares Core S&P 500 ETF (IVV): 0.03%
- Passively managed large-cap index funds: 0.02–0.10%
- Actively managed funds (for comparison): 0.50–1.50%

The expense ratio is the starting point for tracking error. Everything below is either additional drag or, occasionally, slight benefit from securities lending.

## Transaction Costs: Bid-Ask Spreads and Market Impact

When an index fund buys or sells securities, it incurs transaction costs that the index does not:

**Bid-ask spreads.** Every stock trade involves a bid (what a buyer pays) and an ask (what a seller accepts). The spread is the markup—the difference. For large-cap, liquid stocks (Apple, Microsoft), the spread is tiny: fractions of a cent. For smaller stocks in the index, spreads can be 0.02–0.05% per trade. An index fund trading thousands of shares daily accumulates this friction.

**Market impact.** When a large fund buys a less-liquid holding, its order can move the price upward (slippage). Conversely, selling large blocks can depress price. The cost depends on the fund's size and the stock's liquidity.

For a fund tracking the S&P 500, these costs are minimal because the index is extremely liquid. For funds tracking small-cap or international indices, transaction friction is higher.

**Typical annual drag from transaction costs: 0.01–0.05%** depending on the fund's trading activity, index liquidity, and size.

## Dividend Timing and Reinvestment Slippage

Stock indices include dividends in their returns. When a company pays a dividend, the index calculation assumes it is immediately reinvested at the ex-dividend date price. But an index fund has two choices:

**1. Hold cash, wait to accumulate dividends, then reinvest quarterly or semi-annually.** During the holding period, the cash earns money-market rates (currently low, historically ~0–1%). The index assumes the dividend was reinvested immediately at the higher stock price. The fund's return lags.

**2. Reinvest dividends immediately but pay trading costs** to purchase new shares. Small transaction costs persist.

Most funds use a hybrid: they accumulate dividends in a sweep account earning modest interest, then reinvest on a regular schedule (daily, weekly, or monthly). The timing mismatch between the index's assumed reinvestment and the fund's actual reinvestment creates a small drag.

**Typical annual drag from dividend timing: 0.01–0.03%**, higher in periods of very low money-market rates.

## Sampling and Partial Replication

Some index funds do not hold all index constituents. Instead, they use **sampling**: selecting a subset of stocks that statistically represent the index's risk and return characteristics. This reduces trading costs and operational complexity.

For example:
- A fund might hold the 490 largest S&P 500 stocks and omit the smallest 10, reweighting slightly to match the index's sector and risk exposures.
- A total market fund holding 3,500 U.S. stocks might use a representative sample of 1,500 to 2,000 stocks, using statistical models to match the index's factor exposure (value, growth, momentum, size).

Sampling introduces **tracking error** if the selected stocks diverge from the omitted ones in performance. A fund omitting the 10 smallest-cap S&P 500 stocks will drift if those stocks outperform. Over decades, sampling drift compounds, though empirical studies show it is typically small (0.02–0.10% annually).

**Large-cap indices** are almost universally fully replicated because their constituents are few and liquid.
**Total market or small-cap indices** more often use sampling because holdings are numerous and less liquid.

## Securities Lending: A Benefit (Or Drag)

Many index funds lend out their securities to short-sellers and generate fee revenue. This revenue **offsets** some tracking error costs.

Here is how it works:
1. A short-seller wants to borrow Apple shares to sell them.
2. The index fund lends the shares and earns a fee (typically 0.01–0.10% of the borrowed value annually, higher if the stock is hard to borrow).
3. The fund credits this revenue against its operating expenses.

Example: A fund with a 0.06% gross expense ratio but 0.02% securities lending revenue reports a net expense ratio of 0.04%.

**Tracking benefit from securities lending: +0.01–0.05%** annually, though this varies by market conditions, index composition, and stock availability. In periods when stocks are easy to borrow, revenue is minimal. When stocks are hard to borrow (high short interest), revenue spikes.

Large funds (like Vanguard's flagship S&P 500 fund) often show tracking error smaller than the expense ratio because securities lending revenue is substantial.

## Cash Drag from Inflows and Redemptions

When investors pour money into an index fund faster than it is invested, or when redemptions require the fund to hold temporary cash, the uninvested balance earns money-market rates (low) instead of stock market returns (typically higher). Similarly, funds hold a small cash buffer to meet daily redemptions without forced selling.

**Typical cash drag: 0.01–0.05%** depending on the fund's size, the market environment, and the inflow/outflow pattern. Very large funds can minimize this; smaller or hot-money flows incur more.

## Measurement and Benchmarking

Tracking error is measured as the **standard deviation of the fund's returns minus the index's returns** over a rolling period (typically 3 years or 5 years). 

For example:
- Index return (Year 1): +10.00%
- Fund return (Year 1): +9.95%
- Tracking error that year: −0.05%

Over many years, these deviations compound. A fund with 0.10% annual tracking error will lag the index by roughly 0.10% per year (0.20% over two years, 0.50% over five years), though the exact amount depends on whether tracking error is consistent or volatile.

**Real-world examples of published tracking errors (as of 2024):**
- Vanguard Total Stock Market ETF (VTI): 0.03% vs benchmark
- SPDR S&P 500 ETF Trust (SPY): 0.08% vs S&P 500
- Fidelity ZERO Total Market Index Fund (FZROX): 0.05% vs CRSP U.S. Total Market Index

Even the smallest tracking errors of 0.03% represent hundreds of millions of dollars in lost wealth across millions of shareholders—a testament to how sensitive compound returns are to small annual frictions.

## Why Some Funds Track Better Than Others

**Size matters.** A $300 billion S&P 500 fund (like Vanguard's VOO) can negotiate cheaper securities lending, lower custody fees, and economies of scale. A small fund with $5 billion has less bargaining power and proportionally higher fixed costs.

**Index construction.** Large-cap, liquid indices (S&P 500, Nasdaq 100) track nearly perfectly; their constituents are abundant and cheap to trade. Small-cap or emerging-market indices incur larger tracking error because fewer shares trade daily.

**Fee discipline.** Vanguard's investor-owned structure gives it incentive to minimize fees and maximize shareholder value. Mutual funds and ETFs operated by for-profit managers prioritize profits, so expense ratios are higher.

**Securities lending aggressiveness.** Funds that actively lend securities capture more revenue and offset costs more effectively.

## See also

<div class="wiki-seealso">

### Closely related

- [Index Fund](/index-fund/) — What an index fund is and how it works
- [Expense Ratio](/expense-ratio/) — The largest driver of tracking error
- [Bid-Ask Spread](/bid-ask-spread/) — Transaction cost structure in markets
- [Active vs Passive Investing](/actively-managed-fund/) — Comparison of costs and expected returns
- [Dividend Yield](/dividend-yield/) — How dividends affect index fund returns

### Wider context

- [Securities Lending](/mortgage-reit/) — How funds generate revenue from loanable assets
- [Market Making](/market-maker-trading/) — Understand why bid-ask spreads exist
- [Liquidity Risk](/liquidity-risk/) — How fund size and index composition affect trading costs
- [Portfolio Rebalancing](/asset-allocation/) — Why frequent trading increases friction

</div>
