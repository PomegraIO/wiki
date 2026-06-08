---
title: "Probability of Default"
description: "Estimates the likelihood that a borrower will fail to meet obligations over a specified time horizon, typically one year."
keywords:
  - probability of default
  - default rate
  - credit risk
  - borrower creditworthiness
  - default prediction
image: /svg/risk.svg
---

*Probability of Default (PD) answers a straightforward question: what is the chance a borrower will fail to pay within a given period? It is the starting point for any credit risk calculation. Combine PD with [Loss Given Default](/loss-given-default/) (how much you lose if they do fail) and exposure size, and you have *expected loss*—the foundation of credit pricing and [capital-adequacy](/capital-adequacy/) regulation. PD varies wildly with borrower quality, economic conditions, and time horizon.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Probability of Default — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for credit risk." />

<div class="wiki-infobox-caption">The bedrock metric of credit risk: will the borrower pay or not?</div>

|   |   |
|---|---|
| **What it is** | Likelihood borrower defaults within a specified horizon (typically 1 year) |
| **Also called** | PD, default rate, credit probability |
| **Measured as** | Percentage, 0–100% (or decimal, 0–1) |
| **Key inputs** | [Credit rating](/credit-rating/), financial metrics, industry, economic outlook |
| **Counterpart** | [Loss Given Default](/loss-given-default/) — what you lose *if* default occurs |

</aside>

## What counts as default?

Before estimating probability, define what default is. The formal answer in banking and insurance regulation is straightforward: a borrower is in default if they are more than 90 days past due on any material payment (principal or interest). For bonds, default is a missed coupon or principal payment, or a declared bankruptcy. For loan portfolios, banks typically flag accounts as *delinquent* at 30 days past due and *defaulted* at 90 days past due.

But "default" is not always binary. In workouts and restructurings, a borrower might miss a payment (triggering technical default), negotiate new terms with the lender, and emerge with a modified loan. The accountant might record this as a default, but the economic loss might be zero. Modern credit risk frameworks distinguish between *technical default* (a payment was missed) and *economic default* (the creditor incurs a loss). PD estimates usually target economic default.

## Why estimate PD?

A lender's expected loss on a loan is:

$$\text{Expected Loss} = \text{PD} \times \text{LGD} \times \text{Exposure}$$

If you lend $1 million to a borrower with a 2% annual PD and an estimated [Loss Given Default](/loss-given-default/) of 50%, your expected loss is $10,000 per year. That expected loss should be covered by the loan's [coupon payment](/coupon-payment/) (interest). If the coupon is too low, you are not being compensated for credit risk. If the coupon is too high, you are pricing the borrower out of the market and will lose the deal to a competitor.

For banks and bond funds, PD is the foundation of credit pricing, [capital allocation](/capital-flows/), and [risk management](/market-risk/). A portfolio manager who misjudges PD by a factor of two—assuming 1% when the true PD is 2%—will systematically underprice credit and over-allocate to the riskiest names, slowly eroding returns until a default cycle arrives and real losses emerge.

## How PD is estimated: the big three methods

**Credit ratings**: The simplest approach is to delegate PD estimation to the [credit rating](/credit-rating/) agencies (Moody's, S&P, Fitch). Moody's publishes historical default rates for each rating category: AAA-rated bonds default roughly 0.0% per year, A-rated 0.1%, BBB-rated 0.3%, BB-rated 1–2%, and so on. A CCC-rated bond has a PD of 10–15% over one year. These are long-term historical averages (50+ years of data), smoothing out business cycles. A borrower rated A today is assigned the historical PD for A-rated names.

The appeal is simplicity. The problem: ratings are backward-looking and sticky. A company's financial health can deteriorate sharply while its rating remains unchanged, leaving your PD estimate too optimistic. Ratings also exhibit *procyclicality*: agencies downgrade en masse during recessions, just when the market has already sold off the bonds, offering no early warning.

**Structural models**: These estimate PD from the borrower's financial statements and market data. The idea is that a company defaults when its asset value falls below the value of its liabilities. If the company is highly leveraged (low equity value relative to debt), default is more likely. Models incorporate asset volatility, debt maturity, and macroeconomic forecasts to generate a forward-looking PD.

The most famous variant is the **Merton model**, which applies option-pricing theory: treat equity as a [call option](/call-option/) on the firm's assets, struck at the debt level. Solve for the implied asset volatility and asset value, then calculate the probability that assets fall below debt value before maturity. This generates a term structure of PDs (1-year, 5-year, 10-year), not just a single number.

Structural models are intellectually elegant and forward-looking. But they are sensitive to assumptions about asset volatility and require reliable market prices (for equities) or updated balance sheets (for private firms). For a mature company with stable financials, structural PD can be quite good. For a startup with lumpy cash flows, it is guesswork.

**Empirical models**: Lenders build their own models by regressing historical default patterns on borrower characteristics. Do smaller firms default more often? Companies in certain industries? Those with higher debt-to-income ratios? A logistic regression or machine-learning model can be fitted to historical data, generating a PD estimate for each new borrower based on their attributes.

Banks use empirical models constantly. A mortgage lender might estimate PD for a home loan based on FICO score, loan-to-value ratio, debt-to-income ratio, and geography. A credit card company uses spend patterns and payment history. These are usually proprietary and highly tuned.

## Cyclicality and stress

All three methods share a critical weakness: PD is not constant over time. It is cyclical. In good economic times, even weak borrowers are refinancing and paying down debt, so actual default rates plummet. In recessions, defaults spike. A portfolio built assuming an "average" PD of 3% might see actual defaults of 1% one year (when the economy is booming) and 8% the next (when unemployment soars).

This is why large banks now estimate *stressed PD*—the PD they should assume during a severe but plausible stress scenario. Regulators require this for [capital-adequacy](/capital-adequacy/) calculations. A stressed PD might be 2–3 times the historical average, reflecting the likelihood of default if GDP contracts sharply, unemployment spikes, and asset prices collapse.

## PD by borrower type

PD varies radically with the nature of the borrower:

**Sovereign debt**: Countries rarely default, but when they do, it is total. Historical annual PDs for developed sovereigns are near zero; emerging market sovereigns run 0.5–3% depending on historical track record and current imbalances.

**Investment-grade corporates**: [Credit rating](/credit-rating/)-AAA-rated companies have PDs of 0.01–0.1% per year. A-rated, 0.1–0.3%. BBB-rated (the lowest investment grade), 0.5–1.5%.

**Speculative-grade (junk) corporates**: BB-rated firms, 2–5%. B-rated, 5–10%. CCC-rated, 15–30%.

**Consumer credit**: Credit cards, auto loans, and personal loans have PDs ranging from 1% (prime credit) to 10–15% (subprime). Mortgage PDs for conforming loans are typically 0.5–2%; for jumbo or non-prime mortgages, 2–5%.

**Small businesses**: SME loans are harder to predict and historically default at 3–8% annually, depending on age, industry, and leverage.

## See also

<div class="wiki-seealso">

### Closely related

- [Loss Given Default](/loss-given-default/) — the complement; together with PD, determines expected credit loss
- [Credit Rating](/credit-rating/) — the primary input for PD estimation in most institutions
- [Credit Risk](/credit-risk/) — the broader category encompassing PD and LGD
- [Capital Adequacy](/capital-adequacy/) — regulatory capital is calculated using PD estimates

### Wider context

- [Corporate Bond](/corporate-bond/) — issued by borrowers with known PDs
- [Mortgage Backed Security](/mortgage-backed-security/) — pools of mortgages; portfolio PD is critical
- [Stress-Testing](/stress-testing/) — projections of defaults under adverse scenarios
- [Recession](/recession/) — default rates spike sharply during recessions

</div>
