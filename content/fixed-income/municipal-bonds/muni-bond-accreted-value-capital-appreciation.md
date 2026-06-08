---
title: "Accreted Value in Municipal Capital Appreciation Bonds"
description: "Municipal capital appreciation bonds are sold at a deep discount and grow to par maturity. Learn to compute accreted value, understand tax treatment, and assess early sale impact."
keywords:
  - muni bond accreted value
  - capital appreciation bond calculation
  - municipal bond discount to par
  - accretion taxation
  - muni bond early sale
image: /svg/fixed-income.svg
---

*A **municipal capital appreciation bond** (or zero-coupon muni) is issued at a deep discount and makes no coupon payments; its value accretes—grows mechanically—from the discounted purchase price to par at maturity. The **accreted value** at any point is the bond's theoretical value according to its accretion schedule, even though you do not receive that cash until maturity. Computing accreted value is straightforward algebra, but the tax treatment—how much phantom income you owe each year—is a trap that catches many municipal bond investors.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Accreted Value in Muni CABs — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Accretion is predictable, but tax on phantom income surprises investors who hold to maturity.</div>

|   |   |
|---|---|
| **Bond type** | Zero-coupon [municipal bond](/municipal-bond/); no interim cash payments |
| **Purchase** | Sold at deep discount (often 40–60% of par) |
| **Maturity value** | Par value (face amount); e.g., $10,000 |
| **Accretion** | Linear or compound; stated in bond prospectus |
| **Accreted value year *N* | = Purchase Price × (1 + Accretion Rate)^*N* |
| **Tax treatment** | Phantom income is taxable each year; still applies to munis in some cases |
| **Early sale** | Accrued capital appreciation = (Accreted Value) − (Purchase Price); taxable at gain |

</aside>

## Why issuers use capital appreciation bonds

Municipalities issue zero-coupon bonds to fund large projects without annual cash outflows. If a city needs $50 million for a new airport but has no immediate revenue, it can issue $100 million face value of zero-coupon munis maturing in 20 years. The city receives perhaps $32 million upfront (40% of par), avoids coupon payments for two decades, and repays $100 million at maturity.

For investors, these bonds appeal to those saving for a known future expense (college tuition, retirement, project deadline) because the maturity value is certain and the tax structure can be favorable—especially if the bond is issued tax-exempt and held to maturity.

## Computing accreted value

Accreted value follows a straightforward formula. Most capital appreciation munis use **straight-line accretion** (simpler for taxation) or **compound accretion** (constant yield, more realistic).

**Straight-line accretion** (most common for munis):

Accreted Value at Year *N* = Purchase Price + (Par − Purchase Price) × (*N* / Maturity Years)

**Example:**
- Purchase price: $3,500 per $10,000 bond.
- Maturity: 20 years.
- Annual accretion: ($10,000 − $3,500) / 20 = $325.
- Accreted value after 10 years: $3,500 + (10 × $325) = $6,750.
- Accreted value after 15 years: $3,500 + (15 × $325) = $8,375.

**Compound accretion** (yield-based):

Accreted Value at Year *N* = Purchase Price × (1 + Yield Rate)^*N*

This accounts for reinvested earnings and is closer to [bond pricing](/bond/) reality, but most municipal zeros use straight-line for simplicity.

## The accreted value at each reporting date

Your bond's accreted value grows each year—it is printed in the official statement or bond offering document. You can also request it from your broker or the bond trustee. The accreted value is *not* the market price (which fluctuates with interest rates), but rather the "official" intrinsic value according to the bond's terms.

At any point before maturity, the bond's **market price** may trade above or below accreted value, depending on whether [interest rates](/interest-rate/) have fallen (price rises above accreted value) or risen (price falls below). But accreted value is the anchor—the value implied by the original discount and maturity terms.

## Phantom income and annual taxation

Here is the tax trap: even though you receive *no cash* until maturity, the IRS requires you to pay income tax on the annual accretion—the increase in accreted value each year. This "phantom income" applies to most capital appreciation bonds, including tax-exempt municipal zeros (unless they are specifically exempted under state law).

**Example of phantom income burden:**

- You buy a 20-year muni zero for $3,500 (par $10,000).
- Year 1 accretion: $325 (from $3,500 to $3,825).
- Year 2 accretion: $325 (from $3,825 to $4,150).
- ... and so on for 20 years.

If this is a federal tax-exempt muni, you still owe state and local tax (in most states) on that $325 annual phantom income—roughly 5–10% of the accretion, depending on your state. If the bond is *not* tax-exempt, you owe federal tax too.

This is a major risk: investors who buy these bonds expecting low annual tax obligations are shocked to receive a 1099 statement each January, reporting income they have not yet received.

## Tax implications: holding to maturity vs. early sale

**Holding to maturity**: You accumulate phantom income taxes year by year. At maturity, you receive par ($10,000) and have zero capital gain—you already paid tax on the full accretion as it occurred. Your net after-tax proceeds depend on the total phantom income tax owed over the years.

**Early sale before maturity**: Suppose after 10 years the bond's accreted value is $6,750, and you sell it for $6,750 (accreted value; ignoring market fluctuations). You have:

- Realized gain = Selling price − Original purchase price = $6,750 − $3,500 = $3,250.
- Tax owed: Long-term [capital gains tax](/long-term-capital-gain-tax/) on $3,250 (assuming hold > 1 year).
- *But*: You already paid phantom income tax on years 1–10. If those taxes cannot be credited, you face *double* taxation—phantom income tax *and* capital gains tax on the same appreciation.

The precise treatment varies by state and bond type. Some states exempt capital appreciation munis from phantom income taxation if held to maturity, but tax gains on early sales. Others tax phantom income annually regardless. **Consult a tax professional before buying zero-coupon munis.**

## Market price vs. accreted value

As time passes, a capital appreciation bond's market price may diverge from its accreted value:

- **Interest rates fall**: New bonds are issued with lower yields. Existing bonds become more valuable. Market price rises *above* accreted value.
- **Interest rates rise**: New bonds are issued with higher yields. Existing bonds become less attractive. Market price falls *below* accreted value.

The accreted value is not the "fair" price—it is the mechanistic value implied by the original discount rate. The market price reflects the actual [yield to maturity](/yield-to-maturity/) demanded by traders today. If you sell before maturity at a market price above accreted value, you realize a gain beyond the accretion; if you sell below, you realize a loss despite accrual.

## Accreted value and [duration](/duration/)

Capital appreciation bonds have high [duration](/duration/) (interest-rate sensitivity) because all cash flows come at maturity. A 20-year muni zero can have a [duration](/duration/) of 15–18 years, meaning a 1% change in yield causes a 15–18% change in market price. This makes them volatile and suitable only for investors with a long time horizon or a specific maturity target.

If you must sell a 20-year muni zero after 5 years and interest rates have risen, the market price may be 30–40% below accreted value—a severe loss, even though accretion has technically increased the bond's "value."

## When capital appreciation munis make sense

These bonds are most suitable for:

- **Tax-deferred accounts** ([IRA](/traditional-ira/), [401(k)](/401k-plan/)): Phantom income is not taxable in the current year within these accounts.
- **Investors in low tax brackets**: Phantom income tax is minimal.
- **Known future liabilities**: An investor who knows they will need $10,000 in exactly 20 years can buy the zero for $3,500, lock in the maturity value, and avoid phantom income tax if the bond is held in a qualified retirement account.
- **States with exempt or favorable tax treatment**: Some states exempt municipal zeros from state phantom income tax.

For taxable accounts in high-tax-rate states, the annual phantom income burden often makes standard coupon-paying munis or [Treasury bonds](/treasury-bond/) more efficient.

## Accreted value in [municipal bond funds](/municipal-bond-fund/)

Mutual funds holding capital appreciation munis must mark positions to market each day, meaning the accreted value (or market price, if lower) is reflected in the fund's [net asset value](/net-asset-value/). The fund does not distribute cash from these positions, but the phantom income (if any) is still attributed to shareholders for tax purposes. This is another reason many bond funds avoid or minimize zero-coupon holdings.

## See also

<div class="wiki-seealso">

### Closely related

- [Municipal Bond](/municipal-bond/) — the parent asset class; most munis pay coupons
- [Yield to Maturity](/yield-to-maturity/) — the discount rate embedded in the bond's accreted value
- [Duration](/duration/) — why zero-coupon munis are interest-rate sensitive
- [Municipal Bond Fund](/municipal-bond-fund/) — aggregates municipal bonds including some zeros
- [Bond](/bond/) — general bond pricing and terminology
- [Long-Term Capital Gains Tax](/long-term-capital-gain-tax/) — applies to early sales of zeros

### Wider context

- [Traditional IRA](/traditional-ira/) — tax-advantaged account where muni zero phantom income is sheltered
- [401(k) Plan](/401k-plan/) — alternative tax shelter for zero-coupon bond holdings
- [Interest Rate](/interest-rate/) — drives the market price divergence from accreted value
- [Tax Bracket Investor](/tax-bracket-investor/) — determines whether phantom income burden is manageable
- [Reinvestment Risk](/reinvestment-risk/) — zeros eliminate it; all cash is locked in at maturity

</div>
