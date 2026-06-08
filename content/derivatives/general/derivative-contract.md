---
title: "Derivative Contract"
description: "The foundational legal and structural anatomy of any derivative instrument—the binding agreement whose value depends on an underlying asset or benchmark."
keywords:
  - derivative contract
  - derivative definition
  - derivative agreement
  - options contracts
  - futures contracts
image: /svg/derivatives.svg
---

*A **derivative contract** is a binding legal agreement whose value is derived from the price or performance of an underlying asset, index, or benchmark. The contract specifies the rights and obligations of both parties, including the underlying asset, the contract size, the expiration date, settlement terms, and the payoff structure. All derivatives—whether [options](/option/), [futures](/futures-contract/), swaps, or forwards—follow this basic anatomy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Derivative Contract — structural essentials</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivative contracts and structured instruments." />

<div class="wiki-infobox-caption">A legally binding agreement whose payoff depends on an underlying asset or rate.</div>

|   |   |
|---|---|
| **What it is** | A bilateral contract whose value derives from an underlying asset |
| **Key parties** | Two counterparties with opposing economic interests |
| **Underlying asset** | Stock, bond, commodity, currency, index, or interest rate |
| **Contract notional** | The quantity of the underlying referenced in the contract |
| **Expiration date** | When the right or obligation ceases |
| **Settlement** | Physical delivery or cash settlement of the payoff |
| **Legal framework** | ISDA master agreements, exchange rules, or bespoke terms |

</aside>

## The fundamental structure

Every derivative contract contains several essential terms. The **underlying** is the asset or benchmark on which the contract's value depends: crude oil, the S&P 500 index, a currency pair, or a bond. The **contract size** (also called the notional or multiplier) specifies how many units of the underlying the contract represents. A single [crude oil](/crude-oil/) [futures contract](/futures-contract/) on the NYMEX represents 1,000 barrels; a single S&P 500 [options contract](/option/) represents 100 shares of the index.

The **expiration date** is when the contract expires and the parties must settle. Options expire on specific dates (typically the third Friday of the month for equity options). [Futures contracts](/futures-contract/) roll over periodically; a given contract matures and is replaced by the next month out. [Forward contracts](/forward-contract/) have customized expiration dates negotiated between the parties.

The **payoff structure** defines who wins and who loses as the underlying price moves. In a [call option](/call-option/), the buyer has the right to purchase the underlying at a fixed [strike price](/strike-price/)—a right that becomes valuable if the underlying's price rises above the strike. In a [put option](/put-option/), the buyer has the right to sell at the strike, valuable if the price falls. In a [futures contract](/futures-contract/), both parties are obligated to settle at the [expiration date](/expiration-date/) at a price agreed now, locking in the rate today.

## Counterparty dynamics and risk

Every derivative contract is a zero-sum game between two counterparties. If one party profits, the other loses by an equal amount (before [transaction costs](/bid-ask-spread/)). This opposing interest structure creates both benefit and peril. A farmer using a futures contract to lock in the price of next year's wheat harvest offsets the risk of falling grain prices; the buyer of that futures contract—typically a grain handler—accepts the risk in exchange for locking in a known input cost. Both benefit from [price discovery](/price-discovery/) and risk transfer.

But if one counterparty defaults or the other faces unexpected volatility, the contract creates [counterparty risk](/counterparty-risk/). Historically, this was acute in over-the-counter derivatives (customized contracts traded between banks and institutions). The 2008 financial crisis exposed how [counterparty risk](/counterparty-risk/) can cascade through the financial system. Today, most standardized derivatives trade on exchanges or through clearinghouses that interpose themselves as the counterparty, eliminating direct bilateral risk.

## Standardization vs customization

**Exchange-traded derivatives** (such as equity [options](/option/) on US stock exchanges or [futures contracts](/futures-contract/) on commodity exchanges) are standardized. The contract terms—underlying, size, expiration, strike prices—are fixed by the exchange. This standardization enables liquid trading; millions of contracts trade daily, and bid-ask spreads stay tight. The trade-off is inflexibility: if you need an unusual expiration date or strike price, you're out of luck.

**Over-the-counter (OTC) derivatives** are customized, bilateral contracts. Two parties negotiate a forward on a specific commodity, a swaption tailored to a bank's liabilities, or a structured product with exotic payoffs. OTC contracts offer flexibility but carry wider bid-ask spreads, less liquidity, and greater [counterparty risk](/counterparty-risk/). After the 2008 crisis, regulatory pressure pushed standardized derivatives onto exchanges and clearinghouses; many OTC derivatives now clear through central counterparties as well.

## Settlement mechanics

Derivatives settle in two ways. **Physical settlement** means the underlying asset is actually delivered. If you hold a crude oil futures contract to maturity, you take delivery (or arrange for delivery) of 1,000 barrels of oil. If you hold a [call option](/call-option/) on 100 shares of Apple and exercise it, you buy 100 actual shares.

**Cash settlement** means the parties exchange cash equal to the difference between the contract price and the market price. Most equity [index options](/option/) (such as those on the [S&P 500](/sp-500-index/)) settle in cash; you can't take physical delivery of an index. Many commodity and interest-rate [futures contracts](/futures-contract/) can be settled either way, though most are cash-settled or offset (closed out) before expiration.

## Leverage and notional value

A derivative's notional value is often far larger than the cash outlay. An [options contract](/option/) on 100 shares might cost $200 in premium but control $50,000 of stock. A single crude oil futures contract controls 1,000 barrels worth tens of thousands of dollars but requires only a few thousand dollars in [margin](/margin-call-forex/) to maintain. This leverage is a defining feature: derivatives allow you to gain economic exposure to an asset with a fraction of the cost of owning it outright.

Leverage cuts both ways. A modest move in the underlying can result in a total loss of the derivative or, with [margin](/margin-call-forex/), losses exceeding the initial investment. This is why derivative contracts are tools for hedging, speculation, or sophisticated portfolio management—not casual savings vehicles.

## The role of pricing models

Determining the fair value of a derivative requires mathematical models. The [Black-Scholes model](/black-scholes-model/), developed in 1973, revolutionised options pricing by expressing an option's value as a function of the underlying price, volatility, time to expiration, and [interest rates](/interest-rate/). Subsequent models account for [dividends](/dividend/), multiple assets, path-dependent payoffs, and other complexities.

These models aren't perfect—they assume constant volatility, no [dividends](/dividend/), and no [transaction costs](/bid-ask-spread/)—but they provide the benchmark by which traders price and [hedge](/hedge-fund/) derivative positions. The Greeks—[delta](/delta/), [gamma](/gamma/), [vega](/vega/), and [theta](/theta/)—quantify how an option's value changes with moves in the underlying, [volatility](/volatility-smile/), and time decay.

## Regulatory and legal frameworks

Exchange-traded derivatives are governed by the exchange rules and by regulatory bodies such as the [Securities and Exchange Commission](/securities-and-exchange-commission/) and the Commodity Futures Trading Commission. OTC derivatives are typically documented under the International Swaps and Derivatives Association (ISDA) master agreement, a standardised legal framework negotiated between institutions.

Post-2008, the [Dodd-Frank Act](/dodd-frank-act/) imposed clearing and margin requirements on many derivatives, shifting risk from bilateral counterparties to central clearinghouses. The intent was to reduce [systemic risk](/systemic-risk/) but at the cost of higher collateral requirements and administrative overhead.

## Common derivative types

The broad universe of derivatives includes [options](/option/) (rights, not obligations), [futures contracts](/futures-contract/) (binding obligations), [forwards](/forward-contract/) (customized, bilateral futures), swaps (exchanging one cash flow stream for another), and structured products (customised bundles of derivatives and underlying assets). Each serves different hedging, speculative, or arbitrage needs.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — right (not obligation) to buy or sell the underlying at a fixed price
- [Futures Contract](/futures-contract/) — binding obligation to settle at a predetermined price on a future date
- [Forward Contract](/forward-contract/) — customised bilateral agreement equivalent to a futures contract
- [Call Option](/call-option/) — right to purchase the underlying at a strike price
- [Put Option](/put-option/) — right to sell the underlying at a strike price
- [Black-Scholes Model](/black-scholes-model/) — foundational framework for options valuation

### Wider context

- [Counterparty Risk](/counterparty-risk/) — risk that the other party fails to settle
- [Interest Rate](/interest-rate/) — underlying benchmark for many derivatives
- [Volatility Smile](/volatility-smile/) — empirical pattern in option pricing inconsistent with theory
- [Dodd-Frank Act](/dodd-frank-act/) — post-2008 regulatory overhaul governing derivatives clearing
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — oversees exchange-traded derivatives
- [Over-the-Counter Market](/over-the-counter-market/) — venue for customised bilateral derivatives

</div>
