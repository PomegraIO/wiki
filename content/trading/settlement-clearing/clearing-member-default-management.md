---
title: "Clearing Member Default Management"
description: "The auction and portfolio close-out procedure a central counterparty executes when a member fails, protecting the market and non-defaulting members."
keywords:
  - ccp-procedures
  - clearing-default
  - auction-mechanism
  - portfolio-transfer
image: "/svg/trading.svg"
---

*When a clearing member defaults—unable to meet margin calls or variation margin—the [central counterparty](/central-counterparty-clearing/) (CCP) must quickly transfer or liquidate its open positions. Default management is the CCP's core function: a choreographed procedure designed to isolate failure and protect the broader market from cascading losses.*

## Why CCPs exist: the default problem

In the days before [central counterparties](/central-counterparty-clearing/), traders settled bilaterally with each other. If one side failed, the other faced immediate and unpredictable loss. The CCP's innovation is to become the buyer to every seller and the seller to every buyer—a neutral middle layer. This **novation** means that if Trader A goes bust, Trader B's contract is now with the CCP, not with Trader A.

But CCPs themselves face default risk. If a major clearing member fails, it might owe billions to the CCP. That's when default management procedures activate. These procedures were stress-tested through the 2008 financial crisis and the 2020 volatility spike, and they are now codified in regulations ([Dodd-Frank](/dodd-frank-act/) in the US, EMIR in Europe).

## The timeline of default

A member's default rarely comes as total surprise. The CCP monitors [counterparty risk](/counterparty-risk/) in real time:

1. **Early warning**: The member's margin cover drops below regulatory minimums, or it fails to pay [variation margin](/variation-margin/) on time. The CCP sends notices and may freeze new trading.

2. **Default declaration**: The CCP's Risk Committee formally declares the member in default—usually after the member fails to cure a breach within a defined window (often 1–2 hours).

3. **Position freeze**: All trading by the defaulting member ceases immediately. No new orders; existing orders are cancelled.

4. **Liquidity support**: The CCP and other clearing members inject temporary liquidity to prevent a cascade. The default fund (collateral posted by all members ex-ante) becomes available.

5. **Close-out period**: The CCP has 24–72 hours (varies by CCP and product) to auction positions or execute an orderly wind-down.

## The auction mechanism

The CCP's goal is to replace the defaulting member's portfolio without destabilizing prices. The auction unfolds in rounds:

**Round 1: Solicitation**
- The CCP publicly announces the portfolio for auction: notional size, duration, sector breakdown, credit quality if relevant
- Other clearing members (usually the top tier—dealers and large prop firms) are invited to bid
- The CCP also solicits bids from non-members (other brokers, hedge funds) to broaden the buyer pool

**Round 2: Bidding**
- Bidders submit sealed bids specifying which portions of the portfolio they'll accept and at what **price adjustment** (or cash adjustment—a positive amount if they want the CCP to pay them, negative if they demand a discount)
- For equity portfolios, individual stock adjustments vary; for derivative positions, the adjustment reflects the counterparty risk premium bidders demand

**Round 3: Allocation**
- The CCP awards tranches to bidders, prioritizing those offering the best economic terms (lowest cost to the CCP and default fund)
- If no single bid covers the entire portfolio, the CCP splits it across multiple bidders, often imposing transfer fees to incentivize full acceptance

## How auction prices are set

The auction price reflects **replacement cost**, not market price. If the market price of a stock is $100, but a bidder must assume the default risk and operational headache of inheriting the position, they bid lower—say, $99.50. The CCP pays the $0.50 adjustment from the default fund.

For derivatives (futures, swaps, options), adjustments are more complex:
- A trader holding a [call option](/call-option/) deep in-the-money is valuable; bidders compete for it
- A worthless far-out-of-the-money option trades at bid-ask spread or is left behind as a "stub" (minimal net present value)
- Counterparty-specific features (credit quality, funding costs) inflate the adjustment

The CCP aims to complete the auction in hours, not days, to minimize uncertainty and secondary price moves. In the 2008 Lehman bankruptcy, for instance, exchanges and CCPs auctioned his portfolio in a matter of hours across multiple sessions.

## The default fund and liquidity support

If auction adjustments exceed the defaulting member's own margin buffer, the default fund (funded by all clearing members proportionally) covers the shortfall. This is why non-defaulting members post margin upfront—they are, in effect, insuring each other.

If the default fund is insufficient (an extreme scenario, though theoretically possible in a multi-member cascade), the CCP may:
- Invoke a **capped assessment** on non-defaulting members (additional loss-sharing above the default fund)
- In extreme cases, seek central bank liquidity or government support

The [Dodd-Frank Act](/dodd-frank-act/) and EMIR mandate that default funds cover at least the default of the two largest members. Post-2008, many CCPs increased buffers to three or more largest members. The actual default fund size for a large CCP (e.g., LCH, CME Clearing) ranges from $5–15 billion, depending on market stress scenarios.

## Portfolio-specific challenges

**Equity portfolios**: Generally liquid; auctioned in hours. The main risk is a gap in prices if the market shifts overnight or if the portfolio contains illiquid mid-caps. Most clearing members accept equity portfolios as long as the adjustment is reasonable.

**Derivatives**: More complex. Swap and option positions are bespoke; few bidders can actually assume the operational burden. The CCP may be forced to hedge positions or unwind them piecemeal, accepting slippage.

**Cleared repo**: Particularly sensitive. A large failed repo member means massive haircut or liquidity adjustments. CCPs managing repo (e.g., Eurex Repo) maintain separate ring-fenced default procedures.

**Multi-product members**: A member clearing equities, futures, and swaps creates interdependencies. A failed member might have net funding rights in one product but owe in another. The CCP must co-ordinate auctions across silos to avoid artificial breaks.

## Segregation and client protection

When a clearing member defaults, the question "whose positions are these?" becomes critical. Under [omnibus account](/omnibus-account-structure/) structures, the CCP may not know which positions belong to which client of the failed member. This opacity forced regulators to mandate **individual segregation** (each client has a separate sub-account at the CCP) in major markets post-2008.

Individual segregation allows the CCP to port **non-defaulting** clients' positions to another broker immediately, without waiting for the full auction. Only the defaulting member's proprietary positions enter auction. This has become the standard in equities and derivatives.

## Speed and operational reality

Modern CCPs aim to auction within 1–4 hours of default declaration. Automated systems calculate net exposures, mark positions to market, and identify which tranches are saleable. Human traders then manually price adjustments and market to bidders.

Obstacles to speed:
- **Legal complexity**: The failed member's assets are often in insolvency proceedings; the CCP must coordinate with trustees
- **Distributed custody**: Positions held at multiple custodians in different time zones (a London/Tokyo/New York portfolio) are hard to move in parallel
- **Contagion risk**: If the failed member was a counterparty to others, those members may face sudden losses, triggering a secondary wave of stress

## See also

<div class="wiki-seealso">

### Closely related

- [Central Counterparty Clearing](/central-counterparty-clearing/) — the institution managing the default process
- [Counterparty Risk](/counterparty-risk/) — the risk being managed through CCPs
- [T+1 Settlement Migration](/t-plus-one-migration/) — how faster settlement affects default windows
- [Omnibus Account Structure](/omnibus-account-structure/) — segregation of client positions during default
- [Variation Margin](/variation-margin/) — daily adjustments that trigger default checks
- [Default Fund](/default-fund/) — the collateral that backs the auction
- [Margin Call](/margin-call-forex/) — the trigger for default declarations

### Wider context

- [Systemic Risk](/systemic-risk/) — why CCP defaults matter to the whole market
- [Securities Dematerialization](/securities-dematerialization/) — how electronic book-entry settlement supports auctions
- [Dodd-Frank Act](/dodd-frank-act/) — US regulation mandating CCP default procedures
- [Liquidation](/liquidation/) — the broader process of unwinding failed firms
- [Credit Risk](/credit-risk/) — the underlying risk being managed

</div>
