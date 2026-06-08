---
title: "Guaranteed VWAP Order"
description: "A broker commitment to execute a client's order at the day's volume-weighted average price, with the broker absorbing any tracking error risk."
keywords:
  - guaranteed vwap
  - vwap order
  - execution guarantee
  - volume-weighted average price
  - broker risk
image: "/svg/trading.svg"
---

*A **guaranteed VWAP order** is a contractual commitment from a [broker](/broker/) to fill a client's order at the volume-weighted average price (VWAP) for that security on that day. The client names a quantity and a tolerance band; the broker executes the entire order and guarantees a fill price tied to VWAP, absorbing all slippage and tracking error. In exchange, the client pays a fee or wider spread. The guarantee shifts execution risk entirely from trader to broker.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Guaranteed VWAP Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and order mechanics." />

<div class="wiki-infobox-caption">The broker assumes all execution risk between order and VWAP benchmark.</div>

|   |   |
|---|---|
| **What it is** | Broker commitment to fill an order at the day's volume-weighted average price |
| **VWAP defined** | Total dollar volume ÷ total shares traded, weighted by actual trading activity |
| **Broker incentive** | Earns a fee or spread; profit if they execute better than VWAP |
| **Client incentive** | Certainty; knows maximum expected price regardless of order size or timing |
| **Typical spread** | 1–5 basis points, depending on liquidity and order size |
| **Common user** | Large institutions, mutual funds, pension plans, passive rebalancing |

</aside>

## The guarantee and its limits

When you submit a guaranteed VWAP order, you and your broker agree on a reference price: "the VWAP of XYZ stock on [date], as calculated by [data source]." The broker then commits to execute your full order (say, 5 million shares) at a price equal to that VWAP, plus or minus a tolerance band you agree on in advance. The tolerance is usually tiny—a few basis points. This means your maximum cost or minimum receipt is almost locked before the trading day ends.

This is different from asking your broker to "try to get me VWAP." A guaranteed VWAP is a legally binding promise. If the broker executes 5 million shares at an average price of 50.04 but VWAP closes at 50.00, the broker eats the 4-cent difference per share (or credits it back to you). That is a real cost to the broker and a real protection to you.

The guarantee applies only to a single trading day or a specified window. If you want to execute an order over three days, you would submit three separate guaranteed VWAP orders, one per day, or negotiate a multi-day VWAP (a less common variant with higher broker fees).

## Why brokers offer VWAP guarantees

A broker accepting a guaranteed VWAP order knows they will likely lose money on it if they sit passively. They must trade aggressively to minimize tracking error. A smart broker executes the order quickly on a large venue where they can see actual volume and trade alongside legitimate market flow. They also hedge by trading on other venues or with other counterparties to distribute their execution risk.

The broker's profit comes from the spread or explicit fee you pay upfront. On a 5 million-share order in a liquid stock, a 2 basis-point fee might mean $100,000 to $200,000 gross revenue. If the broker can execute the 5 million shares and track VWAP within a 1 basis-point tolerance, they pocket 1 basis point (roughly $50,000–$100,000). If they are sloppy and miss by 3 basis points, they lose money.

For this reason, guaranteed VWAP orders are most attractive to brokers in liquid names and for institutions large enough to pay meaningful fees. A $100 million order in Apple at 2 basis points is worth paying for; a $1 million order in a small-cap is not.

## Execution mechanics

A broker executing a guaranteed VWAP order typically fragments it across the entire trading day, sometimes following a [TWAP](/algorithmic-twap-order/) skeleton (time-based slices) with overlaid volume participation. They watch where volume is trading and lean into that volume at favorable prices. They may also trade on dark pools or alternative venues where large blocks are less visible, reducing market impact.

The calculation of VWAP itself is crucial. Most brokers use official closing VWAP from a major exchange (NYSE, NASDAQ) or a data vendor (Bloomberg, FactSet). The client and broker agree beforehand: "VWAP as calculated by NASDAQ" or "NASDAQ-closing VWAP." This removes disputes. Once the market closes, VWAP is fixed and known to everyone; there is no ambiguity.

## The trader's side: certainty over optionality

As a client, a guaranteed VWAP order removes timing anxiety. You do not need to watch the market all day or second-guess when to enter. You do not need to worry that your 10 million-share order will crush the stock if you try to execute in 30 minutes. The broker takes that risk. You know you will pay or receive a price very close to the day's actual volume-weighted average, and that is the price you budgeted.

This certainty is valuable for passive rebalancing, fund flows into [mutual funds](/mutual-fund/), or any situation where you are indifferent to timing and care only about hitting a known benchmark. An alternative is to submit a [TWAP order](/algorithmic-twap-order/) or [basis order](/basis-order/), where you take more of the execution risk in exchange for lower fees or full transparency.

## Costs and trade-offs

The cost of a guaranteed VWAP is the fee or spread, usually 1–5 basis points depending on the stock's liquidity and the order size. For a 10 million-share order at $100/share—$1 billion notional—a 2 basis-point fee is $200,000. That is a real cost, but it buys you certainty and the benefit of the broker's trading infrastructure and expertise.

If you are patient and willing to submit an algorithmic order yourself, or if you have an in-house trading desk, you might execute cheaper than VWAP on any given day. But you also bear the risk of doing worse. Over many orders, the guaranteed VWAP fee can be cheaper than frequent slippage, especially for large orders in volatile periods.

## When brokers decline the guarantee

Brokers will refuse guaranteed VWAP orders on illiquid securities, very large orders (where tracking risk is extreme), or during market dislocations. If a stock is thinly traded or halted, VWAP is hard to achieve and the broker's cost explodes. Similarly, if you ask for a guaranteed VWAP on $10 billion of a mid-cap stock, few brokers will accept the concentration risk.

Certain asset classes (bonds, structured products, FX) use VWAP-like concepts but without formal guarantees because pricing is decentralized and VWAP is harder to compute.

## See also

<div class="wiki-seealso">

### Closely related

- [TWAP Order](/algorithmic-twap-order/) — time-weighted alternative, leaving tracking risk with trader
- [Basis Order](/basis-order/) — spread-based alternative for basket trading
- [Broker](/broker/) — the counterparty bearing VWAP tracking risk
- Volume-Weighted Average Price — the guaranteed benchmark
- Market Impact — minimized by VWAP's delegation to the broker

### Wider context

- [Algorithmic Trading](/algorithmic-trading/) — the methods brokers use to achieve VWAP
- Execution Algorithm — technical framework
- [Mutual Fund](/mutual-fund/) — frequent user of guaranteed VWAP orders
- [Liquidity Risk](/liquidity-risk/) — borne by broker in a VWAP guarantee
- [Over-the-Counter Market](/over-the-counter-market/) — where VWAP guarantees are less common

</div>
