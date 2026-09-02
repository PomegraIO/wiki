---
title: "Debit Spread"
description: "An options strategy where you pay net premium upfront, with defined maximum profit and defined maximum loss."
---

*A debit spread is any multi-leg options position where you pay more premium than you collect, creating a net debit. Call spreads and put spreads are the most common examples, offering limited risk and limited reward.*

## What defines a debit spread

A debit spread requires a net cash outlay at entry. If you buy a $100 call for $5 and sell a $105 call for $2, you pay $3 net debit. This is a debit call spread.

The opposite is a **credit spread**, where you collect more premium than you pay. If you buy a $100 call for $2 and sell a $95 call for $5, you collect $3 net credit. This is a credit call spread, though it's less commonly used because it reverses the usual bullish/bearish directional bias.

Debit spreads define both max profit and max loss upfront. The max loss is the net debit paid. The max profit is the strike width minus the net debit. This predictability appeals to risk-conscious traders.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Debit Spread — key facts</div>
  <table>
    <tr><th>Type</th><td>Defined-risk multi-leg options strategy</td></tr>
    <tr><th>Net premium</th><td>Paid (debit) upfront</td></tr>
    <tr><th>Max loss</th><td>Net debit paid</td></tr>
    <tr><th>Max profit</th><td>Strike width minus net debit</td></tr>
    <tr><th>Common forms</th><td>Bull call spread, bear put spread, diagonal spread</td></tr>
    <tr><th>Typical use</th><td>Defined-risk directional or hedging strategies</td></tr>
  </table>
</aside>

## Bull call spread: the classic debit spread

The most common debit spread is a **bull call spread** (long lower call, short higher call). You pay to buy the upside option and collect premium from selling the capped upside. It's bullish but with capped profit.

For example: buy a $100 call for $5, sell a $110 call for $2. Net debit: $3. Max loss: $3. Max profit: $7 (the $10 spread width minus the $3 debit).

The payoff curve is linear between the two strikes. If the stock settles at $105, your calls are worth $5 and $0 respectively, netting a $5 gain ($5 long − $3 paid = $2 profit).

## Bear put spread: debit or credit depending on structure

A **bear put spread** buys a lower put (protection) and sells a higher put (income). If you pay more for the long put than you collect from the short put, it's a debit spread. If the short put premium exceeds the long put cost, it's a credit spread.

Most bear put spreads are credit spreads because the short put (closer to current price) is worth more than the long put (further out). But some structures, especially with ATM or ITM puts, create debits.

## Risk and trade-offs

Debit spreads cap both loss and profit, which appeals to conservative traders. You know exactly how much you can lose before entering.

They also require less margin than naked options. A $100 call spread requires margin only for the difference between strikes, not the full strike width.

The trade-off: profit is capped. If you're very bullish and the stock rallies 50%, your call spread caps you at $10 per share. You'd have profited much more with a naked call (but with unlimited loss risk).

## Compared to credit spreads

**Credit spreads** collect premium upfront and profit if the underlying stays within the profit zone. They have higher probability of profit but asymmetric risk (small defined loss, but repeated small losses can add up).

**Debit spreads** pay premium upfront and profit if the underlying moves favorably. They have lower probability of profit (you need the move to exceed the spread width minus debit) but symmetric payoffs.

Professionals often trade both simultaneously (a trader might be long a call spread and short a put spread on the same underlying), creating combinations that express different views.

<div class="wiki-hatnote">For the inverse structure, see <a href="/wiki/credit-spread/">credit spreads</a>.</div>

## Examples beyond calls and puts

A **bull put spread** (long lower put, short higher put) is a debit spread if you pay more for the long put than you collect from the short put. This is sometimes called a "bear put spread" when the structure is inverted.

A **diagonal spread** (long far-dated, short near-dated at different strikes) is typically a debit spread. You pay more for the longer-dated option than the near-term option credits.

## When debit spreads make sense

Debit spreads are ideal when:

1. You have directional conviction (bullish with call spreads, bearish with put spreads).
2. You want defined risk and margin efficiency.
3. Implied volatility is low (you don't want to sell options at low premium).
4. You don't mind capped profit for capped loss.

They're less ideal when implied volatility is high (you'd prefer to sell options, not buy) or when you're uncertain about direction.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/call-spread/">Call spread</a> — a bull call debit spread.</li>
  <li><a href="/wiki/put-spread/">Put spread</a> — a bear put debit spread (less common).</li>
  <li><a href="/wiki/credit-spread/">Credit spread</a> — the inverse structure.</li>
  <li><a href="/wiki/diagonal-spread/">Diagonal spread</a> — uses different strikes and expirations.</li>
  <li><a href="/wiki/implied-volatility/">Implied volatility</a> — affects the net debit paid.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational contract.</li>
  <li>Derivatives — asset class overview.</li>
  <li><a href="/wiki/strike-price/">Strike price</a> — defines the spread width.</li>
</ul>
</div>
