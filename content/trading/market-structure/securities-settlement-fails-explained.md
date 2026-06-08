---
title: "Securities Settlement Fails Explained"
description: "A settlement fail occurs when a buyer or seller cannot deliver securities on the agreed settlement date. Penalties, buy-ins, and systemic risks explained."
keywords:
  - settlement fails securities
  - fail to deliver short selling
  - sec buy-in rules penalties
  - settlement failure systemic risk
  - t+2 settlement securities
  - short sale fail-to-deliver
---

*A **settlement fail** (or **fail-to-deliver**) occurs when a party—buyer or seller—cannot deliver the securities or cash owed on the agreed settlement date. Fails arise from operational breakdowns, voluntary [short selling](/short-selling/), or borrowed shares that are never returned. The [SEC](/securities-and-exchange-commission/) enforces buy-in rules and penalties to deter abuse and reduce market friction, yet fails still cost the system billions annually and create opportunities for manipulation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Settlement Fails — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for market trading structure." />

<div class="wiki-infobox-caption">When delivery doesn't happen, penalties and systemic risk follow.</div>

|   |   |
|---|---|
| **Definition** | Failure to deliver securities or cash by settlement date |
| **Standard settlement** | T+2 (trade date + 2 business days) in US equities |
| **Common causes** | Operational delays, failed locate, short position not covered |
| **SEC buy-in threshold** | Fail must exceed 10,000 shares and $100k value to trigger buy-in rule |
| **Penalties** | Forced buy-in, short-sale buy-in fee, potential civil fines |
| **Systemic effect** | Concentrated fails can undermine price discovery and credit confidence |

</aside>

## What Happens During a Settlement Fail

When you trade a security, settlement—the actual exchange of cash for shares—typically occurs two business days later (T+2 in US equities). Both sides assume each party will deliver.

**A fail happens when:**

- **The buyer doesn't have cash ready**, or the transfer system is slow.
- **The seller doesn't have shares to deliver**—the most common scenario, especially in [short selling](/short-selling/).
- **The [custodian](/custodian/) or clearing firm has an operational glitch** that delays transfer.
- **Borrowed shares from a [broker](/broker/) are recalled** before the short seller can cover, stranding the seller without shares to deliver.

When a fail persists beyond settlement, the buyer is left empty-handed (they paid but got no securities), and the seller's short position remains open—they've received cash but never delivered shares. This asymmetry is the engine of fails.

## Fails Arising from Short Selling

The largest source of fails is [short selling](/short-selling/). Here's why:

1. **Locate requirement**: Before shorting, the broker must "locate" shares to borrow. Locate is not always guaranteed; the lender can recall shares.
2. **Borrow fails**: Even if located, the shares may not arrive from the lender's system by settlement. Operational delays in the securities lending market are endemic.
3. **Naked short selling**: (now heavily restricted by SEC Rule 10b-21) where a seller shorts without even attempting to locate. Fails were virtually guaranteed.

**Example**: You short-sell 10,000 shares of Stock XYZ at $50 on Monday (trade date). Settlement is Wednesday. Your broker locates the shares through a securities lending desk, but the lender's systems malfunction and the shares never arrive. On Wednesday, you fail to deliver those 10,000 shares.

The buyer (who legitimately purchased) is left in limbo. They've paid $500,000 but don't own the shares yet. Meanwhile, you (the seller) have the cash but not the obligation to deliver—the fail hangs indefinitely unless forced resolution.

## Operational Fails and Market Friction

Not all fails stem from deliberate short selling or market abuse. Operational breaks happen:

- **Custody transfer delays**: Especially when securities move between custodians or across borders.
- **Corporate actions**: Dividend payments, [stock splits](/stock-split/), or mergers can jam settlement systems.
- **System outages**: Rare, but when exchanges or clearinghouses go down, settlement lags.
- **Manual processing**: Trades requiring escrow or escrow releases can take longer.

These are genuine accidents, not manipulation. But even innocent fails fragment liquidity and erode confidence in the settlement system.

## SEC Buy-In Rules and Penalties

The SEC's primary tool to combat persistent fails is the **SEC buy-in rule** (Regulation SHO, Rule 10b-21a):

**Threshold and action:**
- If a fail to deliver persists for **13 consecutive settlement days**, the clearinghouse must issue a "buy-in notice" to the party who failed.
- The notice requires the failing party to "close out" the fail by buying back the shares on the open market and delivering them to the buyer, **within five business days**.
- If the fail is not closed out by then, the clearing agency itself can force a **mandatory buy-in**—purchasing shares on the open market and charging the failing party the cost, plus a buy-in fee.

**Penalties:**
- **Buy-in cost**: If you shorted at $50 and the stock has risen to $55, you must buy back at $55 and take the $5/share loss, multiplied by shares failed.
- **Buy-in fee**: A penalty assessed by the clearinghouse, typically $0.05–$0.10 per share or more.
- **Rebate reduction**: Brokers lend shares to earn a rebate; a fail reduces or eliminates that rebate, cutting the short seller's financing benefit.

In extreme cases, the SEC can impose civil fines or enforcement actions for patterns of deliberate fails (e.g., naked shorting).

## Why Fails Matter: Systemic and Market-Structure Risks

### Price Discovery Distortion

When a short seller consistently fails to deliver, they maintain a naked short position—they're receiving the price benefit (cash from the sale) without the obligation to cover. This can depress stock price artificially. Meanwhile, legitimate longs are unable to fully participate (they can't get their shares), distorting supply and demand signals.

### Fail-to-deliver as Manipulation

Coordinated fails can be used to manipulate stock prices, especially in thinly traded or small-cap stocks. A group of traders could short-sell aggressively, deliberately fail to deliver to suppress price, and then cover their actual shorts when the stock tanks.

### Clearinghouse Credit Risk

When fails accumulate, they create a credit risk for the clearinghouse. If the failing party defaults before buy-in is completed, the clearinghouse is on the hook. Massive fails in one security can threaten the financial stability of the clearing system.

### Buyer's Limbo and Collateral Chains

The buyer who never receives shares still has paying cash locked up. If the buyer is a [custodian](/custodian/) or [fund](/mutual-fund/), the blocked cash can cascade through other transactions, stalling their own settlements downstream.

## Fails in the 2008 Financial Crisis and Beyond

During the 2008 crisis, fails exploded. As Lehman Brothers and other institutions failed, trillions of dollars' worth of securities were stuck in settlement limbo. Counterparties couldn't access their collateral, multiplying liquidity stress. The SEC tightened Rule 10b-21 and buy-in rules in response.

Even today, fails remain elevated in certain micro-cap stocks and during market stress. The list of stocks with persistent fail-to-deliver is published by the SEC and is monitored by short-selling activists and value investors as a signal of potential manipulation.

## How Fails Are Resolved

1. **Voluntary delivery**: The failing party buys shares and delivers them before the five-day buy-in deadline.
2. **Clearinghouse buy-in**: The clearinghouse buys shares on the market and charges the failing party.
3. **Fail closure**: Occasionally, fails just close (are written off by the clearinghouse) if the buyer and seller reach an agreement or the buyer releases the claim.
4. **Default and loss absorption**: If the failing party defaults (is insolvent), the clearinghouse may absorb the loss or distribute it to members.

## See also

<div class="wiki-seealso">

### Closely related

- [Short selling](/short-selling/) — Mechanism that generates most settlement fails
- Clearinghouse — Infrastructure that detects and enforces buy-ins
- [Securities and exchange commission](/securities-and-exchange-commission/) — Regulator that sets fail-to-deliver rules
- [Counterparty risk](/counterparty-risk/) — Credit risk when settlement fails
- [Regulation SHO](/regulation-sho/) — SEC rule that defines fail-to-deliver thresholds and buy-in mechanics

### Wider context

- [Market maker trading](/market-maker-trading/) — Primary source of short selling; also subject to fails
- Settlement cycle — The T+2 timeline where fails occur
- 2008 financial crisis — Event that exposed systemic fail risks
- [Stock exchange](/stock-exchange/) — Institution that enforces settlement standards

</div>