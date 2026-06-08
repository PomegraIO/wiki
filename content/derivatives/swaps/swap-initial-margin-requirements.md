---
title: "Initial Margin Requirements for Swaps"
description: "Initial margin for interest rate swaps is the cash buffer required at trade inception to cover potential mark-to-market losses. Learn SIMM, cleared vs. uncleared, and margin calls."
keywords:
  - initial margin requirements interest rate swaps
  - swap margin SIMM calculation
  - cleared swap margin
  - uncleared derivatives initial margin
image: /svg/derivatives.svg
---

*Banks and financial institutions trading [swaps](/swap/) must post **initial margin**—a cash buffer held by a clearinghouse or pledged to the counterparty—from day one of the trade. This margin covers potential losses if the swap's value moves against the trader. For cleared swaps, a central clearinghouse holds the margin; for uncleared swaps (mostly interest rate and credit swaps between banks), counterparties negotiate the amount using the Standard Initial Margin Model (SIMM). When markets spike, margin requirements soar, forcing traders to scramble for cash—a dynamic that nearly froze credit markets during financial crises.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Initial Margin for Swaps — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Upfront collateral required at trade inception to manage counterparty risk.</div>

|   |   |
|---|---|
| **Definition** | Cash or securities posted to cover potential mark-to-market losses on swap trades |
| **Cleared swaps** | Held by central clearinghouse (CME, LCH); standardized calculation |
| **Uncleared swaps** | SIMM model or bilateral negotiation; banks determine collateral |
| **Key driver** | Volatility: higher volatility → higher margin requirement |
| **Related concept** | [Variation margin](/variation-margin/) (daily mark-to-market adjustments) differs from initial margin |
| **Regulatory mandate** | Post-2008, derivatives reform requires initial margin for most swaps |
| **Margin calls** | Additional margin demanded when position loses value or volatility spikes |

</aside>

## Initial Margin vs. Variation Margin

Initial margin and variation margin are both forms of collateral in swap trading, but they serve different purposes and are calculated differently.

**Initial margin** is posted at trade inception. It's a one-time (or reset) collateral amount meant to cover the *potential* mark-to-market loss over the margin period of risk (typically 5–10 business days for cleared swaps). It's conservative: the clearinghouse or counterparty wants to be sure it has enough buffer to cover extreme moves, even if the trader defaults suddenly. This margin sits in a segregated account and is typically not returned to the trader until the swap is closed or the maturity date arrives (and the final settlement occurs).

**Variation margin** is posted daily (or more frequently) after the trade is initiated. It represents the actual, realized change in the swap's value since the last settlement. If an interest rate swap falls in value (because rates rose, making the fixed-rate payer worse off), the losing party posts variation margin to bring the collateral balance to market value. This daily true-up is the standard mechanism for managing mark-to-market risk in exchange-traded derivatives and increasingly in cleared swaps.

The two work together: initial margin is the insurance policy; variation margin is the settlement of daily wins and losses.

## Cleared Swaps: How Margin Is Calculated

When a swap is submitted to a clearinghouse (LCH, CME, EUREX, or others), the clearinghouse calculates initial margin using its own proprietary models, often called "Initial Margin for Extreme Loss Scenarios" or similar. The methodologies differ across clearinghouses, but all aim to cover a 1- to 5-day tail loss under extreme market conditions.

**CME's approach** uses historical and implied volatilities, correlation matrices, and stress-testing across thousands of market scenarios. The clearinghouse computes the initial margin amount such that, in 99% of historical lookbacks and projected scenarios, a trader's default fund contribution and margin would cover losses incurred during the margin period of risk.

**Model inputs:**
- Volatility of the underlying interest rate (short-term and long-term rates)
- Correlation between different curve points and currencies
- Historical extreme moves (e.g., the largest 1% of daily moves over the past 5 years)
- Current market conditions (wider spreads and higher volatility → higher margin)

**Practical figures:** For a $10 million notional interest rate swap, initial margin might be $50,000–$150,000, depending on the swap's tenor, the curve position, and current volatility. In calm markets, it's on the lower end; during a crisis, it can double or triple overnight.

## Uncleared Swaps and the SIMM Standard

Not all swaps are cleared. Many interest rate swaps, credit swaps, and exotic derivatives are traded bilaterally between two counterparties without a central clearinghouse. After the 2008 financial crisis and the Dodd-Frank Act, regulators required initial margin for most uncleared derivatives—but the margin is agreed between the two parties, not mandated by a clearinghouse.

The **Standard Initial Margin Model (SIMM)**, developed by the International Swaps and Derivatives Association (ISDA), is the industry standard for calculating margin on uncleared derivatives. It was formally endorsed by regulators (the Basel Committee on Banking Supervision) and became mandatory for most banks and large hedge funds starting in 2016.

**SIMM's structure:**

1. **Sensitivity calculation:** The model computes how sensitive the swap's value is to small moves in each risk factor (short rates, long rates, credit spreads, FX rates, etc.). This is often called "delta" or "PV01" (present value of 1 basis point move).

2. **Volatility weighting:** Each sensitivity is multiplied by the historical volatility of that risk factor. For interest rates, this might be 70–150 basis points of annualized volatility, depending on market conditions and the specific curve segment.

3. **Correlation and aggregation:** Sensitivities are aggregated using correlation assumptions. The model assumes, for example, that short rates and long rates move together (high correlation), so the risks don't fully diversify. This prevents a trader from claiming false risk reduction by offsetting different risks.

4. **Historical scenario stress:** SIMM also runs historical scenarios (like the 2008 crisis or the 2015 China devaluation) to ensure margin covers tail events. If a particular rate pair moves 10x its normal volatility in a historical worst-case scenario, the margin must cover it.

**SIMM output:** The final initial margin number is the maximum loss across these scenarios. For a $100 million notional two-year interest rate swap with current market volatility, SIMM might calculate initial margin of $200,000–$500,000. The exact amount depends on the counterparty's full portfolio of derivatives; SIMM applies *portfolio-level* margin (offsets are recognized across many trades).

## Why Margin Spikes During Volatility

Initial margin is not static. For cleared swaps, clearinghouses reprice margin daily or intraday if market conditions change sharply. For uncleared swaps, the SIMM is recalculated regularly (typically monthly, but more frequently if triggers are hit).

**The mechanism:** Volatility is a core input. When volatility doubles, margin requirements often double or more, because the potential 5-day loss scenario is now wider. This is what happened in March 2020 (COVID crash), March 2023 (banking crisis), and during the 2008 financial crisis: interest rates and credit spreads moved wildly, volatility spiked, and clearinghouses jacked up initial margin requirements by 50–200% in days.

**The cascade effect:** When a trader is forced to post additional margin, it must do so immediately (usually within one to two business days). If the trader doesn't have cash on hand, it must liquidate positions, sell assets, or tap credit lines. During a crisis, all traders face the same pressure simultaneously, which can force fire sales and accelerate market declines—a dangerous feedback loop.

**Real example:** In September 2019, a glitch in the Federal Reserve's repo market caused short-term interest rate volatility to spike. Major banks trading interest rate derivatives suddenly faced margin calls of billions of dollars. The Fed had to inject liquidity into the overnight lending market to prevent a credit freeze. Initial margin had become a systemic risk amplifier.

## Uncleared Swap Margin: Bilateral Negotiation vs. SIMM

Although SIMM is the standard, not all uncleared swaps use it. Large banks and sophisticated counterparties sometimes negotiate initial margin bilaterally, especially for older trades or exotic derivatives where SIMM doesn't apply cleanly.

**Negotiated margin** can be higher or lower than SIMM, depending on the relationship, the counterparty's creditworthiness, and the time of trade. A well-capitalized bank with strong credit might negotiate lower margin with a prime broker than SIMM would suggest. A struggling counterparty or a new client might face much higher margin.

**Regulatory pressure** has pushed most market participants toward SIMM. Regulators want standardized, transparent margining, not ad-hoc negotiations that could hide risk. Large financial institutions are required to use SIMM for uncleared derivatives. However, smaller participants (e.g., non-financial corporates hedging genuine risks) have some relief from the initial margin requirement for certain types of swaps.

## Variation Margin and Daily Settlement

After initial margin is posted, variation margin is calculated daily (or more frequently, depending on the agreement). For cleared swaps, the clearinghouse reprices the entire position to market every day at close and either receives or pays the cash difference.

Example:
- Trader enters a 5-year interest rate swap at a fixed rate of 4%.
- Next day, rates fall to 3.9%. The swap's value rises; the fixed-rate receiver (our trader) gains.
- The clearinghouse marks the swap to market and credits the trader's variation margin account.
- The other side of the trade posts variation margin to the clearinghouse.
- Initial margin remains in the segregated account, untouched, unless a margin call is issued.

For uncleared swaps, variation margin is typically settled bilaterally, though post-Dodd-Frank, large counterparties also must exchange variation margin daily on uncleared swaps (another regulation intended to reduce counterparty risk).

## Margin Calls: What Triggers Them

Initial margin is recalculated and reset periodically. A trader faces a margin call if:

1. **The position's mark-to-market loss exceeds initial margin:** If a swap has lost more than the initial margin buffer, the trader must post additional margin to restore the cushion.

2. **Volatility surges:** Even if the position hasn't moved much, an increase in implied volatility (volatility smile, vol term structure, or historical realized volatility) triggers higher initial margin requirements. The trader must post the difference.

3. **Correlation assumptions break down:** If a trader has offsetting risks in different currencies or asset classes, and those correlations decline (i.e., risks no longer hedge each other), margin increases.

4. **Credit rating or capital ratios decline:** Some margin agreements include triggers tied to credit metrics. If a trader's credit rating is downgraded, margin requirements can step up automatically.

During stressed periods, margin calls cascade and force immediate liquidity drains. This is why treasury departments at large banks maintain significant cash and credit facility availability specifically for margin calls on derivatives.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — Core swap product structure and mechanics
- [Derivatives Hedging](/derivatives-hedging/) — Using swaps to manage risk
- [Counterparty Risk](/counterparty-risk/) — Credit risk in bilateral derivatives trading
- [Variation Margin](/variation-margin/) — Daily mark-to-market settlement
- Clearinghouse — Central counterparty for exchange-traded and cleared derivatives
- [Credit Spread](/credit-spread/) — Component of swap pricing and margin models

### Wider context

- [Interest Rate Swap](/interest-rate-swap/) — Most common swap type
- [Stress Testing](/stress-testing/) — How banks model extreme scenarios for margin adequacy
- [Systemic Risk](/systemic-risk/) — How margin mechanics amplify market stress
- [Dodd-Frank Act](/dodd-frank-act/) — Post-2008 derivatives regulation

</div>
