---
title: "How to Calculate the Cost of Unwinding a Swap Early"
description: "Terminating a swap before maturity means paying or receiving mark-to-market breakage cost. Learn how fair value is calculated and why the cost can switch from negative to positive."
keywords:
  - how to calculate cost of unwinding swap early
  - swap breakage cost
  - mark to market swap termination
  - swap exit valuation
  - early swap termination
image: /svg/derivatives.svg
---

*Exiting a [swap](/swap/) before maturity requires paying a **mark-to-market breakage cost**—the difference between what the remaining cash flows are worth today and what you owe or receive under the swap's original terms. Rates move after you enter a swap, so the cost of exiting can be large and shift daily.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap Unwind Cost — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Mark-to-market termination reverses the swap at fair value.</div>

|   |   |
|---|---|
| **Core principle** | Pay or receive the present value of all remaining cash flows |
| **Counterparty role** | Your [counterparty](/counterparty-risk/) calculates the mark-to-market; they profit if you exit in-the-money |
| **Positive cost** | You owe money if rates have moved against your position |
| **Negative cost** | You receive money if rates have moved in your favor |
| **Pricing inputs** | Current interest rates, credit spreads, volatility, time to maturity |

</aside>

## The core: present value of remaining cash flows

When you enter a swap, you and your counterparty agree to exchange cash flows on specified dates. A vanilla [interest rate swap](/interest-rate-swap/) might have you paying fixed 3% and receiving floating LIBOR for five years on a $10 million notional.

After two years, you want out. The remaining cash flows are worth something *different* from what they were worth when the swap was signed, because market rates have changed. The **unwind cost** is the net present value of those remaining cash flows, calculated using today's market rates.

If rates have risen since you entered the swap, your fixed-rate obligation (3%) is now below market, so it is valuable—you owe the breakage. If rates have fallen, your fixed rate is above market, so your counterparty is stuck with an expensive obligation—they owe you the breakage.

## Example: an interest rate swap unwind

Suppose you entered a five-year interest rate swap three years ago:
- You pay fixed at 3% semi-annually.
- You receive floating (LIBOR) semi-annually.
- Notional: $10 million.
- Two cash flows remain (every six months for one year).

Today, market rates for similar swaps are 4%. Your 3% obligation is now cheap—a new swap at 4% would cost more. To exit, you must compensate your counterparty for that advantage.

**Step 1: Calculate the fair-value fixed rate for the remaining life.**
Using today's discount curve, determine what fixed rate a new one-year swap should trade. Suppose it is 4.0%.

**Step 2: Calculate the present value of the fixed-leg difference.**
Your swap has you paying 3%; the market rate is 4%. The difference is 1% per annum on $10 million, or $100,000 per year. With two semiannual payments remaining, you owe roughly:

$50,000 (six months) discounted six months + $50,000 (one year) discounted one year.

Using a discount rate of ~4% annually:
- First payment: $50,000 ÷ 1.02 ≈ $49,020
- Second payment: $50,000 ÷ 1.04 ≈ $48,077
- **Total PV ≈ $97,100** (roughly)

**Step 3: Account for the floating leg.**
The floating leg is already priced at market (it resets constantly), so it contributes zero net present value to the termination cost. Your breakage cost is the fixed-leg difference alone.

**Result:** You owe approximately $97,100 to terminate the swap early. Your counterparty receives this as compensation for losing a below-market fixed rate they can no longer collect.

## When the breakage cost is negative (you receive money)

Reverse the scenario. You entered the same swap paying fixed at 3%, but today market rates are 2%. Your fixed rate is now *expensive*—you are locked into paying 3% when the market wants 2%.

Now your counterparty owes *you* the breakage. You would receive roughly:

- Difference: 3% − 2% = 1%, or $100,000 per year on the remaining balance.
- Present value of the remaining two semiannual payments ≈ $97,100 (under 2% discounting).

Your counterparty pays *you* to unwind because they are grateful to escape an above-market obligation.

## Complications in real-world unwinding

**Credit spreads:** The breakage cost is not calculated purely on the risk-free rate; it includes the credit spread between you and your counterparty. If your counterparty's credit quality has deteriorated since you entered the swap, they may demand a wider spread to walk away, raising your unwind cost. Conversely, if your credit has deteriorated, they will demand more.

**Swaption prices:** Large swaps are sometimes unwound using embedded swaptions—options on the swap itself. The cost of unwinding is then the swaption premium, which varies with [volatility](/historical-volatility/) and [implied volatility](/implied-volatility/). On a volatile day, the cost to exit can jump.

**Bid-ask spread:** Your counterparty will quote an "ask" (the price they want to charge you to exit) that is wider than the fair-value midpoint. The spread can be 5–25 basis points on the notional amount, depending on [liquidity](/liquidity-risk/) and the relationship. A small, illiquid swap may be costly to unwind; a vanilla, actively-traded swap may be cheap.

**Accrued interest and variation margin:** If you are unwinding before a payment date, you owe accrued interest on the fixed leg through settlement. Additionally, if the swap is subject to [mark-to-market margin calls](/margin-call-forex/) (common on derivatives), your margin account has already moved; the unwind cost is the incremental cost to close.

## Why early unwinding can be expensive

The largest unwind costs arise when:

1. **You want out at the worst time for your position.** You locked in fixed at 3%, rates fell to 2%, you want out, and your counterparty extracts maximum value.

2. **The swap is long-dated with few offsetting positions.** A ten-year swap has more interest-rate [sensitivity](/sensitivity-analysis-valuation/) than a one-year swap, so the present-value swings are larger.

3. **You lack a natural offset.** If you have no floating-rate debt to hedge anymore, unwinding the swap is purely cosmetic—you are paying to escape a position that no longer serves a business purpose.

4. **Credit spreads have widened.** If your counterparty perceives you as a higher credit risk than when you entered the swap, they will mark up the unwind cost.

## Comparing unwind cost to holding to maturity

If the unwind cost is $100,000 but you have only $20,000 of remaining interest savings (the fixed rate you locked in is still favorable), holding to maturity is better. But if the unwind cost is $20,000 and the savings are $80,000, exiting now locks in a gain.

The decision also depends on what you will do with the capital freed up. If you can redeploy it at a higher return, the unwind cost may be a worthwhile investment.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — the foundational derivative contract
- [Interest Rate Swap](/interest-rate-swap/) — the most common swap type
- [Mark-to-Market](/fair-value/) — the valuation principle for early exit
- [Counterparty Risk](/counterparty-risk/) — why counterparties profit from your loss
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — the PV method underlying unwind costs
- [Bid-Ask Spread](/bid-ask-spread/) — the dealer markup on exit pricing

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — why swaps are entered in the first place
- [Interest Rate Risk](/interest-rate-risk/) — the source of unwind cost volatility
- [Credit Risk](/credit-risk/) — how counterparty quality drives unwind costs
- [Secured Lending](/repurchase-agreement/) — alternative to swaps for rate locking
- [Leverage Ratio](/leverage-ratio-forex/) — swaps often appear in leverage calculations

</div>