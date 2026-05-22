---
title: "Total Return Index"
description: "Stock market index in which dividends are automatically reinvested, showing capital appreciation plus cumulative dividend income."
keywords:
  - total return index
  - dividend reinvestment
  - index methodology
  - index performance
---

*The **total return index** measures the performance of a group of stocks assuming that all [dividends](/wiki/dividend/) are automatically reinvested in the index at the time of payment. This contrasts with [price return indices](/wiki/price-return-index/), which reflect only capital appreciation and ignore dividend income.*

<div class="wiki-hatnote">For the basis index concept, see <a href="/wiki/price-return-index/">Price Return Index</a>. For dividend treatment in ETFs, see <a href="/wiki/etf-distribution-strategy/">ETF Distribution Strategy</a>.</div>

<aside class="wiki-infobox">

| Feature | Total Return | Price Return |
|---|---|---|---|
| **Dividend treatment** | Reinvested; reflected in index level | Ignored; not reflected |
| **Historical performance** | Higher; includes income | Lower; capital only |
| **Use case** | Realistic investor returns; buy-and-hold benchmarking | Academic analysis; price discovery |
| **Calculation** | Requires dividend data and reinvestment timing | Simpler; only requires prices |
| **Typical outperformance** | 2–3% annually in mature markets; higher in high-yield markets | N/A |

</aside>

## The mechanics of total return indexing

A simple example illustrates the difference. Suppose an index contains a single stock trading at $100 with a 2% annual dividend:

**Price return index**: The stock rises to $105 over the year. The index rises from 100 to 105. The return is 5% (capital appreciation only). The dividend is ignored.

**Total return index**: The stock rises to $105. A $2 dividend is paid at mid-year (or end-of-year, depending on convention). That $2 is reinvested at the dividend's ex-date price (say, $102). The reinvested dividend buys $2/$102 = 0.0196 additional shares. At year-end, the investor owns 1.0196 shares at $105 = $107.06. The return is 7.06% (capital appreciation plus reinvested dividend income).

Over decades, this compounding effect becomes large. The total return index for the [S&P 500](/wiki/sp-500-index/) is roughly 50% higher than the price return index over long periods, due to accumulated dividend reinvestment.

## Why the distinction matters

The choice between total and price return indices affects reported performance and investor expectations:

**Realistic investor outcomes**: A buy-and-hold equity investor who reinvests dividends (or who owns a total return ETF) earns the total return index's return, not the price return. Comparing portfolio performance to a price return benchmark understates actual results.

**Benchmarking and mandate design**: If a fund manager is benchmarked to a price return index, she is credited with dividend income as "outperformance" beyond the benchmark, even though that income is part of a realistic index return. This creates a subtle bias: the manager's skill is conflated with the index's income generation.

**International comparisons**: Different markets and index providers use different conventions. Some matkets (UK, dividend-heavy sectors) heavily favor total return; others (growth-focused markets like the US tech sector) weight price return more. International fund comparisons can be misleading if they mix index types.

**Tax considerations**: Dividend reinvestment creates taxable events in taxable accounts. A total return index assumes reinvestment without accounting for taxes, whereas a real investor in a taxable account faces [capital gains tax](/wiki/capital-gains-tax/) on the dividend income.

## Index provider methodologies

Major index providers ([S&P](/wiki/sp-500-index/), [MSCI](/wiki/emerging-markets-fund/), FTSE, etc.) maintain both price and total return versions of their indices. The methodologies are standardized but differ in detail:

**Dividend timing**: When is the dividend assumed to be reinvested? Some indices reinvest at the ex-dividend date; others at the payment date. This timing difference can affect short-term returns by small amounts but rarely materially.

**Gross vs. net total return**: The **gross total return** assumes dividends are reinvested without tax or fees. The **net total return** deducts assumed withholding taxes on dividends (relevant for international indices, where foreign withholding taxes reduce actual dividend income). A US investor in an international index may earn the "net" return after local withholding tax, not the gross return.

**Survivorship**: Does the index reinvest dividends from companies that have been removed (delisted, merged, spun off)? Some indices handle this cleanly; others have edge cases where the treatment is ambiguous.

## Total return vs. price return in practice

For **long-term buy-and-hold investing**, total return indices are the more relevant benchmark:

- The [S&P 500](/wiki/sp-500-index/) price return index has returned roughly 10% annualized since 1950; the total return version has returned roughly 12–13% annualized, reflecting reinvested dividends.
- A retiree withdrawing dividends but living off them (not reinvesting) would match the price return, not the total return.
- A young investor who reinvests dividends would match the total return index.

For **tactical or short-term trading**, price return may be more relevant:

- A trader betting on a 3-month price move cares only about capital appreciation, not dividends paid months later.
- High-frequency traders and algorithms focus on price-level moves, not dividend income.

For **equities research and valuation**, price return is standard. A stock's [earnings yield](/wiki/earnings-yield/) and [dividend yield](/wiki/dividend-yield/) are analyzed separately; dividend policy is a separate strategic decision from operating performance.

## Total return indices and ETF distribution

The rise of [ETFs](/wiki/etf/) has complicated the picture. An ETF tracking the total return version of an index will:

1. Hold all index constituents.
2. Collect dividends.
3. *Either* reinvest dividends in-kind (buying more index shares) *or* distribute them to shareholders.

If the ETF reinvests, its net asset value (NAV) grows with the total return index. If the ETF distributes dividends, its NAV only matches the price return index; the distributed dividends are held in the shareholder's cash, not automatically reinvested in the ETF.

This distinction is crucial for tax planning. A dividend-distributing fund in a taxable account creates annual tax liability on dividends, even if the shareholder wants to reinvest. A reinvesting (accumulating) fund defers tax until the ETF is sold.

Most broad equity ETFs are dividend-distributing, so their performance tracking may show *lower* returns than the total return index (due to taxable distributions) and *higher* returns than the price return index (because dividends are part of the ETF's NAV, even if distributed).

## Historical returns and expected total returns

Over long periods, total return has vastly outpaced price return in mature equity markets:

- **S&P 500** (1950–2024): Price return ~10% annualized; total return ~12–13% annualized.
- **FTSE 100** (UK): Total return has exceeded price return by ~2–3% annualized, reflecting steady dividend yields.
- **Emerging markets**: More variable; markets with high dividend yields (South Africa, Brazil) show larger gaps; markets with low yields (China, India) show small gaps.

This persistence of dividend income in total returns underscores the importance of using the correct index for performance evaluation. An investor benchmarked to a price return index will appear to outperform by the dividend yield each year, even if earning the market return.

Forward-looking, the total return index is typically the baseline for estimating expected equity returns. [Valuation models](/wiki/discounted-cash-flow-valuation/) assume dividend reinvestment and use total return as the discount rate.

<div class="wiki-seealso">

### Closely related
- [Price Return Index](/wiki/price-return-index/)
- [Dividend](/wiki/dividend/)
- [Dividend Yield](/wiki/dividend-yield/)
- [ETF Distribution Strategy](/wiki/etf-distribution-strategy/)

### Wider context
- [S&P 500 Index](/wiki/sp-500-index/)
- [Index Fund](/wiki/index-fund/)
- [Factor Investing](/wiki/factor-investing/)
- [Dividend Reinvestment Plan](/wiki/dividend-reinvestment-plan/)

</div>
