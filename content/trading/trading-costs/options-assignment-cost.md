---
title: "Options Assignment Cost"
description: "Details the fees and indirect costs triggered when an options contract is assigned, including per-contract charges and capital tied up."
keywords:
  - options assignment cost
  - assignment fees options
  - options assignment expenses
  - exercise cost vs assignment
  - options trading fees
image: /svg/trading.svg
---

*An **options assignment cost** encompasses the explicit fees charged by brokers when an option contract is assigned, plus the implicit costs of capital tied up, spread widening on forced liquidation, and timing risk—factors that often exceed the stated per-contract commission.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Options Assignment Cost — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Assignment costs are often hidden; the explicit fee is small, but hidden capital and liquidity costs can be substantial.</div>

|   |   |
|---|---|
| **Typical broker commission per assignment** | $5–$20 per contract (some brokers: $0) |
| **Capital requirement at assignment** | 100 shares × contract price (per share) in cash or margin |
| **Implicit cost** | Bid-ask spread widening, forced liquidation timing, opportunity cost |
| **When assignment hits hardest** | Deep in-the-money short calls; short puts assigned into falling markets |
| **Assignment vs. early exercise** | Both trigger costs; assignment is automatic; exercise is voluntary |

</aside>

## Explicit Assignment Fees

When an options contract is assigned—meaning the holder of a long option exercises it and forces the writer (seller) to fulfill the contract—the broker charges a commission. This fee varies widely:

- **Full-service and traditional brokers**: $10–$20 per contract
- **Discount and zero-commission brokers**: $0–$10 per contract; many now offer zero assignment fees
- **Market-maker fees**: In some accounts, only the initial trade is charged; assignment is free

A trader writing 10 short [call options](/call-option/) who faces full assignment on all 10 contracts could face $100–$200 in direct fees. While this seems modest, assignment costs compound when assignment is frequent—for example, a [covered call](/covered-call/) strategy that rolls every month and experiences partial assignments can easily accumulate hundreds of dollars in assignment fees annually.

## Capital Requirement at Assignment

The larger hidden cost is **capital lockup**. When a short [call option](/call-option/) is assigned, the seller must deliver 100 shares per contract. If the seller does not already own the shares, the broker initiates a forced purchase at the [strike price](/strike-price/). If the seller is short on cash, the broker extends margin credit, triggering:

- **Margin interest**: typically 2–8% annually, prorated to the holding period
- **Margin maintenance requirement**: the collateral ties up additional liquid capital
- **Risk of margin call**: if the underlying asset drops sharply, the seller may face forced liquidation

Conversely, a short [put option](/put-option/) assignment requires cash (or margin availability) equal to the strike price times 100. A trader assigned on 10 short puts at a $50 strike faces a $50,000 capital requirement. If the trader does not have that cash, the broker supplies it via margin, adding interest cost.

Even if the broker charges zero commission, the 6-month cost of margin at 5% on $50,000 equals $1,250—far exceeding the explicit commission.

## Timing and Liquidity Costs

Assignment often occurs at inconvenient moments:

**Forced liquidation after assignment:** A trader assigned on a short [call](/call-option/) must deliver shares. If the trader does not already own them and must buy in the open market, a suddenly adverse price movement forces a purchase at a worse price than expected. The bid-ask spread widens in volatile markets, adding to the true cost.

**Opportunity cost:** If a short [put](/put-option/) is assigned during a market downswing, the trader acquires the stock at the strike price, which may be well above the subsequent low. Assignment does not wait for optimal timing—the trader is forced into the position immediately.

**Reinvestment timing:** An assigned [call](/call-option/) writer who owns shares loses them just before a dividend or earnings announcement, forfeiting upside or dividend income.

## Exercise vs. Assignment: Cost Comparison

A long option holder—the buyer—faces a choice: exercise the option to acquire or sell the underlying asset, or sell the option itself in the market.

**Exercise cost:**
- Broker commission: $5–$20
- Immediate capital requirement if buying shares (no recovery of any [time value](/time-value/))
- No recovery of the [option premium](/option-premium/) paid; the buyer owns the intrinsic value only

**Selling the option instead of exercising:**
- Single broker commission on the sale
- [Time value](/time-value/) is recovered (the bid price includes any remaining extrinsic value)
- No immediate capital requirement
- No assignment cost to the seller of that option (that burden shifts to whoever buys it)

In most cases, a rational buyer should sell a profitable option rather than exercise it early, because the sale price includes both intrinsic value and remaining time value. However, exceptions exist—most notably, exercising a [call option](/call-option/) on a dividend-paying stock just before the ex-dividend date captures the dividend payment, which can outweigh the [time value](/time-value/) sacrifice.

## Assignment Risk in Spreads and Collars

Traders running multi-leg strategies face compounded assignment costs. A [call spread](/call-option/) (long call + short call) assigned on the short leg forces the purchase of 100 shares at the short strike. If the long call expires worthless or must be closed at a loss, the trader experiences:

1. Commission on assignment (the short call)
2. Loss on the long call leg
3. Capital requirement for the long stock position

Similarly, a [collar strategy](/protective-put/)—long stock, long [put](/put-option/), short [call](/call-option/)—suffers assignment if the short call is in-the-money. The seller is forced to sell shares, potentially losing upside if the stock rallies past the strike.

## Minimizing Assignment Costs

Traders reduce assignment costs through:

- **Choosing low-commission or zero-fee brokers:** Assignment fees of $0–$2 per contract are increasingly common
- **Rolling before expiration:** Closing the short option and opening a new one at a later expiration avoids assignment but incurs two commissions; the net benefit depends on time decay and volatility
- **Avoiding deep in-the-money short calls:** [In-the-money](/in-the-money/) short calls are nearly certain to be assigned; a short call significantly out-of-the-money is less likely to be assigned (though not immune)
- **Using cash-settled index options:** Some index options are cash-settled, eliminating the need to deliver shares and reducing assignment-related capital requirements
- **Accepting assignments strategically:** For a [covered call](/covered-call/) strategy, assignment means selling shares at the strike price—often the intended outcome; the "cost" is acceptable if it aligns with the seller's target price

## See also

<div class="wiki-seealso">

### Closely related

- [Call Option](/call-option/) — contracts that trigger assignment costs
- [Put Option](/put-option/) — alternative assignment scenario
- [Strike Price](/strike-price/) — determines capital required at assignment
- [Covered Call](/covered-call/) — strategy where assignment is the expected outcome
- [Time Value](/time-value/) — component of option price lost at early exercise
- [In the Money](/in-the-money/) — deep ITM options are almost certain to be assigned
- [Option Premium](/option-premium/) — price paid or received in the initial trade

### Wider context

- [Option](/option/) — fundamental contract mechanics
- [Derivatives Hedging](/derivatives-hedging/) — assignment in risk management strategies
- Margin — capital requirement and cost when assignment forces a position

</div>
