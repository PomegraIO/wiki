---
title: "Synthetic Forwards"
description: "A portfolio position mimicking the economics of a forward contract—created by combining spot purchases with options or futures—allowing hedgers and traders to customize payoff profiles."
---

*A forward contract is simple: lock in today's price, deliver later. But the actual forward may not exist, or may be expensive. A trader can synthesize one using pieces: buy the spot asset, finance it, and use options to cap downside. The economics are identical; the structure is custom.*

## The put-call parity synthetic

The foundation of synthetic forwards comes from put-call parity, a principle linking [call options](/wiki/call-option/), [put options](/wiki/put-option/), and [forward contracts](/wiki/forward-contract/). Mathematically:

**Call Option - Put Option = Spot Price - Forward Price**

Rearranged: **Spot + Put Option - Call Option = Forward Price**

This means a trader can replicate a forward contract by:

1. Buying the spot asset at its current price.
2. Buying a put option (insurance against price decline).
3. Selling a call option (capping your upside).

The put and call are at the same strike price, typically at-the-money or slightly out-of-the-money. Together, they create a fixed payoff at the forward date: you receive or deliver the asset at a predetermined price, indistinguishable from a true forward contract.

## Why synthesize?

**The forward may not exist.** A company needing to lock in the price of a commodity that has no liquid forward market can synthesize one using futures and options. An emerging-market stock with no forward market can be hedged by buying the stock, buying a put, and selling a call at the forward date.

**Cost control.** A put option might be expensive (in volatile markets), and selling a call generates premium that offsets the put cost. By combining them, a trader creates an effective zero-cost forward at a specific strike, accepting capped upside in exchange for capped downside.

**Customization.** A true forward contract is between two parties; both agree to the terms. But many hedgers face a fragmented forward market: one dealer offers one price, another offers another. By synthesizing, a hedger can achieve the exact payoff they want without negotiating with a forward dealer.

## The put-paid forward

A variant is the **put-paid forward**: a trader who wants to lock in a future purchase price can:

1. Buy a put option at their desired strike price.
2. Sell a call option at the same strike to finance the put.

At expiration, if the asset is below the strike, the put is exercised and they buy at the strike. If the asset is above the strike, the call is exercised and they buy at the strike (because the call buyer exercises). Either way, they buy at the strike—a locked-in forward price.

This structure is useful for companies wanting to hedge commodity costs (oil, metals, agricultural inputs) where forward prices may be expensive or unavailable.

## Variance and convexity: when synthesis breaks down

In theory, a synthetic forward is indistinguishable from a true forward. In practice, three factors create divergence:

**1. Dividend or convenience yield.** If the underlying asset pays dividends (stocks) or has a convenience yield (commodities), the put and call must be struck to account for this. A stock paying a 2% annual dividend has a lower forward price than a non-dividend stock. A synthetic forward that ignores the dividend will be priced incorrectly.

**2. Interest rate risk.** The put and call prices embed the assumed interest rate for financing. If rates change between trade date and expiration, the synthetic's cost of capital changes, and the replicating portfolio loses money even if the synthetic forward price was correct at inception. A true forward dealer carries this rate risk; a synthetic holder must manage it.

**3. Volatility and early exercise.** American options can be exercised before expiration. A synthetic forward using American options faces the risk that one leg is exercised early, breaking the hedge. European options (exercisable only at expiration) are safer but less liquid and more expensive.

## Corporate hedging examples

A US airline hedging fuel costs faces a volatile [jet fuel](/wiki/heating-oil/) market. Jet fuel futures exist but may not cover the airline's full exposure (especially for years 2-3 ahead). The airline can:

1. Buy heating oil futures (a proxy for jet fuel) for the nearest dates.
2. For dates further out, synthesize using heating oil options: buy puts at 80% of current prices (protecting against high fuel costs) and sell calls at 120% of current prices (capping hedging costs).

The result is a hedged fuel cost locked in across multiple years, approximating a forward price without relying on the illiquid forward market.

A gold mining company knows it will produce 100,000 ounces next year. Instead of selling forward (which might be expensive if gold forwards are scarce), it can:

1. Buy gold futures for near-term production months.
2. Synthesize forwards for year-ahead production using gold calls (sold, to cap upside) and gold puts (bought, to protect downside).

The company locks in approximate forward prices without negotiating custom forward contracts with a bank.

## The cost of synthesis

Synthetic forwards are not free. The cost is embedded in option premiums:

- **Buying protection (put) costs money.** If volatility is high, the put is expensive. The synthetic forward cost reflects this volatility premium.
- **Selling upside (call) generates premium.** The premium collected reduces the net cost.
- **Wide bid-ask spreads on options** (compared to forwards or futures) add execution friction.

A true forward between a bank and a client might be quoted with a bid-ask spread of 0.5 cents (in a commodity like oil). A synthetic using options might have a total bid-ask cost of 2-5 cents because each leg (put and call) has its own spread. For a hedger, this cost matters.

## Forwards synthesized from futures

A trader can also synthesize a forward using [futures](/wiki/futures-contract/) and cash lending:

1. Buy spot asset at current price.
2. Finance the purchase at the risk-free rate for the forward term.
3. Short a futures contract expiring at the forward date.

This locks in a forward-equivalent payoff: you own the spot, you've borrowed money for its cost, and you've sold the future delivery. The economics replicate a forward at the cost of spot + financing.

This is how [arbitrage](/wiki/arbitrage-pricing-theory/) traders keep spot and futures prices aligned. If the futures price diverges too far from spot + carry cost, an arbitrageur buys spot, finances it, and shorts futures, locking in the spread. This trade keeps the market honest.

## When synthesis fails

Synthesis assumes frictionless markets and availability of options at all strikes. In reality:

- **Options may not exist at your desired strike.** A small-cap stock or emerging-market currency may have options only at a few strikes, not the full continuum theory assumes.
- **Liquidity may vanish under stress.** During market shocks, bid-ask spreads on options widen dramatically, making synthesis expensive.
- **Funding risk appears.** If you must fund the spot purchase on margin, a large adverse move can trigger margin calls, forcing you to liquidate the synthetic before expiration.

A synthetic forward is a powerful tool for customizing hedges, but it is not a free lunch. It trades the simplicity and capital efficiency of a true forward contract for the flexibility and low cost of options, accepting greater complexity and execution risk.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/forward-contract/">Forward contract</a> — the simple, direct instrument that synthetics aim to replicate.</li>
<li><a href="/wiki/call-option/">Call option</a> — sold in synthetic forwards to cap upside and offset put cost.</li>
<li><a href="/wiki/put-option/">Put option</a> — bought in synthetic forwards to protect against downside.</li>
<li><a href="/wiki/futures-contract/">Futures contract</a> — an alternative to options for synthesizing forward-like payoffs using spot and financing.</li>
<li><a href="/wiki/arbitrage-pricing-theory/">Arbitrage</a> — the mechanism that keeps synthetics, forwards, and spot prices aligned in efficient markets.</li>
<li><a href="/wiki/cost-of-carry/">Cost of carry</a> — the financing and storage cost component of forward pricing.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — overview of the broader option market that provides the building blocks for synthetics.</li>
<li>Derivatives — the category encompassing all hedging and risk-transfer tools.</li>
</ul>
</div>
