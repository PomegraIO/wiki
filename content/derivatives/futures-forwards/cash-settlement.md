---
title: "Cash Settlement"
description: "Resolving a derivatives contract by paying the difference in value rather than delivering the underlying asset—used for index futures, interest rate derivatives, and intangible underlyings."
---

*An [S&P 500 futures](/wiki/sp-500-index/) contract cannot physically deliver the S&P 500. Instead, all positions are settled in cash—longs and shorts receive or pay dollars based on the difference between their contract price and the settlement price.*

## How cash settlement works

When a cash-settled [futures](/wiki/futures-contract/) or [forward contract](/wiki/forward-contract/) expires, the exchange publishes a **settlement price**—typically the spot price or index level at a precise moment (the opening, the close, or a special settlement auction).

Example: A trader goes long the December S&P 500 E-mini futures at 4,500. At expiration (the open of the third Friday in December), the index closes at 4,600. The settlement price is 4,600.

- The contract multiplier is $50 per point.
- The trader's profit is (4,600 - 4,500) × $50 = $5,000.
- The clearing house debits the short trader's account $5,000 and credits the long trader's account.
- The position is closed; no physical delivery occurs.

This is simpler than [physical delivery](/wiki/delivery-mechanisms/) (no warehouses, no logistics, no disputes over grade) and allows contracts on intangible underlyings (indices, interest rates, volatility).

## Cash settlement for indices and rates

**Index futures** are inherently cash-settled because an index is not an asset you can hold. The S&P 500 is a list of 500 stocks; you cannot buy "the S&P 500." But you can buy a [futures](/wiki/futures-contract/) contract that tracks it, and at expiration, cash settles to the index level.

**Interest rate [futures](/wiki/futures-contract/)** (10-year Treasury futures, Euribor futures) also cash-settle:
- A trader long 10-year Treasury futures locked in a rate reflecting the current yield curve.
- At expiration, the contract settles to the yield of the actual 10-year Treasury at that moment.
- No bonds are delivered; only cash changes hands.

**FX [futures](/wiki/futures-contract/) on cross-rates** (euro/yen, pound/AUD) often cash-settle, using the spot rate at expiration as settlement.

## Advantages of cash settlement

**1. Lower friction.** No warehouse disputes, no quality inspection, no transportation logistics. Settlement is instant; money clears within one business day.

**2. Availability for intangible underlyings.** Indices, rates, and volatility indices cannot be delivered. Cash settlement is the only mechanism.

**3. Democratization of derivatives.** A retail trader can hold S&P 500 [futures](/wiki/futures-contract/) without worrying about taking delivery of 500 different stocks. The cash mechanism makes these contracts accessible.

**4. Reduced [basis](/wiki/basis/) risk.** For a [physically deliverable contract](/wiki/delivery-mechanisms/), the long may take delivery of off-specification goods or goods at inconvenient locations, creating [basis](/wiki/basis/) risk. Cash settlement eliminates this; all longs receive or pay the same settlement price.

## Disadvantages of cash settlement

**1. Loss of price discipline.** A [physically deliverable contract](/wiki/delivery-mechanisms/) is constrained by the cost of physical arbitrage. If the December contract is too cheap, an arbitrageur can buy spot, store it, and deliver it in December, forcing price convergence. A cash-settled contract has no such constraint; it can diverge from "fair value" (however defined) without penalty.

**2. Manipulation risk.** If settlement is based on a single reference (e.g., the close price on a specific day), traders have incentive to manipulate that reference. During the final minutes of trading, a large trader might place orders to move the price, benefiting their position. Physical delivery makes this harder: you cannot easily manipulate the price of physical tons of copper actually moving through a warehouse.

**3. Disconnect from the real economy.** A cash-settled contract does not serve actual commodity users. A refiner cannot hedge with crude oil [futures](/wiki/futures-contract/) that cash-settle, because they need actual oil at the end. They need [physically deliverable contracts](/wiki/delivery-mechanisms/) or OTC [forwards](/wiki/forward-contract/).

## Settlement mechanics: special auctions and reference rates

Exchanges often use special mechanisms to determine settlement prices, reducing manipulation risk:

**Opening price auction:** The settlement price is determined by an opening auction on the final day, where orders are crossed at the opening. For Treasury [futures](/wiki/futures-contract/), this method is less susceptible to end-of-day manipulation than a simple closing price.

**Volume-weighted average price (VWAP):** Some contracts settle using a VWAP calculated over a window (e.g., the final 30 minutes of trading), averaging out single-trade manipulations.

**Exchange rate snapshot:** For FX [futures](/wiki/futures-contract/), settlement might be the CBOT or ECB FX rate at a specific time (noon London, for example), not the last trade on the [futures](/wiki/futures-contract/) contract itself.

**Composite settlement:** [Commodity futures](/wiki/commodity-contract-specifications/) sometimes use a weighted average of multiple spot markets. If crude cash-settles, the settlement might be the average of Brent and WTI spot prices at noon on the settlement day, published by an independent source.

## Cash vs. physical: the regulatory tension

Regulators and exchanges balance the need for cash settlement (allowing retail access, serving intangible underlyings) with the need for physical delivery (grounding contracts in reality, preventing pure speculation).

**CFTC position limits:** The US Commodity Futures Trading Commission allows higher position limits for cash-settled contracts (where the underlying is an index or rate, not a scarce physical commodity) than for [physically deliverable contracts](/wiki/delivery-mechanisms/) (where concentration could corner the physical supply).

**Bond futures:** US Treasury [futures](/wiki/futures-contract/) are [cash-settled](/wiki/cash-settlement/) but also offer a **delivery option.** The short side can choose to deliver actual bonds instead of settling cash. This dual option keeps the contract grounded while allowing cash settlement flexibility.

**Crude oil:** WTI [futures](/wiki/futures-contract/) are primarily [physically deliverable](/wiki/delivery-mechanisms/), but [cash-settled](/wiki/cash-settlement/) contracts exist (WTI cash-settled [futures](/wiki/futures-contract/) settling to Brent or other spot indices). The existence of both instruments allows hedgers choosing their preferred mechanics.

## Fair value convergence for cash-settled contracts

At expiration, a cash-settled [futures](/wiki/futures-contract/) converges to the settlement price by definition. But before expiration, it can diverge from "true" value.

Example: S&P 500 E-mini [futures](/wiki/futures-contract/) should theoretically trade at the index level plus the [cost of carry](/wiki/cost-of-carry/) (the interest rate to finance a stock position minus the dividend yield). If E-mini [futures](/wiki/futures-contract/) drift far above or below fair value, an arbitrageur can execute a cash-and-carry or reverse cash-and-carry trade:

- If [futures](/wiki/futures-contract/) are expensive: short the [futures](/wiki/futures-contract/), buy the 500 stocks in the index, hold until expiration, collect the dividend.
- If [futures](/wiki/futures-contract/) are cheap: long the [futures](/wiki/futures-contract/), short the 500 stocks, hold until expiration, pay the dividend.

These arbitrage trades keep cash-settled [futures](/wiki/futures-contract/) approximately aligned with spot plus carry, though imperfectly: transaction costs, borrow availability, and dividends create slack that allows some divergence.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/futures-contract/">Futures contract</a> — standardized derivatives that may be cash or [physically settled](/wiki/delivery-mechanisms/).</li>
<li><a href="/wiki/delivery-mechanisms/">Delivery mechanisms</a> — the alternative settlement method using physical asset transfer.</li>
<li><a href="/wiki/mark-to-market/">Mark-to-market</a> — daily revaluation of positions, typically settling variation margin in cash.</li>
<li><a href="/wiki/cost-of-carry/">Cost of carry</a> — interest and dividend rates that link cash-settled [futures](/wiki/futures-contract/) to spot prices.</li>
<li><a href="/wiki/basis/">Basis</a> — the gap between spot and [futures](/wiki/futures-contract/) prices, relevant to both cash and physical settlement.</li>
<li><a href="/wiki/sp-500-index/">S&P 500 index</a> — the underlying for the most commonly cash-settled [futures](/wiki/futures-contract/) contract.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li>Derivatives — the broader category encompassing all risk-transfer instruments.</li>
</ul>
</div>
