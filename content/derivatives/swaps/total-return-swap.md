---
title: "Total Return Swap"
description: "A swap where one party pays all returns (price appreciation plus dividends) on an asset in exchange for a fixed or floating payment from the other party."
---

*A total return swap (TRS) is a contract where Party A pays the total return (price appreciation, dividends, and other distributions) on an asset to Party B, and Party B pays Party A a fixed or floating interest rate. Party B gains the economic benefit of owning the asset without owning it legally, while Party A monetizes the return and locks in a funding cost.*

## Why total return swaps exist and how they differ from equity swaps

Total return swaps and [equity swaps](/wiki/equity-swap/) are nearly identical in structure and are often used interchangeably. The distinction is subtle:

- An **equity swap** traditionally refers to swaps on a single equity security or broad index.
- A **total return swap** is a broader category that can be written on any underlying asset: equities, bonds, commodities, loans, or entire portfolios.

In practice, the terms are used loosely. A total return swap on a stock is an equity swap. A total return swap on a corporate bond is called a bond TRS and is common in credit markets. The economic mechanics are identical: one party delivers all returns, the other pays financing.

## Structure

**Total return leg**: Party A (usually the asset owner or credit payer) delivers all cash flows and price appreciation from the underlying asset to Party B. If the asset is a bond, Party A pays coupon interest, principal repayment, and any loss from credit deterioration. If the asset is a stock, Party A pays the price appreciation and dividends.

**Financing leg**: Party B (usually the capital provider) pays a fixed or floating interest rate (e.g., SOFR + spread) to Party A.

Settlement occurs periodically (monthly, quarterly) or at maturity. If the asset gains value, Party A sends the gain to Party B. If the asset loses value, Party B sends the loss to Party A.

## Common structures by underlying asset

**Equity TRS**: One party (the hedge fund, long-only investor) pays the return on a stock or equity index; the other party (the bank) pays SOFR + spread. The hedge fund gets leverage without margin. The bank gets a small, reliable financing income.

**Bond TRS**: A bank or dealer holds a corporate bond on its balance sheet. The bank enters a TRS to transfer the credit risk and other risks to an investor. The investor pays the bank financing costs and receives all bond returns (coupons and principal). If the bond defaults, the investor bears the loss. The bank sheds the risk and frees up capital.

**Loan TRS**: A bank originates a leveraged loan to a borrower but doesn't want to hold the credit risk. The bank enters a TRS with a loan investor. The investor "owns" the return on the loan without being the legal lender.

**Portfolio TRS**: A bank or asset manager holds a portfolio of securities and enters a TRS on the entire portfolio to transfer risk. The counterparty bears market risk, credit risk, and operational risk on every holding.

## Why bond TRS is popular in credit markets

**Balance sheet relief**: A bank that holds a $100 million corporate bond bond for regulatory capital. If the bank enters a TRS, it can pay away the credit risk and the bond appreciation risk, freeing up capital for other uses.

**Credit insurance alternative**: Instead of buying a [credit default swap](/wiki/credit-default-swap/) (CDS), which only covers default risk, a bond TRS covers all risks: default, deterioration, and gain/loss from mark-to-market. This is more complete insurance.

**Yield enhancement**: An asset manager that holds a low-yielding bond can enter a TRS to enhance yield. The manager receives the bond's coupon plus the benefit of any price appreciation, minus the financing cost. If the spread between bond yield and financing cost is attractive, the manager profits.

## Uses

**Leverage**: A hedge fund wants $200 million of Microsoft exposure but has only $20 million. It enters a TRS on Microsoft (notional $200 million) with a bank, paying SOFR + 50 bps and receiving the total return. This gives the hedge fund leveraged exposure with minimal capital.

**Financing**: A company that owns an asset (e.g., real estate, equipment) enters a TRS to monetize the asset without selling it. The company receives financing cash upfront and pays the buyer the asset's returns.

**Credit hedging**: A bank holds a bond and fears the issuer's credit will deteriorate. The bank enters a TRS on the bond, transferring the risk to an investor. The bank keeps the interest income (if structured that way) but transfers market risk.

**Exposure monetization**: A private equity fund holds a stake in a private company. The fund enters a TRS on a comparable public company stock to monetize the exposure without selling the private stake. The fund pays returns on the public stock and receives financing; the net effect is similar to a short against a box hedge.

## Valuation and pricing

A TRS is valued as the sum of:

1. **Underlying asset present value**: The expected cash flows and price appreciation, discounted at the appropriate rate (equity risk premium for stocks, credit spread for bonds).

2. **Financing leg present value**: The expected financing payments, discounted at the risk-free rate.

3. **Solving for the fixed rate**: The financing rate is set so the two legs have equal present value at inception.

For a bond TRS, the financing rate often reflects:
- SOFR (risk-free rate).
- A credit spread (compensation for [counterparty risk](/wiki/counterparty-risk/)).
- A small "fee" (e.g., 5-10 bps) that the TRS dealer earns.

For an equity TRS, the rate reflects SOFR + a spread that depends on the [cost of carry](/wiki/cost-of-carry/) (the stock lender's fee, dividend yield, repo rate) and the dealer's credit spread.

## Risks

**Leverage risk**: For the total return payer (the long party), losses are amplified. A 10% decline in the underlying asset, applied to a $200 million notional, is a $20 million loss. For a $20 million capital base, that is 100% loss of capital.

**Counterparty risk**: The financing leg is only as good as the counterparty. If a bank offers very cheap financing in a TRS, but then fails, the total return payer loses the financing source and must unwind at an inopportune time.

**Mark-to-market risk**: If the underlying asset declines, the total return payer must pay the loss to the financing party. Daily or periodic mark-to-market creates cash flow volatility.

**Funding risk**: If the financing rate is floating, the cost can rise sharply. A hedge fund that locked in SOFR + 50 bps faces a much higher cost if SOFR spikes.

**Liquidity risk**: If the underlying asset is illiquid (e.g., a small-cap stock, a loan, a private equity stake), valuing and exiting the TRS is difficult.

**Basis risk**: For a portfolio TRS, the financing rate is fixed for the entire portfolio, but individual assets might have different risk profiles. The portfolio might outperform on average but individual holdings might underperform.

## Mechanics and settlement

Most TRS settle monthly or quarterly with net cash flows:

- If the asset gained $1 million in value and the financing cost is $500k for the period, the total return payer sends the net $500k to the financing party.
- If the asset lost $1 million and the financing cost is $500k, the financing party sends the total return payer $1.5 million.

For long-dated or complex TRS, dealers use collateral management ([repo](/wiki/repurchase-agreement/)) to reduce counterparty risk. The counterparty posting a collateral pool protects the TRS payer against default.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the foundational derivative.</li>
<li><a href="/wiki/equity-swap/">Equity swap</a> — the same structure applied to equities.</li>
<li><a href="/wiki/credit-default-swap/">Credit default swap</a> — covers credit risk; TRS covers all risks.</li>
<li><a href="/wiki/repurchase-agreement/">Repurchase agreement</a> — a funding mechanism often used with TRS.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/leverage/">Leverage</a> — the main benefit of total return swaps.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the primary risk in OTC swaps.</li>
<li><a href="/wiki/cost-of-carry/">Cost of carry</a> — determines the financing cost in TRS on equities.</li>
<li><a href="/wiki/mark-to-market/">Mark-to-market</a> — used for periodic cash settlement.</li>
</ul>
</div>
