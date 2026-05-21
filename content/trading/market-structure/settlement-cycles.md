---
title: "Settlement Cycles"
description: "The timeframe between a trade's execution and the actual transfer of cash and securities, which determines when a trader can use their money."
---

*When you buy a stock, the trade executes instantly, but the cash and securities don't actually change hands for two business days. This period—called T+2 (for trade date plus two days)—gives both buyer and seller time to verify the trade and arrange for the transfer. Shortening settlement cycles reduces counterparty risk and frees up capital, but it requires more sophisticated infrastructure.*

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Settlement cycles — key facts</div>
  <table>
    <tr><th>Current standard for U.S. stocks</th><td>T+2 (two business days)</td></tr>
    <tr><th>Process</th><td>Trade, clearing, settlement</td></tr>
    <tr><th>Where it happens</th><td>DTCC (Depository Trust & Clearing Corporation)</td></tr>
    <tr><th>Risk reduced</th><td>Counterparty risk, operational risk</td></tr>
    <tr><th>Pressure</th><td>Move to T+1 or T+0 for faster capital turnover</td></tr>
  </table>
</aside>

## The three phases: trade, clearing, settlement

When you buy 100 shares of Apple for $15,000, three things must happen.

**Trade** (T+0): You and the seller agree on a price and quantity. The trade is executed on the exchange and reported to the [consolidated tape](/wiki/consolidated-tape/). From the exchange's perspective, the trade is complete.

**Clearing** (T+1): The two sides' brokers confirm the details—price, quantity, settlement instructions (where the cash and shares should go). A clearinghouse (like the [Options Clearing Corporation](/wiki/options-clearing-corporation/) for derivatives) steps in as the counterparty to both buyer and seller. The clearinghouse guarantees the trade will settle even if one party defaults.

**Settlement** (T+2): The actual transfer of cash and securities occurs. The seller's broker moves the shares to the buyer's account (via the [Depository Trust Company](/wiki/depository-trust-company/), the central securities depository). The buyer's broker wires the $15,000 to the seller's broker. The trade is complete.

## Why T+2 exists

Before T+2, settlement could take weeks or months. A buyer might receive shares in one envelope and the seller's receipt in another, with no way to verify that the transaction was complete. This created counterparty risk: the seller delivered shares but never received payment, or vice versa.

T+2 is a compromise. Two business days is long enough to allow both brokers to verify the trade in their back-office systems, confirm the settlement instructions, and arrange wire transfers and physical (or electronic) security delivery. It is short enough to limit the period of uncertainty.

The two-day window excludes weekends and holidays. A trade executed on a Friday settles on the following Tuesday.

## Fails to deliver and settlement risk

Not all trades settle on time. A seller might temporarily run short on shares—they own the shares but they have been lent out as part of a [short sale](/wiki/short-selling/) or to another party. The seller must "buy in" the borrowed shares (repurchase them) before settlement. If this fails, the buyer does not receive their shares on T+2.

The SEC tracks "fails to deliver" as a measure of market health. Chronic failures indicate that a stock is trading more volume than exists (or is available), a sign of manipulation or settlement-system stress.

## T+1 and the push for faster settlement

The industry has been discussing moves to T+1 (one-day settlement) for decades. T+1 would reduce the period of counterparty risk and free up capital that is currently locked up during settlement. For high-frequency traders and institutional investors, faster settlement means lower capital requirements and faster profit realization.

However, T+1 is operationally harder. It requires faster back-office processing, faster credit checks, and faster wire transfers. Some brokers are not equipped to handle it. The SEC has mandated a move to T+1 for U.S. equities, effective in the mid-2020s.

## Settlement in other markets

Not all markets use T+2. Futures contracts settle daily (often called T+0 or "daily settlement") through a process called "mark-to-market." Forex trades settle on T+2 for major currencies. Cryptocurrencies often settle T+0 because the blockchain provides instant final settlement.

## The depository system

Settlement in the U.S. ultimately flows through the [Depository Trust Company](/wiki/depository-trust-company/) (DTC), which holds the shares electronically. Brokers do not physically move stock certificates. Instead, DTC's computers debit shares from the seller's account and credit them to the buyer's account. Wire transfers move cash between broker banks.

## Fails and short squeezes

When a security is in short supply and fails to deliver are common, the security can experience a "short squeeze." Buyers who expected to receive shares on T+2 but don't have to search for shares elsewhere, bidding up the price. The harder-to-find shares are, the higher the short-squeeze price can go. This happened with GameStop and AMC in 2021 when retail traders realized that short sellers could not cover their positions on time.

## Settlement cost and fees

Each settlement involves fees paid to the clearinghouse, the depositories, and the brokers. These fees are typically a small fraction of the trade value (a basis point or two), but for high-volume traders, they add up. Faster settlement (T+1) would reduce some of these costs by freeing up capital, but it would increase others (faster processing, more robust systems).

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/depository-trust-company/">Depository Trust Company</a> — clearinghouse for U.S. equity settlement.</li>
  <li><a href="/wiki/clearing-firm/">Clearing firm</a> — broker responsible for settlement.</li>
  <li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — mitigated by faster settlement.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/short-selling/">Short selling</a> — can fail to deliver in tight settlement.</li>
  <li><a href="/wiki/futures-contract/">Futures contract</a> — use daily settlement.</li>
  <li><a href="/wiki/broker/">Broker</a> — responsible for executing settlement instructions.</li>
</ul>
</div>
