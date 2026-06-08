---
title: "How to Estimate Volatility for a Real Options Model"
description: "Practical methods to estimate volatility for real-options valuation when the underlying asset is not traded, using proxies and simulation."
keywords:
  - estimate volatility real options
  - volatility non-traded asset valuation
  - implied volatility real options
  - volatility proxy real options
  - monte carlo volatility estimation
image: /svg/valuation.svg
---

*The biggest practical headache in real-options valuation is not the formula—it is the **volatility input**. When you value a stock [option](/option/), you can observe historical price swings or extract implied volatility from market quotes. But when you value an embedded option on a mining project, a pharmaceutical drug, or a production facility, the underlying asset does not trade. So **how to estimate volatility for a real options model** becomes a critical bottleneck, and the answer depends on what information you have and what you are trying to capture.*

## The Volatility Problem in Real Options

Real-options models often rest on [Black-Scholes](/black-scholes-model/) or binomial frameworks, both of which require an input: the annualized standard deviation (volatility) of returns on the underlying asset. For a stock, this is straightforward—download five years of daily prices, compute log-returns, annualize, and plug in. Done.

For a mining operation or a real estate development, there is no traded price to observe. The "underlying asset" is a bundle of uncertain cash flows. So volatility becomes a question: *uncertain with respect to what?* The answer shapes everything.

Volatility can represent:

- **Commodity price uncertainty**: For mining, the volatility of ore prices (copper, gold, lithium).
- **Demand/volume risk**: Hospital bed occupancy, project demand, market size.
- **Cost uncertainty**: Operating costs, construction delays, inflation.
- **Cash-flow volatility**: The aggregate standard deviation of net revenues across all sources.

Each interpretation leads to a different estimate, and the choice affects option value materially.

## Method 1: Proxy from Traded Comparables

If your real asset is similar to something that does trade, borrow its volatility.

**Example**: You are valuing a mining project that would extract copper. Copper futures and spot prices are traded every day. Download five years of daily copper prices, compute the annualized standard deviation of log-returns, and use that as the volatility input.

This works because:
- The underlying economic source of value (copper revenue) is directly observable.
- Historical price swings reflect real uncertainty in the commodity.
- The proxy is transparent and auditable.

**Limitations**: Copper price volatility over historical data is not the same as the volatility the project will face in the future, especially over a long development horizon. Volatility regimes shift. And if your project's cash flows depend on multiple commodities (a mining operation might produce gold, silver, and copper), you need to blend volatilities, accounting for correlation.

For diversified projects, a simple approach is to use the volatility of a diversified portfolio (e.g., an index of mining equities), which averages over multiple commodity exposures. This reduces specificity but improves stability.

## Method 2: Historical Cash-Flow Volatility

If you have a history of similar projects' cash flows, compute volatility directly.

Suppose your company has run three similar manufacturing plants for ten years each. For each year, you observe net operating cash flows. Concatenate these into a time series, compute annual percent changes, and calculate the standard deviation.

This approach:
- Captures real-world operational variability (demand swings, cost surprises, equipment downtime).
- Reflects the specific business, not a generic commodity.
- Includes correlations between multiple drivers.

**Caution**: Ten years of historical data is often insufficient to capture the tail of a distribution. A 1-in-20-year shock might not appear in your sample. And if the industry has changed (new competitors, technology shifts, regulatory changes), historical volatility may understate future uncertainty.

Also, observed cash flows are *ex-post* accounting numbers that include management's past decisions (adjustments, hedging, cost controls). The *ex-ante* volatility facing a new project may be higher because those levers haven't yet been pulled.

## Method 3: Simulation and Expert Judgment

When neither a traded comparable nor historical cash flows are available, **Monte Carlo simulation** bridges the gap.

Decompose the project's cash flows into components:

- **Commodity prices**: Oil at $X per barrel, gold at $Y per ounce.
- **Production volumes**: Capacity utilization, geological success rates.
- **Operating costs**: Labor, materials, energy.
- **Capex and financing**: Construction costs, interest rates.

Assign a **distribution** to each component based on engineering estimates, industry benchmarks, or expert judgment. For example:

- Oil price: lognormal, mean $70/bbl, standard deviation $15/bbl.
- Capacity utilization: triangular, low 60%, mode 80%, high 95%.
- Cost inflation: normal, mean 2%, std 1%.

Run thousands of simulations, drawing random values from each distribution and aggregating into annual project cash flows. Compute the standard deviation of the resulting cash-flow distribution. That is your volatility estimate.

**Strengths**:
- Transparent: You document each assumption.
- Flexible: Handles multiple sources of uncertainty.
- Specific: Tailored to the project's cost and revenue structure.

**Weaknesses**:
- Subjective: Each distribution choice requires judgment.
- Correlated components can be difficult to specify correctly (e.g., do oil prices and demand for oil-derived products rise together?).
- Time-consuming: A credible Monte Carlo model of a large project can take weeks.

## Method 4: Implied Volatility from Market Prices

If a similar project or company is traded (a public mining firm, an infrastructure fund), you can back out implied volatility from its stock price.

Use an option-pricing formula in reverse: observe the stock price today, its expected dividend yield, and the risk-free rate. If the stock also trades on options markets, use option prices to extract implied volatility. That rate of volatility, applied to your project, reflects the market's collective estimate of uncertainty.

This is powerful because it incorporates:
- Consensus expectations across many informed investors.
- Real-time feedback from trading activity.

**Drawback**: The stock's volatility includes financial leverage, management decisions, and portfolio effects unrelated to your specific project. A mining company's equity volatility is often much higher than the volatility of its underlying ore deposits because of debt and operational leverage. You may need to "unlever" the equity volatility and re-lever it to your project's capital structure.

## Blending Methods in Practice

Most valuation teams use a combination:

1. **Start with a traded proxy** (method 1) as a baseline.
2. **Sanity-check against historical cash flows** (method 2) if available.
3. **Adjust via simulation** (method 3) if the proxy seems materially misaligned with project specifics.
4. **Cross-reference market prices** (method 4) of similar assets.

A typical range for non-traded real assets is 20–60% annualized volatility, with:
- Stable utilities and infrastructure: 15–30%.
- Manufacturing and mining: 30–50%.
- Early-stage R&D and novel ventures: 50–100%+.

But never rely on a single number. A sensitivity analysis showing how option value changes across a volatility range (say, ±20% around your base case) is far more honest than a false-precision point estimate.

## Why Volatility Matters So Much for Option Value

A simple illustration: A real option with a strike price of $100 million, an underlying value of $110 million, and 3 years to expiration is in-the-money and worth roughly $12 million under low volatility (20% annualized). Under high volatility (50% annualized), it is worth nearly $20 million. The same project, with identical cash flows, yields a dramatically different valuation depending on the volatility assumption.

This sensitivity is why getting volatility right (or at least transparent) is critical. It is also why real-options models are sometimes criticized as exercises in assumption-tuning: small changes in volatility can swing the answer. The antidote is to be explicit about the volatility source and to test across plausible ranges.

## See also

<div class="wiki-seealso">

### Closely related

- [Real Options in Pharmaceutical R&D Valuation](/real-options-in-pharmaceutical-rd/) — How volatility is embedded in staged development decisions
- [Option to Stage an Investment: Phased Capital Commitment](/option-to-stage-investment/) — Volatility drives the value of the option to defer or proceed
- [Real Options in Mining Project Valuation](/real-options-mining-project-valuation/) — Practical example of volatility estimation for commodity-driven projects
- [Black-Scholes Model](/black-scholes-model/) — The standard formula that requires volatility as input
- [Historical Volatility](/historical-volatility/) — How to compute volatility from time-series data

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Static approach that sidesteps volatility by assuming a single forecast
- [Sensitivity Analysis in Valuation](/sensitivity-analysis-valuation/) — How to stress-test a valuation across parameter ranges
- [Value at Risk](/value-at-risk/) — Another framework for quantifying portfolio uncertainty

</div>
