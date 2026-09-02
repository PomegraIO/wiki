---
title: "Trade Reporting"
description: "The requirement for exchanges and dealers to report executed trades to regulatory authorities and the public within strict timeframes."
---

*Every stock trade in the U.S. must be reported to a trade reporting system within seconds of execution. The [consolidated tape](/wiki/consolidated-tape/) aggregates these reports and broadcasts the trade price and volume to all market participants. This transparency ensures that all traders see the same prices and that regulators can monitor for manipulation.*

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Trade reporting — key facts</div>
  <table>
    <tr><th>Reported to</th><td>Trade reporting facilities (TRFs); consolidated tape</td></tr>
    <tr><th>Reporting timeframe</th><td>Generally within 2 seconds of execution</td></tr>
    <tr><th>Data included</th><td>Price, volume, time, buy/sell side, symbol</td></tr>
    <tr><th>Public access</th><td>Near real-time on quote screens; regulatory with delays</td></tr>
    <tr><th>Regulation</th><td>SEC Regulation SHO and other rules</td></tr>
  </table>
</aside>

## Why trade reporting matters

If traders could execute large trades without reporting them, the market price would become unreliable. One trader might pay $150.05 while another pays $149.95, not because of different information, but because they don't know about the other's trade. Trade reporting ensures that all traders are working from the same factual baseline.

Trade reporting also provides a trail for regulators. If a trader is suspected of [insider trading](/wiki/insider-trading-law/) or manipulating prices, the SEC can reconstruct the sequence of trades and discover when the trader bought or sold relative to others, revealing whether their timing was suspicious.

## The consolidated tape system

The [consolidated tape](/wiki/consolidated-tape/) is the central hub for U.S. equity trade reporting. Every trade on every exchange (NYSE, NASDAQ, regional exchanges) and many [over-the-counter](/wiki/over-the-counter-market/) trades must be reported to the [consolidated tape](/wiki/consolidated-tape/). The tape collects these reports and publishes them to market data vendors, brokers, and the public.

The [consolidated tape](/wiki/consolidated-tape/) operates under the auspices of the SEC. It is run by an industry consortium called SROs (self-regulatory organizations) and requires electronic message reporting from all trading venues and dealers.

## Reporting delays and real-time vs. regulatory data

Traders on exchanges see trade data in near real-time—prices and volumes update on their screens within milliseconds of execution. This is necessary for [market makers](/wiki/market-makers/) and algorithmic traders to make decisions.

Regulatory trade data—data provided to the SEC for surveillance and record-keeping—is often delayed. The SEC receives trade reports with a brief delay (typically a few hours) to allow for systematic error correction and processing. This regulatory data is what the SEC uses to investigate suspected fraud or manipulation.

## Trade reporting details

A reported trade includes:

- **Symbol:** The security identifier (e.g., AAPL for Apple).
- **Price and volume:** The price per share and the number of shares traded.
- **Time:** Recorded to the millisecond or microsecond.
- **Venue:** Which exchange or alternative trading system executed the trade.
- **Buy/sell indicator:** Direction of the initiating party.

For options, the [Options Clearing Corporation](/wiki/options-clearing-corporation/) operates a separate trade reporting system.

## Exceptions: dark pools and off-exchange trades

Trades executed in [dark pools](/wiki/dark-pools/) are still reported to the [consolidated tape](/wiki/consolidated-tape/), but with a delay. Some [dark pools](/wiki/dark-pools/) have permission to delay reporting for up to 10 seconds, allowing them to maintain some anonymity.

Over-the-counter trades (trades negotiated directly between brokers without going through an exchange) are also reported, but to a separate system called the Trade Reporting Facilities (TRF).

## Regulation SHO and delayed reporting

SEC Regulation SHO allows [dark pools](/wiki/dark-pools/) and certain other trades to be reported with a delayed modifier. If a trade is marked as "late reported," it goes to the tape with a special indicator. Traders can see that the trade occurred, but know that it may have been executed before a more recent-looking trade. This is a compromise between transparency and privacy.

## Real-time transparency issues

Full real-time transparency can create problems. If a large [dark pool](/wiki/dark-pools/) trade is reported immediately, it reveals the size of the order that just executed, and other traders can infer the likely direction of the next trade from the same institutional player. This is why the SEC allows some delays.

## Tick data and archiving

The [consolidated tape](/wiki/consolidated-tape/) publishes all trade data in real-time and archives it for historical analysis. Researchers and traders can download the entire day's trading data for any security and analyze price movements, volume, and execution quality. This archive is critical for academic research on market behavior and for post-trade compliance review.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/consolidated-tape/">Consolidated tape</a> — central repository for all trade reports.</li>
  <li><a href="/wiki/dark-pools/">Dark pools</a> — trades with delayed reporting.</li>
  <li><a href="/wiki/market-data-feed-consolidated/">Market data feed consolidated</a> — real-time distribution of trade data.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li>SEC — regulator requiring trade reporting.</li>
  <li><a href="/wiki/insider-trading-law/">Insider trading</a> — enforcement relies on trade reporting data.</li>
  <li><a href="/wiki/stock-exchange/">Stock exchange</a> — venues that report trades.</li>
</ul>
</div>
