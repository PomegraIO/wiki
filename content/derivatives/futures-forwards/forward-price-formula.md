---
title: "Forward Price Formula"
description: "The no-arbitrage equation that determines a forward contract's price from the spot price, risk-free rate, carrying costs, and expected income."
keywords:
  - forward price
  - spot price
  - cost of carry
  - no-arbitrage pricing
  - derivatives
  - forward contract
image: "/svg/derivatives.svg"
---

*The **forward price formula** is the mathematical relationship between a [forward contract's](/forward-contract/) price and the current [spot price](/spot-exchange-rate/) of an asset. It encodes the principle of no-arbitrage: the forward price must be set such that no trader can lock in a risk-free profit by simultaneously trading the spot asset and the forward. The formula accounts for the cost of holding the asset until delivery, the interest foregone, and any income (dividends, coupons, convenience yield) the asset generates in the interim.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forward Price Formula — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives markets." />

<div class="wiki-infobox-caption">The no-arbitrage equation binding forward and spot prices across time.</div>

|   |   |
|---|---|
| **What it is** | Formula determining [forward contract](/forward-contract/) price from spot price and cost of carry |
| **Core principle** | No-arbitrage: forward price must prevent risk-free profit |
| **Variables** | Spot price, interest rate, time to delivery, carrying costs, yield |
| **Also called** | Cost-of-carry model, forward-pricing formula |
| **Used in** | Equity, bond, commodity, and currency forwards |

</aside>

## The basic formula

The simplest form of the forward price formula is:

**F = S × e^(r × T)**

Where:
- **F** = forward price
- **S** = current spot price
- **r** = risk-free interest rate (annualized)
- **T** = time to maturity (in years)
- **e** = Euler's constant (approximately 2.718)

This equation says: the forward price equals the spot price grown at the risk-free rate for the contract's duration. If you lock in a price today for delivery in one year, you are essentially lending money at the risk-free rate. The forward price must be high enough to compensate the buyer for the opportunity cost of capital tied up until settlement.

## Why the formula prevents arbitrage

Suppose the formula is violated. The spot price of oil is $100, the annual risk-free rate is 5%, and a one-year forward trades at $110—below the $105.13 predicted by the formula.

A trader exploits this gap immediately:
1. Borrow $100 at 5% interest.
2. Buy the spot oil for $100.
3. Enter a short forward contract to sell in one year at $110.
4. In one year, deliver the oil and receive $110.
5. Repay the $105.13 loan (principal plus interest).
6. Profit: $110 − $105.13 = $4.87, risk-free.

Demand for this trade would push the forward price up until it reaches $105.13, eliminating the profit opportunity. Similarly, if the forward is overpriced, traders reverse the trade: short the spot (borrow and sell), buy the forward, lock in a guaranteed profit, and arbitrage narrows the gap.

The market continuously enforces the formula. Prices that depart from it are eliminated by arbitrageurs almost instantly, so forwards trade at levels consistent with the formula.

## Adding carrying costs and income

The real world is messier. Assets incur storage costs, insurance, or holding expenses. Stocks and bonds throw off dividends or coupons. Commodities have convenience yields. The general formula becomes:

**F = S × e^((r + u − y) × T)**

Where:
- **u** = storage and carrying costs (as a percentage of spot price)
- **y** = yield or income rate (dividends, coupons, convenience yield)

If oil costs 2% per annum to store and transport, but pays no dividend, then **u = 0.02** and **y = 0**. The forward price rises: you are paying not just for the cost of capital but also for the physical burden of holding and storing the asset.

If a stock yields 3% in dividends and carries no storage cost, then **u = 0** and **y = 0.03**. The forward price is lower because the holder receives income along the way, partially offsetting the interest cost.

## Why this matters for traders

The forward price formula tells a trader whether a forward contract is fairly priced relative to the spot market. If a trader observes a forward trading above the formula's prediction, she knows the forward is rich and can execute an arbitrage. If it trades below, the forward is cheap.

This is most visible in [currency markets](/currency-volatility/). A trader comparing the [forward exchange rate](/spot-exchange-rate/) for euros against dollars can check it against the formula using the U.S. and eurozone interest rates. If the forward deviates, she borrows in one currency, invests in another, enters a forward to lock in conversion on the way back, and captures the gap.

Commodity traders use the formula to detect mispricing. Suppose a one-year gold forward is quoting $2,100 per ounce, but the formula—accounting for gold storage, insurance, and the risk-free rate—predicts $2,050. The trader buys the physical gold, funds it at the risk-free rate, insures it, shorts the forward, and keeps the $50 difference at maturity.

## Complications: convenience yield and discrete dividends

The formula simplifies reality in ways that matter.

**Convenience yield** is the unobservable benefit of holding the physical asset right now. Oil refiners value crude oil in inventory; if they need it immediately, they gain from spot ownership versus waiting for a forward delivery. This benefit does not appear on a balance sheet but is real. Estimating it requires market inference: if the formula consistently underpredicts forward prices in a commodity, the residual is attributed to convenience yield. This is why commodity forwards sometimes exhibit a "backwardation" term structure (nearby forwards trading above distant forwards), opposite to the financial asset norm.

**Discrete dividends** complicate equity forwards. A stock's dividend is paid on a specific date, not as a continuous stream. The precise formula then includes the present value of dividends falling within the forward's term, subtracted from the spot price. A stock paying a $2 dividend in six months would have a lower forward price than the continuous-yield formula suggests, because the buyer of the forward misses the dividend.

## The formula in practice: index futures

The [SP 500 Index](/sp-500-index/) provides a clean test case. Index futures trade on the CME, and the index itself is observable daily. The forward price formula predicts that a futures contract maturing three months from now should price the index at:

**F = S × e^((r − d) × T)**

Where **d** is the dividend yield of the 500 companies. U.S. large-cap dividends run roughly 1.5–2% annually, and risk-free rates fluctuate. The formula works remarkably well. Traders routinely exploit deviations: if the futures are cheap, they buy the 500 stocks (or a replicating ETF), short the futures, and harvest the carry. These trades keep index futures prices tethered to the formula.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward Contract](/forward-contract/) — agreement to exchange an asset at a specified future date and price
- [Spot Exchange Rate](/spot-exchange-rate/) — current market price of a currency or asset for immediate delivery
- [Futures Contract](/futures-contract/) — standardized version of a forward traded on exchanges; prices follow the same formula
- [Cost of Carry](/cost-of-carry/) — the net cost or benefit of holding an asset to delivery; central input to the formula
- [Contango](/contango/) — situation where forward prices exceed spot prices, consistent with positive carrying costs

### Wider context

- Arbitrage — exploiting price gaps between markets; the forward formula relies on arbitrage to enforce pricing
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — more general framework for pricing future cash flows
- [Interest Rate](/interest-rate/) — key input to the formula; movements shift all forward prices
- No-Arbitrage Principle — foundational to derivatives pricing; the forward formula is its simplest application

</div>
