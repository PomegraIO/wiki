---
title: "Put Spread"
description: "A bearish options strategy that buys one put and sells another put at a lower strike to reduce cost."
---

*A put spread is a multi-leg options strategy where you buy one put option and sell another put on the same underlying and expiration but at a lower strike price. Like a call spread, it defines risk and profit in advance, but expresses a bearish view.*

## The structure of a put spread

A put spread pairs a long put at a higher strike with a short put at a lower strike. You pay a net debit: the cost of the long put minus the credit from the short put. If you sell the short put for more premium than you pay for the long put, it becomes a credit spread, and the collected premium is your profit if the underlying stays above the long put's strike.

The strategy caps your maximum loss at the difference between the two strikes minus any net credit received. Your maximum profit is the net premium collected (if it's a credit spread) or the strike width minus the net debit (if it's a debit spread).

Most traders structure put spreads as credit spreads: selling a slightly out-of-the-money put and buying protection further out-of-the-money. This makes the trade a net income generator if the underlying holds above the short strike.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Put Spread — key facts</div>
  <table>
    <tr><th>Type</th><td>Multi-leg options strategy</td></tr>
    <tr><th>Legs</th><td>Long put + short put (same expiration, different strikes)</td></tr>
    <tr><th>Max loss</th><td>Strike width minus net credit (or net debit if debit spread)</td></tr>
    <tr><th>Max profit</th><td>Net credit collected</td></tr>
    <tr><th>Market bias</th><td>Bearish to neutral</td></tr>
    <tr><th>Typical use</th><td>Income generation or defined-risk downside bet</td></tr>
  </table>
</aside>

## When put spreads are used

Put spreads appeal to traders who expect moderate downside or no decline, but want defined risk. If you sold a naked put, your loss would be unlimited below the strike (in theory, if the underlying went to zero). A put spread caps that loss because the long put establishes a floor: once both puts are in-the-money, the short put's loss is offset by the long put's gain.

Credit put spreads are popular on liquid indexes like the [S&P 500](/wiki/sp-500-index/). Traders sell a 1–5% out-of-the-money put and buy protection 5–10% below, collecting net premium with limited downside. If the index stays stable or climbs, the trade profits. If it falls moderately, the loss is capped.

## Mechanics of profit and loss

Imagine the stock trades at $100. You buy a $95 put for $2 and sell a $90 put for $4, collecting a $2 net credit. Your maximum profit is $2 (if the stock stays above $95). Your maximum loss is $3 (the $5 strike width minus the $2 credit).

If the stock drops to $92 at expiration, the $95 put is worth $3 and the $90 put is worth $2. Your net gain is $1 ($3 long gain minus $2 you collected, minus $2 you originally received, netting to $1). If it falls further to $85, both puts are in-the-money: the $95 put is worth $10, the $90 put is worth $5, and your net loss is $3, the maximum.

<div class="wiki-hatnote">For strategies that hedge downside without capping gain, see <a href="/wiki/protective-put/">protective puts</a> or <a href="/wiki/collar/">collars</a>.</div>

## Implied volatility's impact

Put spreads benefit from high implied volatility at entry: elevated premiums mean you collect more credit. As volatility collapses toward expiration, both puts decline in value, and your profit expands. This is the opposite of a long option position, where you lose money as implied volatility falls.

If volatility is already low and you structure a credit put spread, you collect minimal premium. The trade's profit-to-risk ratio becomes unfavorable, and most professionals skip it.

## Adjustments and early exits

If the underlying falls sharply and approaches the short strike before expiration, the position is at risk. Many traders close the trade early rather than holding to the maximum loss. Others roll down: buy back the $90 put, sell a new $85 put further out, and extend expiration. Rolling costs commissions on four sides, so it only makes sense on higher-premium trades.

The inverse strategy, a [call spread](/wiki/call-spread/), uses the same structure but is bullish. A naked short put without the long put protection is riskier but more profitable if the underlying stays high.

## When put spreads go wrong

If implied volatility collapses after you open the trade, the premium of both puts shrinks, but the long put shrinks more in percentage terms (it was farther out-of-the-money). You can face losses even if the underlying stays above the short strike. Additionally, if the underlying gaps down sharply at earnings or a major event, both puts move in-the-money quickly, and you might be forced to close early at a significant loss.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/call-spread/">Call spread</a> — the bullish counterpart.</li>
  <li><a href="/wiki/put-option/">Put option</a> — the long leg of a put spread.</li>
  <li><a href="/wiki/iron-condor/">Iron condor</a> — combines put and call spreads for neutral outlook.</li>
  <li><a href="/wiki/implied-volatility/">Implied volatility</a> — shapes the premium you collect.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational derivatives contract.</li>
  <li><a href="/wiki/derivatives/">Derivatives</a> — asset category overview.</li>
  <li><a href="/wiki/strike-price/">Strike price</a> — defines where the strategy breaks even.</li>
</ul>
</div>
