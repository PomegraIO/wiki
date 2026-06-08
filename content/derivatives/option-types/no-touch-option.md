---
title: "No-Touch Option"
description: "A binary option that pays a fixed sum only if the underlying asset never touches a barrier level throughout the option's life."
keywords:
  - binary options
  - barrier options
  - exotic options
  - inverse payoff
  - structured derivatives
image: "/svg/derivatives.svg"
---

*A **no-touch option** is a [binary option](/option/) that delivers a fixed cash payoff if and only if the underlying asset avoids a specified barrier level throughout the entire option life. It is the inverse of the [one-touch option](/one-touch-option/): the buyer is paid for the underlying *staying away* from a price.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">No-Touch Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A binary payoff tied to avoiding a barrier, not hitting it.</div>

|   |   |
|---|---|
| **What it is** | Binary option paying fixed sum if barrier is never touched |
| **Barrier type** | Single predetermined level (above or below spot) |
| **Payoff trigger** | No contact from inception through [expiration-date](/expiration-date/) |
| **Payoff amount** | Typically 100 (or notional) × fixed cash amount |
| **Also called** | No-hit option, avoid-barrier option |
| **Common underlying** | Forex, equity indices, commodities |
| **Inverse of** | [One-touch-option](/one-touch-option/) |
| **Primary use** | Hedging downside or capping upside loss |

</aside>

## The inverse mechanic: paying for stability

Where a [one-touch option](/one-touch-option/) rewards the trader for a sharp move, a no-touch option rewards the trader for *stability*. If an exporter expects his home currency to remain reasonably strong through a fiscal quarter but fears a sudden devaluation event, he might buy a no-touch option struck at a depreciation floor. He pays a premium upfront. If the currency never touches that floor level by expiry, he receives the full fixed payout—a reward for the non-event. The logic is that extreme moves carry tail risk; by paying to insure against them and collecting a payoff if they do not occur, he transforms tail uncertainty into a defined profit.

## Pricing: the cost of confidence in stability

A no-touch option is expensive (relative to its potential payoff) when the barrier is close to the current spot price, because the probability of avoiding it is low. Conversely, it is cheap when the barrier is far from spot, because avoidance becomes nearly certain. This inverse relationship to strike distance is the opposite of a standard [call-option](/call-option/) or [put-option](/put-option/).

The no-touch premium depends critically on [volatility](/historical-volatility/). In a calm market, the no-touch is inexpensive because big moves are unlikely. In a turbulent regime, the same barrier becomes expensive to avoid. A trader selling no-touch options is essentially selling insurance against big moves—the seller collects a high premium but faces catastrophic loss if the barrier is breached even once, even on the final day. This negative [gamma](/gamma/) risk (worsening hedging costs as spot approaches the barrier) is why banks typically do not offer generous no-touch payoffs to retail customers.

## Real-world scenarios and use

No-touch options appear frequently in emerging-market finance, where currency stability is prized. A foreign investor holding Brazilian real assets might buy a no-touch option against the real breaching a critical devaluation level. If political stability holds and the real never touches the barrier, the investor pockets the payoff and keeps the underlying position profitable. If a shock (central-bank crisis, commodity collapse) triggers barrier breach, the investor loses the premium but already has other hedges in place or closes the position.

Equity traders use no-touch structures differently. A long-equity holder worried about a gap-down event (sudden earnings miss, scandal) might buy a no-touch put, paying for the luxury that the stock avoids a certain floor. This is strategically similar to buying [protective-put](/protective-put/) insurance, but with the psychological appeal that no large move = full payout, rather than a gradual payoff schedule.

## Relationship to forward guidance and expectations

In currency markets, no-touch options often reflect trader views on [forward-guidance](/forward-guidance/) by central banks. If a central bank credibly commits to keeping rates stable, the probability of a currency breaching a distant barrier falls, making the no-touch cheap. Conversely, if central-bank credibility is weak or a currency peg is under attack, the same no-touch becomes expensive. This makes no-touch markets excellent barometers of implicit central-bank risk premia.

## Path-dependence and settlement disputes

Like the [one-touch option](/one-touch-option/), the no-touch is path-dependent: it cares about every price point along the way, not just the terminal price. This creates settlement ambiguity. Did the barrier get touched intraday but not at close? How is "touch" defined for illiquid assets or during flash crashes? In OTC markets, contracts specify a monitoring method: continuous spot, close-only, or periodic samples. A disagreement over whether a tick-level spike counts as a barrier breach can lead to costly disputes, especially when millions of dollars hang on the outcome.

## Double-sided bets and range options

A sophisticated trader might combine a [one-touch-option](/one-touch-option/) and a no-touch option to create a range bet. Sell a one-touch call at 110, buy a one-touch call at 120, and simultaneously sell a one-touch put at 90 and buy a no-touch put at 80. The resulting structure is complex but offers defined risk zones: the trader profits if the underlying stays within a band, loses if it breaks out. This is cheaper than buying a [double-no-touch-option](/double-no-touch-option/) outright if the trader has a precise view of the range.

## Comparison to standard options

A [protective-put](/protective-put/) at 90 protects against losses below 90 but costs a premium. A no-touch put struck at 90 costs *less* premium (sometimes much less) if the strike is chosen with confidence that 90 will not be reached. But the no-touch is an all-or-nothing bet: touch 89.99 and receive zero; avoid 90 for six months and receive the full amount. Standard puts offer graduated protection; no-touch options offer binary refuge. This appeals to traders with strong conviction on a barrier but uncertainty about how close spot will get.

## See also

<div class="wiki-seealso">

### Closely related

- [One-Touch Option](/one-touch-option/) — inverse: pays if barrier is touched
- [Double No-Touch Option](/double-no-touch-option/) — extends to two barriers
- [Perpetual Option](/perpetual-option/) — no-touch structure without expiry
- [Binary Option](/option/) — general fixed-payoff derivative class
- [Barrier Option](/option/) — broader family of path-dependent contracts
- [Protective Put](/protective-put/) — standard insurance alternative

### Wider context

- [Put Option](/put-option/) — downside protection comparison
- [Volatility Smile](/volatility-smile/) — distorts no-touch pricing in real markets
- [Implied Volatility](/implied-volatility/) — critical input to premium calculation
- [Option](/option/) — foundational derivative concept
- [Over-the-Counter Market](/over-the-counter-market/) — primary trading venue
- [Forward Guidance](/forward-guidance/) — central-bank communication affecting barrier risk

</div>
