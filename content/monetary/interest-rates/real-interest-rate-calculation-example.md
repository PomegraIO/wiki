---
title: "How to Calculate the Real Interest Rate: Step-by-Step Example"
description: "How to calculate real interest rate using the Fisher equation, with worked examples of ex-ante expected and ex-post realized rates."
keywords:
  - how to calculate real interest rate
  - fisher equation
  - nominal vs real interest rate
  - inflation adjustment
  - real interest rate formula
image: /svg/monetary.svg
---

*The **real interest rate** is what you actually earn (or pay) after accounting for [inflation](/inflation/). It differs from the nominal rate—what's quoted in the market—by subtracting expected or realized inflation. The classic way to calculate it is the **Fisher equation**: Real Rate ≈ Nominal Rate − Inflation Rate. This simple formula obscures a critical distinction: do you use inflation **expected before you lend**, or inflation **observed after the loan matures**? Both calculations are correct for different purposes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Real Interest Rate Calculation — key facts</div>

<img src="/svg/monetary.svg" alt="An abstract editorial mark for monetary policy." />

<div class="wiki-infobox-caption">Subtract inflation from the nominal rate to find what you truly earn.</div>

|   |   |
|---|---|
| **Fisher equation** | Real Rate = Nominal Rate − Inflation Rate |
| **Ex-ante (expected)** | Uses inflation forecast before the loan; guides investment decision |
| **Ex-post (realized)** | Uses actual inflation after the loan ends; reveals true historical return |
| **Exact formula** | (1 + Real) = (1 + Nominal) / (1 + Inflation); useful for large rates |
| **Quick approximation** | Real ≈ Nominal − Inflation; accurate for small rates (under 5% each) |
| **Why it matters** | Inflation erodes purchasing power; nominal rates can mislead about true value |

</aside>

## The Intuition

Imagine you lend $1,000 at a 5% nominal [interest rate](/interest-rate/) for one year. You receive $1,050 at maturity. But if prices rose 2% over that year, the $1,050 buys only what $1,029.41 would have bought a year ago (accounting for the 2% erosion of purchasing power). Your true gain, in terms of goods and services you can buy, is roughly 3%, not 5%.

That 3% is the **real rate**. The other 2% merely compensated you for inflation—for the fact that money itself lost value. A naive lender who ignores inflation and thinks they earned 5% in real terms has been fooled by inflation illusion.

## The Fisher Equation: Exact and Approximate Forms

The exact relationship between nominal rate (i), real rate (r), and inflation rate (π) is:

$$(1 + r) = \frac{1 + i}{1 + \pi}$$

Rearranging:
$$r = \frac{1 + i}{1 + \pi} - 1 = \frac{i - \pi}{1 + \pi}$$

For **small rates** (all of i, π, and r under ~5%), the denominator (1 + π) is close to 1, so the approximation becomes:

$$r \approx i - \pi$$

This is the simple Fisher equation most people use and remember.

## Ex-Ante vs. Ex-Post: A Worked Example

The critical choice is **when you measure inflation**.

### Scenario: A One-Year Bond

Suppose you buy a one-year Treasury bond with a 4% nominal yield. You must estimate the real return. Before you buy, inflation expectations in the market are 2% (based on surveys, inflation swaps, and Fed forward guidance). Using the ex-ante approach:

$$r_{ex-ante} = \frac{0.04 - 0.02}{1 + 0.02} = \frac{0.02}{1.02} \approx 0.0196 \approx 1.96\%$$

Or, using the simple approximation:

$$r_{ex-ante} \approx 4\% - 2\% = 2\%$$

This is your **expected real return** at the time of purchase. It guides your investment decision: am I satisfied with a 2% real gain?

Now, the bond matures a year later. Actual inflation turned out to be 3%—higher than expected, perhaps due to an unforeseen supply shock. Your **realized real return** is:

$$r_{ex-post} = \frac{0.04 - 0.03}{1 + 0.03} = \frac{0.01}{1.03} \approx 0.0097 \approx 0.97\%$$

Or, approximately:

$$r_{ex-post} \approx 4\% - 3\% = 1\%$$

You earned roughly 1% in real terms, not the 2% you expected. The bond paid you back, but inflation was worse than you bargained for, so your purchasing power gain was smaller. This is **inflation risk**: the gap between expected and realized inflation.

## A Table of Examples

Here are several scenarios, using the exact formula, to show how nominal rates, inflation, and real rates interact:

| Nominal Rate | Expected Inflation | Expected Real Rate (ex-ante) | Realized Inflation | Realized Real Rate (ex-post) |
|---|---|---|---|---|
| 4% | 2% | 1.96% | 2% | 1.96% |
| 4% | 2% | 1.96% | 3% | 0.97% |
| 4% | 2% | 1.96% | 1% | 2.97% |
| 7% | 5% | 1.90% | 5% | 1.90% |
| 2% | 0% | 2.00% | 2% | 0.00% |
| 0% | 2% | −1.96% | 2% | −1.96% |

The last row illustrates a painful scenario: if the nominal rate is 0% (a very low interest rate or a zero-coupon bond) and inflation is 2%, you lose purchasing power by simply holding the bond. Your real return is negative—you are being paid to lend, effectively, at a loss in real terms.

## Why the Distinction Matters

**For investors and savers**, the ex-ante real rate drives the decision to lend or save. If you expect a 2% real return but want 3%, you will not buy the bond at the current (4% nominal) price. The ex-ante real rate is the relevant opportunity cost.

**For economic analysis and history**, the ex-post real rate reveals how inflation surprises shaped actual wealth transfers. A borrower who locked in a 4% nominal rate may have benefited from higher-than-expected inflation (which eroded their real debt), while the lender was harmed. By computing the ex-post real rate, we can see who gained and lost.

**For [monetary policy](/monetary-policy/)**, central banks often discuss the "real fed funds rate"—the difference between the [federal funds rate](/federal-funds-rate/) and inflation expectations or realized inflation. If the Fed sets the nominal rate to 1% and inflation is 2%, the real Fed rate is roughly −1%, a very stimulative posture.

## The Reverse: Finding Inflation from Rates

Occasionally, you need to invert the formula. If you observe a nominal [Treasury bond](/treasury-bond/) yield and a [TIPS](/tips/) (Treasury Inflation-Protected Security) yield, you can back out the market's implied inflation expectation:

$$\pi_{implied} = i_{nominal} - i_{TIPS}$$

If a 10-year Treasury yields 4% and the equivalent TIPS yields 1.5%, the market is pricing in 2.5% inflation over the next decade. This is a direct read from market prices, not a survey or forecast, and it reveals what sophisticated investors collectively expect.

## Common Pitfalls

1. **Using the wrong inflation measure.** The choice of [CPI](/consumer-price-index/), core CPI, [PCE](http://www.bea.gov/) (Personal Consumption Expenditures), or another index matters. Different indices can diverge by 1–2% in any given year. Be explicit about which one you are using.

2. **Confusing ex-ante and ex-post.** If you are writing about investment returns in the past, you should use realized inflation (ex-post). If you are discussing market expectations or a portfolio decision today, use expected inflation (ex-ante).

3. **Ignoring compounding for large rates.** The approximation (nominal − inflation) breaks down when either rate is large. A 10% nominal rate and 8% inflation gives a real rate of 1.85% (exact), not 2% (approximation). For precision, always use the exact formula.

4. **Forgetting about taxes.** The real after-tax return is different again. If you earn 4% nominally but pay 25% tax on interest income, your after-tax nominal return is 3%, and then you subtract inflation. This is the return that matters for consumption.

## See also

<div class="wiki-seealso">

### Closely related

- [Real interest rate](/real-interest-rate/) — deeper conceptual treatment of the real rate in economic theory
- [Interest rate](/interest-rate/) — the nominal rates quoted in markets
- [Inflation](/inflation/) — the price-level change driving the adjustment
- [Inflation expectations](/inflation-expectations/) — how markets forecast inflation
- [TIPS](/tips/) — Treasury securities explicitly designed to protect against inflation

### Wider context

- [Federal funds rate](/federal-funds-rate/) — key nominal rate set by the Fed, which drives real rates indirectly
- [Central bank](/central-bank/) — manages monetary policy and inflation targets
- [Monetary policy](/monetary-policy/) — uses interest rate tools to influence real economic activity
- [Bond](/bond/) — primary instruments affected by real rate calculations
- [Discount rate](/discount-rate/) — uses real or nominal rates in valuation models

</div>