---
title: "Yield to Call vs Yield to Maturity: What Callable Bond Investors Need to Know"
description: "How yield to call differs from yield to maturity for callable bonds and why the lower number is the conservative return estimate."
keywords:
  - yield to call
  - yield to maturity
  - callable bonds
  - bond yield calculation
  - fixed income
  - call risk
image: "/svg/fixed-income.svg"
---

*When you buy a **callable bond**, you face a hidden asymmetry: if interest rates fall, the issuer will almost certainly redeem the bond early at the call price, capping your upside. This is why bond investors track two yields—**yield to call** and **yield to maturity**—and rely on the lower of the two as the realistic return estimate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Yield to Call vs YTM — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Callable bonds force investors to choose between two competing return scenarios; the lower one is the prudent forecast.</div>

|   |   |
|---|---|
| **Yield to maturity (YTM)** | Assumes the issuer never calls the bond; you hold until final maturity |
| **Yield to call (YTC)** | Assumes the issuer calls the bond at the earliest call date |
| **Which is lower?** | YTC usually lower when rates fall (calling becomes profitable) |
| **Conservative estimate** | The *minimum* of the two figures |
| **Why it matters** | Misjudging yield costs money in a falling-rate environment |

</aside>

## What Makes a Bond Callable?

A [callable bond](/callable-bond/) gives the issuer the right to redeem it before maturity, usually at a predetermined price (the call price). Corporate bonds, many municipal bonds, and mortgage-backed securities often include call provisions.

The issuer's incentive is straightforward: if interest rates fall, issuing new debt becomes cheaper. The company can call in the old high-coupon bond and refinance at a lower rate, trimming its cost of debt. From the issuer's standpoint, a call option is valuable. From the investor's, it's a headwind.

## The Yield-to-Maturity Illusion

When you buy a bond, you often see a single yield number quoted: the **yield to maturity**. This is the internal rate of return assuming you hold the bond until its final maturity date and reinvest all coupon payments at that same yield. For a non-callable bond, YTM is a reliable number.

For a callable bond, YTM is misleading. It assumes the issuer will never exercise the call option—which is exactly what happens when rates *rise*. But in the most common scenario (falling rates), the assumption breaks down. The issuer will call the bond, and you won't hold it to maturity.

Example: A corporate bond maturing in 30 years, callable after 5 years, has a coupon of 6%. If interest rates have fallen and new bonds yield 4%, the YTM might show as 5.8%, inviting the investor to imagine nearly three decades of 5.8% returns. But the issuer will almost certainly call the bond in year 5.

## Calculating Yield to Call

**Yield to call** measures the return if the issuer calls the bond on the earliest call date. The calculation is identical to YTM, except:

- The final payment is the call price (not the par value at maturity), and
- The holding period ends on the call date, not the maturity date.

Formally:

**Bond Price = (Coupon / (1 + YTC)^1) + (Coupon / (1 + YTC)^2) + ... + ((Coupon + Call Price) / (1 + YTC)^n)**

where n is the number of periods until the call date.

Let's work an example:
- Par value: $1,000
- Coupon: 6% (annual payment: $60)
- Call price: $1,050
- Years to earliest call: 5
- Current price: $1,100 (trading at a premium)

To find YTC, we solve for the discount rate that makes the present value of five years of $60 coupons plus the $1,050 call price equal to $1,100:

$1,100 = $60/(1+YTC) + $60/(1+YTC)² + ... + ($60 + $1,050)/(1+YTC)⁵

YTC works out to roughly 4.5%. Meanwhile, if we calculate YTM (ignoring the call and assuming maturity in 20 years, with a final payment of $1,000), we might get 5.2%.

The investor should assume a 4.5% return, not 5.2%.

## Why the Lower Yield Matters

When a bond trades *at a premium* (above par), the bond has a coupon higher than current market rates. Falling rates make premiums bigger and make calling more likely. In this scenario, YTC will be lower than YTM.

When a bond trades *at a discount* (below par), the bond has a coupon lower than market rates. Falling rates shrink discounts. In this case, YTC and YTM converge, and the call is less likely to happen.

The rule of thumb: **if rates are falling and the bond is trading at a premium, use yield to call as your return estimate.** If rates are rising or stable and the bond trades at par or a discount, YTM is more useful.

## The Investor's Dilemma

By tracking yield to call, you're acknowledging a painful trade-off. If you buy a bond paying 6% and rates fall to 4%, two things happen:
1. The bond's price rises sharply (good for you).
2. The issuer calls it, and you must reinvest the proceeds at 4% (bad for you).

You lock in the low reinvestment rate, losing the opportunity to pocket the full price appreciation. This is [call risk](/call-risk/)—the asymmetry that investors must accept in exchange for higher coupon payments.

## Comparing the Two Yields: A Practical Example

| Scenario | YTM | YTC | Use this |
|----------|-----|-----|----------|
| Bond trading at premium; rates falling | 5.0% | 4.2% | YTC (4.2%) |
| Bond trading at discount; rates rising | 4.5% | 4.5% | Either (they converge) |
| Bond trading at par; rates stable | 4.8% | 4.8% | Either |
| Deep premium; high call probability | 6.0% | 4.8% | YTC (4.8%) |

## See also

<div class="wiki-seealso">

### Closely related

- [Callable Bond](/callable-bond/) — bonds with embedded call provisions
- [Call Risk](/call-risk/) — the risk that an issuer will redeem early
- [Coupon Payment](/coupon-payment/) — the periodic interest paid on bonds
- [Duration](/duration/) — how bond prices respond to interest-rate changes
- [Current Yield](/current-yield/) — simpler yield measure (coupon divided by price)

### Wider context

- [Bond](/bond/) — the fixed-income instrument itself
- [Interest Rate](/interest-rate/) — the rate environment that drives calls
- [Yield Curve](/yield-curve/) — the term structure across all bond maturities
- [Price Discovery](/price-discovery/) — how markets value securities

</div>
