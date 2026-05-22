---
title: "Fail to Deliver Impact"
description: "How delivery failures distort price and create settlement risk; mechanics and systemic consequences."
keywords:
  - fail to deliver
  - FTD
  - settlement failure
  - market impact
---

*A **fail-to-deliver** occurs when a seller does not deliver securities to the buyer by [settlement](/wiki/settlement-cycles/). The buyer is left without shares, the seller retains cash, and the security remains "fails-to-deliver" until delivered, creating localized scarcity and price distortion.*

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Definition** | Seller fails to deliver shares by T+2 settlement |
| **Cause** | Naked short selling, operational errors, localized shortage |
| **Duration** | Hours to weeks (enforced after T+4 in most markets) |
| **Price effect** | Upward pressure; fails create artificial scarcity |
| **Systemic risk** | Usually low; containment at [CCP](/wiki/central-counterparty-clearing/) level |

</aside>

## How fails occur: mechanics and the naked short connection

A **fail-to-deliver** happens when a seller has sold shares it does not own (a [short sale](/wiki/short-selling/)) and fails to borrow them before settlement. The DTCC's [settlement](/wiki/settlement-cycles/) system is T+2 (trade on Monday, deliver Wednesday). A seller shorts 1,000 shares on Monday, expecting to borrow them by Wednesday. But all available shares are already borrowed (lenders exhausted). Wednesday arrives, the seller cannot deliver. Now there's a fail—the buyer is missing 1,000 shares; the seller is missing nothing (they've already received cash). This asymmetry is the core of the problem.

Fails can also occur from **operational errors**: a custodian loses track of shares, an settlement instruction is misrouted, or a [transfer agent](/wiki/transfer-agent/) is backlogged. These are typically resolved within days. But **naked short fails**—shorts without any borrow intention—can persist for months, especially in micro-cap or distressed stocks where locating borrow is hard or impossible.

## Pricing impact: artificial scarcity and upward bias

When a stock is on the **fail-to-deliver list** (DTCC publishes fail data every two weeks), it creates a perception of artificial scarcity. If 100,000 shares are fails, the market has 100,000 fewer shares than it should. Buyers who expected to own shares are disappointed; they bid harder to acquire available shares, pushing price up. Short-sellers desperate to cover their fails also bid aggressively (to locate borrow), further pressuring price upward. Studies show that stocks with heavy fails underperform expectations in the short term but eventually correct downward once fails are cleared and reality reasserts itself. The 2008 Lehman bankruptcy and 2020 meme-stock surges (GameStop, AMC) saw massive fails; short-sellers covered at inflated prices as pressure mounted.

## Duration and regulatory enforcement

**U.S. regulation** (SEC [Regulation SHO](/wiki/regulation-sho/)) mandates that fails be resolved within T+4 (four business days). After T+4, the short-seller *must* buy-in the securities at market price (forced covering) to force delivery. However, enforcement is uneven. During volatile periods (2008, 2020), the SEC temporarily halted buy-in requirements, allowing fails to linger for weeks. Stocks with persistent fails become difficult to borrow; lenders charge 100%+ annualized borrow fees (compared to 0.5% for stocks with ample borrow). This makes naked shorting economically irrational for legitimate investors but appealing to bad actors willing to accept the risk to manipulate price.

## Systemic risk: usually contained, but concentration matters

A single stock with 10 million fails is manageable; the CCP and market can absorb it. But if a systemic event (e.g., a major clearing member defaults) causes millions of fails across hundreds of stocks, settlement cascades can freeze. The 2008 crisis saw Lehman Brothers' fails surge to billions; DTCC and regulators had to manually work through the position. Modern systems are more resilient—CCPs hold [default funds](/wiki/ccp-default-waterfall/) and [liquidity facilities](/wiki/liquidity-pool/) to handle stress. But **concentration risk** remains: if a single short-seller has built massive fails (millions of shares across multiple stocks), their inability to cover could destabilize markets in those stocks.

## Market-wide data: fails and short interest

The DTCC publishes **fail-to-deliver data** biweekly, showing the total fails in each security. Researchers compare this to [short interest](/wiki/short-selling/) (short positions outstanding) to assess how many shorts are actually failing. In most stocks, fails are <1% of shares outstanding—noise. But in heavily shorted, illiquid names, fails can be 5–10% of float, creating obvious market distortion. This is why advocates for tighter short-selling restrictions often cite fail data—they argue it proves naked shorting is widespread and market manipulation occurs. Critics counter that fails are mostly operational and quickly resolved, so regulation is unwarranted.

## Borrow and stock lending: the mitigation

The equity lending market exists to *prevent* fails. Before shorting, a short-seller must locate borrow—usually from a custodian, prime broker, or institutional lender. A share is **on loan** from the lender to the short-seller. The short-seller pays borrow fees (daily, accruing) and can be recalled by the lender at any time. The availability and cost of borrow directly determine how many shares can be shorted. In stocks with ample shares available to lend (mega-caps like Apple), borrow is cheap (near 0%), and short-selling is easy. In illiquid or hard-to-borrow stocks, borrow fees spike (10%–100%+ annualized), capping naked short-selling because the economics break. Market-making and arbitrage require borrow; naked manipulation doesn't, so manipulation happens in hard-to-borrow names where fails are endemic.

## Fails and the meme-stock cycle

The 2021 meme-stock surge (GameStop, AMC) revealed fail mechanics to retail traders. These stocks had massive short interest and poor borrow availability. Fails accumulated. Short-sellers were trapped—they couldn't deliver on fails and had to cover at escalating prices. Retail traders, aware of the fails, coordinated buying to force squeezes. Short-sellers covered, buying in fails at $200, $300, $400 per share (vs. pre-squeeze $5–$20). The fails eventually cleared, but not before massive wealth transfers and regulatory scrutiny. The SEC later tightened Regulation SHO enforcement, mandating shorter deadlines for buy-ins and increasing borrow-locate requirements.

## Preventative measures and regulatory proposals

**Market-wide initiatives**:
1. **Shorter settlement cycles**: Moving from T+2 to T+0 (same-day settlement) would eliminate the window for fails. The SEC has proposed T+1; full T+0 is years away.
2. **Mandatory borrow** (pre-borrow rule): Requiring all shorts to have located borrow *before* the sale, not afterward. This would nearly eliminate naked shorting. Critics argue it would reduce market liquidity and short-selling's role in price discovery.
3. **Fail haircuts**: Penalizing fails with interest charges or forced buy-ins on shorter timelines (T+3 instead of T+4).
4. **Blockchain settlement**: Real-time blockchain settlement would eliminate fails by making settlement instantaneous.

Each measure has trade-offs. Faster settlement increases operational burden on custodians. Mandatory borrow reduces shorting capacity and liquidity. Blockchain is promising but unproven at scale.

---

<div class="wiki-seealso">

### Closely related
- [Settlement Cycles](/wiki/settlement-cycles/) — T+2, T+1, and settlement timelines
- [Short Selling](/wiki/short-selling/) — Selling shares you don't own
- [Stock Lending](/wiki/stock-lending-market/) — Borrowing shares for short-selling
- [Regulation SHO](/wiki/regulation-sho/) — SEC rules on short-selling and fails

### Wider context
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — DTCC role in processing settlement
- [Market Manipulation](/wiki/insider-trading-law/) — Using fails to artificially depress price
- [Short Squeeze](/wiki/short-squeeze/) — Forced covering when fails accumulate
- [Naked Short Selling](/wiki/naked-short-selling-ban/) — Selling without locating borrow

</div>
