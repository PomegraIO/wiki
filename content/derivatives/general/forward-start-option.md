---
title: "Forward Start Option"
description: "An option that is activated in the future with the strike price set at inception based on a predetermined formula."
keywords:
  - exotic option
  - forward contract
  - option strike
  - deferred exercise
---

*A forward start option is an [exotic option](/wiki/option/) that does not begin its active life immediately. Instead, the option is initiated at a future date (the "start date"), and the strike price is determined either at inception or on the start date using a preset formula, typically as a percentage of the spot price at that time. The holder receives the benefit of an already-determined strike price, locked in through the formula, eliminating strike-setting uncertainty at the start date.*

<aside class="wiki-infobox">

| Attribute | Detail |
|---|---|
| **Start date** | Fixed future date when option becomes active |
| **Strike setting** | Formula-based (e.g., 100% of spot price on start date) |
| **Payoff** | Standard option payoff at expiration |
| **Counterparty** | Usually banks or institutions trading derivatives |
| **Premium** | Paid at inception, not at start date |
| **Use case** | Equity compensation, deferred hedge strategies |

</aside>

## How the strike price is determined in advance

The key innovation of a forward start option is that the strike price is set according to a formula, not simply deferred. The most common formula is: the strike equals 100% of the spot price on the start date (an "at-the-money forward start"). If the stock is $50 today and the start date is 6 months away, the exact strike price on that date is unknown. But the formula guarantees that the strike will equal the stock price on that date—making the option at-the-money when it activates.

Alternative formulas are common. A strike might be set at 105% of the spot price on the start date (a slightly out-of-the-money starting point). Or it might be set at the spot price on the start date plus a fixed spread. The key is that the formula is agreed today; the parties are not negotiating the strike on the start date. This eliminates price discovery risk and transaction costs.

The premium (the option price) is paid today, at inception. The holder pays for the option immediately, even though the option doesn't become active for months. This is conceptually clean: you pay today for an option that will exist in the future. The future is certain because the start date is fixed and the strike formula is already set.

## Why companies use forward start options in compensation

Forward start options are most commonly seen in [equity compensation](/wiki/equity-compensation/) for executives. A company grants an executive a forward start option as part of their bonus or incentive plan. The option might start one year in the future and expire three years after that (a two-year exercise window). The strike is set at the stock price on the grant date of the option (not the day the option becomes active).

This serves several purposes. First, it aligns executive compensation with long-term performance—the executive must hold through the start date to benefit. Second, it avoids repricing issues. If the company's stock has fallen by the start date, the at-the-money forward start option may be underwater (out-of-the-money), penalizing the executive. But the formula was agreed in advance, avoiding the political problem of resetting the strike after adverse performance.

Third, it allows the company to smooth compensation expense. If the company grants a large option package, spreading it across multiple start dates (some options starting after 1 year, others after 2 years) distributes vesting and exercise decisions, reducing the lumpiness of expense and allowing executives multiple chances to exercise profitably.

## Forward start options vs. standard options

A standard option is active from inception. You buy a call option on XYZ stock today for $3 (the premium), with an expiration six months away and a $50 strike. You can exercise today or any time until expiration. A forward start option is different: you pay the $3 premium today, but the option doesn't activate for 6 months. At that point, it becomes active, likely at-the-money, and you have perhaps 2 years to exercise.

The forward start option is cheaper than an equivalent standard option because the optionality is deferred. Volatility affects option pricing; less time to expiration means less time for the stock to move favorably. A standard 2.5-year option is more valuable than a forward start option that activates in 1 year and expires in 2.5 years. The extra 1 year of dormancy reduces the option's value.

The formula-based strike is a crucial difference from a standard option bought later. If you buy a call option 6 months from now with a $50 strike, the strike is whatever XYZ's price is at that moment. If XYZ has risen to $60, a $50 strike is in-the-money—deep in-the-money, in fact, and much more valuable. But if XYZ has fallen to $40, the option is out-of-the-money. The forward start option with the at-the-money formula guarantees you an at-the-money starting point, eliminating this uncertainty.

## Pricing forward start options

Forward start options are harder to price than standard options because they depend on two sources of uncertainty: the stock price at the start date (which determines the strike) and the stock price at expiration. Using the [Black-Scholes model](/wiki/black-scholes-model/), a standard option has one uncertain endpoint; a forward start option has two.

The standard approach is to condition on the stock price on the start date. At that point, the forward start option becomes a standard option with a known strike (determined by the formula and the prevailing stock price). The value of the forward start option today is the expected value of what that option will be worth on the start date. This requires integrating over all possible stock prices on the start date, weighted by their probability.

Because the strike is set as a function of the stock price, the option is always at-the-money when it activates. An at-the-money option has roughly 50% probability of expiring in-the-money and 50% probability of expiring out-of-the-money. This predictability is valuable for pricing. The [implied volatility](/wiki/implied-volatility/) of the forward start option reflects not just the volatility of the stock but also the correlation between the stock price on the start date and its price at expiration. High volatility increases the option's value; high correlation between the two dates decreases it.

## Forward start options in hedging strategies

Beyond compensation, forward start options are used in deferred hedging strategies. A company knows it will have a risk six months from now (for example, it will receive a shipment of inventory and needs to hedge currency risk), but it doesn't want to pay for the hedge today. A forward start option allows the company to pay for the hedge now but have it become active when the risk emerges.

This is cheaper than buying a standard option today that would be active for the full 6 months before the risk begins. The company avoids paying for a 6-month dormancy period. It's also more flexible than waiting to buy the option in 6 months, when the underlying price may have moved unfavorably and the option may be cheaper or more expensive.

## Risk and tax considerations

From a risk perspective, the forward start option has an unusual feature: the holder's profit/loss depends heavily on the stock price on the start date. If the stock falls sharply and is low on the start date, the option activates with an at-the-money strike, and the holder must wait for the stock to recover to break even. If the stock rallies on the start date, the option activates deep in-the-money (relative to where the holder started), increasing the probability of profit.

This makes forward start options sensitive to "early" price movements—moves before the start date. An executive granted a forward start option that activates in 1 year has no payoff in that first year. If the stock doubles in the first year, the option activates at-the-money, and the executive loses the entire first-year gain. The option only captures gains after the start date.

For tax purposes, the timing of the forward start option is important. Under U.S. tax law, if the option is granted as compensation, the grant date (not the start date) determines the holding period for long-term capital gains treatment. The spread between the strike and the exercise price is taxed as ordinary income or deferred compensation, depending on the option type ([nonqualified option](/wiki/employee-stock-options/) vs. incentive stock option).

## Variations: cliquets and cliquet options

A related structure is the **cliquet option** (from the French word for "ratchet"), which combines multiple forward start options into a single package. Each cliquet "level" is a forward start option that activates sequentially. The first level activates today; the second activates one year from now; the third activates two years from now. Each level is at-the-money when it activates. The payoff at expiration is the sum of all levels' payoffs.

Cliquets are common in long-dated compensation plans and guarantee-seeking strategies. They lock in gains at each level while allowing future gains to be captured at each step. If the stock rises every year, each level captures the year's gain. If the stock falls one year and recovers the next, the fallen year's level might expire worthless, but the recovery year captures fresh gain.

<div class="wiki-seealso">

### Closely related
- [Option](/wiki/option/) — Basic right to buy or sell at a future date
- [Call Option](/wiki/call-option-equity/) — Right to buy at a preset price
- [Exotic Option](/wiki/option/) — Non-standard option structures
- [Black-Scholes Model](/wiki/black-scholes-model/) — Standard option pricing model
- [Implied Volatility](/wiki/implied-volatility/) — Volatility implied by option prices

### Wider context
- [Equity Compensation](/wiki/equity-compensation/) — Stock and option grants to employees
- [Derivatives](/wiki/option/) — Financial instruments derived from underlying assets
- [Hedging with Futures](/wiki/hedging-with-futures/) — Using futures to reduce risk
- [Option Pricing](/wiki/monte-carlo-options-pricing/) — Valuation of option contracts

</div>
