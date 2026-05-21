---
title: "Bull Put Spread"
description: "A credit strategy using short and long puts at different strikes, designed to profit when the stock stays above the short put strike through expiration."
---

*A bull put spread sells a [put option](/wiki/put-option/) and buys a lower-strike put for protection, netting an upfront credit. It profits when the stock holds above the short put, making it a popular income strategy for moderately bullish outlooks.*

## What a bull put spread is

A bull put spread sells a put at one strike and simultaneously buys a put at a lower strike, both expiring the same period. You collect a net credit at entry. If the stock stays above the short put's strike through expiration, both puts expire worthless and you keep the full credit as profit. If the stock falls below the long put's strike, you've hit maximum loss: the strike difference minus the credit received.

The strategy is the put equivalent of a [bear call spread](/wiki/bear-call-spread/)—you're collecting premium from the short put while hedging the downside with the long put.

## Why to use a bull put spread

The primary appeal is **income generation on a bullish outlook**. If you believe the stock will stay flat or rise modestly, selling a put is a natural way to earn return. Buying a lower-strike put cuts the credit in half but eliminates unlimited loss, making the position manageable.

Professional income portfolios routinely deploy bull put spreads on stocks they wouldn't mind owning. If assigned on the short put, they buy the stock at the strike; if the stock rallies, they've pocketed the credit. Either outcome is acceptable.

A second reason is **capital efficiency**. You're collecting upfront credit, which reduces margin requirements and capital tie-up compared to owning the stock outright. For traders managing limited capital, spreads amplify return-on-capital deployed.

## When a bull put spread wins

This strategy thrives when **implied volatility is elevated**. High IV inflates put premiums, widening the spread's credit window. You're effectively selling overpriced downside fear while buying cheaper deep-OTM protection.

Bull put spreads also excel in **rallying markets**. As the stock rises away from your short strike, [theta](/wiki/theta/) (time decay) accelerates and [gamma](/wiki/gamma/) turns in your favor. The short put decays fast while the long put may even gain value as the stock drifts higher.

The strategy works best when you have **bullish-to-neutral conviction**. You don't need the stock to moon—you just need it to hold above your short strike. That modest bar makes spreads forgiving compared to directional bets.

## When a bull put spread loses money

If the stock crashes below your long put's strike, you've hit maximum loss. The long put's protection becomes academic—you're locked into the worst-case outcome.

Bull put spreads also struggle in **sharply collapsing implied volatility**. If IV drops after entry (especially on good news when the stock rallies), the premium you sold in the short put disappears faster than you'd like. Your credit is locked in, but unrealized losses can widen dramatically if you try to close early.

Early assignment risk is a hidden cost. If the short put goes deep ITM and the stock pays a dividend, assignment is likely—you'll be forced to buy stock at your short strike. This isn't always bad (you wanted the stock), but if you didn't, you're forced into a position.

## Mechanics and adjustment

You receive a credit at entry—typically $200–$800 per spread. Maximum profit is the credit received. Maximum loss is `(difference between strikes) – (credit)`. Return on risk is `credit / max loss`, often 25–50%.

**Adjustment** happens when the stock falls toward your short strike. Common moves:
- **Rolling down and out**: Buy back the short put at a loss, sell a lower-strike put for a later month. Regenerates credit and buys time.
- **Converting to an iron condor**: Simultaneously sell a call spread against the put spread, turning it into a four-leg structure that profits from stagnation.

## Bull put spread vs. owning stock outright

If you're bullish and considering stock ownership, a bull put spread lets you earn income while waiting. If assigned, you own the stock at a discounted effective price (strike minus credit received). If not assigned, you've pocketed a return on zero capital deployed—a psychological win. The trade-off is capped upside; if the stock rallies 50%, you don't participate.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/bear-put-spread/">Bear Put Spread</a> — bearish analog using two puts.</li>
<li><a href="/wiki/put-option/">Put Option</a> — the short leg of a bull put spread.</li>
<li><a href="/wiki/bull-call-spread/">Bull Call Spread</a> — call-based strategy with similar risk/reward.</li>
<li><a href="/wiki/iron-condor/">Iron Condor</a> — four-leg structure combining bull and bear spreads.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — central to put spread credit.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — the contract type underlying spreads.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits this strategy.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for managing spread risk.</li>
</ul>
</div>
