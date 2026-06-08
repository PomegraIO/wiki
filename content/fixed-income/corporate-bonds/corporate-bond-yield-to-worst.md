---
title: "Yield to Worst on Corporate Bonds"
description: "Yield to worst is the lowest yield a bondholder can earn if the bond is called, put, or matures early. It matters more than yield-to-maturity for callable corporate bonds."
keywords:
  - yield to worst corporate bond
  - ytw corporate bonds
  - callable bond yield calculation
  - bond yield to worst explained
image: /svg/fixed-income.svg
---

*The **yield to worst on corporate bonds** is the lowest yield an investor could actually realize if the bond is called (redeemed early by the issuer) before maturity. For any bond with a call or put feature, yield to worst is the realistic worst-case return, not the advertised yield-to-maturity. It directly addresses why callable bonds underperform when interest rates fall.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Yield to Worst — Key Facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Yield to worst protects investors from surprise reinvestment at lower rates after an early call.</div>

|   |   |
|---|---|
| **Definition** | Lowest yield across maturity, call date, or put date |
| **Applies when** | Bond is callable, putable, or has multiple redemption dates |
| **Why it matters** | Issuers call when rates fall; holders lose upside |
| **Calculation** | Test YTM at every possible redemption date, pick lowest |
| **Example scenario** | 6% bond, callable in 2 years at par, rates fall → likely called early |

</aside>

## What Makes a Bond Callable, and Why It Matters

A callable corporate bond gives the issuer the right to redeem (call) the bond at a specified price (usually par, sometimes higher) on or after a specified date. This feature benefits the issuer: if interest rates fall, the company can call the bond and refinance the debt at lower rates, just as a homeowner might refinance a mortgage.

But the bondholder bears the risk. When rates fall, the bond's price rises—standard inverse relationship. However, instead of enjoying the full capital gain, the call feature caps the upside. The issuer redeems the bond at the call price (usually $1,000), and the investor is forced to reinvest the proceeds at the new, lower market rates. The investor loses the opportunity to hold a high-coupon bond.

This is why a callable bond trading at a premium (price above par) is riskier than a non-callable bond with the same coupon and maturity. The premium can be capped by the call feature, yet the price can still fall if rates rise—downside is uncapped, upside is capped. Yield to worst quantifies the true return in the most conservative scenario.

## How to Calculate Yield to Worst

Yield to worst is calculated by testing the yield at every possible redemption scenario and picking the lowest result. For a simple callable bond, you would calculate:

1. Yield to maturity (assuming the bond is held to its stated maturity date)
2. Yield to the first call date
3. Yield to any intermediate call dates (if the bond is callable on multiple dates)
4. Yield to any put date (if the bondholder can force redemption)

Then you choose the lowest of these yields. That is the yield to worst.

**Worked example:**

- Bond: $1,000 par, 6% annual coupon ($60 per year), 5-year maturity
- Call feature: Callable at $1,000 starting in year 2
- Current market price: $1,100 (the bond is trading at a premium because its 6% coupon is attractive)
- Assume current market yield for similar bonds is 4.5%

Calculate yield to maturity (5 years):
Using a financial calculator or spreadsheet, the 5-year YTM is approximately 4.4% (the investor pays $1,100 upfront, receives $60 annually for 5 years, then $1,000 at maturity).

Calculate yield to first call date (2 years):
The investor pays $1,100, receives $60 annually for 2 years, then the bond is called and redeemed at $1,000. The YTC (yield to call) is approximately 2.3%.

Yield to worst = 2.3% (the call is likely, because the bond's coupon is above market; the issuer will call it to refinance).

The bond is advertised as a "5-year, 6% bond," but the realistic yield is only 2.3%, not 4.4%. This is the critical insight that yield to worst provides.

## Why Issuers Call Bonds: Economic Incentive

An issuer calls a bond when interest rates have fallen and the benefit of refinancing exceeds the call cost. If a company issued a 6% bond at par when rates were high, and rates later fall to 4%, the company can call the bond, pay off the holders at par, and refinance by issuing new bonds at 4%. The annual interest savings of 2% ($20 per $1,000) justifies the transaction cost of refinancing.

The bondholder, who was happy earning 6%, suddenly receives their $1,000 back and must reinvest at 4%. Over the remaining period of the original maturity, they earn less income. This is the reinvestment risk that yield to worst addresses.

## Callable vs. Non-Callable: The Yield Difference

A callable bond must offer a higher yield than an otherwise identical non-callable bond to compensate investors for the call risk. If both were priced at par, the non-callable bond would clearly be better (you'd earn the stated coupon for the full maturity). To make the callable bond attractive, it must offer more current yield (a higher coupon) to offset the risk of early redemption and reinvestment at lower rates.

This is why corporate bonds are typically callable and thus priced higher in yield than government bonds. Investors accept the call risk in exchange for higher coupons. Yield to worst is the tool to fairly compare a callable corporate bond to a non-callable Treasury bond of similar maturity.

## When Yield to Worst Equals Yield to Maturity

If a bond is trading below par (at a discount), the call feature is far less likely to be exercised. If a bond has a 4% coupon and current market yields are 6%, the bond trades below par and the issuer has no incentive to call it. The company is better off keeping low-cost debt. In this case, yield to maturity and yield to worst converge, because the maturity date is the realistic redemption date.

Only when a bond trades at a premium (coupon above current market yield) is the call feature a material threat. And only then does yield to worst diverge meaningfully from yield to maturity.

## Practical Implications for Bond Investors

When shopping for corporate bonds, never rely solely on the coupon or even yield to maturity. Always ask: Is this bond callable? If so, what is the call price, and when can it first be called? What is the yield to worst? A bond trading at $1,100 with a 6% coupon might seem attractive until you realize its yield to worst is 2.3% and it will likely be called in 2 years, forcing reinvestment at lower rates.

Conversely, a callable bond trading at a discount to par offers genuine safety. The call feature is unlikely to hurt you, and you can rely on the yield to maturity as a fair estimate of your return.

Yield to worst is the reality check that prevents "yield-chasing" investors from overpaying for bonds that sound attractive on paper but deliver disappointment in practice.

## See also

<div class="wiki-seealso">

### Closely related

- [How Corporate Bond Prices Move With Interest Rates](/how-corporate-bond-prices-move-with-interest-rates/) — Why prices rise when rates fall, and how calls prevent full upside
- [Duration for Corporate Bonds Explained](/bond-duration-for-corporate-bonds/) — How to measure the interest rate sensitivity of bonds
- [Corporate Bond Secondary Market](/corporate-bond-secondary-market/) — Where and how corporate bonds trade after issuance
- [Call Option](/call-option/) — The general mechanics of the call feature embedded in bonds
- [Coupon Rate](/coupon-rate/) — The stated interest payment on a bond

### Wider context

- [Corporate Bond](/corporate-bond/) — Full overview of corporate bond features and risks
- [Yield to Maturity](/yield-to-maturity/) — The standard YTM calculation and its limitations
- [Bond](/bond/) — General bond pricing and terminology
- [Refinancing Risk](/refinancing-risk/) — The issuer's motivation to call bonds when rates fall
- [Interest Rate Risk](/interest-rate-risk/) — How bonds are affected by market rate moves

</div>
