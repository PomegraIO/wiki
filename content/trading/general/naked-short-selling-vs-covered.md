---
title: "Naked Short Selling vs Covered Short Selling"
description: "Naked short selling lacks a borrow arrangement for the shares; covered shorts are backed by an agreement to locate and deliver securities."
keywords:
  - naked short selling definition
  - covered short selling
  - fails to deliver
  - short selling regulations
  - sec naked short rules
  - borrow requirement
image: "/svg/trading.svg"
---

*A **naked short sale** is a sale of stock the seller does not own and has not borrowed, while a **covered short sale** is backed by a borrow arrangement that obligates the seller to deliver the shares within a settlement period. The distinction determines whether a trade is legal, whether the seller can actually fulfill the delivery obligation, and what regulatory scrutiny it faces.*

<div class="wiki-hatnote">

This article distinguishes short sales by borrow status. For the general mechanics of short-selling, including the profit motive and risk profile, see [Short Selling](/short-selling/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Naked vs Covered Shorts — Core Differences</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Borrow status is the legal and operational line between compliant and non-compliant short sales.</div>

|   |   |
|---|---|
| **Borrow Requirement** | Naked: None. Covered: Prior arrangement with a lender. |
| **Delivery Obligation** | Naked: Unmet; results in fail-to-deliver. Covered: Backed by borrowed shares. |
| **SEC Regulation** | Naked: Prohibited since 2008 (limited exceptions). Covered: Compliant if executed properly. |
| **Settlement Risk** | Naked: Counterparty cannot be delivered to; system fails. Covered: Lender retains shares until repurchase. |
| **Enforcement** | Naked: SEC can fine or revoke trading permissions. Covered: Routine; no additional scrutiny if borrow is documented. |
| **Common Occurrence** | Naked: Rare in equities; more historical than current practice. Covered: Standard for any institutional short. |

</aside>

## How Naked Shorts Arose

In the pre-digital era, when trades settled in physical certificates or ledgers that could not be instantly verified, it was possible to sell stock without immediately confirming you had the shares to deliver. A broker might execute a short sale and have a day or two (the settlement cycle) to locate and borrow the shares from another account holder before the trade had to settle. If the shares could not be found in time, a "fail to deliver" occurred—the buyer was owed shares but did not receive them.

This was a loophole, not by design, but because settlement infrastructure was slow and trades could outpace verification. By the early 2000s, with electronic trading enabling massive volumes and settlement cycles standardized at T+3 (three business days), the practice of selling shares one had no reasonable expectation of borrowing became more systematic. Some traders would deliberately short a stock naked, betting that the fail-to-deliver would signal distress to the market and push the price down—a form of market manipulation.

The clearest harms emerged in smaller companies or thinly traded stocks where few shares were available to borrow. Naked shorting could create phantom shares that depressed prices artificially, while the broker and seller profited from the fail. Legitimate shareholders found their holdings diluted by undelivered shares floating through the system.

## Regulatory Response and Current Status

In 2008, the Securities and Exchange Commission (SEC) issued Rule 10b-21, which prohibited "naked access"—the ability to place orders without pre-trade verification that the shares could be delivered. Shortly after, the SEC mandated that all short-sale orders be marked as "short" at order entry, allowing brokers to check borrow availability before execution.

The SEC also clarified that a short sale becomes illegal if, at the time of order placement or shortly thereafter, the broker has no reasonable belief that the shares can be borrowed for delivery. The term "naked" in this context does not mean the shares are never borrowed; rather, it means the seller did not confirm a borrow *before* selling.

In practice, brokers now maintain borrow inventory—relationships with prime brokers, other institutions, and lending agents who supply shares for short. When a short order is received, the broker checks this inventory. If shares are available, the borrow is reserved and the sale is covered. If not, the order is rejected.

The result is that naked shorting in equities is now rare in the regulated market. A broker that allows a naked short violates SEC rules and faces penalties, reputational damage, and potential loss of brokerage license. However, compliance is not perfect, and fails to deliver still occur—usually when a borrow breaks (the lender recalls shares unexpectedly) or when execution and settlement occur so quickly that the normal locate process lags.

## Fails to Deliver and Their Consequences

A **fail to deliver** occurs when a seller cannot deliver shares by settlement. The buyer does not receive the stock and the seller's obligation sits open.

When a fail persists beyond a few days, it signals a breakdown in the system. In regulated venues like U.S. stock exchanges, brokers are required to buy back shares to close a fail (a "close-out" requirement under SEC Rule 10b-21). Until the fail is resolved, the shares remain in limbo—the buyer has a financial claim but not legal ownership, and the seller retains a profitable short position without the capital outlay of an actual borrow.

A famous example occurred in 2005 when Overstock.com alleged that a flood of fails to deliver in its shares was evidence of naked shorting meant to drive down its stock price. The company sued and ultimately settled with clearing firms. The incident highlighted how fails, even if caused by operational failures rather than deliberate manipulation, can distort share prices and undermine market confidence.

Today, the SEC publishes a monthly list of stocks with significant fails to deliver. Stocks that consistently appear on that list face intense scrutiny and possible enforcement action against the brokers responsible.

## The Gray Areas

**Authorized Participation in ETFs.** Authorized participants who create and redeem exchange-traded fund shares are exempt from the locate requirement for the underlying securities in some cases. They may short shares without pre-confirming a borrow, provided they deliver the shares within a set window. This is not considered naked shorting because the exemption is explicit and the timeframe is tightly constrained.

**Options and Derivatives.** Naked shorting rules apply primarily to equities. In options markets, a seller of a call option may not hold shares (a "naked call"), and the seller of a put may not hold cash to buy the shares. These are permissible and common. The term "naked" in options refers to leverage, not to failure to deliver, and is not prohibited.

**International Markets.** Different jurisdictions have different rules. Some countries prohibit naked shorting entirely; others allow it under certain circumstances. The EU banned some forms of naked short selling in 2012, while other regions have lighter restrictions. This creates opportunities for arbitrage and complicates enforcement.

## The Debate Over Naked Shorting

Critics argue that even with SEC rules in place, naked shorting persists in illicit over-the-counter markets and through regulatory gaps. They contend that any naked shorting—even in small amounts—distorts prices and harms legitimate shareholders.

Defenders of the pre-2008 framework (a minority view today) argued that the efficiency gains from allowing short settlement to be asynchronous outweighed the manipulation risk, and that aggressive enforcement was preferable to a blanket prohibition. That position has been largely abandoned in the U.S., though some economists still debate whether the 2008 rules were too stringent.

The practical consensus is now that covered shorts—with confirmed borrows and full settlement—are the only compliant way to short, and that market infrastructure should make naked shorting effectively impossible. Whether that ideal has been fully achieved remains an open question, particularly in OTC and international venues.

## See also

<div class="wiki-seealso">

### Closely related

- [Short Selling](/short-selling/) — The mechanics and rationale for betting on price declines
- Fails to Deliver — Why shares don't settle and their market implications
- Borrow and Lending in Markets — How shares are sourced for short sales
- Market Manipulation — The regulatory framework and enforcement for deliberate price distortion
- Regulation SHO — The SEC's comprehensive short-sale rule framework

### Wider context

- [SEC Enforcement](/sec-enforcement/) — How regulations are monitored and violators sanctioned
- Settlement and Clearing — The backend infrastructure that enables or prevents naked shorting
- [Counterparty Risk](/counterparty-risk/) — Why fails to deliver threaten system stability
- Equity Markets Structure — Exchanges, brokers, and the plumbing of stock trading

</div>
