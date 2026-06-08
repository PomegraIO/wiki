---
title: "RSU Tax Withholding"
description: "The mandatory income-tax collection that occurs when restricted stock units vest, treating the grant value as ordinary income."
keywords:
  - rsu tax withholding
  - rsu vesting tax
  - restricted stock units taxation
  - employment tax withholding
  - equity income tax
image: "/svg/equity.svg"
---

*RSU **tax withholding** is the automatic income-tax collection that occurs on the vesting date of restricted stock units. The moment RSUs vest, they convert from restricted to freely tradeable shares, and the IRS recognises that as a taxable event. The employee must pay federal, state, and payroll taxes on the fair market value of vested shares, calculated using their marginal tax rate; the company withholds shares or cash to satisfy this obligation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">RSU Tax Withholding — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for equity and share ownership." />

<div class="wiki-infobox-caption">When RSUs vest, income tax is owed immediately, even if you hold the shares.</div>

|   |   |
|---|---|
| **What it is** | Federal, state, and FICA tax on RSU vesting date fair market value |
| **Timing** | At each vesting event (usually quarterly or annually) |
| **Tax character** | Ordinary income (not capital gains) |
| **Taxable amount** | FMV of vested shares on vesting date |
| **Withholding mechanism** | [Net settlement](/net-settlement-rsu/) (forfeited shares), cash payment, or broker-assisted sale |
| **Marginal rate applied** | Employee's combined federal + state + FICA rate (often 40–65% at tech companies) |
| **W-2 reporting** | Reported as wages + federal/state/FICA withholding |

</aside>

## Why vesting triggers tax

The IRS treats RSU vesting as compensation income. When a company grants RSUs, they are forfeited if the employee leaves before vesting. Upon vesting, they become the employee's unrestricted property, which the IRS considers equivalent to receiving a bonus or salary payment. The employee has not purchased the shares—they received them as consideration for services—so vesting is a taxable income event, not a capital gain.

The taxable amount is the fair market value (FMV) of vested shares on the vesting date. If an engineer vests 100 RSUs on a day when the company's stock trades at $200, the taxable income is $20,000, and taxes are due immediately, even if the engineer never sells the shares. This is distinct from [options](/option/) or [ISO](/iso/), where the taxable event may be deferred to exercise date or sale date; RSUs trigger tax at vesting.

This creates a timing mismatch. The employee has a tax liability but may not have cash if the stock is illiquid. A private-company employee with unvested RSUs worth millions on paper faces a multi-million-dollar tax bill on a vesting date, with no ability to sell shares and raise cash. This friction is why [net settlement](/net-settlement-rsu/) exists—to allow companies to withhold shares directly and remit taxes without requiring the employee to find cash.

## Withholding rates and calculations

The amount withheld depends on the employee's marginal tax rate. In the United States, this includes:

- **Federal income tax** (22–37% marginal, depending on income)
- **State and local income tax** (0–13.3% depending on jurisdiction; California, New York, and others levy 10%+)
- **FICA payroll tax** (7.65% for employee, 6.2% Social Security + 1.45% Medicare, capped at Social Security wage base of ~$168K)
- **Medicare surtax** (0.9% additional Medicare tax on wages above ~$200K)

A Bay Area tech-company employee earning $200K in salary plus vesting RSUs faces a combined marginal rate of roughly 50–55% (37% federal + 13.3% California + 7.65% FICA - some federal/state overlap). Some companies withhold at a flat statutory rate (22% federal, 10% state, 7.65% FICA ≈ 40%) and let overwithholding or underwithholding reconcile at tax-return time.

Net Settlement calculates the number of shares forfeited as follows:

**Shares Withheld = Vested Shares × Estimated Tax Rate**

If 100 shares vest at $200/share and the withholding rate is 40%, the company retains 40 shares (= $8,000 at current price) and delivers 60 shares to the employee. The company sells those 40 shares and remits $8,000 to tax authorities.

The withholding rate may differ from the employee's true marginal rate, resulting in over- or underwithholding. If the company withholds at 40% but the employee's true rate is 35%, the employee overwitheld and claims a refund. If the true rate is 50%, the employee owes additional tax.

## Withholding vs. the actual tax bill

It's critical to distinguish between **withholding** (cash or shares remitted to tax authorities at vesting) and **actual tax owed** (determined on the annual tax return). Withholding is the employer's best estimate; actual tax owed may differ based on the employee's full-year income and deductions.

An employee might receive RSU grants in multiple tranches over a year, with withholding calculated independently on each vesting date. If the employee changes jobs mid-year, works two jobs, or has other income, their total-year tax bracket differs from the bracket at each individual vesting date. The company's withholding might be too high or too low.

At tax-return time, the employee reports RSU vesting as ordinary income (on W-2 forms, or as part of self-employment income), reports the withholding that occurred, and calculates whether additional tax is due or a refund is owed. If the stock price drops after vesting, the employee still owed tax on the higher FMV at vesting date, creating a loss-harvesting opportunity if shares are sold below that amount.

## State tax complications

State tax withholding adds significant complexity. Some states (California, New York, Delaware) impose withholding on vesting. Some employees work in a state where they don't live, creating questions about which state's tax should be withheld. An employee who vests RSUs while working in California but later moves to Texas and sells shares has California withholding at vest, plus capital-gains taxes at the federal level when sold.

New York requires withholding on RSU vesting at the top state rate (~10.9%) for nonresidents, creating overwithholding for out-of-state employees who should owe little or no state tax. Delaware and some other low-tax jurisdictions may not require withholding, yet employees still owe tax where they actually reside. This multi-jurisdiction mess often requires amended state returns or careful tracking of credits.

## Interaction with capital gains and holding periods

Withholding on RSU vesting is separate from capital gains tax on sale. The vesting is ordinary income withholding; the subsequent sale is a capital-gains event (short-term or [long-term](/long-term-capital-gain-tax/), depending on holding period). The cost basis of the vested shares is typically the FMV at vesting (the amount withheld against), so the capital gain or loss is calculated from that basis.

Example: An employee vests 100 RSUs at $200/share on 1 June. The company withholds 40 shares and delivers 60 shares. Cost basis for those 60 shares is $200/share. If the employee sells them on 1 July at $210/share, the capital gain is $10/share × 60 = $600 (short-term). The tax bill is ordinary income tax on the $12,000 vesting value (after withholding was applied) plus short-term capital-gains tax on the $600 appreciation.

The ordinary income is locked in at vesting; the capital gain is determined at sale. If the employee never sells, there is no capital-gains tax, but the ordinary income tax (withholding) remains due. Many private-company employees hold RSUs long after vesting in hopes of appreciation or acquisition, paying the ordinary-income tax on vesting but deferring the capital-gains tax to acquisition or IPO.

## Private vs. public company differences

At public companies, withholding and subsequent sale are often immediate or happen within days. Employees can sell shares easily, and the company's net-settlement calculation is accurate because the share price is known.

At private companies, withholding is enforced, but the share price may be opaque or illiquid. A startup might value stock at $10/share for option-grant purposes but withhold at that same price even though secondary-market trading (if it exists) suggests $15 or $25/share. Employees may pay ordinary-income withholding at $10/share, only to discover their true income was higher. Alternatively, if the share price is later reduced (down round, bridge financing), the withholding may have been excessive relative to true value.

## Relationship to performance shares and other equity vehicles

RSUs are subject to mandatory withholding on vesting. Some companies offer performance shares or performance stock units (PSUs), which have an additional performance gate before vesting. The withholding timing is still the vesting date—when the PSU becomes an RSU or share outright. The calculation remains the same: FMV at vesting times marginal tax rate.

Non-qualified [stock options](/option/) trigger withholding at exercise (if the company is subject to OASDI Social Security tax caps and other specifics). [ISO](/iso/) defer withholding until sale but have different tax-withholding mechanics. Restricted stock (shares granted outright, not units) may have withholding at grant or at cliff vesting, depending on the plan and whether a Section 83(b) election was made.

## See also

<div class="wiki-seealso">

### Closely related

- RSU — Restricted stock units, the underlying equity grant subject to withholding
- [Net Settlement (RSU)](/net-settlement-rsu/) — The mechanism by which vested shares are forfeited to satisfy withholding taxes
- [ISO](/iso/) — Incentive stock options, which defer tax withholding until exercise or sale
- [Vesting Schedule](/vesting-schedule/) — The multi-year schedule determining when RSUs vest and withholding occurs
- [Cost Basis](/cost-basis/) — The FMV at vesting, used to calculate capital gains at sale
- [Repurchase Right](/repurchase-right/) — Company option to buy back vested shares; interacts with withholding obligations

### Wider context

- [Marginal Tax Rate (Investor)](/marginal-tax-rate-investor/) — The top tax rate applied to incremental income, used for withholding estimates
- [Long-Term Capital Gains Tax](/long-term-capital-gain-tax/) — Preferential tax rates on gains from shares held over one year
- [Schedule D](/schedule-d/) — Tax form for reporting capital gains and losses from equity sales
- [Qualified Dividend](/qualified-dividend/) — Dividend income taxed at capital-gains rates, relevant post-vesting
- [Earnings Per Share](/earnings-per-share/) — EPS impact when shares are withheld for taxes and not issued to employees

</div>
