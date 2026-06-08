---
title: "Stop-Loss Order"
description: "An automatic sell order that executes when a position falls to a predetermined price, limiting losses on a trade."
keywords:
  - stop-loss order
  - loss limitation
  - exit strategy
  - automated trading
  - risk control
  - protective order
image: "/svg/risk.svg"
---

*A **stop-loss order** is a standing instruction to sell a security automatically once its price drops to a specified level, designed to cap the maximum loss on a position. It sits between active trading discipline and the psychological difficulty of admitting a trade went wrong.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stop-Loss Order — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for risk management and loss control." />

<div class="wiki-infobox-caption">An automated safety valve that removes emotion from the exit decision.</div>

|   |   |
|---|---|
| **What it is** | A pre-set order to sell when price hits a floor, locking in maximum loss |
| **Also called** | Stop order, loss-limiting order |
| **Typical use** | Exiting unprofitable trades before losses grow unbounded |
| **Key parameter** | Stop price (absolute or percentage below entry) |
| **Execution risk** | Order may fill below stop price in volatile markets (gapping) |
| **Cost implication** | Commissions apply; repeated stops can erode small gains |

</aside>

## Why traders place them, and why they hesitate

The appeal is straightforward: set it and walk away. You decide at the moment of entry—when thinking is clearest—where you will admit defeat. The stop becomes your off-ramp, protecting you from the most human of errors: holding a loser in the hope it bounces back, then watching the hole deepen.

But stop-loss orders are psychologically harder than they sound. Markets whipsaw. A stock touches your stop, triggers a sale at a loss, then rallies 20% the next week. That sting teaches traders to move stops higher after minor gains, or to widen them to avoid false exits. Both moves drift toward the same problem: the stop is no longer a rule, it's a suggestion. When discipline evaporates, so does the order's protection.

## The mechanics: price-based triggers

A stop-loss is typically entered as a stop price—an absolute dollar level or, more commonly, a percentage below the entry price. For example, you buy a stock at £100 and place a stop at £95. If the price touches £95 or falls below it, the order converts to a [market order](/market-order/) and sells at the next available price.

That conversion is the trap. In a liquid market, you sell near £95. In a volatile or illiquid one—a gapping down open, a sudden earnings miss—you may sell at £90 or £85. The order guaranteed you would *try* to exit at £95; it did not guarantee the *price* you'd receive.

Some platforms offer a stop-limit order, which pairs a stop price with a limit price: sell only if the price is at or better than the limit. This prevents panic-selling at distressed levels, but it also means your order may never execute, and you stay trapped in the losing position anyway.

## A flawed ally in [market-timing](/market-timing/) disguises

Stop-loss orders often fail for a simple reason: they're frequently set at round or psychologically significant levels where many other traders have stops too. A stock at £100 may attract stops at £95, £90, and £85. Smart market-makers or algorithmic traders know this and may push the price down just far enough to touch the level, triggering a cascade of stops, before reversing sharply upward. You sell the bottom, having been swept up in a liquidity vacuum.

More broadly, frequent stop-losses can fragment your returns. If you're stopped out of a winning thesis at a 5% loss, only to watch the position rise 30% in the next three months, your track record becomes a patchwork of small losses and missed gains. This is especially true for [volatile](/volatility-smile/) or cyclical holdings, which may require patience to recover.

The alternative—holding positions without stops and absorbing catastrophic losses—is worse. The middle ground is discipline: a stop placed at a level that respects volatility (not too tight) and serves a genuine thesis (not a fear-driven reflex).

## When stops make sense, and when they don't

Stops work best in liquid markets with tight [spreads](/bid-ask-spread/), where you can trust that your sell order fills near your stop price. They suit traders with finite risk capital and a strict loss tolerance—those who must protect against ruin.

Institutional [hedge funds](/hedge-fund/) often use stops on individual positions while maintaining a broader [portfolio](/asset-allocation/) view; a single position's exit doesn't dictate the overall [strategy](/value-investing/). Retail traders using stops on isolated picks often make the reverse mistake: slavishly following each stop while ignoring whether the broader portfolio is sound.

Stops are less useful for long-term investors. If you own a stock because you believe in its five-year fundamentals, a stop-loss at 20% down merely crystallizes a temporary drawdown into a permanent loss. You've exited on emotion precisely when holding takes discipline. [Value investors](/value-investing/) often forgo stops entirely, accepting that temporary weakness is part of the game.

The costs add up quietly. Commissions on each stop-triggered exit, slippage on the actual fill, and the mental tax of re-evaluating each stopped position—these erode returns in ways that simple arithmetic misses.

## The automation trap

Modern trading platforms make it trivial to set stops on hundreds of positions. Simplicity breeds false confidence. A trader might set a 10% stop on every long position, believing they've solved the risk problem. In reality, they've outsourced their judgment to a dumb rule: if price falls 10%, sell. That rule doesn't know whether the 10% drop reflects a temporary panic or a fundamental deterioration. It sells in both cases.

More sophisticated [algorithmic trading](/algorithmic-trading/) systems layer stops atop other signals—technical indicators, [volatility](/historical-volatility/) thresholds, [correlation](/diversification/) breakdowns—to avoid mechanical whipsaws. But for the individual trader, automation often means abdication. A stop is only as good as the thought behind it.

## See also

<div class="wiki-seealso">

### Closely related

- [Position Sizing](/position-sizing/) — deciding trade size before entry, complementing the exit discipline of stops
- [Market Order](/market-order/) — the execution method into which a triggered stop converts
- [Protective Put](/protective-put/) — an options-based alternative that caps losses without forced sales
- [Risk Budgeting](/risk-budgeting/) — setting and enforcing portfolio-wide loss limits that give stops context
- [Kelly Criterion](/kelly-criterion/) — a mathematical approach to sizing positions to withstand small losses
- Loss Aversion — the psychological bias that makes stop discipline hard to follow

### Wider context

- [Market Volatility](/volatility-smile/) — the price swings that can gap stops unfavourably
- [Automated Trading](/algorithmic-trading/) — the broader context for order automation
- [Hedge Fund](/hedge-fund/) — institutional use of stops within diversified strategies
- [Bid-Ask Spread](/bid-ask-spread/) — the liquidity cost affecting stop-order fills

</div>
