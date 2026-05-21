---
title: "Trading Halts"
description: "Temporary suspension of trading in a security, typically triggered by news announcements or regulatory concerns. Allows fair dissemination of material information."
---

*A trading halt stops all buying and selling of a security for a period, usually 15 minutes but sometimes longer. Halts are used to ensure that all investors learn of material news (a merger, earnings surprise, an investigation) at roughly the same time, before trading resumes at new valuations. Without halts, early-informed traders could profit at the expense of uninformed traders trading on stale information.*

<div class="wiki-hatnote">
For systemwide trading halts triggered by steep market declines, see <a href="/wiki/circuit-breakers/">/circuit-breakers/</a>.
</div>

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Trading halts — key facts</div>
  <table>
    <tr><th>Typical duration</th><td>15 minutes for news halts; varies for regulatory halts</td></tr>
    <tr><th>Who initiates</th><td>Company, exchange, SEC, or FINRA</td></tr>
    <tr><th>Reason</th><td>Material news, pending news, unusual price/volume activity</td></tr>
    <tr><th>Effect</th><td>All orders cancelled; trading paused; no price discovery</td></tr>
  </table>
</aside>

## News halts: when companies announce

When a company is about to announce material news—a merger, a major acquisition, earnings that vastly miss or beat expectations, or a leadership change—the company files a notification with its exchange. The exchange then halts trading before the news is released. The halt period gives news agencies and investors time to read the announcement and form valuations. When trading resumes, the repricing happens in an orderly [opening auction](/wiki/opening-auction/) rather than a chaotic scramble.

News halts typically last 15 minutes. The company can request a longer halt if there is complexity (a very large M&A deal, for instance) that requires more time to explain.

## Regulatory halts

The SEC or FINRA may halt trading in a security if they suspect fraud, if financial statements are unreliable, or if there are unanswered questions about the company's recent filings. For example, if a company's auditor resigns and the company refuses to explain why, that raises red flags. The exchange may halt trading pending a filing from the company that clears up the matter.

Regulatory halts can last longer—days or weeks—if the underlying issue is complex. A company under SEC investigation for accounting fraud may be halted for months while the investigation unfolds.

## Volatility halts

Some exchanges halt trading in a security if its price or volume spikes dramatically in a short time, without obvious news. This is an automated check to ensure the move is real, not the result of a "fat finger" typo (accidentally entering 1 million shares instead of 1,000). The exchange contacts the brokers involved and the company to confirm what happened.

Volatility halts are typically brief—5 to 15 minutes—and the exchange resumes trading once the issue is resolved.

## The impact on liquidity and valuations

While a security is halted, no new [market orders](/wiki/market-order/) can execute. [Limit orders](/wiki/limit-order/) continue to sit in the order book but do not fill. The security is effectively illiquid—you cannot sell at any price, however low you're willing to go.

When trading resumes, the [opening auction](/wiki/opening-auction/) mechanism ensures that an order is matched at a price that clears the market—the price at which the most orders can execute. This repricing, while sudden, is fair to all traders simultaneously. It avoids the scenario where an early-arriving trader buys cheaply on stale information before later traders realize the news.

## Halts and algorithmic strategies

[Algorithmic traders](/wiki/algorithmic-trading/) who rely on automated strategies must plan for halts. A strategy that buys whenever a stock dips 3% can be caught off-guard if a halt interrupts the dip and the stock gaps much higher at the [open](/wiki/opening-auction/). Professional strategies include circuit-breaker logic to pause orders during halts and wait for the resume.

## How long can a company stay halted?

There is no hard maximum. A company facing serious allegations—like Wirecard, which admitted to accounting fraud in 2020—may be halted for weeks or months. Eventually, the company either resolves the issue with a credible statement, or shareholders vote to liquidate and the company delists. Some exchanges allow a halted company to remain halted for up to 30 trading days before automatic delisting procedures begin, but rules vary by venue.

## Distinction from halts due to circuit breakers

[Circuit breakers](/wiki/circuit-breakers/) halt the entire market when the [S&P 500](/wiki/sp-500-index/) falls by 7%, 13%, or 20%. These are systemwide halts affecting all stocks. Trading halts, by contrast, affect individual securities. A stock can be halted while the rest of the market continues trading.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/circuit-breakers/">Circuit breakers</a> — systemwide trading halts on large market declines.</li>
  <li><a href="/wiki/opening-auction/">Opening auction</a> — repricing mechanism after a halt.</li>
  <li><a href="/wiki/sec/">SEC</a> — regulator that can initiate halts for investor protection.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/stock-exchange/">Stock exchange</a> — venue that enforces halts.</li>
  <li><a href="/wiki/limit-order/">Limit order</a> — orders held pending during halt.</li>
</ul>
</div>
