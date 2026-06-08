---
title: "Pin Risk"
description: "The danger when an underlying closes at a strike price at expiration, leaving delta and exercise outcome undefined until the final moment."
keywords:
  - options
  - pin risk
  - expiration
  - delta
  - strike price
  - derivatives
  - assignment risk
image: /svg/derivatives.svg
---

*Pin risk is the uncertainty that occurs near [expiration](/expiration-date/) when an underlying's price hovers around a [strike price](/strike-price/), leaving it unclear whether an [option](/option/) will be exercised. The holder cannot know until settlement whether they will be assigned shares or cash, forcing them to make trading or hedging decisions in limbo.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Pin Risk — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and options pricing." />

<div class="wiki-infobox-caption">Uncertainty about exercise turns a simple boundary into a minefield.</div>

|   |   |
|---|---|
| **What it is** | The undefined [delta](/delta/) and assignment outcome when an underlying closes exactly at a [strike](/strike-price/) at expiration |
| **Why it's risky** | Hedges may not execute as planned; [assignment](/assignment/) happens unpredictably |
| **Timing** | Most acute in the final hours and minutes before expiration |
| **Affected positions** | Short calls/puts, [spreads](/spread/), [straddles](/option/), any position with tightly clustered strikes |
| **Mitigation** | Close the position, roll to later expiration, or accept assignment risk |
| **Related concept** | [Delta](/delta/) — undefined when price equals strike |

</aside>

## The boundary condition

In theory, a [call option](/call-option/) with a $100 strike is worth more than zero if the underlying is $101; it is worth exactly zero if the underlying is $99. The jump occurs at the strike itself. In practice, especially in the last hour before expiration, the underlying may be trading within cents of the strike, and no one knows whether it will close above or below that price. The [delta](/delta/) of a short call at-the-money is undefined — it could be exercised or expire worthless in an instant.

This boundary condition creates pin risk. A short call holder cannot know whether they will be assigned shares (forced to deliver them at the strike) until the market closes and the underlying's final price is locked in. A long [put](/put-option/) holder cannot know whether they will be exercised (forced to take on shares at the strike). If the underlying closes exactly at the strike, market rules vary, but typically the option is considered in-the-money and can be exercised at the holder's discretion, giving the short side uncertainty until the afternoon of expiration day.

## Why hedges fail at the pin

Pin risk becomes acute when a trader has tried to hedge a position by selling options and buying protective options at nearby strikes. Consider a trader who is long 10,000 shares of a stock and wants to protect against downside while collecting premium. She sells $100 [put options](/put-option/) and buys $95 puts as a hedge. If the stock closes at $99.98 at expiration, the $100 puts might be exercised (forcing her to buy 10,000 shares, worsening her position). But the $95 puts expire worthless because the stock is still above that strike. Her hedge fails precisely when it was supposed to protect her.

Alternatively, she might sell a [call spread](/call-option/) — selling $110 calls and buying $115 calls. If the stock closes at $110.50 at expiration, the short calls might be assigned (forcing her to deliver shares at $110), but the long $115 calls expire worthless. She has capped her upside at $110 but now owns no shares to deliver, forcing a scramble to buy shares or face a short position.

## The mechanics of last-minute assignment

Exchange rules for stock options typically allow assignment to occur through the next morning if the underlying closes in-the-money. But exercises are voluntary for [American options](/option/) — the holder chooses to exercise, not the exchange. This means the short side never knows for certain whether assignment will occur until the final moment. A small company with a stock around a strike price might see traders making last-minute decisions: *Is the juice worth the squeeze? Do I exercise this option or let it expire?* The short side is completely at the mercy of that decision.

Brokers typically exercise [in-the-money](/in-the-money/) options automatically, but errors and exceptions exist. A position might sit unexercised overnight, then be assigned the next morning, forcing the short seller to scramble to cover or deliver shares in a new trading session, often at worse prices. This is less common with large, liquid instruments but frequent with smaller-cap stocks and [index options](/option/).

## Compounding effects in spreads and collars

[Spreads](/spread/) concentrate pin risk. A [bull call spread](/call-option/) (long $100 call, short $110 call) faces pin risk at both strikes, though the short $110 call is the primary exposure. If the stock closes at $110, the short call might be assigned while the long call expires at-the-money, creating a gap where the trader suddenly owns an obligation. Similarly, an [iron condor](/option/) — selling calls and puts at two strike levels — can face simultaneous assignment on both sides if the stock closes exactly at one of the middle strikes, creating a chaotic unwinding.

Protective [collars](/option/) — long stock, short call, long put — have a similar problem. If the stock pins exactly at the put strike and call strike, both options might be exercised or both might expire worthless, leaving the collar unexercised on one side and the hedge either redundant or absent.

## The real cost: operational chaos

Pin risk is ultimately about operational uncertainty and the cost of unplanned outcomes. A portfolio manager with a $1 million short call position that pins at the strike faces an operational decision: buy shares to cover or let the assignment happen and scramble tomorrow? With thousands of positions across a book, multiple pins can create cascading operational problems. Risk systems assume that positions will behave predictably; pin risk introduces chaos.

Brokers and market participants have learned to price this in. On the last day of expiration, bid-ask spreads widen around strike prices. Brokers discourage holding positions into expiration, charging higher fees or refusing to carry them. This is the market's way of saying: *The uncertainty costs money, so pay for it.* A savvy trader avoids this by closing or rolling positions one or two days before expiration rather than holding them until the final bell.

## Mitigation strategies

Professional traders simply do not hold significant positions into expiration. They close or roll to the next month one or two days before expiration. Closing costs a small amount but eliminates pin risk entirely. Rolling — closing the current expiration and selling options for the next month — preserves the exposure while removing the boundary condition.

For positions that must be held (unusual, but it happens), traders can widen the spread between strikes to reduce the chance of pinning. Instead of a bull call spread with $100 and $110 calls, use $100 and $115. The underlying is less likely to close in the pin zone. Alternatively, accept assignment and plan for it. If you expect to be assigned, buy or sell the underlying proactively on expiration day at a price you control, rather than waiting for the broker to assign the next morning at potentially worse levels.

## Why exchanges and regulators tolerate it

Pin risk is a known feature of options markets, not a bug. The root cause is that exercise is binary (either happens or it doesn't) while the stock price is continuous. Regulators and exchanges could eliminate it by forcing automatic cash settlement rather than physical delivery, but that would change the entire market structure and destroy the ability to use options for actual hedging. Instead, participants adapted: sophisticated traders avoid holding into expiration, retail traders learn the hard way, and brokers profit from the chaos by charging extra fees.

## See also

<div class="wiki-seealso">

### Closely related

- [Strike Price](/strike-price/) — the boundary where pin risk occurs
- [Delta](/delta/) — undefined at-the-money
- [Assignment](/assignment/) — the forced delivery or purchase outcome
- [Expiration Date](/expiration-date/) — when pin risk becomes acute
- [In-the-Money](/in-the-money/) — the condition that triggers assignment

### Wider context

- [Option](/option/) — the instrument exposing traders to pin risk
- Greeks — the framework for understanding option behaviour
- [Call Option](/call-option/) and [Put Option](/put-option/) — the specific positions that pin
- [Spread](/spread/) — strategy that amplifies pin risk
- Risk Management — how professionals mitigate it

</div>
