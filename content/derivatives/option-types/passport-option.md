---
title: "Passport Option"
description: "An exotic option whose payoff equals the profit (or loss) from an optimally-traded account in the underlying asset, chosen freely by the holder."
keywords:
  - passport option
  - exotic option
  - trading option
  - derivatives
image: "/svg/derivatives.svg"
---

*A **passport option** is an [option](/option/) that pays off the cumulative profit or loss from a self-directed trading account in an underlying asset, where the holder decides the timing and size of every buy and sell transaction within the option's life. The holder is free to trade as much or as little as desired; the option's payoff at expiry equals whatever the optimally-chosen trading strategy earned, with a defined loss floor.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Passport Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and structured contracts." />

<div class="wiki-infobox-caption">A trader's option: payoff is the profit from optimal self-directed trading.</div>

|   |   |
|---|---|
| **What it is** | An option granting the right to trade freely in a designated account and keep the profit (or absorb a floored loss) |
| **Also called** | Passport option, trading option, account option |
| **Payoff at expiry** | Max(0, cumulative P&L from all trades executed) or Max(floor, cumulative P&L) |
| **Holder's control** | Entry and exit timing, position size, and number of trades entirely at holder's discretion |
| **Common underlyings** | Single [stocks](/stock/), [indices](/sp-500-index/), [commodities](/crude-oil/), [forex](/us-dollar/) pairs |
| **Floor mechanism** | Limits the holder's loss; usually zero or a specified negative amount |
| **Seller's risk** | Unlimited if holder executes an optimal strategy; premium reflects this |

</aside>

## The core concept: optionality on trading outcomes

Unlike a standard [call option](/call-option/), which gives the holder one right (to buy at a fixed strike), a passport option grants the holder a sequence of decisions spanning the entire life of the contract. Within a defined account, the holder can buy and sell the underlying as many times as desired. Every trade is executed at the prevailing market price (or a benchmark price, depending on contract terms). At expiry, the holder receives the aggregate [profit](/stock/) from all these trades.

The brilliance of the structure lies in its flexibility. If the underlying trends upward, the holder can scalp small gains repeatedly, or hold through the entire move. If the underlying oscillates between two levels, the holder can buy at the low and sell at the high, multiple times over. If the market crashes, the holder simply does not trade, limiting losses to zero (or the contract's specified floor).

## The valuation paradox

Passport options pose a formidable pricing problem. The seller is, in effect, offering the holder a free live-trading account where every transaction incurs zero [bid-ask spread](/bid-ask-spread/) and zero commissions, and the holder faces no [margin calls](/margin-call-forex/) or funding costs. The holder's optimal strategy—knowing the full path of prices in advance (via perfect hindsight)—would generate a profit equal to the sum of all intra-period moves in one direction.

In real time, the holder does not have perfect hindsight. The passport option's theoretical value reflects the expected payoff under the holder's best reasonable trading strategy—a strategy that adapts to market moves as they occur, but without knowledge of future prices. This makes valuation complex: the option's value depends not just on the underlying's volatility and path, but on how rational, liquidity-constrained traders would actually respond to observed prices.

[Monte Carlo simulation](/discounted-cash-flow-valuation/) with optimal stopping problems offers one numerical approach. The simulation models price paths, and for each path, an optimal-control algorithm determines the best sequence of trades (buy/sell decisions) a trader could execute. The average payoff across all paths, discounted, approximates the option's fair value.

## Why passport options are rare and why they matter

Passport options are exotic enough that only specialist banks quote them, and volumes are tiny. The reason: the premium is expensive because the seller is exposed to very large losses if the underlying exhibits high [volatility](/historical-volatility/) and frequent mean-reverting swings (ideal for a scalping trader). During periods of rising volatility, dealers will either stop quoting entirely or demand massive premiums.

Yet passport options are conceptually important. They represent the limit case of path-dependent, American-style ([exercisable at any point](/option/)) exotic options. They also embody a fundamental insight: if a seller can force a buyer to behave like a disciplined trader (buying low, selling high) and capture the spread between the buyer's profit and the seller's hedging cost, the seller has a scalable business. In practice, traders and hedge funds face funding costs, [bid-ask spreads](/bid-ask-spread/), and opportunity costs that erode this edge—but on a frictionless passport, the holder's advantage is nearly complete.

## The floor mechanism and loss containment

Most passport options include a **floor**, often set at zero. The holder can never lose more than the [premium](/option-premium/) paid upfront. Some contracts allow a small negative floor (e.g., −500 basis points), giving the holder a tiny buffer of downside tolerance in exchange for a lower premium.

The floor is critical to the seller's survival. Without it, a seller of an unfloored passport option faces infinite loss: if the underlying falls from 100 to 50, stays there, and the holder makes no trades, the payoff is zero (the holder's loss floor). But if the underlying then falls to 25, rises back to 100, and falls to 50 again, the holder with perfect hindsight could scalp the move repeatedly, generating a large profit. The seller's hedge—a static position or options overlay—may be insufficient for such extreme scenarios.

## Use cases and audience

Passport options appeal most to experienced traders and proprietary trading desks with strong convictions about market [volatility](/historical-volatility/) and mean reversion. A desk convinced that equity indices will swing between tight bands over the next six months might use a passport option to exploit those swings without putting up capital or risking margin.

[Hedge funds](/hedge-fund/) with algorithmic trading capabilities sometimes view passport options as a way to outsource execution risk. Rather than running their own models and incurring slippage, they purchase a passport option and execute their strategy within its protected envelope.

Portfolio managers sometimes use passport options as a volatility play. If [implied volatility](/implied-volatility/) is low but the manager expects sharp moves, a passport option's value will rise as realized volatility increases, even if the underlying's direction is unclear.

## Comparison to other exotics

A passport option gives maximum flexibility; the holder's edge is the freedom to trade. A [cliquet option](/cliquet-option/) locks in gains on a rigid schedule, offering less control but more certainty about payoff distribution. A [shout option](/shout-option/) grants one reset choice. A [power option](/power-option/) has a fixed, nonlinear payoff formula—no trading involved.

The passport option is the most "trader-friendly" of these structures because the payoff rewards optimal decision-making. But that optionality is also why it's priced aggressively and rarely offered by conservative dealers.

## The practical constraints

In live markets, the passport option is typically confined to major [liquid](/liquidity-risk/) underlyings: large-cap stocks, major [indices](/sp-500-index/), commodity [futures](/futures-contract/), and active [forex](/currency-risk/) pairs. Dealers will not quote on illiquid securities because the hedging cost becomes prohibitive.

Execution is usually via a benchmark price (e.g., the opening or closing price of each day, or a volume-weighted average price over a time window) rather than true live pricing. This simplifies settlement and reduces disputes over "what price did you get."

Terms typically include position limits: the holder may be restricted to a maximum notional size per trade or in aggregate, preventing the holder from leveraging a single underlying to extreme levels.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational derivative granting a right to buy or sell
- [Call Option](/call-option/) — the right to purchase an asset at a strike price
- [Bid-Ask Spread](/bid-ask-spread/) — the cost of buying and selling in financial markets
- [Volatility](/historical-volatility/) — the degree of price fluctuation in an asset
- [Implied Volatility](/implied-volatility/) — the expected volatility priced into an option
- [Cliquet Option](/cliquet-option/) — exotic option with automatic periodic resets
- [Shout Option](/shout-option/) — exotic option with one holder-chosen reset moment
- [Power Option](/power-option/) — exotic option with a nonlinear payoff function

### Wider context

- [Exotic Option](/option/) — family of nonstandard derivatives with complex features
- [Derivatives](/option/) — financial contracts whose value derives from an underlying asset
- [Hedge Fund](/hedge-fund/) — investment fund employing active trading and sophisticated strategies
- [Volatility Smile](/volatility-smile/) — structure of implied volatilities across strikes
- [Futures Contract](/futures-contract/) — standardized derivative traded on organized exchanges
- [Currency Risk](/currency-risk/) — exposure to changes in foreign exchange rates

</div>
