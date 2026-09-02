---
title: "Ratio Spread"
description: "An options strategy that buys and sells unequal numbers of options at different strikes to magnify income or reduce cost."
---

*A ratio spread uses an unequal number of long and short options at different strikes. It reduces net cost or generates higher income but creates uncapped risk if the underlying moves sharply through the short strike.*

## Structure of a ratio spread

A ratio spread might involve buying one call and selling two calls at higher strikes, or selling more options than you buy. The asymmetric structure changes the payoff profile from a typical spread.

For example, buy a $100 call for $5 and sell two $105 calls for $2 each, netting a $1 debit. If the underlying stays below $105, both short calls expire worthless and the long call is also worthless (or in-the-money, but offset by the short calls' max loss). You've "sold" more exposure than you've "bought," creating asymmetric risk.

If the stock rises to $110, the long call is worth $10, but each short call is worth $5, totaling $10. Your net is zero. Above $110, you have naked short call exposure on one of the short legs, and losses accelerate.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Ratio Spread — key facts</div>
  <table>
    <tr><th>Type</th><td>Advanced, asymmetric options strategy</td></tr>
    <tr><th>Legs</th><td>Unequal number of long and short options</td></tr>
    <tr><th>Max loss</th><td>Typically unlimited on one side</td></tr>
    <tr><th>Max profit</th><td>Capped at the short strike width</td></tr>
    <tr><th>Profit zone</th><td>Wide but asymmetric</td></tr>
    <tr><th>Typical use</th><td>Advanced income generation or cost reduction</td></tr>
  </table>
</aside>

## Why use a ratio spread

The primary appeal is reduced cost or collected premium. By selling more options than you buy, you collect more premium, dramatically lowering entry cost. If you'd normally pay $300 for a spread, a ratio spread might cost $100 or generate a $50 credit.

Professional traders use ratios in specific market conditions: when they're very confident about a direction and want to amplify income. If you're very bullish and believe the stock will rise between two strikes (say $100 to $110), selling two short calls above $110 generates income while capping risk in that zone. If the stock doesn't rise past $110, you keep the income.

## The danger of naked short exposure

The key risk is naked short call exposure. If the stock gaps above the short strikes, you have unlimited loss potential. This is why most professional traders avoid naked ratios and instead use "covered" ratios: buying stock first, then selling more calls than the stock covers (covered ratio call spread).

For example, own 200 shares at $100, buy two $105 calls, and sell four $110 calls. The long calls and owned stock provide some cover, but you're still exposed to losses if the stock crashes or gaps above $110. The ratio amplifies both gains and losses.

## Alternative: cash-secured ratios

To limit risk, some traders structure "cash-secured" ratios. Instead of leaving risk naked, they maintain enough buying power to cover the difference. If they sell two calls, they set aside enough cash to buy back both if needed. This eliminates naked risk but also ties up capital.

<div class="wiki-hatnote">For defined-risk alternatives, see <a href="/wiki/call-spread/">call spreads</a> or <a href="/wiki/butterfly-spread/">butterfly spreads</a>. For covered strategies, see <a href="/wiki/covered-call/">covered calls</a>.</div>

## Greeks and management

A ratio spread's [delta](/wiki/delta/) can swing dramatically. If you're long one call and short two calls, your net delta changes as the underlying moves. Near the short strike, gamma is high and the position can flip from profitable to deeply unprofitable quickly.

[Theta](/wiki/theta/) is typically positive (you benefit from time decay), but only in a bounded range. Outside that range, negative gamma overwhelms theta's gain.

Most professional traders don't hold ratios to expiration. They close when the position reaches either max profit or early exit points, typically at 50% of max profit. This avoids the explosive risk that emerges as expiration approaches.

## Adjustments and rolling

If the underlying moves toward the short strike faster than expected, traders often roll. Buy back the short calls and sell them at a higher strike, or buy back some short calls and sell new ones at different strikes. Rolling costs commissions and requires careful execution, but it's how professionals keep the position alive and profitable.

## When ratios go wrong

Ratios can catastrophically fail if the underlying gaps sharply. An earnings surprise can gap the stock past all short strikes in seconds, creating instantly large losses that can exceed total account equity. This is why many brokers restrict or don't allow naked ratios for retail accounts.

They also suffer from assignment risk. If one short call is assigned early (on dividend-paying stocks or near expiration), you might be forced to close the position at a loss or manage a partially closed ratio.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/call-spread/">Call spread</a> — defined-risk alternative with equal legs.</li>
  <li><a href="/wiki/butterfly-spread/">Butterfly spread</a> — another multi-leg asymmetric strategy.</li>
  <li><a href="/wiki/covered-call/">Covered call</a> — the basis for covered ratio spreads.</li>
  <li><a href="/wiki/gamma/">Gamma</a> — convexity risk of ratio spreads.</li>
  <li><a href="/wiki/theta/">Theta</a> — time decay benefit in the profit zone.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational contract.</li>
  <li>Derivatives — asset class overview.</li>
  <li><a href="/wiki/strike-price/">Strike price</a> — defines the zone of profitability.</li>
</ul>
</div>
