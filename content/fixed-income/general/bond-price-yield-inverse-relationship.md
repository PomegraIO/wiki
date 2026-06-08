---
title: "Why Bond Prices and Yields Move in Opposite Directions"
description: "The inverse relationship between bond prices and yields is arithmetic: when market interest rates rise, older bonds with lower coupons become less attractive, so their market prices fall."
keywords:
  - bond prices yields inverse relationship
  - why bond prices fall when yields rise
  - bond pricing mechanism
  - interest rate and bond price
image: /svg/fixed-income.svg
---

*The **inverse relationship between bond prices and yields** is not a mystery—it follows from pure arithmetic. When market interest rates rise, an existing bond paying a fixed coupon becomes less attractive than a newly issued bond paying higher interest. The old bond's price must fall to make its yield competitive. The opposite happens when rates drop: old bonds with higher coupons become more valuable. Walk through a concrete example and the mechanism becomes clear.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bond Price-Yield Relationship — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed income." />

<div class="wiki-infobox-caption">Fixed coupon, flexible price: the bond market adjusts price to match the yield environment.</div>

|   |   |
|---|---|
| **Core principle** | Bond price and yield are inversely related |
| **Why** | A bond's coupon payment is fixed; price adjusts to equate the return |
| **Market driver** | Changes in prevailing interest rates |
| **Magnitude** | Longer-maturity bonds see bigger price swings for the same rate move |
| **Yield measure** | [Yield-to-maturity](/yield-to-maturity/) (YTM) is the relevant rate |
| **Price reference** | Par value ($1,000 for most corporate and Treasury bonds) |

</aside>

## The Coupon Payment Never Changes

A bond is a contractual obligation. Issuer promises: "Pay the bondholder X% of par value every six months (the coupon), and return the principal at maturity." That X% is locked in at issuance and never changes. A 10-year corporate bond issued with a 4% annual coupon pays 2% of par ($20 per $1,000 bond) every six months for ten years, regardless of what happens to the economy, the issuer's credit, or market interest rates.

But the bond's *price*—what you pay to buy it on the secondary market—is not fixed. It fluctuates based on what other investors are willing to pay. And here is the key: the bond's price moves to keep its return competitive with prevailing interest rates.

## The Worked Example: A Bond Issuance and a Rate Shock

Imagine the day an issuer floats a new 10-year bond:
- Par value: $1,000
- Coupon: 4% ($40 per year, or $20 every six months)
- Market [yield-to-maturity](/yield-to-maturity/) at issuance: 4%
- Price: $1,000 (par)

An investor buying at par receives a 4% annual return—the coupon yield matches the market rate. This is the starting point.

Now, three months later, market interest rates have spiked. The Federal Reserve has raised rates; new 10-year bonds are being issued with a 5% coupon. The investor holding the original 4% bond thinks: "I own a bond paying $40 per year for the next 9.75 years, then I get $1,000 back. But new bonds are paying $50 per year. Mine is worth less."

To sell the bond, the holder must offer it at a discount. What discount? Enough to make the total return match the new 5% yield. Let's calculate:

**The buyer's perspective:** If I buy the old bond at price P and hold it to maturity, I receive:
- Nine coupon payments of $20 each: $180
- Final payment of $1,000

Total future cash: $1,180, spread over 9.75 years. What price P makes this equivalent to a 5% annual return? The calculation uses [discounted-cash-flow](/discounted-cash-flow-valuation/) math:

P = $20/(1.025) + $20/(1.025)² + ... + $20/(1.025)^19 + $1,000/(1.025)^19

(Using semi-annual compounding: 5% annual = 2.5% per half-year.)

Solving: P ≈ $926.40

So the bond price falls to $926.40. Let's verify: A buyer paying $926.40 and holding to maturity receives $1,180 in cash ($180 in coupons + $1,000 principal). The gain is $1,180 − $926.40 = $253.60. Over 9.75 years, this compounds to a 5% annual return—matching the new market yield.

## The Reverse: Rates Fall

Now suppose, instead, rates fall after three months. New 10-year bonds are issued at 3% coupons. The holder of the original 4% bond thinks: "My bond pays $40 per year, but new bonds only pay $30. Mine is worth more."

To sell, the holder can demand a premium—a price above par. The math is the same:

P = $20/(1.015) + $20/(1.015)² + ... + $1,000/(1.015)^19

(Using 3% annual = 1.5% per half-year.)

Solving: P ≈ $1,077.50

Now a buyer pays $1,077.50 and receives $1,180 in total cash over 9.75 years—a $102.50 gain, which on a 3% annual return basis checks out.

## Duration: Why Long Bonds Are Riskier

The price change from a rate move depends on the bond's **maturity** and **coupon**. The longer the bond's remaining life, the larger the price change for a given rate move.

A 2-year bond with a 4% coupon and a 5% yield might fall from $1,000 to $981—only a 1.9% price drop. A 30-year bond with a 4% coupon and a 5% yield might fall to $828—a 17.2% price drop. The 30-year bond's longer stream of fixed payments gets hit harder by the new discount rate.

This sensitivity is measured by [duration](/duration/) — the weighted-average time to receive the bond's cash flows. A bond with a 5-year duration loses roughly 5% of its value if yields rise by 1%. A bond with a 15-year duration loses roughly 15% if yields rise by 1%.

## Why This Matters for Bond Investors

This inverse relationship is not an accident of math—it's the mechanism by which the bond market finds equilibrium. When the Federal Reserve raises interest rates, all existing bonds—whether Treasuries, corporate bonds, or municipal bonds—instantly become less attractive. To find new buyers, they must fall in price. When rates drop, existing bonds become attractive bargains and prices rise.

This also explains why [bond ETFs](/bond-etf/) and [mutual funds](/mutual-fund/) fluctuate in value as rates change. A fund holding $100 million in 10-year Treasuries will see its net asset value swing $5–10 million if the yield environment shifts 50 basis points (0.5%).

## Bond Price and Yield in Different Curve Environments

The relationship holds across the entire [yield curve](/yield-curve/). Short-term bonds (2-year Treasuries) are less sensitive to rate changes; 30-year bonds are highly sensitive. This means:

- When the Fed raises rates sharply, long-term bonds fall more than short-term bonds.
- When the Fed cuts rates, long-term bonds rally more than short-term bonds.
- Investors seeking to dampen volatility often buy short-term bonds or [Treasury bills](/treasury-bill/); those seeking total return often hold longer bonds (accepting bigger price swings).

## Key Distinctions: Holding vs. Selling

This price-yield inverse relationship matters most when selling a bond before maturity. An investor who holds a bond to maturity receives the full coupon stream and principal—price fluctuations are irrelevant. An investor who must sell (or chooses to sell) is exposed to whatever the market price is at that moment. A rising-rate environment can force a capital loss on that sale.

This is why [interest-rate risk](/interest-rate-risk/) is a key bond investment consideration. A retiree holding bonds for cash flow is less concerned with price fluctuations; a trader or fund manager constantly adjusts positions and cares deeply about price changes.

## See also

<div class="wiki-seealso">

### Closely related

- [Yield-to-Maturity](/yield-to-maturity/) — the discount rate that makes a bond's cash flows equal its current price
- [Duration](/duration/) — how sensitive a bond's price is to interest-rate changes
- [Accrued Interest on a Bond: How It Is Calculated](/accrued-interest-bond-calculation/) — the mechanism for fair pricing between coupon dates
- [Interest-Rate Risk](/interest-rate-risk/) — the risk that rates move and hurt bond prices
- [Coupon Payment](/coupon-payment/) — the fixed cash flow a bond pays
- [Bond](/bond/) — the foundational fixed-income instrument

### Wider context

- [Federal Reserve](/federal-reserve/) — the institution setting short-term rates that cascade through bond markets
- [Interest Rate](/interest-rate/) — the broad economic variable driving bond yields
- [Yield Curve](/yield-curve/) — how yields vary across bond maturities
- [Fixed-Rate Mortgage](/fixed-rate-mortgage-personal/) — mortgages follow the same inverse relationship as bonds

</div>
