---
title: "Maker-Taker Fee Model Explained"
description: "The maker-taker fee model pays liquidity providers (makers) a rebate while charging liquidity takers a higher fee. This incentivizes passive orders but distorts routing incentives and raises trading costs for many participants. Understand the mechanics and the controversy."
keywords:
  - maker taker fee model
  - maker taker explained
  - liquidity rebate
  - exchange fee structure
  - market maker incentives
image: /svg/markets.svg
---

*The **maker-taker fee model** is an exchange pricing structure where a liquidity **maker**—a trader posting a resting order—earns a rebate (or pays nothing) when another trader (a liquidity **taker**) hits that order and executes the trade. The **taker** pays the full transaction fee, often 3–5 basis points, while the **maker** receives a rebate (typically 1–2 bps). This inverts the traditional fee structure and is meant to encourage passive liquidity provision, but in practice it has driven fragmentation, adverse selection, and higher execution costs for retail traders.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Maker-Taker Fee Model — Core Structure</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for markets." />

<div class="wiki-infobox-caption">A fee split designed to reward passive order placement, with unintended consequences.</div>

|   |   |
|---|---|
| **Maker (passive order)** | Receives rebate: −1 to −2 bps per share (effectively paid to trade) |
| **Taker (market order)** | Pays fee: +3 to +5 bps per share |
| **Net to exchange** | Roughly breakeven to profitable (taker fee > maker rebate) |
| **Who benefits** | High-frequency market makers, passive traders, brokers routing for rebates |
| **Who pays** | Active traders, retail investors, momentum traders (takers) |
| **Typical asset class** | Equities on U.S. exchanges (NASDAQ, NYSE MKT/ARCA); less common in bonds, futures |
| **Controversial aspect** | Incentivizes payment-for-order-flow and best-execution conflicts |

</aside>

## How Maker-Taker Works: A Simple Example

Suppose **Alice** submits a limit order to buy 1,000 shares of XYZ at $50 (a maker order—she's providing liquidity by waiting). Her order sits on the [order book](/limit-order/).

**Bob** enters a market order to sell 1,000 shares of XYZ at market. His order immediately hits Alice's resting order, executing at $50. Both trades settle.

Under the maker-taker model:
- **Alice (maker)**: Receives a rebate of −1.5 bps = −$0.15 per share × 1,000 = −$150 total. She's *paid* $150 for her liquidity.
- **Bob (taker)**: Pays a fee of +4.0 bps = +$0.40 per share × 1,000 = +$400 total. He pays $400 to execute immediately.
- **Exchange**: Net +$250 revenue on the trade ($400 taker fee minus $150 maker rebate).

Alice's incentive is clear: posting limit orders is rewarded. Bob's cost is high: demanding immediate execution is expensive. This is the intended behavior—the exchange wants to encourage passive resting orders and discourage urgent, aggressive order flow.

## The Inversion from "Maker Pays" Model

Historically, exchanges used a "maker pays" model: the trader who posted the order (the maker) paid a fee, and the taker received a rebate or paid nothing. This made intuitive sense—the maker consumed the exchange's resources (holding the order, matching engines, regulatory overhead), so they paid.

In the late 1990s and 2000s, exchanges like NASDAQ and direct-access venues (island, INET) flipped the model. As markets fragmented across dozens of venues, competition for order flow intensified. An exchange offering maker rebates could attract passive traders and market makers, increasing volume on their platform.

The maker-taker model became the industry standard for equities. Its logic: passive liquidity is scarce and valuable; active liquidity (takers) is abundant, so let's price accordingly.

## Motivation: Incentivizing Passive Liquidity

Markets need passive [liquidity](/liquidity-risk/)—people willing to resting orders at tight spreads so others can trade without waiting. Without passive market makers, the [bid-ask spread](/bid-ask-spread/) widens, and everyone's execution costs rise.

By paying makers, exchanges incentivize market-making firms to:
- Deploy capital at many venues.
- Post tight spreads (e.g., 1-cent wide on liquid stocks).
- Maintain presence even in slow markets.

This has worked. Spreads have narrowed dramatically over the past two decades, particularly in large-cap equities. Retail traders benefit from tighter spreads and cheaper passive execution.

But the model's success created perverse incentives.

## The Payment-for-Order-Flow Problem

The maker-taker rebate creates an incentive for brokers to route retail order flow to exchanges paying the highest maker rebates, rather than to exchanges offering the best execution prices for the customer.

Here's the conflict:

**Scenario 1: Best execution (no rebate influence)**
- Exchange A: Bid $50.00, Ask $50.01 (1-cent spread)
- Exchange B: Bid $49.98, Ask $50.02 (4-cent spread)
- Exchange B offers the highest maker rebate (−2.5 bps).

A customer wanting to buy should route to Exchange A (best ask, $50.01). But if Exchange B pays a 2.5 bps rebate on the maker's side, and the broker is the market maker on Exchange B, the broker earns a rebate that offsets the worse execution price. The broker might route there anyway, pocketing the rebate as profit and passing the worse execution cost to the customer.

Over millions of trades, this leakage adds up. Studies estimate retail traders lose tens of basis points per year to adverse routing decisions driven by rebate incentives.

## Market Fragmentation and Adverse Selection

The maker-taker model incentivized new exchanges to launch with aggressive maker rebates, splintering order flow across many venues. This fragmentation has created several problems:

**Stale quotes**: With orders scattered across 13+ equity exchanges, a trade on one venue might not reflect updated prices on others. Retail traders can hit stale asks on venue A while better bids are live on venue B (but unseen).

**Adverse selection**: Market makers earning rebates on passive orders face a classic adverse selection problem. If I post a bid of $50.00 and aggressive traders hit my order every time the stock spikes (and ignore me when it crashes), I'm making money on the rebate but losing money on the adverse selection. This leads to wider spreads and faster quote updating—eventually harming the passive traders the rebate was meant to help.

**Information leakage**: Sophisticated traders use rebate structures to infer order flow patterns. High rebate-payers attract certain types of orders, signaling information about order direction and volume to predatory traders.

## Who Gains, Who Loses

**Winners:**
- **High-frequency market makers**: Firms like Citadel Securities, Virtu, and Tower Research operate at scale, posting millions of maker orders and collecting rebates of millions per year. The model is effectively a subsidy for them.
- **Institutional passive traders**: Large funds executing via algorithms (e.g., VWAP) that post limit orders benefit from rebates and tight spreads.
- **Exchanges**: Volume grows as brokers compete to capture rebates, and exchanges profit from the spread (taker fee minus maker rebate).

**Losers:**
- **Retail active traders**: Retail day traders and momentum traders are almost always takers. They pay the full fee and subsidize makers' rebates.
- **Poorly routed retail**: Brokers routing to highest-rebate venues (even if execution is worse) pass the cost to customers.
- **Institutional takers**: Large funds executing market orders or urgently pressing through the market also pay taker fees.

## Regulatory Scrutiny

The SEC has criticized the maker-taker model for decades. In 2005–2010, the SEC opened rulemaking on whether maker-taker rebates violate "best execution" rules under Reg SHO. Several proposals were floated to ban the model outright but ultimately failed due to industry pushback and the empirical ambiguity—spreads *did* tighten post-maker-taker, even if fragmentation and adverse selection got worse.

In 2021–2022, the SEC again questioned whether rebates unduly incentivized payment-for-order-flow and hurt retail customers. While no ban has passed, pressure remains high for the industry to reform or justify the model.

Some international exchanges (notably Japan's TSE) banned maker-taker rebates entirely, moving back to taker-pays-maker structures or flat fees.

## Alternative Fee Models

**Flat-fee model**: Both makers and takers pay the same per-share fee (e.g., 0.5 bps). No rebate, simpler, no adverse selection. Used by some venues and preferred by regulators.

**Tiered volume model**: Maker and taker fees decline as a trader's volume increases, but they aren't inverted. Rewards volume without paying for liquidity.

**Hybrid**: Some venues offer flat fees to retail and selective rebates to institutional market makers, attempting to balance simplicity and liquidity incentives.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the price difference maker-taker rebates help narrow
- [Market maker](/market-maker-trading/) — the primary beneficiary of maker rebates
- [Liquidity risk](/liquidity-risk/) — why passive liquidity is valuable
- [Order book](/limit-order/) — where makers' resting orders reside
- [Best execution](/bid-ask-spread/) — regulatory standard the model can conflict with
- [High-frequency trading](/algorithmic-trading/) — primary practitioners of maker-seeking strategies

### Wider context

- [Stock exchange](/stock-exchange/) — venues employing the maker-taker model
- [Algorithmic trading](/algorithmic-trading/) — how orders are routed to capture rebates
- [Regulation A](/regulation-a/) — SEC rules governing rebates and order routing
- [Market fragmentation](/fragmented-market/) — consequence of maker-taker incentives

</div>
