---
title: "Constant Maturity Swap"
description: "A swap where one leg's rate is reset periodically to match the yield of a fixed-maturity security, isolating curve positioning."
---

*A constant maturity swap (CMS) is a derivative where one leg pays a rate that resets periodically to the yield of a specific fixed-maturity security—typically a 10-year Treasury bond or a 10-year swap rate—while the other leg pays a floating rate like SOFR. It isolates exposure to the yield curve shape, not just the absolute level of rates.*

## Why constant maturity swaps exist

In a standard [interest-rate swap](/wiki/interest-rate-swap/), the floating leg resets every three months to the 3-month SOFR rate. The rate you pay or receive is purely a short-term reference. If you want to hedge or position your exposure to a longer-term rate—say, the 10-year Treasury—a vanilla swap doesn't do that efficiently.

A constant maturity swap lets you directly hedge or bet on the 10-year rate (or whatever maturity you choose) without having to build a complex position in Treasury bonds or long-dated swaps. If you think 10-year yields are too high and will fall, you can receive fixed (or pay floating CMS) in a CMS, profiting when the 10-year yield drops and the CMS rate falls.

## Structure

A CMS typically has:

- **Floating leg**: pays SOFR (or another short-term benchmark) + spread.
- **CMS leg**: pays a rate equal to the yield of a security with a specified maturity (often 10-year), reset at intervals (quarterly, semi-annually).

When the CMS rate resets, it is set to the yield of that benchmark security on that reset date. The "constant maturity" name comes from the fact that the maturity of the reference security is held constant: even after one year, the reference is still the 10-year yield, not the 9-year yield that the original bond now has.

Example: A swap resets quarterly to the 10-year Treasury yield. At the first reset date, the 10-year yield is 3.5%, so the CMS payer pays 3.5% on the notional for that quarter. Three months later, the yield is 3.7%, so for the next quarter the CMS payer pays 3.7%. The reference maturity never changes; the security that is used to determine it rolls continuously.

## Common variations

**CMS-linked to swap rates**: Instead of using a Treasury yield, the CMS rate is tied to a fixed-maturity [interest-rate swap](/wiki/interest-rate-swap/) rate. A 10-year CMS might reset to the 10-year swap rate rather than the 10-year Treasury. These are liquid and actively traded.

**Leveraged CMS**: The CMS rate is multiplied by a factor greater than 1. For example, you might pay 2 × (10-year swap rate) + 100 bps. This amplifies your exposure to changes in the 10-year rate. Leveraged CMS swaps are more aggressive and carry larger [duration](/wiki/duration/) risk.

**Range-bounded CMS**: The CMS rate is capped or floored. You might cap the rate you receive at 5% and floor it at 2%, creating convexity and limiting your risk.

**CMS spread**: The two legs both reference different fixed-maturity rates. For example, you pay the 2-year CMS rate and receive the 10-year CMS rate, isolating your exposure to the 2-10 spread (curve steepness).

## Valuation and pricing

A CMS swap is harder to value than a vanilla interest-rate swap because the CMS rate is not deterministic—it depends on the future level of the 10-year rate (or whatever maturity), which is unknown.

Dealers use **one-factor or multi-factor interest-rate models** (e.g., Hull-White, LMM) to:

1. Simulate future paths of short-term and long-term rates.
2. For each date the CMS resets, determine the expected value of the reference rate.
3. Discount expected cash flows back to present value.
4. Solve for the fixed spread that makes the two legs equal in value.

The pricing involves estimating **convexity adjustments**. When the 10-year rate is volatile, there is a convexity effect: the CMS payer is short convexity (they benefit if the curve flattens and loses if the curve steepens). Dealers adjust the CMS rate down slightly to compensate for this cost.

## Uses

**Portfolio positioning**: An investor or fund manager who believes long-term rates will fall can receive fixed (pay floating CMS) in a CMS to profit from the decline without buying bonds, which carry [duration](/wiki/duration/) risk and other complications.

**Curve trades**: A trader who believes the 10-year yield will rise faster than the 2-year yield (steepener trade) might pay the 10-year CMS and receive the 2-year CMS. The P&L depends on how the curve shape changes.

**Hedging long-duration exposure**: A bank that holds a portfolio of long-term fixed-rate mortgages or bonds can use CMS swaps to hedge the [interest-rate risk](/wiki/interest-rate-risk/) from long-term rates moving against them.

**Structured notes**: Banks embed CMS coupons in structured notes sold to retail investors. For example, a note might pay 2% + (10-year CMS rate), giving investors exposure to rising long-term rates with downside protection from the guaranteed 2%.

## Risks

**Model risk**: The valuation depends heavily on the interest-rate model used. Different models can give materially different prices for the same trade, creating disagreement between traders and dealers.

**Basis risk**: The CMS rate is a theoretical construct—the yield of a bond with a fixed maturity. In reality, the exact "10-year rate" depends on which security you choose (on-the-run vs. off-the-run Treasury, swap rate, etc.). Basis risk arises if the actual rate you care about doesn't match the CMS reference exactly.

**Convexity risk**: If you are long CMS exposure (receiving CMS), you are short convexity. If volatility spikes, or if the curve becomes more volatile, you can lose money even if you predicted the CMS rate level correctly.

**Liquidity and counterparty risk**: CMS swaps are less liquid than vanilla interest-rate swaps, and they carry standard [counterparty risk](/wiki/counterparty-risk/) from the dealer or counterparty.

**Curve shape risk**: The P&L depends not just on the absolute level of rates but on how the curve shape evolves. A trader can be right about the 10-year yield level but wrong about the relationship between the short and long end, leading to losses.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the parent derivative structure.</li>
<li><a href="/wiki/interest-rate-swap/">Interest-rate swap</a> — the vanilla swap against which CMS swaps are compared.</li>
<li><a href="/wiki/swaption/">Swaption</a> — an option on a swap, sometimes used alongside CMS.</li>
<li><a href="/wiki/yield-curve/">Yield curve</a> — the curve that CMS rates help isolate and position.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/duration/">Duration</a> — the interest-rate sensitivity that CMS swaps create.</li>
<li><a href="/wiki/interest-rate-risk/">Interest-rate risk</a> — what CMS swaps are designed to hedge or create.</li>
<li><a href="/wiki/convexity/">Convexity</a> — the curve adjustment cost in CMS pricing.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the exposure both parties bear.</li>
</ul>
</div>
