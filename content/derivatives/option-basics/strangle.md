---
title: "Strangle"
description: "An option strategy combining out-of-the-money call and put options at different strikes, betting on large price moves at lower upfront cost than a straddle."
---

*A strangle pairs an out-of-the-money [call option](/wiki/call-option/) with an out-of-the-money [put option](/wiki/put-option/) at different strikes. Like a [straddle](/wiki/straddle/), it's a volatility bet that profits from large moves in either direction. The advantage is lower cost—both legs start out-of-the-money—but the disadvantage is that you need a larger move to break even.*

## Cost advantage and breakeven trade-off

A long straddle might cost $8 ($4 call + $4 put) at an at-the-money strike. A long strangle might cost $4 ($2 call + $2 put) by moving both strikes away from current price. You've halved the cost, but now the stock must move further to hit the [strike prices](/wiki/strike-price/) and generate profit. If a straddle breaks even at a 8% move, the strangle might need a 12% move. This cost-saving appeal makes strangles popular among options traders working with smaller accounts or expecting less dramatic moves.

## Why short strangles are more common than long

Selling strangles is arguably more intuitive than buying them. You collect premium from both legs, betting that volatility will be subdued and the stock will stay between the two strikes until expiration. A stock at $100 with a sold $95 put and $105 call gives you a $10 profit zone. If the stock finishes anywhere between $95 and $105, you keep all the premium. Max profit is the combined premium; max loss is theoretically unlimited in the call direction and substantial in the put direction (unless the put is on a stock that can't go to zero). This is why short strangles are a staple of income traders.

## Timing and event-driven strangles

Long strangles are often constructed around events with known high-volatility potential—earnings announcements, FDA approvals, merger arbitrage deals. The seller believes the market is underpricing the move. A trader might buy a strangle before earnings, expecting the stock to gap sharply, and exit for a profit immediately after the announcement. The compressed time-to-event means less theta decay to fight through.

## Comparing strangles and straddles

Both are volatility strategies, but strangles require larger moves and cost less; straddles are more expensive but break even sooner. In high-volatility markets, [implied volatility](/wiki/implied-volatility/) premiums are fat and strangles become cheaper relative to straddles. In calm markets, strangles are extremely cheap because out-of-the-money premiums collapse. The choice depends on: (1) how much you expect to move, (2) your capital, and (3) your edge on volatility.

## Greeks and position management

A long strangle's [delta](/wiki/delta/) is close to zero initially because it's out-of-the-money on both sides. [Gamma](/wiki/gamma/) is positive: as the stock moves toward and past the strikes, gamma accelerates your profits. [Theta](/wiki/theta/) is negative: time decay erodes both legs daily, especially as expiration nears. Long strangle holders are fighting a clock and need the stock to move before time becomes too costly. This is why many traders close strangles early, even if profitable, rather than sweating the final week.

## Wide strangles vs. tight strangles

You can choose how far apart the strikes are. A wide strangle ($95/$105 on a $100 stock) costs very little but requires a huge move to profit. A tight strangle ($99/$101) costs more but is more likely to profit from normal volatility. There's no best choice; it depends on where you think volatility lies relative to [implied volatility](/wiki/implied-volatility/).

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/straddle/">Straddle</a> — same strikes for both call and put.</li>
<li><a href="/wiki/call-option/">Call option</a> — the upper leg of the strangle.</li>
<li><a href="/wiki/put-option/">Put option</a> — the lower leg of the strangle.</li>
<li><a href="/wiki/out-of-the-money/">Out-of-the-money</a> — where strangle strikes typically sit.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/implied-volatility/">Implied volatility</a> — the bet you're making against the market.</li>
<li><a href="/wiki/gamma/">Gamma</a> — accelerates profits on large moves.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay working against the buyer.</li>
</ul>
</div>
