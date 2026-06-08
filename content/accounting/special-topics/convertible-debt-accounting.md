---
title: "Convertible Debt Accounting"
description: "How issuers split convertible notes into liability and equity components, and the amortisation of the debt discount."
keywords:
  - convertible bonds
  - debt-to-equity conversion
  - bifurcation accounting
  - compound instruments
  - debt discount amortisation
image: /svg/accounting.svg
---

*A **convertible debt** is a [bond](/bond/) or [note](/bond/) that the holder can convert into the issuer's common [stock](/stock/) at a predetermined price. Under current GAAP, issuers must **bifurcate** the instrument into two components: a [liability](/accounts-payable/) (the bond's debt portion) and an [equity](/common-stock/) (the value of the conversion option). This split affects interest expense, [earnings per share](/earnings-per-share/), and [balance sheet](/balance-sheet/) presentation.*

## The economic substance: embedded optionality

When a company issues a $100 million convertible bond paying 3% annual coupon, convertible into shares at $50 per share, it has effectively issued two things. The holder receives a bond (worth, say, $85 million) plus an embedded [call option](/call-option/) on the company's stock (worth $15 million). The option allows conversion only if the stock price rises above $50.

Traditional bond accounting would record the entire $100 million as debt and recognize the 3% coupon as interest expense. But that understates the true economics. The company is not just borrowing at 3%; it is granting an equity upside to the bondholder. If the stock soars, the bondholder converts and the company has issued stock at $50 per share—a dilution that was baked into the original deal. GAAP's bifurcation approach makes this explicit.

## Bifurcation: splitting liability and equity

The issuer records the convertible in two steps:

**Step 1: Measure the liability component.** Calculate the present value of the bond's contractual cash flows (coupon and principal repayment) discounted at the interest rate the company would pay on a non-convertible bond of similar credit quality and maturity. If a non-convertible bond would cost 5%, discount the convertible's cash flows at 5%.

**Step 2: Measure the equity component.** Record the remainder—the difference between the issue price and the liability value—as equity in the [stockholders' equity](/common-stock/) section. This represents the value attributable to the conversion option.

Example: A company issues $100 million convertible at 3% coupon, five-year maturity. The non-convertible rate is 5%. The PV of cash flows discounted at 5% is $85 million (liability). The equity component is $100 million – $85 million = $15 million. The company records:

- Debit: Cash $100 million
- Credit: Convertible debt (liability) $85 million
- Credit: Conversion option (equity) $15 million

This entry is permanent—the equity component is never remeasured. It sits in paid-in capital and is not marked to market.

## The debt discount and amortisation

The $85 million liability is recorded at a discount to its face value ($100 million). This $15 million discount is amortised over the bond's five-year life using the effective interest method. The amortisation increases [interest expense](/interest-rate/) beyond the stated 3% coupon.

Annual amortisation on a straight-line basis would be $3 million per year. But the effective interest method is more precise: it applies the non-convertible interest rate (5%) to the bond's carrying amount each period, and the difference between that calculated interest and the coupon paid flows through the [income statement](/income-statement/).

Year 1: Interest expense = $85 million × 5% = $4.25 million. Coupon paid = $100 million × 3% = $3 million. Discount amortisation = $1.25 million. The liability balance rises to $86.25 million.

Year 2: Interest expense = $86.25 million × 5% = $4.31 million. Coupon paid = $3 million. Discount amortisation = $1.31 million.

By maturity, the liability balance reaches $100 million and the entire discount has been amortised into interest expense. This accounting ensures that the total interest expense over the life of the bond reflects the true economic cost of borrowing at 5% (the non-convertible rate), not the misleading 3% coupon rate.

## Effect on interest expense and net income

Bifurcation increases reported interest expense. A company that issues a convertible bond intended to be cheaper than a straight bond is surprised to find that its interest expense is higher. This is not a real cash effect—the coupon is still 3%—but a non-cash charge from amortising the discount.

For companies focused on [earnings](/earnings-per-share/) metrics, this can be painful. A high-growth tech firm might issue a convertible at a low coupon to reduce near-term cash interest, only to discover that GAAP interest expense is elevated by the discount amortisation. Some companies manage this by sizing the equity component to be smaller (moving more value to the liability), which reduces the discount but also reduces the attractiveness of the conversion option to investors.

The discount amortisation is a non-cash item—it does not affect [cash flow](/cash-flow-statement/) from operations. Many investors adjust EBITDA or operating cash flow to exclude it, treating it as a financing artifact.

## Conversion and retirement

When a bondholder converts, the company eliminates the liability and issues stock. The accounting is straightforward:

- Debit: Convertible debt (liability) – carrying amount at conversion
- Debit: Conversion option (equity) – original amount (never changed)
- Credit: Common stock and paid-in capital – total of the above, plus any excess (if the stock is worth more than the debt carrying amount, the excess is paid-in capital)

No gain or loss is recorded. The conversion price is fixed at issuance ($50 in the earlier example), and the stock is recorded at the debt's carrying amount plus the conversion option value.

If the convertible is redeemed by the company before conversion (called by the issuer), the liability is retired at its carrying amount, and the equity component is reclassified to paid-in capital. Again, no gain or loss—the entire instrument is treated as a single, composite transaction.

## Dilution and earnings per share

The conversion option creates potential dilution. When calculating [diluted earnings per share](/earnings-per-share/), the company must include the shares that would be issued upon conversion in the denominator, using the treasury stock method. This treats the conversion as if it occurred at the beginning of the period (or at issuance if more recent).

The treasury stock method works as follows: assume the convertible is converted into (say) 2 million shares. Assume those shares are sold at the current market price, and the proceeds are used to repurchase the company's own stock. The net increase in share count is 2 million shares minus the repurchased shares. This net amount is added to the denominator of EPS.

A convertible with a low conversion price (deep in-the-money) will have high dilution; one with a high conversion price (far out-of-the-money) will have low dilution. As the stock price rises, dilution increases, making the convertible a more expensive financing in hindsight.

## When to use convertible debt

Companies issue convertibles for several reasons:

- **Lower coupon**: The conversion option is valuable to investors, so they accept a lower interest rate. A 2–3% coupon is typical vs. 4–5% for a non-convertible bond, saving annual interest expense.
- **Deferring dilution**: The company does not immediately issue stock; instead, it delays equity issuance until (or if) the conversion option is exercised. Existing shareholders appreciate the postponement.
- **Financing flexibility**: A convertible is easier to sell to conservative investors (who focus on the bond floor) and equity investors (who focus on the upside) simultaneously.

The trade-off is future dilution and more complex accounting. A company issuing convertibles must be comfortable with the possibility of significant equity dilution if stock prices rise, or with refinancing the debt if prices stagnate.

## Recent changes: ASU 2020-06

In August 2020, FASB issued ASU 2020-06, which simplified convertible debt accounting for certain issuers. Under the new guidance, companies may elect a reduced-disclosure presentation that removes the bifurcation of the equity component in specific cases (primarily when the conversion feature is not separately exercisable and the debt has only one embedded conversion option). However, most convertibles still require bifurcation.

The update also clarified the diluted [EPS](/earnings-per-share/) calculation, allowing issuers to use the "if-converted" method in more situations, which can reduce the reported dilution in some cases. These changes have made convertible debt slightly simpler to account for, but bifurcation remains the default treatment.

## See also

<div class="wiki-seealso">

### Closely related

- [Bond and debt instruments](/bond/) — the debt component of a convertible
- [Call option](/call-option/) — the embedded conversion option
- [Stockholders' equity and paid-in capital](/common-stock/) — where the conversion option is recorded
- [Earnings per share dilution](/earnings-per-share/) — effect of convertible conversion on share count
- [Debt-to-equity ratio](/debt-to-equity-ratio/) — balance sheet impact of bifurcation

### Wider context

- [Interest expense and amortisation](/amortization/) — the discount amortisation mechanics
- [Fair value measurement](/fair-value/) — valuing the embedded option
- [Cash flow statement](/cash-flow-statement/) — non-cash discount amortisation effects
- [Capital structure and financing](/equity-financing/) — strategic role of convertibles in capital-raising
- [Securities issuance and disclosure](/securities-and-exchange-commission/) — regulatory requirements for convertible offerings

</div>
