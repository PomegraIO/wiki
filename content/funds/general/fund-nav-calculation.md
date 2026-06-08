---
title: "How Fund NAV Is Calculated"
description: "Step-by-step explanation of net asset value calculation: asset valuation, liability deduction, and share division that determines the per-share fund price."
keywords:
  - how is fund nav calculated
  - net asset value calculation
  - fund nav formula
  - fund valuation daily
  - per share price calculation
image: "/svg/funds.svg"
---

*The **net asset value (NAV) per share** of a fund is calculated by a simple formula: total fund assets minus liabilities, divided by the number of outstanding shares. This daily calculation determines the exact price you pay when buying or the proceeds you receive when selling an [open-end fund](/open-end-vs-closed-end-fund/). Understanding the formula and its components reveals why NAV changes every business day and why it matters.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fund NAV Calculation — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A daily mechanical calculation that determines the exact price per fund share.</div>

|   |   |
|---|---|
| **Formula** | (Total Assets − Total Liabilities) ÷ Outstanding Shares |
| **Timing** | Calculated once daily, typically after market close (4 p.m. ET) |
| **Frequency** | Every business day for open-end funds; less frequent for closed-end funds |
| **Who performs it** | Fund transfer agent or administrator |
| **Uses** | Purchase price, redemption price, expense ratio baseline |
| **Precision** | Typically calculated to four decimal places (e.g., $23.4567) |
| **Valuation method** | Market prices for liquid holdings; valuation models for illiquid holdings |

</aside>

## The NAV formula broken down

The formula is straightforward:

**NAV per Share = (Total Assets − Total Liabilities) / Outstanding Shares**

For example, suppose a fund has:
- Total securities holdings: $500 million
- Cash and equivalents: $10 million
- Total assets: $510 million

And:
- Accrued management fees: $1 million
- Other liabilities: $0.5 million
- Total liabilities: $1.5 million

With 50 million shares outstanding:

NAV = ($510M − $1.5M) / 50M shares = $508.5M / 50M = $10.17 per share

Every investor holding shares of this fund owns a piece of that $508.5 million net asset pool. If you hold 1,000 shares, you own approximately 0.002% of the fund's net assets, or roughly $10,170.

## What goes into "total assets"

The main component is the fund's portfolio of securities—stocks, bonds, commodities, derivatives—at their current market value.

**Equity holdings** are valued at the closing price on the exchange where they trade. If the fund owns 100,000 shares of Apple, and Apple closes at $180, that position is worth $18 million.

**Bond holdings** are more complex. Bonds don't always trade every day. The fund values them using pricing services that blend recent transaction prices, dealer quotes, and valuation models. A corporate bond might be marked to "mid-market," the midpoint between what dealers would pay and what they'd ask.

**Cash and money market instruments** are valued at face value (principal plus accrued interest).

**Derivatives** (options, futures, swaps) are marked to market using pricing models based on underlying asset prices.

**Illiquid holdings** (private equity, some alternatives) are valued using internal models or independent appraisers. This is where subjectivity enters NAV. A private company's value is estimated, not observed, and different valuations could be defensible.

**Foreign holdings** are converted to the fund's home currency using the exchange rate at the valuation time.

For example, if a fund holds Japanese stocks, the yen price is converted to US dollars using the closing yen/dollar rate. If the yen appreciates, the dollar value of those holdings rises even if the stock prices in yen don't change.

## What goes into "total liabilities"

This is often overlooked but essential.

**Accrued management fees** are the largest liability. If the fund charges 0.50% annually and the NAV before fees is $1 billion, the fund accrues roughly $1.37 million per day in management fees. This amount is subtracted from the fund's NAV continuously, reducing the per-share value.

**Distribution payables** are dividends or capital gains declared but not yet paid. The day after ex-dividend date, the fund's liability increases and NAV per share drops by approximately the dividend per share.

**Accrued administrative costs** include custodial fees, audit costs, and regulatory fees.

**Borrowings** appear here if the fund uses leverage.

**Accounts payable** for transactions pending settlement.

Unlike assets, which are updated minute-by-minute in real time, liabilities accrue over days or months and are incorporated into the single daily NAV calculation.

## When NAV is calculated

For most open-end mutual funds, NAV is calculated once per day, typically after the US stock market closes at 4 p.m. Eastern Time. All buy and sell orders received that day are executed at that single NAV price, regardless of when during the day the order was placed.

If you place a buy order at 10 a.m., 2 p.m., or 3:59 p.m., you pay the NAV calculated at 4 p.m. This is different from stock trading, where you see a live price and execute immediately.

ETFs calculate NAV continuously throughout the trading day, updated every few seconds. This frequent updating is one reason [ETFs](/etf/) can trade on exchanges while traditional mutual funds cannot.

Closed-end funds trading on exchanges show a market price that differs from their NAV. The fund calculates NAV daily (usually after market close), but the market price reflects ongoing trading. The premium or discount emerges from this mismatch.

## Valuation challenges and estimates

For most holdings, NAV is mechanical. But certain assets require judgment:

**Illiquid securities** in a fund might include thinly traded bonds or private investments. The fund's valuation committee or administrator estimates fair value using models, recent sales of similar assets, or broker quotes. This estimate is sometimes called a "fair value adjustment." If two funds hold similar private assets, they might assign different values, leading to different NAVs for essentially the same portfolio.

**International holdings** expose funds to currency risk. The fund values foreign stocks in the foreign currency's closing price, then converts to dollars. If the dollar strengthens unexpectedly overnight, the NAV might drop not because the stock fell but because the exchange rate moved.

**Distressed securities** might be valued well below their nominal value. The fund's pricing service estimates recovery value or uses observable trades of comparable debt.

Most funds use standardized pricing providers (Interactive Data, Thomson Reuters, Bloomberg) that apply consistent methodologies. But for unique or distressed assets, judgment unavoidably enters NAV.

## How NAV relates to fund expense ratios and management fees

The [expense ratio](/expense-ratio/) is expressed as a percentage of assets under management. A fund with a 0.50% expense ratio deducts 0.50% of NAV per share annually.

This deduction happens continuously. Each day, the accrued daily management fee (1/365th of the annual rate) is included in the NAV calculation, reducing the per-share value. Over a year, these daily reductions add up to the stated expense ratio.

If a fund's holdings earn 8% but the expense ratio is 0.50%, the fund's NAV grows at approximately 7.50%.

## Small-number precision and rounding

NAVs are calculated to many decimal places—typically four (e.g., $23.4567). When you buy or sell, the price might be rounded to the nearest cent for your statement, but the fund's internal accounting uses full precision.

This precision matters for large transactions. If an institution redeems $100 million, the difference between $23.4567 and $23.46 could be thousands of dollars.

## Example: A day in a fund's NAV calculation

Suppose it's the last trading day of the week for a diversified equity fund:

1. **11:59 a.m. ET:** The fund's stock positions are worth $2.005 billion at real-time prices. Cash is $45 million. Estimated total assets: $2.050 billion.

2. **4:00 p.m. ET (market close):** The stock market closes. Final closing prices update the portfolio value to $2.010 billion. Cash is still $45 million. Total assets: $2.055 billion.

3. **4:15 p.m. ET:** The transfer agent calculates liabilities:
   - Accrued management fees (0.07% daily on $2.055B): $0.144 million
   - Distribution payable (announced quarterly dividend): $2 million
   - Total liabilities: $2.144 million

4. **Net assets:** $2.055B − $2.144M = $2.052.856 billion

5. **Outstanding shares:** 200 million

6. **NAV per share:** $2,052.856M / 200M = $10.26428

7. All orders placed during the day settle at $10.26.

If a shareholder buys $10,000 worth, they receive 973.99 shares (or the fractional equivalent their fund allows).

## See also

<div class="wiki-seealso">

### Closely related

- [Net Asset Value](/net-asset-value/) — the broader concept and its role in fund pricing
- [Fund Expense Ratio Explained](/fund-expense-ratio-explained/) — how ongoing costs reduce NAV
- [Open-End vs Closed-End Fund](/open-end-vs-closed-end-fund/) — why NAV calculation differs between structures
- [Fund of Funds Fee Drag](/fund-of-funds-fee-drag/) — how layered funds affect NAV calculations
- [Fair Value](/fair-value/) — methodologies used to value illiquid holdings in NAV

### Wider context

- [Mutual Fund](/mutual-fund/) — the primary vehicle using daily NAV calculations
- [ETF](/etf/) — uses continuous NAV updates instead of once-daily
- Asset Valuation — broader principles underlying the calculation
- [Transfer Agent](/transfer-agent/) — administrative entity that performs NAV calculations
- [Custodian](/custodian/) — safeguards assets that feed into NAV

</div>
