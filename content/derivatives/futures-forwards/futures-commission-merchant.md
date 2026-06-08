---
title: "Futures Commission Merchant"
description: "A CFTC-registered intermediary that accepts customer orders and margin for futures and options trading, acting as a broker and custodian of collateral."
keywords:
  - futures commission merchant
  - FCM
  - futures broker
  - CFTC registration
  - margin custodian
image: /svg/derivatives.svg
---

*A **Futures Commission Merchant (FCM)** is a U.S. [broker](/broker/) licensed by the Commodity Futures Trading Commission (CFTC) to accept customer orders for [futures](/futures-contract/) and options contracts, and to hold customer margin (collateral) on their behalf. The FCM is the interface between retail or institutional traders and the exchange—executing orders, managing collateral, clearing trades, and enforcing [margin](/margin-call-forex/) rules. Most futures trading in the United States flows through FCMs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Futures Commission Merchant — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">The regulated custodian of customer margin and the gateway to the futures markets.</div>

|   |   |
|---|---|
| **What it is** | A CFTC-registered intermediary accepting customer futures and options orders and holding margin |
| **Also called** | Futures broker; introducing broker (introduces clients but does not hold margin itself) |
| **Regulation** | Subject to CFTC and National Futures Association (NFA) oversight; must meet capital and segregation rules |
| **Key roles** | Execute trades; hold and manage customer collateral; enforce margin requirements; clear and settle |
| **Largest FCMs** | JPMorgan, Goldman Sachs, Morgan Stanley, CME Clearing, many smaller regional firms |
| **Required for** | Any customer wishing to trade exchange-listed [futures](/futures-contract/) or [options](/option/) in the U.S. |

</aside>

## The FCM's place in the trading chain

When a trader wants to buy a [crude oil futures contract](/futures-contract/) on the Chicago Mercantile Exchange (CME), they do not call the exchange directly. They call or log into a Futures Commission Merchant. The FCM accepts the order, submits it to the exchange, confirms execution, and credits the trader's account.

The FCM also holds the trader's margin—the collateral required to support open positions. If a trader buys one crude oil contract, they must deposit margin with the FCM (typically $2,000–$5,000, depending on [volatility](/historical-volatility/)). The FCM segregates this margin in a client trust account, separate from the FCM's own capital. This segregation is a cardinal rule: customer funds may never be co-mingled with or lent to the FCM's operations.

The FCM is not the counterparty to the trade; the exchange is. The FCM is the middleman—a critical one, but a middleman. If the trader's position moves in their favour, the exchange credits the FCM, and the FCM credits the trader. If it moves against them, the process reverses.

## Margin management and daily reconciliation

Every day, the exchange "marks to market" all open [futures](/futures-contract/) positions. A trader long crude oil at $75 per barrel sees the contract revalued if crude closes at $76. If it closed at $76, the trader's position gained $100 per contract (1,000 barrels × $1). The FCM automatically credits the trader's account with this gain; if the price fell to $74, the FCM debits the account with the loss.

As long as the trader's account balance exceeds the **maintenance margin** (typically 70–80% of the initial margin requirement), the position stands. But if a market move wipes out a significant portion of the account, the trader may receive a **margin call**. The FCM demands that the trader deposit more collateral within a set time (often hours). If the trader fails to do so, the FCM [liquidates](/liquidation/) the position without permission, selling it into the market at whatever price clears. This can be brutal if the market is moving fast; the trader may receive nothing or even owe money.

In extreme crises (a sudden currency devaluation, a flash crash), a trader can owe the FCM more than their initial deposit. The FCM remains liable to the exchange even if the customer defaults, so the FCM pursues the trader for the shortfall.

## The rise of tiered clearing and prime brokers

Historically, every trader had a direct relationship with an FCM. Today, the structure is more tiered. Large institutional traders (hedge funds, asset managers) often use a "prime broker"—a division of a major bank like JPMorgan or Goldman Sachs. The prime broker acts as an FCM for the hedge fund but is itself an FCM at the exchange. There is a hierarchy: customer → introducing broker → FCM → exchange.

An **introducing broker (IB)** is a simpler license that allows the firm to solicit customers and manage their accounts, but does not hold their margin. The IB collects orders and passes them to a "clearing FCM" (a bigger firm with exchange access and CFTC approval). The customer's margin sits with the clearing FCM, not the IB, so the IB's failure does not directly threaten customer funds.

This tiering reduces operational complexity for smaller firms but introduces [counterparty risk](/counterparty-risk/): if the clearing FCM fails, the customer is first in line for segregated funds but still exposed to potential delays or haircuts if the FCM's own capital is insufficient.

## Capital and prudential requirements

The CFTC requires FCMs to maintain minimum net capital (adjusted for risk) to cover losses and unexpected shocks. The ratio varies by size and complexity, but a typical FCM must keep at least 4–8% of customer margin on hand in liquid capital. Larger, systemically important FCMs (the big banks) face stricter requirements.

The National Futures Association (NFA), a self-regulatory organization, enforces compliance. FCMs must undergo regular audits, file financial reports, and maintain detailed customer account records. If an FCM violates rules or mishandles funds, the NFA can impose fines, bar traders, or revoke registration. The framework is designed to be robust, but failures do happen; MF Global's collapse in 2011 (a major FCM and clearing firm) wiped out hundreds of millions in customer funds despite segregation rules, exposing regulatory gaps.

## The FCM's revenue model

FCMs earn money in several ways. First, they charge **commissions** on trades: perhaps $20–$50 per contract, depending on volume and customer size. Large hedge funds negotiate steep discounts; retail traders pay standard fees. Second, FCMs earn **clearing fees** (charged by the exchange, some of which the FCM pockets). Third, they earn interest on customer cash balances and sometimes on margin balances, generating "float"—a small but steady profit.

For some FCMs (especially the largest banks), the [margin management](/margin-call-forex/) business is secondary to their core derivatives trading operations. JPMorgan's FCM business, for example, is a fraction of its total revenue, but it is essential infrastructure.

## Global variations

Outside the U.S., futures brokers operate under different regulatory regimes. In the UK, the Financial Conduct Authority regulates futures intermediaries. In Asia, local securities commissions oversee the business. The regulatory structures differ, but the economic function is identical: accept orders, hold margin, manage collateral, enforce risk limits.

## Risks specific to FCMs

An FCM's greatest risk is a **customer default**: a trader's position moves against them, margin is exhausted, and the FCM must liquidate at a loss. In volatile markets (March 2020, during COVID), many retail traders faced forced liquidations. Some FCMs (brokerage firms without sufficient capital buffers) buckled under the losses.

Another risk is **operational failure**: a hack, a system outage, a collateral mix-up. In 2022, the Commodity Futures Trading Commission warned of cyber threats to FCMs' systems. A breach could expose customer data, compromise trade confirmation, or delay margin transfers.

Regulatory change is also a constant risk. New rules (like higher capital requirements or segregation mandates) can raise the cost of operation and pressure smaller FCMs, consolidating the industry.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures Contract](/futures-contract/) — the products FCMs facilitate
- [Margin Call](/margin-call-forex/) — the daily mechanic of FCM collateral management
- [Liquidation](/liquidation/) — what happens when a trader cannot meet a margin call
- [Broker](/broker/) — the general intermediary role, of which FCMs are a specialized type
- [Counterparty Risk](/counterparty-risk/) — the risk an FCM's failure poses to customers
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulatory parent of the CFTC

### Wider context

- [Options](/option/) — another asset class FCMs service
- Derivatives — the broader market FCMs enable
- [Over-the-Counter Market](/over-the-counter-market/) — where swap dealers operate (similar but distinct from FCMs)
- [Custody](/custodian/) — the broader function of holding customer assets

</div>
