---
title: "Put Option (Equity)"
description: "Shareholder right to force a company to repurchase shares, often embedded in preferred stock."
keywords:
  - put option
  - shareholder rights
  - redemption rights
  - preferred stock
  - equity compensation
---

*A **put option (equity)** is a shareholder right to force a company to repurchase shares at a specified price and date. Unlike the financial derivative [put option](/wiki/put-option/) (which is tradeable), an equity put is embedded in a security—usually [preferred stock](/wiki/preferred-stock/)—and grants the holder a claim on the issuer's balance sheet.*

<aside class="wiki-infobox">

| Feature | Detail |
|---|---|
| **Holder's right** | Sell shares back to issuer at strike price |
| **Issuer's obligation** | Repurchase at the specified terms |
| **Common structure** | Redeemable/putable preferred stock |
| **Strike price** | Usually par value or cost basis |
| **Maturity** | 3–10 years (varies by security) |
| **Trigger** | Change of control, IPO, specified date |
| **Cash requirement** | Company must have cash or credit to repurchase |
| **Accounting treatment** | Often marked as liability, not equity |

</aside>

## How an equity put works

A venture-backed company issues 1 million shares of **Series A Preferred Stock** at $10/share to an investor. The terms include:

- **Coupon/dividend** — 8% annual preferred dividend
- **Put option** — shareholder can require the company to repurchase shares at $10/share on January 1, 2030 (8 years hence)
- **Conversion right** — can convert to common stock if company goes public at a high valuation

The investor has a claim: if the company stalls and doesn't exit by 2030, the investor can force a repurchase, recovering the $10/share investment plus accrued dividends. This protects against indefinite illiquidity.

## Motivation: protecting investors from dead companies

Equity puts are a contractual shield against the scenario where:
- A [startup](/wiki/venture-capital-fund/) raises capital, spends it, and fails to achieve its milestones
- The company doesn't fail catastrophically (bankruptcy) but slowly declines
- The investors are trapped holding illiquid shares worth a fraction of cost
- There is no [acquisition](/wiki/acquisition/) or [IPO](/wiki/initial-public-offering/), and the company never pays a dividend

The put option forces a resolution: either the company succeeds (pays the dividend, gets [acquired](/wiki/acquisition/), or goes public), or the investor can force a cash return.

## Legal mechanics: redemption rights

Equity puts are often called **redemption rights** or **repurchase rights**. The key distinction from financial [put options](/wiki/put-option/):

| Feature | Financial Put | Equity Put |
|---|---|---|
| **Trading** | Tradeable on exchanges | Usually illiquid, attached to stock |
| **Strike** | Market-determined | Contractually specified |
| **Counterparty** | Seller (unknown) | Issuing company |
| **Liquidity** | High | Low (dependent on issuer's cash) |
| **Obligation** | Can be exercised by buyer | Can be exercised by holder; triggers balance-sheet impact |

## Cash drain and accounting treatment

When a put option is exercised, the issuer must pay cash to buy back the shares. For a company with thin margins or negative cash flow, this is a significant drain.

**Accounting rules** (under GAAP and IFRS) often require companies to **classify putable preferred stock as a liability**, not equity. This is because the company has an obligation to repurchase, not a permanent equity base. A company's [balance sheet](/wiki/balance-sheet/) might show:

```
Assets: $50M
Liabilities: $20M (including $10M putable preferred)
Equity: $30M
```

When the put is exercised, cash decreases and the liability disappears, but the company's equity takes the full hit. If cash is insufficient, the company may need to restructure or seek emergency financing.

## Put option triggers

Equity puts can be triggered by:

1. **Specified date** — "On January 1, 2030, shareholder may put shares to issuer"
2. **Change of control** — "If acquired for less than $X per share, investor can put shares at par"
3. **IPO failure** — "If company doesn't IPO by 2035, shares revert to issuer at strike price"
4. **Non-performance** — "If cumulative revenue misses guidance by 50%, put is triggered"

The most common is the **specified date** put, which is a backstop if the company stalls.

## Strategic negotiation points

In [preferred stock](/wiki/preferred-stock/) [financing](/wiki/venture-capital-fund/) rounds, entrepreneurs and investors negotiate put terms:

- **Investors want** — low strike price, short window, broad triggers (any of several milestones), convertibility if IPO prices high
- **Founders want** — high strike price, long window, few/no triggers, forced conversion to common if company succeeds

A typical compromise: 5–7 year maturity, strike at cost basis, triggered only if company misses defined milestones (revenue targets, [Series B](/wiki/venture-capital-fund/) close by date X).

## Put options and [acquisition](/wiki/acquisition/) scenarios

If a company is [acquired](/wiki/acquisition/):

**Scenario 1: High acquisition price** — Preferred shareholders can **convert to common** and participate in the upside (diluting down to founders). They'd prefer this to exercising the put.

**Scenario 2: Low acquisition price** — If acquisition price is below the put strike, preferred shareholders **exercise the put** and receive the guaranteed amount, not the low acquisition consideration.

This creates tension in M&A negotiations. Founders and acquirers may want to pay a price that wipes out preferred return, but the put option prevents it—the preferred investors must be paid their strike price first.

## Put options and liquidation

In liquidation, [preferred stock](/wiki/preferred-stock/) with a put option has two possible paths:

1. **Standard preferred liquidation** — preferred shareholders are paid at [liquidation preference](/wiki/liquidation-preference/) (often 1X or 2X their investment) before common shareholders receive anything.
2. **Putable preferred** — if the put strike is *higher* than the liquidation preference, the put option is irrelevant (they're already getting paid more via liquidation).

If the company is worth less than the strike price, the put option may be worthless (company can't pay).

## Comparison to [callable bonds](/wiki/callable-bond/)

An equity put is structurally similar to a [put option](/wiki/put-option/) embedded in a [corporate bond](/wiki/corporate-bond/):

- **Bond put** — bondholder can force the issuer to redeem at par if rates rise or credit deteriorates
- **Preferred put** — preferred shareholder can force repurchase if company stalls

Both are protections against unfavorable scenarios. The difference: bond puts are senior (bonds are paid before equity), while preferred puts are subordinated to debt.

## Modern usage: employee stock options and RSUs

A new use of equity puts is in [employee stock plans](/wiki/employee-stock-options/). Some [restricted stock units](/wiki/restricted-stock-units/) (RSUs) grant employees a put option: if the company is acquired below a certain price, or if the company misses its IPO window, the employee can sell the shares back to the company at a guaranteed price. This protects employees from illiquidity risk.

## Limitations and risks

1. **Company insolvency** — if the company can't pay cash (no credit line, bankruptcy), the put option is worthless. Preferred shareholders become unsecured creditors.

2. **Dilution** — put options can be watered down if the company issues new preferred stock with better terms (junior puts, longer windows), pushing existing preferred investors down the [waterfall](/wiki/liquidation-preference/).

3. **Market risk** — if the preferred stock trades in a secondary market at a discount to strike price, the put is worth more to the holder than the current market value, creating arbitrage expectations. But the holder may not be able to exercise if the company refuses (legal battle).

<div class="wiki-seealso">

### Closely related
- [Put option](/wiki/put-option/) — the financial derivative; different mechanics
- [Preferred stock](/wiki/preferred-stock/) — where equity puts are embedded
- [Convertible preferred](/wiki/convertible-preferred/) — putable preferred with upside conversion
- [Liquidation preference](/wiki/liquidation-preference/) — senior claim in [preferred stock](/wiki/preferred-stock/)
- [Redemption rights](/wiki/redemption-rights-equity/) — alternative term for put-like rights

### Wider context
- [Venture capital fund](/wiki/venture-capital-fund/) — primary issuer of putable preferred
- [Employee stock options](/wiki/employee-stock-options/) — puts appear in equity comp
- [Change of control](/wiki/change-of-control/) — common trigger for puts
- [Acquisition](/wiki/acquisition/) — scenario where puts become relevant
- [Balance sheet](/wiki/balance-sheet/) — where putable liabilities appear

</div>
