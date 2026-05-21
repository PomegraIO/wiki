---
title: "Extension Risk"
description: "Extension risk is the danger that a borrower will hold a loan or mortgage longer than expected when interest rates rise, forcing the lender to remain locked into a low coupon while rates elsewhere have increased."
keywords:
  - extension risk
  - rate lock risk
  - mortgage holding risk
  - duration extension
  - reinvestment opportunity loss
image: "/svg/risk.svg"
---

*Extension risk is the probability that a borrower will hold a loan or mortgage longer than expected — typically when interest rates rise — leaving the lender locked into a low-coupon investment while missing the opportunity to reinvest at higher rates. It is the inverse of [prepayment-risk](/prepayment-risk/) and represents the asymmetric exposure inherent in mortgages and [bonds](/bond/).*

<div class="wiki-hatnote">

This entry covers the risk that borrowers hold longer than expected. For the risk that they prepay early, see [prepayment-risk](/prepayment-risk/); for the risk that a [bond](/bond/) issuer repays it, see [call-risk](/call-risk/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Extension Risk — key facts</div>

<img src="/svg/risk.svg" alt="A calendar extending beyond the original maturity date, marked in red" />

<div class="wiki-infobox-caption">Rising rates lock lenders into low coupons longer than expected.</div>

|   |   |
|---|---|
| **What it is** | Risk that loan is held longer, locking in low rates while rates rise |
| **Most common in** | Mortgages; agency mortgage-backed securities; bonds with embedded optionality |
| **Trigger** | Rising interest rates; borrowers choose not to refinance |
| **Materializes when** | Rates rise after loan originated |
| **Opposite of** | [Prepayment-risk](/prepayment-risk/); rates falling instead |
| **Affects returns** | Caps upside if rates rise; extends duration and [interest-rate-risk](/interest-rate-risk/) |
| **Measured by** | WAL (weighted average life), option-adjusted spread (OAS) |

</aside>

## How extension risk works

You lend $400,000 to a homeowner at 3% rate, expecting a 15-year mortgage. Coupons of $12,000 per year seem attractive in the origination context.

But suppose interest rates rise to 6% within two years. The homeowner now faces a choice: refinance the 3% mortgage into a new loan at 6%, paying much higher monthly payments, or keep the low 3% mortgage. Almost all borrowers choose to keep it. From your perspective as the lender, you are now earning 3% while new mortgages yield 6%. You are stuck in a low-rate investment, and you cannot exit without taking a loss.

Moreover, the mortgage's **expected maturity** has extended. Homeowners holding low-rate mortgages often hold them for longer, pay them down slower, or sell their homes less frequently (because selling means giving up the low rate). The 15-year maturity becomes 20 or 25 years in practice. This is extension risk: you expected principal back in 15 years and can reinvest at higher rates then, but instead you must wait longer, trapped in low rates.

## The asymmetry of mortgage optionality

Extension risk is the asymmetric counterpart to [prepayment-risk](/prepayment-risk/). Together, they create a no-win situation for mortgage investors:

- When rates **fall**, borrowers prepay (exercise the option to refinance), and you get principal back to reinvest at low rates. This is bad for you.
- When rates **rise**, borrowers hold (extend), and you are locked into low rates while rates elsewhere are high. This is also bad for you.

The borrower holds the implicit option and exercises it in their favour. Rates fall? Prepay and refinance at lower rates. Rates rise? Hold and keep the low rate. The lender is short the option in both directions.

In markets with high [volatility](/stock-market/), this asymmetry is more pronounced, and the value of the embedded option is higher. This is why mortgage yields widen in high-volatility environments — compensation for the uncertainty about whether prepayment or extension will occur.

## Extension risk in agency mortgage-backed securities

Investors in mortgage-backed securities bear extension risk acutely. The stated maturity of an MBS is often 30 years, but the **expected weighted average life (WAL)** might be 5 years if refinancing rates are high. But if rates rise, WAL extends. The investor planned for principal in 5 years and reinvestment at high rates; instead, principal comes in 12 years, and rates have risen only slightly, negating the reinvestment benefit.

This mismatch between expected and actual maturity creates [duration](/interest-rate-risk/) uncertainty. A portfolio manager planning to hold MBS because they have a 5-year WAL finds that when rates rise (and they need the capital), the WAL is now 15 years. The portfolio's [interest-rate-risk](/interest-rate-risk/) has increased unexpectedly.

## The broader impact

Extension risk is part of why mortgages and mortgage-backed securities are riskier than they initially appear. A 3% mortgage might seem safe and liquid, but if rates rise 200 basis points, that mortgage becomes a liability — low-yielding, hard to sell, and locked in for longer than expected.

Pension funds and insurance companies holding large MBS allocations learned this lesson painfully in 2022, when rising rates caused mark-to-market losses on bonds they expected to hold to maturity. The combination of [interest-rate-risk](/interest-rate-risk/) (principal value down) and extension risk (maturity extended, locking in those losses longer) created double damage.

## Managing extension risk

Investors can limit extension risk through:

- **Avoiding mortgages and mortgage-backed securities.** Hold plain [bonds](/bond/) or Treasuries without embedded optionality. The trade-off is lower yield.

- **Buying mortgages with short expected maturity.** When rates are high relative to expectations, mortgages likely have short WAL and extension risk is lower.

- **Hedging with interest-rate futures or swaptions.** Short an interest-rate future or buy a swaption that pays off if rates rise, offsetting extension risk.

- **Laddering maturities.** A mix of short, medium, and long bonds smooths the reinvestment rate if maturities shift.

- **Understanding OAS.** Option-adjusted spread analysis prices the embedded option risk, allowing comparison across mortgages and callable [bonds](/bond/). A higher OAS indicates higher option risk (prepayment + extension).

For most individual investors, the practical defense is to limit exposure to mortgages and mortgage-backed securities to a small portion of the portfolio, and avoid them entirely if interest rates are unusually low (when extension risk is highest).

## See also

<div class="wiki-seealso">

### Closely related

- [Prepayment-risk](/prepayment-risk/) — opposite risk when rates fall
- [Interest-rate-risk](/interest-rate-risk/) — underlying driver of extension
- [Duration](/interest-rate-risk/) — extends with rising rates
- [Reinvestment-risk](/reinvestment-risk/) — consequence when duration extends
- [Bond](/bond/) — may carry extension risk if options embedded

### Broader context

- [Mortgage-backed security](/bond/) — classic example of extension risk
- [Volatility](/stock-market/) — increases value of embedded option
- [Interest-rate-risk](/interest-rate-risk/) — combines with extension for double impact
- [Federal Reserve](/federal-reserve/) — rate policy determines extension outcomes
- [Scenario analysis](/scenario-analysis/) — stress test portfolios for extension scenarios

</div>
