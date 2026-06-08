---
title: "Rolling an Option Position"
description: "Rolling an option means closing one position and opening another with a different strike or expiration. Learn when traders use rolls to extend gains or manage risk."
keywords:
  - rolling an option
  - roll an option position
  - option roll management
  - closing and opening options
  - extend option position
  - manage option trades
image: "/svg/derivatives.svg"
---

*Rolling an option position means closing an existing option and simultaneously opening a new one, typically with a different strike price or expiration date. Traders roll to lock in gains, extend a profitable bet, adjust risk exposure, or avoid assignment while staying in the trade.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Rolling an Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and options." />

<div class="wiki-infobox-caption">A strategic move to restructure an option trade without exiting the market entirely.</div>

|   |   |
|---|---|
| **What it is** | Close one option leg, open another (different strike, expiration, or both) |
| **Common types** | Up roll, down roll, out roll, diagonal roll (combo of strike + expiration shifts) |
| **Why traders do it** | Avoid assignment, collect more premium, extend a winning position, reduce risk |
| **Cost** | Commissions, bid-ask spreads, and slippage on both legs |
| **Outcome** | New position with reset risk profile and fresh time decay |

</aside>

## Why traders roll instead of exiting

The core appeal of rolling is staying in the trade while resetting the clock. If you sold a [call option](/call-option/) and the underlying stock rallies, assignment could force you to sell shares—often not what you want. Rolling the call "out" (to a later [expiration date](/expiration-date/)) and "up" (to a higher [strike price](/strike-price/)) lets you keep the stock and collect fresh premium. The alternative—closing the old call and buying the stock back—locks in a loss immediately. A roll defers that reckoning and potentially profits from a continuation.

Similarly, buyers facing expiration can roll losing positions into later expirations, hoping for a reversal. Sellers of covered calls or cash-secured puts roll routinely to maintain income streams month-to-month.

## Types of rolls: direction and timing

**Up roll** means raising the [strike price](/strike-price/). A seller of a 100 call might roll up to a 105 call, reducing the chance of early assignment and opening room for stock appreciation. A buyer rolling up shifts to a higher strike—profitable if the underlying has already risen.

**Down roll** means lowering the strike. A buyer of a 100 call rolling down to a 95 call reduces the break-even point and can recover losses if the underlying has fallen.

**Out roll** extends the [expiration date](/expiration-date/) without changing the strike. A seller might roll from a 30-day call to a 60-day call at the same strike, collecting extra premium as compensation for fresh [time decay](/time-decay-theta/). A buyer rolling out extends the duration of a position, delaying the deadline for the underlying to move.

**Diagonal roll** combines a strike and expiration change. For instance, selling a 30-day 100 call and simultaneously buying a 60-day 105 call locks in a credit if the near-term call is worth more, extends exposure, and raises the breakeven.

## The mechanics: buying and selling legs at once

Rolling is best executed as a single transaction—selling (or buying to close) the original option and buying (or selling to open) the new one in one order. Many brokers support "close and open" or "roll" order types that pair the legs, minimizing the risk that one fills without the other. The net credit or debit determines whether you're paying out of pocket or receiving cash.

Example: You sold a 30-day call at a 100 strike for $2.00. It's now 10 days from expiration, the stock has rallied to $102, and the call is trading at $2.50. You could close it for a $0.50 loss, but instead you sell a new 45-day call at a 105 strike for $1.80. Net: you spend $0.70 to close and open ($2.50 – $1.80). Your total credit from both calls is now $1.30 ($2.00 + –$0.70). The new call expires later and has a higher strike—less risk of assignment.

## When rolling makes sense

Rolling is economical when the credit (or debit) you receive from the new leg offsets or exceeds the cost of closing the old one, AND when the reset position aligns with your outlook.

**Rolling out before expiration** is the most common scenario. If you sold a call and the stock rose, rolling out and up (or at the same strike) avoids assignment and lets time decay work in your favor again. The longer the new expiration, the more premium you typically collect—but only if implied volatility hasn't collapsed.

**Adjusting risk mid-trade** is another use. If a position has moved deeply in-the-money or out-of-the-money, rolling to a different strike realigns the [delta](/delta/) and [probability](/implied-volatility/) of success.

**Avoiding whipsaw on assignment** appeals to covered call sellers. Rolling up and out just before a call goes in-the-money prevents the loss of shares.

Rolling is less sensible when commissions and spreads eat up the premium advantage, or when your outlook has fundamentally changed—in which case closing and moving on may be cleaner.

## The costs and limitations

Each roll incurs trading costs: commissions on both legs, [bid-ask spreads](/bid-ask-spread/), and potential slippage if market depth is thin. On spreads, the cost can be material. Rolling also resets [assignment risk](/exercise-price/). If you roll into a new position and the stock moves sharply against you before expiration, you face a fresh threat.

Psychologically, rolling can trap a trader into managing a bad position indefinitely rather than accepting a loss and redeploying capital. Rolling should be a tactical adjustment, not a way to dodge accountability.

Tax treatment can matter too. Closing a position and opening a new one are separate trades for IRS purposes. Some traders monitor the [wash-sale](/wash-sale/) rule if rolling into a losing position.

## Rolling on earnings or events

Traders often roll in the week before earnings announcements. [Implied volatility](/implied-volatility/) typically rises ahead of earnings—making short options pricey to close and long options expensive to sell. Rolling can lock in that volatility inflation without exiting the trade entirely. After earnings, if volatility contracts, the new position starts with lower premium but less uncertainty.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Option](/call-option/) — what you're selling or buying in a roll
- [Expiration Date](/expiration-date/) — the deadline that often triggers a roll
- [Strike Price](/strike-price/) — the reference level you adjust in an up or down roll
- [Time Decay (Theta)](/time-decay-theta/) — the force that makes rolling out attractive to sellers
- [Implied Volatility](/implied-volatility/) — affects the premium you collect on a new leg
- [Option Premium](/option-premium/) — what you receive or pay in a roll transaction
- [Delta](/delta/) — helps you decide whether to roll up, down, or out

### Wider context

- [Option](/option/) — the underlying derivative you're managing
- [Derivatives: Hedging](/derivatives-hedging/) — how professionals use rolls in risk management
- [Put Option](/put-option/) — rolls apply to puts as well as calls

</div>
