---
title: "Cross-Hedging with Futures"
description: "Cross-hedging uses futures on a correlated but different asset to hedge exposures when no direct futures contract exists."
keywords:
  - cross hedging
  - cross hedge futures
  - basis risk
  - hedge ratio
  - imperfect hedge
  - commodity hedging
---

*Cross-hedging with futures is a technique for protecting against price risk on an asset when no futures contract on that exact asset exists. You instead use futures on a highly correlated asset—a proxy—accepting some residual basis risk in exchange for actual hedging capability.*

<div class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Hedging — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Hedging with a correlated but different asset when direct futures unavailable.</div>

|   |   |
|---|---|
| **Core concept** | Use a related futures contract to hedge an unrelated or illiquid exposure |
| **Key challenge** | [Basis risk](/basis-risk/) — the proxy doesn't track perfectly |
| **Calculation** | Hedge ratio = correlation × (volatility of position / volatility of futures) |
| **Common examples** | Jet fuel hedged with crude oil, copper hedged with generic metals |
| **Residual risk** | Spread between the two assets can move against you |
| **Effectiveness** | Depends on correlation strength and contango/[backwardation](/backwardation/) alignment |

</aside>

## When Direct Hedges Don't Exist

A regional heating-oil distributor faces risk on its inventory, but has no liquid futures on home heating oil—the volumes are tiny. Instead, it buys [crude oil futures](/futures-contract/), which are liquid and move in lockstep with refined products. An airline manufactures jet fuel but can hedge with crude oil or, if crude is imperfect, with a broader energy index. A foreign subsidiary with revenue in the Brazilian real might hedge using the Mexican peso, if the real has no liquid forwards.

The cross-hedge is imperfect. Heating oil doesn't track crude perfectly; the cracking spread (the profit a refiner makes from cracking crude into gasoline and diesel) widens and narrows. The jet fuel price diverges from crude when regional jet fuel supply tightens. The real-peso correlation can break during currency crises. But an imperfect hedge is usually better than none.

## The Hedge Ratio

To set up a cross-hedge, you need to size the futures position correctly. If you have 100,000 barrels of heating oil and want to hedge with crude futures, buying 100,000 barrels of crude futures is a naive starting point—but it only works if heating oil and crude track perfectly. They don't.

The correct sizing formula is:

**Hedge Ratio = Correlation × (Volatility of position / Volatility of futures)**

If heating oil and crude correlation is 0.95, heating oil volatility is 15%, and crude volatility is 18%, then:

Hedge Ratio = 0.95 × (15% / 18%) = 0.79

You'd buy 79,000 barrels of crude futures (not 100,000) to hedge the 100,000-barrel heating oil position. This accounts for the fact that heating oil is slightly less volatile and not perfectly correlated. Buying fewer futures contracts limits the upside capture on a downturn but also reduces the downside loss on an upturn—it's a trade-off.

## Basis Risk in Cross-Hedges

The residual risk after hedging—the difference between how much your position loses and how much the hedge gains—is called [basis risk](/basis-risk/). In a perfect hedge, basis risk is zero. In a cross-hedge, it's always positive.

For heating oil hedged with crude, the spread (heating oil price minus crude price, or "crack spread") can widen or narrow. If you're short heating oil and long crude futures, a widening crack spread hurts: your heating oil declines in value faster than crude, so the futures hedge doesn't fully protect you. This is the core risk of cross-hedging.

During normal times, the crack spread is stable, averaging around $0.10–0.25 per barrel. But during supply shocks—a refinery fire, a geopolitical disruption—cracks can blow out. A significant refining disruption might widen cracks by \$0.50, leaving a cross-hedger partially exposed.

## Calculating Optimal Hedge Ratios

Institutional hedgers use regression analysis to estimate the hedge ratio precisely. They regress historical price changes of the position against price changes of the proposed futures contract. The regression slope *β* tells you how sensitive the position is to futures moves.

If heating oil returns move 0.79× as much as crude returns (and correlation is 0.95), then *β* = 0.79, and you hedge 79% of the position. Running monthly or quarterly regressions on 3–5 years of data gives a robust estimate.

More sophisticated approaches use value-at-risk (VaR) optimization or scenario analysis. You might stress-test: if the crack spread widens by \$0.50 tomorrow, how much money do I lose? How many crude contracts do I need short to break even? This dynamic method adjusts the hedge ratio as spreads change.

## Choosing the Right Proxy Asset

The most successful cross-hedges use assets with high, stable correlation and deep liquidity. Crude oil and heating oil: correlation ~0.92, crude is among the most liquid futures. Copper and generic metals indices: correlation ~0.85. The US dollar and other major currencies: correlation ~0.70+.

Weak cross-hedges—like trying to hedge a specialized chemical with general oil prices, or a small-cap emerging market currency with a basket of developed-market currencies—often fail. The correlation is too low, or it breaks exactly when you need it most.

Geographic proximity helps. A Philippine shipper can better hedge peso risk with the Singapore dollar (neighboring currency, trade ties) than with the Korean won (fewer shared supply chains). An Indian textiles exporter hedges cotton price risk well with US cotton futures (global commodity, high correlation) but poorly with polyester (different supply chain, weak link).

## When Cross-Hedges Break Down

Basis risk materializes hardest during crises. In March 2020, when COVID-19 lockdowns hit, correlations between assets shifted and spread relationships blew out. Airlines hedging jet fuel with crude oil found that jet demand collapsed far faster than crude demand; the hedge protected less than expected.

During financial crises, even highly correlated assets can decouple. Bank stocks and financial derivatives often move together, but during banking panics, credit spreads spike, and a financial company hedged with a broad equity index suddenly faces losses on both sides.

Supply shocks are another weak point. If the position is long copper ore (waiting to be processed) and you hedge with copper futures (which reflect processed copper prices), a sudden jump in refining costs widens the spread, and your hedge is partially useless. You bet on correlation; the market bet on absolute price levels.

## The Role of Volatility and Correlation Stability

Successful cross-hedges depend on both correlation and volatility remaining relatively stable. In normal markets, copper and nickel move together (correlation 0.65–0.75). During a copper shortage when nickel demand stays soft, that correlation collapses to 0.2. A nickel miner hedging with copper futures suddenly finds the hedge broken.

This is why institutional treasurers and risk managers rebalance hedge ratios regularly. They monitor rolling correlations and regressions, sometimes quarterly or monthly. If a correlation that was 0.9 drops to 0.7, they adjust the position—either increasing or decreasing the futures hedge, or swapping to a different proxy asset.

Some firms use dynamic hedging: they adjust the hedge ratio daily or weekly based on real-time correlation estimates. This adds cost—transaction fees and slippage—but can prevent surprises.

## Practical Examples Across Industries

**Airlines:** Hedge jet fuel exposure with crude oil futures (correlation ~0.93). The crack spread is the residual risk.

**Aluminum smelters:** Hedge bauxite ore prices with aluminum futures (correlation ~0.70). Ore and finished metal don't track perfectly because refining costs and technology add a spread.

**Shipping companies:** Hedge fuel costs with oil futures and currency risk with currency forwards (correlation depends on trade routes).

**Emerging-market corporates:** Hedge revenue in a weak currency (say, Turkish lira) with major-currency futures (EUR or USD) or cross-pairs. Correlation to exact exposure is imperfect but better than unhedged.

**Agricultural processors:** Hedge corn inputs with corn futures (correlation ~0.95, relatively stable). Hedge soybean meal byproducts with soybean futures (correlation ~0.85) or wheat futures (lower).

## The Cost-Benefit Trade-Off

Cross-hedging is cheaper than buying custom OTC derivatives, but more expensive and riskier than hedging with a perfect futures contract. The cost is paid in basis risk—the possibility that your proxy asset moves differently than your actual exposure, leaving you partially unprotected.

A wheat processor buying wheat futures can hedge nearly perfectly; basis risk is minimal because they're hedging the same commodity. An agricultural firm hedging a mixed crop portfolio with wheat and corn futures accepts more basis risk because the crop mix is a custom blend. A company hedging a unique commodity with a generic index accepts even more.

The decision to cross-hedge depends on the alternatives: Is the exposure material enough to justify a custom OTC hedge with a bank (expensive and illiquid)? Is the basis risk acceptable given your risk tolerance? Would leaving the position unhedged and taking the financial hit be worse? Often, a cross-hedge—even an imperfect one—beats these alternatives.

## Monitoring and Adjusting

The best cross-hedges are actively managed. You monitor:

- **The correlation:** Is the proxy still moving with your position?
- **The basis:** How wide is the spread, and is it widening?
- **Volatility:** Has the position become more or less volatile?
- **The hedge ratio:** Does your regression estimate suggest a different position sizing?

If any of these shift materially, rebalancing may be needed. A hedge that was optimal three months ago might be underwater today if correlations have collapsed or spreads have blown out. Professional hedgers review these metrics at least quarterly, sometimes monthly.

## See also

<div class="wiki-seealso">

### Closely related

- [Basis Risk](/basis-risk/) — residual risk from mismatch between position and hedge
- [Futures Contract](/futures-contract/) — standardized instruments used as hedging proxies
- [Derivatives Hedging](/derivatives-hedging/) — broader framework for using derivatives to manage risk
- Hedge Ratio — calculating optimal sized hedge positions
- [Forward Contract](/forward-contract/) — OTC alternative to cross-hedging with futures

### Wider context

- Correlation — statistical relationship between position and futures price
- [Value at Risk](/value-at-risk/) — measuring and managing residual hedge risk
- Commodity Markets — where proxies (crude, metals, grains) trade
- [Volatility Smile](/volatility-smile/) — how volatility patterns affect hedge effectiveness
- [Treasury Bond](/treasury-bond/) — another cross-hedge proxy for general interest-rate risk

</div>
