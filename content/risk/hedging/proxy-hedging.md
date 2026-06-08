---
title: "Proxy Hedging"
description: "Using a liquid, correlated instrument to hedge an exposure that is illiquid, bespoke, or non-tradable."
keywords:
  - proxy hedging
  - cross-hedge
  - basis risk
  - correlated instruments
  - illiquid exposures
image: "/svg/risk.svg"
---

*A **proxy hedge** replaces a direct offset with a surrogate: you buy or sell a liquid, correlated instrument when the true underlying cannot be traded efficiently or at all. The gap between your hedge and your exposure—the basis—is the cost of using the imperfect substitute.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Proxy Hedging — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk and hedging." />

<div class="wiki-infobox-caption">A practical second-best when the ideal hedge doesn't exist or costs too much to execute.</div>

|   |   |
|---|---|
| **What it is** | Using a correlated but distinct instrument to offset risk in an illiquid or non-tradable underlying |
| **Also called** | Cross-hedge, surrogate hedge, proxy offset |
| **Why it matters** | Allows hedging of bespoke, illiquid, or outright non-tradable exposures |
| **Key risk** | [Basis risk](/basis-risk/) — mismatch between hedge movement and underlying movement |
| **Common use** | Hedging physical commodity holdings, private assets, or customised liabilities |
| **Typical instruments** | Index futures, [ETFs](/etf/), [options](/option/), swaps on related underlyings |

</aside>

## When the real thing is unavailable

Not every exposure can be hedged directly. A wheat farmer in Manitoba cannot short individual futures on her farm's grain at harvest. A private equity sponsor cannot trade puts on a company inside their portfolio. A corporation with a rare, complex interest-rate liability cannot find a counterparty willing to sell a bespoke swap on precisely those terms. Enter the proxy: a publically traded, liquid instrument that moves roughly in tandem with the unhedgeable exposure.

The farmer might buy put options on [wheat futures](/corn/) instead of hedging her physical holding directly. The PE sponsor might short [S&P 500 futures](/sp-500-index/) to hedge a portfolio concentrated in technology companies. The corporation might hedge via [interest-rate swaps](/interest-rate/) on standard tenors and floating-rate references. None of these is a perfect match. But when the true underlying is illiquid, bespoke, or non-tradable, the proxy is often the only game in town.

## Basis: the permanent tension

The essence of proxy hedging is **basis risk**. You own an exposure in asset A; you hedge by trading asset B. As long as A and B are not identical, they will move differently. The difference—called the basis—is your residual risk.

Suppose you hold a privately placed bond. The issuer is not widely followed; there's no liquid secondary market. You cannot sell short a short-dated put on the exact bond. Instead, you might short [corporate bond index futures](/corporate-bond/) or enter a [credit default swap](/credit-risk/) on a lower-rated public peer with similar leverage and industry. These proxies are liquid and transparent, but they do not track your private holding perfectly. If credit spreads widen, the proxy may fall harder than your bond, leaving you under-hedged. If spreads narrow and your bond is repriced upward due to issuer-specific news, the proxy gains less, and you've bought unnecessary insurance.

Most proxy hedges carry two sources of basis risk: **systematic** basis (the beta of A against B, which is predictable) and **idiosyncratic** basis (issuer-specific, event-driven, or correlation-breakdown moves that are not). The systematic basis can often be estimated and adjusted for. Idiosyncratic basis is harder to forecast and is where proxy hedges tend to disappoint.

## Choosing the proxy

A good proxy should be correlated with your exposure over the relevant time horizon, liquid enough to trade at tight [bid-ask spreads](/bid-ask-spread/), and transparent in pricing and risk characteristics.

Commodity producers often use futures on major [exchanges](/stock-exchange/) as proxies. A copper mine in Peru might hedge via London Metal Exchange copper futures, even if the local concentrate has slightly different metallurgy and logistics costs. The correlation is high; the liquid hedge is standard. An oil producer in a remote region might use [crude oil](/crude-oil/) futures because regional crude has a local price premium or discount that is relatively stable.

Equity proxies are common in concentrated portfolios. A holding company with a large stake in a single tech stock cannot short the individual stock without triggering disclosure or lending restrictions. Shorting the [Nasdaq-100 index](/nasdaq/) or a [semiconductor sector ETF](/equity-etf/) provides partial protection, with known correlation to the concentrated position.

In credit, proxies proliferate. A bank may hedge a private credit exposure using [high-yield bond ETFs](/high-yield-bond/) or credit indices. A pension fund holding a mix of corporate bonds cannot hedge every holding directly; it uses [bond ETFs](/bond-etf/) or [credit derivatives](/credit-risk/) on baskets of liquid issuers.

## The calculation and adjustment

To size a proxy hedge, you estimate the correlation or beta between your exposure and the proxy, then scale the hedge notional accordingly. If your private equity holding has a 1.2 beta to the broad market, you short 1.2 units of market exposure per unit of holding. If a physical commodity's local price moves 0.8 times the futures price (due to basis factors like transport and storage), you hedge 0.8 units of futures per unit of physical.

These ratios are not static. As market structure, liquidity, or fundamentals change, correlations drift. A diligent hedger re-estimates the hedge ratio periodically and rebalances. This rebalancing, though necessary, introduces transaction costs and may lock in basis losses or gains.

## Why proxy hedges remain imperfect

Even a well-sized proxy hedge will underperform or overperform relative to an ideal direct hedge. This is not a defect of the hedger's skill but a mathematical truth: two imperfectly correlated instruments will diverge. The residual risk—basis risk—is the price paid for using a substitute.

In severe market dislocations, basis risk amplifies. Liquidity evaporates; correlations break down. During the 2008 financial crisis, many proxies that had moved together for years decoupled. A fund hedging illiquid mortgage exposures with [Treasury bonds](/treasury-bond/) found that the hedge fell in value just as the underlying exposure tumbled, offering no protection when it mattered most.

Despite these limitations, proxy hedges are ubiquitous and often unavoidable. The alternative—remaining unhedged—is often worse. A partial hedge via a liquid proxy is usually superior to no hedge at all.

## See also

<div class="wiki-seealso">

### Closely related

- [Basis risk](/basis-risk/) — the mismatch between a hedge and its underlying exposure
- [Gamma hedging](/gamma-hedging/) — managing the rate of change of a hedge as prices move
- [Duration hedging](/duration-hedging/) — hedging interest-rate sensitivity via duration matching
- [Convexity hedging](/convexity-hedging/) — adjusting hedges for second-order price sensitivity
- Cross-hedge — hedging one asset with a futures contract on a different but correlated asset
- Hedging — general offsetting of market risk via financial instruments

### Wider context

- Derivative — financial instruments used for hedging and speculation
- [Liquidity risk](/liquidity-risk/) — risk that an instrument cannot be sold or bought without significant cost
- Correlation — statistical measure of how two assets move together
- [Over-the-counter market](/over-the-counter-market/) — decentralised market for bespoke and illiquid instruments
- Risk management — broad discipline of identifying and offsetting financial risk

</div>
