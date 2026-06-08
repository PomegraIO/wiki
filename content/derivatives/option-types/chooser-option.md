---
title: "Chooser Option"
description: "An exotic option that lets the holder decide at a future date whether it becomes a call or put."
keywords:
  - chooser option
  - exotic option
  - call-or-put
  - flexible derivative
  - option strategy
  - structured derivatives
image: "/svg/derivatives.svg"
---

*A **chooser option** is an [exotic option](/option/) that grants the holder the right to choose, at a specified future date, whether the [option](/option/) becomes a [call](/call-option/) or a [put](/put-option/). The holder pays one [premium](/option-premium/) upfront but decides only later whether to bet on appreciation or depreciation—a bet each way disguised in a single contract.*

<div class="wiki-hatnote">

For basic [option](/option/) mechanics, see [Option](/option/); for other exotic variants, see [Rainbow Option](/rainbow-option/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Chooser Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and structured instruments." />

<div class="wiki-infobox-caption">Optionality on optionality: choose your direction later.</div>

|   |   |
|---|---|
| **What it is** | [Option](/option/) where holder chooses at a pre-set future date whether it becomes [call](/call-option/) or [put](/put-option/) |
| **Choice date** | Date the holder must decide; typically weeks or months before [expiration](/expiration-date/) |
| **Strike price** | Same [strike](/strike-price/) typically applies whether [call](/call-option/) or [put](/put-option/) |
| **Payoff** | Max(call value, put value) at choice date; then the chosen type exercises at original [expiration](/expiration-date/) |
| **Upfront cost** | Single [premium](/option-premium/); roughly the cost of owning both a [call](/call-option/) and [put](/put-option/), minus diversification [benefit](/option/) |
| **Pricing model** | [Black-Scholes](/black-scholes-model/) extended; Monte Carlo simulation for barriers or path-dependent features |
| **Use cases** | Uncertain volatility direction; hedging pending announcements; speculative bets on volatility |

</aside>

## Basic structure

In its simplest form, a chooser [option](/option/) works like this: you buy the right to choose—at date T—whether you own a [call option](/call-option/) or a [put option](/put-option/), both struck at K and [expiring](/expiration-date/) at time T+τ.

At time T, the underlying asset is at price S. You look at the market. If S is well above K and the stock looks strong, you elect the [call](/call-option/) and pocket any upside above K. If S is below K and the outlook is weak, you elect the [put](/put-option/) and gain from any further decline. You've gotten to choose the profitable direction after seeing more information.

The value of that choice is significant. Suppose a stock will announce earnings at month 3, but your [option](/option/) [expires](/expiration-date/) at month 6. Before earnings, the stock's direction is genuinely uncertain. A standard [call](/call-option/) or [put](/put-option/) is a bet: pick a direction and live with it. A chooser defers the bet until after earnings. Once you know earnings, you choose the [option](/option/) type that profits.

## Pricing and the optional payoff

The value of a chooser [option](/option/) is bounded. At minimum, it's worth the greater of a [call](/call-option/) or a [put](/put-option/)—specifically, Max(Call value, Put value) calculated at the choice date T. At maximum, it's worth slightly less than owning both a [call](/call-option/) and [put](/put-option/) outright.

Why less than both? Because you can only exercise one. If you own both a [call](/call-option/) and [put](/put-option/) on the same stock at the same [strike](/strike-price/), you can sell one when it goes into-the-money and exercise the other if needed. A chooser forces you to commit to one choice. But this is a minor inefficiency; the chooser is typically 80–95% as expensive as owning both [options](/option/).

The [Black-Scholes model](/black-scholes-model/) extends naturally to chooser [options](/option/). The formula involves calculating call and put values at the choice date, then weighting by the probability that each is optimal. Higher volatility raises the value—more volatility means a larger gap between the call and put payoffs, making the choice more valuable.

## Why hold a chooser instead of a straddle?

A **straddle** is the direct alternative: buy both a [call](/call-option/) and [put](/put-option/), then exercise whichever becomes profitable. Straddles cost more upfront, but they offer continuous optionality—you can switch at any time, not just on the choice date.

A chooser is cheaper and simpler for investors with a known decision point. If you're waiting for:
- Earnings
- FDA approval
- A merger announcement
- Election results
- A central bank decision

Then a chooser's locked choice date aligns with your information arrival. You pay less [premium](/option-premium/) because you lose the continuous switching right. The payoff is nearly identical if you exercise the chooser optimally.

Speculators also use choosers. A trader who expects high volatility but is unsure of direction might prefer a chooser (cheaper than a straddle) to a one-sided [call](/call-option/) or [put](/put-option/) (leaves half the outcome uncovered). The choice date lets you wait and see which way the vol explosion goes.

## Variations and complications

**Simple chooser:** Same [strike](/strike-price/) K for both the eventual [call](/call-option/) and [put](/put-option/). At the choice date T, you pick whichever is worth more.

**Complex chooser:** Call and put can have different [strikes](/strike-price/). A chooser might offer: choose between a [call](/call-option/) struck at K₁ or a [put](/put-option/) struck at K₂. This adds degrees of freedom but complicates the decision.

**American-style chooser:** You can choose any time before T. This is much more valuable—equivalent to holding a straddle—and almost never issued.

**Path-dependent variants:** Some exotic choosers depend not just on the price at the choice date, but on the price path taken. For instance, a "lookback chooser" might let you choose between a [call](/call-option/) and [put](/put-option/) based on the minimum and maximum prices over the preceding period. These are priced via simulation.

## Practical use in structured products

Banks embed choosers in **structured notes** aimed at uncertain investors. A note might offer: "At year 2, choose whether to own (a) a [call](/call-option/) on the S&P 500 struck at today's level or (b) a [put](/put-option/) at today's level. Plus a guaranteed 2% coupon." The bank funds the initial deposit and coupon from the note's premium, then profits on the embedded chooser's mispricing or sells it to a [hedge fund](/hedge-fund/).

Retail investors are drawn to the "heads I win, tails I don't lose as much" narrative. But issuers price choosers fairly; the apparent flexibility is baked into a higher [strike](/strike-price/) or lower coupon elsewhere. The advantage goes to issuers and sophisticated traders, not to ordinary buyers.

## Pitfall: choosing poorly

The chooser's supposed flexibility is illusory if you choose badly. At the choice date T, one type will be in-the-money and one out. You'll pick the in-the-money option—that's automatic. But *how far* in-the-money? If both the [call](/call-option/) and [put](/put-option/) are slightly in-the-money (price sits near the [strike](/strike-price/)), the choice matters less; both are worth similar small amounts.

Worst: what if both are out-of-the-money? Then you choose whichever is less bad, but you've paid [premium](/option-premium/) upfront for optionality that was worthless. This happens if the underlying price lands near the [strike](/strike-price/) at the choice date, with low [implied volatility](/implied-volatility/). You've wasted your bet.

Also, chooser issuers often impose [strike](/strike-price/) and expiry terms designed to underdeliver. The choice date might be very close to [expiration](/expiration-date/), leaving little time for the chosen [option](/option/) to gain value. The [strike](/strike-price/) might be far out-of-the-money. These details matter more than the headline "you get to choose."

## Comparison to [rainbow options](/rainbow-option/)

Both choosers and [rainbow options](/rainbow-option/) are exotic [options](/option/) that add complexity to defer or distribute risk. But they operate on different axes. A [rainbow option](/rainbow-option/) lets one underlying asset's performance determine payoff on a basket; a chooser lets the holder's decision at a later date determine the [option](/option/) type. A chooser is about timing and choice; a [rainbow](/rainbow-option/) is about correlation and structure.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the fundamental [derivative](/option/) contract; chooser is an exotic variant
- [Call Option](/call-option/) — the right to buy; one of the two choices a chooser holder makes
- [Put Option](/put-option/) — the right to sell; the other choice available to a chooser holder
- [Strike Price](/strike-price/) — the reference price for both the eventual [call](/call-option/) and [put](/put-option/)
- [Option Premium](/option-premium/) — the upfront cost of buying a chooser [option](/option/)
- [Expiration Date](/expiration-date/) — when the chosen [option](/option/) matures and must be exercised or expires
- [Rainbow Option](/rainbow-option/) — another exotic [option](/option/) adding complexity for different reasons
- [Implied Volatility](/implied-volatility/) — expected future volatility; critical to chooser [option](/option/) pricing

### Wider context

- [Black-Scholes Model](/black-scholes-model/) — theoretical pricing framework extended to choosers
- [Straddle](/protective-put/) — owning both [call](/call-option/) and [put](/put-option/); the direct alternative to a chooser
- [Hedge Fund](/hedge-fund/) — sophisticated user of exotic [options](/option/)
- [Discounted Cash Flow Valuation](/discounted-cash-flow-valuation/) — Monte Carlo simulation often used for complex chooser pricing
- [Volatility Smile](/volatility-smile/) — pricing anomaly affecting exotic [options](/option/) like choosers

</div>
