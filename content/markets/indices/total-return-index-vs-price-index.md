---
title: "Total Return Index vs Price Index"
description: "How total return indices reinvest dividends, creating vastly different long-term performance from price-only indices tracking the same basket."
keywords:
  - total return index vs price index
  - price return index
  - dividend reinvestment
  - index total return
---

*A **total return index** reinvests all dividends and distributions automatically, while a **price return index** (or "price index") reflects only the capital appreciation of the underlying stocks. Over decades, a total return index for the same set of stocks will be substantially higher—often 2–3× or more—because dividends compound. The difference matters hugely when comparing funds or benchmarking portfolio performance.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Total Return vs Price Index — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Same stocks, different accountings: one includes reinvested dividends, one does not.</div>

|   |   |
|---|---|
| **Price Index** | Capital appreciation only; dividends ignored |
| **Total Return Index** | Dividends reinvested as if bought new shares |
| **Long-term gap** | 2–4× difference over 30+ years |
| **Example** | SP 500 price index ~13× since 1980; total return ~50× |
| **Fund matching** | Total return indices track most [index-fund](/index-fund/) performance |
| **Tax impact** | Total return assumes tax-free reinvestment (not true in reality) |

</aside>

## Why the gap exists

Stocks generate two sources of return: price appreciation (capital gains) and [dividend](/dividend/) payments. A price index captures only the first. If a stock rises from $100 to $120, that's a 20% return in a price index. But if it also paid a $5 dividend during that year, the total economic return to an investor was ($120 − $100 + $5) / $100 = 25%.

A total return index assumes that every dollar of [dividend-distribution](/dividend-distribution/) received is immediately reinvested into the index at the prevailing price. Over time, that reinvestment compounds—each year's dividend buys new shares, which themselves pay dividends the next year. The result is exponential growth, not linear.

## A concrete example

Consider a simplified index of two stocks held over 10 years:

| Year | Stock A Price | Stock A Dividend | Stock B Price | Stock B Dividend |
|------|---------------|------------------|---------------|------------------|
| 0    | $100          | —                | $50           | —                |
| 1    | $105          | $4               | $52           | $2               |
| 2    | $110          | $4.50            | $55           | $2.25            |
| 3    | $115          | $5               | $58           | $2.50            |

**Price Index:** Weights stocks equally (50/50). Year 0 index level = 100 (baseline). Year 3 index level:

(($115 − $100) / $100 + ($58 − $50) / $50) / 2 = (15% + 16%) / 2 = 15.5% total return over 3 years, or index of 115.5.

**Total Return Index:** Each year, reinvest dividends. After year 1, the $4 dividend from Stock A buys 0.038 shares at $105. Stock B's $2 buys 0.038 shares at $52. New position: 1.038 shares of A, 1.038 shares of B. Year 3 calculation: those accumulated shares now worth (1.0 shares × $115 + 0.13 shares × $115) + (1.0 shares × $58 + 0.13 shares × $58) = higher than the price index alone.

Over 3 years, the price index rises ~15.5%. The total return index rises ~17–18% (depending on exact reinvestment timing). The gap is small early on but widens with decades.

## Long-term empirical gap

The US [sp-500-index](/sp-500-index/) illustrates the scale. From 1980 to 2020 (40 years):

- **S&P 500 Price Index:** Roughly 13.5× (annualized ~6.1%)
- **S&P 500 Total Return Index:** Roughly 50× (annualized ~9.3%)

The difference is staggering. A $10,000 investment tracking price-only would grow to ~$135,000. Tracking total return grows to ~$500,000. Dividends accounted for roughly **two-thirds of the total return** over that period.

This ratio varies by market, era, and sector. Technology stocks pay sparse dividends, so price and total return indices diverge slowly. Utility stocks or REITs pay high yields, so the gap widens quickly. In bull markets, price appreciation dominates; in sideways or bear markets, dividends make up lost ground.

## Why this matters for comparing funds

Most [index-fund](/index-fund/) prospectuses quote total return because that's what investors actually capture. An [active-etf](/active-etf/) or [mutual-fund](/mutual-fund/) claiming to beat the market is benchmarked against a total return index. If the index only counted prices, the fund would appear to outperform even if it merely matched the index plus collected fees.

Conversely, if you're comparing two funds on your own, ensure you use the same denominator. Comparing Fund A (tracking total return) against a price index will make Fund A look artificially strong.

For [tax-loss-harvesting](/tax-loss-harvesting/) and [form-8949](/form-8949/) calculations, you need the actual cash flows (dividends and capital gains separately), not the blended total return. But for buy-and-hold performance measurement, total return is the right lens.

## The reinvestment assumption

Total return indices assume dividends are reinvested tax-free and with zero friction. In reality, there are costs: broker fees (minimal today), bid-ask spreads, and crucially, income tax. A taxable investor doesn't get to reinvest $1 of dividends; they get to reinvest maybe $0.75–$0.85, depending on tax bracket. A [tax-bracket-investor](/tax-bracket-investor/) in a 37% bracket reinvests only $0.63 per dollar of dividend.

This is why [roth-ira](/roth-ira/) and [401k-plan](/401k-plan/) returns tend to exceed taxable account returns even for the same index—the tax-free reinvestment in retirement accounts compounds faster.

Total return index figures are *not* an investor's personal experience unless they hold the assets in a tax-sheltered account and pay no trading costs.

## Price index use cases

Price indices are mostly used for:

1. **Historical comparison.** Analysts sometimes cite the price index to isolate capital appreciation (separating the stock market's "real" growth from the income it generated).

2. **Momentum and technical analysis.** Traders care about price action, not dividends, so price indices can feel more relevant to short-term trading.

3. **Commodity indices.** Commodities like [crude-oil](/crude-oil/) or [copper](/copper/) don't pay dividends, so price and total return are the same.

4. **Institutional hedging.** Some equity derivatives and index options are struck on price indices, a legacy of older market infrastructure.

But for long-term portfolio performance tracking and fund evaluation, total return is the standard.

## Index-by-index comparison

Most major indices publish both versions:

- **US large-cap:** S&P 500 (price and total return available)
- **US broad market:** Nasdaq Total Market Index, Wilshire 5000 (both versions)
- **Bonds:** Bloomberg Aggregate Bond Index (total return, as reinvested coupons are critical)
- **International:** MSCI World (price and net total return; "net" means dividends taxed at withholding rates)

A [index-fund](/index-fund/) tracking the S&P 500 typically trails the price index slightly (due to fees) and matches or slightly lags the total return index. If the fund holds the exact same stocks but lags total return by more than 0.1–0.2% annually, expenses and trading costs are eating performance.

## See also

<div class="wiki-seealso">

### Closely related

- [Index Fund](/index-fund/) — passively managed funds that track indices, using total return as the performance benchmark
- [Dividend](/dividend/) — the cash payment underlying the gap between price and total return
- [Dividend Distribution](/dividend-distribution/) — mechanics of how dividends are paid and reinvested
- Total Return — the combined impact of price and income
- [SP 500 Index](/sp-500-index/) — the most widely tracked US large-cap benchmark

### Wider context

- [Return on Assets](/return-on-assets/) — measuring investment performance more broadly
- [Tax Loss Harvesting](/tax-loss-harvesting/) — strategy that relies on understanding realized vs. total returns
- [Actively Managed Fund](/actively-managed-fund/) — alternatives benchmarked against total return indices
- [Roth IRA](/roth-ira/) — account type where tax-free compounding maximizes total return advantage

</div>
