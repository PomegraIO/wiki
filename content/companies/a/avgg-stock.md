---
title: "Leverage Shares 2X Long AVGO Daily ETF (AVGG)"
description: "A leveraged single-stock ETF targeting 2X the daily return of Broadcom using total return swap contracts, designed for tactical trading rather than long-term holding."
keywords:
  - leveraged ETF
  - single-stock leverage
  - Broadcom
  - daily reset
  - volatility decay
  - swap contract
handwritten: true
---

*The Leverage Shares 2X Long AVGO Daily ETF is an exchange-traded fund that seeks to deliver twice the daily return of Broadcom shares. Rather than buying Broadcom stock on margin, it achieves leverage through a derivative contract with a bank counterparty — a structure designed for traders making short-term bets, not long-term investors.*

<aside class="wiki-infobox">
<table>
<tr><th>Ticker</th><td>AVGG (NASDAQ)</td></tr>
<tr><th>Sponsor</th><td>Leverage Shares (UK/EU-based)</td></tr>
<tr><th>Type</th><td>Leveraged single-stock ETF</td></tr>
<tr><th>Underlying</th><td>Broadcom Inc. (AVGO)</td></tr>
<tr><th>Leverage</th><td>2X daily return</td></tr>
<tr><th>Mechanism</th><td>Total return swap with bank counterparty</td></tr>
<tr><th>Reset</th><td>Daily, midnight UTC</td></tr>
</table>
</aside>

## The swap structure

AVGG does not borrow cash to buy Broadcom shares on margin. Instead, Leverage Shares enters a total return swap — a contract with a large bank. Under this swap, the bank agrees to pay AVGG twice Broadcom's daily return, and AVGG pays the bank a financing cost plus a spread. The bank then hedges itself by purchasing Broadcom shares and financing them through its own borrowing.

This arrangement removes AVGG from the traditional margin-borrowing ecosystem. Instead of AVGG holding the stock directly, the fund holds a contractual claim on Broadcom's return. The advantage is simplicity — the swap is embedded in the fund structure and requires no active margin management from the investor. The disadvantage is that the cost of the swap (the financing rate and the bank's spread) is embedded in the fund's expense ratio and creates drag.

The financing cost varies with short-term interest rates. When the Federal Funds Rate is low, financing is cheap and decay is modest. When rates are high, financing costs spike and returns suffer. This makes AVGG's cost dependent on macroeconomic conditions beyond Broadcom's own performance.

## Daily resets and compounding losses

AVGG rebalances every trading day to lock in its 2X leverage ratio. This daily reset is where long-term investors encounter a mathematical trap called volatility decay.

The trap works like this. Suppose Broadcom starts at $100 and AVGG starts at the same $100. Broadcom rises 10% to $110. AVGG, targeting 2X the daily return, rises 20% to $120. The next day, Broadcom falls 10% (from $110 to $99). AVGG falls 20% (from $120 to $96). The investor in Broadcom lost $1 (1% loss). The investor in AVGG lost $4 (4% loss) on a stock that only fell 1% total.

This decay accelerates with volatility. The same gain-then-loss sequence, when it happens over weeks, erodes the fund substantially — even if the underlying stock rises overall. If Broadcom swings 2–3% per day (common for semiconductors), AVGG loses 2–4% per day to decay alone, regardless of Broadcom's net direction.

The mathematics are unkind to buy-and-hold. A trader holding AVGG overnight or for a few days while making a directional bet can profit from the leverage without accumulating much decay. An investor holding for months or years will see a large fraction of gains consumed by compounding losses in the daily reset cycle.

## Concentrated risk and counterparty exposure

AVGG offers zero diversification. The entire investment is a leveraged bet on Broadcom — a semiconductor company exposed to cyclical demand, intense competition from AMD and NVIDIA, geopolitical trade risks, and the execution complexity of managing fabs and chip design.

Leverage concentrates that risk. If Broadcom falls 50%, AVGG will lose close to 100% of value (less any daily rebalancing mechanics, but the outcome is near-total loss). That is not a possibility; it is the structural outcome of 2X leverage on a single name if the name declines sharply enough.

There is also counterparty risk. The bank providing the swap is exposed to AVGG's potential losses, and AVGG investors are exposed to the bank's creditworthiness. The swap should be collateralized, but in financial crises, collateral values can evaporate faster than expected. Even systemically important banks have faced solvency questions during market dislocations.

## Mechanical trading and fees

AVGG trades throughout the day on NASDAQ like any stock, with tight bid-ask spreads in normal markets. Settlement is immediate, and there is no friction to buying or selling — that makes it accessible to retail traders.

The expense ratio is typically 0.9% to 1.4% annually. On top of that, the embedded swap financing costs add another 1–2% per year in drag. For a fund designed to last days or weeks, that cost is acceptable. For a fund held a year or more, the cumulative drag becomes substantial.

AVGG does not pay dividends. The total return swap captures Broadcom's dividend, but it is reinvested rather than distributed — avoiding the tax inefficiency of dividend payments to a leveraged holder.

## Market conditions and return assumptions

AVGG's performance depends critically on what Broadcom does and how volatile it is. In a calm month where Broadcom rises 5% without swinging wildly day to day, AVGG will rise roughly 10% minus fees. Decay is minimal.

In a volatile month where Broadcom swings 2–3% per day, accumulating a 5% gain or loss, AVGG will underperform 2X leverage substantially because the daily resets cost more. That is when the structural weakness of the product surfaces.

The product is also sensitive to interest rates. The swap financing cost is typically pegged to SOFR or similar overnight funding rates. When the Federal Reserve is hiking and rates are rising, AVGG's embedded cost rises, reducing returns further.

## Appropriate uses and risks

AVGG is a tactical instrument. A trader who believes Broadcom will rise 10% in the next two weeks can use AVGG to make a leveraged directional bet without learning options or opening a margin account. If the thesis plays out quickly, the leverage works.

AVGG is inappropriate for buy-and-hold investors who think Broadcom is great and want leverage. Decay and costs will erode returns over months, even if Broadcom rises. It is also inappropriate for uncertain theses or for investors who cannot psychologically tolerate seeing the fund to zero if Broadcom crashes.

For investors who want Broadcom leverage over longer horizons, owning AVGO directly and using call options, or spreading leverage across multiple holdings, or using a traditional margin account, is often clearer and cheaper than AVGG's all-in-or-nothing bet.

## Due diligence for users

Read the prospectus carefully. Understand the swap counterparty, the collateral arrangements, and the method for calculating the financing cost. The financing cost formula is critical — if it is tied to SOFR plus a wide spread, the fund will be expensive in a rising-rate environment.

Compare AVGG's returns to 2X of Broadcom's returns over rolling periods. In calm months, decay should be minimal. In volatile months, decay should be substantial. Measure this gap and price it into your decision.

If you use AVGG, hold it for days or weeks, not months. Monitor Broadcom's competitive position, earnings, and semiconductor cycle continuously — you are making a tactical, levered bet on near-term execution, not a passive position.
