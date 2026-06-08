---
title: "Rehypothecation"
description: "The practice of brokers reusing client-posted collateral as security for their own borrowing, creating leverage and systemic risk."
keywords:
  - broker leverage
  - collateral reuse
  - rehypothecation
  - systemic risk
  - client collateral
image: "/svg/trading.svg"
---

*A **rehypothecation** is a broker's use of client-posted collateral to secure its own loans and funding needs. By reusing pledged assets as security for external borrowing, a broker amplifies its leverage, and if that collateral is liquidated in a crisis, clients face unexpected shortfalls. The 2008 financial crisis exposed how systemic this practice had become.*

## The mechanics

When a client opens a margin account or borrows securities from a broker, that client typically must post collateral—cash, treasury bonds, or other liquid assets. The broker is permitted to hold and invest this collateral. Rehypothecation is the next step: the broker takes that collateral and pledges it to a lender (usually another bank) to borrow cash at a low rate, which it then re-lends to other clients at a higher rate.

The client's collateral is no longer sitting idle. It is working as security on the broker's borrowing book. In legal terms, the broker has taken ownership of the collateral and granted a security interest to the lender, converting the original client claim into a general unsecured claim against the broker. If the broker becomes insolvent, the client's collateral may already have been liquidated and the proceeds used to cover the broker's other obligations.

This is perfectly legal in most jurisdictions, provided the broker discloses the practice and reserves the right to rehypothecate. Many prime brokers include a standing rehypothecation clause in the client agreement, sometimes without explicit separate consent for each pledge.

## Why brokers do it

Rehypothecation is highly profitable. A prime broker can borrow cash secured by client collateral at SOFR (or LIBOR-linked rates) and lend it to other clients at SOFR plus 50–150 basis points. If the spread is 100 basis points and the broker rehypothecates billions of dollars in client collateral, the annual profit is substantial.

It also funds the broker's own operations. Rather than raising equity or issuing unsecured bonds, a broker can use client collateral to borrow cheaply. For large prime brokers serving hedge funds and institutional clients, rehypothecation can account for a third or more of total funding.

From the client's point of view (when they benefit), rehypothecation can lower the client's own borrowing costs. If a hedge fund borrows from a prime broker at SOFR + 75bps, and the broker turns around and rehypothecates the fund's collateral to fund the loan at a cheaper rate, the broker may pass some of that savings back in the form of a lower rate. The client sees lower financing costs; the broker keeps a spread.

## The systemic risk

Rehypothecation creates a critical vulnerability: if the lender (the entity that the broker borrowed from) marks down the value of the collateral or becomes stressed and demands repayment, the broker must liquidate the rehypothecated assets immediately. Because these assets were originally pledged by clients to secure margin loans or other credit lines, their forced sale can trigger margin calls on the original client accounts, forcing those clients to post additional collateral or liquidate positions—even though the clients themselves have done nothing wrong.

This is precisely what happened during the 2008 financial crisis. Lehman Brothers, one of the largest prime brokers, had rehypothecated billions of dollars in client collateral. When Lehman collapsed, its lenders and the broader repo market began withdrawing credit simultaneously. Lehman was forced to liquidate client collateral to raise cash, and clients woke up to find their security interests suddenly worthless. Some hedge funds and institutional investors lost billions.

Even more troubling, rehypothecation can propagate across the system. If Broker A rehypothecates Client X's collateral by pledging it to Bank B, and Bank B then uses that collateral to borrow from Bank C, a default by Bank B or Bank C can trigger a cascade of forced liquidations that spreads far beyond the original client relationship.

## Regulatory responses

After 2008, regulators moved to constrain rehypothecation, though the rules remain loose relative to the systemic risk. In the United States, the SEC and CFTC require disclosure of rehypothecation rights and set some limits on the amount brokers can rehypothecate, but the practice remains essentially legal.

The Dodd-Frank Act introduced higher capital and margin requirements that make rehypothecation less profitable for large brokers, reducing the incentive. It also strengthened the bankruptcy code provisions that protect client assets held in custodial accounts, though these protections are incomplete and depend on broker insolvency status.

In Europe, the Markets in Financial Instruments Regulation (MiFID II) requires explicit opt-in consent before rehypothecation and imposes tighter limits on the proportion of collateral a broker may rehypothecate. Japan's Financial Instruments and Exchange Act similarly restricts rehypothecation to client consent and sets caps.

Despite these regulations, rehypothecation remains standard practice among major prime brokers and is still significant in repo markets. The regulatory approach is to make it transparent and to require additional safeguards, rather than ban it outright.

## Alternatives and limits

Some institutional clients—particularly large hedge funds and asset managers—now avoid or limit rehypothecation by negotiating carve-outs in their prime brokerage agreements. They may insist that their collateral be held in segregated, non-rehypothecatable accounts, accepting a higher borrowing cost in exchange for greater safety. This is more expensive for the client and less profitable for the broker, so it is negotiated only by clients with enough leverage.

Smaller clients typically have no choice. When they sign a prime brokerage agreement or margin account agreement, rehypothecation is almost always included, often in small print.

## Connection to broader collateral dynamics

Rehypothecation sits at the intersection of [collateral haircuts](/collateral-haircut/), [securities lending](/securities-lending-haircut/), and [counterparty risk](/counterparty-risk/). The valuation of rehypothecated collateral is subject to the same haircuts applied in repo and securities lending markets; the lender will demand a discount to market value as a buffer against liquidation losses. And the systemic risk created by rehypothecation is fundamentally a [counterparty risk](/counterparty-risk/) problem compounded across layers of intermediaries.

The practice also illustrates why [leverage ratios](/leverage-ratio-forex/) and [capital adequacy](/capital-adequacy/) rules matter. A broker that rehypothecates aggressively is borrowing beyond what its own balance sheet can support, and in a market stress event, that overleveraged funding structure can unravel rapidly.

## See also

<div class="wiki-seealso">

### Closely related

- [Collateral haircut](/collateral-haircut/) — discount applied to pledged assets
- [Securities lending](/securities-lending-haircut/) — lending of securities backed by collateral
- [Counterparty risk](/counterparty-risk/) — exposure to a defaulting counterparty
- [Forced buy-in](/forced-buy-in/) — mandatory purchase after settlement failure
- [Margin call](/margin-call-forex/) — demand for additional collateral from a leveraged borrower

### Wider context

- Prime brokerage — bundled execution, financing, and custody services for hedge funds
- [Leverage ratio](/leverage-ratio-forex/) — proportion of debt to equity in a firm's capital structure
- [Capital adequacy](/capital-adequacy/) — regulatory capital required to absorb losses
- [Systemic risk](/systemic-risk/) — danger of cascading failures across the financial system
- [Dodd-Frank Act](/dodd-frank-act/) — post-2008 US financial reform legislation

</div>
