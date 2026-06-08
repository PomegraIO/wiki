---
title: "How Covered Calls Can Disqualify Dividend Tax Treatment"
description: "Writing a covered call during a dividend's holding period can disqualify the dividend from preferential long-term capital gains treatment and convert it to ordinary income tax rates."
keywords:
  - covered call disqualify qualified dividend
  - covered call dividend qualification rules
  - qualified dividend holding period
  - dividend tax treatment covered call
  - qualified dividend loss of status
image: "/svg/taxes.svg"
---

*Writing a **covered call** during the period when a dividend is being held to qualify for long-term favorable tax treatment can disqualify that dividend, forcing the investor to pay ordinary income tax rates instead of the preferential long-term [capital-gains-tax-investor](/capital-gains-tax-investor/) rate. The IRS treats a covered call as a hedging transaction that breaks the holding period required to claim the dividend as "qualified."*

## Qualified dividend requirements

A **qualified dividend** is eligible for long-term capital gains tax rates (0, 15, or 20 percent, depending on income) if two conditions are met:

1. The stock or fund paying the dividend must be a U.S. corporation or a foreign corporation listed on a U.S. exchange (certain other foreign stocks may qualify).
2. The investor must have held the stock for a minimum holding period—60 days before and after the ex-dividend date (or 90 days for preferred stock).

The holding period rule exists to prevent investors from buying stock just before the dividend is paid and selling immediately after. By requiring ownership for a period surrounding the dividend date, the IRS ensures the investor has genuine equity exposure.

## How a covered call triggers disqualification

When an investor writes a covered call, they grant someone the right to purchase their shares at a specified strike price on or before the expiration date. If the call is in-the-money (the stock price rises above the strike), the buyer will likely exercise the option and the shares will be called away.

The IRS treats a covered call written during the holding period as a constructive sale—a commitment that substantially reduces the investor's risk of loss. Even if the call is not exercised, the act of writing it creates a hedging position that violates the holding period requirement. The Treasury regulations, specifically Treasury Regulation Section 1.246–5, state that a holding period is broken if the investor has written an uncovered call option (in the case of long positions) or held a similar offsetting position while holding the stock.

In practical terms: if you own 100 shares of XYZ Corp and write a covered call on those shares, and those shares then pay a dividend, that dividend cannot be treated as qualified—even if the call expires worthless and is never exercised.

## The 60-day window and its implications

The holding period requirement is 60 days before the ex-dividend date and 60 days after it. If you write a covered call at any point during this 120-day window, the dividend loses qualified status.

Example: XYZ Corp announces a dividend with an ex-dividend date of June 15. You own the shares, but you write a covered call expiring in July on June 1 (14 days before the ex-dividend date). Even though you hold the shares, even though you receive the dividend in full, that dividend is not qualified. You must report it as ordinary income.

If you had written the call after June 15 (after the ex-dividend date), and if the holding period is still satisfied (you owned for 60 days before June 15 and continue to own past June 15), the dividend could still be qualified—*provided* the call was written after the 60-day period or you can demonstrate no call was in effect during the critical window.

## Interaction with other covered call tax rules

Covered calls create other tax complications beyond dividend qualification. If a call is assigned (exercised), the premium received increases your cost basis for the call option and reduces your capital gain or increases your loss on the stock sale. The holding period for the underlying shares rolls into the holding period of the option position.

For qualified dividends, the issue is compounded because the loss of qualified status is automatic, not dependent on whether the call is exercised. The disqualification occurs the moment the call is written during the holding period, not upon exercise.

Some investors write calls after the ex-dividend date and after the 60-day post-dividend holding period to avoid this issue. If you own a stock that pays a dividend in June, you could write a covered call in September or later without affecting the dividend's qualified status.

## Planning strategies to preserve qualified dividend treatment

Investors concerned about dividend qualification should follow these approaches:

**Avoid covered calls during the holding period**: The simplest approach is to refrain from writing covered calls for 60 days before and after the ex-dividend date. If you plan to write calls on a dividend-paying stock, wait until after the 60-day post-dividend period elapses.

**Use protective puts instead**: If you want downside protection while holding dividend-paying shares, a protective put does not trigger the disqualification rule in the same way a covered call does. A put gives you the right to sell; it does not reduce your equity exposure the way a call (which obligates the other party to buy) does. Protective puts are more expensive, but they preserve qualified dividend treatment.

**Track multiple positions**: If you own the same stock in multiple accounts or positions, track the holding periods separately. You might write a call against a position you've held for less than 60 days while preserving qualified status for another position that satisfies the holding period.

**Sell before writing the call**: If the call is in-the-money and likely to be assigned, you might sell the shares before writing the call and avoid both the disqualification issue and the forced sale at the strike price.

## Reporting and compliance

Dividends that are not qualified are reported on your tax return as ordinary dividend income, taxed at your ordinary income tax rate (10 to 37 percent, depending on your bracket). Qualified dividends are reported separately and taxed at preferential rates.

If the IRS audits your return and finds that you reported a dividend as qualified when a covered call was in effect, the dividend will be reclassified as ordinary income, resulting in additional tax plus interest and potential penalties.

Form 1040 requires taxpayers to report qualified dividends separately. Many brokers now automatically flag dividends on shares with written options to alert you to the disqualification, but this is not universal. It is your responsibility as the investor to track the issue.

## Interaction with the holding period for capital gains

It is important to note that a covered call disqualifies the *dividend*, not necessarily the underlying stock position's holding period for long-term capital gains purposes. If you own a stock for more than one year and it pays a dividend while a covered call is in effect, the *dividend* is ordinary income, but if you later sell the stock (assuming the call is not exercised), the gain on the stock itself is a long-term capital gain.

This distinction matters: the loss of qualified dividend status is specific to the dividend and is not a failure of the holding period for the stock itself.

## International considerations

Non-U.S. investors and U.S. investors holding foreign stocks should be aware that dividend qualification is limited to U.S. corporations and specific foreign corporations. Writing a covered call on a foreign dividend-paying stock does not affect qualification in most cases because the dividend may not qualify regardless. However, the regulation applies uniformly, so a covered call written during the holding period will still disqualify a foreign dividend that would otherwise have been qualified.

## See also

<div class="wiki-seealso">

### Closely related

- [Qualified Dividend](/qualified-dividend/) — the tax treatment that covered calls can disqualify
- [Covered Call](/covered-call/) — the option strategy that triggers disqualification
- [Option Premium](/option-premium/) — the income received from writing a call
- [Long-Term Capital Gains Tax](/capital-gains-tax-investor/) — the preferential rate qualified dividends receive
- [Dividend Yield](/dividend-yield/) — the return dividends represent
- [Form 8949 and Schedule D](/form-8949/) — tax forms on which option and dividend transactions are reported

### Wider context

- Options Trading and Taxes — the broader tax framework for option strategies
- [Tax-Loss Harvesting](/tax-loss-harvesting/) — another strategy that interacts with holding periods
- [Marginal Tax Rate](/marginal-tax-rate-investor/) — the tax rate applied to ordinary dividends
- [Cost Basis](/cost-basis/) — adjusted basis calculations affected by option premiums

</div>
