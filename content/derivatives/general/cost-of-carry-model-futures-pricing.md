---
title: "Cost-of-Carry Model for Futures Pricing"
description: "The cost-of-carry model explains how storage costs, interest rates, dividends, and convenience yield determine futures prices. Learn the formula and application."
keywords:
  - cost of carry model futures pricing
  - futures fair value calculation
  - basis futures contract
  - cost of carry formula
  - convenience yield
  - futures pricing model
image: /svg/derivatives.svg
---

*The **cost-of-carry model** is the theoretical foundation for pricing [futures contracts](https://en.wikipedia.org/wiki/Futures_contract). It answers a simple question: if I buy the underlying asset today and hold it to maturity, what price should the futures contract trade at? The answer hinges on four elements: financing cost, storage cost, yield received, and the mysterious "convenience yield" that makes some assets worth holding.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cost-of-Carry Model — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Futures price encodes the full cost to carry physical inventory forward.</div>

|   |   |
|---|---|
| **Formula (simple)** | F = S × e^((r + u - y) × T) or F = S + carrying costs − income |
| **S** | Spot price (current underlying price) |
| **F** | Futures price |
| **r** | Risk-free interest rate (financing cost) |
| **u** | Storage and insurance cost |
| **y** | Yield from holding (dividend, coupon, lease rate) |
| **T** | Time to [expiration-date](https://en.wikipedia.org/wiki/Expiration_date) (in years) |
| **Convenience yield** | Hidden benefit from holding physical; drives [contango](https://en.wikipedia.org/wiki/Contango) or [backwardation](https://en.wikipedia.org/wiki/Backwardation) |

</aside>

## The Core Insight: No Arbitrage

The cost-of-carry model rests on a no-arbitrage principle. If I can borrow money at a known interest rate, purchase the spot commodity, and store it until futures maturity, the futures price must equal my total cash outlay plus a reasonable return. If not, an arbitrageur would buy the spot, sell the future (or vice versa), and lock in a risk-free profit.

For equities, this means: buy the stock today, finance it for three months at the risk-free rate, pay any dividends owed, and sell it forward at the futures price. The futures price must cover the financing cost, minus any dividends received.

For commodities, the calculation includes storage (warehouse fees, insurance, spoilage risk) and can include convenience yield—the intangible benefit of having physical supply on hand.

## The Basic Formula

The continuous-time cost-of-carry formula is:

**F = S × e^((r + u - y - c) × T)**

Or in simpler discrete form:

**F = S + Interest + Storage − Dividends**

Where:
- **S** = Spot price today
- **r** = Risk-free interest rate (cost of financing the purchase)
- **u** = Storage and insurance cost, expressed as a percentage of spot
- **y** = Yield (dividends for stocks, coupons for bonds, lease rates for commodities)
- **c** = Convenience yield (benefit of holding physical; often unknown)
- **T** = Time to expiration (in years)

## Applied Example: Stock Index Futures

Suppose the S&P 500 trades at 5,000. A three-month (0.25-year) [futures-contract](https://en.wikipedia.org/wiki/Futures_contract) should trade around:

F = 5,000 × e^((0.05 − 0.02) × 0.25)
F = 5,000 × e^(0.0075)
F ≈ 5,037.50

Here, the risk-free rate is 5% (financing cost), dividend yield is 2% (reduces carry cost), and time is 0.25 years. The futures price reflects a modest premium over spot—the net cost of carrying the position.

If the futures contract is trading at 5,050, a trader could:
1. Borrow $5 million at 5%, buy the index (via ETF or replicating portfolio)
2. Hold it three months, receiving 2% in dividends
3. Sell the futures at 5,050
4. Lock in the spread

This arbitrage pressure keeps futures prices close to theoretical fair value.

## Storage: The Commodity Twist

For commodities—oil, grain, metals, livestock—storage and insurance add a material cost component. Unlike a stock ETF, you cannot just hold crude oil in your brokerage account. You need a tank farm, insurance, spoilage risk, and logistics.

If you're carrying crude oil at $80 per barrel for six months, and storage/insurance runs 2% per annum, the cost-of-carry model predicts:

F = 80 × e^((0.05 + 0.02 − 0.00) × 0.5)
F ≈ 82.83

The futures should trade in contango—at a premium to spot—reflecting the cost of storing physical inventory.

But actual [futures-contract](https://en.wikipedia.org/wiki/Futures_contract) prices often deviate. If oil futures trade at $82, below the model's prediction, it suggests convenience yield is at work.

## Convenience Yield: The Elusive Component

**Convenience yield** is the benefit, expressed as a percentage, that someone receives from holding the physical commodity rather than futures contracts. For oil, it might reflect the value of having immediate supply when refinery demand spikes. For agricultural commodities, it might reflect the logistics value of holding inventory during seasonal shortages.

Convenience yield is not directly observable; it is inferred by rearranging the cost-of-carry model:

c = (r + u − y) − ln(F / S) / T

If oil futures are in backwardation (trading below fair value), convenience yield is high—the market is willing to pay a premium for immediate physical supply.

This is most visible in commodity markets during supply disruptions. During a geopolitical crisis or production shock, crude oil futures might trade in steep backwardation, signaling that refineries desperately need immediate barrels. Conversely, during periods of ample supply, convenience yield falls and the curve inverts into contango.

## Dividend-Paying Stocks and Bonds

For stocks, the cost-of-carry model must account for [dividend](https://en.wikipedia.org/wiki/Dividend) income. Holding the stock entitles you to dividends; holding the futures contract does not. The futures price must be lower than a simple financing calculation would suggest.

For a high-dividend stock (say, a utility paying 4% annually), the futures curve will be relatively flat or slightly inverted because dividends offset financing costs.

For bonds, the cost-of-carry includes [coupon-payment](https://en.wikipedia.org/wiki/Coupon_payment) reinvestment. The model predicts bond futures prices by accounting for the present value of all coupons and the principal repayment.

## Contango vs. Backwardation: Reading the Curve

The cost-of-carry model explains why commodity futures curves take their shape:

**Contango** (upward slope): Storage costs exceed convenience yield. The farther out you go, the higher the futures price. Oil and grains typically exhibit contango during periods of ample supply. A trader or producer who buys and "rolls" futures forward—selling the near contract and buying the far contract—pays the contango spread repeatedly.

**Backwardation** (downward slope): Convenience yield exceeds storage costs. Near-term contracts trade above far contracts. This signals scarcity or urgent demand. During oil supply crunches or poor harvests, backwardation can be steep. A trader rolling forward loses money; a holder of physical supply is rewarded.

The cost-of-carry model makes both of these patterns predictable if you know (or can estimate) the underlying components.

## Basis and Mispricing

The difference between the futures price and the spot price is called [basis](https://en.wikipedia.org/wiki/Basis). The cost-of-carry model tells you what that basis *should* be. If actual basis is much wider, you have a mispricing opportunity.

A producer of oil, for example, might short futures (hedge expected production) when the curve is in steep contango—locking in the high future price. Conversely, during backwardation, a producer might delay hedging, betting that spot prices will rise or that backwardation will flatten.

## Limitations and Real-World Complications

The cost-of-carry model assumes:
- Perfect markets (no bid-ask spread, no transaction costs)
- Known, constant storage costs
- No default or [counterparty-risk](https://en.wikipedia.org/wiki/Counterparty_risk)
- Ability to borrow and short freely at the risk-free rate

In reality:
- Financing costs vary (small speculators pay more than large dealers)
- Storage estimates are uncertain, especially for metals or agricultural goods
- Convenience yield is hard to quantify and changes rapidly
- Market frictions can push prices away from theoretical fair value for days or weeks

Nonetheless, the model provides a strong anchor. Large dealers and exchanges use cost-of-carry formulas to mark prices and detect arbitrage opportunities. It is the industry standard.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — Instrument mechanics and clearing
- [Basis](/basis/) — Price difference between futures and spot
- [Contango](/contango/) — Upward-sloping futures curve and implications
- [Backwardation](/backwardation/) — Downward-sloping curve signaling scarcity
- [Forward contract](/forward-contract/) — Over-the-counter version of futures
- [Derivatives hedging](/derivatives-hedging/) — Why firms use futures and forwards
- [Interest rate swap](/interest-rate-swap/) — Cost-of-carry applies to interest rate derivatives

### Wider context

- Commodity markets — Agricultural, energy, and metal futures
- [Price discovery](/price-discovery/) — Role of futures in information aggregation
- Arbitrage — Enforcing no-arbitrage through dealer activity
- [Discounted cash flow valuation](/discounted-cash-flow-valuation/) — Related present-value logic
- [Volatility smile](/volatility-smile/) — How volatility enters option pricing

</div>
