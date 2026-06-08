---
title: "Net Settlement (RSU)"
description: "An automatic withholding mechanism where a portion of vested RSU shares is surrendered to cover employee tax obligations."
keywords:
  - net settlement RSU
  - tax withholding shares
  - net-share settlement
  - rsu withholding
  - equity tax
image: "/svg/equity.svg"
---

*A **net settlement** is the automatic sale or forfeiture of a portion of vested restricted stock units to satisfy federal, state, and employment-tax withholding. When RSUs vest, the employee receives shares but also incurs a tax liability; net settlement simplifies payment by having the company surrender shares directly to the tax authorities or retain them as payment, so the employee receives only the after-tax residue.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Net Settlement (RSU) — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for equity and share ownership." />

<div class="wiki-infobox-caption">A streamlined way to pay taxes on vested equity without needing cash.</div>

|   |   |
|---|---|
| **What it is** | Automatic forfeiture of RSU shares to cover income and FICA withholding taxes |
| **Also called** | Net-share settlement, net-settle withholding, cashless withholding |
| **Triggered** | RSU vesting date |
| **Mechanism** | Company retains shares equal to estimated tax, employee receives net shares |
| **Tax withheld** | Federal, state, local income tax plus payroll taxes (FICA) |
| **Calculation** | Vested shares × share price at vesting × marginal tax rate ≈ shares forfeited |
| **Timing** | Automatic unless employee elects alternative withholding method |

</aside>

## Why net settlement exists

RSU vesting is a taxable event. The moment shares vest and become the employee's unrestricted property, the IRS treats the vest as ordinary income recognition. The taxable amount is the fair market value (FMV) of vested shares on the vesting date, and the tax due is calculated using the employee's marginal federal, state, and FICA rates. A mid-level engineer receiving 100 RSUs worth $200 each faces a $20,000 income tax bill on that single vest date—even if they hold the shares and have no cash to pay.

Without net settlement, the company would need the employee to wire cash to cover withholding, which is administratively messy and often impossible for employees with little disposable income. Net settlement sidesteps this friction: the company automatically designates enough shares to satisfy the tax bill, surrenders those shares, and deposits the proceeds with tax authorities. The employee receives only the net shares, and the withholding obligation is satisfied.

## How the math works

When shares vest on a given date at a known share price, withholding is straightforward algebra. An employee vests 100 RSUs at $200/share = $20,000 of income. If the employee's all-in marginal tax rate (federal + state + FICA) is 40%, the company withholds 40 shares ($8,000) and delivers 60 shares ($12,000) to the employee net of tax. The company immediately sells those 40 shares and remits the $8,000 to the IRS and state tax authority.

In practice, the withholding rate is an estimate. The company often uses a flat corporate withholding rate (often 22% federal for supplemental income, plus state and FICA), which may be higher or lower than the employee's actual marginal rate. If the estimate is too high, the employee can claim an overwithholding refund on their annual return. If too low, they may owe additional tax on the vesting event.

Some companies offer employees a choice of withholding rates—a statutory withholding rate (22% or 37% federal, depending on income) or an estimated rate provided by the employee (who knows their bracket better). This flexibility reduces the likelihood of significant overwithholding.

## Relationship to RSU vesting and tax events

Net settlement is not the only way to satisfy [RSU tax withholding](/rsu-tax-withholding/). An employee can also:

- Pay cash directly to the company or tax authority on the vesting date
- Sell shares on their own (a taxable event in its own right) and wire proceeds
- Borrow against vested shares to pay taxes (rare and typically unavailable)

Most employees with illiquid employer stock choose net settlement because it's automatic, requires no cash on hand, and is the path of least resistance. For employees at public companies, selling shares is an alternative, especially if they believe the share price will rise and prefer to maximise holdings. But for private-company employees with illiquid stock, net settlement is the only practical option.

This creates a subtle distinction: RSU tax withholding is the *obligation*; net settlement is the *mechanism* to satisfy it. Not all withholding uses net settlement—cash payment or employee-directed sale also satisfies the obligation. But net settlement is by far the most common mechanism.

## The alternative: employee-directed withholding

Some employees, particularly those at companies with liquid equity, exercise an alternative withholding method. Rather than let the company choose which shares to forfeit, they direct the company to withhold cash (from salary or bonus) or allow them to sell a portion of vested shares on the open market. This is technically a choice, but it requires the employee to have cash or liquidity, which most don't at the moment of vesting.

A related mechanism is [broker-assisted cashless exercise](/iso/) for options, where a broker facilitates exercise and immediate sale in one transaction, with the broker depositing shares sold and taking the exercise cost and taxes from proceeds. RSUs don't require a broker—net settlement is built into the company's stock plan—but the principle is the same: minimise friction and cash requirement.

## State and international complications

Net settlement becomes more complex with state and local tax considerations. California, New York, and other high-tax states impose combined income-tax rates above 13%, and they also require withholding on vesting. A California resident vesting RSUs at a Bay Area startup can face federal (24–37%), FICA (15.3%), and state (9.3–13.3%) withholding totalling 48–65% of the grant value.

Some companies calculate net settlement using an all-in rate; others separate federal, state, and FICA withholding into distinct tranches. This can result in over- or underwithholding if the employee's mix of taxes is unusual (e.g., someone subject to the Net Investment Income Tax, or living in two states during a tax year).

International employees face even more variation. Some countries (UK, Canada) use net settlement on RSU vesting much like the US. Others (Germany, Switzerland) have different tax timing (tax at grant, not vesting) and don't use net settlement at all. An employee relocating mid-year may face a mismatch between the company's withholding methodology and their actual tax jurisdiction.

## The withholding certificate and tax reporting

The company's withholding on net settlement is reported on the employee's W-2 as income and federal/state/FICA withholding. The number of shares forfeited and the share price at vesting determine the income reported; the shares retained and their [cost basis](/cost-basis/) are what the employee owns post-vesting. This cost basis is usually the FMV at vesting, which is the same amount reported as income, so there is no additional gain or loss until the employee eventually sells.

If net settlement results in overwithholding, the employee claims a refund on their tax return. If underwithholding, they owe additional tax (or the amount is caught in a quarterly estimated-tax payment). The company's withholding certificate should reconcile the number of shares, the FMV at vesting, and the withholding amount.

## Interaction with alternative trading systems and secondary sales

Employees at private companies often cannot simply sell vested shares on an exchange, so net settlement is the primary source of liquidity. The company sells the forfeited shares to satisfy withholding, and the proceeds flow to tax authorities. The employee retains shares that remain illiquid until acquisition, [IPO](/initial-public-offering/), or a [secondary market](/secondary-market/) transaction.

Employees at public companies have an additional option: sell shares themselves after vesting (subject to [Rule 10b5-1](/form-8949/) trading plans and blackout periods) and pay taxes from proceeds. This gives them control over timing and price realization, useful if they believe the stock will appreciate or if they want to diversify.

## See also

<div class="wiki-seealso">

### Closely related

- [RSU Tax Withholding](/rsu-tax-withholding/) — The income-tax event triggered when restricted stock units vest
- RSU — Restricted stock units, the underlying security subject to withholding
- [Cost Basis](/cost-basis/) — The purchase or grant price used to calculate capital gains on future sale
- [Repurchase Right](/repurchase-right/) — Company's option to buy back vested shares from departing employees
- [Vesting Schedule](/vesting-schedule/) — The multi-year schedule determining when RSUs become fully owned

### Wider context

- [Marginal Tax Rate (Investor)](/marginal-tax-rate-investor/) — The top rate applied to additional income, used to estimate RSU withholding
- [Schedule D](/schedule-d/) — Tax form reporting capital gains and losses from equity sales
- [Long-Term Capital Gains Tax](/long-term-capital-gain-tax/) — Preferential rates on gains from shares held over a year
- [Qualified Dividend](/qualified-dividend/) — Dividend income taxed at capital-gains rates rather than ordinary rates
- [ISO](/iso/) — Incentive stock options, an alternative equity grant with different tax withholding mechanics

</div>
