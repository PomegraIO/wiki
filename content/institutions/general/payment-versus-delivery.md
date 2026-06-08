---
title: "Payment Versus Delivery"
description: "Settlement principle ensuring securities transfer occurs only when cash payment simultaneously clears, eliminating counterparty risk in the interim."
keywords:
  - settlement
  - dvp
  - delivery versus payment
  - counterparty risk
  - securities transfer
  - cash settlement
image: "/svg/institutions.svg"
---

*[Payment versus Delivery](/payment-versus-delivery/) (often abbreviated DVP, for Delivery Versus Payment) is a [settlement](/stock-exchange/) rule governing how securities and cash change hands during a trade: the transfer of the security occurs if and only if cash payment clears simultaneously. This atomic coupling eliminates the risk that one party receives their goods while the other receives nothing.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Payment Versus Delivery — key facts</div>

<img src="/svg/institutions.svg" alt="An editorial mark for financial institutions." />

<div class="wiki-infobox-caption">The settlement principle that links securities transfer to cash payment to eliminate credit risk.</div>

|   |   |
|---|---|
| **Also called** | Delivery versus payment (DVP) |
| **Core principle** | Securities move only when cash clears, and vice versa |
| **Risk it eliminates** | [Counterparty risk](/counterparty-risk/) during settlement |
| **Timing** | Same day or within defined settlement window |
| **Regulator** | National securities authorities and central banks |
| **Standard model** | T+2 (settlement two business days post-trade) |

</aside>

## The settlement problem it solves

In the earliest days of securities trading, deals closed with a handshake: one party promised to deliver shares, the other promised to send money. But promises are fragile. If Counterparty A handed over the certificate and Counterparty B never paid, A had a legal claim but no shares. If B sent the cash and A never delivered, B owned nothing but an IOU. The interval between delivery and payment was a chasm of credit risk.

This risk was material. Securities trades involved large sums, settlement took days or weeks, and the distance between delivery and payment meant both parties had [credit exposure](/credit-risk/) to each other. A counterparty's financial condition could deteriorate overnight, and the receiving party—holding either shares or cash they should not yet own—faced loss.

Payment versus Delivery eliminates this gap by linking the two legs legally and operationally. Securities and cash move together, creating a single atomic transaction. If cash fails to clear, shares do not transfer. If shares cannot be delivered, cash does not debit. The two events are inseparable.

## How DVP operates in practice

Modern DVP systems are technical achievements. A [clearinghouse](/stock-exchange/) or settlement agent (often a central bank or depository) acts as an intermediary. On settlement day, the buyer's bank confirms cash is available, the seller's depository confirms securities are held, and the settlement system executes the trade atomically: cash moves from buyer to seller, shares move from seller to buyer, all within the same instant or within a tightly defined window.

The mechanics vary by market. In many developed markets, settlement occurs over a central securities depository where shares are held in book-entry form (not physical certificates). The buyer's cash account is debited and the seller's account is credited at the same moment the shares move in the depository ledger. No party receives anything until both legs clear.

This operational architecture requires deep [counterparty trust](/counterparty-risk/) between the buyer, seller, and the settlement infrastructure—typically a national central bank or its designated agent. Participants must be creditworthy and operationally reliable. Settlement failure—where one party cannot deliver or pay—does occur, but it is rare in developed markets precisely because DVP discipline and clearing-house backstops (which may extend credit overnight) make it costly.

## Variants: DVP and beyond

The simplest DVP model pairs delivery with payment on the same day. In practice, settlement timelines have evolved. The historical standard was T+5 (five business days post-trade), which allowed time for physical delivery and cheque clearing. Modern markets have compressed this to T+2 or T+1, and some are moving toward same-day settlement.

A variant called [Delivery Versus Payment](/payment-versus-delivery/) with an intra-day settlement cycle exists in large markets: trades execute on one day but settle within hours, reducing overnight risk exposure. This is especially common in [government bonds](/treasury-bond/) and [currency](/us-dollar/) markets where settlement volumes are enormous and speed is operationally feasible.

Another variant pairs securities against securities, without a cash leg. In [repo](/stock-market/) transactions or securities lending, two parties exchange securities simultaneously under DVP logic, eliminating the risk that one lender sends securities without receiving collateral in return.

## Why counterparty risk matters

The stakes of settlement are highest in volatile markets. During a financial crisis or market shock, counterparties may default. If Counterparty A fails to pay after receiving shares, the seller loses both shares and cash. If Counterparty B fails to deliver after the buyer's cash has cleared, the buyer is left holding cash equivalents in a depository and facing delay and legal costs to recover shares or cash.

Historically, settlement failures cascaded. During the 1987 stock market crash, US [stock](/stock/) trading volumes surged and settlement delays lengthened, creating a temporary but alarming chain of [counterparty defaults](/counterparty-risk/). This prompted regulators to tighten DVP discipline and codify settlement timelines in law.

The 2008 financial crisis reinforced these lessons. Large securities dealers failed mid-settlement, and the Lehman Brothers collapse froze settlement networks. Markets that had robust DVP infrastructure and central-bank backstops recovered faster than those without. The result was global regulatory push toward tighter settlement standards, including the shift to T+2 and the proliferation of central clearinghouses.

## DVP in different asset classes

[Equities](/common-stock/) settled via a central depository (like DTC in the US or Euroclear across Europe) have nearly perfect DVP enforcement. Shares are immobilized in book-entry form, and cash moves through the banking system in lockstep with share transfers.

[Government bonds](/treasury-bond/) also settle via DVP in most developed markets, though sometimes with same-day windows due to the volumes involved.

[OTC derivatives](/option/) and [forward contracts](/forward-contract/) historically operated with weaker DVP discipline, settling bilaterally between counterparties. This left credit exposure overnight. Regulatory reform post-2008 pushed OTC derivatives toward central clearing and [trade repositories](/trade-repository/), tightening DVP enforcement. Now, most major derivatives must be reported to a trade repository and, if eligible, centrally cleared through a clearinghouse that operates DVP principles.

Private or [illiquid securities](/over-the-counter-market/) may settle outside formal DVP infrastructure, relying on trust and legal contractual protection. But for liquid, standardised instruments traded on [exchanges](/stock-exchange/) or between regulated institutions, DVP is nearly universal.

## The economic role of settlement finality

DVP creates what regulators call "settlement finality"—the moment at which a trade becomes irreversible and both parties' rights and obligations crystallise. This finality is crucial to [market confidence](/stock-market/). Traders and institutions need to know that once a trade settles, it cannot be undone, and their counterpart cannot default retroactively. Without this certainty, credit premiums would widen, trading volumes would shrink, and markets would fragment.

Central banks treat DVP and settlement finality as pillars of financial stability. Laws codify which authority declares a trade settled and irreversible, and this authority (typically the central bank's real-time gross settlement system) cannot later be overridden by a bankruptcy court or counterparty dispute.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty risk](/counterparty-risk/) — the credit exposure DVP eliminates
- [Trade repository](/trade-repository/) — regulated infrastructure that aggregates settlement and transaction data
- [Self-regulatory organisation](/self-regulatory-organisation/) — industry bodies that enforce settlement standards
- [Settlement](/stock-exchange/) — the final exchange of securities and cash
- [Central bank](/central-bank/) — typically the operator of real-time gross settlement systems
- [Clearinghouse](/stock-exchange/) — intermediaries that enforce DVP by interposing between buyer and seller

### Wider context

- [Over-the-counter market](/over-the-counter-market/) — where DVP discipline has historically been weaker
- [Stock exchange](/stock-exchange/) — markets where DVP is standard for listed securities
- [Securitization](/securitization/) — complex instruments where DVP enforcement is critical
- [Forward contract](/forward-contract/) — bilateral instruments that may settle outside formal DVP infrastructure

</div>
