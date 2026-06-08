---
title: "Maker-Taker vs Taker-Maker Fee Models"
description: "Learn how maker-taker and taker-maker exchange fee structures differ, and why each shapes order routing and trading costs differently."
keywords:
  - maker taker exchange fees
  - taker maker fee model
  - market maker rebates
  - exchange fee structures
  - order routing incentives
  - trading cost model
---

*The **maker-taker fee model** rewards traders who supply liquidity (makers) with rebates while charging those who consume it (takers), whereas the **taker-maker model** reverses that logic, charging makers and rebating takers. Which model applies shapes the effective cost of a trade and how brokers route orders.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fee Models — key contrasts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two competing incentive structures that flip who bears the cost of providing liquidity.</div>

|   |   |
|---|---|
| **Maker-Taker** | Rebate to those adding limit orders; fee from those taking liquidity |
| **Taker-Maker** | Rebate to those taking liquidity; fee from those providing it |
| **Typical rebate size** | $0.20–$0.50 per 100 shares (US equities) |
| **Adoption** | Maker-taker dominates US equities and equity options |
| **Main effect** | Encourages passive market-making; discourages aggressive order-taking |
| **User impact** | Frequent traders benefit more than buy-and-hold investors |

</aside>

## The core difference

Under maker-taker, the exchange or market operator charges a taker (an aggressive trader who places a market order or crosses the spread) and pays a rebate to the maker (a patient trader whose limit order was filled). Imagine a stock trading at $100.05 bid / $100.10 ask. A trader who buys at $100.10 by submitting a market order is the taker; the trader whose limit order to sell at $100.10 is resting on the book is the maker. The taker pays a fee; the maker receives a rebate.

Taker-maker flips the logic entirely. The exchange charges the maker (the patient limit-order provider) and rebates the taker (the aggressive market-order placer). The same trade would now see the market maker pay and the aggressive buyer receive a rebate.

## Why maker-taker became dominant

Nasdaq and the SEC adopted maker-taker explicitly in the 2000s to encourage the participation of passive market makers. The idea was simple: if you supply liquidity at the ask and someone buys from you, you earn a rebate instead of losing money on the bid-ask spread. This expanded the ecosystem of retail-focused electronic communication networks (ECNs) and electronic market makers, shrinking spreads and increasing trading volume.

The result worked. When maker-taker arrived, US equity spreads narrowed significantly, and trading volume grew. Brokers—especially those offering low-cost retail access—loved the model because rebates offset some of their order-execution costs, allowing them to offer commissionless trading and still profit.

## Taker-maker and its rare applications

A handful of exchanges, notably some European venues and certain cryptocurrency platforms, have used taker-maker to charge aggressive traders and reward patient ones. The stated aim is to discourage high-frequency trading and flash orders while favoring buy-and-hold investors. Some regional or equity derivative venues have also tested it to differentiate themselves from the Nasdaq / NYSE duopoly.

Taker-maker trades remain much rarer. One reason: most sophisticated traders and market makers prefer a model that rewards them for sitting on the book. Flipping the incentive doesn't just change who gets paid; it often shrinks overall participation if the rebate levels don't stay generous enough to compete with maker-taker venues for order flow.

## How each model affects trading decisions

The fee structure baked into an exchange's model powerfully influences how traders and brokers route orders. Under maker-taker, a broker has incentive to route retail customer orders to venues where the rebate is highest (assuming executions and fees are otherwise equivalent). A customer buying 100 shares might land on the exchange where the maker rebate is fattest, not necessarily where the spread is tightest. This can occasionally hurt price execution quality for the customer.

Conversely, taker-maker encourages brokers to route to the venues with the lowest taker charge or highest taker rebate. The priority shifts—suppliers of liquidity may face less incentive to show orders, since they are charged instead of rebated.

## The real cost to the trader

The nominal fee paid by the taker (say, $0.30 per 100 shares) is only half the story. What matters is the *effective* cost after rebates and fees are netted across all the venues where an order might execute. A frequent retail trader under maker-taker may find that their buy orders land at rebate-paying venues, effectively reducing their cost below the posted fee. Conversely, aggressive proprietary traders or high-frequency firms paying taker fees bear a direct cost that doesn't benefit them as makers.

Under taker-maker, the taker often faces no charge or a rebate, but passive limit-order providers—including retail traders entering limit orders—pay. For a buy-and-hold investor placing a single limit order and forgetting it, the fee structure matters less. For someone constantly managing orders, it compounds.

## Regulatory debate

US regulators have occasionally questioned whether maker-taker incentives distort routing decisions in ways that harm retail investors. The SEC has examined whether exchanges use rebates to lure order flow that would be better served elsewhere. Some proposals have surfaced to cap or eliminate rebates, or to require brokers to disclosure rebate conflicts of interest more explicitly. No broad ban has materialized, and the model persists as the standard in US equities.

Internationally, the taker-maker and flat-fee models continue as alternatives, particularly where regulators view maker-taker as tilting the field toward high-frequency and algorithmic trading.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the fundamental cost of immediacy that fee models layer on top of
- [Market Maker](/market-maker-trading/) — the passive liquidity provider who benefits from maker rebates
- [Market Order](/market-order/) — the aggressive order that pays the taker fee
- [Limit Order](/limit-order/) — the patient order that earns the maker rebate
- [Alternative Trading System](/alternative-trading-system/) — the smaller venues competing for order flow through fee structures

### Wider context

- [Stock Exchange](/stock-exchange/) — the central venues where fee models are applied
- [Algorithmic Trading](/algorithmic-trading/) — strategy type that fee structures can inadvertently incentivize
- [Price Discovery](/price-discovery/) — the market function that rebates are meant to enhance
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — the regulator that oversees fee fairness

</div>
