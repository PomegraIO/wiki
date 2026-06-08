---
title: "Bracket Order Explained"
description: "A bracket order combines entry, profit target, and stop-loss into one instruction, automating your complete trade plan from execution."
keywords:
  - bracket order explained
  - bracket orders trading
  - entry with stops and targets
  - automated trade plan
  - bracket order mechanics
  - two-legged order
image: "/svg/trading.svg"
---

*A **bracket order** is a single instruction that places an entry order, then immediately queues two exit orders — a profit-taking [limit order](/limit-order-vs-market-order-when-to-use/) above entry and a [stop-loss](/market-order-risk-in-low-liquidity/) below entry — so your risk, reward, and entry are locked in before the trade begins.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bracket Order Structure — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">One entry order spawns two exit orders; whichever fills first cancels the other.</div>

|   |   |
|---|---|
| **Entry order** | Buy/sell at market or limit price |
| **Profit target** | Limit order above buy (or below short) to lock gains |
| **Stop-loss** | Stop order below buy (or above short) to cap losses |
| **Execution rule** | Whichever exit fills cancels the other |
| **Best for** | Defined-risk trades with known targets and stops |
| **Main limitation** | No protection against [slippage](/market-order-risk-in-low-liquidity/) on entry fill |

</aside>

## The three-part structure

A bracket order bundles entry, profit target, and stop-loss into a single order submission. You specify:

1. **Entry**: Buy 100 shares of XYZ at $50 (or $50 market)
2. **Upper leg (profit target)**: Sell 100 shares at $55 [limit order](/limit-order-vs-market-order-when-to-use/)
3. **Lower leg (stop-loss)**: Sell 100 shares at $47 [stop order](/market-order-risk-in-low-liquidity/)

Once your entry order fills at $50, both exit orders activate simultaneously. If the stock rises to $55, your limit order fills and you're out at your target. The stop order automatically cancels. If the stock falls to $47, your stop fills at or below $47, and the limit order cancels. Only one exit can execute; the other vanishes.

## Why bracket orders simplify trading

The core appeal is mechanical. Once you submit the bracket, your risk and reward are determined. You don't have to babysit the position, set mental stops, or hand-enter exit orders once the entry fills. This removes emotional friction and ensures you have a plan before the trade begins.

For short-term traders, this is invaluable. You decide your acceptable risk ($3 per share in the example above) and your expected reward ($5 per share), then execute. The risk-reward ratio is explicit: 3 to 5 is unfavorable to many traders, so you might adjust your target or stop. But that negotiation happens before money is at risk, not mid-trade.

Bracket orders also force discipline. They make you articulate "if I'm wrong by X amount, I'm out." Many retail traders resist setting stops until losses mount, then exit in panic at the worst price. A bracket order locks in the stop level preemptively.

## When the entry doesn't fill as expected

Bracket orders have a subtle vulnerability: they assume the entry fills at your specified price. If you submit a bracket to buy 100 shares at $50 limit, and the stock leaps to $51, your entry never triggers — and neither do the exits. You're left order-less, watching the stock continue up, with no trade executed.

Conversely, if you use a market entry and the stock gaps or slips, you may fill at $51 instead of $50. Your profit target is still $55 and your stop is still $47, so your risk-reward ratio changes. The bracket was built around a $50 entry; if you filled at $51, you're now risking $4 to win $4 — a worse trade. Most traders accept this as the cost of execution certainty.

## Partial fills and position sizing

Bracket orders typically execute all-or-nothing: either the full entry fills (or gets cancelled if it doesn't), or the orders don't activate. Some platforms allow partial fill handling, but this complicates the bracket logic. If you submit a bracket for 100 shares and only 60 fill at entry, do both exits scale to 60? Most brokers require you to re-submit or manually adjust.

For this reason, bracket orders work best on [liquid stocks](/stock-exchange/) where fills are predictable. On a stock with a wide [bid-ask spread](/bid-ask-spread/) or low volume, your entry might partially fill, leaving you with an incomplete bracket.

## Profit-target mechanics

The upper exit leg is typically a [limit order](/limit-order-vs-market-order-when-to-use/). This gives you price certainty: if the stock reaches $55, you're out at $55 (or better, if there's slippage). The drawback is that the stock might never reach $55. If it rallies to $54.90 and reverses, your limit order never fills, and the stock may fall through your stop while you're waiting for the target.

To mitigate this, some traders use a limit order for part of the position (say, 60% at the target) and let the remainder [trail behind](/trailing-stop-percentage-vs-dollar/) to capture further upside. This is no longer a pure bracket order, but a hybrid approach.

## Stop-loss mechanics and gap risk

The lower exit leg is a [stop order](/market-order-risk-in-low-liquidity/) that becomes a [market order](/market-order-risk-in-low-liquidity/) once the stock falls through your stop level. On a liquid stock, this executes promptly at or slightly below your stop price. On a gapping stock (especially at open or in response to news), the stock may gap below your stop level and you may fill at a much worse price.

Bracket orders offer no protection against overnight gaps or extreme volatility. If you buy a stock at $50 with a $47 stop, then a bad earnings announcement hits and the stock opens at $40, your stop-loss order will fill at or near $40, not $47. Your loss is $1,000 (100 shares × $10), not the $300 ($100 shares × $3) you expected.

## Sector and market conditions

Bracket orders work best in calm, liquid markets where stocks move gradually and gaps are rare. A trader in a [blue-chip stock](/stock/) trading millions of shares daily can set a tight bracket with confidence. A trader in a micro-cap or biotech stock prone to news-driven gaps faces real risk that the stop-loss will fail to protect at the intended level.

High-volatility environments make bracket orders riskier because the distance between entry and stop must widen to avoid whipsaws, which in turn widens potential loss. A stable stock lets you set a tight bracket; a volatile stock requires you to loosen it, increasing risk.

## Bracket orders versus other strategies

Unlike [trailing stops](/trailing-stop-percentage-vs-dollar/), bracket orders have fixed exit levels; the stops don't move as the stock rises. If you want your stop to climb with the stock, you need a separate trailing-stop instruction. Some platforms allow "bracket orders with trailing stops," which combine the initial entry structure with dynamic stop adjustment — but this is a platform-specific feature.

Compared to manual order entry, bracket orders save time and enforce discipline. You're trading a defined-risk scenario: "I can lose X, I want to win Y, I'm entering at Z." The math is done upfront. Compared to [algorithmic trading](/algorithmic-trading/) or complex multi-leg strategies, bracket orders are simpler and more transparent.

## See also

<div class="wiki-seealso">

### Closely related

- [Trailing Stop: Percentage vs Dollar Amount](/trailing-stop-percentage-vs-dollar/) — dynamic stop-loss that rises with price, versus bracket's fixed stops
- [Limit Order vs Market Order: When to Use Each](/limit-order-vs-market-order-when-to-use/) — entry and exit certainty trade-offs
- [Market Order Risk in Low-Liquidity Stocks](/market-order-risk-in-low-liquidity/) — why stops may slip on thin stocks

### Wider context

- [Bid-Ask Spread](/bid-ask-spread/) — the gap between buy and sell prices affecting execution
- [Stock Market](/stock-market/) — how stocks trade and settle
- [Stop Order](/limit-order-vs-market-order-when-to-use/) — mechanism underlying the stop-loss leg
- [Market Maker Trading](/market-maker-trading/) — who fills your orders and how

</div>
