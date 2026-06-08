---
title: "Zero-Coupon Yield Curve Construction"
description: "Zero-coupon yield curve construction extracts spot rates from coupon bond prices using bootstrapping, revealing the true discount rate for any maturity."
keywords:
  - zero coupon yield curve construction
  - bootstrapping yield curve
  - spot rate extraction bonds
  - zero coupon curve bootstrapping
  - discount rate yield curve
  - coupon stripping methodology
---

*The **zero-coupon yield curve construction** process extracts spot rates—the true discount rates for each maturity—from the prices of coupon-bearing bonds. This mathematical technique, called bootstrapping, peels away the coupon payments to reveal what rate of return investors demand for lending money for exactly one year, two years, three years, and so on. The resulting zero-coupon curve serves as the foundation for virtually all fixed-income valuation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Zero-Coupon Yield Curve — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Spot rates reveal what plain lending actually costs.</div>

|   |   |
|---|---|
| **What it shows** | The discount rate for each maturity, isolated from coupon noise |
| **How it's built** | Bootstrapping: observed bond prices reveal spot rates step-by-step |
| **Starting point** | Shortest-maturity [bonds](/bond/) (Treasury bills, overnight rates) |
| **Key input** | Actual prices of coupon bonds across the maturity spectrum |
| **Output** | A spot rate for 1Y, 2Y, 3Y, 5Y, 10Y, 30Y, etc. |
| **Why it matters** | Discount-rate anchor for all fixed-income valuation |

</aside>

## Why coupon bonds can't directly tell you the discount rate

When you observe the price of a 10-year [Treasury bond](/treasury-bond/) paying a 3% coupon, you don't immediately know what discount rate drove that price. The price reflects a blend: some of the return comes from the coupon payments, some from the difference between purchase price and face value (if it's a discount or premium), and the timing of each cash flow matters.

To value a bond correctly, or to discount the cash flows of any fixed-income instrument (a [corporate bond](/corporate-bond/), a [mortgage](/fixed-rate-mortgage-personal/), a lease payment), you need a **spot rate** for each maturity: the actual rate of return demanded for lending for exactly one year, exactly two years, and so on. A coupon bond's price doesn't give you that directly. Instead, you must reverse-engineer the spot rates from observed bond prices—a process called bootstrapping.

## The bootstrapping process, step by step

Bootstrapping works sequentially, starting with the shortest maturities and working outward.

**Step 1: The one-year rate.** Start with a one-year Treasury bill or a one-year bond. A T-bill is a pure zero-coupon security—it pays no coupons, just face value at maturity. If a $100 one-year bill trades at $98, then the one-year spot rate is simply (100 / 98) − 1, or approximately 2.04%. This is your anchor point; there's no bootstrapping needed.

**Step 2: The two-year rate.** Next, observe a two-year coupon bond. Say it has a 2.5% coupon (so it pays $2.50 per year) and its current market price is $101. The bond will deliver $2.50 in one year and then $102.50 (coupon plus face value) in two years.

The one-year cash flow of $2.50 can be discounted using the one-year spot rate you just established (2.04%). That gives you $2.50 / 1.0204 = $2.45.

The two-year cash flow of $102.50 must be discounted at an unknown two-year spot rate. But you know that the bond's total price must equal the sum of the present values of both cash flows:

101 = 2.45 + 102.50 / (1 + r₂)²

Solving for r₂ (the two-year spot rate):

102.50 / (1 + r₂)² = 98.55

(1 + r₂)² = 102.50 / 98.55 = 1.0401

1 + r₂ = 1.0198

r₂ ≈ 1.98%

Now you have the two-year spot rate.

**Step 3: The three-year rate, and beyond.** A three-year coupon bond will pay coupons at years 1, 2, and 3. Discount the year-1 coupon using the one-year spot rate, the year-2 coupon using the two-year spot rate (which you just calculated), and solve for the three-year spot rate that makes the bond's current price equal the sum of discounted cash flows. This process repeats for every maturity along the curve.

## Why this approach reconstructs the true discount rates

The insight behind bootstrapping is that market prices are observable facts. If the market is willing to buy a two-year bond at a certain price, that price embeds the collective judgment of thousands of buyers about what return they demand. By starting from instruments with the fewest cash flows (one-year bills) and working toward more complex ones, you peel away each layer of timing and recover the underlying spot rate for each maturity.

The zero-coupon curve derived this way is sometimes called the **spot rate curve** or the **pure discount curve**. It represents, for each maturity, the interest rate you would receive if you lent money for that exact period and received no interest until the end. In other words, it answers the question: "What return does the market demand for zero-coupon lending at each maturity?"

## Using the zero-coupon curve for valuation

Once you have a zero-coupon yield curve, you can value any fixed-income security by discounting each of its cash flows at the appropriate spot rate. A corporate bond paying coupons at years 1, 2, 3, 4, and 5 would be valued as:

Bond Price = C₁/(1+r₁) + C₂/(1+r₂)² + C₃/(1+r₃)³ + C₄/(1+r₄)⁴ + (C₅+FV)/(1+r₅)⁵

where r₁, r₂, r₃, etc., are the spot rates you extracted from the Treasury curve (or another baseline curve).

This matters because it ensures consistency: you're using the market's own revealed preferences about the cost of borrowing at each maturity, not an arbitrary single discount rate that might misvalue long-dated cash flows.

## Coupon stripping and synthetic zeros

The bootstrapping process is conceptually distinct from coupon stripping, though they're related. In coupon stripping (sometimes called securitization), a dealer takes a single coupon-bearing Treasury bond and legally separates it into a package of zero-coupon instruments: one for each coupon payment and one for the final principal. These stripped securities, called STRIPS (Separate Trading of Registered Interest and Principal of Securities), trade separately. Their market prices provide direct observations of spot rates—no algebra required. These STRIP prices often serve as inputs to the bootstrapping process, confirming or refining the spot rates extracted from regular coupon bonds.

## Challenges and limitations

Real-world curve construction faces complications. Bonds don't exist at every maturity: the market might have liquid instruments at 1, 2, 3, 5, 10, and 30 years, but not 2.5 or 7 years. Practitioners use interpolation (fitting a smooth curve through observed points) to estimate spot rates at maturities where no traded bonds exist. The choice of interpolation method can affect results slightly, especially at the long end of the curve.

Bid-ask spreads and the changing composition of the Treasury market also introduce noise. A bootstrapped curve is only as accurate as the input prices, and prices can vary across dealers and venues. Professional traders and central banks smooth these inconsistencies using statistical methods and cross-checks against STRIP prices.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield Curve](/yield-curve/) — the relationship between maturity and interest rates
- [Spot Rate](/spot-rate/) — the actual discount rate for a specific maturity
- [Bond Valuation](/discounted-cash-flow-valuation/) — pricing fixed-income securities from their cash flows
- [Discount Rate](/discount-rate/) — the interest rate used to find present value
- [Treasury Bond](/treasury-bond/) — the baseline reference for constructing yield curves
- [Duration](/duration/) — how a bond's price changes when interest rates move

### Wider context

- [Fixed-Income Fundamentals](/bond/) — overview of debt securities and how they work
- [Coupon Payment](/coupon-payment/) — the periodic interest paid by bonds
- [Interest Rate](/interest-rate/) — what drives bond prices and yields
- [Mortgage-Backed Securities](/mortgage-backed-security/) — bonds backed by mortgages, often valued off the zero-coupon curve

</div>
