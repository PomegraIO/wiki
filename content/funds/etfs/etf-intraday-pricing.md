---
title: "ETF Intraday Pricing"
description: "How ETFs are priced and traded throughout the day, unlike mutual funds which price once daily at market close."
---

*ETFs trade on stock exchanges during market hours and reprice continuously, just like stocks. You can buy or sell at any moment the market is open, at whatever price the [market](/wiki/stock-market/) is willing to pay. This is the fundamental difference from traditional mutual funds, which price once per day at 4 p.m. ET and execute all trades at that single closing price.*

## The mutual fund pricing model

Mutual funds calculate their [net asset value](/wiki/intrinsic-value/) (NAV) once per day, typically at the end of the trading day. If you submit an order to buy or sell between 9:30 a.m. and 4 p.m., your transaction doesn't execute until 4 p.m. ET—you have no idea what price you'll get. The fund manager values every holding in the portfolio at that moment, sums the total, divides by shares outstanding, and that's your price. It's efficient for the fund because it centralizes settlement, but it's opaque for the investor. You can't see what you're paying in real time.

## How ETF continuous pricing works

An ETF, by contrast, has two prices at any moment the exchange is open: the [market price](/wiki/market-order/) and the underlying [NAV](/wiki/intrinsic-value/). The market price is what you actually pay—the bid and ask quotes from market makers and other traders. The underlying NAV is the theoretical value of the ETF's portfolio, updated continuously throughout the day as the constituent stocks move.

These two prices are usually very close, within a few cents. But the mechanism that keeps them aligned is the authorized participant. If the market price trades a few pennies above NAV, an authorized participant will buy shares at the market price, exchange them for the underlying stocks (via the [creation-redemption mechanism](/wiki/etf-creation-redemption/)), and sell those stocks for more than they paid. This [arbitrage](/wiki/etf-arbitrage/) opportunity forces the market price back down toward NAV.

The same process works in reverse. If the market price falls below NAV, an arbitrageur buys the underlying stocks, exchanges them for ETF shares, and sells those shares at the market price for a profit. Again, this closes the gap. As long as authorized participants are actively watching the [bid-ask spread](/wiki/etf-bid-ask-spread/), the market price stays tightly anchored to NAV.

## Timing advantages and disadvantages

Intraday pricing is an advantage if you need to trade during the day. Suppose the Fed makes an announcement at 2 p.m. that the market hates. You can sell your [equity ETF](/wiki/equity-etf/) immediately at the new lower price. With a mutual fund, you're stuck—you can place an order, but it won't execute until 4 p.m., at which point the price might have moved further.

Conversely, intraday pricing is a disadvantage if you execute a market order without thinking. A beginner might panic-sell an [S&P 500 ETF](/wiki/sp-500-index/) during a 3% intraday drop, missing a recovery that afternoon. With a mutual fund, the order sits until 4 p.m., buying you a few hours to change your mind (or forcing you to wait, depending on your perspective).

The practical reality is that for most buy-and-hold investors, the daily pricing of mutual funds is irrelevant. You're not trading intraday. But for tactical traders, market makers, and [day traders](/wiki/day-trading/), the continuous pricing of ETFs is essential.

## Tracking the underlying NAV

Throughout the trading day, the ETF's underlying NAV is published to the market, typically every 15 seconds. This is the fair value of the ETF if you were to liquidate the full portfolio at current prices. Market makers use this published NAV to calculate bid-ask quotes; if the NAV is $50.30 and the spread is 1 cent, the bid might be $50.29 and the ask might be $50.31.

In liquid, large-cap [sector ETFs](/wiki/sector-etf/) or broad [index funds](/wiki/index-fund/), this intraday NAV is very accurate. The stocks in the fund are actively traded, the published quotes are tight, and the arbitrage mechanism is fast. In less liquid funds—say, a [commodity ETF](/wiki/commodity-etf/) holding thinly traded metals or a [thematic ETF](/wiki/thematic-etf/) holding niche growth stocks—the NAV can lag real-time prices. The underlying stocks may not have fresh quotes at that exact second, so the fund's computed NAV is stale. This is where [tracking error](/wiki/etf-tracking-error/) emerges.

## The role of [liquidity](/wiki/liquidity-risk/) and market hours

ETF pricing is only continuous during the hours the exchange is open. In the U.S., that's 9:30 a.m. to 4 p.m. ET. After-hours quotes do exist—brokers and market makers show bids and asks during [pre-market](/wiki/pre-market-trading/) and [after-hours](/wiki/after-hours-trading/) sessions—but the NAV isn't updated, so those prices are less reliable. Buying an ETF at 6 p.m. means you're transacting with a market maker at whatever spread they're willing to quote, with no arbitrage mechanism to enforce fair value.

For [commodity ETFs](/wiki/commodity-etf/) or [international ETFs](/wiki/international-etf/), the situation is more complex. The underlying assets may trade on non-US exchanges and around the clock. A [bond ETF](/wiki/bond-etf/) might hold Treasuries that trade actively in overnight markets. In these cases, the ETF's NAV updates all day, but the published NAV lags by 10–30 seconds; the market price may diverge further if local market hours and US exchange hours don't overlap. This is why global ETFs can trade at larger discounts or premiums to NAV than US domestic funds.

## Real-time arbitrage and market efficiency

The beauty of continuous intraday pricing is that it creates a continuous arbitrage opportunity. If the ETF price drifts away from its underlying NAV, a sophisticated trader can exploit that gap in seconds. This keeps ETF pricing honest and efficient in a way mutual fund pricing cannot. It also means that [ETF premiums and discounts](/wiki/etf-premium-discount/) exist but rarely exceed 0.1% in liquid funds—the arbitrage trade would be profitable and would snap them back.

This same mechanism is why [inverse ETFs](/wiki/inverse-etf/) and [leveraged ETFs](/wiki/leveraged-etf/) can offer short or multiplied exposure to indices: the intraday pricing and arbitrage mechanism allows them to reset daily without drifting wildly away from their stated multiplier.

## Implications for end-of-day trades

If you place a market order to buy an ETF at 3:55 p.m., you may or may not get filled at 3:55 p.m. prices. If the order reaches a broker after 4 p.m., it might be held for the next trading day. If you use a limit order instead—specifying a price you're willing to pay—the order sits on the order book and executes only if the market reaches that price. This intraday mechanism requires more active management than mutual funds and carries more tail risk for passive investors who aren't paying attention to order types.

For long-term ETF holders, this complexity is easily avoided by using simple limit orders at reasonable prices or by buying in after-hours windows when you know the direction of the market. For day traders and high-frequency investors, it's the defining advantage of the ETF structure.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/etf/">ETF</a> — the broader definition and comparison to mutual funds.</li>
<li><a href="/wiki/etf-bid-ask-spread/">ETF Bid-Ask Spread</a> — the cost of intraday trading.</li>
<li><a href="/wiki/net-asset-value/">Net Asset Value</a> — the underlying valuation that anchors pricing.</li>
<li><a href="/wiki/etf-arbitrage/">ETF Arbitrage</a> — the mechanism enforcing price efficiency.</li>
<li><a href="/wiki/market-order/">Market Order</a> — the order type used for intraday ETF trades.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/mutual-fund/">Mutual Fund</a> — the daily-pricing alternative.</li>
<li><a href="/wiki/stock-market/">Stock Market</a> — the venue where ETF prices form.</li>
<li><a href="/wiki/day-trading/">Day Trading</a> — an application of intraday pricing.</li>
</ul>
</div>
