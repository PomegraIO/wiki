---
title: "Net Return Index"
description: "An index variant that deducts the tax withheld on dividend payments, reflecting returns available to foreign or tax-exempt investors."
keywords:
  - net return index
  - total return index
  - withholding tax
  - dividend tax
  - index returns
image: "/svg/institutions.svg"
---

*A **net return index** is a version of a [total return index](/index-fund/) that reduces total return by the amount of tax withheld on [dividend](/dividend/) payments, typically at statutory rates. It models the after-tax return experienced by a foreign investor or one without recourse to dividend tax credits.*

## Contrast with total return and price return

Most [equity](/stock/) indices exist in three flavours:

1. **Price return index** — tracks only capital appreciation; ignores dividends.
2. **Total return index (gross)** — assumes all dividends are reinvested immediately and fully captured, with no tax.
3. **Net return index** — reinvests dividends but deducts modeled withholding tax, leaving the "net" amount available to invest.

An investor in the S&P 500 might track different index versions depending on tax status and nationality. A US domestic investor holding individual stocks can use the gross total return index and account for taxes separately at year-end. A non-resident foreign investor in a US-domiciled mutual fund faces a 15% dividend [withholding tax](/withholding-tax/) under US law (or treaty rates), so a net return index deducting 15% from each dividend more accurately reflects her actual economic experience.

## Calculation mechanics

Suppose an index has a gross total return of 8% per year, composed of 3% capital appreciation and 5% in [dividend yield](/dividend-yield/). A net return index version would assume that dividends are:

1. Paid in full (5% yield captured)
2. Subject to statutory withholding tax (e.g., 15%)
3. Reinvested after tax

The withholding reduces the reinvestable dividend to 5% × (1 – 0.15) = 4.25%. The net return index would therefore show approximately 3% + 4.25% = 7.25% annual return, versus the gross 8%.

More formally:

> **Net Return = Capital Appreciation + (Dividend Yield × (1 – Withholding Tax Rate))**

The exact rate depends on the investor's domicile and applicable tax treaties.

## Who uses net return indices

**Non-resident foreign investors** are the primary audience. A German pension fund investing in a US equity index fund faces US dividend withholding tax. Rather than tracking a gross total return index (which overstates returns), the fund can benchmark against the net return version.

**Currency-neutral funds** sometimes use net return indices for the same reason: to model the actual economic return a non-resident experiences after tax and currency conversion.

**Tax-exempt entities** (endowments, foundations, some sovereign wealth funds) that are exempt from US withholding may not use net return indices, because they recover withheld tax through treaty reclaim processes. For them, gross total return is more relevant.

**Funds marketed globally** (like MSCI World or FTSE All-World indices) often publish both gross and net versions to accommodate diverse investor bases.

## Treaty and statutory variations

Withholding rates are not uniform. US dividend withholding is typically 15% under US law but can be reduced to 5% or 0% under tax treaties with certain countries (Canada, UK, Australia, most OECD members). So a UK pension fund investing in the US may see a 0% withholding rate and thus use a higher "net" return index, while a Chinese investor sees 10% and uses a lower one.

Index providers publish multiple net return variants, one for each major treaty jurisdiction. The "MSCI USA Net Return Index for Non-Resident Investors" might reflect 0% US withholding for treaty-eligible funds, while a "Net Return — Statutory Rate" version uses the baseline 15%.

## Reinvestment assumption

A critical assumption in net return indices is immediate reinvestment of after-tax dividends at each [ex-dividend](/stock/) date. In reality, a fund may receive dividends quarterly or annually and reinvest with a lag. Additionally, the index assumes reinvestment at the exact dividend rate; if some dividends are missed (e.g., due to portfolio sampling or liquidity), actual returns will diverge.

For [ETF](/etf/) and [mutual fund](/mutual-fund/) providers tracking a net return index, this gap is often acceptable because index tracking allows for **sampling**—holding a representative subset of constituents rather than all of them—and small reinvestment lags are absorbed in typical [tracking error](/index-fund/).

## International context

Net return indices are particularly important for non-US markets. A European equity fund (tracking the STOXX 600, for example) available to US investors will be benchmarked against a gross total return index because US law does not impose dividend withholding on such funds. But the same fund available to, say, Canadian investors may benchmark a net return index reflecting Canadian withholding rates.

Some index providers publish "Net Return Hedged" indices for currency-hedged portfolios, further adjusting returns for the cost of currency forward contracts used to eliminate [currency risk](/currency-risk/).

## Practical differences in performance

Over long periods, the difference between gross and net return indices compounds. A 20-year equity market rising at 7% per year (gross) grows to roughly 3.87x its starting value. The same market at 6% per year (net, after 1% annual withholding) grows to roughly 3.26x—a meaningful 13% performance gap by the end.

This is why index selection and tax structure matter: an investor tracking a gross total return index in a jurisdiction with withholding tax will experience returns well below the published index, potentially raising questions about fund quality or design. Using a net return index benchmark clarifies the picture.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Yield](/dividend-yield/) — the key component modeled in net return indices
- [Total Return](/index-fund/) — the broader concept net return refines
- [ETF](/etf/) — products often benchmarked to net return indices
- [Index Fund](/index-fund/) — passive vehicles relying on accurate index variants
- [Index Licensing](/index-licensing/) — licensing agreements cover index variants
- [Fundamental Weighting](/fundamental-weighting/) — alternative indices also have gross/net versions

### Wider context

- [Dividend](/dividend/) — the source of withheld tax
- [Withholding Tax](/withholding-tax/) — statutory or treaty rates deducted from dividends
- [Tax Bracket Investor](/tax-bracket-investor/) — tax status determines which index version is relevant
- [International Financial Reporting Standards](/international-financial-reporting-standards/) — accounting treatment of withholding
- [Currency Risk](/currency-risk/) — often paired with net return indexing for foreign investors

</div>
