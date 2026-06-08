---
title: "Why a Stop-Limit Order Can Go Unfilled"
description: "Stop-limit order never filled: gaps, volatility, and illiquidity can breach the stop price but skip the limit price, leaving the order unfilled and the position unprotected."
keywords:
  - stop limit order
  - stop limit order never filled
  - gap risk stop limit
  - unfilled order trading
  - order execution risk
image: /svg/trading.svg
---

*A **stop-limit order**—which activates a limit order once a trigger price is hit—can leave you stranded. If the stock gaps past the stop price or moves too fast, the limit leg may never execute, and your position remains unprotected. This happens constantly in volatile, thinly traded, or overnight-gapping stocks.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Stop-Limit Risk — why orders go unfilled</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading and orders." />

<div class="wiki-infobox-caption">The gap between stop and limit prices is where protection fails.</div>

|   |   |
|---|---|
| **The danger** | Stop price hit, limit price never reached; order expires unfilled |
| **When it happens** | Overnight news, earnings, gaps, fast-moving rallies or selloffs |
| **Affected stocks** | Penny stocks, microcaps, low-volume equities, illiquid options |
| **The gap risk** | Stock opens below stop, but above limit, leaving a gap of no execution |
| **Better alternative** | [Stop-loss order](/protective-put/) (market order) or wider limit spread in volatile periods |
| **Core lesson** | No execution = no protection; a stop-limit can fail exactly when you need it most |

</aside>

## How Stop-Limit Orders Work

To understand when a stop-limit fails, first recall how it works.

You own 1,000 shares of XYZ at $50. You set a stop-limit order: **stop at $48, limit at $46**. You mean: "If the stock drops to $48, convert this into a limit order to sell at $46 or better."

As long as XYZ stays above $48, nothing happens. If XYZ drops to $48, the stop is **triggered**, and a limit sell order for 1,000 shares at $46 or better is sent to the market. If there are buyers at $46 or higher, the order fills. If the stock drops below $46 before any offer lands at $46, your limit order sits at $46 waiting for a buyer to come in at that price.

This works smoothly in liquid, slow-moving stocks. XYZ drifts from $50 to $49 to $48; the limit order activates, and because the stock is still in the $47–$48 range, a buyer shows up at $46 and the order fills.

## The Gap: Stop Triggered, Limit Skipped

The failure mode emerges when the stock **gaps**—moves in a discontinuous jump—or **gaps through** your limit price.

**Overnight gap scenario:**
- You own XYZ, currently $50.
- Stop-limit: stop $48, limit $46.
- At market close, XYZ is at $49.50.
- Overnight, the company announces disappointing earnings.
- The market opens at $45 (a $4.50 gap down).

What happens? The stop at $48 is triggered overnight during the gap. A limit order to sell at $46 is now active. But the opening price is $45—below your limit. Your order may fill, but at a worse price than the $46 limit, or it may sit unfilled as the stock bounces off the opening low.

In the worst case, the stock rallies to $46.50 the moment it opens, your limit order at $46 remains unfilled (there are no sellers below $46.50), and by the time you realize the order didn't execute, the stock is back above $48. Your stop-limit has expired or been canceled, and you are unprotected, owning the stock at a loss.

## The Illiquid Stock Problem

Stop-limits fail more frequently in illiquid and thinly traded stocks.

Consider a microcap or penny stock where daily volume is 50,000 shares. You own 5,000 shares and set a stop-limit: stop $5, limit $4.80. The stock drops to $5.00, activating the limit order. But there are few buyers at $4.80, and your 5,000-share order is large relative to the typical daily volume. Your order sits, unfilled, for minutes or hours. By then, the stock may have bounced or continued down.

In stocks with wider bid-ask spreads, the limit price itself becomes a moving target. If the bid is $4.70 and the ask is $5.10, a limit order at $4.80 (between them) will never fill—there are no sellers at $4.80; all sellers are asking $5.10 or above.

## Fast-Moving Rallies and Selloffs

Stop-limits fail not only on gaps but also on sustained, fast moves.

A stock rallies from $50 to $52 in two minutes on sector momentum. Your buy stop-limit was set to trigger at $51 with a limit of $51.50. The stock gaps through $51 in a single tick; the stop activates, but the order to buy at $51.50 is already behind the price (the stock is now at $52), and no one is selling at $51.50. The order never fills, and you miss the entry you intended.

This is especially common in options, where a move of 5–10% can happen in seconds if volatility spikes or the underlying stock makes a surprise announcement.

## The Distinction: Stop Order vs Stop-Limit

This is why many investors distinguish between a **stop order** (or stop-loss) and a **stop-limit order**.

A **stop order** (market order triggered at a price) is executed *at the market price* once the stop is hit. You will definitely exit if the stop is triggered—but the price may be much worse than you wanted.

A **stop-limit order** guarantees a maximum loss (the limit price) but offers *no guarantee of execution*. If the limit is skipped, you have no sale, no exit, and the position remains open.

For protection against catastrophic losses, a simple stop market order is often safer than a stop-limit. You sacrifice price certainty to guarantee execution.

## When Stop-Limits Make Sense

Stop-limits are most reliable in four scenarios:

1. **Highly liquid stocks** with tight spreads and high daily volume (e.g., [S&P 500](/sp-500-index/) components, major exchange-listed securities). The stop-to-limit distance can be small, and there are always counterparties.

2. **Non-volatile periods**. During slow, steady markets, the chance of a gap past your limit is low. Stop-limits work better in calm trading environments.

3. **When you can afford to be unfilled**. If you're trying to trim a position but don't need to exit immediately, a stop-limit is acceptable. If you miss the order, you try again later.

4. **Wide stop-to-limit spreads** when you're willing to accept a lower exit price. If you set stop $48, limit $44 (a $4 gap), you're much more likely to fill than with a $0.50 spread. But then you've accepted a worse price.

## The Real-World Cost

Every major broker has seen stop-limit orders expire unfilled during earnings seasons, market rallies, Fed announcements, or thinly traded securities. The psychological cost is high: you believed you were protected, only to discover the protection never activated.

Experienced traders and risk-conscious investors often use stop-market orders (accepting price uncertainty) in volatile stocks, or they use [protective puts](/protective-put/) in options markets, where execution is guaranteed and the price floor is defined upfront.

## See also

<div class="wiki-seealso">

### Closely related

- [Limit Order](/limit-order/) — orders that execute only at a specified price or better
- [Market Order](/market-order/) — orders that execute immediately at the best available price
- [Protective Put](/protective-put/) — buying a put option to guarantee a minimum sale price
- [Bid-Ask Spread](/bid-ask-spread/) — the gap between buy and sell prices in the market
- [Market Maker Trading](/market-maker-trading/) — how liquidity is provided and prices are stabilized

### Wider context

- [Execution Risk](/execution-risk/) — the risk that an order may not fill as intended
- [Volatility Smile](/volatility-smile/) — how implied volatility varies by strike, affecting options pricing
- [Time Value](/time-value/) — the premium paid for time remaining in an option or order
- [Stock Exchange](/stock-exchange/) — where orders are matched and executed

</div>