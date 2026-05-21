---
title: "Par Swap"
description: "A swap whose fixed rate is set so that both legs have equal present value at inception, requiring no upfront payment."
---

*A par swap is a standard [interest-rate swap](/wiki/interest-rate-swap/) where the fixed rate is set to a "par" level—meaning the swap has zero market value at inception. No upfront payment is needed; both parties are indifferent between the fixed and floating rates offered. It is the default structure for most interest-rate swaps traded in the market.*

## Why "par" and what it means

When a swap is initiated, the fixed-leg present value should equal the floating-leg present value if both parties are willing to enter without additional side payments. The fixed rate that achieves this equality is the "par" rate, or the "par swap rate."

**Example**: A 5-year par swap might have a fixed rate of 4.5%. At today's date, the present value of paying 4.5% fixed for 5 years equals the expected present value of receiving SOFR (expected to average ~4.5%) over the same period. The swap is "at par" — balanced.

If you tried to set the fixed rate at 5%, the fixed leg would be more valuable (you are paying more), and you'd have to pay the other party to enter the swap. If you set it at 4%, the opposite: the other party would pay you.

## Distinction from off-par and seasoned swaps

**Par swap (at inception)**: Zero market value; no upfront payment.

**Off-par swap**: The fixed rate is set away from par (e.g., 3.5% instead of 4.5%). One party makes an upfront payment to compensate the other. Used when a customer wants a specific fixed rate even if it's not par.

**Seasoned swap (aged swap)**: A swap entered months or years ago that is now "off market" because rates have moved. If rates have risen since the swap was signed, the fixed rate (locked in at inception) is now below the par rate, making the swap valuable to the fixed-rate receiver.

Most swaps are entered as par swaps. They become off-par as market conditions change.

## Valuation of a par swap

A par swap is valued such that:

$$ PV(\text{Fixed Leg}) = PV(\text{Floating Leg}) $$

The fixed leg pays a constant rate R (the par swap rate):
$$ PV(\text{Fixed}) = R \times \sum_{i=1}^{n} DF(t_i) \times \Delta t_i $$

where DF(t_i) is the zero-coupon discount factor at time t_i and Δt_i is the day-count fraction.

The floating leg pays the expected forward SOFR rate:
$$ PV(\text{Floating}) = \sum_{i=1}^{n} DF(t_i) \times [F(t_{i-1}, t_i) \times \Delta t_i] $$

where F is the forward SOFR rate from t_{i-1} to t_i.

Setting them equal and solving for R gives the par swap rate.

## Why par swaps matter

**Market convention**: The quoted swap rates in the market (e.g., "5-year swap at 4.52%") are par swap rates. This is how dealers and brokers communicate: a quote of 4.52% means a par swap at that rate.

**Pricing other swaps**: A swap at a different fixed rate (off-par) is priced as a par swap plus a fixed payment to compensate for the rate difference. If the par rate is 4.5% and a customer wants 5%, the customer pays the difference upfront (or it amortizes over the swap life).

**Dynamic hedging**: If a dealer enters a par swap with a customer, the dealer immediately turns around and enters an offsetting swap at the current par rate. The dealer is hedged (long and short offsetting swaps) and pockets the bid-ask spread.

## Par swap rates as market consensus

The par swap rate is a consensus view of:
1. **Expected short-term rates**: The floating leg pays SOFR, which is reset frequently. The par rate reflects where the market expects SOFR to be, on average, over the swap's life.
2. **The term premium**: A longer-dated swap has higher interest-rate risk (longer [duration](/wiki/duration/)), so the market demands a higher rate to compensate. The par rate includes this premium.
3. **Credit and liquidity spreads**: The rate also compensates for the risk that the counterparty defaults and the cost to hedge if that happens.

Par swap rates are watched closely by traders, investors, and policymakers:
- **Central banks** watch par swap rates to gauge market expectations of future short-term rates, which inform their policy.
- **Asset managers** use par swap rates to decide whether bonds are fairly valued.
- **Traders** use par swaps as a benchmark to identify arbitrage opportunities in other instruments (bonds, futures, other swaps).

## Par swap rates and the yield curve

The **par swap curve** is the plot of par swap rates across tenors (1, 2, 3, 5, 7, 10, 30 years). It is a key financial market indicator.

**Comparison to Treasury yields**: Par swap rates are typically higher than comparable Treasury yields (e.g., 5-year swap rate > 5-year Treasury yield). Why? Because swaps carry [counterparty risk](/wiki/counterparty-risk/) while Treasuries are backed by the U.S. government. The difference is called the **TAS (Swap-Treasury) spread**.

**Comparison to bond yields**: Corporate bonds trade at spreads over Treasuries. Swaps trade at spreads over Treasuries (the TAS). A bond's value can be thought of as: Treasury yield + credit spread. A swap's value is: Treasury yield + TAS spread.

## Market dynamics and par rate changes

Par swap rates are dynamic. They change when:

1. **Central bank actions**: A rate cut or hint of a cut lowers expected future short-term rates, driving par swap rates down.

2. **Inflation expectations**: Higher inflation expectations raise par swap rates (markets expect higher future rates to combat inflation).

3. **Economic growth**: Strong growth raises rates; recession fears lower them.

4. **Supply and demand**: If many investors want to pay fixed and receive floating (e.g., fear of rising rates), the par swap rate falls (the market compensates fixed-rate payers with a lower rate). If demand shifts the other way, rates rise.

5. **Credit stress**: In a financial crisis, [counterparty risk](/wiki/counterparty-risk/) rises and the swap-Treasury spread widens, pushing par swap rates higher relative to Treasuries.

## Par vs. par-value in bonds

Don't confuse par swap with par value of a bond:

- **Par swap**: A swap whose fixed rate equals the fair rate (zero upfront payment).
- **Par value (bond)**: The principal amount of a bond (e.g., a bond with $100 par that matures for $100).

The terms are unrelated except etymologically (both from "par," meaning equal or at parity).

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the foundational structure.</li>
<li><a href="/wiki/interest-rate-swap/">Interest-rate swap</a> — the most common type of par swap.</li>
<li><a href="/wiki/yield-curve/">Yield curve</a> — the parallel structure for bonds; par swap curve parallels it.</li>
<li><a href="/wiki/forward-contract/">Forward contract</a> — another financial instrument priced at par at inception.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/duration/">Duration</a> — the interest-rate sensitivity that determines par swap rates.</li>
<li><a href="/wiki/sofr/">SOFR</a> — the floating rate referenced in par swaps.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the spread over Treasuries in par swap rates.</li>
<li><a href="/wiki/federal-reserve/">Federal Reserve</a> — policy decisions drive par swap rate changes.</li>
</ul>
</div>
