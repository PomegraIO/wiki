---
title: "Repo Haircut"
description: "How collateral is marked below market value in repo to protect lenders against price and liquidity risk."
keywords:
  - repo haircut
  - collateral haircut
  - margin requirement
  - repo discount
  - credit protection
image: "/svg/fixed-income.svg"
---

*A **repo haircut** is a markdown applied to the market value of collateral posted in a [repurchase agreement](/repurchase-agreement/), creating a cushion that protects the cash lender against losses if the borrower defaults or the collateral declines in value. The haircut is the difference between what the borrower receives in cash and the full market value of the security pledged.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Repo Haircut — key facts</div>

<img src="/svg/fixed-income.svg" alt="An abstract editorial mark for fixed-income and money-market topics." />

<div class="wiki-infobox-caption">A collateral discount that insulates repo lenders from mark-to-market and liquidation losses.</div>

|   |   |
|---|---|
| **What it is** | Percentage discount applied to collateral value to compute cash advanced in repo |
| **Also called** | Haircut, repo discount, margin requirement |
| **Typical range** | 0.5% to 5% for Treasury collateral; much higher for lower-rated securities |
| **Why it exists** | Protects lender against counterparty default, price moves, and liquidity risk |
| **Adjusts for** | Collateral volatility, issuer credit risk, and market liquidity |
| **Inverse measure** | LTV (loan-to-value) – the amount lender will advance |

</aside>

## The mechanics of a haircut

In a standard repo, the borrower sells a security and agrees to repurchase it at a set price on a future date. The cash advanced to the borrower is always less than the current market value of the collateral. That gap is the haircut.

Suppose a borrower posts Treasury bonds currently worth $100. If the repo haircut is 1%, the lender advances only $99 in cash. The borrower receives $99 and pledges collateral worth $100 at market. The $1 difference is the haircut—a buffer that protects the lender if the bond's value falls or if the borrower fails to repurchase.

Equivalently, if a lender advances $99, they are lending at an 99% loan-to-value (LTV) ratio. Higher LTV means smaller haircut; lower LTV means larger haircut. The relationship is simple: **Haircut % = 100% – LTV%**.

## Why lenders demand haircuts

A [repo transaction](/repurchase-agreement/) is technically a sale followed by a forward purchase agreement, but economically it functions as a collateralised loan. The lender faces three key risks.

**Counterparty risk.** If the borrower fails to repurchase the security, the lender must liquidate the collateral to recover their cash. If the market has moved against the collateral in the interim, the lender suffers a loss. A haircut provides a cushion. If the collateral price drops 0.5%, and the haircut is 1%, the lender still breaks even (the price decline consumes only half the haircut buffer).

**Price risk.** Most repo collateral is actively traded and marked daily or multiple times per day. [Duration](/duration/) and [credit spread](/credit-spread/) movements can swing collateral values substantially, especially for longer-dated bonds. A lender who advances cash against a 10-year Treasury with a 1-day repo term still faces the risk that yields spike overnight. The haircut absorbs expected intraday or short-term volatility.

**Liquidity risk.** Even the most liquid securities can become difficult to liquidate during market stress. A lender forced to sell collateral quickly may face a bid-ask spread wider than normal, or a market depth so thin that they cannot exit without moving prices against themselves. The haircut compensates for this emergency liquidation cost.

## How haircuts vary

Haircuts are not uniform; they scale with the riskiness and liquidity profile of the collateral.

[Treasury securities](/treasury-bond/) typically carry the smallest haircuts—often 0.5% to 2%—because they are liquid, have no credit risk, and their prices move predictably. Bills, notes, and bonds all trade special and general collateral markets with tight spreads.

[Agency mortgage-backed securities (MBS)](/mortgage-backed-security/) have haircuts usually in the 1% to 3% range, reflecting their relative safety but slightly lower liquidity compared to Treasuries.

[Corporate bonds](/corporate-bond/) and [municipal bonds](/municipal-bond/) attract haircuts of 2% to 8% or more, depending on the issuer's credit rating, the bond's tenor, and market liquidity.

Non-investment-grade or high-yield collateral may be rejected outright by conservative repo lenders, or accepted only at haircuts of 15% or higher—effectively making repo financing uneconomical for the borrower.

## Dynamic haircuts and margin calls

In overnight or term repo, haircuts are typically fixed at the initiation of the trade. But in some agreements, especially longer-dated or bespoke repo arrangements, haircuts can be dynamic—adjusted daily or weekly based on mark-to-market revaluation of the collateral.

If a borrower posts a $100 bond backed by a 1% haircut, receiving $99 in cash, and the bond then declines to $98 in value, the lender's cushion has eroded. Under a dynamic haircut regime, the lender can issue a [margin call](/margin-call-forex/), demanding the borrower post an additional $1 (or other collateral) to restore the 1% haircut. Failure to meet the margin call can trigger an event of default.

For the borrower, rising haircuts or surprise margin calls during market volatility can be destabilizing. During the 2008 financial crisis, haircuts spiked across asset classes, and margin calls on repo positions contributed to forced asset sales and contagion.

## Regulatory and market-driven haircuts

Post-2008, regulators and central banks have taken a keen interest in haircut practices. The [Federal Reserve](/federal-reserve/) publishes guidelines on appropriate haircuts for different collateral types, especially for facilities like the Discount Window and reverse repo operations. The goal is to prevent pro-cyclical margin hikes that amplify fire sales during stress.

In normal markets, competition among dealers and money-market lenders keeps haircuts stable and fair. But during periods of illiquidity or credit stress, borrowers may find haircuts expanding, the cost of repo rising sharply, or repo access drying up entirely. The haircut becomes not just a discount, but a market-wide signal of risk appetite.

## Haircut vs. [repo rate](/repurchase-agreement/)

Haircuts and repo rates are distinct but complementary tools for pricing repo risk. The haircut is a one-time collateral markdown; the repo rate is the interest charged on the cash lent. A borrower might access cheap repo funding (low rate) but face a large haircut, making the true cost of leverage high. Conversely, a high-credit borrower postcard [Treasury collateral](/treasury-bill/) might enjoy both a low rate and a minimal haircut.

## See also

<div class="wiki-seealso">

### Closely related

- [Repurchase Agreement](/repurchase-agreement/) — the repo transaction structure within which haircuts apply
- [Specials Repo](/specials-repo/) — repo financing for high-demand collateral, often with below-GC rates
- [Margin Call](/margin-call-forex/) — the demand for additional collateral when haircuts erode
- [Credit Risk](/credit-risk/) — the lender risk that haircuts help mitigate
- [Liquidity Risk](/liquidity-risk/) — the sell-cost cushion that haircuts provide
- [Treasury Bill](/treasury-bill/) — the lowest-haircut collateral in money markets

### Wider context

- Money Market — the short-term funding context where repo and haircuts operate
- [Bond](/bond/) — the typical repo collateral asset
- [Federal Reserve](/federal-reserve/) — regulator of repo and haircut practices
- Risk Management — the framework in which haircuts function
- Leverage — the financing mechanism that haircuts constrain

</div>
