---
title: "Principal Trading"
description: "A financial firm buying or selling securities for its own account rather than as an agent for clients."
keywords:
  - principal trading
  - proprietary trading
  - market making
  - dealer inventory
---

*Principal trading occurs when a financial firm commits its own capital to buy or sell [securities](/wiki/securities-and-exchange-commission/), [derivatives](/wiki/derivatives-exchange-crypto/), or currencies, with the intent to profit on the spread or price movement. This contrasts with [agency trading](/wiki/broker/), where a firm merely matches buy and sell orders without taking risk.*

<aside class="wiki-infobox">

| Concept | Definition |
|---|---|
| **Principal** | The firm owns the [security](/wiki/securities-and-exchange-commission/) and bears [market risk](/wiki/market-risk/) |
| **Agency** | The firm brokers trades without holding inventory |
| **Market Maker** | A principal trader providing [liquidity](/wiki/liquidity-risk/) by maintaining bid-ask [spreads](/wiki/bid-ask-spread/) |
| **Profit Motive** | Spread capture (sell high, buy low) or directional bets |
| **Inventory Risk** | Price moves against the firm's holdings |
| **Financing Cost** | Carry cost of holding [securities](/wiki/securities-and-exchange-commission/) overnight |
| **Regulation** | Broker-dealers must separate agency and principal accounts |
| **Examples** | [Market makers](/wiki/market-makers/), [proprietary trading](/wiki/algorithmic-trading/), [hedge funds](/wiki/hedge-fund/) |

</aside>

## Principal trading vs. agency trading: the structural divide

In agency trading, a broker finds a buyer and seller, matches them, and earns a commission. The broker never owns the [security](/wiki/securities-and-exchange-commission/), takes no [market risk](/wiki/market-risk/), and profits only if the trade completes. In principal trading, a dealer buys 1,000 shares of Apple at $150/share, holds them in inventory, and later sells them at $150.05—pocketing the $50 spread. The dealer bears the risk that Apple stock falls to $149 before the shares are sold, crystallizing a loss.

This distinction matters because:
- **Principal traders** have incentives to hold inventory, provide [liquidity](/wiki/liquidity-risk/), and absorb volatility. They profit from [spreads](/wiki/bid-ask-spread/), not trading volume.
- **Agency traders** (brokers) have incentives to maximize trading volume and minimize inventory. They profit from commissions.

Most major [broker-dealers](/wiki/broker/) operate both sides: they earn spreads on principal trading and commissions on agency business. Regulators require firewall separation to prevent conflicts of interest.

## Market makers as principal traders

The classic principal trader is a [market maker](/wiki/market-makers/)—a dealer who continuously buys and sells, maintaining bid-ask [spreads](/wiki/bid-ask-spread/). On a [stock](/wiki/stock/), a market maker might be willing to buy at $100.00 (bid) and sell at $100.05 (ask). For every round-trip trade ($100.00 → $100.05), the market maker profits $0.05 per share (the spread).

Market makers provide the critical economic function of absorbing imbalance. If 1,000 buyers arrive before sellers, a market maker buys shares to prevent a price spike. If sellers dominate, the market maker holds inventory and sells, preventing a collapse. This inventory absorption incurs [carrying costs](/wiki/cost-of-carry/) (financing the inventory overnight) and [market risk](/wiki/market-risk/) (if prices move sharply against the position). To compensate, market makers earn the spread.

## Proprietary trading: the now-constrained activity

Proprietary trading is principal trading with explicit directional intent. A [bank](/wiki/bank-reserve-injection/) sets up a proprietary desk that bets on stocks, [bonds](/wiki/bond-basics/), [currencies](/wiki/currency-pair/), or [commodities](/wiki/commodity-swap/) using the bank's balance sheet. If the desk believes Apple is undervalued, it buys aggressively. Unlike market making (which is market-neutral and spread-focused), prop trading is directional and profit-seeking.

The 2008 financial crisis exposed that prop trading at large banks contributed to excessive risk-taking. [Goldman Sachs](/wiki/goldman-sachs/), [Morgan Stanley](/wiki/morgan-stanley/), and others racked up billions in prop trading losses. In response, the [Dodd-Frank Act](/wiki/dodd-frank-act/) introduced the **Volcker Rule** (Section 619), which banned federally insured banks from proprietary trading. The intent was to separate the speculative, risky activities from the deposit-taking, lending businesses that are critical to the financial system.

The Volcker Rule's implementation was contentious. Banks argued that distinguishing prop trading from [market making](/wiki/market-makers/) is impossible (they use the same traders and capital). Regulators countered that risk limits and trading strategies can be monitored. After years of legal and regulatory debate, enforcement remains active but inconsistent.

## Why principal trading carries inherent risks

Principal traders must finance their inventory. If a market maker holds 100,000 shares of a stock overnight, the cost is: 100,000 × stock price × overnight [interest rate](/wiki/interest-rate/). During normal times, overnight rates are low (0.5–1.5%), and financing is cheap. During crises (like March 2020), overnight [repo](/wiki/repurchase-agreement/) rates spike to 10%+, and carrying costs become prohibitive.

Additionally, principal traders face **adverse selection risk**: if a customer suddenly wants to sell large amounts, the market maker must buy and hold inventory that may be about to fall in price (why the customer is selling). This "toxic flow" can erode spread profits, especially in periods of volatility.

Finally, principal trading creates **inventory risk**. A market maker that has accumulated 1 million shares of a stock faces potential loss if the market moves. To manage this, market makers set position limits, use [hedging strategies](/wiki/hedging-with-futures/), and monitor real-time [Greeks](/wiki/options-greeks/) (if trading [options](/wiki/option/)).

## Principal trading in derivatives and foreign exchange

In [derivatives](/wiki/derivatives-exchange-crypto/) markets, principal trading is ubiquitous. Investment banks act as [market makers](/wiki/market-makers/) in [interest-rate swaps](/wiki/interest-rate-swap/), [credit default swaps](/wiki/credit-default-swap/), and [equity options](/wiki/call-option-equity/). They quote prices to clients (principal quotes) and earn spreads. They also hedge their principal positions by trading with other dealers.

In **[foreign exchange](/wiki/forex-leverage/)**, principal trading is the norm. Dealers buy and sell [currency pairs](/wiki/currency-pair/) continuously, earning tiny spreads (0.0001 on EUR/USD). Success depends on high volume, tight [spreads](/wiki/bid-ask-spread/), and low financing costs. During the 2015 Swiss franc shock, principal traders in [forex](/wiki/forex-leverage/) faced catastrophic losses when the [Swiss National Bank](/wiki/central-bank/) suddenly appreciated the franc by 20% in one day. Many dealers had shorted the franc (betting it would weaken), and losses exceeded their capital.

## Distinguishing principal trading from agency trading in practice

Regulators struggle to distinguish principal from agency trading. Consider a [broker](/wiki/broker/) that receives a large buy order: the broker could (a) immediately find a seller (agency) or (b) buy first, then try to sell (principal). Both occur in sequence, but (b) is principal trading.

The Volcker Rule attempts to distinguish by prohibiting trades where the bank has "trading desks" using the bank's capital. But "desks" and "trading strategies" are vague. [Goldman Sachs](/wiki/goldman-sachs/) faced enforcement action in 2020 for allegedly operating prohibited prop trading desks disguised as [market-making](/wiki/market-makers/) operations.

## Recent shifts: passive execution and internalization

In recent years, principal trading has been rebranded. Many large banks now use "internalization"—they route client orders through their own principal account as a form of principal trading, arguing it improves execution by eliminating exchange prices. Critics argue it is predatory principal trading, where the bank profits at the client's expense by embedding unfavorable pricing.

**Payment for order flow** (PFOF) is a related phenomenon: retail [brokers](/wiki/broker/) sell customer orders to [market makers](/wiki/market-makers/) (principal traders), who then execute the orders at slightly worse prices than available on public exchanges. This monetizes client order flow and enriches the broker and the principal trader at the customer's expense. PFOF is controversial and faces regulatory pushback.

## Conclusion: principal trading's paradox

Principal trading is essential for market liquidity and the functioning of financial markets. Without [market makers](/wiki/market-makers/) who principal trade, [spreads](/wiki/bid-ask-spread/) would widen, and transactions would become costly. Yet principal trading also creates [systemic risk](/wiki/systemic-risk/): large principal traders can amplify volatility and trigger crises if they abruptly withdraw [liquidity](/wiki/liquidity-risk/) (as happened on Flash Crash day, May 6, 2010, and during the March 2020 pandemic panic).

Regulators balance this by requiring [capital reserves](/wiki/capital-adequacy/), position limits, [stress testing](/wiki/stress-testing/), and [market surveillance](/wiki/market-surveillance/). As [algorithmic trading](/wiki/algorithmic-trading/) and [high-frequency trading](/wiki/high-frequency-trading/) accelerate principal trading speed and scale, the balance between efficiency and risk becomes ever more precarious.

<div class="wiki-seealso">

### Closely related
- [Market makers](/wiki/market-makers/) — Dealers providing bid-ask spreads
- [Bid-ask spread](/wiki/bid-ask-spread/) — The spread between buy and sell prices
- [Proprietary trading](/wiki/algorithmic-trading/) — Directional trading using firm capital
- [Market making](/wiki/market-makers/) — Core principal-trading activity

### Wider context
- [Broker-dealer](/wiki/broker/) — Firms engaged in both agency and principal trading
- [Volcker Rule](/wiki/volcker-rule/) — Ban on proprietary trading at banks
- [Liquidity](/wiki/liquidity-risk/) — Ability to buy or sell at market prices
- [Market surveillance](/wiki/market-surveillance/) — Monitoring for manipulation and abuse

</div>
