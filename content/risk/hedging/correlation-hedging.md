---
title: "Correlation Hedging"
description: "Protecting a portfolio against unexpected changes in the statistical relationships between asset returns using correlation swaps."
keywords:
  - correlation swap
  - portfolio correlation risk
  - statistical dependence
  - diversification breakdown
  - dispersion trading
image: "/svg/risk.svg"
---

*A **correlation hedge** is a derivative strategy that protects against changes in how assets move together. Most portfolios assume that [diversification](/diversification/) reduces [idiosyncratic-risk](/idiosyncratic-risk/), but when correlations rise—especially during market stress—assets that should move independently start moving in tandem, and diversification fails. A correlation swap lets investors lock in or offload that risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Correlation Hedging — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark denoting risk and hedging strategies." />

<div class="wiki-infobox-caption">Correlation hedges protect against the statistical dependence between asset returns.</div>

|   |   |
|---|---|
| **What it is** | A derivative contract tied to the realised or implied correlation between two or more underlyings |
| **Also called** | Correlation swap, dispersion hedge, correlation trading |
| **Key premise** | Diversification benefit erodes when correlations spike during market stress |
| **Measured in** | Percentage points (correlation ranges from 0 to 1) |
| **Used by** | [Hedge funds](/hedge-fund/), [asset managers](/asset-allocation/), [banks](/bank-of-america/) trading volatility, and portfolio insurers |
| **Related instruments** | [Option](/option/) (implied vol skew), [variance swap](/variance-swap/), [stress test](/stress-testing/) |

</aside>

## Why correlations matter for portfolios

A textbook portfolio holds stocks and bonds that move in opposite directions, lowering overall [volatility](/volatility-smile/). A 60/40 equity-bond split should dampen swings relative to a pure equity portfolio. But this diversification benefit rests on a hidden assumption: that the correlation between equities and bonds stays roughly constant. In reality, correlations are not fixed. During a [recession](/recession/), bonds and stocks can both fall as [interest-rate](/interest-rate/) expectations shift upward and [credit-risk](/credit-risk/) spreads widen. During a geopolitical crisis, previously uncorrelated assets suddenly move together as investors flee to safety.

When correlation rises unexpectedly, a portfolio's [volatility](/historical-volatility/) jumps even if the individual assets' volatilities have not changed. A portfolio manager who believed they were protected by diversification suddenly faces much larger drawdowns. The hedging ratio is wrong, the strategy is exposed, and the [value-at-risk](/value-at-risk/) model is too optimistic. This is correlation risk, and it is distinct from and often larger than the [market-risk](/market-risk/) of the portfolio itself.

## The correlation swap: locking in dependence

A correlation swap is the standard tool for hedging this. In its basic form, the swap is a contract between two counterparties: one pays a floating leg equal to the realised correlation between a basket of stocks (or any two underlyings) over the contract period, and the other pays a fixed correlation level that both parties agree on at the start.

For example, an asset manager enters a correlation swap on the [S&P 500](/sp-500-index/) stocks, agreeing to pay 0.60 (60 per cent implied correlation) and receive the realised correlation over six months. If the stocks move tightly together and the realised correlation comes in at 0.70, the manager pays the difference on a notional amount. If correlations fall to 0.45, the manager receives. By locking in 0.60, the manager has insured against an unexpected spike in interdependence.

The payout is often squared and calculated on a dispersion index or on variance-based measures. A basket of stocks with low dispersion—they all move together—has low correlation; a basket with high dispersion—some stocks surge while others fall—has high correlation. The math is subtle, but the intuition is simple: if your portfolio benefits from diversification, you are implicitly short correlation, and a swap transfers that risk to someone willing to take it.

## Why correlation risk exists: loss of independence

Correlation risk stems from several sources. First, during market downturns, investors' risk appetite declines uniformly, pushing all risky assets down together. [Equities](/common-stock/), [high-yield bonds](/high-yield-bond/), and [commodities](/crude-oil/) all become correlated with downside shocks. Second, central-bank policy can induce correlation; when [quantitative easing](/quantitative-easing/) floods the system with liquidity, all assets rally, and their movements become synchronised. Third, technical factors—quant fund crowding, passive-index inflows, [leverage](/leverage-ratio-forex/) unwinds—can force sales across asset classes, raising correlations mechanistically.

Crucially, correlations are lowest in benign times and highest when you need diversification most. A hedge that costs money every year in a bull market may save a portfolio's life in a crash. This is a classic insurance dynamic: you pay in calm periods and collect in crises.

## Dispersion trading: the flip side

If correlation hedging is about paying to lower your exposure to correlation risk, dispersion trading is the opposite. A dispersion trader believes that implied correlations (priced into options and swaps) are too high relative to what future realised correlations will be. They sell correlation swaps (receiving the fixed leg, paying realised) and simultaneously hedge their [delta](/delta/) and [vega](/vega/) exposure using single-name [options](/option/). If realised correlation comes in lower than implied, the dispersion trade profits.

Dispersion trades are common in equity derivatives markets and require sophisticated hedging. A trader who is short correlation but delta-neutral is essentially betting on the third and fourth moments of return distributions—skew and kurtosis—as well as the realised vol surfaces of the individual stocks. Many [hedge funds](/hedge-fund/) and volatility specialists make this bet.

## Correlation baskets: which assets?

A correlation swap can be on any pair or basket of underlyings: equity indices, currencies, commodities, [bond](/bond/) yields, or a mix. An equity-bond correlation swap is useful for institutional investors worried about the classic diversification benefit breakdown. A commodity-equity correlation swap hedges the risk that inflation shocks drive both bond yields and stock prices downward (historically rare, but possible). A [currency](/currency-risk/)-commodity correlation swap is relevant for multinational firms that earn in foreign currencies and face commodity price volatility.

The choice of basket determines the hedge's effectiveness. If a portfolio manager holds ten specific stocks but hedges correlation on the broad [S&P 500](/sp-500-index/), the hedge is imperfect; the stocks' individual [idiosyncratic-risk](/idiosyncratic-risk/) matters. Tighter, custom baskets offer better protection but are harder to trade and more expensive.

## Cost and counterparty exposure

Correlation swaps, like all [over-the-counter-market](/over-the-counter-market/) derivatives, incur bid-ask spreads and require collateral posting. The cost of a hedge—the fixed correlation leg you pay—reflects the market's consensus about future correlation risk and the [counterparty-risk](/counterparty-risk/) premium. In a stressed market, implied correlations spike, and hedging becomes expensive exactly when you need it most. A manager who waits to hedge until correlations are high pays a premium.

[Counterparty risk](/counterparty-risk/) is also elevated because correlation swaps often involve major [banks](/bank-of-america/) or [hedge funds](/hedge-fund/) with leverage. A correlation swap with a bankrupt counterparty becomes a claim in a queue of creditors, not a reliable hedge. Diversifying counterparties and using [central clearing](/central-bank/) reduce this risk but are not always available, especially for bespoke baskets.

## Limitations and alternative hedges

Correlation hedges do not protect against extreme [tail-risk](/tail-risk/) events, where correlations approach 1.0 and no diversification remains. A [protective-put](/protective-put/) on the overall portfolio may be more cost-effective for very bad outcomes, though puts on broad indices are not perfectly correlated with your specific holdings either.

Additionally, correlation swaps assume that past [historical-volatility](/historical-volatility/) and correlation patterns persist. In a regime shift—a new geopolitical threat, a monetary-policy reversal—both volatility and correlation can change structurally. Static correlation hedges can become obsolete, and dynamic rebalancing is necessary but expensive.

## See also

<div class="wiki-seealso">

### Closely related

- [Diversification](/diversification/) — the portfolio strategy that correlation hedges protect
- [Quanto hedging](/quanto-hedging/) — hedging the correlation between an asset and its currency
- [Cross-currency basis hedging](/cross-currency-basis-hedging/) — hedging correlation-like risks in foreign funding
- [Volatility smile](/volatility-smile/) — related pricing anomaly in [option](/option/) markets
- [Value-at-risk](/value-at-risk/) — risk model that depends on correlation assumptions
- [Variance swap](/variance-swap/) — a related derivative tied to realised volatility
- [Stress testing](/stress-testing/) — analysis of how correlations break down in crises

### Wider context

- [Hedge fund](/hedge-fund/) — major users of correlation hedges and dispersion trades
- [Asset allocation](/asset-allocation/) — strategic framework that correlation risk threatens
- [Systemic risk](/systemic-risk/) — correlation spikes are a hallmark of system-wide crises
- [Market risk](/market-risk/) — broader category of portfolio risks
- [Idiosyncratic risk](/idiosyncratic-risk/) — company-specific risk that correlation hedges do not address

</div>
