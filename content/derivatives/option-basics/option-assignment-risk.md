---
title: "Option Assignment Risk"
description: "The risk that a short option holder will be forced to settle the underlying position early when the option holder exercises their right."
keywords:
  - assignment risk
  - early exercise
  - short call assignment
  - short put assignment
image: "/svg/derivatives.svg"
---

*An **assignment risk** on options is the possibility that someone holding a short (sold) [option](/option/) will be forced to buy or sell the underlying before [expiration](/expiration-date/) when the option holder chooses to exercise. The assignment happens with little warning and can lock you into an unexpected transaction at precisely the wrong moment.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Assignment Risk — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for financial derivatives." />

<div class="wiki-infobox-caption">Selling an option means accepting the risk of sudden assignment.</div>

|   |   |
|---|---|
| **What it is** | Forced settlement of an underlying position when a short option is exercised |
| **Also called** | Early exercise risk, settlement risk |
| **Most common on** | [In-the-money](/in-the-money/) options with large [dividend](/dividend/) payments upcoming |
| **Affects** | [Covered call](/covered-call/) writers, [naked option](/naked-option/) sellers, [put option](/put-option/) sellers |
| **Timing** | Can occur at any time, even days before [expiration](/expiration-date/) |
| **Primary defence** | Monitor for [dividend](/dividend/) dates, manage position size, actively roll positions |

</aside>

## Why assignment happens

When a trader sells an [option](/option/), they are granting the buyer the right to exercise. That buyer can choose to exercise early—before the [expiration date](/expiration-date/)—if it benefits them. Most of the time, the buyer will wait until expiration to see if the [option](/option/) is profitable. But in certain situations, early exercise is rational, and the short seller must be ready.

The classic trigger is a dividend announcement. If you sold a [call option](/call-option/) and the underlying [stock](/stock/) is about to pay a large [dividend](/dividend/), the call buyer might exercise early to capture that dividend. You had no say in the matter. On assignment, you must deliver the shares at the [strike price](/strike-price/), forfeiting the [dividend](/dividend/) yourself—even though your shares were called away before the payment date.

Similarly, if you sold a [put option](/put-option/) on a [stock](/stock/) that has dropped sharply, the buyer might exercise to force you to buy the now-discounted shares. Again, you have no choice. The assignment happens via the clearinghouse overnight, and on the next morning, you own the shares.

## When assignment is likely

Assignment risk is highest on [in-the-money](/in-the-money/) options, especially those that are deep [in-the-money](/in-the-money/). If you sold a $95 call on a $110 stock, the buyer has strong incentive to exercise because the intrinsic value ($15) is already realised. If the underlying stock is about to ex-dividend, that incentive becomes nearly irresistible.

For [put option](/put-option/) sellers, assignment is most likely on deep [in-the-money](/in-the-money/) puts where the buyer sees no reason to wait. There is no dividend upside; the sooner they force you to buy, the sooner they pocket the intrinsic gain.

[American-style options](/option/) (which is what most U.S. listed equity options are) can be exercised at any time. [European-style options](/option/) can only be exercised at expiration. American options carry more assignment risk because the window is unlimited.

## Real-world mechanics

When a [call option](/call-option/) is assigned, you must deliver the underlying shares at the [strike price](/strike-price/). If you are a [covered call](/covered-call/) writer (you own the shares), the mechanics are tidy: the shares are removed from your account and cash is deposited. If you are a [naked option](/naked-option/) seller with no shares, you are forced to buy them in the market at the current price—possibly well above the [strike price](/strike-price/) if the stock has rallied further. Your loss is unlimited.

When a [put option](/put-option/) is assigned, you must buy the shares at the [strike price](/strike-price/). The shares land in your account and cash leaves. If you are a seller with no intention to own the stock, you are now long at an unfavourable entry point.

Assignment notices typically arrive overnight via your [broker](/broker/). You do not see it coming; you cannot negotiate or refuse. Your only defence is foresight: knowing when [dividend](/dividend/) dates are approaching, monitoring whether your short [option](/option/) is [in-the-money](/in-the-money/), and actively rolling the position before the danger window opens.

## Rolling to manage risk

The professional answer to assignment risk is to *roll*: close the short [option](/option/) (buy it back) and simultaneously sell a new [option](/option/) further out in time (and often at a different [strike price](/strike-price/)). By rolling out, you reset your [assignment](/option-assignment-risk/) date to a later [expiration](/expiration-date/). You also collect fresh premium, which cushions the cost of buying back the original [option](/option/).

A [covered call](/covered-call/) writer who sold June calls will often roll them in late May to August calls if the stock has rallied sharply or a [dividend](/dividend/) is due. The new August calls are [out-of-the-money](/out-of-the-money/) (if written at a higher [strike price](/strike-price/)), reducing assignment risk. The premium collected on the new call offset part of the cost to close the June call.

This roll-forward discipline is how large market-makers survive selling millions of dollars of [option](/option/) premium every day. They accept assignment risk but never hold the risk for long; they rotate it to the next cycle month before it becomes dangerous.

## Naked option sellers face unlimited risk

A [naked option](/naked-option/) seller bears the full brunt of assignment risk with no hedge. Selling a naked [put option](/put-option/) means you must be prepared to own the stock if assigned—at a loss if the stock continues to fall. Selling a naked [call option](/call-option/) means you must buy shares at market prices if assigned, potentially at a massive loss if the stock has rallied past your [strike price](/strike-price/).

Many retail traders underestimate this risk. They sell a "small" [put option](/put-option/) thinking the [premium](/option-premium/) is free money, only to face assignment of 100 shares when the underlying drops. If the [stock](/stock/) plunges further, they are left holding a losing position with no exit strategy.

## The dividend calendar as your crystal ball

Traders who focus on [option](/option/) income (selling [covered call](/covered-call/) and [put option](/put-option/) strategies) rely heavily on a dividend calendar. Most companies publish dividend dates a quarter in advance. If your short [call option](/call-option/) is [in-the-money](/in-the-money/) and an ex-dividend date is less than two weeks away, assignment risk is material. Rolling to a later [expiration](/expiration-date/) or closing the position early is prudent risk management.

## See also

<div class="wiki-seealso">

### Closely related

- [Option Expiration Cycle](/option-expiration-cycle/) — the predictable quarterly schedule of expiration dates
- [Naked Option](/naked-option/) — selling without a hedge, bearing unlimited risk
- [Covered Call](/covered-call/) — selling calls against shares you own to limit assignment loss
- [In-the-Money](/in-the-money/) — an option with intrinsic value, most likely to be exercised
- [Dividend](/dividend/) — the trigger for most early assignment on calls
- [Put Option](/put-option/) — the right to sell; assignment forces you to buy
- [Call Option](/call-option/) — the right to buy; assignment forces you to deliver

### Wider context

- [Option](/option/) — contracts granting the right to buy or sell at a fixed price
- [Broker](/broker/) — intermediaries executing assignment on behalf of the clearinghouse
- [Exercise Price](/exercise-price/) — the price at which assignment settles

</div>
