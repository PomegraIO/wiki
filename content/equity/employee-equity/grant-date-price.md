---
title: "Grant Date Price"
description: "The fair market value of a company's stock on the date an equity award is issued to an employee, which determines the tax basis and exercise price for that grant."
---

*The grant date price is the anchor point for all subsequent equity math—exercise prices, tax liability, and profit or loss all flow from this single number set on day one. Get it wrong and you've corrupted the tax treatment of a multi-year compensation package.*

<div class="wiki-hatnote">This is distinct from the exercise price of an <a href="/wiki/employee-stock-options/">option</a>, though the two are often identical.</div>

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Grant date price — key facts</div>
  <table>
    <tr><th>Definition</th><td>Fair market value on day of grant</td></tr>
    <tr><th>Sets</th><td>Option exercise price, RSU tax basis</td></tr>
    <tr><th>For public companies</th><td>Official closing price that day</td></tr>
    <tr><th>For private companies</th><td>Board-approved valuation</td></tr>
  </table>
</aside>

## How grant date price works in practice

When your company grants you 1,000 [restricted stock units](/wiki/restricted-stock-units/) on January 15, the stock price that day (say, $50) becomes your grant date price. Over the next four years, as those units [vest](/wiki/vesting-schedule/), the grant date price remains fixed at $50. If the stock rises to $200 by the time your shares vest, you owe income tax on a $150-per-share gain. If it falls to $30, you owe tax on a $20-per-share loss (though this only matters for tax-loss harvesting purposes—you still keep the grant).

For [employee stock options](/wiki/employee-stock-options/), the grant date price becomes the strike price. An option granted at $50 remains a $50 option for its entire 10-year term. You can only exercise it at $50, no matter whether the stock rises to $500 or collapses to $5.

## Public vs. private: how the price is determined

**Public companies** have it easy. The grant date price is the official closing price on the grant date—look at Yahoo Finance or any brokerage. No judgment, no discretion. The IRS accepts this as binding fair market value.

**Private companies** operate in a gray zone. Without a public market, the board must approve a fair market value, usually by one of these methods:

- **409A valuation**: A third-party appraiser (often a Big Four accounting firm) values the company using market multiples, comparable transactions, or discounted cash flow. This is the gold standard for tax compliance—if challenged, the IRS defers to 409A opinions. Costs $5k–$50k per valuation, done annually or after major financing rounds.
- **Board determination**: The board votes on the value, typically informed by recent funding rounds. If a Series C just valued the company at $500M per share, the board grants equity at that price. Riskier than 409A, but faster and cheaper.
- **Safe harbor pricing**: Using the price from a recent qualified financing round (within 120 days of the grant date) is considered presumptively fair. The most common route for venture-backed startups.

If the board grants options at $10 per share but a 409A valuation later finds the company is actually worth $50 per share, you've got a problem: the options are now heavily discounted and may trigger adverse tax treatment (see "409A violations" below).

## The 409A nightmare

A 409A violation is the grant date price's biggest gotcha. The rule, from Section 409A of the tax code, says that equity awards must be granted at fair market value. If you later discover that the grant date price was too low—typically because a new financing round or acquisition proves the company was worth more—the IRS can reclassify the award as a gross "transfer of property" with immediate tax consequences.

In practice: your startup granted options at $1 per share in 2020. In 2024, the company raises a Series D at $20 per share. The 409A valuation finds the company was worth $15 per share on the grant date. You now owe back taxes (and penalties) as if you'd already exercised those options years ago, even though they haven't vested. This can be tens of thousands of dollars.

To avoid this, private companies either commission frequent 409A valuations (often after each funding round) or use safe-harbor pricing tied to recent financings. The small cost of annual 409A updates is insurance against a six-figure reckoning.

## Tax treatment at vesting

When your [restricted stock units](/wiki/restricted-stock-units/) vest, the difference between the grant date price and the current stock price is ordinary income. If you received 1,000 RSUs at $50 grant price and they vest when the stock is $75, you owe ordinary income tax on $25,000. This is reported on your W-2 or as a supplemental 1099, depending on your structure.

For [employee stock options](/wiki/employee-stock-options/), the grant date price is fixed forever as the strike. When you exercise, the spread between strike and exercise price is either ordinary income ([non-qualified options](/wiki/nqso/)) or taxable gain ([ISOs](/wiki/iso/)).

## Grant date price and [cost basis](/wiki/cost-basis/)

If the company later distributes the vested shares to you, your cost basis for capital gains purposes is the grant date price plus the ordinary income you paid at vesting. Hold the shares for more than a year, and future appreciation is taxed as long-term capital gain (15–20% federal rate, vs. ordinary income at 37%). This is why equity compensation is so valuable: ordinary-income taxation at vesting, then long-term capital gains on the growth.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/restricted-stock-units/">Restricted stock units</a> — RSUs are taxed based on grant date price at vesting.</li>
  <li><a href="/wiki/employee-stock-options/">Employee stock options</a> — options use grant date price as the strike.</li>
  <li><a href="/wiki/cost-basis/">Cost basis</a> — grant date price is a component of cost basis for capital gains.</li>
  <li><a href="/wiki/iso/">ISO</a> — ISOs have special tax rules but still use grant date price as strike.</li>
  <li><a href="/wiki/nqso/">NQSO</a> — non-qualified options use grant date price as the exercise price.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/vesting-schedule/">Vesting schedule</a> — when shares vest relative to grant date.</li>
  <li><a href="/wiki/409a-valuation/">409A valuation</a> — third-party appraisal protecting against tax reclassification.</li>
</ul>
</div>
