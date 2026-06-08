---
title: "Slippage Cost Per Trade"
description: "Slippage cost per trade is the difference between expected and actual execution price; it accumulates across fills and hits hardest in illiquid or volatile markets."
keywords:
  - slippage cost per trade
  - price slippage execution
  - trading slippage definition
  - market slippage costs
  - adverse price movement
image: "/svg/trading.svg"
---

*A **slippage cost per trade** is the difference between the price you expected to pay (or receive) and the price you actually paid (or received) when an order executed—a hidden friction that erodes returns one fill at a time.* For retail traders executing small orders in liquid markets, slippage might be fractions of a cent per share; for institutional traders moving large size in thinly traded securities, slippage can exceed dollars per share. Unlike a commission, which appears as a line item on a broker statement, slippage is invisible—yet it accumulates across all the trades a portfolio makes.

## How Slippage Occurs

Slippage happens for three core reasons.

**Bid-ask spread** is the first and most immediate. You decide to buy a stock; the bid (what buyers offer) is $100.00 and the ask (what sellers ask) is $100.10. You buy at the ask. Slippage: $0.10. This spread exists because market makers require compensation for providing instant liquidity and bearing inventory risk. It's measurable and unavoidable for any trade you want to execute right now.

**Market impact from your own order** occurs when your trade is large enough to move the market. Suppose a day trader wants to buy 50,000 shares of a mid-cap stock with average daily volume of 200,000 shares. The first 10,000 shares might fill at $100.10; as the order consumes available sellers, the ask ticks up to $100.15, $100.20, and so on. By the time all 50,000 shares are filled, the average execution price might be $100.35—$0.25 of slippage purely from the order's own weight on the market. This impact scales with order size, illiquidity, and speed of execution.

**Timing delays and volatility** create slippage when conditions change between your decision and execution. You decide to sell a stock at 9:30 AM when it's trading at $50.00; the order takes 2 seconds to route and execute, but the stock drops to $49.98 during that window. Slippage: $0.02. In fast markets or during news events, this delay slippage can spike unpredictably.

## Slippage at Different Account Sizes

The impact of slippage per dollar invested is vastly different depending on position size.

A retail investor buying 100 shares of Apple at $180 per share ($18,000 invested) might incur a $0.05 spread—a slippage of 0.03%. The same investor buying 100 shares of a micro-cap OTC stock with a $0.50 spread suffers $50 of slippage on a $2,000 position, or 2.5%—the same position size as a percentage of their account but 80 times worse as a drag on returns.

An institutional investor buying 1 million shares of a mid-cap stock in normal conditions might experience average slippage of $0.15 per share across the entire fill—not from spread alone, but from market impact accumulation across tranches. That's $150,000 of slippage on a $150 million position (0.1%), which is manageable. But if volatility spikes or the order goes out during low-volume hours, slippage could double or triple, creating a $450,000 drag that materially affects fund performance.

For a typical day trader making 10 trades per day with average position size of $5,000 per trade, cumulative slippage of $5 to $20 per trade (0.1% to 0.4%) compounds to $50–$200 daily—before accounting for commissions or the spread of wins versus losses. Over 250 trading days, that's $12,500–$50,000 in slippage alone, a meaningful cost that many retail traders don't consciously track.

## Measuring Slippage

The simplest measure is **arrival price slippage**: the difference between the mid-market price when an order is submitted and the average execution price.

**Slippage Per Share = Execution Price − Expected/Decision Price**

For a buy order:
- Decision price (mid-market): $100.00
- Execution price (average fill): $100.12
- Slippage: $0.12 per share

For a sell:
- Decision price: $100.00
- Execution price: $99.88
- Slippage: $0.12 per share (same direction, unfavorable)

Some traders also track **real-time slippage**, comparing the price at the instant you hit send versus the fill price. If the stock moved from $100.00 to $100.08 in the 300 milliseconds it took your order to reach the market, that $0.08 is timing slippage you cannot recover.

Professional traders decompose slippage further:
- **Spread slippage**: The cost of crossing the bid-ask.
- **Market impact slippage**: The price tick-up or tick-down from your order's own size.
- **Timing slippage**: The price move between decision and execution.

The ratio of these components depends on order size and market conditions. A small retail order is nearly 100% spread; a multi-million share institutional order can be 70% market impact and 20% timing, with spread becoming almost negligible.

## Why Slippage Hurts More in Illiquid Markets

A stock with 1 million shares of daily volume and a $0.02 spread behaves very differently from a stock with 50,000 shares of daily volume and a $0.50 spread—even if both trade at $100 per share.

Buying 10,000 shares in the liquid stock: You consume 1% of daily volume, market impact is minimal, and total slippage might be $0.03 per share.

Buying 10,000 shares in the illiquid stock: You are 20% of daily volume, and you will face a wall of ask prices climbing higher as you consume available liquidity. If the first 2,000 shares are at $100.50, the next 2,000 at $100.75, the next at $101.00, and so on, your average execution price could be $101.10—$1.10 of slippage on a $100 stock. That's a 1.1% cost just from execution, before any commission.

Fast-moving markets amplify slippage further. In a stock that's surging on news, the bid-ask spread widens from $0.02 to $0.50, and by the time your order reaches the market, the mid has already moved up $0.30. Your expected slippage triples or quadruples.

## Cumulative Impact Across a Portfolio

A fund that makes 500 trades per year across 50 different securities—a typical mid-cap or small-cap strategy—might average 0.08% slippage per trade if well-executed, or 0.15% if poorly executed. Over 500 trades:

- Good execution: 500 × 0.08% = 40 basis points annual drag
- Poor execution: 500 × 0.15% = 75 basis points annual drag

A 35 basis point difference in total slippage is roughly equivalent to a 0.35% annual fee—the difference between a cheap index fund and a modestly priced actively managed fund. For active managers claiming 100 basis points of alpha, execution quality (the difference between good and sloppy slippage management) can claim half that edge.

Retail day traders are even more exposed. A trader making 20 round-trip trades per month (buys and sells) with average slippage of 0.3% per leg incurs 0.6% per round-trip × 240 annual trades = 144 basis points of slippage—a hurdle that nearly all active retail traders fail to clear after accounting for taxes and opportunity cost.

## Strategies to Minimize Slippage

**Limit orders** replace market orders to avoid worst-case slippage; you specify a price and accept the risk that the order doesn't fill. This trades certainty of execution for control over price.

**Scaling in and out** (breaking large orders into smaller tranches) reduces market impact, especially over time. Rather than buy 100,000 shares at once, a patient trader buys 20,000 each day, averaging the price over a week and reducing the price impact of any single day.

**Off-peak execution** can help for illiquid stocks; trading in the first hour after open or final hour before close often offers better spread and less impact than lunch-hour lows.

**Broker selection** matters. Institutional brokers offer smart order routing, dark pool access, and algorithms that can reduce market impact 10–20% versus naive execution.

For retail traders, **choosing liquid instruments** is often the single highest-impact decision: trading large-cap stocks and major ETFs minimizes spread and impact versus micro-caps or illiquid options.

## See also

<div class="wiki-seealso">

### Closely related

- [Implementation Shortfall Explained](/implementation-shortfall-explained/) — The complete gap between decision price and execution price across all fills
- [Bid-Ask Spread Cost for Small Accounts](/spread-cost-small-account/) — How spreads disproportionately affect smaller traders
- [Payment for Order Flow: Cost to Retail Traders](/payment-for-order-flow-cost-to-retail/) — Whether free trading routes through wholesalers cause hidden slippage
- [Market Maker Trading](/market-maker-trading/) — How spreads are set and why they widen in stress
- [Limit Order](/limit-order/) — Setting price floors to control slippage
- [Market Order](/market-order/) — Accepting whatever price is immediately available

### Wider context

- [Algorithmic Trading](/algorithmic-trading/) — Execution algorithms designed to minimize slippage
- [Over-the-Counter Market](/over-the-counter-market/) — Where slippage can be extreme due to lower liquidity
- [Liquidity Risk](/liquidity-risk/) — The broader framework for understanding execution risk
- [Price Discovery](/price-discovery/) — How trades reveal and influence market prices

</div>
