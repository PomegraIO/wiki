---
title: "How Mutual Fund NAV Is Calculated at End of Day"
description: "How is mutual fund NAV calculated: total assets minus liabilities divided by shares outstanding, priced at market close each trading day."
keywords:
  - how mutual fund nav calculated
  - net asset value calculation
  - fund valuation
  - end-of-day pricing
  - fund share price
  - nav formula
  - daily redemption pricing
---

*The **net asset value (NAV)** of a mutual fund is calculated once daily, after the market closes, using a simple formula: total assets minus total liabilities, divided by the number of shares outstanding. All investors who submit orders before the 4 PM ET cutoff receive that day's closing NAV, regardless of when during the day they placed their trade.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">NAV Calculation — key facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">One price per day for all investors is the standard; orders before cutoff share that price.</div>

|   |   |
|---|---|
| **Formula** | (Total Assets − Total Liabilities) ÷ Shares Outstanding |
| **Calculation timing** | Once daily, after US market close (4 PM ET) |
| **Order cutoff** | Orders submitted by 4 PM ET settle at that day's NAV |
| **What assets include** | Stocks, bonds, cash, dividends received but not yet paid |
| **What liabilities include** | Operating expenses accrued, management fees, accrued payables |
| **Valuation method** | Mostly market prices; illiquid securities at fair value |
| **Same price for all buyers** | Yes—all orders before cutoff receive the same closing NAV |

</aside>

## The basic formula

A mutual fund's [net asset value](/net-asset-value/) is the value of one share. It's calculated by taking everything the fund owns, subtracting everything it owes, and dividing by the total number of shares in circulation.

NAV = (Total Assets − Total Liabilities) ÷ Number of Shares Outstanding

If a fund holds $100 million in stocks and bonds, carries $1 million in accrued management fees and operating expenses, and has 10 million shares outstanding:

NAV = ($100,000,000 − $1,000,000) ÷ 10,000,000 = $9.90

Each share is worth $9.90. Someone buying shares gets $9.90 shares per dollar; someone selling redeems at $9.90.

## What counts as assets

Total assets include everything of value the fund holds:

- **Stocks and bonds**: marked to the market price at close on the valuation date.
- **Cash and cash equivalents**: bank deposits, Treasury bills, money-market holdings.
- **Accrued income**: dividends that have been announced and are due but not yet received; interest earned but not yet paid.
- **Securities purchased but not yet settled**: if the fund buys a stock trade on a T+1 basis (settles the next day), it counts as an asset on the valuation date.

Notably, the market price used is the closing price on the valuation date. If a stock is worth $50 at market close, the fund values its shares at $50, period. Prices from pre-market or after-hours trading are not used.

For most holdings—stocks and bonds on major exchanges—the closing price is objective and real-time. The fund's pricing service (often a third-party vendor like Interactive Data or Bloomberg) pulls the closing prices automatically.

For less liquid securities—emerging-market bonds, illiquid private securities, or securities with no recent trade—the fund uses a "fair value" estimate. A committee of fund managers and advisers, sometimes in consultation with pricing vendors, estimates what the security would trade for if a buyer and seller were present. This is more subjective and allows for honest disagreement, but it is required by regulation to be reasonable and in good faith.

## What counts as liabilities

Total liabilities include amounts the fund owes:

- **Accrued management fees**: the portion of the annual [expense-ratio](/expense-ratio/) that has accrued since the last payment.
- **Accrued operating expenses**: custodian fees, transfer agent fees, audit fees, legal fees that have been incurred but not yet paid.
- **Payables for securities sold**: if the fund has sold securities that have not yet settled, it records a payable for the sale proceeds due back to the seller.
- **Payables to shareholders**: if the fund is distributing a dividend or capital gain, the fund records the liability as it accrues (even before the payment date).

These liabilities are usually small relative to assets—perhaps 0.01% to 0.05% of total assets on any given day. But they reduce the value available to shareholders, so they are subtracted from assets before dividing by shares.

## Timing: once daily, market close

NAV is calculated exactly once per trading day, after the US stock market closes at 4:00 PM Eastern Time. For a domestic stock fund holding US-traded securities, this is straightforward: at 4 PM, the market closes, final prices are set, the fund's pricing service pulls those prices, liabilities are confirmed, and the NAV is calculated.

For an international fund holding securities in Tokyo, London, or Hong Kong, the timing is trickier. The Japanese market closes at 3 AM ET the next day, well after the fund's 4 PM close. The fund must use the previous day's closing price for Japanese holdings or wait until the next business day (delaying NAV calculation) to use more current prices. Most funds use the latest available prices and note the timing difference in their prospectus.

On non-trading days (weekends and holidays), the fund does not calculate NAV. There is no NAV on a Saturday or on Thanksgiving. Orders submitted on a non-trading day are held and processed at the next business day's NAV.

## Orders before 4 PM: same NAV

All orders to buy or sell mutual fund shares submitted before 4 PM ET are executed at that day's closing NAV. It doesn't matter if you submit your order at 9:30 AM or 3:59 PM—you get the same price. This is known as "forward pricing," and it's a legal requirement for open-end mutual funds in the United States.

Forward pricing serves investors. It prevents timing arbitrage and ensures that all shareholders are treated identically. If the fund's price was updated continuously (as [ETF](/etf/) prices are), early-day buyers might have a minute-to-minute advantage over late-day buyers, and market-moving news during the day could create perverse incentives. By locking everyone into a single daily price, forward pricing is fair.

The mechanism works because a mutual fund is not traded on an exchange. The fund itself manages share creation and redemption. When you buy, the fund creates new shares at NAV. When you redeem, the fund cancels shares at NAV. The fund is both the market maker and the issuer.

An order placed at 3:59 PM, one minute before the cutoff, receives that day's NAV. An order placed at 4:01 PM, one minute after, is held and executed at the next business day's NAV. Some investors misunderstand this and think they can "lock in" a price by submitting an order seconds before close. They cannot; the cut-off is absolute.

## Valuation dates and corporate actions

On the valuation date (the close of each trading day), the fund snapshots its holdings. Dividends declared as of close are counted as assets (accrued income). Stock splits or other corporate actions are reflected immediately.

If a stock splits 2-for-1 between one valuation date and the next, the fund adjusts its holdings and NAV accordingly. The fund doesn't buy or sell; it simply updates the count of shares held and the price per share.

If a dividend is paid on a specified record date, the fund's NAV drops on that date by the dividend amount per share (assuming nothing else changes). A fund with NAV of $10 that distributes a $0.50 per-share dividend ex-dividend drops to $9.50 on the ex-date, all else equal. This is automatic and reflects the fact that the dividend is now gone from the fund (it has been paid to shareholders).

## Fair value and gate mechanisms

For most funds, NAV is calculated using market prices because most holdings are liquid and actively traded. But some funds invest in securities that are hard to value—emerging-market equities, high-yield bonds, illiquid alternatives, or direct private equity holdings.

For these securities, the fund uses a fair-value committee process. Managers and valuations experts estimate a price based on similar trades, fundamentals, and comparable securities. The process is subjective but required by regulation to be reasonable. The fund's prospectus discloses the methodology.

Some funds that experienced large outflows (especially alternative or hedge-fund-like funds) have invoked "gating" or "side-pocket" provisions—temporarily restricting redemptions or locking some assets away—when fair valuation becomes so difficult that redeeming at NAV would harm remaining shareholders. This is rare in mainstream mutual funds and is disclosed in the prospectus.

## Impact on investors

For buy-and-hold investors, the NAV calculation matters less directly. You buy at one NAV, hold for years, and redeem at a future NAV. The calculation is accurate and fair, and you move on.

For active traders or those rebalancing, the NAV calculation has two practical implications:

1. **Order timing doesn't matter (before 4 PM)**: whether you trade at 9:30 AM or 3:59 PM, you get the same price. There's no first-mover advantage.
2. **After-hours trades are next-day**: if you submit an order after 4 PM, it settles at tomorrow's NAV, not today's. Don't be surprised if overnight news changes the price.

For funds holding illiquid or hard-to-value assets, understand that NAV is an estimate, and the estimate can be off. The fund manager's fair-value opinion is reasonable but not certain. This is why funds with complex holdings disclose their valuation policies in detail.

## See also

<div class="wiki-seealso">

### Closely related

- [Net Asset Value](/net-asset-value/) — the NAV itself and why it matters
- [Mutual Fund](/mutual-fund/) — structure and mechanics
- [Fund Prospectus](/fund-prospectus/) — where valuation policies are disclosed
- [Expense Ratio](/expense-ratio/) — ongoing costs factored into NAV
- [ETF](/etf/) — continuous intraday pricing vs. daily mutual fund NAV

### Wider context

- [Mutual Fund Minimum Investment](/mutual-fund-minimum-investment/) — investment amounts
- [Mutual Fund Redemption Fee](/mutual-fund-redemption-fee/) — exit costs
- [Index Fund](/index-fund/) — passive fund structure
- [Capital Gains Tax Investor](/capital-gains-tax-investor/) — distribution timing
- [Mutual Fund vs ETF in a Taxable Account](/mutual-fund-vs-etf-for-taxable-account/) — pricing and tax implications

</div>
