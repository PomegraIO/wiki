---
title: "How to Use Dollar Duration to Estimate Bond P&L"
description: "Step-by-step method for converting modified duration into dollar profit-and-loss estimates for basis-point moves in bond yields."
keywords:
  - dollar duration bond
  - how to use dollar duration
  - modified duration P&L
  - bond basis point risk
  - duration calculation
image: /svg/fixed-income.svg
---

*Bond traders use **dollar duration** to translate yield moves into profit-and-loss dollars without running a full repricing model. It is a first-order approximation: multiply the bond's [modified duration](/duration/) by its market value by the yield change in decimal form. The result is an estimate of how much you gain or lose if yields move by a given number of basis points.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dollar Duration P&L Estimate — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A fast mental math tool for risk managers and traders.</div>

|   |   |
|---|---|
| **Formula** | Dollar P&L ≈ −Modified Duration × Market Value × Yield Change (decimal) |
| **Yield change** | Convert basis points ÷ 10,000 (e.g., 50 bps = 0.0050) |
| **Sign** | Negative sign means yields up = price down |
| **Accuracy** | Good for small moves (±100 bps); [convexity](/option/) adjusts for larger moves |
| **Example** | See worked example below |

</aside>

## The modified duration concept

Modified duration is the percentage change in a bond's price for a 1% (100 basis point) move in yield. A bond with a [modified duration](/duration/) of 5 will rise roughly 5% in price if yields fall 100 basis points, and fall 5% if yields rise 100 basis points.

Modified duration differs from [Macaulay duration](/duration/), which is a cash-flow-weighted measure of time. Macaulay duration must be adjusted downward for the bond's [yield-to-maturity](/yield-to-maturity/) to become modified duration. For a bond trading near par (100), the two are close; for a bond trading at a steep discount or premium, they diverge.

Modified duration is the relevant number for price risk. That is the input you need for dollar P&L math.

## The dollar duration formula

Dollar duration converts a percentage move into dollars:

**Dollar Duration = −Modified Duration × Market Value × Change in Yield (as decimal)**

The negative sign reminds us that bond prices move opposite to yields: when yields go up, prices go down.

Example setup: You own a bond with a [modified duration](/duration/) of 6.5, trading at a market value of $1,000,000. You want to estimate P&L if yields rise 25 basis points.

Calculation:
- Yield change in decimal: 25 basis points = 25 / 10,000 = 0.0025
- Dollar P&L = −6.5 × $1,000,000 × 0.0025 = −$16,250

Interpretation: If yields rise 25 basis points, your position is estimated to lose approximately $16,250.

## Worked example: a hypothetical corporate bond

Let's build out a more realistic scenario. You hold $5,000,000 face value of a corporate bond maturing in 7 years, currently trading at 101.50 (103.5% of par). The bond has a [coupon rate](/coupon-rate/) of 4.5%, paid semi-annually, and the current [yield-to-maturity](/yield-to-maturity/) is 4.0%.

Step 1: Calculate or look up modified duration.
For a 7-year bond with a 4.0% YTM, the modified duration is approximately 6.3 (you would use a bond calculator or approximation formula in practice).

Step 2: Calculate market value.
Market value = Face value × Price as percentage = $5,000,000 × 1.015 = $5,075,000

Step 3: Estimate P&L for different yield scenarios.

If yields rise 50 basis points (0.50%):
- Dollar P&L = −6.3 × $5,075,000 × 0.0050 = −$159,863

If yields fall 30 basis points (0.30%):
- Dollar P&L = −6.3 × $5,075,000 × (−0.0030) = +$95,918

## Why the negative sign matters

The negative sign in the formula is not a stylistic choice; it is the economic sign. When yields fall, the term "change in yield" is negative (e.g., −0.0030 for a 30 bps fall). Multiplying by the negative sign flips the result to positive, correctly reflecting the fact that falling yields create gains for bond holders.

Conversely, rising yields produce a positive yield change (e.g., +0.0050), and the negative sign flips it to a loss (negative P&L). This automatic sign-flipping is a feature, not a bug. It forces you to think in the right direction: yields up = my bond loses value.

Some traders omit the negative sign and manually apply the inverse sign to the yield change. This is fine as long as you're consistent.

## Limitations: convexity and large moves

Dollar duration is a linear approximation. It assumes that the percentage change in price is proportional to the percentage change in yield. This is accurate for small moves (±50 basis points) but begins to break down for larger moves.

The reason is [convexity](/option/): the relationship between bond prices and yields is not a straight line but a curve. Convexity is positive for most bonds—meaning that the actual price gain from a 100 bps fall in yields is slightly larger than the actual price loss from a 100 bps rise in yields.

For a 100+ basis point move, you need to add a convexity adjustment:

**Adjusted P&L = Dollar Duration P&L + (0.5 × Convexity × Market Value × Yield Change²)**

Convexity is typically small (often 50–150 for a mid-duration bond), so the adjustment is often in the range of $5,000 to $20,000 for a $5 million position. For risk management and quick estimates, traders often ignore convexity for moves under 100 bps; for larger moves or precision work, convexity is included.

## Practical applications

**Risk management**: A portfolio manager with a $200 million bond portfolio wants to know how much market value she is at risk of losing if the Fed raises rates and yields spike 75 basis points. If the portfolio duration is 5.2, dollar duration = −5.2 × $200,000,000 × 0.0075 = −$7,800,000. She is at risk of a $7.8 million loss. If her risk budget is $5 million, she must de-risk.

**Scenario analysis**: A trading desk is evaluating whether to increase duration. They model P&L across several yield scenarios (rates up 50 bps, rates flat, rates down 50 bps) using dollar duration, then decide whether the asymmetry of payoffs justifies the extra risk.

**Hedge sizing**: A company has issued a $100 million bond and wants to hedge [interest rate risk](/interest-rate-risk/). It can buy a Treasury bond with the same duration. Dollar duration tells it exactly how much Treasury to buy so that the P&L of the Treasury hedge offsets the P&L of the cash position.

## Comparing bonds with different durations

Dollar duration is most useful when comparing positions of vastly different sizes and durations. A $10 million holding of a 2-year bond (duration ~1.9) has much lower dollar duration ($190,000 per 100 bps move) than a $5 million holding of a 20-year bond (duration ~15, so $750,000 per 100 bps move). The 20-year position is riskier in absolute dollar terms, despite being a smaller face value.

This is why risk managers always measure and limit duration-adjusted exposure, not just face value.

## See also

<div class="wiki-seealso">

### Closely related

- [Duration](/duration/) — the foundational concept that underlies the dollar duration calculation
- [Modified duration](/duration/) — the specific form of duration used in P&L math
- [Yield-to-maturity](/yield-to-maturity/) — the yield assumption that feeds into duration and P&L estimates
- [Convexity](/option/) — the curvature adjustment needed for large yield moves
- [Interest rate risk](/interest-rate-risk/) — the source of P&L volatility in bond positions

### Wider context

- [Bond](/bond/) — the instrument itself, and the relationship between coupons and price
- [Coupon payment](/coupon-payment/) — the cash flows that shape a bond's duration
- [Treasury bond](/treasury-bond/) — the benchmark for interest rate moves
- [Value at risk](/value-at-risk/) — a broader framework for modeling portfolio losses
- [Sensitivity analysis](/sensitivity-analysis-valuation/) — the general practice of stress-testing to basis-point moves

</div>
