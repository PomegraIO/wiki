---
title: "Futures Roll Yield"
description: "Futures roll yield is the gain or loss from rolling an expiring contract into the next maturity, separate from spot price movements."
keywords:
  - futures roll yield
  - rolling futures
  - contract rollover
  - curve slope
  - contango backwardation
  - futures curve
---

*Futures roll yield is the profit or loss you realize simply by rolling an expiring **futures contract** into the next maturity month, independent of any change in the underlying asset's spot price. It arises purely from the shape of the futures curve—how far forward contracts trade relative to near-term ones.*

<div class="wiki-infobox">

<div class="wiki-infobox-title">Futures Roll Yield — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Profit or loss from contract timing, not spot price movement.</div>

|   |   |
|---|---|
| **What it is** | Return from switching from an expiring contract to a later-dated one |
| **Arises from** | The difference in price between near and far contracts on the curve |
| **In contango** | Negative roll yield (you sell low, buy high) |
| **In backwardation** | Positive roll yield (you sell high, buy low) |
| **Key for** | Long-only commodity indices, trend-following funds, systematic traders |
| **Not affected by** | Spot price movement—pure curve effect |

</aside>

## The Basic Roll Mechanic

Imagine you own a near-month crude oil futures contract at \$75/barrel with one week left to expiration. You want to stay long oil but can't take physical delivery. You sell that contract and simultaneously buy the next contract out, which trades at \$76. You've just locked in a \$1 loss per barrel solely from the curve structure—that's negative roll yield.

If instead the next contract traded at \$74 while your expiring contract was at \$75, you'd pocket \$1 per barrel just by rolling. That's positive roll yield.

The remarkable part is that this gain or loss has nothing to do with whether oil prices are rising or falling in absolute terms. You could be rolling into a market where prices collapse tomorrow, or into one headed for all-time highs. The roll yield captures only the mechanical cost of managing the contract switch.

## Roll Yield in Contango vs. Backwardation

Most commodity and financial [futures curves](/futures-contract/) spend most of their time in *contango*—a state where contracts further out trade higher than near-term ones. This happens naturally when storage, financing, and other carry costs are positive: holding the asset forward costs money, so far contracts embed that premium.

In contango, rolling is a drag. Each month, you sell a relatively cheap (near) contract and buy a relatively expensive (far) contract. Over time, this bleeds returns. A fund holding long oil futures through a steep contango can lose 10–20% annually just from rolling, even if oil prices go nowhere.

*Backwardation* is the opposite: near contracts trade richer than far ones. This signals scarcity or high convenience value. Rolling is a gift: you sell at the higher near price and buy at a lower far price. Trend-following funds and commodity traders relish backwardated markets because roll yield stacks on top of any spot-price gains.

## How Roll Yield Compounds

The cumulative effect of roll yield matters far more than any single month's roll. A trader managing a long exposure to crude oil might roll twelve times a year. If the curve is consistently 2% in contango per quarter, four rolls per year translate to roughly 8% annual drag. Over five years, that's material—it's wealth transfer from the futures holder to whoever is short the commodity or managing the physical supply.

Conversely, in a sustained backwardation, the same trader captures 8% per year from rolling alone, independent of spot price movement. During the 2008 oil crisis, backwardation was so steep that some commodity index funds made more from rolling than from spot appreciation—a rare and profitable state.

## The Futures Curve and the Roll Schedule

The shape of the [futures curve](/futures-contract/) tells you the entire roll schedule in advance. If Dec 2024 crude trades at \$75 and Jan 2025 trades at \$76, and Feb at \$77, you can calculate your expected roll yield for the next year. Each transition from one month to the next will cost you roughly \$1/barrel.

Professional commodity traders track these curves obsessively. A fund holding long positions in a steeply contangoed market may rotate into assets with shallower contango, or pivot to backwardated curves where roll yield is positive. Some funds are so sensitive to roll dynamics that they'll shift between different commodity sectors based purely on curve slope.

Weather, geopolitical events, and supply surprises reshape the curve constantly. A hurricane in the Gulf of Mexico instantly flattens the oil curve, turning contango into backwardation or deepening existing backwardation. Traders who anticipate these shifts can position to benefit from roll yield before it materializes.

## Roll Yield vs. Spot Price Moves

A crucial distinction: roll yield is *orthogonal* to spot price moves. You can experience massive positive roll yield while spot prices fall, and vice versa. A fund long crude oil futures in a strongly backwardated market might gain 5% from rolling over three months while crude spot prices drop 3%. The net result is a 2% gain, but only 0% came from the fundamentals of supply and demand—it all came from curve positioning.

This is why some hedge funds and systematic traders treat roll yield as a separate alpha stream. They'll dedicate a portfolio sleeve to "harvesting" roll yield by taking long positions in backwardated markets and short positions in contangoed markets, while staying flat on spot direction. It's a pure curve play.

## Who Benefits and Who Pays

Long commodity index funds pay roll yield drag in contango. Those funds hold real long exposure to commodity futures, so they're the natural payers. Whoever is short those contracts—often producers hedging supply, or dealers laying off their long exposure—pockets the drag.

In backwardation, the relationship flips. Index fund holders gain from rolling; producers or short speculators lose. This is why commodity producers monitor the curve shape vigilantly. In backwardation, they want to lock in sales at higher near prices and avoid selling forward into the weaker far months if they can.

Trend-following funds and systematic commodity traders actively trade roll yield. If they detect a shift from contango to backwardation, they may increase long positioning to capture the positive rolls. If contango is steepening, they may trim or hedge.

## The Relationship to Convenience Yield

Roll yield and [convenience yield](/convenience-yield-explained/) are deeply connected but distinct. Convenience yield is the implicit benefit of holding the physical commodity—the scarcity value embedded in the curve shape. When convenience yield is high, the curve is steep in backwardation, and roll yield is positive.

When convenience yield is low (supplies are ample, scarcity is minimal), [contango](/contango/) dominates, and roll yield is negative. But they're not identical: convenience yield is an economic reality that forward pricing tries to capture, while roll yield is the actual mechanical cost or gain you experience when rolling.

Understanding both together allows traders to see the true carry dynamics. High roll yield in backwardation signals that convenience value is priced and available. Steep negative roll yield in contango warns that you're buying forward exposure at a premium and paying that cost every roll.

## Strategic Use in Long-Only Positioning

Passive commodity index funds are structurally obligated to roll: they hold continuous long exposure and must sell expiring contracts and buy new ones. They have no choice but to absorb roll yield, whatever it is. This is why commodity index returns can lag spot returns in steep contango—the index methodology forces repeated rounds of selling low and buying high.

Some funds try to optimize rolling by shifting roll dates or choosing different contract months, but the curve shape ultimately determines the outcome. In deep contango, there's no hiding: rolls will cost you.

Active managers can time rolls or even go flat temporarily if they see the curve becoming unattractively contangoed. This flexibility is one reason actively managed commodity funds sometimes outperform passive indices, especially in transition periods when curves are flattening or shifting from contango to backwardation.

## See also

<div class="wiki-seealso">

### Closely related

- [Convenience Yield Explained](/convenience-yield-explained/) — scarcity premium that drives curve shape
- [Contango](/contango/) — futures trading above spot, creates negative roll drag
- [Backwardation](/backwardation/) — futures below spot, generates positive roll returns
- [Futures Contract](/futures-contract/) — standardized derivatives where rolls occur at maturity
- [Cost of Carry](/cost-of-carry/) — financing and storage costs that feed into contango

### Wider context

- [Trend-Following](/trend-following/) — systematic strategies that exploit roll dynamics
- [Derivatives Hedging](/derivatives-hedging/) — why producers and consumers face roll yield impact
- [Index Fund](/index-fund/) — passive commodity indices absorb roll yield drag
- Commodity Markets — spot and futures landscape where curves take shape
- [Volatility Smile](/volatility-smile/) — curve patterns that affect pricing across maturities

</div>
