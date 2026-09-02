---
title: "Collar"
description: "A hedging strategy that buys downside protection and sells upside call options to offset the cost, capping both loss and gain."
---

*A collar combines a long put and short call at different strikes to protect a stock position against large declines while capping upside profit. It's a zero-cost or low-cost insurance strategy widely used by executives and investors.*

## How a collar works

A collar pairs a long put (downside protection) with a short call (upside cap). Suppose you own a $100 stock. You buy a $95 put for $2 and sell a $105 call for $2, netting zero cost. Below $95, the put protects you: if the stock crashes to $80, you can exercise the put and sell at $95. Between $95 and $105, you keep the full profit. Above $105, the short call caps your gain: if the stock rallies to $110, the call is exercised and you sell at $105.

The cost is often zero or negative. You collect premium on the short call that offsets or exceeds the cost of the long put. This makes collars attractive to stock holders who want downside insurance without paying for it upfront.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Collar — key facts</div>
  <table>
    <tr><th>Type</th><td>Hedging strategy for stock positions</td></tr>
    <tr><th>Legs</th><td>Long stock + long put + short call</td></tr>
    <tr><th>Max loss</th><td>Difference between stock price and put strike</td></tr>
    <tr><th>Max gain</th><td>Difference between stock price and call strike</td></tr>
    <tr><th>Cost</th><td>Often zero or negative (call premium offsets put cost)</td></tr>
    <tr><th>Typical use</th><td>Downside protection for concentrated stock holdings</td></tr>
  </table>
</aside>

## Why executives and investors use collars

Collars are popular with company founders and executives holding concentrated stock. If you own $5 million of your company's stock, a sudden 20% decline could significantly impact your net worth. A collar lets you sleep at night: you know your downside is protected at, say, $95. The cost is capped upside gain—you won't benefit from extreme rallies—but that's often acceptable insurance.

They're also used in M&A contexts. If a shareholder is concerned about deal risk, a collar on the acquirer's stock provides downside protection. Or if a company is issuing new stock and the CEO wants to hedge, a collar on the old stock protects against sudden declines.

Collars are also used by investors with inherited stocks, founders' shares, or restricted stock. The tax treatment is favorable in many jurisdictions: entering a collar doesn't trigger a taxable event, unlike outright selling.

## Customizing the strikes for different protection levels

A collar isn't a single strategy; it's a framework. You choose how far out-of-the-money the put and call are based on risk tolerance. If you own a $100 stock:

- **Narrow collar**: Buy $99 put, sell $101 call. Maximum loss: $1, maximum gain: $1. Expensive put, cheap call (far OTM). Often you collect premium.
- **Wide collar**: Buy $90 put, sell $110 call. Maximum loss: $10, maximum gain: $10. Cheap put, cheap call. You may pay a small net debit.
- **Balanced collar**: Buy $95 put, sell $105 call. Maximum loss: $5, maximum gain: $5. Often zero-cost.

Executives often choose balanced or wide collars to preserve upside while insuring catastrophic losses.

## Unwind and tax considerations

A collar is typically held until the stock price moves close to one of the barriers. If the stock rallies and approaches the call strike, you might close the call to eliminate the cap (paying to buy it back), then keep the put as tail-risk protection. Or you might roll both positions forward to extend the collar.

In some tax regimes, collars are treated as constructive sales, triggering capital gains taxes immediately. In others, they're not. Consult a tax advisor before implementing collars on taxable accounts, especially large positions.

<div class="wiki-hatnote">For pure downside protection, see <a href="/wiki/protective-put/">protective puts</a>. For income strategies, see <a href="/wiki/covered-call/">covered calls</a>.</div>

## Compared to protective puts and covered calls

A **protective put** (own stock, buy put) provides downside insurance but is expensive. A **covered call** (own stock, sell call) generates income but has unlimited loss if the stock crashes. A **collar** combines both, providing insurance while offsetting the cost with income.

The trade-off: you cap your upside. If you're extremely bullish and believe the stock will double, a collar is not appropriate. If you're neutral to modestly bullish and want to sleep at night, a collar is ideal.

## Risk and limitations

Collars can fail if the stock gaps down overnight, below the put strike. Your put floor is based on option prices; a true catastrophic event (company bankruptcy filed pre-market) might render the put worthless before you can exercise. For true tail risk, collars should complement, not replace, other risk management.

They also require monitoring. As expiration approaches, you must decide to close, roll, or let assignment happen. If the stock is near the call strike, you risk forced sale. Some investors view this as acceptable; others find it annoying.

Liquidity can be an issue on small or illiquid stocks. Bid-ask spreads on both the put and call can widen significantly, making the zero-cost promise illusory.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/protective-put/">Protective put</a> — downside protection without upside cap.</li>
  <li><a href="/wiki/covered-call/">Covered call</a> — income generation without downside protection.</li>
  <li><a href="/wiki/put-option/">Put option</a> — the protection leg of a collar.</li>
  <li><a href="/wiki/call-option/">Call option</a> — the income-generating leg.</li>
  <li><a href="/wiki/implied-volatility/">Implied volatility</a> — determines put and call costs.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational contract.</li>
  <li>Derivatives — asset class overview.</li>
  <li><a href="/wiki/stock/">Stock</a> — the underlying asset being hedged.</li>
</ul>
</div>
