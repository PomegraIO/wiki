---
title: "Payment for Order Flow: Cost to Retail Traders"
description: "Payment for order flow arrangements route retail orders to market makers who pay brokers for the order, potentially resulting in inferior execution prices for retail traders."
keywords:
  - payment for order flow cost to retail traders
  - PFOF execution costs
  - order flow monetization
  - retail trading rebates
  - wholesaler order routing
image: "/svg/trading.svg"
---

*Payment for order flow (PFOF) is a fee arrangement in which a market maker pays a broker to route customer orders to them instead of sending those orders to a stock exchange—a model that offers retail traders "free" or "commission-free" trading while potentially hiding the cost in worse execution prices.* The debate over PFOF centers on a simple question: when a retail investor saves $0 in commission but receives a slightly worse price than they would on an exchange, who benefits and who pays?

## How Payment for Order Flow Works

Under the traditional model, a retail investor places a buy order through a broker. The broker sends the order to an exchange (like NASDAQ or NYSE), where it is matched with a seller. The exchange may or may not offer a rebate to the broker for adding liquidity, but the core transaction is transparent—the buyer and seller meet at a published price on a lit venue.

Under PFOF, the broker instead routes the order to a market maker (a proprietary trading firm) who is willing to *pay* the broker for that order. The market maker fills the retail investor's order at a price the market maker chooses, then either closes out their inventory on an exchange or hedges the position. The broker receives a few cents per share (sometimes more); the retail investor receives "free" trading; the market maker profits from the spread between the retail order price and the exchange price they use to hedge.

The SEC and FINRA allow PFOF because the broker is required to offer the retail customer "best execution"—a standard that has been defined (controversially) as not just price, but a bundle of factors including speed, likelihood of immediate execution, and overall value. A market maker paying for an order must offer a price at least as good as the best publicly quoted price at the time the order reaches the market maker—a requirement called the National Best Bid and Offer (NBBO) rule.

In theory, the NBBO rule protects retail traders. In practice, the line between "as good as NBBO" and "better than retail could get elsewhere" is where PFOF extracts its cost.

## The Execution Cost Question

Consider a simple scenario. You place a market buy order for 100 shares of a $100 stock at 10:00 AM. At that instant:

- The best ask on NASDAQ is $100.10 (the best price you could get by routing to the exchange).
- A market maker accepting PFOF offers the broker $100.12 for your order (better than NBBO).
- Your broker accepts the market maker's offer.
- You fill at $100.12.

This looks like a win: you got $100.12 when the worst exchange price was $100.10. Your broker also won: they earned, say, $0.05 per share in PFOF revenue ($5 on the 100-share order). The market maker won: they bought at $100.12 and sold the hedge on NASDAQ at $100.10 to other customers, pocketing $0.02 per share ($2).

But the math is revealing. The market maker was willing to pay the broker $0.05 per share ($5 total) to get this order, because they expected to profit more than $0.05 per share on the entire round-trip. If the market maker's total profit is $0.07 per share, that's $7 extracted from the retail customer's side of the market—a cost that is real, even though the price you received was "better than NBBO."

The real comparison is not between PFOF price and exchange price, but between what you could have achieved with an unmediated exchange order versus what you got. If an exchange order would have filled at $100.09 (perhaps a patient limit order a fraction below the $100.10 ask) and PFOF fills you at $100.12, you've lost $0.03 per share due to PFOF, even though PFOF is "better than NBBO."

## Why Retail Orders Are Valuable to Market Makers

Market makers pay for retail order flow because retail orders are typically small, non-strategic, and predictable in aggregate.

A retail investor buying 100 shares of Apple has no hidden agenda; they're not front-running a large block trade, and they're not exploiting information. From a market maker's perspective, a retail order is easy money: the market maker can immediately hedge the short-term inventory risk on an exchange and pocket the spread.

Professional traders, by contrast, often move in ways that correlate with information or large block trades. A professional's buy order might signal that a big buyer is accumulating; a market maker might lose money taking the other side because the price is about to spike. Retail orders carry no such adverse selection risk.

This information asymmetry is what allows market makers to profit from PFOF. They pay for retail orders because retail orders are low-risk; they avoid or charge more for professional orders because those carry information risk. The $0.05 they pay the broker for your order is cheap insurance against adverse selection compared to the cost of trading with a hedge fund or algorithmic trader.

## Measuring the Cost

Quantifying PFOF cost is harder than it appears, because the counterfactual (what you would have received) is never observed.

Academic research and SEC analysis suggest that:

- For highly liquid mega-cap stocks (Apple, Microsoft, Tesla), PFOF costs are typically 0–2 basis points (0–0.02%), sometimes in the retail trader's favor if the market maker is in aggressive competition for order flow.
- For less liquid large-cap stocks, PFOF costs can reach 2–5 basis points.
- For mid-cap and small-cap stocks, PFOF costs can exceed 10 basis points (0.1%), where the market maker's edge widens substantially.

To put this in perspective: on a $10,000 retail order in a mega-cap stock, 1 basis point of cost is $1. On the same order in a thinly traded mid-cap, 10 basis points is $10. For day traders making 20 trades per month, 5 basis points per trade compounds to 60 basis points annual—a material drag.

The 2023 SEC examination of several major PFOF brokers found evidence that they had not always routed orders to market makers offering the best price; in some cases, brokers prioritized order flow that generated the highest PFOF revenue rather than the best execution. These findings led to enforcement actions and settlements, but the practice persists.

## The Comparative View: PFOF vs. Commission

The trade-off between commission and execution quality is genuine. In the pre-PFOF era (1990s), retail commissions were high—$10–$25 per trade—and trading costs at the retail level were a significant hurdle. PFOF, paired with commission-free trading, democratized market access; a retail trader could now make dozens of trades without eroding capital to fees.

But the question is whether zero commission is truly better if execution quality has declined by an offsetting amount. A trader paying $5 commission but receiving exchange-best price might break even versus a trader paying zero commission but receiving a price $0.05 worse on the same order.

For very small accounts or very passive traders (a few trades per month), PFOF may be a net benefit because the execution cost is low and the ease of access is high. For active day traders or swing traders, PFOF can be a significant drag.

## Alternatives to PFOF

Some brokers have moved away from PFOF, instead:

- Charging modest commissions ($1–$2 per trade) and routing to exchanges, capturing no PFOF revenue but claiming better execution quality.
- Operating as "market makers" themselves (internalization) and committing to NBBO or better; this avoids external PFOF payments but introduces broker-side conflicts of interest.
- Offering both PFOF and direct-exchange routing as separate account tiers, letting traders choose.

## The Regulatory Landscape

The SEC has expressed concern about PFOF, particularly regarding the misalignment of incentives (brokers choosing PFOF revenue over best execution). In 2023–2024, enforcement actions targeted major brokers for PFOF violations, but the model remains legal under best-execution standards. Attempts to ban PFOF outright (like the Gamestop Markets Act) have not passed Congress, and industry lobbying argues that PFOF is not inherently harmful—it is merely an alternative form of broker compensation that must be disclosed and monitored.

Disclosure requirements are now strict: brokers must inform retail customers whether they use PFOF and must publish quarterly reports on order routing, showing the volume of orders and execution quality by venue. This transparency is useful for sophisticated investors but rarely affects retail behavior.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread Cost for Small Accounts](/spread-cost-small-account/) — How spreads on executed trades directly affect retail capital
- [Slippage Cost Per Trade](/slippage-cost-per-trade/) — The price difference between intention and execution
- [Implementation Shortfall Explained](/implementation-shortfall-explained/) — The complete cost measure across institutional order execution
- [Market Maker Trading](/market-maker-trading/) — How market makers profit from retail order flow
- [Broker](/broker/) — Intermediaries and their role in order routing
- [Over-the-Counter Market](/over-the-counter-market/) — Off-exchange trading where PFOF is prevalent

### Wider context

- [Price Discovery](/price-discovery/) — How trading venues discover and communicate prices
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — The regulator overseeing best-execution standards
- [FINRA](/finra/) — Broker regulation and order routing compliance
- [Algorithmic Trading](/algorithmic-trading/) — How professionals minimize execution costs

</div>
