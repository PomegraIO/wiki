---
title: "How to Calculate a Bond's Price: Step-by-Step Example"
description: "A worked numerical example showing how to discount a bond's future cash flows to arrive at its fair market price using present-value math."
keywords:
  - how to calculate bond price example
  - bond pricing calculation
  - discount cash flow bond
  - bond present value
  - discounted cash flow fixed income
image: /svg/fixed-income.svg
---

*The **bond price calculation** starts with two facts: the cash flows the [bond](/bond/) will deliver (regular [coupon payments](/coupon-payment/) plus principal repayment) and the [discount rate](/discount-rate/) (the yield the market demands). Discount each cash flow back to today using that rate, add them up, and you have the bond's fair market price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">How to Calculate a Bond's Price — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Bond math is present-value math: future cash, discounted to today.</div>

|   |   |
|---|---|
| **Formula** | Price = Σ (Coupon / (1 + y)^t) + (Par / (1 + y)^n) |
| **Key inputs** | Coupon payment, par value, discount rate (yield), number of periods |
| **Result** | Fair market price per $100 of par value |
| **Intuition** | Higher discount rate → lower price; higher coupons → higher price |
| **Use cases** | Valuation, [yield-to-maturity](/yield-to-maturity/) calculation, relative trading |

</aside>

## The logic behind bond pricing

A bond is a stream of future cash: annual or semi-annual [coupon](/coupon-payment/) checks plus the return of principal at maturity. Today's fair price must balance two forces: the cash you'll receive and the opportunity cost of tying up capital.

If you pay $1,000 for a bond that delivers $50 per year for ten years plus $1,000 at the end, you are implicitly accepting a certain return. If the market demands a higher return (because interest rates have risen or risk has increased), that same bond is now worth less. Conversely, if the market demands a lower return, the bond is now worth more.

Bond pricing is the mechanical calculation that links coupon, par value, and market yield to arrive at that fair price.

## A worked example: $1,000 par, 5% coupon, maturing in 3 years

Assume a corporate bond with:
- **Par value:** $1,000
- **Annual coupon rate:** 5% (so annual coupon payment = $1,000 × 0.05 = $50)
- **Years to maturity:** 3
- **Market yield (discount rate) demanded:** 6% per year

At maturity, you receive the final coupon plus principal, so your cash flows are:
- Year 1: $50
- Year 2: $50
- Year 3: $50 + $1,000 = $1,050

Now discount each backward using 6% as the discount rate:

**Year 1:** $50 / (1.06)^1 = $50 / 1.06 = $47.17

**Year 2:** $50 / (1.06)^2 = $50 / 1.1236 = $44.50

**Year 3:** $1,050 / (1.06)^3 = $1,050 / 1.1910 = $881.68

**Sum:** $47.17 + $44.50 + $881.68 = **$973.35**

The bond's fair price is approximately **$973.35**, or **97.34 per $100 of par**. Since the coupon (5%) is lower than the market yield (6%), the bond trades at a discount to par. An investor is willing to accept a lower coupon rate *only if* they pay less upfront; the capital gain at maturity compensates for the shortfall in annual coupon income.

## What happens if the coupon equals the yield?

Now assume the same bond but with a 6% coupon (annual payment $60) and a 6% market yield:

- Year 1: $60 / 1.06 = $56.60
- Year 2: $60 / 1.1236 = $53.40
- Year 3: $1,060 / 1.1910 = $889.99

**Sum:** $56.60 + $53.40 + $889.99 = **$999.99 ≈ $1,000**

The bond trades at **par**. This is the equilibrium: if the coupon rate matches the market yield, today's buyer receives a fair return and pays the full par value.

## What happens if the coupon exceeds the yield?

Finally, a 7% coupon (annual $70) with a 6% market yield:

- Year 1: $70 / 1.06 = $66.04
- Year 2: $70 / 1.1236 = $62.31
- Year 3: $1,070 / 1.1910 = $898.86

**Sum:** $66.04 + $62.31 + $898.86 = **$1,027.20**

The bond trades at a **premium** to par. The high coupon income compensates the buyer for locking in below-market yield on the principal; the bond is worth more than $1,000.

## Semi-annual coupon bonds (the real world)

Most corporate and [Treasury](/treasury-bond/) bonds pay coupons semi-annually, not annually. The adjustment is straightforward: divide the annual coupon rate by two, and double the number of periods. For a 5% coupon bond with a 6% annual yield and 3 years to maturity:

- Semi-annual coupon = ($1,000 × 0.05) / 2 = $25
- Semi-annual yield = 6% / 2 = 3%
- Number of periods = 3 × 2 = 6

Then discount using the same formula with the semi-annual figures. The result is typically slightly higher (earlier coupons are discounted less) than the annual approach, but the difference is small.

## Using yield to maturity as the discount rate

In practice, when you see a bond quoted at "a 6% yield," that figure is the [yield-to-maturity](/yield-to-maturity/)—the discount rate that makes the bond's price equal to the cash flows you'll receive if you hold to maturity. It is circular: you calculate the bond price *by* using the yield as the discount rate, and the yield is defined as the rate that reconciles price and cash flows.

This means if you observe a bond's market price, you can back into the implied yield by solving the discounted-cash-flow formula for the rate. That's how traders and investors quickly assess whether a bond is a good relative buy.

## Price sensitivity to yield changes

A small change in yield causes a larger change in price for longer-dated bonds. A 3-year bond might fall 3% in price if yield rises by 1%; a 10-year bond might fall 8%. This sensitivity is called [duration](/duration/). High-[coupon](/coupon-payment/) bonds are less sensitive to yield moves than low-coupon bonds maturing at the same date because the high coupon income cushions the price decline.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield-to-maturity](/yield-to-maturity/) — The discount rate that defines the bond's current return
- [Coupon payment](/coupon-payment/) — The cash flow stream being discounted
- [Discount rate](/discount-rate/) — The percentage used to bring future cash to present value
- [Duration](/duration/) — How sensitive bond price is to yield changes
- [Par value](/par-value/) — The principal amount repaid at maturity
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — The broader valuation framework

### Wider context

- [Bond](/bond/) — The security being priced
- [Corporate bond](/corporate-bond/) — Common example bonds with credit risk
- [Treasury bond](/treasury-bond/) — Risk-free government bonds
- [Interest rate risk](/interest-rate-risk/) — Why bond prices move when yields change
- [Current yield](/current-yield/) — A simpler but less accurate yield metric
- [Yield curve](/yield-curve/) — How yields vary across maturity dates

</div>
