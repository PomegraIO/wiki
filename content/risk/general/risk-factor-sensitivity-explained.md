---
title: "Risk Factor Sensitivity Explained"
description: "Risk factor sensitivity metrics—delta, DV01, beta—measure how much a position's value changes per unit move in an underlying risk driver."
keywords:
  - risk factor sensitivity explained
  - delta hedging
  - dv01
  - sensitivity analysis
  - duration risk
  - beta portfolio
  - greeks finance
image: "/svg/risk.svg"
---

*A **risk factor sensitivity** quantifies the change in a position's value for a one-unit move in a specific underlying risk driver—whether a stock price, interest rate, or volatility surface. These sensitivities (delta, duration, beta, vega) let traders, portfolio managers, and risk officers know exactly which bets they've placed and what happens when markets move.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Risk Factor Sensitivity — Key Facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Greeks, duration, and beta are the lingua franca of risk measurement.</div>

|   |   |
|---|---|
| **What it measures** | Price change per unit move in a risk driver |
| **Common metrics** | Delta, DV01, duration, beta, vega, gamma, theta |
| **Use case** | Hedging, position sizing, risk reporting, limits |
| **Time horizon** | Instantaneous (Greeks) or rolling (beta, duration) |
| **Key insight** | Sensitivity is only valid near the current market level |

</aside>

## The Core Purpose: Know Your Exposures

Sensitivity analysis strips away the noise. If you own 1,000 shares of a stock trading at $50, your delta is straightforward: +1,000 shares means you gain $1,000 for every dollar the stock rises. But when you hold a bond, a swaption, a currency basket, or a portfolio of 500 securities, you need a precise language to describe risk without reciting every holding.

**Risk factor sensitivity metrics provide that language.** They answer: "If the 10-year Treasury yield moves up 25 basis points, how much does my position lose?" or "If the USD strengthens 1%, what happens to my yen exposure?" The metrics are designed to be additive—you can sum sensitivities across trades to understand your net portfolio risk.

## The Greeks: Instantaneous Sensitivities

For derivatives—options, swaptions, equity forwards—the Greeks are the standard toolkit.

**Delta** measures the first-order price change. A call option with delta 0.6 gains approximately $0.60 in value for every $1 rise in the underlying stock. Delta varies with the underlying price, time to expiration, and volatility; it is not constant. Traders use delta to determine how many shares to buy or sell to hedge an option position (delta-neutral hedging).

**Gamma** is the rate of change of delta itself—the curvature of the price-sensitivity curve. High gamma means delta changes sharply as the underlying moves; low gamma means delta is relatively stable. An at-the-money option has the highest gamma; an out-of-the-money option has lower gamma.

**Vega** measures sensitivity to changes in volatility. A vega of 0.02 means the option's value rises by $0.02 for every 1% increase in implied volatility. Vega matters most for longer-dated options and is crucial for strategies that bet on volatility shifts.

**Theta** (time decay) captures the daily erosion in option value as expiration approaches, holding price and volatility constant. Longer-dated options have lower theta per day; near-the-money options experience rapid theta decay as expiration nears.

**Rho** measures sensitivity to interest rate changes. For long-dated options, especially on stocks or bonds, a 1% rise in rates can noticeably change the present value of future payoffs.

These Greeks are not independent: as the underlying price moves, delta changes (gamma effect), and the passage of time alters the entire set. Professional traders monitor all of them because a hedged position (e.g., delta-neutral) can still bleed value if gamma and theta move in opposite directions.

## Duration and DV01: Bond Sensitivities

**Duration** is the weighted-average time to receive a bond's cash flows, expressed in years. More usefully, it approximates the percentage price change for a 1% change in yield. A bond with duration 5 loses roughly 5% of its value if yields rise by 1 percentage point.

**DV01** (dollar value of a 1 basis point move) is the absolute dollar change in the bond's price for a 1 basis point (0.01%) move in yield. A DV01 of $50 means the bond loses $50 in value for every basis point increase in yield. Portfolio managers often speak in DV01 because it directly translates to P&L impact.

Modified duration and effective duration account for options embedded in bonds (e.g., a refinancing option in a mortgage-backed security); they are more accurate for bonds where the coupon and principal may vary with rates.

## Beta: Systematic Risk Exposure

**Beta** measures the sensitivity of a stock or portfolio to broad market movements. A beta of 1.2 means the stock tends to move 1.2% when the market moves 1%; a beta of 0.8 means it moves only 0.8% for a 1% market move.

Beta captures systematic risk—the volatility tied to overall market swings—and is central to the [capital-asset-pricing-model](/capital-asset-pricing-model/) and modern portfolio construction. A portfolio manager uses beta to understand sector rotation and [market-timing](/market-timing/) decisions: a high-beta portfolio is more aggressive, a low-beta portfolio more defensive.

Importantly, beta is estimated over a historical period (often three to five years) and assumes that past market relationships persist. During structural breaks—regime shifts, policy changes, credit events—historical betas can become unreliable.

## Limitations and Non-Linearity

All sensitivities are local. **Delta assumes linear price movement**: true only for small moves. When an underlying price jumps 10%, delta has shifted, and the Greeks themselves have changed. This is why gamma and higher-order derivatives matter.

**Volatility assumptions** embedded in option Greeks are only valid if the future volatility matches the implied volatility priced into the option. If implied volatility rises unexpectedly, vega profits can offset delta losses, and vice versa.

**Historical beta** assumes the relationship between a stock and the market is stable. It can shift during crises, during earnings surprises, or when a company enters a new business line.

Sensitivity metrics are best understood as local guides, not absolute predictions. Risk officers use them alongside [stress-testing](/stress-testing/) and [value-at-risk](/value-at-risk/) to capture tail risk and non-linear moves.

## Using Sensitivities in Practice

**Hedging**: A trader long a call option (positive gamma, positive vega) sells some shares (negative delta) to neutralize delta risk. That trader is now long volatility and can profit if the underlying becomes more volatile while staying delta-neutral.

**Position sizing**: An equity fund allocates capital using target beta. If it wants a portfolio beta of 1.0 and a holding has beta 1.8, the fund sizes that position smaller.

**Risk reporting**: Firms compute daily sensitivities (delta, vega, DV01) across trading books and report them to the chief risk officer and regulators. Limits are often set in sensitivity terms ("no more than $10M DV01 on the bond desk").

**Sensitivity analysis for valuation**: When [discounted-cash-flow-valuation](/discounted-cash-flow-valuation/) requires assumptions (discount rate, growth rate), sensitivity analysis shows how the valuation changes across a range of inputs, revealing which assumptions drive the most uncertainty.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — instantaneous rate of change of a derivative's price
- Greeks — comprehensive toolkit for derivatives risk
- [Duration](/duration/) — bond sensitivity to yield changes
- [Beta](/beta/) — systematic risk measure for equities
- [Gamma](/gamma/) — curvature of delta and second-order risk
- [Value at Risk](/value-at-risk/) — tail-risk quantile measurement
- [Stress Testing](/stress-testing/) — scenario-based portfolio resilience

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — mechanics of reducing risk via offsetting positions
- [Market Risk](/market-risk/) — systematic exposure to asset-price moves
- Portfolio Construction — integrating risk metrics into allocation
- [Volatility Smile](/volatility-smile/) — non-linear volatility across strike prices

</div>
