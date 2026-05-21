---
title: "Option Chain"
description: "A table showing all available call and put options for a stock, organized by strike price and expiration date."
---

*An option chain displays every call and put option available for a single underlying asset, arranged in rows by [strike price](/wiki/strike-price/) and grouped by [expiration date](/wiki/expiration-date/). Each row shows the bid-ask price, [implied volatility](/wiki/implied-volatility/), open interest, volume, and the Greeks ([delta](/wiki/delta/), gamma, [theta](/wiki/theta/), [vega](/wiki/vega/)). For traders, the option chain is the primary data interface—it's where all options trading begins.*

## The layout: strikes down, expirations across

The standard format is a grid. Rows are strike prices, typically listed from lowest to highest, or with at-the-money in the middle. Columns separate calls and puts, sometimes with separate tabs for different expirations. A typical chain for a $100 stock might show strikes at $90, $95, $100, $105, $110 with expirations ranging from weekly to monthly to annual. Each cell contains pricing and risk data.

## Bid-ask spreads and trading reality

The chain displays both bid (what buyers will pay) and ask (what sellers want). The width of this spread varies by strike and expiration. At-the-money options near the current expiration are tight (bid-ask spread might be $0.05); way out-of-the-money or far-dated options are much wider (spreads of $0.50 or more). Wide spreads mean worse execution and higher effective cost. Sophisticated traders often skip extreme strikes where liquidity is too thin.

## Implied volatility across strikes: the smile

Looking at the IV column across a row (same expiration, different strikes), you'll notice IV is not flat. It dips at the at-the-money strike and rises for both deeper in-the-money and deeper out-of-the-money strikes—the [volatility smile](/wiki/volatility-smile/). This shape reflects the market's hedging costs and tail-risk pricing. Understanding the smile is critical for spread pricing and arbitrage.

## Expirations and contract selection

Most options markets offer weekly, monthly (third Friday), and quarterly expirations; larger markets (SPY, QQQ, major stocks) offer multiple expirations each week. Farther-out expirations have more time value and are less sensitive to daily price moves; near-term expirations decay rapidly. Traders select expiration based on their time horizon—a 2-week earnings trade calls for a weekly contract; a 3-month hedge calls for quarterly.

## Open interest and volume

Open interest shows how many contracts are outstanding; volume shows how many changed hands today. High open interest signals liquid, tradeable options; low open interest means wide spreads and execution risk. A strike with zero open interest today might still have a quote, but that quote is theoretical—no one will trade at those prices. Professional traders focus on the strikes with decent open interest for their expiration.

## The Greeks in the chain

Most platforms show delta, gamma, theta, and vega directly in the option chain. Delta tells you directional sensitivity; theta tells you time decay; gamma tells you how delta changes. These are essential for position management and hedging. A trader constructing a [covered call](/wiki/covered-call/) might scan the chain looking for a strike with delta around 0.30 (roughly 30% probability of finishing in-the-money)—that trade-off between premium and safety.

## Building spreads from the chain

Spreads are constructed by picking multiple strikes from the chain. A [bull call spread](/wiki/bull-call-spread/) might be: buy the $100 call, sell the $105 call. The chain shows the prices of both legs, and most brokers calculate the net debit/credit and break-even on the fly. The ability to see all strikes at once makes spread construction intuitive.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/strike-price/">Strike price</a> — the row variable in the chain.</li>
<li><a href="/wiki/expiration-date/">Expiration date</a> — the column grouping in the chain.</li>
<li><a href="/wiki/implied-volatility/">Implied volatility</a> — key column showing market expectations.</li>
<li><a href="/wiki/volatility-smile/">Volatility smile</a> — the IV pattern across strikes.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/call-option/">Call option</a> — one side of the chain.</li>
<li><a href="/wiki/put-option/">Put option</a> — the other side.</li>
<li><a href="/wiki/options-greeks/">Greeks</a> — the sensitivity metrics shown in the chain.</li>
</ul>
</div>
