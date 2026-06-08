---
title: "Share-Based Compensation Accounting"
description: "The methods by which companies measure and expense employee stock options, restricted stock, and other equity awards according to fair value standards."
keywords:
  - stock options accounting
  - restricted stock units
  - equity compensation
  - ASC 718
  - fair value measurement
  - vesting schedules
image: "/svg/accounting.svg"
---

*Share-based compensation—stock options, restricted stock units, and other equity awards—must be measured at fair value on the grant date and expensed over the vesting period as a non-cash charge against earnings. The accounting is designed to reflect the true economic cost to shareholders of diluting ownership, but the fair value estimates are subject to judgment and can obscure the real value transferred.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Share-Based Compensation — key facts</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for accounting topics." />

<div class="wiki-infobox-caption">The accounting framework that forces companies to expense equity awards and measure their economic cost to existing shareholders.</div>

|   |   |
|---|---|
| **What it is** | Non-cash expense recorded for employee equity awards granted over their vesting period |
| **Also called** | Stock-based compensation; equity compensation; stock option expense |
| **Governed by** | ASC 718 (US GAAP); IFRS 2 (IFRS) |
| **Measured at** | Fair value on the grant date |
| **Expensed over** | The vesting period (usually 4 years for options and restricted stock) |
| **Key impact** | Reduces [net income](/income-statement/) but does not reduce cash (until settlement) |
| **Employees affected** | Typically executives and key talent; may extend to all employees |

</aside>

## Why this expense exists at all

Before 2005, companies in the US could avoid expensing stock options altogether—a loophole that created perverse incentives. A tech company could grant executives millions of options at zero recorded expense, then repurchase shares to offset the dilution. The [earnings](/income-statement/) appeared untouched, but shareholders had been economically diluted. The FASB closed this loophole by requiring all share-based awards to be expensed at fair value.

The logic is straightforward: when a company grants an employee 10,000 stock options, it has given away something of value—the right to buy shares at a fixed price. If those options vest, the company's existing shareholders will be diluted. Expensing the award forces the company to recognize this cost upfront.

## The grant date and fair value measurement

The accounting journey begins on the grant date—the day the company and employee agree to the award terms. On that date, the company measures the fair value of the award using one of two methods:

**Intrinsic value** (rarely used now): The difference between the stock price and the strike price on the grant date. For an option granted at-the-money (strike = current stock price), intrinsic value is zero, so this method understates the option's true economic value.

**Fair value** (the required standard): An estimate of what a willing buyer and seller would pay for the award. For options, companies use the [Black-Scholes model](/black-scholes-model/) or a binomial tree, which incorporates stock price volatility, time to expiration, [risk-free rate](/interest-rate/), and [dividend yield](/dividend-yield/). For restricted stock, fair value is simply the stock price on the grant date (since the recipient will receive shares outright upon vesting).

## Volatility and the Black-Scholes judgment call

The Black-Scholes model's largest input is **volatility**—the expected standard deviation of future stock returns. A company with 30% implied volatility will generate a much higher option fair value than one with 10% volatility. And volatility is a forecast, not a known number.

Therein lies a major judgment point. Should a company use historical volatility (the past 2 years of stock price swings) or implied volatility (the market's expectation embedded in traded options)? A mature, stable company might use 15% historical volatility; a high-growth tech startup might justify 60% implied volatility. The difference can double the option's calculated fair value, and thus the annual expense.

Regulators scrutinize this assumption. If a company appears to be gaming the volatility input to suppress expense, auditors will push back. But the reality is that volatility estimates can reasonably vary, and no auditor can prove the "true" future volatility.

## Vesting and the matching principle

Once the grant-date fair value is locked in, the company recognizes that expense over the vesting period. If an option vests 25% per year over 4 years, the company recognizes 25% of the total fair value as an expense in each of years 1–4.

This follows the [matching principle](/revenue-recognition/): the company links the expense to the periods in which the employee provides service in exchange for the award. An executive who stays 4 years and vests fully delivers 4 years of service; the expense is recognized ratably over those 4 years.

However, if the employee leaves before fully vesting, the unvested portion is never expensed. This creates a partial reversal: if an employee granted 10,000 options vests 50% and then leaves, the company reverses the remaining 50% of the deferred expense.

## Stock price changes and the fixed fair value problem

Here is a subtle but important fact: **once the fair value is fixed on the grant date, stock price changes after that date do not affect the recorded expense.** An option granted when the stock is $50 and valued at $10 per option is expensed based on that $10 fair value, even if the stock rises to $150 during the vesting period.

This asymmetry can be jarring. An option that was "underwater" (out-of-the-money) on the grant date—i.e., the strike price is above the stock price—is measured at some positive fair value by Black-Scholes (because there is still time value), but if the stock subsequently crashes, the option may expire worthless. Yet the company will have expensed its full fair value.

Conversely, if an option is granted at-the-money for $5 and the stock doubles, the option might be worth $100, but the company expenses only the $5 grant-date fair value. This is why equity compensation can be a bargain for shareholders if the stock performs well.

## Treatment of different award types

**Stock options:** Expensed based on Black-Scholes or binomial fair value, with adjustments for forfeitures.

**Restricted stock and RSUs (Restricted Stock Units):** Expensed at the stock price on the grant date, straight-line over vesting. If the award includes a market condition (e.g., vest only if the stock outperforms the S&P 500), the company uses a Monte Carlo simulation to estimate probability-adjusted fair value.

**Performance stock:** If vesting depends on meeting a profit or revenue target, the company reverses expense if the performance condition appears unlikely to be achieved.

## The interaction with [share buybacks](/share-buyback/)

Many companies offset the dilutive effect of equity compensation through share repurchases. The [earnings per share](/earnings-per-share/) math is revealing: if a company earns $1 billion and has 500 million weighted-average shares outstanding, EPS is $2. If it then grants options that dilute to 510 million shares (a 2% dilution), EPS would fall to $1.96—unless the company repurchases 10 million shares, maintaining 500 million shares outstanding.

From a real economic perspective, this repurchase is partially a response to the dilution from equity compensation. The company pays real cash to repurchase shares, offsetting the non-cash equity expense. Investors who focus only on the P&L can miss this cash outflow.

## International variations

IFRS 2 requires similar fair value measurement and expense recognition, but with some differences in timing and treatment of modifications. If a company reprices options (e.g., reduces the strike price when the stock falls), IFRS 2 can require remeasurement of the award at the repricing date, increasing expense. US GAAP (ASC 718) is more restrictive about when remeasurement is required, which can result in lower total expense under GAAP.

Additionally, IFRS 2 requires companies to recognize a liability (rather than equity) for cash-settled awards (e.g., cash bonuses tied to stock price), with remeasurement at each reporting date until settlement.

## Quality of earnings concerns

A sophisticated investor will note that share-based compensation is a growing slice of total compensation at many tech and high-growth companies. The expense is real—it represents a transfer of economic value to employees—but it does not consume cash in the current period. This creates a wedge between [net income](/income-statement/) and [free cash flow](/free-cash-flow/).

Moreover, if a company is granting large equity packages to retain talent, the dilution to existing shareholders can be substantial. A company that earns $1 billion but grants equity that dilutes shareholders by 5% per year is transferring real wealth to employees and new shareholders at the expense of existing long-term holders.

## See also

<div class="wiki-seealso">

### Closely related

- [Black-Scholes model](/black-scholes-model/) — the standard formula for valuing stock options
- [Earnings per share](/earnings-per-share/) — diluted EPS reflects the assumption of option exercise
- [Share buyback](/share-buyback/) — the typical offsetting transaction companies use to neutralize dilution
- [Free cash flow](/free-cash-flow/) — the metric that reveals actual cash impact despite non-cash equity expense
- [Stock](/stock/) — the underlying security whose fair value drives option valuation

### Wider context

- [Income statement](/income-statement/) — where stock-based compensation expense reduces net income
- [Retained earnings](/retained-earnings/) — the equity account debited for the expense
- Dilution — the economic concept of reduced ownership percentage
- [Volatility smile](/volatility-smile/) — the market reality that implied volatility varies by strike price

</div>
