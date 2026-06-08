---
title: "Grant-to-Vesting Gap"
description: "The lag between when equity is approved and when it actually vests, creating tax and valuation uncertainty."
keywords:
  - equity vesting
  - grant date
  - vesting schedule
  - tax treatment
  - time value
image: "/svg/equity.svg"
---

*The **grant-to-vesting gap** is the calendar period between the date equity is formally awarded to an employee and the date that equity begins to vest (typically four years later for common stock grants). This delay creates both real economic consequences and hidden tax complications: the value of the award is locked in at grant-date prices, volatility accumulates over years, and the tax treatment depends on complex rules that treat the grant date and exercise date as separate taxable moments.*

## Why the gap exists

When a company awards equity—whether as a stock option, restricted stock unit (RSU), or restricted stock grant—the grant date is the moment the award is formally documented and approved by the board or compensation committee. For tax purposes, the grant date is often the clock-starting event for [alternative minimum tax (AMT)](/alternative-minimum-tax/) calculations and for determining whether the grant qualifies under certain tax statutes.

Vesting, however, almost never starts immediately. Most equity grants use a four-year vesting schedule with monthly or quarterly increments, with or without a one-year cliff (a period during which no shares vest at all). This gap—one to four years between grant and the start of vesting—is deliberate: it's meant to bind employees to the company and create incentive alignment over time.

During the gap, the shares or options are worthless to the employee in a practical sense. You cannot sell them, exercise them, or convert them to cash. If you leave the company before vesting begins, you forfeit the grant entirely. This creates genuine economic uncertainty: you have a right that may or may not pay off, depending on your continued employment.

## The valuation trap

The grant-to-vesting gap creates a tax and financial reporting problem: what is the fair value of an award that cannot vest for four years?

For non-qualified stock options, [ASC 718](/equity-compensation-expense/) (the accounting standard that governs stock-based compensation) requires companies to estimate the option's value on the grant date using models like Black-Scholes. That value is then recognised as an expense over the vesting period. If you're granted a four-year vesting option on January 1st worth $50 (per Black-Scholes), the company expenses $12.50 per year, regardless of whether the stock rises or falls.

This creates a misalignment. If the stock rises 50% during the grant-to-vesting gap, the true economic value of your option is much higher than the grant-date estimate—but you don't benefit from the additional appreciation when you eventually exercise. You still have the same number of shares, but the company's [equity-compensation expense](/equity-compensation-expense/) was calculated years ago and is now understated relative to the real value you received.

Conversely, if the stock falls, your grant-date valuation was too optimistic, but the company has already expensed it. From an earnings quality perspective, the expense does not track economic reality.

For RSUs, the problem is different but equally real. RSUs are typically settled in stock on the vesting date, at whatever the stock price is on that day. But for ASC 718 purposes, the expense is recorded based on the grant-date fair value. If the stock triples between grant and vesting, you receive a windfall gain, and the company's expense was calculated at a much lower stock price. The opposite is true if the stock crashes.

## Tax timing complications

The grant-to-vesting gap also creates tax timing friction, especially for ISOs.

For an ISO, the two-year and one-year holding-period clocks start on different dates: the two-year clock starts on the grant date, the one-year clock starts on the exercise date. This means that if you're granted an ISO and want to satisfy the [qualifying disposition](/disqualifying-disposition/) test, you must hold the shares for one year after exercise AND two years after grant—whichever extends further.

If you're granted an option on January 1, 2024, it vests on January 1, 2025, and you exercise immediately, the one-year clock starts January 1, 2025. You can sell after January 1, 2026. But the two-year clock started January 1, 2024, so you can sell after January 1, 2026 anyway. In this case, the dates align.

But if you wait to exercise, the dates diverge. If you exercise on June 1, 2025, you need to hold until June 1, 2026 (one year), but the two-year grant-date window requires holding until January 1, 2026. The two-year rule is now binding. The longer you delay exercising, the more the one-year clock lags the two-year clock.

## The cliff risk

Many equity grants include a one-year cliff, meaning no shares vest until you've been employed for one year. During that cliff period—year one of the grant-to-vesting gap—you have zero vested equity. If you leave on day 365, you lose the entire grant. If you stay one day into year two, you usually vest 25% of the grant (assuming four-year vesting).

The cliff creates a real forfeiture risk that is not fully captured in the grant-date valuation. An employee who leaves at month 11 loses everything; an employee who stays to month 13 gets 25%. This binary outcome is front-loaded risk, and from a time-value perspective, it's asymmetric: the company can retain you cheaply during the cliff (because the cost of leaving is total forfeiture), but the moment you pass the cliff, the incentive is weaker.

## Refresh cycles and stacking

Large tech and finance companies mitigate the grant-to-vesting gap by issuing new grants every year or every two years (a practice called "refresh"). If you receive a new grant each year, your equity pipeline is continuously refreshed, and you always have recently granted options with high perceived value, plus older options nearing full vesting.

Without refreshes, a four-year vesting schedule means that for the first four years, employees are accumulating vested equity; after four years, the vesting profile flattens unless new grants arrive. This creates a retention cliff: employees often leave after their initial grants fully vest and before new grants arrive.

Refresh cycles are common in competitive markets, effectively shortening the perceived grant-to-vesting gap by resetting the clock every few years. However, they also increase total dilution and expense to the company.

## Negotiating around the gap

In startup recruiting, the grant-to-vesting gap is a critical negotiation point. An employee offered a four-year vesting grant has no immediate liquidity and faces forfeiture risk if they leave. Early-stage companies sometimes offer an accelerated vesting schedule (two-year vesting instead of four) or a larger grant amount to compensate for the gap.

Some companies accelerate vesting upon [change of control](/merger/) or fundraising events, reducing the gap risk. Others grant options with a double-trigger: vesting accelerates only if the company is acquired AND the employee is terminated without cause. This softens the impact of the gap during the exit scenario.

Understanding the grant-to-vesting gap is essential when evaluating a job offer. A $200,000 equity grant spread over four years is not the same as a $200,000 cash bonus: the present value depends on your assessment of the company's success and your own retention.

## See also

<div class="wiki-seealso">

### Closely related

- [Equity compensation expense](/equity-compensation-expense/) — how companies record option and RSU costs
- ISO stock option — options with tax incentives and holding-period rules
- [Disqualifying disposition](/disqualifying-disposition/) — sale that fails holding-period test
- [Vesting schedule](/vesting-schedule/) — the time-based release of equity
- [Change of control](/merger/) — triggering event for accelerated vesting

### Wider context

- Employee stock compensation — broader equity compensation landscape
- [Alternative minimum tax](/alternative-minimum-tax/) — applies to ISOs and affects tax planning
- [Fair value measurement](/fair-value/) — how valuations are set on grant date

</div>
