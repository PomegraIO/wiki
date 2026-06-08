---
title: "Intraday Liquidity Facilities at Central Banks"
description: "How central banks extend same-day credit to smooth payment-system settlement and why this differs from overnight lending facilities."
keywords:
  - intraday liquidity facilities central banks
  - daylight overdraft
  - central bank credit facilities
  - settlement liquidity
  - payment system timing
image: "/svg/monetary.svg"
---

*Intraday liquidity facilities at central banks are same-day credit lines that allow banks and settlement institutions to manage the timing mismatches between payment obligations sent and payment receipts collected during business hours. Unlike overnight lending, which bridges gaps between close-of-business and the next morning, intraday facilities smooth the within-day flow of trillions of dollars through payment, clearing, and settlement systems.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Intraday Liquidity Facilities — Key Facts</div>

<img src="/svg/monetary.svg" alt="An abstract editorial mark for monetary policy." />

<div class="wiki-infobox-caption">Central banks lend money within business hours to prevent settlement gridlock.</div>

|   |   |
|---|---|
| **Core function** | Provide same-day credit to smooth intra-day payment obligations |
| **Time horizon** | Hours to minutes, not overnight |
| **Use case** | Settlement of securities, checks, wire transfers during trading hours |
| **Pricing** | Often free or very low-cost; goal is system stability, not profit |
| **Collateral** | Usually [high-quality securities](/bond/) or deposits |
| **Risk** | Operational: borrower must repay before close-of-business |
| **Examples** | Federal Reserve's Payment System Risk management programs; Fedwire and large-value payment systems |

</aside>

## Why Intraday Liquidity Matters

Imagine a morning in the U.S. Treasury market. A pension fund buys $100 million of 10-year bonds at 9:30 AM. The cash leg must settle (payment delivered, securities received) the same day. But the pension fund's bank has not yet collected payments from client redemptions. For a few hours, it is short $100 million—not because it is illiquid or insolvent, but because of the calendar: the *exact* timing of who owes money when does not align perfectly.

Without a mechanism to bridge these gaps, the bank would have to hold enormous precautionary cash buffers, or settlement would slow to a crawl. Instead, the central bank steps in via intraday facilities, lending the bank money for a few hours so it can settle promptly. By close of business, the pension fund's cash arrives, the bank repays the central bank, and the system moves smoothly.

This is distinct from overnight lending (like the [Federal Funds Rate](/federal-funds-rate/)). Overnight markets are about funding the balance sheet from close-of-business to the next morning. Intraday facilities are about managing cash flows *within* the trading day, minute by minute.

## How Intraday Facilities Work in Practice

The mechanics are straightforward but critical to systemic stability:

**Morning (Daylight Phase)**
A bank participates in multiple payment systems simultaneously. Its Fed wire terminal shows outgoing wires it must send (paying counterparties), incoming wires it expects to receive (being paid), and outstanding loans it may have taken. If outgoing payments exceed available cash and incoming receipts, the bank faces a shortfall. It requests an intraday loan from the central bank, collateralizing it with Treasury securities, agency paper, or other eligible assets.

The loan is credited to the bank's reserve account at the central bank. The bank can now send its payments, and the system continues. Other banks send payments to this bank; those payments also arrive via the wire system.

**Afternoon (Approach to Close)**
As the afternoon progresses, banks attempt to minimize their outstanding intraday borrowing. This is called "square up"—they attempt to match outgoing payments with incoming receipts so they owe as little as possible at close of business. Traders adjust large transactions, chains of settlement settle out, and the system naturally nets down.

**Close of Business**
The payment system closes at a fixed time (5 PM ET for Fedwire). All outstanding intraday loans must be repaid. The bank's reserve account is reconciled: money owed to the central bank is deducted, and the bank closes the day in balance.

If a bank cannot repay by close of business, it has violated its credit limit, and sanctions or enforcement may follow.

## Free or Subsidized Intraday Credit

One of the defining features of central bank intraday facilities is that they are typically *free* or very cheap—far cheaper than overnight lending at the [federal funds rate](/federal-funds-rate/) or commercial bank lines of credit. The Federal Reserve, for example, historically charged zero interest on intraday overdrafts (though it now requires collateral and may impose modest fees in some programs).

Why subsidize this credit? Because the goal is not to make a profit; it is to prevent settlement gridlock and systemic risk. If intraday credit were expensive, banks would hold larger cash buffers, locking up liquidity that could be lent to the real economy. By making it cheap and available, the central bank encourages banks to trust the system and minimize precautionary hoarding.

This is a form of [monetary policy](/monetary-policy/) in its own right: the central bank is smoothing money-market friction, not directing where credit flows.

## Collateral and Credit Risk

Intraday loans are always fully collateralized—usually with Treasury securities, agency [mortgage-backed securities](/mortgage-backed-security/), or eligible corporate bonds. The central bank marks to market and applies a haircut (discount) to the collateral value to cover potential losses if the borrower defaults.

But default risk is low in practice. Intraday lending is offered only to large, creditworthy institutions (primary dealers, big banks, major clearing houses). A bank that defaults during the day has already failed—there is no "overnight" recovery period. So central banks are comfortable lending to this narrow set with minimal haircuts.

The collateral requirement also serves a governance purpose: it limits the amount any one bank can borrow intraday (bounded by its collateral holdings) without explicit central bank approval.

## Intraday vs. Overnight Lending

The distinction is critical:

| Aspect | Intraday | Overnight |
|--------|----------|-----------|
| **Duration** | Within trading hours; repay by close of business | Overnight; repay next morning |
| **Pricing** | Free or subsidized | [Federal funds rate](/federal-funds-rate/) or negotiated overnight rate |
| **User** | Settlement and payment system participants | All banks needing balance-sheet funding |
| **Gridlock risk** | Settlement freezes if unavailable | Banks cannot function; credit transmission breaks |
| **Amount** | Limited by collateral; may be rationed in crisis | Unlimited within demand; central bank controls rate |

Overnight lending is about macroeconomic policy (controlling the money supply and interest rate). Intraday lending is about plumbing—keeping the pipes flowing.

## The Payment System Timing Problem

Why does this gap exist in the first place? It is purely technological and operational:

**Processing Delays**
A wire instruction sent at 9 AM may not settle until 11 AM, depending on clearing-house processing. In the interim, the sending bank has sent money but does not know yet whether it has received a matching payment.

**Batch Processing**
Some payment systems (particularly older check-clearing systems) settle in batches, not continuously. A bank may not know its full daily balance until mid-afternoon.

**Securities Settlement**
In Treasury and stock markets, trades happen during the day, but final settlement (securities delivered, cash paid) often happens end-of-day, hours after the transaction. A bank financing a large purchase must bridge the gap.

**Interbank Transfers**
A bank may have sent a payment to a correspondent bank in another country; the receipt may arrive hours later due to time zones or correspondent-banking delays.

All of these create predictable (but hard to schedule) mismatches that intraday facilities exist to bridge.

## Limits and Reforms

Central banks do set limits on intraday lending. The Federal Reserve, for instance, imposes credit limits per bank based on an assessment of that bank's financial condition and operational reliability. A bank that regularly approaches its limit, or that defaults on repayment, will have its limit reduced.

In the 2008 financial crisis, some institutions breached their limits or demanded more credit than available, signaling systemic stress. In response, the Federal Reserve expanded intraday lending programs and lowered haircuts to stabilize the system.

Modern central banks now publish data on intraday loan volumes, usage patterns, and collateral flows. This transparency helps regulators spot stress building in payment systems before it becomes critical.

## See also

<div class="wiki-seealso">

### Closely related

- [Federal Funds Rate](/federal-funds-rate/) — Overnight lending rate influenced by central bank policy
- [Liquidity Risk](/liquidity-risk/) — Why matching payment timing is critical to stability
- Haircut — Collateral discounts applied in central bank lending
- [Monetary Policy](/monetary-policy/) — Broader framework for central bank credit operations
- Settlement and Clearing — How payment and securities systems process transactions

### Wider context

- [Central Bank](/central-bank/) — Central banks' tools and mandates
- [Financial Stability](/systemic-risk/) — Why gridlock in payment systems threatens the broader economy
- [Reserve Requirements](/reserve-requirements/) — Bank liquidity rules that interact with intraday credit needs
- Payment Systems — Design of Fedwire, CHIPS, and other networks

</div>
