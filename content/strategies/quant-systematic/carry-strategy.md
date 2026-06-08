---
title: "Carry Strategy"
description: "Harvesting yield differentials by longing high-carry assets and shorting low-carry assets across currencies, bonds, and commodities."
keywords:
  - carry strategy
  - yield harvesting
  - currency carry
  - cross-asset carry
  - convergence trading
image: "/svg/strategies.svg"
---

*A **carry strategy** profits from the yield or convenience return of an asset, typically by holding (or going long) an asset that pays a premium and funding that position at a lower cost. The classic example is the [currency carry trade](/carry-strategy/)—borrowing in a low-interest-rate currency and lending in a high-rate currency—but carry principles apply across [bonds](/bond/), commodities, and equities.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Carry Strategy — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for systematic trading strategies." />

<div class="wiki-infobox-caption">A principal arbitrage of yield differentials; profitable in stable regimes, vulnerable to sudden reversals.</div>

|   |   |
|---|---|
| **Core mechanism** | Long high-yield asset, finance at lower rate |
| **Primary markets** | Currency, bonds, commodities, equity [dividend](/dividend/) spreads |
| **Funding source** | Repo markets, [libor](/libor/) rates, or lower-yielding collateral |
| **Return drivers** | Yield pickup + [price appreciation](/price-to-earnings-ratio/) (or depreciation) |
| **Rebalance frequency** | Daily to monthly |
| **Key risk** | Regime change; funding crisis; correlation breakdown |

</aside>

## The core principle

A carry strategy exploits the difference between the return you earn from holding an asset and the cost of financing that position. If a [treasury bond](/treasury-bond/) yields 4% and you can borrow at 3%, you pocket 1% annually—plus or minus [price appreciation](/price-to-earnings-ratio/) or depreciation.

The beauty of carry is that it requires no view on future prices. You are indifferent to whether the asset rises or falls, provided it does not move too much. You are simply collecting the spread. This contrasts sharply with directional bets (which demand that you predict price direction) and with [pairs trading](/pairs-trading/) (which demands mean reversion).

Carry is often called a "convergence trade" or "basis trade." The spread between the yield and the funding cost is the basis. Over time, carry traders expect the basis to persist (hence the return accumulates) or to tighten favourably. In normal markets, this works. In crisis, the basis can blow out catastrophically, causing large losses.

## Currency carry in depth

The [currency carry trade](/carry-strategy/) is the most famous variant. In the early 2000s, when the [Japanese yen](/japanese-yen/) yielded near zero and the [Australian dollar](/australian-dollar/) yielded 4–5%, investors could borrow yen, convert to Australian dollars, and collect 4–5% annual return with virtually no [currency risk](/currency-risk/) if the exchange rate remained stable.

This worked for years. Billions of dollars flowed into high-yielding emerging-market currencies and commodities. But when crisis hit—2008, 2011, 2020—the carry trade unwound ferociously. Investors liquidated their high-yield positions to cover losses elsewhere, flooding the market with sell orders. The currency spiked upward (against the yen), losses mounted, and forced liquidations accelerated. The correlation between carry flows and [currency risk](/currency-risk/) became dramatically positive—exactly when diversification was most needed.

The carry trade is profitable in long stretches but occasionally delivers massive drawdowns. [Hedge funds](/hedge-fund/) and institutional investors run carry strategies; some blow up when unexpected [tail risk](/tail-risk/) materializes.

## Bond carry

A [bond](/bond/) carry strategy borrows short-term (via repo markets or [libor](/libor/)) to finance long-dated [bond](/bond/) holdings. If the [yield curve](/yield-curve/) is steeply sloped (long bonds yield much more than short rates), the strategy earns the spread. This is called "roll-down" or [duration](/duration/) capture.

Over the past two decades, bond carry was lucrative: borrowing at 0–2% and buying 10-year [treasuries](/treasury-bond/) yielding 3–4%. But bond carry also faces [duration risk](/duration/) and [interest-rate risk](/interest-rate-risk/). If [rates](/interest-rate/) rise 100 basis points, the 10-year [bond](/bond/) declines sharply, wiping out the carry profit and more. Long-duration positions financed short-term are vulnerable to sudden [curve](/yield-curve/) flattening or [rate](/interest-rate/) shocks.

A variant: buy [corporate bonds](/corporate-bond/) (higher yield) and short [government bonds](/treasury-bond/) (lower yield) of the same duration. You harvest the [credit spread](/credit-spread/), but you face [credit risk](/credit-risk/) if the issuer deteriorates.

## Commodity and equity carry

**Commodity carry.** A [oil](/crude-oil/) or [agricultural](/corn/) future trading in [contango](/contango/) (forward prices higher than spot) creates carry opportunity. Buy spot [oil](/crude-oil/) and sell a forward, locking in the carry. This is how commodity indices function: they repeatedly sell near-term futures and buy deferred ones, harvesting the [contango](/contango/) spread. In [backwardation](/backwardation/), carry is negative, and the strategy loses money.

**Equity dividend carry.** Stocks paying high [dividends](/dividend/) finance short positions in lower-dividend stocks. Many [yield funds](/income-fund/) and international [dividend](/dividend/) strategies use this. The carry comes from the [dividend yield](/dividend-yield/) difference. Risk: growth stocks (low [dividend](/dividend/) yield) appreciate, while dividend-paying stocks stagnate or decline.

## Risk and regime sensitivity

Carry strategies are deceptively simple but harbour hidden risks.

**Funding risk.** If your financing dries up (repo markets freeze, [libor](/libor/) spikes, counterparties withdraw credit), you are forced to liquidate at the worst time. The 2008 financial crisis and 2020 March panic both crushed carry trades via funding shocks.

**Correlation breakdown.** Carry strategies often implicitly assume that the high-yield asset and the funding asset are uncorrelated. In reality, both respond to risk appetite. In risk-off environments, funding rates rise (cost of borrow increases), and high-yield assets fall simultaneously. The correlation flips from near-zero to strongly positive, amplifying losses.

**Tail risk.** Carry strategies often deliver small, steady gains punctuated by rare, severe drawdowns. A tail-hedging cost (buying [out-of-the-money](/out-of-the-money/) [options](/option/) or [volatility](/volatility-smile/) insurance) can improve risk-adjusted returns, but it eats into the carry profits.

**Model risk.** Carry traders often rank assets by their historical yield and overweight the highest carriers. In backtests, this works. But if carry returns are mean-reverting (today's highest-carry assets underperform tomorrow), the strategy underperforms.

## Cross-asset carry frameworks

Modern carry strategies blend signals across currencies, bonds, and commodities into a single framework. The idea: carry is a universal principle. Assets offering the best risk-adjusted carry, wherever they exist, should be overweighted. This reduces dependence on any single market's carry premium and improves diversification.

Implementation requires a consistent measure of carry across asset classes—usually the [dividend yield](/dividend-yield/) for equities, [coupon](/coupon-payment/) minus funding rates for bonds, and [forward](/forward-contract/) premium for currencies and commodities. Weights are often adjusted dynamically based on [volatility](/volatility-smile/), with high-volatility assets receiving smaller positions to keep portfolio volatility constant.

## Profitability and practical considerations

[Carry strategy](/carry-strategy/) performance varies dramatically by period. During low-volatility, risk-on environments, it is one of the best-returning strategies. During crises, it is among the worst. Over full market cycles, robust, diversified carry strategies have delivered 4–8% annually (before fees) with [Sharpe ratios](/sharpe-ratio/) around 0.5–0.8—respectable, but not exceptional.

**Costs erode returns.** [Bid-ask spreads](/bid-ask-spread/), repo fees, [borrowing costs](/cost-of-debt/), and taxes take a bite, especially for frequent rebalancing. Low-cost systematic implementation (via [futures](/futures-contract/) or [ETFs](/etf/)) is preferable to ad-hoc manual trading.

**Scale matters.** Huge positions in carry trades can become self-defeating: your entry and exit orders move the markets against you. Many carry strategies are crowded, and flows reverse abruptly when sentiment shifts.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — when forward prices exceed spot; creates positive carry opportunity
- [Backwardation](/backwardation/) — when forward prices are below spot; carry is negative
- [Dividend yield](/dividend-yield/) — the income component of equity carry
- [Credit spread](/credit-spread/) — the yield premium of corporate over government bonds
- [Duration](/duration/) — the sensitivity of bond prices to rate moves; key to bond carry risk
- [Kalman filter trading](/kalman-filter-trading/) — dynamic filtering for stable carry estimates
- [Factor timing](/factor-timing/) — systematic allocation to factors; similar philosophy

### Wider context

- [Libor](/libor/) — the funding benchmark for carry traders
- [Currency risk](/currency-risk/) — a key risk in multi-currency carry portfolios
- [Tail risk](/tail-risk/) — the drawdown risk of carry strategies
- [Hedge fund](/hedge-fund/) — institutional vehicle for carry trading
- Repo market — the financing backbone for bond and equity carry

</div>
