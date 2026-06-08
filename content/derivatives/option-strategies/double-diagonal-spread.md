---
title: "Double Diagonal Spread"
description: "An option strategy selling short-term OTM calls and puts while buying further-dated OTM options to manage premium and directional risk."
keywords:
  - option spread strategy
  - calendar spread
  - directional options
  - premium selling
  - volatility trading
image: "/svg/derivatives.svg"
---

*A **double diagonal spread** sells near-term out-of-the-money options on both the upside and downside, simultaneously buying longer-dated out-of-the-money options at both strikes. This structure keeps the position [delta](/price-to-earnings-ratio/)-neutral while collecting premium from the rapid [time decay](/time-decay-theta/) of the short options, with the long options protecting against catastrophic moves.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Double Diagonal Spread — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A premium-collecting spread that trades short-term decay for long-term protection on both sides.</div>

|   |   |
|---|---|
| **What it is** | Sell near-term OTM calls and puts; buy longer-dated OTM calls and puts |
| **Also called** | Double calendar spread, diagonal strangle |
| **Max profit** | Premium collected from short options minus long option cost |
| **Max loss** | Limited by long options (far wider than short strikes) |
| **Ideal market** | Low volatility or mildly directional moves |
| **Key risk** | Early assignment or [volatility crush](/implied-volatility/) narrowing the spread |
| **Legs** | Four (short call, long call; short put, long put) |

</aside>

## How the structure works

A double diagonal spread is built in two distinct vertical layers. First, you establish a [call spread](/call-option/) on the upside: sell a near-term call at a higher strike, buy a farther-out call at an even higher strike. Simultaneously, you construct a [put spread](/put-option/) on the downside using the same logic—sell the near-term put, buy the farther-dated put deeper out of the money.

The short options are typically 30–45 days out; the long options are 90–180 days out. This timing difference is where the name "diagonal" comes from—the strikes and expirations form a diagonal line when plotted on a payoff diagram.

The core appeal is that the long options are cheaper (less [time value](/option-premium/)) than they appear, because you're offsetting their cost with the premium you collect from the nearer-term shorts. If the underlying stays within a defined range, both short options expire worthless and you keep the net credit.

## Why premium decay matters more than direction

The [time decay](/time-decay-theta/) of the short options is the strategy's engine. As expiration approaches, the value of 30-day options collapses far faster than 180-day options. A week before the shorts expire, you pocket most of the collected premium.

However, you're explicitly accepting that if the underlying races past your long strikes (the disaster barrier), your profit becomes a loss. This is the trade-off: you sell protection cheaply by buying it farther away. If volatility spikes and the stock gaps hard, your long options may not be far enough out to save you.

Most traders who run double diagonals plan to roll the short options forward before expiration—close the near-term shorts at a loss or for a small profit, and sell new near-term calls and puts one or two months further out. This rolling is labour-intensive but converts the one-time play into a recurring income stream.

## Volatility is the hidden opponent

The strategy thrives when [implied volatility](/implied-volatility/) remains stable or rises mildly. A sharp drop in IV—especially after an earnings report or economic surprise—can invert your position overnight. Your long options lose value faster than your short options do, particularly if the stock remains near the point where you sold the shorts.

A volatility spike, conversely, helps short positions more than long ones in the near term. You benefit if the underlying stays calm while you collect the shorts' decay, but panic selling or a black-swan event can expose your wider long strikes faster than you can manage.

Because of this asymmetry, traders often set a hard loss threshold (say, 50% of the initial credit) rather than waiting to see what happens.

## The mechanics of rolling and adjustment

Unlike a simple [covered call](/covered-call/), a double diagonal with four legs has multiple adjustment paths. If the stock rises sharply:

- Roll the short call up and out (buy to close the near-term short, sell a farther-out call at a higher strike).
- Leave the short put alone if it's staying deep out of the money.
- Widen the put side, if needed, to collect more premium and offset any call-side losses.

Conversely, if the stock drops sharply, you can defend the put side while letting the call expire.

The cost of each roll is real; commissions and bid-ask slippage erode returns on strategies with many legs. This makes a double diagonal more suitable for accounts with larger positions and lower commission structures, or traders with high conviction about the stock's range.

## When to use this strategy

Double diagonals work best for stocks you expect to trade sideways for months, with occasional minor moves in either direction. They suit companies with predictable [earnings announcements](/earnings-per-share/) (you can sell the near-term shorts before earnings and collect premium from IV expansion, then adjust if needed).

They are harder to justify if you're unsure about direction or expect a catalyst. If you believe the stock will move sharply in one direction, a simple [bull call spread](/call-option/) or [bear put spread](/put-option/) with tighter strikes is simpler and cheaper to manage.

The strategy also assumes you're disciplined enough to roll or close positions before expiration. Passive double diagonal traders who let both sides expire simultaneously often face assignment and forced rolling, which locks in suboptimal outcomes.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Backspread](/ratio-spread-backspread/) — sells fewer ATM calls and buys more OTM calls for upside explosions
- [Put Backspread](/put-backspread/) — the downside equivalent of a call backspread
- [Reverse Calendar Spread](/reverse-calendar-spread/) — buys near-term volatility while selling far-dated options
- [Option Premium](/option-premium/) — the time value and implied volatility that power diagonal spreads
- [Time Decay (Theta)](/time-decay-theta/) — the daily erosion of option value that double diagonals exploit
- [Implied Volatility](/implied-volatility/) — the hidden cost or benefit that can make or break the trade

### Wider context

- [Option](/option/) — the foundational derivative contract
- [Delta](/delta/) — directional risk measure for option positions
- [Volatility Smile](/volatility-smile/) — the pattern of IV across strikes that shapes spread economics
- [Strike Price](/strike-price/) — the key parameter that defines profitable and loss-making outcomes

</div>
