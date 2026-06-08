---
title: "Short Sale Locate Requirement"
description: "The regulatory obligation for brokers to locate available shares before facilitating a short sale, and what counts as a valid locate."
keywords:
  - short sale locate requirement
  - locate requirement regulation
  - short selling compliance
  - borrow locate
  - SEC Regulation SHO
  - pre-borrow short sales
image: /svg/markets.svg
---

*The **short-sale locate requirement** is a regulatory mandate that a broker must confirm that shares are available to borrow and hold a documented borrow arrangement *before* executing a short sale on behalf of a customer. Introduced in the U.S. by the SEC's Regulation SHO in 2005, this rule prevents [naked short selling](/naked-short-selling-mechanics/) and protects the market against settlement failures and manipulative trading practices.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Short Sale Locate Requirement — Key Facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Brokers must confirm a borrow before any short sale is permitted.</div>

|   |   |
|---|---|
| **Regulatory source (U.S.)** | SEC Regulation SHO, Rule 10b-21; adopted 2005 |
| **Key obligation** | Broker must locate available shares and document the borrow before execution |
| **Timing** | Locate must be in place *before* the short sale trade is sent to the market |
| **What counts as a locate** | Broker inventory, client securities lending, third-party lending pools, affirmative commitments |
| **Violations** | SEC enforcement, fines, suspension of short-selling privileges, regulatory censure |
| **Market makers** | Limited exemption under Rule 10b-21(d) to short without pre-borrow in certain conditions |

</aside>

## The Locate Standard

A valid locate is a documented confirmation that shares are available to borrow. It must be in writing (electronic records count) and must include:

- The security to be shorted
- The number of shares
- The expected lending period or loan duration
- Confirmation that the lender will deliver shares to the broker by settlement (T+2)

The broker must obtain this documentation before the short sale order leaves its systems. A post-hoc affirmation—locating shares *after* the trade executes—does not satisfy the requirement. The order flow itself must be gated by a pre-execution locate check.

Three main sources can satisfy a locate:

1. **Broker inventory**: The broker itself owns shares available to lend to the customer's short position.
2. **Client loaned securities**: Another client of the same broker has deposited shares in a securities lending program, and the broker can offer those shares as a borrow.
3. **Third-party lenders**: The broker has an arrangement with a securities lending desk, clearing broker, or prime brokerage service that confirms availability of shares to borrow.

In practice, large brokers maintain standing lending arrangements with multiple sources and can execute short sales within milliseconds because the locate infrastructure is pre-positioned.

## Why the Requirement Was Adopted

Before 2005, brokers were permitted to execute short sales without confirming a borrow in advance. Some traders exploited this to sell short massive quantities of illiquid or hard-to-borrow stocks without any realistic way to deliver. The resulting settlement failures created market distortions:

- Buyers failed to receive shares, disrupting settlement chains.
- Brokers scrambled to source shares at inflated prices, passing costs to other market participants.
- Naked short sellers profited from the panic and supply disruption, incentivizing further naked shorting.

Small-cap and microcap stocks were especially vulnerable to manipulation. A coordinated campaign of naked shorts could cascade into a short squeeze, with prices spiking as brokers forced buy-ins to cover failed deliveries.

The SEC determined that the locate requirement was necessary to restore confidence in settlement integrity and eliminate an avenue for market manipulation.

## Enforcement and Compliance

Brokers are responsible for compliance and face direct SEC enforcement if they execute short sales without valid locates. Penalties include:

- **Monetary fines** (often in the millions of dollars for systematic violations)
- **Suspension of short-selling privileges** for the broker or trading desk
- **Mandatory surveillance programs** requiring real-time locate validation
- **Regulatory restrictions** on future short-selling activity

The SEC conducts periodic sweeps of major brokers' short-selling practices, using data from the [order book](/limit-order/) and clearing systems to identify trades that may not have had valid locates. If a broker cannot produce documentary evidence of a pre-execution locate, the SEC will assert a violation.

Brokers have strong incentives to comply because loss of short-selling privileges is commercially devastating—it cuts off a major revenue stream (borrowing fees) and customer-facing services.

## Special Cases and Exemptions

Most traders must operate within the locate requirement, but exceptions exist:

- **Market makers**: Under Rule 10b-21(d), designated market makers and specialists may short to provide liquidity without a pre-locate in certain circumstances. They must locate and borrow by end-of-day or the next trading day.
- **Affirmative commitments**: A broker can rely on a contractual commitment from a lender to deliver shares, even if the lender hasn't yet sourced them. This is common for large, institutional short positions.
- **Borrow pools**: If a broker participates in a centralized borrow pool (like a clearing house pool), shares are deemed available if the pool confirms them, even if the specific lender hasn't been identified.

For retail and most institutional traders, these exemptions don't apply. The locate must be concrete and documented before the trade executes.

## The Locate and Cost

The requirement to locate shares creates a cost structure for short selling. Brokers charge borrowing fees to the customer based on the scarcity and hold period of the borrow. For a hard-to-borrow stock (a microcap, a heavily-shorted security, or a newly IPO'd company), borrowing rates can be substantial—sometimes 5%, 10%, or even 30% annualized.

These borrowing costs are a feature, not a bug, of the system. They discourage frivolous naked shorting and create a market mechanism for allocating scarce borrows to traders who are willing to pay for them. A trader who believes a stock will fall must weigh the conviction against the carrying cost of the borrow.

Brokers have an incentive to maintain diverse lending relationships so they can reliably locate shares and offer competitive borrowing rates to customers. Competition among brokers for prime brokerage and institutional short-selling business has driven down borrowing costs in many widely-traded securities.

## Locate vs. Settlement

The locate requirement is distinct from the settlement process. Locate is about confirming availability *before* the trade; settlement is the actual delivery of shares *after* the trade, typically T+2. A valid locate doesn't guarantee smooth settlement if the lender fails or if the underlying shares are unavailable at settlement time, but it makes settlement failures far less likely.

If a settlement failure occurs despite a valid locate, the broker's recourse is to buy shares at market prices and charge the customer the cost. But the locate requirement ensures that failures are rare exceptions, not systematic features of the market.

## Global Framework

The locate requirement is a uniquely rigorous standard adopted widely but with variations:

- **U.S. (SEC)**: Strict pre-execution locate; enforced continuously.
- **EU (ESMA)**: Equivalent requirement under the short-selling ban regulation (2012); brokers must confirm locate before execution.
- **U.K. (FCA)**: Pre-execution locate requirement for non-market-maker short sales.
- **Canada (OSC)**: Similar to U.S. approach; pre-execution locate mandatory.

Most major financial centers have converged on the locate requirement as a baseline market integrity rule.

## See also

<div class="wiki-seealso">

### Closely related

- [Naked Short Selling Mechanics](/naked-short-selling-mechanics/) — Why the locate requirement prevents unborrowable shorts and settlement risk
- [Short Selling](/short-selling/) — Core mechanics of selling borrowed shares
- [Borrow](/short-selling/) — How shares become available to short and the cost structure
- [Settlement](/short-selling/) — T+2 delivery process and how locates reduce failure rates
- [Tick Size and Market Quality](/tick-size-and-market-quality/) — Market structure rules that affect short-selling dynamics

### Wider context

- [Regulation SHO](/short-sale-locate-requirement/) — SEC rules governing short sales and locates
- [Broker](/broker/) — Intermediaries who enforce locate requirements
- [Stock Exchange](/stock-exchange/) — Venues where short sales are monitored and enforced
- [Market Manipulation](/short-selling/) — How locate requirements curtail price manipulation

</div>
