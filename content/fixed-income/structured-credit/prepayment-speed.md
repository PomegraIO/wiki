---
title: "Prepayment Speed"
description: "The rate at which mortgage borrowers repay principal ahead of schedule, measured by PSA or CPR conventions and critical to mortgage-backed security valuation."
keywords:
  - mortgage-backed-security
  - prepayment-risk
  - mortgage-reit
  - structured-credit
  - fixed-income
  - bond-valuation
image: /svg/fixed-income.svg
---

*[Mortgage-backed securities](/mortgage-backed-security/) are fundamentally dependent on how quickly homeowners repay their loans. **Prepayment speed** is the annualized rate at which borrowers return principal early, measured in two industry standard formats: the CPR (Conditional Prepayment Rate) and the PSA (Public Securities Association) model. CPR is the simplest—a single percentage, like "20% CPR" means borrowers are repaying 20% of the remaining principal balance per year. PSA is a ramp: it starts at 0.2% in month one, rises by 0.2 percentage points each month until it reaches 6% in month 30, then stays flat. Actual prepayment speeds matter enormously because they determine cash flow timing, [duration](/duration/), and the value of [mortgage derivatives](/mortgage-backed-security/) like [interest-only strips](/interest-only-strip/) and [principal-only strips](/principal-only-strip/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Prepayment Speed — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the fixed-income topic." />

<div class="wiki-infobox-caption">The pace at which homeowners repay mortgage principal, driving cash-flow timing and bond price volatility.</div>

|   |   |
|---|---|
| **What it is** | The annualized rate of principal repayment (both scheduled and early) as a percentage of outstanding balance |
| **Also called** | CPR (Conditional Prepayment Rate), PSA speed, turnover rate |
| **Measured as** | CPR: single percentage per year; PSA: ramp from 0.2% to 6% over 30 months, then flat |
| **What drives it** | Interest rates, [refinancing](/refinancing-risk/) incentive, home prices, seasonality, borrower behaviour |
| **Why it matters** | Affects [duration](/duration/), cash-flow timing, [option-adjusted spread](/interest-rate-risk/) valuation |
| **Key relationship** | Lower rates → faster prepayment; higher rates → slower prepayment |
| **Used by** | [Mortgage REITs](/mortgage-reit/), portfolio managers, [securitization](/securitization/) dealers, risk models |

</aside>

## CPR: The simple annual rate

The simplest measure is the **Conditional Prepayment Rate** (CPR). It is the annualized percentage of the remaining mortgage balance that is repaid as principal in a given period, excluding scheduled amortization. If a pool has an outstanding balance of USD 1 billion and USD 100 million is prepaid in a month (excluding the regular amortized principal), the monthly CPR is 12% (USD 100 million ÷ USD 1 billion ÷ 1 month × 12 months).

In practice, investors quote CPR for a given pool or in a market context ("The market is pricing in 25% CPR") to describe the speed assumption. A 6% CPR is very slow (prepayment is minimal, meaning rates are high or borrowers have little incentive to refinance). A 40% CPR is very fast (rates have fallen sharply, or there is significant turnover for other reasons like property sales). CPR is not the same as [mortgage turnover](/mortgage-reit/) or default rate; it is strictly the voluntary prepayment of principal.

## PSA: The standardized ramp

The **Public Securities Association** model is a historical standard that creates a shape rather than a single number. It assumes prepayment ramps up as mortgages age (because the pool matures and refinancing becomes more likely) and levels off after 30 months. The model starts at 0.2% CPR in month one and adds 0.2 percentage points each month, reaching 6% CPR in month 30, and then holds flat at 6% thereafter.

Investors then quote multiples of this model: "100% PSA" means the speed follows the standard ramp exactly; "150% PSA" means the speed is 1.5× the ramp (so 0.3% CPR in month one, reaching 9% in month 30); "50% PSA" means half the standard ramp (so 0.1% CPR in month one, reaching 3% in month 30).

PSA was useful when [mortgage-backed securities](/mortgage-backed-security/) were simpler and less transparent. It imposed structure on an otherwise arbitrary forecast. Modern dealers often estimate PSA as a shorthand for market expectations, but many also build more sophisticated [refinancing](/refinancing-risk/) models that account for current rates, [rate volatility](/historical-volatility/), and borrower-level data.

## What drives prepayment speed

The primary driver is the gap between the mortgage coupon (the rate borrowers are paying) and current market rates. If you are paying 4% on a mortgage and rates drop to 3%, you have a strong incentive to refinance. If rates rise to 5%, you have zero incentive. The difference (called the *refinancing incentive* or *refi wave trigger*) is the most predictable force on prepayment speed.

Beyond rates, other factors matter:
- **Home price appreciation.** Rising home values increase [equity](/equity-financing/), making it easier to refinance or sell.
- **Seasonality.** Spring and summer see more home sales and refinancings than winter.
- **Loan age.** Very young mortgages (month 1–6) prepay slowly because borrowers rarely refinance immediately after origination. Older mortgages have more turnover.
- **Borrower credit quality.** A pool of prime mortgages may prepay faster than a pool of subprime mortgages (assuming rates fall equally) because prime borrowers have better access to refinancing.
- **Economic cycles.** In recessions, unemployment rises and prepayment slows because homeowners with job uncertainty defer refinancing even if rates favour it.

The relationship is not perfectly predictable. In March 2020, for example, rates fell sharply, but [mortgage REITs](/mortgage-reit/) experienced slower-than-expected prepayment for several months because lenders delayed closings due to pandemic lockdowns. Model assumptions broke, and bond prices moved unexpectedly.

## Duration and the prepayment trap

The reason prepayment speed matters so much is [duration](/duration/). A [mortgage-backed security](/mortgage-backed-security/) issued at par with a 4% coupon and a 30-year maturity doesn't actually have 30-year duration. If prepayment is 6% CPR (very slow), the effective duration might be 7 years. If prepayment is 50% CPR (very fast), effective duration might be 2 years. The same bond, same coupon, wildly different interest-rate sensitivity depending on the prepayment assumption.

This is called *negative convexity*: when rates fall, prepayments accelerate, shortening duration, capping the bond's price appreciation. When rates rise, prepayments slow, extending duration, magnifying price loss. An investor who buys an [MBS](/mortgage-backed-security/) expecting 5 years of duration can wake up with 8 years when rates rise unexpectedly and refinancing dries up.

[Interest-only strips](/interest-only-strip/) and [principal-only strips](/principal-only-strip/) are extreme cases: their returns are entirely dependent on prepayment speed forecasts.

## Modeling prepayment speed

Modern [securitization](/securitization/) teams and [mortgage REITs](/mortgage-reit/) build detailed refinancing models. These typically:
1. Calculate the refinancing incentive (current rates vs. mortgage coupon, adjusted for refi costs).
2. Estimate the probability that a borrower in each [segment](/segment-reporting/) (by loan age, credit score, state, etc.) will refinance.
3. Add a lag (borrowers don't refinance instantly even if it's profitable).
4. Run the scenario through a cash-flow model to compute [option-adjusted spread](/interest-rate-risk/) and price.

The models improve with historical data and can be backtested against past prepayment performance. However, they are not crystal balls. A sudden rise in home prices, a change in lender lending standards, or an economic shock can break historical relationships and cause large forecast errors.

## Market pricing and spread risk

When [mortgage-backed securities](/mortgage-backed-security/) trade, dealers quote a price, yield, and implied prepayment speed. A dealer might offer an [MBS](/mortgage-backed-security/) at "par +2, 95 CPR"—meaning at par plus 2 points, the dealer is assuming 95% PSA prepayment. If the actual prepayment turns out to be 150% PSA (much faster), the bondholder will receive cash back sooner at lower reinvestment rates, and the total return will disappoint. If prepayment is 50% PSA (much slower), the bondholder is stuck with a longer-duration bond in a rising-rate environment, and price declines.

This is *prepayment risk* or *model risk*. Even if you buy a [mortgage security](/mortgage-backed-security/) at a fair [option-adjusted spread](/interest-rate-risk/), if the market's prepayment assumption is wrong, you lose.

## See also

<div class="wiki-seealso">

### Closely related

- [Mortgage-Backed Security](/mortgage-backed-security/) — the bond whose cash flow is shaped by prepayment speed
- [Interest-Only Strip](/interest-only-strip/) — the derivative that loses value as prepayment accelerates
- [Principal-Only Strip](/principal-only-strip/) — the derivative that gains value as prepayment accelerates
- [Duration](/duration/) — the interest-rate sensitivity measure heavily impacted by prepayment
- [Option-Adjusted Spread](/interest-rate-risk/) — the valuation framework that inputs prepayment assumptions
- [Refinancing Risk](/refinancing-risk/) — the risk that borrowers refinance when rates fall

### Wider context

- [Mortgage REIT](/mortgage-reit/) — institutional investor heavily exposed to prepayment speed changes
- [Securitization](/securitization/) — the bundling of mortgages that introduces prepayment variability
- [Bond](/bond/) — basic fixed-income security and valuation framework
- [Negative Convexity](/duration/) — the price asymmetry caused by prepayment optionality
- [Yield-to-Maturity](/yield-to-maturity/) — misleading for mortgages because prepayment changes the actual maturity

</div>
