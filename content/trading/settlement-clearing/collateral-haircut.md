---
title: "Collateral Haircut"
description: "The percentage discount applied to pledged assets to buffer against price volatility and default risk in lending relationships."
keywords:
  - haircut discount
  - collateral valuation
  - margin lending
  - default buffer
  - repo collateral
image: "/svg/trading.svg"
---

*A **collateral haircut** is a percentage reduction in the value of an asset when it is pledged as security for a loan. A bond worth 100 might be accepted as collateral only to 95 (a 5% haircut), so the borrower must post more assets to secure the same size loan. Haircuts protect the lender against price declines and default risk.*

## The fundamental logic

When a borrower pledges an asset as collateral, the lender doesn't accept it at full market value. Instead, the lender applies a discount—the haircut—to calculate the amount the borrower can borrow against that asset. The haircut is pure insurance: it creates a buffer so that if the collateral asset falls in price or becomes illiquid, the lender is still covered.

If a US Treasury bond is trading at par (100), the lender might apply a 0.5% haircut, accepting it as worth 99.5 for collateral purposes. If a corporate bond is trading at 100, the lender might apply a 3% haircut, treating it as worth 97. The difference between market value and haircut-adjusted value is the lender's safety margin.

The borrower experiences the haircut as a cost: to borrow $100, they must post assets with a market value greater than $100. This is why haircuts vary by asset class and borrower creditworthiness. The riskier the asset or the weaker the borrower, the larger the haircut.

## Haircuts across asset classes

Haircuts are most transparent and regulated in repo markets, where they are set by clearing houses and major dealers. In a Treasury repo, the haircut might be as low as 0.5% because US government debt is liquid and sovereign default risk is minimal. In a corporate bond repo, the haircut might be 2–5% depending on the issuer's credit rating. In an equity repo, haircuts are typically 5–15% because stock prices are volatile.

Bank loans and private credit arrangements rarely disclose their haircuts explicitly, but they are implicit in loan-to-value (LTV) ratios. A mortgage with an 80% LTV means the bank will lend only 80% of the property's appraised value—a 20% haircut. A margin account that requires 30% equity (the client covers 30% of the position in cash) is applying a 30% haircut to the securities in the account.

Derivative positions are also subject to haircuts, usually styled as "initial margin" or "variation margin." When a trader posts collateral to back a futures contract or an OTC swap, the clearing house or counterparty will require more collateral than the notional mark-to-market loss—applying a haircut to absorb potential moves before the next margin call.

## Why haircuts change

Haircuts are not fixed. They rise when volatility increases, when credit risk spikes, or when market liquidity dries up. During the 2008 financial crisis, haircuts on mortgage-backed securities spiked from a few percentage points to 20–50%, making it nearly impossible for large financial institutions to fund themselves using these assets as collateral. Some securities became uncollateralisable overnight.

Central banks can use haircuts as a policy tool. When the Federal Reserve offers emergency lending through a discount window or repo facility, it adjusts haircuts to signal how much credit it wants to extend. Lower haircuts encourage borrowing; higher haircuts restrict it.

Market participants also adjust haircuts based on forward-looking risk assessments. If consensus forecasts expect rising interest rates, haircuts on long-duration bonds might rise in anticipation of price declines. If a company's credit rating is under review for downgrade, haircuts on its debt will rise even before the rating change is official.

## The borrower's perspective

For the borrower, haircuts directly affect the cost and availability of funding. If a hedge fund has $100 million in assets and wants to lever up 2:1 using repo financing, it needs to borrow $100 million against those assets. If haircuts are 5%, the fund must post $110.6 million in collateral to borrow $100 million—a costly arrangement. If haircuts rise to 10%, the fund must post $123 million to borrow the same $100 million, reducing its effective leverage and squeezing its returns.

This is particularly painful for leveraged investors in a rising-haircut environment. A prime broker or repo lender can raise haircuts on existing positions, forcing the borrower to post more collateral or liquidate positions immediately—a margin call with no opportunity to negotiate. In March 2020, when volatility spiked, haircuts rose sharply and many hedge funds were forced to liquidate to meet margin calls, amplifying the market decline.

## Relationship to other credit safeguards

Haircuts are one of several tools lenders use to protect themselves. [Margin requirements](/margin-call-forex/) are often paired with haircuts: a borrower must maintain a minimum equity cushion (e.g., 30% of the position), and that equity is calculated using haircut-adjusted collateral values. [Credit ratings](/credit-rating/) inform haircut levels; lower-rated borrowers are assigned higher haircuts. [Concentration limits](/concentration-risk/) prevent lenders from accepting too much collateral in a single issuer or sector, further reducing exposure.

In repo markets, haircuts work alongside standardised terms (fixing the maturity, the cash payment, and the repurchase price) to create predictable, scalable funding. A repo dealer can repo billions of dollars of bonds intraday, relying on haircuts and the standardised structure to manage risk without individual credit analysis of each counterparty.

## Haircuts in securities lending

Securities lending, where a lender loans securities to a borrower in exchange for a fee, uses a related mechanism: the lender requires the borrower to post collateral (typically cash or high-grade bonds) at an amount greater than the market value of the loaned securities. The difference is the haircut. If the loaned security is worth 100, the lender might require 105 in cash collateral—a 5% haircut. This protects the lender if the security's value rises and the borrower refuses to return it, or if the borrower defaults and the lender must liquidate collateral.

These [securities lending collateral schedules](/securities-lending-haircut/) often specify different haircuts by asset class and issuer quality, creating a granular risk framework.

## See also

<div class="wiki-seealso">

### Closely related

- [Securities lending collateral schedule](/securities-lending-haircut/) — tiered haircut table for non-cash collateral
- [Margin call](/margin-call-forex/) — demand for additional collateral from a leveraged borrower
- [Rehypothecation](/rehypothecation/) — reuse of client collateral to secure broker borrowing
- [Forced buy-in](/forced-buy-in/) — mandatory purchase after settlement failure
- [Credit rating](/credit-rating/) — assessment of creditworthiness affecting haircut levels

### Wider context

- [Leverage ratio](/leverage-ratio-forex/) — proportion of debt to equity
- [Capital adequacy](/capital-adequacy/) — regulatory capital requirements
- [Counterparty risk](/counterparty-risk/) — exposure to default by another party
- [Liquidity risk](/liquidity-risk/) — inability to sell assets at fair prices
- [Volatility](/historical-volatility/) — degree of price variation affecting haircut sizing

</div>
