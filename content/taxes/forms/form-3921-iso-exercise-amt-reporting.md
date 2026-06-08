---
title: "Form 3921: Incentive Stock Option Exercise and AMT Reporting"
description: "Form 3921 reports the incentive stock option spread at exercise, which creates an AMT preference item. Understand how the spread affects Form 6251 and when AMT is triggered."
keywords:
  - form 3921
  - iso exercise amt reporting
  - incentive stock option
  - amt preference item
  - stock option exercise
---

*When you exercise an **incentive stock option** (ISO), your company issues **Form 3921** documenting the grant date, exercise date, and fair market value. That last piece—the gap between your [strike price](/strike-price/) and the FMV at exercise—becomes an AMT preference item on [Form 6251](/form-6251-amt-exemption-phase-out/). Understanding Form 3921 and how it flows into AMT is essential for tech and biotech workers with large option grants.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Form 3921 ISO Exercise — key facts</div>

<img src="/svg/taxes.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The fair market value spread at exercise is not ordinary income but does trigger AMT preference treatment.</div>

|   |   |
|---|---|
| **What it is** | IRS form issued by employer; reports ISO grant and exercise details |
| **Key fields** | Grant date, exercise date, grant price, FMV at exercise, shares exercised |
| **AMT trigger** | FMV at exercise minus grant price creates preference item |
| **Where it flows** | Line 12d of Form 6251 (ISO adjustment) |
| **Ordinary income** | Zero (unlike non-qualified stock options) |
| **Long-term capital gains potential** | Yes, if you meet 1-year post-exercise and 2-year post-grant holding periods |

</aside>

## What Form 3921 reports

When you exercise an ISO, the company that issued the grant must provide Form 3921 to you and file a copy with the IRS. The form captures:

- **Grant date** and the original grant price (strike price)
- **Exercise date** and the number of shares exercised
- **Fair market value (FMV)** of the company's stock on the exercise date
- The name, address, and employer ID of the company

From these fields, you can calculate the **spread**: FMV at exercise minus the grant (strike) price. This spread is the economic gain you capture by exercising. For example, if you exercise 1,000 shares granted at $10 per share when the stock trades at $50, the spread is $40 per share, or $40,000 total.

## The critical distinction: no ordinary income at exercise

This is where ISOs differ sharply from non-qualified stock options. With a non-qualified option, the $40,000 spread is ordinary income. It hits your W-2 or 1099, increases your AGI, and is subject to regular income tax rates.

With an ISO, the $40,000 spread is **not** ordinary income at exercise. It doesn't appear on your W-2 or any 1099. To a standard income-tax calculation, the exercise is invisible.

But to the **alternative minimum tax** system, it's not invisible. The spread is treated as a preference item—an item that swells Alternative Minimum Taxable Income (AMTI) without appearing as ordinary income. This preference item can trigger [AMT](/form-6251-amt-exemption-phase-out/) liability.

## The AMT preference item: Form 6251, line 12d

When you complete [Form 6251](/form-6251-amt-exemption-phase-out/) to calculate whether you owe AMT, line 12d asks for "Incentive stock options (excess of FMV over exercise price on date of exercise)." This is where the Form 3921 spread lands.

If you exercised 1,000 ISO shares at $10 when the stock was $50, you enter $40,000 on line 12d. That $40,000 is added to your AMTI; it doesn't reduce your AMT base the way a tax deduction would.

The AMT preference item is permanent until you sell the stock. If you hold the shares and the stock rises to $70, the unrealized gain is not an additional preference item. Only the original spread at exercise counts. But if the stock falls to $30 at the time of sale, you've crystallized a loss; your [cost basis](/cost-basis/) for ordinary income purposes is $10 per share, so you'd report a $20 per share capital loss. For AMT purposes, your basis is also $10, so the same loss applies. But for the year of exercise, the $40,000 preference item stood, potentially triggering AMT, even though you later lost money.

## When AMT is triggered: the threshold

AMT becomes due when AMTI exceeds the [AMT exemption](/form-6251-amt-exemption-phase-out/). For 2024, the exemption is $85,250 for married filing jointly and $56,550 for single filers. Above those thresholds, the exemption is phased out at 25 cents per dollar of excess income.

A high-earning employee exercising a large ISO grant can easily reach AMT. Suppose you earn $300,000 in salary and bonus, and you exercise an ISO with a $100,000 spread. Your AMTI is roughly $400,000 (simplified; includes other adjustments). Your exemption is phased out and may be nearly exhausted. At the 26% (or 28%) AMT tax rate, you could owe tens of thousands of dollars in AMT, even though no ordinary income tax was due on the exercise itself.

## The holding periods: ordinary income deferral and long-term capital gain

The real tax advantage of ISOs emerges if you satisfy two holding periods:

1. **At least 2 years from the grant date**
2. **At least 1 year from the exercise date**

If you meet both, any gain on the sale of the shares is treated as a long-term capital gain, eligible for the preferential 15% or 20% rates.

But there's a twist when you sell within these holding periods—or in the year of exercise.

**If you sell before the 1-year post-exercise period:** The sale is **disqualifying**. You lose the ISO preferential treatment. The spread ($40,000 in our example) becomes ordinary income in the year of sale, even though Form 3921 was issued in the exercise year. This is called **disqualifying disposition**. You report the spread as ordinary income and claim the benefit of the lower [cost basis](/cost-basis/) for capital gains purposes. The net effect: ordinary income on the spread, plus long-term or short-term capital gain/loss on the appreciation above the spread.

**If you hold past the 1-year post-exercise and 2-year post-grant period:** The entire gain (from grant price to sale price) is treated as a long-term capital gain. No ordinary income. No AMT adjustment on the sale. The original $40,000 spread, which was a preference item in the exercise year, becomes embedded in the long-term capital gain tax treatment on the sale year.

Example:
- Grant: 1,000 shares at $10 on Jan 1, 2024
- Exercise: $50 on Jan 1, 2025
- Sale: $70 on Jan 2, 2026

Assuming you hold past both dates, your sale in Jan 2026 is a long-term capital gain of $60,000 ($70 sale price minus $10 grant price). You pay long-term capital gains tax on the full $60,000. No ordinary income. No AMT adjustment for the sale itself.

But in 2025, when you exercised, you had a $40,000 AMT preference item. That year, you may have owed AMT. However, when you file a later return (if eligible), you can claim an **AMT credit** for the AMT paid on the original spread, to the extent that your future ordinary income-tax liability exceeds your AMT liability in a later year.

## Form 3921 and AMT calculations in parallel

Many ISO-holding employees find themselves calculating tax two ways:

1. **Regular income tax:** Based on W-2 income, deductions, and capital gains/losses. Often results in a low or zero tax after deductions.
2. **AMT:** Based on AMTI, which includes the ISO preference item. Often results in a substantial tax.

You pay whichever is higher. In years with large ISO exercises, AMT usually wins.

Form 3921 is the starting point. The FMV spread on Form 3921 is the number you carry forward to Form 6251 to calculate AMT. If you're unsure of the FMV on the exercise date, the Form 3921 value is dispositive—it's what the company reported to the IRS.

## Planning and documentation

Employees with vesting schedules involving multiple exercises need to track each grant and exercise separately. A single Form 3921 covers one grant, so if you've received multiple ISO grants over the years, you'll receive multiple Form 3921s, one for each exercise.

For AMT planning, accumulating a multi-year record of exercises helps you foresee AMT liability. If you're vesting into an exercise every quarter, and each exercise is a $50,000 spread, you'll likely hit AMT every year you're exercising, plus for a few years after if your ordinary income is stable or rising.

Some employees spread exercises over multiple years to smooth AMTI and avoid clustered AMT bills. Others exercise in years when their ordinary income is expected to be low, to keep total AMTI closer to the AMT exemption threshold. Tax planning with Form 3921 in hand can save tens of thousands of dollars.

## See also

<div class="wiki-seealso">

### Closely related

- [Form 6251: AMT Exemption Phase-Out for High-Income Investors](/form-6251-amt-exemption-phase-out/) — where the ISO spread triggers AMT liability
- [Schedule D: Wash Sale Adjustment Reporting](/schedule-d-wash-sale-adjustment-reporting/) — related capital gain and loss tracking
- [Form 709: Annual Gift Tax Exclusion Reporting](/form-709-annual-gift-tax-exclusion-reporting/) — another high-income reporting requirement
- [Cost Basis](/cost-basis/) — basis is the grant price for ISOs meeting holding periods
- [Strike Price](/strike-price/) — the exercise price specified in the ISO grant

### Wider context

- Long-Term Capital Gains Tax for Investors — the preferential rates achievable with ISOs if holding periods are met
- [Capital Gains Tax](/capital-gains-tax-investor/) — how gains on exercised ISOs are taxed at sale
- [Stock](/stock/) — the underlying security issued as an ISO
- [Alternative Trading System](/alternative-trading-system/) — where employee stock from exercises may be traded

</div>
