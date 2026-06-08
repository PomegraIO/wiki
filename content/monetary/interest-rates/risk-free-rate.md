---
title: "Risk-Free Rate"
description: "The theoretical yield on a default-free investment, typically proxied by government debt or overnight repo, and the benchmark discount rate in valuation models."
keywords:
  - risk-free rate
  - government bonds
  - treasury yields
  - discount rate
  - capm
  - sovereign debt
image: /svg/monetary.svg
---

*The **risk-free rate** is the yield an investor receives on a default-free investment. In practice, no investment is entirely free of risk; instead, practitioners select a proxy—usually the yield on a government [bond](/bond/) of a stable state, or the rate on [overnight repo](/sofr/) backed by government collateral. The rate serves as the floor in valuation models: no risky asset should yield less than the risk-free return on average.*

## Why "risk-free" is a theoretical construct

Pure safety from default is unattainable. A bond issued by any government faces political, economic, and inflationary risk. But certain sovereigns have never defaulted and command markets deep enough to trade continuously. The US Treasury market is by convention treated as risk-free for USD-denominated contracts; German Bunds serve the same role for EUR; UK Gilts for GBP. The term "risk-free" actually means "free of credit risk" (not default), though it retains inflation and [interest-rate risk](/interest-rate-risk/).

The concept emerged in financial theory because models require a baseline. If every asset carried some default probability, you could not establish a floor for required returns. By treating one safe sovereign bond as risk-free, theorists carved out a reference point from which all other yields are measured as spreads.

## How practitioners choose a proxy

The choice depends on the valuation context and the currency of the cash flows:

- **Valuing a US firm**: Use the yield on a US [Treasury bond](/treasury-bond/) matching the forecast horizon (often the 10-year Treasury for a long-lived business).
- **Valuing a eurozone bank**: Use the German Bund yield (or increasingly, the overnight €STR rate for short-horizon valuations).
- **Private equity or project finance**: Use the government bond of the country where the asset operates, or apply a sovereign [credit spread](/credit-spread/) uplift if the borrower's [credit rating](/credit-rating/) is below the state.

Overnight rates ([SOFR](/sofr/), €STR, SONIA) have gained ground as risk-free proxies for short-term discounting, especially for derivative and swap valuations. These rates are backed by repo on government securities and reflect the lowest funding cost available to the banking system daily. For longer horizons, practitioners still default to nominal bond yields because overnight rates are volatile and term risk premium is material over years.

## The role in discounted cash flow and CAPM

In any [discounted-cash-flow valuation](/discounted-cash-flow-valuation/), the numerator is future free cash flows and the denominator is the [discount rate](/discount-rate/). The discount rate is typically built as:

Discount rate = Risk-free rate + Risk premium

The risk premium captures the additional return investors demand for bearing business, market, and operational risk. A mature, low-leverage utility might justify a 4–5% premium over the risk-free rate; a volatile growth startup might face a 12–15% uplift. The risk-free rate is the anchor. If it rises (because inflation expectations increase or the government's creditworthiness deteriorates), all valuations compress, and discount rates rise across the board.

In the [Capital Asset Pricing Model](/capital-asset-pricing-model/) (CAPM), the risk-free rate appears as the intercept:

Expected return = Risk-free rate + [Beta](/beta/) × Market risk premium

A stock's expected return is the risk-free rate plus its systematic risk (beta) times the average excess return of the market over the risk-free asset. Again, the risk-free rate anchors the entire framework.

## Why the choice of proxy matters and causes controversy

In periods of sovereign stress, the assumption of zero default probability breaks down. During the 2011 eurozone crisis, southern European government yields spiked because markets suddenly priced non-trivial default risk into Italian and Spanish bonds. Practitioners who had been using those yields as "risk-free" for local valuations had to scramble. Some switched to German Bunds (treating the entire EUR zone as homogeneous), others applied sovereign [credit spreads](/credit-spread/) to Bund yields as the best available proxy. The choice changes both the discount rate and the implied firm valuations.

More subtly, the risk-free rate rose significantly between 2021 and 2023 as inflation surged and [central banks](/central-bank/) tightened [monetary policy](/monetary-policy/). A 10-year US Treasury yielding 1% in early 2021 jumped to over 4% by 2023. For investors and analysts, this shift was mechanically painful: firms valued at low discount rates suddenly appeared overpriced at higher rates, and equities sold off. No change in business fundamentals occurred; only the risk-free anchor moved.

## Differences across markets and currencies

Each major economy has its own risk-free rate. The spread between government yields of different sovereign issuers reflects perceived differences in creditworthiness and currency risk. A US firm discounted at 4% (on the 10-year Treasury) will have a different enterprise value than an identical firm in a country whose government bonds yield 6%, all else equal. [Capital flows](/capital-flows/) and [currency risk](/currency-risk/) further complicate cross-border comparisons.

For emerging markets without a truly safe domestic bond, practitioners often use the US Treasury rate plus a sovereign credit spread—treating the emerging market's cash flows as if discounted in USD, then adjusted upward for the perceived default risk of the issuing country.

## See also

<div class="wiki-seealso">

### Closely related

- [Interbank Offered Rate Benchmark](/interbank-offered-rate-benchmark/) — Panel-bank survey rates that historically served as reference benchmarks, now superceded by risk-free overnight rates.
- [Interest Rate](/interest-rate/) — The cost of borrowing or return on lending, varying by tenor, credit quality, and currency.
- [Discount Rate](/discount-rate/) — The rate used to convert future cash flows into present value; typically risk-free rate plus a risk premium.
- [Treasury Bond](/treasury-bond/) — A government-issued bond, the closest practical proxy for a risk-free investment.
- [Credit Spread](/credit-spread/) — The additional yield above the risk-free rate that borrowers pay to compensate for default risk.
- [Secured Overnight Financing Rate](/sofr/) — The transaction-based overnight rate on Treasury-backed repo, increasingly used as the short-term risk-free benchmark.

### Wider context

- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — A method that values an asset as the present value of its future cash flows, requiring a risk-free rate to discount.
- [Price-to-Earnings Ratio](/price-to-earnings-ratio/) — A market valuation multiple often compared against implied returns from the risk-free rate.
- [Bond](/bond/) — A fixed-income security whose yield reflects credit risk, inflation expectations, and the prevailing risk-free rate.
- [Monetary Policy](/monetary-policy/) — Actions by the central bank to influence interest rates and inflation, affecting the risk-free rate over time.
- [Sovereign Debt](/sovereign-debt/) — The obligations of a government, whose yields anchor risk-free benchmarks by country.

</div>
