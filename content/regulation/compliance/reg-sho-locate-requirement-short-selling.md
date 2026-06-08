---
title: "Reg SHO Locate Requirement for Short Selling"
description: "The SEC's Regulation SHO Locate Requirement mandates that brokers verify borrowable shares before executing short sales, reducing settlement failures and naked shorts."
keywords:
  - reg sho locate requirement
  - short selling locate requirement
  - fail-to-deliver settlement
  - naked short selling regulation
---

*Before a [broker](/broker/) can execute a [short sale](/short-selling/), it must **locate** borrowable shares—confirming that securities exist and can be borrowed to deliver on settlement day. This is the **Reg SHO Locate Requirement**, a critical rule under SEC Regulation SHO designed to prevent **naked short selling** (selling shares you haven't borrowed) and reduce fails-to-deliver. The locate obligation applies primarily to broker-dealers, who must document the locate before order execution and monitor fails-to-deliver across their short position inventory.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reg SHO Locate Requirement — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation." />

<div class="wiki-infobox-caption">A pre-trade gating mechanism that ensures borrowed shares exist before a short sale settles.</div>

|   |   |
|---|---|
| **Regulation source** | SEC Regulation SHO, Rule 10a-1c |
| **Obligation holder** | Broker-dealers executing short sales on behalf of customers |
| **Core requirement** | Document availability of borrowable shares **before** order entry |
| **Documentation** | Marked locate ticket; internal records linking order to borrowable inventory |
| **Fail-to-deliver consequences** | Position must be bought in; broker-dealer liable for settlement failure |
| **Exemptions** | Market makers under Rule 10a-1(b); certain defined circumstance exemptions (narrow) |
| **Enforcement** | SEC exam findings; SRO (FINRA/NYSE) rule violations; reputational/capital impact |

</aside>

## The Problem: Naked Short Selling and Fails-to-Deliver

Before Reg SHO's Locate Requirement (adopted 2005), it was theoretically possible for a broker-dealer to execute a short sale without confirming it could borrow shares. The [short seller](/short-selling/) would deliver an IOU on settlement day instead of actual securities. These settlement failures, or **fails-to-deliver**, created "naked" short positions—borrowed shares that never actually existed.

Fails-to-deliver are problematic because:
- **Dilution illusion**: Investors buy shares thinking they own them, but the [broker](/broker/) never actually borrowed or delivered them. This can artificially inflate float and dilute shareholder value.
- **Forced buy-ins**: When a fail-to-deliver persists, the [broker](/broker/) must buy the shares at market price to settle, potentially causing sudden price spikes that hurt the short seller.
- **Market integrity**: Uncontrolled fails undermine [price discovery](/price-discovery/) and settlement certainty.

The Locate Requirement was designed to prevent this. Before executing a short sale, the broker-dealer must confirm that shares are available to borrow—and document it in writing.

## How the Locate Requirement Works

### Before Order Entry

The broker-dealer (or its [prime broker](/prime-broker/) for a [hedge fund](/hedge-fund/) executing the short) checks its available inventory of shares to borrow. This check typically happens through:
- **Internal borrow desk**: The firm's own stock lending operation notes which shares are available for short sale
- **Prime broker borrow availability**: For [hedge funds](/hedge-fund/), the [prime broker](/prime-broker/) confirms it can lend the shares
- **Third-party borrow sources**: The [broker](/broker/) may consult external borrow facilities or [market makers](/market-maker-trading/) who aggregate lendable shares

Once the broker-dealer confirms shares are locatable, it creates a **locate ticket**—a contemporaneous record showing:
- The security symbol and quantity
- The date and time the locate was confirmed
- The source of borrowable shares
- The identity of the broker-dealer executing the locate

This ticket must be created **before** the order is entered into the exchange or [alternative trading system](/alternative-trading-system/).

### After Execution

The located shares are typically flagged in the broker-dealer borrow system, ensuring they are not double-allocated to multiple short sellers. On settlement (usually T+2 for [stocks](/stock/)), the broker-dealer must deliver the securities or replace the failed position via a forced buy-in.

If the broker-dealer cannot deliver on settlement day, it becomes a fail-to-deliver and the broker-dealer is out-of-pocket. It must buy-in the position at the market price, often at a loss. This creates a strong incentive to locate before accepting the order.

## Documentation and Record-Keeping

Reg SHO requires broker-dealers to maintain detailed borrow records:

| Record | Retention | Purpose |
|--------|-----------|---------|
| **Locate tickets** | 5 years | Proof that shares were located before execution |
| **Borrow confirmations** | 5 years | Identity and availability of lendable shares |
| **Buy-in records** | 5 years | Documentation of forced purchases to cover fails |
| **Fails-to-deliver inventory** | 10 trading days | Real-time tracking of open settlement failures |

The SEC exam teams regularly request these records to verify compliance. A broker-dealer that cannot produce a locate ticket for a short sale faces examination findings and potential enforcement action.

## Close-Out Rules for Fails-to-Deliver

Under Reg SHO Rule 204T (now simplified to Rule 204), a broker-dealer must close out any fail-to-deliver by the end of the settlement date (T+2 for equities). If shares are not delivered by T+3 or T+4 (depending on SEC emergency orders), the broker-dealer must buy-in the position at the market price and force it to the [short seller](/short-selling/) or its lender.

A buy-in order is typically executed at the best available price, sometimes at a loss to the [short seller](/short-selling/). This is intentional—it penalizes short sellers who fail to borrow.

In rare cases, the SEC can issue a close-out order, requiring even faster settlement. During extreme volatility or naked short selling campaigns against specific [stocks](/stock/) (e.g., heavily shorted micro-caps), the SEC may enforce stricter close-out timelines.

## Exemptions and Special Cases

### Market Maker Exemptions

**Market makers** are exempted from the Locate Requirement under Rule 10a-1(b). A [market maker](/market-maker-trading/) can short a [stock](/stock/) at the offer price without locating, as long as the short is part of market-making activities (providing liquidity). This is necessary for market makers to operate—they must be able to short into strong bid interest without delay.

However, market makers are subject to close-out rules and cannot accumulate naked short positions indefinitely.

### Threshold Securities

The SEC maintains a list of **threshold securities**—heavily shorted or volatile [stocks](/stock/) where special locate and close-out rules apply. During periods of high short interest or multiple fails, threshold securities face tighter restrictions, including earlier buy-in deadlines.

### Defined Circumstances Exemptions

In limited cases, the SEC may issue exemptive orders allowing short sales without locates (e.g., during a market emergency or for specific institutional transactions). These are rare and narrowly granted.

## FINRA and Exchange Enforcement

FINRA (the Financial Industry Regulatory Authority) and individual exchanges (NYSE, NASDAQ) enforce Reg SHO through rule violations and surveillance:
- **FINRA Rule 5210**: Requires broker-dealers to locate shares before short sale execution
- **Real-time surveillance**: Exchanges flag trades that settle late or fail repeatedly
- **Exam findings**: SEC and SRO examiners identify locate ticket gaps and inadequate borrow procedures

Violations can result in:
- Regulatory censures and fines (often in the millions for major broker-dealers)
- Suspension of short-selling privileges
- Reputational damage and loss of client business
- Capital charges for persistent fails-to-deliver

## Impact on [Short Sellers](/short-selling/) and [Hedge Funds](/hedge-fund/)

For [short sellers](/short-selling/), the Locate Requirement has several practical effects:

- **Borrow availability**: Hot short ideas may become unavailable to borrow, capping short interest
- **Borrow costs**: [Hedge funds](/hedge-fund/) pay [prime brokers](/prime-broker/) for stock loans. Locate verification adds operational costs
- **Execution delays**: In illiquid stocks, confirming a locate may take hours, delaying order entry
- **Forced buy-ins**: If the [short seller](/short-selling/) fails to return borrowed shares, it is forced to buy back at market—creating unexpected losses

For [market makers](/market-maker-trading/) and institutional investors, the Locate Requirement is less disruptive because of exemptions and because their short sales are typically hedges tied to specific trades.

## See also

<div class="wiki-seealso">

### Closely related

- [Short selling](/short-selling/) — strategy, mechanics, and risks of selling borrowed securities
- Fail-to-deliver — settlement failures and their market impact
- Naked short selling — selling securities without borrowing, regulated under Reg SHO
- Broker-dealer — financial firms that execute trades and settle securities
- Stock lending — market for borrowing shares, underpinning locate availability
- [Prime broker](/prime-broker/) — specialized broker serving hedge funds and [short sellers](/short-selling/)

### Wider context

- Settlement — clearing and delivery of traded securities
- [Market maker](/market-maker-trading/) — liquidity providers exempt from locate restrictions
- Threshold securities — heavily shorted stocks subject to enhanced regulation
- [SEC enforcement](/sec-enforcement/) — regulatory action against locate violations

</div>
