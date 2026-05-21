---
title: "Zero-Coupon Swap"
description: "A swap where one or both parties defer receiving cash flows until maturity, concentrating the settlement into a single terminal payment."
---

*A zero-coupon swap is a contract in which one or both parties do not receive interim interest payments. Instead, all cash flows—or at least the floating leg—are compounded and settled as a single lump sum at maturity. This structure is useful for managing long-term liabilities and hedging where periodic resets are undesirable.*

## Structure

A zero-coupon swap has several variants:

**Fixed-only zero-coupon**: The fixed-leg payer receives no interim payments. All accrued fixed interest compounds to maturity and settles in one payment.

**Floating-only zero-coupon**: The floating-leg payer receives no interim payments. All floating-leg returns compound to maturity.

**Fully zero-coupon**: Both legs defer all payments until maturity. Very rare; usually one leg still pays periodically.

Example: A pension fund enters a 20-year zero-coupon swap. The pension pays no coupons for 20 years. At maturity, the pension receives a single lump sum equal to the compounded value of all accumulated floating-leg payments minus accumulated fixed rates. This matches the fund's long-term payout schedule.

## Comparison to vanilla swaps

**Vanilla swap**: Both parties exchange interest payments every 3 or 6 months. If floating rates are SOFR 4% and fixed is 4.5%, they net settle 0.5% quarterly. Over 10 years, many small payments occur.

**Zero-coupon swap**: No interim payments. Over 10 years, interest accrues. At year 10, a single net payment occurs, based on the compounded value of all intervening floating rates compared to the fixed accrual.

The vanilla swap's known periodic cash flows suit operational treasuries (banks, corporates managing daily liquidity). The zero-coupon swap's single terminal payment suits long-term balance sheet management (pension funds, insurers, sovereigns).

## Valuation

Valuing a zero-coupon swap is more complex than a vanilla swap because the floating leg must be projected forward for the entire term (not reset periodically), and all cash flows must be compounded.

Dealers:

1. **Project forward rates**: Use the [forward curve](/wiki/forward-exchange-rate/) to estimate the floating rate at each future date (even if no payment occurs until maturity).

2. **Compound the floating leg**: Calculate the cumulative value of floating payments compounded to maturity.
$$ \text{Floating PV at Maturity} = \text{Notional} \times \prod_{i=1}^{n} \left(1 + r_i \times \Delta t_i \right) $$

3. **Compound the fixed leg**: The fixed payment compounds at the same fixed rate.
$$ \text{Fixed Payment at Maturity} = \text{Notional} \times (1 + R_{fixed})^T $$
where T is the time to maturity.

4. **Discount back to present**: Both legs are discounted to present value using zero-coupon discount factors.

5. **Solve for the fixed rate**: Find the rate that equates both legs in present value.

The zero-coupon swap rate is typically **higher** than the vanilla swap rate for the same tenor, because:
- The fixed-rate payer locks in a rate for a longer period (no periodic reset).
- There is no opportunity to refinance early.
- [Convexity](/wiki/convexity/) of long-term yields affects the longer-dated projections.

## Uses

**Long-term liability matching**: A pension fund with a 20-year liability uses a zero-coupon swap to hedge the liability's expected cost. The swap's single terminal payment aligns with when the pension must pay retirees.

**Insurance reserving**: An insurance company with long-dated claims (e.g., asbestos liabilities) uses zero-coupon swaps to lock in yields without interim cash flow surprises.

**Corporate bond hedging**: A company that issued a 30-year zero-coupon bond (no coupons, all return at maturity) can use a zero-coupon swap to convert it to a synthetic floating-rate bond or synthetic fixed-rate bond at a different rate.

**Debt restructuring**: A sovereign or stressed borrower might defer interest payments (using a zero-coupon structure) until cash flow improves.

**Structured finance**: Zero-coupon swaps are embedded in [structured notes](/wiki/bond/) and CLOs (collateralized loan obligations) to match the payment timing of the underlying collateral.

## Risks

**Reinvestment risk is gone, but long-term rate risk is concentrated**: With a vanilla swap, you receive floating payments and can reinvest them, giving you some optionality. With zero-coupon, you have no interim cash flow, so no reinvestment opportunity, but you are fully exposed to long-term rate moves.

**Liquidity risk**: Zero-coupon swaps are less liquid than vanilla swaps. Dealers quote wider spreads, and large trades can move the market.

**Convexity risk**: Because the fixed rate is locked for the entire term, the zero-coupon swap is convex in interest rates (more sensitive to large rate moves). A sharp decline in rates can make a fixed-rate zero-coupon swap much more valuable, but an equally sharp rise can be painful for the fixed-rate receiver.

**Counterparty risk**: Long-dated zero-coupon swaps (10+ years) expose both parties to significant [counterparty risk](/wiki/counterparty-risk/). The accumulated value at maturity can be very large.

**Model risk**: Valuation of zero-coupon swaps depends heavily on forward-rate models and curve assumptions. Different models can produce materially different prices.

**Inflation risk**: For very long-dated swaps (30+ years), inflation can be a major risk. A fixed rate locked for 30 years might seem attractive today but become undesirable if inflation is high throughout the period.

## Mechanics and considerations

**Compounding convention**: The swap agreement specifies how interest compounds (daily, monthly, annually, continuously) and the daycount convention.

**Reset mechanisms**: Some zero-coupon swaps have intermediate resets. For example, interest might compound quarterly until year 5, then annually thereafter. This is a hybrid between zero-coupon and vanilla.

**Caps and floors**: Some zero-coupon swaps have rate caps or floors to limit the extremes of potential outcomes.

**Collateral management**: For long-dated swaps, dealers may require [collateral](/wiki/repurchase-agreement/) to mitigate credit risk. The collateral amount can be significant.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the foundational structure.</li>
<li><a href="/wiki/interest-rate-swap/">Interest-rate swap</a> — the vanilla version with periodic payments.</li>
<li><a href="/wiki/amortizing-swap/">Amortizing swap</a> — another variant for specialized uses.</li>
<li><a href="/wiki/constant-maturity-swap/">Constant maturity swap</a> — a different variant for curve positioning.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/duration/">Duration</a> — the interest-rate sensitivity of zero-coupon swaps is high.</li>
<li><a href="/wiki/convexity/">Convexity</a> — affects long-dated zero-coupon swap pricing.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — significant in long-dated swaps.</li>
<li><a href="/wiki/bond/">Bond</a> — zero-coupon swaps are often used to hedge or replicate bonds.</li>
</ul>
</div>
