---
title: "Failed Settlement"
description: "Operational and financial condition when a trade fails to settle on its intended delivery or payment date."
keywords:
  - failed settlement
  - settlement failure
  - securities settlement
  - trade settlement
  - clearing and settlement
image: "/svg/institutions.svg"
---

*A **failed settlement** occurs when a trade does not settle—meaning the buyer does not receive the asset and the seller does not receive cash—on the agreed settlement date. In equity markets, this typically means a seller fails to deliver shares; in fixed income, it means failure to deliver bonds or cash. A settlement failure disrupts the entire [cash conversion cycle](/cash-conversion-cycle/) for both parties and can create cascading operational and credit costs across the financial system.*

<div class="wiki-hatnote">

For the broader mechanics of how trades move from execution to final settlement, see [Straight-through processing](/straight-through-processing/). For central counterparty safeguards against failure, see Clearinghouses.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Failed Settlement — key facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for financial institutions and regulatory frameworks." />

<div class="wiki-infobox-caption">When a trade fails to settle, both parties face operational costs, extended credit risk, and potential regulatory penalties.</div>

|   |   |
|---|---|
| **What it is** | Non-delivery of securities or cash on the scheduled settlement date |
| **Common cause** | Missing collateral, operational error, counterparty failure, custody chain breakdown |
| **Settlement date** | T+1 (same-day or next-day settlement) in modern equity markets; varies for bonds and derivatives |
| **Consequences** | Lost interest income, collateral calls, reconciliation costs, potential [counterparty risk](/counterparty-risk/) |
| **Resolution** | Force settlement, cash compensation, or mutual agreement to cancel the trade |
| **Regulatory consequence** | Fines, buy-in penalties, or forced liquidation of the security |

</aside>

## Why settlements fail

A settlement failure is fundamentally an operational breakdown, but it exposes financial risk. The most common cause is simple: the seller does not have the securities to deliver. This may happen because the seller miscounted inventory, because a prior trade failed to settle and left the seller short of the asset, or because the seller sold more shares than it actually owned (a naked short position).

In some cases, a seller deliberately withholds delivery because the price has moved against the contract, hoping to renegotiate or delay. More often, the failure stems from a custody chain rupture: securities are held in multiple nested accounts (buyer's broker, prime broker, custodian), and one link in the chain miscommunicates or loses track of the asset. A stock transfer agent might reject a certificate due to incorrect paperwork. A securities depository (like the Depository Trust Company in the US) might be unable to locate a position.

Payment failures—where the buyer does not provide cash—are less common in liquid markets because buy-side operations are more regimented, but they happen. A buyer's bank might block a wire transfer due to sanctions screening. A buyer facing a sudden liquidity crunch might simply not move the cash on time.

In cleared markets, a clearinghouse carries the risk that a defaulting member will not deliver. The CCP steps in and uses its insurance fund to settle with the other side. In bilateral settlement, there is no intermediate buffer—the failure is between the original buyer and seller.

## The cascade of costs

A single failed settlement can trigger a chain of downstream failures. Suppose a seller owes securities to Buyer A, who in turn owes them to Buyer B. If the seller fails, Buyer A is unable to deliver to Buyer B, creating two failures. Buyer B may have simultaneously promised the same securities to Buyer C, and so on. The result is a "fail chain" that can paralyse a market corner if the security is illiquid or in short supply.

Each failed trade generates financial friction. The buyer, who expected to receive a security on day T, is denied it. The buyer loses one day of [dividend](/dividend/) income or interest accrual. If the buyer is a fund manager, the buyer may face redemption pressure from investors who expected certain holdings. If the buyer financed the purchase with a repo loan, the buyer still owes interest on cash it never received, creating a cash flow gap.

The seller, who expected to receive cash, is similarly stuck. The seller loses one day of interest income on the proceeds and may face its own funding commitments downstream. In a liquid market, the parties can buy or sell the security elsewhere to "make whole," but this requires posting additional cash or collateral and may lock in a loss if the price has moved.

Regulators take fails seriously because widespread settlement failures can spill into systemic risk. If fails cluster in a single security or clearing member, they signal operational or financial distress. A major fail in US Treasury markets, for instance, could ripple into the entire fixed-income ecosystem.

## Operational and regulatory responses

Markets and regulators have adopted several levers to manage failed settlements:

**Fails penalties and buy-in mechanisms:** If a seller fails to deliver, exchanges and clearinghouses may impose penalties or allow the buyer to force a buy-in—purchasing the security in the open market and billing the seller for any premium over the original contract price. US equity exchanges, for example, impose automatic buy-ins on fails older than a specified number of days.

**Shortened settlement cycles:** The industry has moved from T+3 (three days after trade date) to T+1 (next day) in many equities markets, and toward T+0 (same day) in some segments. A shorter cycle leaves less room for operational failure, though it imposes heavier technology and collateral burdens on participants.

**Regulatory buy-in orders:** Regulators like the SEC have the power to order forced buy-ins of persistent fails to clear backlogs.

**Collateral and margin tightening:** Clearinghouses and banks impose stricter collateral requirements and margin calls on counterparties with a history of fails.

**[Straight-through processing](/straight-through-processing/):** Automating the entire settlement workflow from trade confirmation to final delivery reduces manual re-entry errors and speeds matching.

**Mutual agreement to fail:** In some cases, the buyer and seller agree to a brief extension (a "fail buy-in" grace period) rather than liquidating forced settlement, reducing disruption to both.

## Settlement fails in different asset classes

**Equities:** Concentrated in small-cap stocks and heavily shorted securities. A short seller must borrow shares before sale; if the lending pool is exhausted, delivery becomes impossible.

**Fixed income:** Bond fails are less visible but potentially larger in notional value. US Treasury fails, though rare, have triggered regulatory intervention. Fails in corporate bonds and municipals tend to spike during credit events or market dislocations.

**Derivatives:** In cleared markets, the clearinghouse absorbs default risk, so a clearing member's failure does not directly cascade to other members. However, a CCP itself could default in an extreme scenario, which is why CCP safeguards (capital, insurance funds, stress testing) are critical.

## See also

<div class="wiki-seealso">

### Closely related

- [Straight-through processing](/straight-through-processing/) — automated workflows that reduce settlement failures
- Clearinghouses — institutions that guarantee settlement in cleared markets
- [Counterparty risk](/counterparty-risk/) — credit exposure created by failed settlement delays
- [Clearing mandate](/clearing-mandate-emir-dodd-frank/) — post-2008 regulation requiring central clearing to prevent cascading fails
- [Trade compression](/trade-compression/) — mechanism to reduce notional outstanding and exposure concentration

### Wider context

- [Over-the-counter market](/over-the-counter-market/) — bilateral markets prone to settlement opacity
- [Securities and exchange commission](/securities-and-exchange-commission/) — US regulator overseeing settlement practices
- [Systemic risk](/systemic-risk/) — interconnection risk that settlement failures can amplify
- [Central bank](/central-bank/) — backstop liquidity provider during settlement crises

</div>
