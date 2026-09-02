---
title: "Market Surveillance"
description: "Continuous monitoring of trading activity to detect fraud, manipulation, and violations of trading rules."
---

*Every trade on an exchange is analyzed by algorithms looking for suspicious patterns. Did someone buy a huge quantity just before an announcement? Did a trader execute a rapid sequence of trades to create the illusion of volume? Market surveillance systems catch these patterns and alert regulators, who investigate and can bring enforcement actions.*

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Market surveillance — key facts</div>
  <table>
    <tr><th>Monitors</th><td>Exchanges, SEC, FINRA, CFTC</td></tr>
    <tr><th>What's tracked</th><td>Price, volume, timing, order sequences, insider relationships</td></tr>
    <tr><th>Red flags</th><td>Unusual volume, layering, spoofing, pump-and-dump, front-running</td></tr>
    <tr><th>Tools</th><td>Algorithms, pattern matching, statistical anomaly detection</td></tr>
    <tr><th>Action</th><td>Halt, fine, ban from trading, criminal referral</td></tr>
  </table>
</aside>

## What market surveillance detects

Modern surveillance systems analyze every trade in real-time or near-real-time. They are looking for:

**Suspicious timing:** Did a trader buy or sell immediately before a major announcement? This could indicate [insider trading](/wiki/insider-trading-law/).

**Unusual volume:** A stock that typically trades 100,000 shares a day suddenly trades 10 million. This could indicate manipulation, a leak, or a major news event.

**Layering:** A trader submits multiple large orders on one side of the book, creating the appearance of demand, then cancels them without executing. The goal is to trick other traders into thinking there is strong buying interest.

**Spoofing:** A trader submits orders in one direction (say, buying) with no intent to execute, only to cancel them after the price moves in their desired direction (up), then they profit by selling the shares they actually wanted to dispose of.

**Pump-and-dump:** A trader buys a lightly-followed stock, then aggressively buys it to push the price up, publicizes the stock to other retail traders to generate buying pressure, and then dumps their shares at the inflated price.

## Who does market surveillance

**Exchanges:** The NYSE, NASDAQ, and other trading venues employ dedicated surveillance teams. They monitor for violations of exchange rules, such as trading halts or quote obligations for [market makers](/wiki/market-makers/).

**SEC:** The Securities and Exchange Commission oversees markets and can investigate suspected violations of securities laws, including [insider trading](/wiki/insider-trading-law/) and market manipulation.

**FINRA:** The Financial Industry Regulatory Authority oversees [brokers](/wiki/broker/) and enforces rules among its members. FINRA has detailed surveillance rules (notably Rule 5210) that members must implement.

**CFTC:** The Commodity Futures Trading Commission oversees [futures markets](/wiki/futures-contract/) and [derivatives](/wiki/option/) trading. It has specific rules against manipulation and has brought major enforcement actions against high-frequency traders and spoofing.

## Surveillance technology

Surveillance systems ingest trade data in real-time from the [consolidated tape](/wiki/consolidated-tape/) and exchange order books. They use statistical models and machine learning to identify anomalies:

**Volume analysis:** If volume is more than 5 standard deviations above the 30-day moving average, flag it.

**Timing analysis:** If a trade occurs within minutes of a scheduled announcement or earnings release, and the trade is on the correct side of the news, flag it.

**Order book analysis:** Detect patterns like layering (large orders that cancel immediately) or spoofing (orders far away from the market that are never intended to execute).

**Network analysis:** Track relationships between traders, brokers, and insiders to identify whether a trader might have access to material non-public information.

## Limitations and false positives

Surveillance systems are powerful but imperfect. They generate false positives: legitimate trading activity that looks suspicious. A [market maker](/wiki/market-makers/) might submit and cancel orders hundreds of times a day as part of normal quoting. An investor might buy shares the day before an announcement because they are rebalancing their portfolio, not because they have inside information.

Investigators must review flagged activity manually to separate legitimate trading from fraud. This manual review is expensive, which is why the SEC and exchanges focus on the most egregious cases.

## Enforcement outcomes

When market surveillance detects a serious violation, regulators can:

**Issue a citation or fine:** The first step for minor violations like failing to report a trade correctly.

**Suspend or revoke trading privileges:** Prevent the trader or broker from accessing the market for a period (ranging from days to permanently).

**Disgorgement:** Force the violator to return profits made from illegal trading. If a trader made $500,000 from insider trading, they must return it.

**Criminal referral:** For serious crimes like insider trading or large-scale fraud, the SEC can refer the case to the U.S. Department of Justice, which can prosecute and seek prison time.

## The challenge of high-frequency trading

Surveillance of [high-frequency traders](/wiki/high-frequency-trading/) (HFT) is particularly challenging. HFT firms execute thousands of orders per second, making it hard for surveillance systems to distinguish legitimate market-making from manipulation. The CFTC brought a major case against a HFT trader for spoofing in 2015 (after the "flash crash" incident), winning a multimillion-dollar settlement.

## Transparency and data access

Regulators have broad authority to demand trading data from brokers and exchanges. The SEC maintains a Central Repository of submissions from brokers, including suspicious activity reports. Law enforcement agencies can issue subpoenas to access specific trader records.

However, oversight has limits. Some trades occur in [dark pools](/wiki/dark-pools/) where transparency is reduced, making surveillance harder. And the sheer volume of trading data means that some violations slip through.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/insider-trading-law/">Insider trading law</a> — most common violation detected by surveillance.</li>
  <li>SEC — primary regulator conducting surveillance.</li>
  <li><a href="/wiki/finra/">FINRA</a> — broker regulator with surveillance requirements.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/stock-exchange/">Stock exchange</a> — venue being surveilled.</li>
  <li><a href="/wiki/high-frequency-trading/">High-frequency trading</a> — modern challenge for surveillance.</li>
  <li><a href="/wiki/consolidated-tape/">Consolidated tape</a> — data source for surveillance.</li>
</ul>
</div>
