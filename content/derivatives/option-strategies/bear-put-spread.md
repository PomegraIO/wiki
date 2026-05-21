---
title: "Bear Put Spread"
description: "A debit strategy using short and long puts at different strikes, used to bet on a stock declining or staying flat with defined maximum loss."
---

*A bear put spread shorts a [put option](/wiki/put-option/) and buys a lower-strike put for protection, paying a net debit upfront. It profits as the stock falls or stays above the short put through expiration, capping loss at the strike difference minus the debit paid.*

## What a bear put spread is

A bear put spread sells a put at one strike and simultaneously buys a put at a lower strike, both expiring in the same period. You pay a net debit (the spread's cost at entry). If the stock falls below the short put's strike at expiration, both puts have value; the long put limits how much you lose. If the stock stays above the short put, both puts expire worthless and you lose the full debit paid.

The strategy is directionally bearish—you profit from the stock declining—but the long put provides a floor for losses.

## Why to use a bear put spread

The primary reason is **defined-risk bearish exposure**. If you're pessimistic about a stock but unwilling to sell it naked short (which has theoretically unlimited loss), a bear put spread offers directional leverage with a hard stop-loss built in.

A second reason is **cost reduction in high-IV environments**. When puts are expensive (high implied volatility), you offset your short put's debit by selling a long put. The cost shrinks; the risk definition remains.

Bear put spreads also suit **portfolio hedging**. If you own stock and want downside protection while lowering the cost of that protection, buying a put is expensive; selling a lower-strike put against it partially funds the hedge.

## When a bear put spread wins

This strategy excels when **implied volatility is elevated**. Fat option premiums mean both the short and long puts are expensive, widening the spread's debit. More cushion means better profit potential.

Bear put spreads also win in **crashing markets**. If the stock falls sharply, both puts gain value, but the short put (closer to the money) accelerates upward faster. Your debit paid shrinks quickly, locking in profits early.

The strategy is ideal when you're **confident in downside but cautious on magnitude**. You don't need the stock to crater—just decline past your short strike. That modest bar makes spreads more attainable than directional bets.

## When a bear put spread loses money

If the stock rallies above the short put's strike, both puts expire worthless. You've lost the full debit paid—your maximum loss is realized immediately.

Bear put spreads also suffer in **collapsing implied volatility**. If IV drops sharply (especially on good news when the stock rallies), the premiums you sold deflate. The short put's credit shrinks, widening your net debit. Early closure becomes expensive; you're forced to realize a loss or hold the full position.

Time decay works against you until the stock falls. Early in the spread's life, theta decay is minimal on the long put (far OTM) and modest on the short put. You're paying time decay without getting paid for it until the stock moves.

## Mechanics and adjustment

You pay a debit at entry—typically $100–$400 per spread. Maximum profit is the debit paid (if both puts expire worthless, you lose nothing net). Maximum loss is `(difference between strikes) – (debit paid)`. Return on risk is `debit / max loss`, often 25–50%.

**Adjustment** happens if the stock rallies toward your short strike instead of falling. Common moves:
- **Rolling down and out**: Buy back the short put at a loss, sell a lower-strike put for a later month. Resets the profit window downward.
- **Closing and pivoting**: Exit the spread at a loss and redeploy into a new bearish setup elsewhere, cut your losses, and move on.

Unlike credit strategies, bear put spreads don't always benefit from rolling. If you're wrong about direction, rolling often locks you deeper into a losing position.

## Bear put spread vs. outright short put sale

An outright short put collects the same premium but with theoretically unlimited loss if the stock crashes. A bear put spread pays to remove that tail risk—the long put caps loss. Choose outright shorts when you're deeply confident and can absorb a worst-case loss; choose spreads when you want leverage with guard rails.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/bull-put-spread/">Bull Put Spread</a> — bullish analog using two puts.</li>
<li><a href="/wiki/put-option/">Put Option</a> — the short leg of a bear put spread.</li>
<li><a href="/wiki/bear-call-spread/">Bear Call Spread</a> — bearish strategy using calls.</li>
<li><a href="/wiki/short-selling/">Short Selling</a> — alternative bearish exposure without options.</li>
<li><a href="/wiki/strike-price/">Strike Price</a> — defines the two put levels in a spread.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying spreads.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects spread cost and profitability.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for managing spread risk.</li>
</ul>
</div>
