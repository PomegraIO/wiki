---
title: "Delivery-Versus-Payment Failure Scenarios"
description: "How delivery-versus-payment settlements fail: short squeezes, custodian delays, corporate actions. Remedies and outcomes for traders."
keywords:
  - delivery versus payment failure
  - settlement failure scenarios
  - dvp settlement fail
  - short squeeze settlement
  - custodian settlement delay
  - corporate action settlement risk
image: "/svg/trading.svg"
---

*A **delivery-versus-payment failure** occurs when one party cannot simultaneously deliver securities while receiving cash at settlement — stranding counterparties and triggering buy-ins, fails, or forced extensions. Understanding common failure modes and their remedies keeps traders and operations teams out of costly disputes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">DVP Failure — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">When settlement mechanics break down, liability flows to the party that cannot deliver.</div>

|   |   |
|---|---|
| **Core rule** | Securities and cash must exchange simultaneously; delay or absence of either triggers failure |
| **Who bears risk** | The party failing to deliver (often the seller in short sales) |
| **Typical resolution** | Buy-in, cash settlement at mark-to-market, or settlement extension |
| **Timeline** | Fails cost money daily; equity short fails incur [borrow fees](/short-selling/) and [mark-to-market losses](/mark-to-market/) |
| **Clearinghouse role** | Guarantees settlement; steps in to force buy-in or cash settlement |

</aside>

## The Mechanics of DVP Failure

**Delivery-versus-payment** is the standard for [equities](/stock/), [bonds](/bond/), and many [derivatives](/derivatives-hedging/) — both parties' obligations are linked. The buyer sends cash; the seller delivers securities. If either leg fails, both parties are suspended. The party obligated to deliver (usually the seller) is said to have a *settlement fail*, and the buyer becomes the *fail-to-receive* counterparty.

In centralized [clearinghouses](/), such as the [Depository Trust & Clearing Corporation](/dtcc/) (DTCC) in the US, the clearinghouse guarantees both sides of the trade. If a seller cannot deliver, the clearinghouse is legally obligated to deliver the securities to the buyer — and then forces the seller to buy them back or pay damages. This protection is why clearinghouse failures are rare; actual loss falls on the trading member that breached.

## Short Squeeze and Inability to Locate Shares

One of the most common DVP failure triggers is the **short squeeze**. A trader sells short expecting to repurchase shares later at a lower price. At settlement, the clearing broker must *locate* and *borrow* those shares on behalf of the short seller. If the borrow market is tight — too few shares available to lend, or borrow fees spike — the broker cannot deliver, and a settlement fail occurs.

In extreme short squeezes, the short seller may not be able to buy shares back cheaply (or at all) because the price has moved violently upward. The fails typically persist until:
- The short seller closes the position by buying shares at market price.
- The borrow supply increases, and the short position can settle.
- The clearinghouse forces a buy-in at fair value, compelling the short seller to cover.

High-profile examples include certain heavily shorted stocks during retail trading surges, where borrow availability collapsed and settlement fails accumulated. Each day a fail persists, the short seller accrues [carrying costs](/cost-of-debt/) — borrow fees, [mark-to-market losses](/mark-to-market/), and penalties.

## Custodian and Operational Delays

Another common scenario is a **custodian failure to deliver** due to operational error, system outage, or processing delays. A large institutional investor instructs its custodian (a bank or specialized [clearing agent](/custodian/)) to settle a trade. The custodian may experience:

- A software glitch in the settlement instruction flow.
- A missing or incorrect [DTC](/dtcc/) account number on the settlement ticket.
- A delay in matching the buyer's and seller's settlement instructions.
- A lock (a dispute between buyer and seller over trade terms that prevents settlement).

If the custodian cannot deliver by the T+2 or T+1 deadline, the fail-to-receive counterparty must decide whether to:
1. **Wait** — the fail-to-receive party may accept an extension (allowing additional time for the custodian to cure).
2. **Buy-in** — the buyer purchases the shares in the open market and charges the shortfall cost to the seller.
3. **Force cash settlement** — if settlement deadlines have passed, the buyer may demand mark-to-market cash payment instead of shares.

Operational fails typically resolve within one to three settlement cycles once the custodian corrects the error.

## Corporate Actions and Record-Date Misalignment

A subtler DVP failure arises when **corporate actions** occur between the trade date and settlement date. Suppose a short seller sells shares before an announced dividend [ex-date](/dividend-distribution/). On settlement day, the buyer is entitled to the dividend, but the short seller's broker must obtain and deliver those exact shares (or cash-settle the dividend equivalent). If the broker cannot coordinate delivery and dividend simultaneously, a failure cascades.

Similar issues occur with:
- **Stock splits** — a trade to deliver 1,000 shares may become undeliverable if a 2-for-1 split occurs mid-settlement.
- **Mergers and [acquisitions](/acquisition/)** — a seller may have agreed to deliver Target shares, but Target has been acquired. Settlement instructions must be rewritten for the acquirer's shares.
- **Rights offerings** — a seller is liable for subscription rights attached to the shares at trade-date settlement.

In these cases, fails often resolve through contractual amendment (the buyer and seller agree to adjust terms for the corporate action) or cash settlement at fair value.

## Buy-In Procedures and Costs

When a fail persists beyond market norms (typically 20 calendar days for equities in the US), the [clearinghouse](/dtcc/) or the fail-to-receive party may initiate a **buy-in**. The short seller is forced to repurchase shares at the best available market price, often at a significant markup if the stock has rallied. The short seller bears the full cost difference.

A buy-in is costly and punitive, which creates incentives for sellers to cure fails quickly. However, the short seller's broker also faces pressure: if the short seller cannot or will not buy shares to settle, the broker's own capital is at risk. In competitive markets, this credit risk can cause a broker to liquidate the short seller's entire account.

## Bilateral vs. Clearinghouse-Mediated Fails

Over-the-counter ([OTC](/over-the-counter-market/)) trades that do not clear through a central clearinghouse carry higher DVP failure risk. Buyer and seller are directly counterparties; there is no guarantor. If the seller fails to deliver, the buyer must:

1. Pursue a legal claim against the seller.
2. Buy shares in the open market (a buy-in) and seek damages.
3. Accept a renegotiated settlement date.

In cleared markets ([NYSE](/new-york-stock-exchange/), [NASDAQ](/nasdaq/)), the clearinghouse steps in automatically, reducing legal friction. Fails are still expensive, but the remedies are faster and more standardized.

## Fails and Regulatory Constraints

Regulators impose [short-sale locate rules](/short-selling/) specifically to prevent settlement fails. In the US, a broker must locate and reserve shares *before* a short sale is executed. Despite these rules, fails still occur in volatile markets where borrow supply cannot keep pace with new short positions.

Some markets ban naked short selling entirely (shares cannot be sold short unless already borrowed or reserved). Other markets allow it but impose penalties. The [SEC](/securities-and-exchange-commission/) and [FINRA](/finra/) publish fail-to-deliver data; high levels signal market stress or manipulation.

## Resolution and Settlement Finality

Once a fail is resolved — whether through delivery, buy-in, or cash settlement — settlement finality is achieved: the obligation is extinguished and both parties' records are cleared. In cleared markets, finality is usually declared when the clearinghouse confirms the settlement, typically one to two days after the original settlement date.

For parties on the losing end of a forced buy-in, the economic impact can be severe. A short seller caught in a hard-to-borrow squeeze faces compounding losses; a buyer subjected to a custodian delay may face opportunity cost or missed investment deadlines. This is why operational excellence and active monitoring of settlement instructions are critical in trading operations.

## See also

<div class="wiki-seealso">

### Closely related

- Settlement and Clearing — how trades move from execution to finality
- [Short Selling](/short-selling/) — mechanics and risks of selling borrowed shares
- [Custodian](/custodian/) — role of depositories and settlement agents
- [Mark-to-Market](/mark-to-market/) — daily valuation of open positions and failed trades
- T+2 Settlement — the two-day standard for equity settlement
- [Borrow Fees and Short Squeezes](/short-selling/) — why short fails cluster during supply crunches

### Wider context

- [Counterparty Risk](/counterparty-risk/) — credit exposure between trading parties
- [Clearinghouse](/dtcc/) — central guarantors of settlement
- [Liquidation](/liquidation/) — forced closure of accounts that cannot meet obligations
- [Broker](/broker/) — settlement intermediary for retail and institutional traders
- [Securitization](/securitization/) — how underlying assets are packaged and settled

</div>
