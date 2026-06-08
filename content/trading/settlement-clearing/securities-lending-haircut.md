---
title: "Securities Lending Collateral Schedule"
description: "The tiered haircut table governing which non-cash collateral a lender accepts and at what valuation in securities lending."
keywords:
  - securities lending
  - collateral schedule
  - non-cash collateral
  - haircut tiers
  - lending risk
image: "/svg/trading.svg"
---

*A **securities lending collateral schedule** is the lender's published table specifying which assets the borrower may post as collateral, the haircut applied to each asset class, and the daily mark-to-market process. Rather than require cash alone, lenders accept bonds, equities, and other securities—but only at discounted valuations that reflect risk and liquidity.*

## Why schedules matter

When a lender loans securities to a borrower, the lender must retain protection against borrower default and against the value of loaned securities rising unexpectedly. The simplest protection is to require the borrower to post cash collateral in excess of the market value of the loaned securities—a cash-only model. But cash collateral is expensive for the borrower to source; they must finance it somewhere.

Most large securities lending programs therefore accept non-cash collateral: government bonds, investment-grade corporate bonds, equities, and other securities. Accepting non-cash collateral is cheaper for the borrower and increases the lender's yield (the lender keeps the interest earned by the collateral securities), but it introduces new risks. The collateral itself might fall in value, or become illiquid in a stress event.

To manage these risks, lenders publish a collateral schedule—a table that lists each permissible collateral type, applies a [haircut](/collateral-haircut/) (discount to market value), and specifies daily valuation rules. This schedule is the operational framework for the entire lending relationship.

## Structure of a typical schedule

A collateral schedule usually has columns for:

| Collateral Type | Haircut | Concentration Limit | Pricing Source |
|---|---|---|---|
| US Treasury bills (T-bills) | 0.25% | 50% | Market close |
| US Treasury bonds (2–10 year) | 0.5% | 50% | Market close |
| US Treasury bonds (>10 year) | 1.0% | 50% | Market close |
| Investment-grade corporate bonds (AAA/AA) | 2% | 30% | Consensus pricing |
| Investment-grade corporate bonds (A) | 3% | 25% | Consensus pricing |
| Investment-grade corporate bonds (BBB) | 5% | 15% | Consensus pricing |
| US equities (S&P 500) | 10% | 20% | Market close |
| International equities (major markets) | 15% | 10% | Market close |
| Emerging-market equities | 25% | 5% | Day-lagged pricing |
| Municipal bonds | 7% | 10% | Mid-pricing |
| Mortgage-backed securities (agency-backed) | 2% | 15% | Bloomberg |

Each row specifies the haircut applied to that collateral type, the maximum amount of the overall collateral pool that can be in that type (concentration limit), and the daily pricing source. The schedule is published in the master securities lending agreement and updated periodically as market conditions change.

## How haircuts are applied

The haircut is subtracted from the market value of the collateral to calculate the "haircut-adjusted value" available to satisfy the collateral requirement. If a borrower posts $100 million in investment-grade corporate bonds (BBB-rated) with a 5% haircut, only $95 million counts toward the collateral requirement. If the borrower wants to borrow $100 million in securities, they must post $105.26 million in BBB corporates to meet the requirement.

Haircuts can be symmetric (applying equally to increases and decreases in collateral value) or asymmetric (typically broader on downsides to protect the lender). Most schedules use symmetric haircuts for simplicity.

Some lenders apply an additional "concentration haircut" if the borrower posts too much of a single collateral type. For example, if the schedule allows US Treasury bonds as up to 50% of the collateral pool, and the borrower posts 60%, the lender might apply an additional 2% haircut to the excess, incentivising diversification.

## Daily mark-to-market and collateral management

Each business day, the lender marks the collateral to market (revalues it using current prices) and recalculates the haircut-adjusted collateral value. If the collateral falls in value, the borrower's cushion shrinks. If the haircut-adjusted value drops below the required amount, the borrower must post additional collateral immediately—a collateral call. If the borrower fails to respond within the contractual deadline (usually 1–2 business days), the lender has the right to liquidate collateral and unwind the loan.

This daily reconciliation is operationally intensive. Large lenders employ teams to manage collateral valuation, track concentration limits, and issue calls. Technology systems automate much of this, but manual review is common for edge cases (e.g., newly delisted equities, hard-to-price securities).

The pricing source matters. For liquid assets like Treasury bonds and S&P 500 equities, market-close pricing is straightforward. For less liquid assets (municipal bonds, emerging-market equities), pricing sources might be consensus pricing from specialist vendors or day-lagged pricing to reflect valuation delays.

## Why schedules vary

Different lenders publish different schedules, reflecting their own risk appetite and the borrower's creditworthiness. A prime broker might accept a broader range of collateral (including emerging-market equities and high-yield bonds) for a prime hedge fund customer, with lower haircuts. The same lender might accept only Treasury bonds and S&P 500 equities, with higher haircuts, for a smaller or less creditworthy borrower.

Schedules also respond to market conditions. During the 2008 financial crisis, many lenders removed mortgage-backed securities from their collateral schedules entirely, and haircuts on other asset classes spiked from single digits to 20–40%. After the crisis, schedules gradually returned to pre-crisis breadth, though with permanently higher haircuts in some classes (like mortgages and emerging-market debt).

Corporate-action events—dividend payments, stock splits, mergers—can temporarily affect pricing until the schedule is updated. A lender might apply a temporary surcharge or hold back if a security has an upcoming corporate action that could affect valuation.

## Connection to broader collateral frameworks

A securities lending collateral schedule is related to, but distinct from, [collateral haircuts](/collateral-haircut/) in general. Haircuts apply to any lending relationship; the schedule is the securities lender's specific operational tool. Both serve the same purpose: protecting the lender by discounting collateral value.

The schedule also interacts with [forced buy-in](/forced-buy-in/) rules. If the borrower fails to return loaned securities, the lender can sell the collateral to recover the securities' value. The haircut and concentration limits in the schedule ensure the lender has enough collateral value to cover the cost of replacement.

In [rehypothecation](/rehypothecation/) arrangements, the lender often applies its own collateral schedule to collateral pledged by the borrower. A prime broker, which has accepted client collateral and then rehypothecates it to a bank, must transfer the original collateral schedule (or one at least as strict) to the bank. This creates a chain of collateral standards.

## Renegotiation and disputes

Collateral schedules are contractual, so they can be renegotiated. A borrower facing onerous haircuts or narrow asset acceptance might negotiate for a tighter schedule if their credit quality improves or if they move to a less risky counterparty. Conversely, a lender might tighten its schedule in response to market stress.

Disputes can arise over valuation. If a collateral security is thinly traded or has just paid a dividend, pricing disagreements are not uncommon. Large lending programs typically include a dispute-resolution clause allowing either party to escalate to senior management or an external pricing service to break ties.

## See also

<div class="wiki-seealso">

### Closely related

- [Collateral haircut](/collateral-haircut/) — discount applied to pledged assets across all lending types
- [Forced buy-in](/forced-buy-in/) — purchase of securities after failure to deliver
- [Rehypothecation](/rehypothecation/) — reuse of client collateral as security for broker borrowing
- [Margin call](/margin-call-forex/) — demand for additional collateral
- [Credit rating](/credit-rating/) — assessment of creditworthiness affecting collateral acceptance

### Wider context

- [Counterparty risk](/counterparty-risk/) — exposure to default by another party
- [Liquidity risk](/liquidity-risk/) — inability to sell or revalue assets at fair prices
- [Interest rate risk](/interest-rate-risk/) — exposure to price changes from interest rate moves
- [Concentration risk](/concentration-risk/) — excessive exposure to a single issuer or sector
- [Leverage ratio](/leverage-ratio-forex/) — proportion of debt to equity

</div>
