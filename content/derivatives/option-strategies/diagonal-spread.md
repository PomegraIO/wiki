---
title: "Diagonal Spread"
description: "An option strategy using calls or puts at different strikes and expirations, combining directional bias with time decay profits."
---

*A diagonal spread pairs long and short options of the same type at different strikes and different expirations. It merges the properties of vertical spreads (direction) with [calendar spreads](/wiki/calendar-spread/) (time decay), offering flexibility for traders managing multiple concerns.*

## What a diagonal spread is

A diagonal spread typically buys a longer-dated option and sells a shorter-dated option at a different strike. For example: buy a $100 call expiring in 90 days, sell a $110 call expiring in 30 days. As the short call expires, you can roll it (close and sell a new one), converting the position into a calendar spread or adjusting the strike for a new direction.

The payoff combines theta decay (profits from the short) with directional exposure (profits from the long being further OTM or ITM).

## Why to use a diagonal spread

The primary reason is **flexibility**. Unlike a static vertical spread, a diagonal spread allows you to roll the short option monthly while holding a longer-dated long option. This lets you adjust direction and capture multiple months of theta decay from a single long option purchase.

A second reason is **capital efficiency with adjustability**. You pay once for the long option (a multi-month position) and collect premium monthly from the short, turning the long into a effectively self-financing position over time.

Diagonal spreads also suit **uncertain or evolving outlooks**. You commit to a longer-term directional thesis but adjust your short-term positioning weekly or monthly.

## When a diagonal spread works

Diagonal spreads thrive when **you have a long-term conviction but uncertain short-term direction**. You're bullish long-term but want to harvest income and flexibility along the way.

They also excel in **choppy, range-bound markets** where rolling the short option multiple times captures multiple cycles of time decay.

Diagonals work well when **implied volatility is elevated**. You sell expensive short options monthly while your long option remains cheap, widening the spread.

## When a diagonal spread loses money

If the stock moves sharply in the opposite direction of your long option, the long depreciates and losses mount. Unlike a vertical spread with a hard cap, a diagonal's loss can expand as the long decays.

Diagonals also require **active management**. Passive, buy-and-hold doesn't work; you're rolling the short option multiple times. Each roll costs commissions and subjects you to execution risk.

If the stock gaps through your short option strike early, you're forced to manage assignment or roll at an inopportune moment. The complexity increases.

## Mechanics and adjustment

You pay an initial debit: the cost of the long option minus the premium from the short option. If the long costs $500 and the short generates $200, your net debit is $300.

Maximum profit is theoretically unlimited (long call direction) with the spread's width as a lower bound. Maximum loss is the initial net debit paid.

**Adjustment** is the core of diagonal trading:
- **Rolling the short**: Every 21–30 days, buy back the short and sell a new one at the same or different strike for the next month.
- **Rolling the long**: If the stock moves significantly, buy back the long and sell a new one at a new strike, resetting the position.
- **Closing and pivoting**: If the trade isn't working, exit both legs and deploy capital elsewhere.

## Diagonal spread vs. vertical spread

A vertical spread is static: defined risk and profit on day one, no management required. A diagonal spread is dynamic: adjustable, requires monitoring and rolling, but offers flexibility. Choose verticals for simplicity; choose diagonals for active traders who want to adjust positions.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/calendar-spread/">Calendar Spread</a> — same strikes, different expirations.</li>
<li><a href="/wiki/vertical-spread/">Vertical Spread</a> — same expiration, different strikes.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits diagonal spreads.</li>
<li><a href="/wiki/delta/">Delta</a> — directional exposure from the long option.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects short-option premiums.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying diagonal spreads.</li>
<li><a href="/wiki/expiration-date/">Expiration Date</a> — defines when rolling occurs.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for managing diagonal risk.</li>
</ul>
</div>
