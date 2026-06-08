---
title: "Decomposing the Risk Premium in a Commodity Futures Curve"
description: "A commodity futures curve embeds multiple risk premiums: hedging pressure, convenience yield, and expected spot change. Understanding how to decompose them reveals market expectations."
keywords:
  - commodity futures curve risk premium decomposition
  - risk premium in futures prices
  - hedging premium and convenience yield
  - contango and backwardation
  - commodity price expectations
image: /svg/commodities.svg
---

*The **commodity futures curve risk premium decomposition** breaks down the excess return embedded in commodity futures prices into three components: the insurance premium paid to hedgers, the convenience yield (the benefit of holding the physical commodity), and the expected change in the spot price. This decomposition reveals whether the futures curve reflects genuine shortage expectations, storage costs, or hedging demand.*

## Why futures prices differ from spot

When a futures contract trades at a premium to the current [spot rate](/spot-rate/), the gap is not random. It reflects the market's collective belief about three distinct drivers. A farmer selling forward might demand a premium for deferring sale. A refiner holding crude oil might benefit from immediate availability in ways that depressed storage markets don't capture. Speculators might pile into the curve expecting prices to rise. The decomposition framework separates these signals.

The futures price can be written as: Futures Price = Spot Price + Cost of Carry − Convenience Yield + Risk Premium. Rearranging to isolate the risk premium requires stripping away the costs and benefits, leaving what the market actually expects about future supply and demand.

## The three components: definitions

**The hedging premium** (or risk premium proper) is compensation that speculators and investors demand to absorb the price risk that hedgers offload. A wheat farmer afraid of lower prices in six months will short futures contracts. To entice a speculator to take the other side—to go long and assume downside risk—the farmer may implicitly offer a discount, or the futures price may sit below where a risk-neutral market would place it. Conversely, a food manufacturer afraid of *higher* prices will buy futures; to attract a short seller to absorb upside risk, the futures might trade at a premium. This premium or discount is what hedgers collectively pay or receive for transferring risk.

**The convenience yield** is the non-monetary benefit of holding the physical commodity rather than owning a futures contract. Holding crude oil allows a refiner to respond immediately to supply disruptions or sudden demand spikes; a futures contract does not. Holding wheat allows a miller to manage production and avoid production delays; pure financial exposure does not. This benefit is highest when supplies are tight and inventory low—in shortage conditions—and falls to near-zero when storage is abundant. Mathematically, convenience yield acts like a "dividend" on the physical good, reducing the futures price relative to what pure storage costs would predict.

**The expected change in spot price** is the expected direction and magnitude of the commodity price over the contract period. If traders expect crude oil to be worth $5 more per barrel in three months, the futures price will embed that expectation upward. This component is forward-looking and inherently uncertain.

## The relationship to contango and backwardation

When the futures curve slopes upward ([contango](/contango/)), the futures price is higher than spot. The decomposition reveals why. In a typical contango, storage costs dominate: a physically-backed index fund buying spot oil and rolling futures contracts into forward months will gradually lose money to storage and financing. The futures premium exactly compensates for these costs, leaving no excess return—a condition called *full carry*. In this scenario, hedging premiums are near-zero, convenience yield is low, and expected spot change is neutral.

In [backwardation](/backwardation/), futures trade below spot, or near-term futures trade above distant contracts. Backwardation reveals tight supplies and high convenience yield. When inventories are depleted and the market is desperate for immediate physical delivery, the convenience of holding spot outweighs all costs, and futures must trade at a discount to compensate. Hedging premiums can also be negative (speculators earn a risk premium for going short and absorbing upside risk), further deepening backwardation. Backwardation is a powerful signal that supplies are constrained.

## How hedging demand shapes the curve

The hedging premium is where the microstructure of commodity markets shows. Oil producers hedging selling risk typically short futures. Refiners hedging buying risk typically go long. Airlines hedging fuel costs go long. When one side of the hedger community is much larger, the curve adjusts to compensate.

Consider a period when airline industry fuel demand is surging and many airlines are locking in fuel costs. Their collective long positions create demand pressure that pushes futures prices higher relative to risk-neutral expectations. Speculators on the short side demand a premium (a higher futures price) in exchange for absorbing the risk that oil prices fall and the airlines' hedge pays off handsomely. This premium shows up in the curve's slope and can persist for months or years, depending on the hedging imbalance.

Empirical research has shown that commodity futures curves with steep positive hedging premiums tend to underperform risk-neutral expectations—backwardation and hedging premiums correlate, and rolling hedges often encounter losses when hedging demand is highest.

## Convenience yield as a shortage signal

Convenience yield is most crucial for understanding real supply conditions. When it is zero or negative, the market is well-supplied; storage is abundant and cheap; there is no scarcity benefit to holding physical inventory. Traders expect to walk into any warehouse and find what they need at posted prices.

When convenience yield spikes, it signals the opposite: supplies are stretched. Refineries are running hot; strategic reserves are drawn; transportable inventory (pipeline stocks, tank cars) is scarce. A high convenience yield means traders will pay for the *option* to deliver or draw down physical stock right now rather than wait for a future delivery.

Measuring convenience yield empirically requires knowing storage costs and financing rates and then backing out the "missing" value from the futures-spot relationship. When this residual is large and positive, convenience yield is substantial—and market participants are rationing the scarce good through scarcity premiums, not just higher prices.

## Spot price expectations embedded in long-term curves

The expected spot change component is smallest in the near-term and largest in long-term futures. When a market goes through a supply shock (e.g., a major hurricane shutting off Gulf oil production), spot prices spike, but the longer-dated futures may not move as much—because the market expects conditions to normalize. The difference between current spot and distant futures prices reflects the market's best guess about mean reversion.

Long-dated curves (e.g., five-year crude oil futures) are heavily influenced by this term-structure expectation. If OPEC is expected to pump less for five years, the five-year futures may remain elevated. If speculators expect a glut, the curve may be shaped by a gradually declining price expectation over the next decade.

This component is the hardest to measure directly because expectations are unobservable. But when a major fundamental shift occurs (peak oil fears, shale revolution, transition to renewables), long-term futures curves reprice sharply, revealing that market expectations about long-run spot prices have shifted.

## Risk-neutral versus physical measures

Academic decomposition methods separate the risk premium into a "risk-neutral" component (the pure cost-of-carry plus convenience yield) and an "unexpected" component (the actual drift in prices above or below what risk-neutral models predict). Some practitioners use implied volatility to estimate how much of the futures premium reflects tail-risk hedging versus fundamental supply expectations.

For practitioners, the key insight is that futures curves embed three overlapping signals, and disentangling them requires context: supply reports, storage data, hedging flows, and seasonal patterns. A steep contango might indicate abundant supply (bullish fundamentals, high storage) or high short-term hedging demand; the decomposition helps interpret which story dominates.

## See also

<div class="wiki-seealso">

### Closely related

- [Contango](/contango/) — When futures trade at a premium to spot, driven by cost-of-carry and hedging dynamics
- [Backwardation](/backwardation/) — When futures trade at a discount, signaling tight supplies and high convenience yield
- [Futures Contract](/futures-contract/) — The derivative instrument through which commodity risk premiums are transacted
- [Spot Rate](/spot-rate/) — The current market price to which all decomposition analysis is anchored
- [Carry Trade](/carry-trade/) — Strategy that exploits commodity curve shape and cost-of-carry mismatch
- [Volatility Smile](/volatility-smile/) — How implied volatility across strikes hints at market fear and hedging demand

### Wider context

- Commodities — The asset class where risk-premium decomposition is most visible and practical
- [Price Discovery](/price-discovery/) — How futures and spot markets collectively reveal expectations and constraints
- [Market Risk](/market-risk/) — The fundamental drivers of hedging demand and risk premiums
- Commodity Cycles — Secular supply-demand shifts that reshape risk premiums over years

</div>
