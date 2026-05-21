---
title: "Inflation Swap"
description: "A swap that exchanges fixed interest payments for floating payments linked to inflation, used to hedge or speculate on inflation trends."
---

*An inflation swap is a contract where one party pays a fixed rate and the other pays a rate tied to a consumer price index, such as the U.S. Consumer Price Index (CPI). The swap isolates exposure to inflation expectations and is used by pension funds, insurers, and traders to hedge or position on inflation.*

## Why inflation swaps matter

Many financial obligations are indexed to inflation. A pension plan promises retirees a payment that rises with CPI. An insurance company that sold inflation-linked annuities has a liability that grows when CPI rises. A bank that borrowed short-term but lent long-term at fixed rates faces inflation risk: if inflation rises sharply, the fixed-rate loans don't rise, but their funding costs do (assuming they refinance at higher rates).

An inflation swap lets these parties hedge that risk. Instead of buying [TIPS](/wiki/tips/) (inflation-linked Treasury bonds) or other inflation-protected securities, they can enter a swap and get a tailored exposure to inflation without holding bonds.

## Structure

An inflation swap has:

**Fixed leg**: Party A pays a fixed rate (the "inflation swap rate") once a year or twice a year.

**Inflation leg**: Party B pays the inflation rate, typically calculated as the percentage change in the Consumer Price Index (CPI) over a specified period (usually one year).

The payments are usually net-settled in cash. If inflation was 5% and the fixed swap rate was 3%, Party A pays the difference (2%) times the notional to Party B. Conversely, if inflation is 1%, Party B pays 2% to Party A.

## Two types: year-on-year and zero-coupon

**Year-on-year inflation swaps**: The inflation rate is the annual percentage change in CPI (e.g., January CPI / January previous-year CPI - 1). The swap resets and settles every year. Common for shorter-dated swaps.

**Zero-coupon inflation swaps**: No interim cash flows. A single payment occurs at maturity, equal to the cumulative inflation from the start of the swap to maturity, applied to the notional principal. A 5-year zero-coupon inflation swap settles at maturity based on the total cumulative inflation over the 5 years.

Zero-coupon swaps are more common in longer-dated exposures because they avoid the cash-management complexity of annual resets.

## Valuation and pricing

An inflation swap is priced by:

1. **Forward inflation expectations**: Dealers estimate the expected inflation rate at each reset date using:
   - Breakeven inflation rates implied by the difference between Treasury yields and TIPS yields.
   - Market-traded inflation derivatives and swaps.
   - Economic forecasts and models.

2. **Discount rates**: Both legs are discounted using real (inflation-adjusted) discount rates for the inflation leg and nominal (conventional) rates for the fixed leg.

3. **Solving for the fixed rate**: The inflation swap rate is set so that the present value of the fixed leg equals the expected present value of the inflation leg.

The inflation swap rate is typically close to the breakeven inflation rate, but not identical, because of:
- Convexity: volatility in inflation affects the swap value.
- Liquidity premium: the fixed leg of an inflation swap is less liquid than a Treasury bond.
- [Counterparty risk](/wiki/counterparty-risk/): the dealer's credit spread.

## Common uses

**Pension funds**: A pension that owes retirees inflation-linked annuities enters an inflation swap to hedge the liability. If inflation rises, the pension's payments rise, but the swap receives more from the floating leg, offsetting the cost.

**Insurance companies**: Insurers that sold inflation-linked products (e.g., inflation-adjusted annuities) use swaps to manage the inflation risk without buying a large portfolio of TIPS.

**Asset-liability matching**: A firm with fixed-rate assets but inflation-linked liabilities (or vice versa) uses an inflation swap to synchronize them.

**Inflation positioning**: A trader who believes inflation will rise faster than the market expects can receive inflation (go long) in a swap. If actual inflation exceeds the swap rate, they profit.

**Central banks and sovereigns**: Central banks sometimes trade inflation swaps for policy or hedging purposes. Sovereigns that have inflation-linked debt might hedge with swaps.

## Advantages over TIPS and other instruments

**Customization**: You can set the maturity and notional to exactly match your exposure. TIPS are issued in standard tenors.

**No duration extension**: A TIPS bond extends in maturity if inflation is high (because the principal grows). An inflation swap is fixed-maturity, so no extension.

**Efficient capital use**: You don't need to buy and finance $100 million of bonds; you enter a swap with minimal collateral.

**Liquid across maturities**: While TIPS are concentrated in a few on-the-run maturities, inflation swap dealers quote rates for nearly any maturity.

## Risks

**Inflation forecast risk**: The valuation depends on market expectations of future inflation. If inflation surprises, the swap's value swings.

**Basis risk**: The swap rate is tied to an index (e.g., CPI), but your actual economic exposure might differ. A company that pays workers based on regional wage inflation might find that CPI doesn't match their actual cost increases.

**Timing risk**: Year-on-year swaps reset at fixed dates (e.g., January). If inflation spikes after the reset, you don't capture it until the next reset.

**Lag risk**: CPI is published with a lag (usually mid-month for the prior month). If the swap relies on the published CPI for that month's value, you have timing mismatches.

**Counterparty risk**: The dealer might default, especially in a period of high volatility and large swap values.

**Model risk**: Valuation depends on forward inflation forecasts, which are models. Different models give different prices, leading to wide bid-ask spreads.

## Market conventions

- **Typical maturities**: 5, 10, 15, 20, 30 years. Longer maturities for pension and insurance liabilities.
- **Notional**: Often very large ($100 million+) because inflation exposure is measured in notional terms.
- **Settlement**: Year-on-year swaps settle annually. Zero-coupon swaps settle at maturity.
- **Index**: Most common in the U.S. is CPI. Other regions use their local inflation measures.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the foundational structure.</li>
<li><a href="/wiki/interest-rate-swap/">Interest-rate swap</a> — the single most common swap type.</li>
<li><a href="/wiki/tips/">TIPS</a> — Treasury Inflation-Protected Securities, an inflation-linked bond alternative.</li>
<li><a href="/wiki/commodity-swap/">Commodity swap</a> — similar OTC derivative for commodity prices.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/inflation/">Inflation</a> — the economic phenomenon the swap hedges or positions on.</li>
<li><a href="/wiki/consumer-price-index/">Consumer Price Index</a> — the index the swap is typically tied to.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the primary risk in OTC swaps.</li>
<li><a href="/wiki/duration/">Duration</a> — the interest-rate sensitivity component of inflation swap risk.</li>
</ul>
</div>
