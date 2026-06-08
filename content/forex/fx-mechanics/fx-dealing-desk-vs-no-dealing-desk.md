---
title: "Dealing Desk vs No-Dealing-Desk Forex Brokers"
description: "Compare dealing-desk and no-dealing-desk forex brokers: how order flow is handled, pricing transparency, conflict of interest, and execution speed."
keywords:
  - dealing desk vs no dealing desk forex
  - market maker vs ecn forex broker
  - dealing desk broker forex
  - ndd forex broker ecn stp
  - market maker conflict of interest
image: "/svg/forex.svg"
---

*A **dealing desk** forex broker acts as a market maker, internalizing your order by taking the other side of the trade. A **no-dealing-desk** (NDD) broker routes your order directly to liquidity providers without taking principal risk. The choice between them shapes your execution speed, spreads, and whether your broker profits when you lose.*

---

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dealing Desk vs NDD — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex mechanics." />

<div class="wiki-infobox-caption">Order routing method defines friction, transparency, and alignment of incentives.</div>

|   |   |
|---|---|
| **Dealing desk** | Market maker; internalizes order; takes counterparty risk |
| **No-dealing-desk (NDD)** | Acts as agent; routes to liquidity providers; earns commissions |
| **Spreads (dealing desk)** | Fixed, wider; wider in volatile conditions |
| **Spreads (NDD)** | Tighter, variable; narrower at peak hours |
| **Execution risk** | Dealing desk: slippage on fast moves; NDD: less internal slippage |
| **Broker incentive** | Dealing desk: profits if you lose; NDD: profits on volume alone |
| **Minimum conflict** | NDD has lower inherent conflict; dealing desk has structural opposite |

</aside>

---

## How the dealing desk model works

A dealing-desk (or "market maker") broker holds its own inventory of currency pairs. When you place a buy order for EUR/USD, the broker does not immediately find an external seller; instead, it sells the pair to you from its own book. You become the customer, and the broker becomes your counterparty.

This arrangement lets the broker:

- **Control spread width**: Set the bid–ask spread independently, narrowing it to attract volume or widening it to cover risk. In volatile hours, spreads widen mechanically.
- **Internalize flow**: Profit when you lose money. If you buy EUR/USD and the price drops, the broker's short position is in-the-money.
- **Execute instantly**: Your order fills at the posted price within milliseconds, with no routing delay or dependence on external liquidity.

The structural conflict is unavoidable: the dealing-desk broker makes money when you lose, and may be less motivated to improve your execution if it means lower profit.

---

## How the no-dealing-desk model works

A no-dealing-desk (NDD) broker is an agent that routes your order to external liquidity providers—banks, hedge funds, or other forex dealers. The broker itself takes no market risk. Instead, it earns money through:

- **Commission per trade**: A small per-lot or per-dollar fee, regardless of the trade outcome.
- **Wider spreads**: A markup on top of the best available bid–ask from liquidity providers (e.g., the bank wholesale spread is 0.5 pips; the broker adds 1 pip and shows 1.5 pips to you).
- **Volume-based rebates**: Some brokers earn kickbacks from liquidity providers for sustained order flow.

Within the NDD category, two subtypes exist:

**STP (Straight Through Processing)**: The broker's systems automatically route your order to the liquidity provider offering the tightest price. Faster, but the broker has limited control over final price.

**ECN (Electronic Communications Network)**: The broker displays a consolidated order book of bids and asks from multiple liquidity providers and matches buyers and sellers directly. You see the top-of-book prices and can walk away if the spread widens mid-trade.

NDD brokers have aligned incentives: they earn money whether you win or lose, so they benefit from lower friction and faster execution.

---

## Spreads and pricing transparency

**Dealing desk spreads** are fixed or semi-fixed. The broker commits to a visible spread—say 1.2 pips on EUR/USD—and maintains it during normal market hours. If volatility spikes (e.g., central bank announcement), the broker may widen the spread suddenly to protect itself or halt trading temporarily.

Fixed spreads have a major appeal: you know your cost up front and can plan positions. But in illiquid conditions, the posted spread is not your true fill price if slippage occurs.

**NDD spreads** are variable because they pass through the wholesale market's bid–ask directly. During liquid hours (e.g., 8:00–16:00 London time), spreads are often tighter than dealing-desk spreads. During Asian overnight sessions, spreads widen because fewer market makers are active. A typical ECN broker shows real-time bid–ask from its liquidity providers, so you see the true market price at any moment.

The transparency is a double-edged sword: you see real pricing, but you also bear the execution risk if you hit an order during a fast move and the price slips away.

---

## Execution speed and slippage

**Dealing desk execution** is fast: your order reaches the broker's matching engine, and you get filled at the posted price instantly. Slippage is rare because the spread is fixed. However, if the market moves rapidly—e.g., a 20-pip rally in 50 milliseconds—the broker's entire order flow moves against its position simultaneously, creating inventory risk.

**NDD execution** depends on liquidity availability and network routing. On major pairs with multiple liquidity providers, fills are near-instantaneous. On exotic pairs or during thin market hours, your order may wait milliseconds longer as the broker finds a matching counterparty. Slippage risk is higher: you may request to buy at 1.0950 but fill at 1.0952 if the external market moved between your order submission and execution.

---

## Conflict of interest and broker incentives

The dealing-desk model creates an inherent misalignment: the broker is not a neutral intermediary. It profits when you lose and loses when you win. This incentive can lead to:

- **Widened spreads on retail signals**: If the broker detects that many small accounts are buying a pair, it may widen spreads on that pair specifically to discourage or capture retail orders.
- **Rejection of winning trades**: Some dealing-desk brokers reserve the right to decline large winning orders at fill time, citing "system issues" or "risk limits"—a tactic known colloquially as "dealing desk manipulation."
- **Re-quotes**: The broker may revise the quoted price between order submission and execution, especially in fast-moving markets. If you accept a re-quote at a worse price, you continue your trade; if you reject, the order is cancelled. Repeated re-quotes create friction and cost.

NDD brokers have no intrinsic reason to work against you. They earn commissions and markup regardless of trade outcome. This does not mean NDD brokers are riskless—they still collect margin and can close positions if you miss a margin call—but the fee structure is neutral.

---

## Regulatory and practical considerations

**Regulatory framing**: Many jurisdictions treat dealing-desk and NDD brokers differently. In the EU, brokers must classify themselves and disclose conflicts; clients of dealing-desk brokers have extra safeguards (negative-balance protection, for instance). In the US, the [Dodd-Frank Act](/dodd-frank-act/) requires [best execution](/best-execution-compliance-obligation/) disclosures regardless of model, but enforcement focus differs.

**Account minimums and leverage**: Dealing-desk brokers often allow smaller account minimums and higher leverage (50:1 to 500:1 on retail accounts), because they profit on spreads and slippage. NDD brokers, which have lower internal margin, sometimes require larger minimums but offer lower fixed commissions.

**Market conditions and broker solvency**: A dealing-desk broker that internalizes too much one-way flow can face acute solvency risk if market moves are violent and one-directional. NDD brokers transfer that risk to external liquidity providers, reducing their own solvency burden but also making them more vulnerable to sudden liquidity drought (which happened during the 2015 CHF unpegging event).

---

## See also

<div class="wiki-seealso">

### Closely related

- [Best Execution as a Compliance Obligation](/best-execution-compliance-obligation/) — How brokers must measure and report their execution quality
- [Bid–Ask Spread](/bid-ask-spread/) — The mechanics of how spreads are quoted and maintained
- [Market Maker Trading](/market-maker-trading/) — How market makers manage inventory and profit
- [Over-the-Counter Market](/over-the-counter-market/) — Forex as a decentralized, dealer-based market

### Wider context

- [Broker](/broker/) — Intermediaries in financial markets
- [Derivative Securities](/derivatives-hedging/) — How forwards and swaps relate to the broader landscape
- [Interest Rate](/interest-rate/) — Central to carry trades and forex positioning

</div>
