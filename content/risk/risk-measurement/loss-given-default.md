---
title: "Loss Given Default"
description: "The fraction of a loan or bond exposure actually lost when a borrower defaults, accounting for recovery from collateral and liquidation."
keywords:
  - loss given default
  - lgd
  - recovery rate
  - credit loss
  - default loss
image: /svg/risk.svg
---

*Loss Given Default (LGD) estimates the percentage of exposure that is genuinely lost when a borrower fails to pay. It is not the same as [probability of default](/probability-of-default/)—which answers "will they fail?"—but rather "if they do fail, how much money do I lose?" The answer depends on what collateral backs the loan, what seniority the claim has, and how much can be recovered through bankruptcy proceedings. For credit risk models, LGD is as important as [probability of default](/probability-of-default/); together, they determine expected loss.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Loss Given Default — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for credit risk." />

<div class="wiki-infobox-caption">Measures the economic loss when a borrower defaults, net of recovery.</div>

|   |   |
|---|---|
| **What it is** | Percentage of exposure lost upon borrower default |
| **Also called** | LGD, loss rate, severity |
| **Complement** | [Probability of Default](/probability-of-default/) — the likelihood of default |
| **Measured as** | (Exposure - Recovery value) / Exposure, expressed as %, typically 0–100% |
| **Key driver** | Collateral coverage and seniority in [bankruptcy](/foreclosure/) hierarchy |

</aside>

## Default is not total loss

A common misconception is that default equals 100% loss. It does not. When a company defaults on its bonds, bondholders typically recover something—either through liquidation of the company's assets, through a restructuring deal in bankruptcy, or through sale to a buyer who assumes the obligations. The recovery amount, expressed as a percentage of the original exposure, becomes the LGD.

For a secured [mortgage](/fixed-rate-mortgage-personal/), LGD is usually modest. If a homeowner defaults on a $300,000 mortgage and the house is worth $250,000, the lender loses $50,000, yielding an LGD of roughly 17% ($50k / $300k). The collateral—the house—covers most of the exposure.

For an unsecured [corporate bond](/corporate-bond/), LGD can be much higher. If a company goes bankrupt, senior secured creditors (banks with liens on assets) recover first, secured bondholders recover second, and unsecured bondholders recover last, if at all. An unsecured bondholder might lose 50–80% of principal, yielding an LGD of 50–80%.

## The recovery process and its costs

LGD is not determined in a single moment. It emerges over months or years as the defaulted borrower moves through bankruptcy, restructuring, or workout proceedings. Several forces shape the final recovery:

**Collateral liquidation value**: If the loan is backed by specific assets (a piece of equipment, real estate, inventory), those assets are sold or applied to the debt. But sales in distress are rarely full-price; a foreclosed house sells at a discount, used manufacturing equipment fetches pennies on the dollar. The *liquidation value* is typically 50–80% of normal market value, depending on how quickly the sale must happen and how specialized the asset is.

**Priority in the capital structure**: In bankruptcy, [debt](/sovereign-debt/) is repaid in strict seniority order. First-lien mortgages on real estate rank high. Unsecured [bonds](/bond/) rank low. A first-lien lender might recover 90 cents on the dollar; an unsecured bondholder, 20 cents. The same borrower, two entirely different LGDs.

**Direct and indirect costs**: The bankruptcy process itself consumes resources. Lawyers, accountants, and advisors take large fees. Court proceedings delay recovery by years. For a small business, legal fees alone might consume 5–15% of asset value before any creditor is paid. For a large corporation, the percentage is smaller but the absolute amount substantial. These costs are ultimately borne by creditors.

**Economic conditions at the time of default**: An LGD estimate based on historical data reflects recovery rates during the periods included in that data. But recovery is cyclical. In a strong economy, a defaulted borrower's assets fetch high prices and the business might be salvageable by a buyer, lifting recovery rates (lowering LGD). In a severe recession, asset values plummet and buyers evaporate, gutting recovery rates (raising LGD). A portfolio with an estimated LGD of 40% during good times might see actual LGD of 65–70% when defaults cluster during a downturn.

## Estimating LGD in practice

Banks estimate LGD using three broad approaches:

**Historical observation**: Track actual defaults in the portfolio and measure what was recovered. If the bank has lost 100 mortgages over ten years, on average recovering 85% of principal before costs, historical LGD is 15%. This is the gold standard but requires large history (especially for rare, high-quality borrowers, where default samples are tiny).

**Market prices**: For traded [bonds](/bond/) and [credit swaps](/credit-spread/), the market price of a defaulted bond reflects expected recovery. If a bond in default trades at 40 cents on the dollar, the market is implying a 60% LGD. This is forward-looking but noisy—distressed debt markets have few buyers, spreads are wide, and prices can be stale.

**Loan-level fundamentals**: Lenders segment their portfolio by collateral type, seniority, and borrower credit quality, then estimate LGD for each segment based on historical recoveries in that segment. Mortgages on single-family homes in US metro areas might be assigned an LGD of 15%; commercial real estate loans, 35%; unsecured auto loans, 25%. These plug into regulatory formulas (e.g., Basel III [capital-adequacy](/capital-adequacy/) rules).

## Correlation with probability of default

LGD and [probability of default](/probability-of-default/) are not independent. They are correlated, especially at times of macroeconomic stress. In a boom, both [probability of default](/probability-of-default/) and LGD are low: few borrowers default, and those who do often have assets that fetch good prices. In a recession, [probability of default](/probability-of-default/) rises sharply, and LGD rises with it: asset values collapse, businesses fail in clusters, and recovery rates plummet.

This correlation creates a problem for simple [Value at Risk](/value-at-risk/) models. If you assume [probability of default](/probability-of-default/) and LGD are independent, you underestimate tail risk. Regulators and large banks have increasingly moved toward *stressed LGD* estimates—asking, "what LGD should I assume if default rates are at 90th percentile levels?"—rather than using historical averages. Stressed LGD is typically 20–40 percentage points higher than the long-run average.

## LGD across asset classes

LGD varies sharply by what is being financed:

**Mortgages**: US [residential real estate](/residential-real-estate/) [mortgages](/fixed-rate-mortgage-personal/) have historically low LGD (10–20%) because houses are hard to destroy and have stable demand. [Commercial real estate](/commercial-real-estate/) mortgages run higher (25–50%), especially for specialized properties.

**Auto loans**: Car loans have LGD of roughly 15–25%. Cars depreciate fast, but they have liquid secondary markets and collateral is well-documented.

**Corporate loans**: Secured corporate loans might have LGD of 25–45%; unsecured [corporate bonds](/corporate-bond/), 40–70%.

**Trade receivables**: Unsecured invoices due from a customer have high LGD (60–80%) because they rank low in bankruptcy and customers in distress delay payment.

**Credit card debt**: Unsecured, unsecured, unsecured. LGD runs 85–95% because recovery is minimal and write-off is fast.

## See also

<div class="wiki-seealso">

### Closely related

- [Probability of Default](/probability-of-default/) — the likelihood of default; combined with LGD, determines expected loss
- [Credit Risk](/credit-risk/) — the broader category; LGD is a component
- [Foreclosure](/foreclosure/) — the process through which mortgage LGD is realised
- [Bankruptcy](/foreclosure/) — the formal proceedings that determine LGD for corporate debt

### Wider context

- [Corporate Bond](/corporate-bond/) — debt for which LGD is a key consideration
- [Mortgage Backed Security](/mortgage-backed-security/) — pools of mortgages; average portfolio LGD is a critical metric
- [Stress-Testing](/stress-testing/) — stress scenarios should model higher LGDs in downturns
- [Capital Adequacy](/capital-adequacy/) — regulatory capital is calculated using LGD estimates

</div>
