---
title: "How Partial Settlement Works in Securities Markets"
description: "Partial settlement occurs when a fraction of a failing trade settles on time while the remainder fails, creating unresolved positions and counterparty obligations."
keywords:
  - how partial settlement works securities
  - partial settlement trade failure
  - securities settlement
  - trade failure mechanics
  - settlement default
---

*A **partial settlement** happens when only a fraction of a trade's shares or bonds actually exchange hands on settlement day. The buyer receives fewer shares than purchased, the seller delivers fewer than obligated, and both parties are left with open positions and ongoing obligations to the counterparty. Partial settlement creates operational complexity because each side must manage both the settled portion and the unsettled remainder—two separate obligations in two separate accounts.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Partial Settlement — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Not all trades settle fully on day one; the remainder becomes an open position.</div>

|   |   |
|---|---|
| **Trigger** | Buyer or seller lacks sufficient funds/securities on settlement day |
| **Who bears risk** | Both parties; unresolved portion remains live obligation |
| **Typical duration** | Days to weeks; driven by delivery capability or funding |
| **Pricing of remainder** | Typically repriced daily or settled at original contract price |
| **Default event** | If unsettled portion remains beyond grace period, becomes failure |
| **Custody and financing** | Unsettled shares may incur repo costs or dividend/voting risk |
| **Frequency** | Rare in equity markets; more common in bonds and repo |

</aside>

## What Triggers a Partial Settlement?

A partial settlement occurs when one side of a trade cannot deliver full performance on settlement day. Common causes:

1. **Insufficient funds**: The buyer has only $500,000 available but owes $1,000,000. They pay for 5,000 shares instead of 10,000.

2. **Insufficient securities**: The seller promised 10,000 shares but only has 6,000 in their account. They deliver what they have; 4,000 remain unsettled.

3. **Delayed custody transfer**: Securities are en route from a custodian or transfer agent but haven't arrived by settlement time. The custodian delivers a partial batch.

4. **Corporate actions interference**: A dividend cutoff, rights offering, or stock split occurred between trade date and settlement. The number of deliverable shares changed unexpectedly.

5. **Reconciliation errors**: Both parties agree the trade exists, but their settlement instructions (quantity, ISIN, account details) don't match perfectly. They settle what matches and hold the rest.

In a normal, frictionless market (which rarely exists), partial settlements would be rare. But they occur regularly in international trades, repo markets, and bond trading because logistics and funding are genuinely difficult to synchronize.

## The Accounting and Operational Chain

Once a partial settlement occurs, both parties must track two positions:

| State | Position | Status |
|-------|----------|--------|
| **Settled portion** | Buyer: 5,000 shares acquired; Seller: $500,000 received | Closed; legal ownership transferred |
| **Unsettled portion** | Buyer: 5,000 shares still owed; Seller: 5,000 shares still owed | Open obligation; counterparty risk active |

The buyer now holds 5,000 shares and an open purchase for 5,000 more at the contract price. The seller has received $500,000 and an open sale obligation for 5,000 shares.

This dual state creates several problems:

**Dividend and Voting Rights**: The buyer owns the 5,000 settled shares. Do they own dividend rights on the unsettled 5,000? Typically no—until settlement, the seller retains those rights. This creates a mismatch if a dividend is declared during the settlement gap.

**Financing Costs**: If the buyer funded the purchase with a loan, they're now paying interest on $1,000,000 borrowed but only holding $500,000 worth of security. The unsettled portion must be financed separately or the trade must be repriced.

**Counterparty Risk**: Both parties have open exposure until the remainder settles. If the counterparty defaults or becomes insolvent, the unsettled portion may never settle; the non-defaulting party is now an unsecured creditor.

## How the Unsettled Portion Is Handled

Settlement agreements differ, but common approaches are:

### Rolling Obligation (Most Common)

The unsettled portion remains an open trade with the same contract price and terms. It settles "as soon as feasible," often with a daily reaffirmation:

- Both parties confirm the unsettled quantity every day
- If funding or securities become available, settlement occurs
- If a deadline passes (typically 5–10 business days), the trade fails and may trigger remediation (buy-in/forced delivery)

### Repricing (Less Common)

The unsettled portion is repriced at current market rates. The buyer and seller might agree: "We settled 5,000 shares at $100. The remaining 5,000 will settle tomorrow at market price, or we'll cancel the remainder and settle cash difference."

This approach is riskier because it reopens negotiation on price, creating potential disputes.

### Cancellation and Buy-In

The buyer or seller can demand the unsettled portion be cancelled, and then execute a new trade at current market prices to close the gap. If the market has moved against the original seller, they face a loss. This is a form of "buy-in" or "sell-out"—forced to cover at a different price.

## Real-World Scenario: Partial Settlement in a Cross-Border Trade

A U.S. investor (Buyer) agrees to buy 10,000 shares of a Tokyo-listed stock from a London bank (Seller). Trade date: Monday.

**Settlement day (Wednesday)**:

- The Tokyo exchange processes Japanese settlements at 3 PM Tokyo time (11 PM London, 6 AM New York)
- The buyer's custodian in Japan has only 6,000 shares available; the full 10,000 won't arrive until Thursday morning
- The seller delivers 6,000 shares to the buyer's account; 4,000 remain unsettled

**Overnight Wednesday–Thursday**:

- Both parties confirm: 6,000 settled at contract price; 4,000 open
- The buyer has now paid $600,000 (assuming $100/share) and received 6,000 shares
- The seller has received $600,000 and delivered 6,000 shares; owes 4,000 more
- The buyer is exposed to counterparty risk on $400,000 owed
- The seller is exposed if the market price moves and the buyer no longer wants the remainder

**Thursday morning (Tokyo time)**:

- The remaining 4,000 shares arrive; both parties confirm and complete settlement
- The transaction closes; no further obligations

This scenario was straightforward—just a timing gap. But if the buyer or seller faces a financial crisis or bankruptcy during that overnight period, the unsettled portion becomes a contested claim.

## Partial Settlement vs. Trade Failure

A **partial settlement** is a controlled outcome: both parties expected some delay and agreed to handle it. A **trade failure** is when the unsettled portion doesn't settle within the grace period (typically T+4 or T+5) and is then forced to fail.

Once a trade fails, regulatory rules (like Reg SHO in the U.S., or CSDR in Europe) kick in. The non-defaulting party may force a buy-in or sell-out—liquidating the position at market price, and the defaulting party must make good the difference. This is expensive and reputationally damaging.

Partial settlement, by contrast, is temporary—a both-sides acknowledgment that logistics or funding created a gap, but the position is live and both parties are working to close it.

## Partial Settlement in Different Market Segments

### Equity Markets
Relatively uncommon. Most brokers are well-funded and have established securities transfers. Partial settlements occur mainly in:
- Large block trades with tight settlement windows
- International trades crossing multiple custody systems
- Corporate actions (spinoffs, special dividends) that change deliverable quantity

### Bond Markets
More common. Reason: bonds settle over multiple days, and sellers often source bonds from their custodian or via repo only after receiving buyer funds. Partial delivery-versus-payment (DvP) is routine.

### Repo and Collateral Markets
Very common. Repo trades are short-term; if collateral isn't transferred by end-of-day, a partial repo settlement occurs—the cash leg settles but the security leg rolls forward. Both parties will typically adjust pricing (add repo rate adjustment) and reattempt settlement the next day.

### Derivatives and Clearing Houses
Rare. Most derivatives settle via central counterparties (CCPs) that guarantee settlement; partials are absorbed by the CCP, not seen by end users.

## Cost and Risk of Unsettled Positions

Leaving a position unsettled carries real costs:

| Cost | Impact |
|------|--------|
| **Financing** | Buyer pays interest on full purchase price but receives only partial security; seller may need to finance the unsettled obligation |
| **Dividend/voting rights** | Mismatch if corporate action occurs during settlement gap |
| **Mark-to-market** | If market price moves, unrealized loss/gain on unsettled portion |
| **Counterparty default** | If seller becomes insolvent before settling, buyer is unsecured creditor |
| **Regulatory buy-in cost** | If failure extends beyond grace period, forced buy-in at potentially much higher market price |

A partial settlement that lasts days costs less than one lasting weeks. Most settlement agreements include penalty rates or forced buy-in timelines to incentivize closure.

## Settlement Instructions and Prevention

To minimize partial settlements, institutional traders:

- **Pre-fund**: Buyer maintains sufficient cash; seller pre-positions securities in the settlement custodian
- **Alignment of settlement instructions**: Buyer, seller, and both custodians agree on account numbers, ISIN, quantity, and settlement date *before* trade execution
- **Standing settlement instructions (SSI)**: Automated instructions held with custodians reduce manual error
- **Synchronized settlement**: Using central counterparty clearing (for eligible products) guarantees settlement if either side defaults

## See also

<div class="wiki-seealso">

### Closely related

- Settlement default — When unsettled portion fails and trade failure rules apply
- Trade failure — Outcome if partial settlement doesn't close within grace period
- [Delivery versus payment](/delivery-versus-payment/) — Settlement mechanism underlying partial settlement scenarios
- [Custody](/custodian/) — Third parties who hold securities and execute settlement
- [Counterparty risk](/counterparty-risk/) — Active during unsettled portion
- [Repo](/repurchase-agreement/) — Market where partial settlement is common; collateral may settle separately from cash

### Wider context

- [Securities and exchange commission](/securities-and-exchange-commission/) — Regulator of settlement rules
- [Stock](/stock/) — The core instrument that settles partially
- [Bond](/bond/) — Common instrument in partial settlement scenarios
- [Credit risk](/credit-risk/) — Unsettled position carries credit exposure

</div>
