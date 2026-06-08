---
title: "Futures Carry Decomposition"
description: "Breaking down the cost of carry in commodity futures into financing, storage, convenience yield, and insurance components to explain curve slope and pricing."
keywords:
  - carry decomposition
  - cost of carry
  - storage costs
  - convenience yield
  - financing costs
  - commodity futures basis
image: "/svg/commodities.svg"
---

*The **cost of carry** in commodity [futures](/futures-contract/) is not a single number but a layered set of real and opportunity costs that collectively explain why a futures curve slopes upward or inverts. Decomposing this carry into its components—financing, storage, convenience yield, and insurance—reveals which economic forces dominate the market at any moment and forecasts where prices are likely to be pulled.*

## The curve is made of components, not magic

When a commodity trades in [contango](/contango/), the forward price sits above the spot price. That gap must be explained. The textbook formula says forward price equals spot plus the total cost of carry, but "carry" bundles four distinct economic realities:

1. **Financing cost** — the interest you pay to borrow money and hold the commodity from today until delivery.
2. **Storage cost** — the physical cost of warehousing, insurance, shrinkage, quality degradation.
3. **Convenience yield** — the implicit benefit (usually negative, a cost) of holding the spot commodity rather than the future, because you can use it immediately.
4. **Insurance or hedging value** — the extra cost (or sometimes credit) for bearing the risk that supply shocks move the spot price.

A trader who understands decomposition does not memorise curve shapes; instead, he asks: *Which component is dominant right now?* When oil is in severe backwardation (forward price below spot), convenience yield is screaming. When a crop trades in steep contango shortly after harvest, storage and financing are the story. Decomposition turns the curve from a black box into a readable ledger.

## Financing is the floor

The minimum carry cost is interest. If you buy physical crude at $80 per barrel today and lock in sale six months forward, you have financed that $80 for six months. At a 5% annual rate, that costs roughly 2.5%. The forward price must at least cover that interest, or an arbitrageur would borrow at that rate, buy spot, and sell forward to lock in a riskless profit.

Financing cost grows with the [interest rate](/interest-rate/) and the time to maturity. A 12-month contract on wheat costs twice as much to finance as a 6-month contract, all else equal. In periods of high [central bank](/central-bank/) rates, financing dominates the curve slope. In periods of negative real rates, financing shrinks—sometimes even becomes a credit to holders who park cash in commodities.

## Storage: the unglamorous but relentless component

Storing a million barrels of oil for a year costs real money—tank rental, heating to prevent wax buildup, insurance against leakage. For some commodities the cost is minuscule (copper, gold, which barely degrade). For others it is brutal: crude oil, for example, can run 1–2% of spot value per month in tight storage markets. Grains rot or attract pests; perishables demand temperature control.

Storage cost is also not constant. When the world is awash in inventories, storage is cheap—warehouses are empty and landlords slash rates. When supplies are tight, storage becomes scarce and expensive. A sudden supply shock (a refinery fire, a harvest failure) can flip storage from a minor carry component to the dominant cost in days. Traders watch inventory levels obsessively because they predict storage cost trajectories.

## Convenience yield: the value of having it now

Convenience yield is the inverse concept. It is the benefit—economic or operational—of holding the physical commodity today rather than waiting for future delivery. A refinery wants crude now, not six months hence, because delay means lost production. A utility holding natural gas reserves values flexibility to meet winter demand spikes.

Convenience yield appears as a *negative* carry cost—it reduces the forward price below what financing and storage alone would predict. During a supply crisis, convenience yield spikes. In the 1990 Gulf War, oil [convenience yield](/contango/) exceeded storage and financing combined, pushing the curve into sharp backwardation: the forward price collapsed relative to spot because every barrel in hand was desperately valuable.

Convenience yield is unobservable directly. Traders infer it by subtracting known financing and storage costs from the observed curve slope. When that residual is large and negative, the market is rationing supply tightly. When it approaches zero, supply is ample and holders feel no pressure to deliver.

## Insurance and option value

The fourth component captures the extra cost—or credit—of bearing tail risk. A producer selling futures is short the commodity; he wants to hedge, so he will pay a small premium to shift downside risk to someone else. A consumer buying futures is long; he is willing to pay less than pure carry suggests to lock in future supply.

This component is hardest to quantify because it is purely a function of risk appetite and expectations. In calm markets, it is negligible. In periods of high [volatility](/volatility-smile/) or when geopolitical threats loom, it can shift curve shape noticeably. For example, tensions in the Middle East might make buyers of near-month oil willing to pay less (accepting higher prices now) because the futures contract insures them against an even worse supply shock later.

## Why decomposition matters in practice

A trader in oil [contango](/contango/) might ask: Is this curve steep because storage is full (storage cost rising) or because interest rates climbed? The answer changes the trading decision. If storage is the culprit, the curve will flatten when inventories decline. If interest rates are the issue, the curve will stay steep until rates fall.

Similarly, a curve that flips from contango to [backwardation](/backwardation/) overnight does not mean market fundamentals have reversed entirely. It usually means convenience yield has spiked—the market is signalling tight supply right now—even as financing and storage remain stable. Decomposition reveals the shift in a single component rather than forcing you to rationalize a complete curve inversion.

Producers and consumers use decomposition to forecast curve moves and set [hedge](/hedge-fund/) ratios. A grain elevator storing corn for sale in six months knows storage will cost 3% of spot; he expects financing at 2% and convenience yield near zero. So he budgets for 5% carry cost. If the forward curve only offers 4% above spot, storage is not economic—he should sell the physical now rather than finance and store for later delivery.

## The curve as a menu of costs

The [forward curve](/futures-contract/) is ultimately a menu of carry costs at different horizons. A steep curve (contango) says: "It costs a lot to defer delivery." A flat or inverted curve says: "You barely pay to wait, or you actually earn money by waiting (backwardation)." Decomposition teaches you which cost is speaking—and therefore which market stress is real. When you know whether tightness, storage congestion, or rate cycles are driving curve shape, you can make predictions about when that shape will persist or revert.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — forward price above spot; the curve slopes upward, embedding carry costs.
- [Backwardation](/backwardation/) — forward price below spot; convenience yield dominates, signalling tight supply.
- [Futures Contract](/futures-contract/) — standardized agreement to deliver at a future date; foundation for curve trading.
- [Cost of Carry](/cost-of-debt/) — the financing and storage costs of holding a commodity until delivery.
- [Convenience Yield](/forward-contract/) — the implicit benefit of holding spot versus futures; dominant in tight markets.
- [Crude Oil Curve Structure](/crude-oil-curve-structure/) — how OPEC discipline and inventory levels drive oil curve dynamics.
- [Natural Gas Seasonal Strip](/natural-gas-seasonal-strip/) — winter-summer pricing differential reflecting demand seasonality.
- [Curve Roll-Down](/curve-roll-down/) — P&L from a contract rolling down a sloped curve as time passes.

### Wider context

- [Bond](/bond/) — fixed-income securities with coupons; their curves also decompose into carry and option value.
- [Yield Curve](/yield-curve/) — the maturity structure of interest rates; a parallel to commodity curve structure.
- [Spread Trading](/credit-spread/) — profiting from price differences between instruments; decomposition identifies tradable spreads.
- [Price Discovery](/price-discovery/) — how markets arrive at prices; futures curves aggregate cost-of-carry signals.
- [Volatility Smile](/volatility-smile/) — pricing variations across strikes; another layer of embedded options and risk.

</div>
