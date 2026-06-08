---
title: "Open Interest and Clearing: How Contracts Are Tracked"
description: "How the clearinghouse records open interest after novation; why the CCP is the counterparty to every open position."
keywords:
  - open interest tracking clearinghouse
  - how open interest is tracked by clearinghouse
  - novation clearing position
  - central counterparty open interest
  - ccp counterparty to all trades
image: "/svg/institutions.svg"
---

*After a futures or options trade is executed, the clearinghouse **novates** the contract—inserting itself as the counterparty to both buyer and seller.* This means **open interest**, the count of all contracts outstanding, is now a record of positions held against the clearinghouse, not between traders directly. Understanding how the clearinghouse tracks and reports **open interest** reveals the structure of derivatives markets and explains why the CCP's solvency matters to everyone holding a position.

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Open Interest and Clearing — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for institutions." />

<div class="wiki-infobox-caption">Open interest is the count of all outstanding contracts after novation; the clearinghouse is the counterparty to every one.</div>

|   |   |
|---|---|
| **Open interest definition** | Number of contracts held long and short at session end |
| **Who records it** | Clearinghouse; reported daily to exchange and public |
| **Novation** | Clearinghouse replaces original bilateral trade; becomes counterparty |
| **Why it matters** | Measure of market activity, liquidity, and institutional involvement |
| **Default scenario** | CCP's exposure to defaulted trader's position = open interest × (current price – entry price) |
| **Clearing member role** | Supervises clients' positions and margin; position data flows from CM to CCP |

</aside>

## What Open Interest Counts

**Open interest** is the total number of outstanding contracts in a given instrument at the end of a trading session. If 1,000 traders are long and 1,000 traders are short a crude oil futures contract, open interest is 1,000 (not 2,000)—because a long is always paired with a short. Open interest rises when new contracts are created (both parties are new or at least one is new to the market); it falls when contracts are closed (both buyer and seller exit).

**Example:** At the close of trading:
- Trader A buys 10 contracts. Trader B sells 10 contracts. Open interest: 10.
- The next day, Trader C buys 5 contracts. Trader D sells 5 contracts. Open interest: 15.
- Trader A sells 10 contracts to close. Open interest: 5. (Trader B's short is also closed.)

Open interest is distinct from trading volume (the number of contracts traded that day). A contract that is bought and sold 100 times in a single day counts as 100 volume but may contribute only 1 to open interest if the same two traders keep buying and selling to each other. Conversely, if 100 different pairs of traders each establish a position, volume is 100 and open interest rises by 100.

## The Role of Novation

**Novation** is the legal substitution of the clearinghouse as the counterparty to every trade. Here's the sequence:

1. **Original trade:** Trader A agrees to buy 1 crude contract from Trader B at $70/barrel.

2. **Novation:** The clearinghouse steps in and says: "Trader A, you are now long 1 contract *against me (the clearinghouse).* Trader B, you are now short 1 contract *against me.* Trader A and Trader B are no longer counterparties to each other."

3. **Result:** Open interest records 1 contract (the long-short pair is against the CCP, not bilateral between Traders A and B).

Why novate? Because if Trader B later defaults, Trader A's long position is still intact—it is owed by the clearinghouse, a nearly risk-free entity backed by a default fund and regulatory capital requirements. Without novation, Trader A would have unsecured exposure to Trader B's credit quality and would need to decide whether to accept or reject that risk. Novation eliminates bilateral credit risk and centralizes it on the clearinghouse.

## How the Clearinghouse Tracks Open Interest

The clearinghouse maintains a position ledger for each clearing member. A **clearing member** is a bank, broker, or market maker that is a direct participant in the clearinghouse:

| Trader (via Member A) | Position | Contracts | Against CCP |
|---|---|---|---|
| Trader A | Long | 10 | CCP owes A 10 longs |
| Trader B | Short | 10 | CCP owes B 10 shorts |
| Trader C | Long | 5 | CCP owes C 5 longs |

The clearinghouse's grand total open interest = 25 contracts: 15 longs (A's 10 + C's 5) and 10 shorts (B's 10). The market is imbalanced because the numbers are illustrative. In reality, every long is matched by a short.

Each day, after market close, the clearinghouse:

1. Receives trade data from the exchange (buyer, seller, quantity, price, time).
2. Updates each clearing member's position ledger.
3. Calculates new open interest by counting all long and short contracts.
4. Reports open interest to the exchange, which publishes it to the public (usually the next morning).

## Open Interest as a Liquidity Signal

Open interest is one of the primary signals of market health and liquidity:

- **Rising open interest + rising price:** New long positions are entering the market; bullish sentiment; stronger likelihood of further gains (sustained demand).
- **Rising open interest + falling price:** New short positions are entering; bearish sentiment; stronger downtrend (sustained selling).
- **Falling open interest + rising price:** Longs are exiting or shorts are covering; rally is driven by short-covering, may be shallow.
- **Falling open interest + falling price:** Decline is due to longs exiting, not new shorting; less conviction.

Traders use open interest to gauge whether a price move is backed by conviction or is just technical noise. A stock's options with rising open interest in out-of-the-money calls suggest traders are accumulating bullish leverage. Falling open interest in puts might suggest hedgers are exiting.

## Open Interest and Clearing Member Risk

From the clearinghouse's perspective, open interest is the measure of its exposure. If a clearing member defaults with 10,000 open contracts, the CCP must:

1. Immediately liquidate or hedge those 10,000 contracts.
2. Absorb any loss if the market moves against the defaulted position.
3. Cover the cost using the default fund and, if insufficient, other clearing members' capital.

This is why clearinghouses monitor large clearing members' positions carefully. A single member with, say, 20% of total open interest in a contract is a concentration risk. The CCP may require that member to reduce positions or post additional capital.

## Clearing Member Position Reports

Each clearing member must file position reports with the clearinghouse daily or intraday, showing:

- Total long and short contracts held.
- Position by customer (segregated account) and proprietary (house account).
- Large or concentrated customer positions.

The clearinghouse aggregates these reports, and regulators (SEC, CFTC) also monitor them for systemic risk. If one member is heavily short and a major catalyst moves prices sharply, that member could face losses that impair its capital and force liquidation of customers' positions.

## Public Reporting of Open Interest

Clearinghouses publish open interest figures publicly, usually the next morning after market close. For major contracts:

- **CME crude oil futures:** Open interest reported daily; often 1+ million contracts open at any time.
- **S&P 500 futures:** Open interest typically 0.5–2 million contracts, depending on season and volatility.
- **Treasury futures:** Open interest varies by tenor (2-year, 10-year, 30-year); the 10-year often leads with millions of contracts.

Traders and analysts watch open interest trends as a leading indicator of market direction, leverage, and conviction. A long-term rally on rising open interest suggests institutional accumulation; a rally on falling open interest suggests retail liquidation.

## Open Interest During Default

If a clearing member defaults, the clearinghouse must manage the member's open positions. The CCP's default procedures typically include:

1. **Position transfer:** Other members may accept the defaulted member's positions at a negotiated price; open interest is re-attributed.
2. **Liquidation:** The CCP auctions the positions to the highest bidder; open interest declines as positions are closed.
3. **Loss allocation:** Any shortfall is covered by the default fund; if depleted, losses are socialized among surviving members.

In the 2008 financial crisis, Lehman Brothers was a major clearing member. When it defaulted, its large open positions in futures and cleared derivatives (estimated at tens of billions of notional value) had to be transferred or liquidated. The clearinghouses' default procedures and default funds protected the market from cascading failures.

## See also

<div class="wiki-seealso">

### Closely related

- [Variation Margin vs Initial Margin](/variation-margin-vs-initial-margin/) — margin is collected against open interest
- [Clearing Fee How It Works](/clearing-fee-how-it-works/) — fees often scale with open interest levels
- [Counterparty Risk](/counterparty-risk/) — novation eliminates bilateral risk; CCP concentrates systemic risk
- [Futures Contract](/futures-contract/) — the primary cleared instrument tracked by open interest
- [Market Order](/market-order/) — trades create or reduce open interest

### Wider context

- [Central Bank](/central-bank/) — oversees clearinghouse solvency and systemic role
- [Systemic Risk](/systemic-risk/) — why large clearing members' open interest matters
- [Concentration Risk](/concentration-risk/) — when one member holds too much open interest
- [Leverage Ratio (Forex)](/leverage-ratio-forex/) — how clearing members use leverage against open positions
- [Credit Rating](/credit-rating/) — clearinghouse credit quality depends on default fund adequacy relative to open interest

</div>
