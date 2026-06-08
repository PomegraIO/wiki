---
title: "ADR to Ordinary Share Conversion: Tax Consequences"
description: "Tax consequences of converting an ADR to ordinary shares depend on whether the conversion is a taxable event, how cost basis transfers, and reporting obligations that arise."
keywords:
  - tax consequences of converting adr to ordinary shares
  - adr conversion tax treatment
  - american depositary receipt conversion
  - basis step-up adr conversion
  - adr exchange tax impact
image: /svg/equity.svg
---

*Converting an [American Depositary Receipt](/adr/) (ADR) into its underlying ordinary shares is generally **not a taxable event** for US tax purposes. You do not recognize a gain or loss at conversion; instead, your [cost basis](/cost-basis/) in the ordinary shares equals your basis in the ADR. However, if the conversion involves a currency exchange or fees, the treatment becomes more complex, and reporting obligations differ depending on whether the conversion is domestic or involves cross-border flows.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ADR-to-Ordinary Conversion — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The conversion itself is not a taxable event; gain or loss is deferred until you sell the ordinary shares.</div>

|   |   |
|---|---|
| **Taxable event** | No; conversion is a tax-deferred exchange |
| **Cost basis transfer** | Carries over from ADR to ordinary shares; no step-up or step-down |
| **Currency treatment** | If ADR is denominated in USD and ordinary share in foreign currency, conversion may trigger forex gain/loss |
| **Fees and costs** | Custodial fees reduce basis; conversion costs may be capitalized |
| **Holding period** | Carries over; no reset on conversion |
| **Reporting** | Form 8949 for any forex component; Schedule D for eventual sale of ordinary shares |
| **Foreign tax credits** | Potential; depends on withholding by the issuer country |

</aside>

## Why ADR-to-ordinary conversion is not a taxable event

The IRS treats an [ADR](/adr/) and its underlying [ordinary shares](/common-stock/) as substantially the same security for tax purposes. When you convert an ADR into ordinary shares, you are exchanging one form of the same equity security for another form. This falls under **non-taxable exchange** treatment, similar to a stock split or share dividend.

The IRC does not require you to recognize gain or loss on the conversion itself. Your tax basis in the ordinary shares is carried over directly from your basis in the ADR. If you bought an ADR for $1,000, your cost basis in the ordinary shares is $1,000. You defer any gain or loss until you sell the ordinary shares.

This treatment applies whether you convert at a custodian's request (a forced conversion during depositary termination), at your election during normal operation, or through a corporate action (e.g., the issuer instructs the ADR depositary to convert all outstanding ADRs and retire them).

## Carrying over cost basis and holding period

Your cost basis in the ordinary shares is equal to your cost basis in the ADR, plus any capitalized conversion costs, minus any custodial fees allocable to the conversion.

If you held the ADR for three years before conversion, your holding period in the ordinary shares includes that time. The conversion does not reset the clock. This matters for [long-term capital gains](/long-term-capital-gain-tax/) treatment: if you convert after holding the ADR for more than one year, any gain on the ordinary shares is long-term, taxed at favorable rates (15% or 20% depending on income).

**Example**: You buy an ADR for $100 per share on January 1, 2022. On June 1, 2025, the ADR is worth $150. You convert it to ordinary shares. Your cost basis in the ordinary shares is still $100; your holding period is 3.5 years. When you sell the ordinary shares for $180 in 2026, your long-term capital gain is $80, taxed at the long-term rate, not ordinary income.

## Currency exchange complications

The straightforward treatment above assumes the ADR and ordinary shares are denominated in the same currency (typically USD for an ADR, local currency for ordinary shares). But if conversion involves a currency mismatch, the IRS may recognize a separate currency gain or loss.

Some ADRs are quoted and traded in USD on US exchanges but represent shares of non-US companies. If the underlying ordinary shares are traded in a foreign currency (euros, yen, pesos), conversion from USD-denominated ADR to foreign-currency ordinary shares may trigger a **recognized foreign exchange gain or loss** at the time of conversion.

**Example**: You own an ADR of a German company, quoted in USD. At conversion, 1 ADR = 1 ordinary share worth 95 euros. If the ADR is trading at $100 USD, but the ordinary share is worth 95 euros and the USD/EUR rate is 1.05, there is an implicit currency mismatch. The IRS may treat this as a gain or loss depending on the specific conversion mechanics.

However, if the ADR custodian or your broker handles the conversion and absorbs any currency risk (converting USD to foreign currency), the conversion is often priced to be economically neutral, and no explicit forex gain is recognized. The treatment depends on whether the conversion involves actual currency exchange or is purely a custodial paper conversion.

It is wise to consult a tax professional if conversion involves currency exchange, as the IRC treatment of such conversions is context-specific.

## Custodial fees and their basis impact

The custodian holding your ADR typically charges fees for conversion—ranging from $5 to $100+ per ADR, depending on the custodian and the issuer. These fees reduce the net proceeds of conversion or are charged separately.

**Tax treatment**: Custodial fees paid to convert are capitalized—they increase your cost basis in the ordinary shares. So if you convert an ADR with a $1,000 basis and pay a $50 custodial fee, your cost basis in the ordinary shares is $1,050. This defers the fee's tax impact until you sell the shares, at which point it reduces your taxable gain.

This is different from custodial fees for holding an ADR while you own it, which are sometimes deductible as miscellaneous itemized deductions (though deduction has been limited since 2017 for most taxpayers). Only the specific conversion fee is added to basis.

## Holding period and washout risk

Your holding period in the ordinary shares begins on the original purchase date of the ADR, not the conversion date. This is important if the ADR price has fallen since purchase and you are considering converting and then immediately selling the ordinary shares at a loss.

The IRS will not challenge this as a wash sale (which would disallow the loss) because conversion is not a "sale or other disposition" of substantially identical security in the wash-sale sense. However, if you buy ADRs, convert to ordinary shares, immediately sell at a loss, and then repurchase ADRs or ordinary shares within 30 days, the wash-sale rule *will* apply to the repurchase, disallowing the loss and adding its amount to the basis of the repurchased shares.

## Reporting the conversion

**For the conversion itself**: Since conversion is not a taxable event, you do not report it on Form 8949 (Sale of Capital Assets) or Schedule D in the year of conversion. However, if the conversion includes a forex component (foreign exchange gain or loss), you must report that separately, usually on Form 8949 as a Section 988 forex transaction.

**For the subsequent sale**: When you eventually sell the ordinary shares, you report the sale on Form 8949 and Schedule D, using the carried-over cost basis and holding period. Your broker will not issue a Form 1099-B for the conversion itself; instead, it will track the ordinary shares as a continuation of your ADR position.

**Annual foreign taxes**: If you receive [dividend](/dividend/) payments on the ordinary shares and the issuer is in a country that imposes withholding tax, you may be eligible for a foreign tax credit or exclusion under IRC Section 933 (if you qualify as a bona fide foreign resident). Report this on Form 1116 (Foreign Tax Credit) or Schedule 3, depending on your situation.

## Forced conversions during depositary termination

Sometimes an ADR issuer or depositary decides to terminate the ADR program, forcing all ADR holders to convert. This is common when an ADR program becomes too expensive to maintain or when a company is acquired.

In a forced conversion:

- The conversion is still non-taxable
- You receive one (or a specified ratio of) ordinary share(s) per ADR
- Your cost basis carries over
- Any cash received in lieu of fractional shares is treated as a sale of that fractional share; you report any gain or loss on Form 8949

The forced conversion itself does not trigger tax; only the cash-out of fractional shares does. And even then, if the fractional share value equals your basis (no gain), there is no tax owed.

## Foreign tax implications for non-US tax residents

If you are a non-US citizen or tax resident converting ADRs to ordinary shares, your home country's tax system may have different rules. Some countries treat conversion as a triggering event (even if the US does not), while others align with the US treatment.

Additionally, when you hold ordinary shares directly (not as an ADR), your obligations for foreign investment reporting (FBAR, FATCA, etc.) may change. If you reside outside the US, consult your home country's tax authority regarding any new reporting requirements or tax exposure arising from the conversion.

## Strategic timing and tax planning

Because conversion is non-taxable, timing the conversion itself does not matter for tax purposes. However, if you plan to sell the ordinary shares shortly after conversion, be mindful of:

- **Wash-sale rules** if you have recent losses in the ADR or ordinary shares
- **Year-end gains harvesting** if you want to realize long-term gains in a specific tax year
- **Currency exposure** if conversion locks in a specific exchange rate that you would prefer to avoid
- **Dividend ex-dates** on the ordinary shares, which affect when you receive income

None of these changes the tax treatment of the conversion itself; they are considerations for the overall strategy.

## See also

<div class="wiki-seealso">

### Closely related

- [ADR](/adr/) — the depositary receipt structure and mechanics
- [Ordinary Share](/common-stock/) — the underlying security represented by the ADR
- [Cost Basis](/cost-basis/) — how your tax basis is determined and tracked
- [Long-Term Capital Gains Tax](/long-term-capital-gain-tax/) — the preferential tax rate on gains held over one year
- [Form 8949](/form-8949/) — the tax form for reporting sale of capital assets

### Wider context

- [Dividend](/dividend/) — income received on ordinary shares and foreign withholding treatment
- Foreign Tax Credit — credits for taxes paid to foreign countries
- ADR Ordinary Share Conversion — the mechanics of the conversion process
- [Depositary Receipt](/depositary-receipt/) — the broader category including ADRs and GDRs
- [Currency Risk](/currency-risk/) — foreign exchange exposure relevant to ADRs of non-US companies

</div>
