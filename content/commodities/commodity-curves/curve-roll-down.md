---
title: "Curve Roll-Down (Commodities)"
description: "The profit or loss a futures holder realizes as a contract rolls down a steep backwardated or upward-sloping forward curve over time, independent of spot price moves."
keywords:
  - curve roll-down
  - futures P&L
  - contango roll loss
  - backwardation roll gain
  - carry trade
  - forward curve
image: "/svg/commodities.svg"
---

*A trader holding a commodity [futures](/futures-contract/) contract realizes two sources of profit or loss: the change in the underlying spot price, and the change in the contract's value relative to the curve. The second effect—**curve roll-down**—occurs because as time passes, a distant contract rolls down the forward curve toward spot and eventually to maturity. In [backwardation](/backwardation/), this roll-down is profitable. In [contango](/contango/), it is a drag on returns.*

## The static curve and rolling time

Imagine the natural gas curve on 1 January looking like this: January futures $3.50/MMBtu, February $3.40, March $3.30, April $3.20. This is backwardation; deferred contracts trade below near-month because supply is tight and the market is rationing availability.

Now suppose a trader buys 100 January contracts at $3.50. He holds them through January, and on 1 February, January has expired and is no longer quoted. But February is now the front contract. If the curve has not moved (flat roll), February is still $3.40, and March is still $3.30, April $3.20.

The trader is now holding February contracts, which traded at $3.40 but he bought (via rollover) at $3.50. Ouch. He has lost $0.10 per contract, or $10,000 on 100 contracts, *purely from the curve rolling down*, even though the underlying market prices have not changed at all.

This is curve roll-down in contango: the contract rolled from a deferred, cheaper position down the curve closer to spot (and higher prices), but in this case "down" meant toward dearer prices, so the trader lost money on the roll. Most textbooks call this "roll drag" or "roll loss" in contango.

## The mechanics: rolling toward spot in a sloped curve

The mechanism is simple. Futures contracts have a finite life—they expire on a set date. A trader who wants to maintain a position over multiple contract months must sell the expiring contract and buy the next contract along the forward curve.

In contango, the next contract is cheaper than the spot-proximate one. A trader with a March contract in February will sell March (now the front) and buy April (now the deferred). April is cheaper than March, so he gives up a higher price for a lower price. The curve has "rolled down" in the sense of time progression, but the trader has rolled from a higher price to a lower price—a loss.

In backwardation, the next contract is more expensive than the spot-proximate one. Selling the March (front) and buying April (deferred) means selling at a lower price and buying at a higher price. On the surface that looks bad, but it is actually a gain in total P&L, because the deferred contract (April) is worth more than the near-contract (March). The trader has rolled down to a more valuable contract—a gain.

## Roll-down gain in backwardation

When [crude oil](/crude-oil/) is in sharp backwardation—say, February at $85 and March at $83—a trader who buys February and rolls to March will suffer an immediate loss: he is buying March at $83 when he could have locked in $85 in February. But that is not the full story.

He bought February at $85 because he expected the market was tight and he wanted to be long. As he rolls into March at $83, the June contract (further out) is $81. The entire curve is backwardated. If he continues rolling every month, he is capturing the roll-down gain month after month.

Over a full year of rolling, he might capture $4 to $6 per barrel in total roll-down gains—the slope of the backwardated curve multiplied by the number of roll periods. This is the reward for holding long in a tight market. It is compensation for the carry cost and the risk that supply will suddenly loosen and the backwardation will flatten.

## Roll-down loss in contango

The inverse applies in contango. When the natural gas curve is steep contango—June $2.50, December $3.50—a trader who buys June and rolls forward every month will capture the upward slope, but at a cost. Each month he sells the near contract and buys the deferred, he locks in a smaller price. Over six months, he might give up $0.50–$1.00 per MMBtu, a substantial drag on returns.

This is the cost of carry embedded in the contango. The curve is steep because [storage](/contango/) and [financing](/contango/) are expensive; producers and refiners who need to push physical commodity forward in time must pay that cost, and futures traders who are "long carry" (buying spot and selling forward, or buying the near-term contract and rolling into deferred) absorb the same cost.

## Roll-down as a hidden source of return or loss

Many traders think of futures returns solely in terms of spot price appreciation or depreciation. If they buy oil futures and oil prices rise, they make money; if oil prices fall, they lose. But that frame misses the curve roll-down return entirely.

A trader who buys oil futures in a backwardated market and the spot price stays flat is still profitable because of the roll-down gain. Similarly, a trader who is short oil in a contango market and the spot price stays flat still loses money because of the roll-down cost.

Professional commodity traders always account for roll-down when sizing positions and forecasting returns. A [hedge fund](/hedge-fund/) manager might say: "I am bullish on oil, but the market is in steep contango at 3% for six months. If I buy oil futures and roll forward every month, I will capture that contango as a drag unless prices appreciate more than 3%." This forces the manager to think rigorously about conviction: Is the upside really more than the roll cost?

Conversely: "I am bearish on natural gas, but the market is in backwardation at 2% for the next quarter. If I short gas futures and roll forward, I will give up that backwardation as a cost. I need the price to fall more than 2% over the next quarter to profit." The backwardation is working against the short; it is compensation for longs who are willing to hold tight supply.

## Roll-down as a predictor of curve flattening or steepening

The roll-down calculation also points to when a curve is likely to flatten or steepen. A very steep backwardated curve (say, 10% roll-down annually) is unsustainable long-term because it implies that holding the commodity and rolling costs enormous capital. Eventually, either:
1. Supply will come online to flatten the backwardation, or
2. Consumers will reduce demand or substitute to avoid the high forward-roll costs.

A very steep contango (say, 8% annual roll-down cost) implies expensive storage and financing; this too will eventually unwind as supply exceeds demand enough that storage becomes cheaper or producers cut output.

The roll-down path is a clue to mean-reversion. If a curve is in extreme backwardation, roll-down gains are large, but those gains are eating into the return of traders holding long; eventually the market will equilibrate and the backwardation will flatten. The roll-down becomes self-limiting.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — forward prices above spot; roll-down is a cost for holders in contango markets.
- [Backwardation](/backwardation/) — forward prices below spot; roll-down is a gain for holders in backwardated markets.
- [Futures Contract](/futures-contract/) — the instruments that roll forward; maturity and roll dates are structural.
- [Futures Carry Decomposition](/futures-carry-decomposition/) — breaking down storage, financing, and convenience yield that drive roll costs and gains.
- [Crude Oil Curve Structure](/crude-oil-curve-structure/) — how OPEC and inventory dynamics create backwardation and contango for oil.
- [Natural Gas Seasonal Strip](/natural-gas-seasonal-strip/) — seasonal curve slopes that roll down predictably over the year.
- [Spread Trading](/credit-spread/) — capturing curve slope differences; roll-down is embedded in spread returns.

### Wider context

- Commodity Curves — forward price structures across all storable commodities.
- [Carry Trade](/leverage-ratio-forex/) — financing and storing an asset to capture a forward premium or avoid a discount.
- [Price Discovery](/price-discovery/) — how futures curves aggregate cost-of-carry and convenience yield signals.
- [Option Premium](/option-premium/) — another source of decay in options; analogous to roll-down in futures.
- [Yield Curve](/yield-curve/) — interest rate curves; roll-down concepts apply to bond futures and duration.

</div>
