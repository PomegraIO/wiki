---
title: "Clearing Fee Per Trade Explained"
description: "What clearing and settlement fees are, who charges them, and how they stack against other explicit costs for active traders."
keywords:
  - clearing fee per trade
  - settlement fees
  - trading costs
  - execution costs
  - brokerage fees
  - trading commissions
image: "/svg/trading.svg"
---

*A **clearing fee per trade** is a fixed or percentage-based charge imposed by the clearing house—the intermediary that guarantees both sides of a trade—on each transaction. For active traders, these fees are one of several explicit costs (alongside commissions, bid-ask spreads, and [exchange](/stock-exchange/) fees) that eat into profits.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clearing Fee Per Trade — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and market mechanics." />

<div class="wiki-infobox-caption">A small but unavoidable cost charged by the clearing house for each transaction settlement.</div>

|   |   |
|---|---|
| **Typical range** | $0.01–0.05 per share, or $0.50–$5 per contract (options) |
| **Who charges** | The clearing house (e.g., NSCC, OCC, DTCC) |
| **When paid** | At settlement, typically T+2 (two business days after trade) |
| **Who pays** | Usually the [broker](/broker/), which may pass it to the client |
| **Industry structure** | Mandatory; all trades through a regulated [exchange](/stock-exchange/) incur clearing fees |
| **Frequency impact** | Cumulative burden for day traders and high-volume traders |

</aside>

## The clearing process and why it exists

When you buy 100 shares of a stock on a [stock exchange](/stock-exchange/), you are not trading directly with the seller. Instead, your [broker](/broker/) matches your order with a counterparty's order on the [exchange](/stock-exchange/) and then passes the trade to a **clearing house**—an institution that stands between buyer and seller.

The clearing house's role is to:

1. **Validate the trade**: Confirm that both parties are registered and authorized to trade.
2. **Guarantee settlement**: Ensure that when the seller delivers shares, the buyer delivers payment (or vice versa). The clearing house assumes the counterparty risk.
3. **Facilitate delivery vs. payment**: Hold funds and securities in escrow until the settlement date (typically T+2, meaning two business days after the trade).
4. **Manage default risk**: If one party fails to settle, the clearing house steps in to complete the trade.

This infrastructure is expensive. The clearing house maintains [capital](/capital-asset-pricing-model/), technology, insurance, and staff to manage trillions of dollars' worth of daily transactions. **Clearing fees** are how the clearing house recovers these costs.

## Who are the major clearing houses?

In the United States:

- **NSCC** (National Securities Clearing Corporation): Clears equity and corporate bond trades.
- **OCC** (Options Clearing Corporation): Clears all [options](/option/) trades on U.S. exchanges.
- **DTCC** (Depository Trust & Clearing Corporation): Owns both NSCC and OCC, and operates the central securities depository.
- **CME Clearing** (part of CME Group): Clears futures and derivatives.

Each charges its own schedule of fees. For equities, NSCC fees are typically $0.01–0.05 per share on both buy and sell sides, or sometimes a flat per-trade fee. For [options](/option/), OCC charges per contract (a [contract](/futures-contract/) = 100 shares of the underlying stock). A 10-lot options trade (1,000 shares notional) might incur $25–$50 in OCC clearing fees alone.

## Fee structure: per-share, per-contract, or flat

Clearing fees vary by asset class:

### Equities
- **Per-share fee**: $0.001–0.005 per share. On a 1,000-share trade, this is $1–$5.
- **Flat fee**: Some brokers negotiate flat monthly or quarterly clearing fees.
- **Volume tiering**: High-volume traders may negotiate lower per-share rates.

### Options
- **Per-contract fee**: $0.05–0.30 per contract. A 100-contract trade incurs $5–$30 in clearing fees.
- **Volume discounts**: Institutional traders and market makers may pay $0.01–0.10 per contract.

### Futures
- **Per-contract fee**: Often $0.10–0.50 per contract, charged on open and close.
- **Round-turn pricing**: Some brokers charge a single fee for the round-trip (buy and sell).

## Who actually pays?

Clearing fees are charged to the clearing member—typically a large financial institution that is a member of the clearing house. That member then passes the fee to the [broker](/broker/), which may:

1. **Absorb it**: Eat the cost as part of the spread or commission.
2. **Pass it on directly**: Charge the client a separate "clearing fee" line item.
3. **Bundle it**: Fold it into a broader commission or brokerage fee.

Retail brokers (e.g., Fidelity, E*TRADE) often absorb small clearing fees because the cost is negligible per trade for most clients. But for a day trader placing 100+ trades per day, clearing fees add up: $100–1,000 per week depending on trade size and asset class.

Institutional traders and market makers negotiate directly with their clearing members to minimize these costs. Large hedge funds may pay $0.001–0.002 per share or even get rebates if they provide liquidity.

## Clearing fees vs. other trading costs

For an active trader, the total cost per trade is a sum of several components:

| Cost | Typical amount | Notes |
|---|---|---|
| Commission | $0–10 per trade | Often waived for equities; standard for options |
| Bid-ask spread | $0.01–0.50 (equity); 1–10 cents (options) | Varies by liquidity |
| Clearing fee | $0.01–0.05 per share; $0.05–0.30 per contract | Mandatory; clearing house revenue |
| Exchange fee | $0.001–0.003 per share | Rebate for providing liquidity; charge for removing |
| [SEC](/securities-and-exchange-commission/) fee | $0.0000211 per trade (sell-side only) | Minuscule; securities transaction tax |

The **bid-ask spread** is usually the largest cost for retail traders, especially on liquid stocks. For a stock trading with a 1-cent spread, 100 shares, the spread cost is $1. Clearing fees ($0.01–0.05 per share) add $1–$5.

For options, which have wider spreads and higher commissions, clearing fees are a smaller proportion of total cost but still material.

## High-frequency and algorithmic traders

Algorithmic traders and market makers are extremely cost-sensitive and will optimize for clearing fees explicitly. Some strategies:

1. **Order routing**: Route trades through brokers with the lowest clearing fee schedules.
2. **Clearing member selection**: Partner directly with low-cost clearing members.
3. **Netting**: Batch trades and close out positions intra-day to minimize settlement obligations and thus clearing fees.
4. **Venue selection**: Execute on exchanges with lower fees (though this trades off against liquidity or spread quality).

For a trader executing 10,000 shares per day at $0.02 per share in clearing fees, annual cost is roughly $50,000 (assuming 250 trading days). A 0.005 reduction in the rate saves $12,500 per year—significant at the margin.

## The settlement lag and margin requirements

Clearing fees are charged at settlement, typically T+2. Until the trade settles, the clearing house and brokers extend [credit](/credit-rating/) to facilitate the transaction. During this period, the broker may charge [margin](/margin-call-forex/) interest on the unsettled position.

For very active day traders (buying and selling the same position multiple times per day), the number of unsettled trades can stack up, creating a large margin interest burden. Some brokers offer "same-day settlement" or intra-day buying power to reduce this, though these features come with higher fees or interest charges.

## Regulatory and policy context

Clearing fees are generally not regulated by the [SEC](/securities-and-exchange-commission/) or [FINRA](/finra/). The clearing houses (NSCC, OCC, etc.) set their own fees, though they must be "fair and reasonable" and not discriminatory.

In 2020–2021, the [SEC](/securities-and-exchange-commission/) and Congress began scrutinizing clearing fees and margin requirements after the GameStop/Meme Stock events. There was concern that high clearing fees and [margin calls](/margin-call-forex/) were creating procyclical risk (widening spreads and reducing liquidity when volatility spikes). No major legislative changes ensued, but the issue remains on regulators' radar.

## How to minimize clearing costs

For active traders:

1. **Negotiate broker terms**: If you trade high volume, ask your broker to reduce clearing fees or pass through rebates.
2. **Choose the right asset class**: Equities usually have lower fees (per share) than options or futures.
3. **Batch orders**: Minimize the number of settlement legs by closing out day-trading positions.
4. **Compare brokers**: Some brokers absorb clearing fees; others are transparent about them.
5. **Trade liquid securities**: Wider spreads on illiquid stocks often dwarf the clearing fee savings.

Retail investors making occasional trades are unlikely to notice clearing fees because brokers absorb them or they are tiny relative to the bid-ask spread. But for a serious active trader, they are a real and avoidable cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Broker](/broker/) — the intermediary that routes trades and pays clearing fees
- [Stock Exchange](/stock-exchange/) — the venue where trades are executed and then cleared
- Settlement — the process by which trades are finalized and funds exchanged
- [Bid-Ask Spread](/bid-ask-spread/) — often a larger cost than clearing fees for most traders
- [Execution Risk](/execution-risk/) — risks and costs incurred during trade execution

### Wider context

- [Market Order](/market-order/) — an order type subject to clearing fees and slippage
- [Margin Call (Forex)](/margin-call-forex/) — related to the credit and collateral used during settlement
- [SEC](/securities-and-exchange-commission/) — regulator overseeing fair clearing practices
- [FINRA](/finra/) — self-regulatory organization that monitors broker conduct

</div>
