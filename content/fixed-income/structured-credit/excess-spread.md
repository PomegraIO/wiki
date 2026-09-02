---
title: "Excess Spread"
description: "The difference between the interest rate earned on securitized collateral and the sum of rates paid to bondholders and servicing fees, flowing to the originator or equity holder."
---

*Excess spread is the profit margin built into a securitization. If mortgages in a pool yield 4% and bondholders are paid an average of 2.5%, the initial excess spread is 1.5%. This cash flow goes to the originator (or is retained by a hedge fund that bought the equity). If defaults consume excess spread faster than forecast, the cushion against losses shrinks, and junior tranches suffer. Excess spread is both the reward for risk-taking and a measure of buffer available to absorb credit deterioration.*

## The components of excess spread

Excess spread is calculated monthly:

**Collateral yield**: Total interest collected from borrowers (4%)
**Less:**
- Bondholder interest (2.5%)
- Servicing fee (0.25%)
- Trustee fees (0.05%)

**Equals excess spread: 1.2%**

This 1.2% is available for:
- Originator/equity holder profit
- Building reserve accounts
- Maintaining overcollateralization
- Absorbing losses

In a stable pool with low defaults, excess spread flows to the equity holder as profit. In a stressed pool, excess spread is consumed by delinquencies and defaults.

## The income statement of a securitization

A securitization's monthly "income statement" looks like:

**Collections**
- Principal collections: $800,000
- Interest collections: $1,200,000

**Disbursements**
- Bondholder principal: $700,000
- Bondholder interest: $2,500,000
- Servicing fee: $250,000
- Trustee fees: $50,000

**Cash available for equity**: ($1,200,000 - $2,500,000 - $250,000 - $50,000) = -$1,600,000

In this example, there is negative excess spread—collateral income is insufficient to cover all obligations. The shortfall comes from principal repayment (principal collections exceed principal payments). But if defaults are high, this becomes untenable.

## Excess spread triggers and maintenance

Many securitizations include excess spread triggers and maintenance covenants:

**Target OC covenant**: If overcollateralization falls below a target, excess spread is diverted to retire senior bonds, rebuilding OC.

**Reserve account funding**: Excess spread is allocated to fund and maintain reserve accounts.

**Subordination targets**: If subordination falls below levels needed for ratings, excess spread is retained.

These covenants mean that in a healthy pool, excess spread flows to equity. In a stressed pool, it is diverted to protect senior investors.

## Excess spread as loss absorption

The fundamental point: excess spread absorbs losses. Consider a pool with:

- Collateral yield: 4%
- Average bondholder cost: 2.5%
- Servicing and fees: 0.25%
- **Excess spread: 1.25% annually**

If the pool is $100 million, excess spread is $1.25 million per year. If annual losses are $500,000, excess spread covers them with $750,000 left over. If losses hit $1.5 million, excess spread is consumed and equity takes losses.

An equity holder is implicitly short a volatility option: excess spread is capped at forecast levels (1.25%) but losses can be unlimited. That is why equity is high-risk/high-return. In a good pool, it generates 8–12% returns. In a bad pool, it is wiped out.

## Excess spread and structuring decisions

When a securitization is structured, the amount of excess spread (and how it is allocated) is a key negotiation:

- **Aggressive structure**: Target high excess spread (tight bond pricing, higher coupons), maximizing equity return potential but providing minimal loss cushion.
- **Conservative structure**: Target lower excess spread, leaving more cushion via higher bond prices (lower coupons) and larger reserve accounts.

An originator might push for aggressive structuring to maximize the equity's value (which it will sell). Investors might push for conservative to maximize safety. The deal's terms reflect this tradeoff.

## Excess spread allocation and waterfall

The waterfall specifies excess spread allocation:

Priority 1: Delinquency and loss reserves (ensure reserves are topped up)
Priority 2: Maintain overcollateralization (if OC is below target)
Priority 3: Originator/servicer carried interest (profit)
Priority 4: Seller incentive fees (typically paid to the owner of the equity)

A deal might allocate excess spread 0.25% to reserves, 0.40% to OC maintenance, 0.60% to carried interest. Only after all tiers are filled does equity profit.

## Excess spread in different market regimes

**Low-default environment**: Excess spread generates attractive equity returns. Equity holders earn 8–12% annually from excess spread.

**Stressed environment**: Defaults spike, excess spread shrinks or turns negative. Equity holders stop receiving distributions; some pools are entirely consumed by losses.

**Recovery environment**: Defaults normalize, excess spread recovers. Equity distributions resume.

Equity investors closely monitor excess spread trends. A consistent decline in excess spread (even if still positive) signals deterioration ahead.

## Excess spread and incentive alignment

Excess spread can create perverse incentives. If an originator profits from excess spread (by retaining equity), it has incentive to underestimate losses so that excess spread is high (making the securitization more attractive to buyers, raising the equity's sale price).

To prevent this, modern deals include originator retention (Dodd-Frank's 5% rule): the originator keeps some portion of the risk, ensuring losses directly impact the entity that profits from excess spread.

An originator that retains 5% equity and profits from excess spread on the remaining 95% has aligned incentives: accurate loss forecasting maximizes total value.

## Excess spread in CLOs (collateralized loan obligations)

In CLOs, excess spread is critical. CLOs leverage the underlying collateral heavily (issuing bonds equal to 90%+ of collateral value), so excess spread is thinner and more volatile. A CLO's waterfall might allocate excess spread:

- 0.5% to management fee
- 0.2% to reserves
- 0.3% to carried interest (manager compensation)
- Remainder to equity

CLO managers are incentivized by carried interest to maintain strong collateral and minimize losses. In a CLO with thin excess spread, this incentive aligns well with investor interests.

## Monitoring excess spread

Securitization trustees publish monthly factor data including:

- Weighted average coupon (WAC) of the collateral
- Weighted average cost of funds (WACF) of bonds and fees
- Implied excess spread

Investors track these metrics to see:
- Is excess spread stable or declining?
- Are defaults consuming spread?
- Is OC maintenance consuming spread?

A sharp drop in excess spread (collateral coupons falling as mortgages prepay, or losses rising) signals deterioration. Investors often use this as a sell signal (or a signal to hedge).

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/securitization/">Securitization</a> — excess spread is the mechanism driving securitization economics.</li>
<li>Weighted Average Coupon — the numerator of excess spread.</li>
<li><a href="/wiki/overcollateralization/">Overcollateralization</a> — often funded by excess spread.</li>
<li><a href="/wiki/tranche/">Tranche</a> — equity tranches are compensated via excess spread.</li>
<li>Servicing Fee — a component subtracted from collateral yield.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/structured-finance/">Structured Finance</a> — excess spread is the driver of structured-finance economics.</li>
<li><a href="/wiki/asset-backed-security/">Asset-Backed Security</a> — ABS returns depend on excess spread.</li>
<li><a href="/wiki/collateralized-loan-obligation/">Collateralized Loan Obligation</a> — CLOs are highly sensitive to excess spread.</li>
</ul>
</div>
