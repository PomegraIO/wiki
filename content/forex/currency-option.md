---
title: "Currency Option"
description: "A currency option gives the holder the right, but not the obligation, to buy or sell a currency pair at a specified price on or before a specified date. Options offer payoff flexibility that forwards and futures do not."
keywords:
  - currency option
  - FX option
  - call option
  - put option
  - option premium
image: "/svg/forex.svg"
---

*A **currency option** gives the buyer the right — but not the obligation — to buy or sell a [currency pair](/currency-pair) at an agreed-upon rate on or before an agreed-upon date. The buyer pays a premium upfront; the seller (writer) receives that premium and accepts the obligation if the option is exercised. Currency options are more flexible than [forwards](/fx-forward) but more expensive.*

<div class="wiki-hatnote">

For binding obligations without choice, see [FX Forward](/fx-forward) and [currency future](/currency-future); for volatility-based strategies, see [fx-volatility-surface](/fx-volatility-surface).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Currency Option — key facts</div>

<img src="/svg/forex.svg" alt="Payoff diagrams for call and put currency options" />

<div class="wiki-infobox-caption">Options are rights, not obligations; payoffs are flexible.</div>

|   |   |
|---|---|
| **What it is** | Right to buy (call) or sell (put) at a fixed rate |
| **Premium** | Price paid upfront for the right |
| **Expiration** | European (only at maturity) or American (anytime before) |
| **Strike price** | The exchange rate at which you can exercise |
| **Intrinsic value** | Max(0, payoff at current spot) |
| **Time value** | Option price minus intrinsic value |
| **Used for** | Hedging with flexibility; directional bets; volatility trades |

</aside>

## Call and put options

A **call option** on EUR/USD gives the right to buy euros (and sell dollars) at a strike price. If EUR/USD is 1.0850 and you buy a call at strike 1.1000, you have the right to buy euros at 1.1000. If the euro strengthens to 1.1200 by expiration, you exercise the call: buy at 1.1000, instantly worth 1.1200 = $200 per euro of profit. If the euro weakens to 1.0600, you do not exercise. Your loss is just the premium paid.

A **put option** on EUR/USD gives the right to sell euros (and buy dollars) at a strike price. If EUR/USD is 1.0850 and you buy a put at strike 1.0700, you have the right to sell euros at 1.0700. If the euro weakens to 1.0600, you exercise: sell at 1.0700, avoid the 1.0600 spot = $100 per euro gain. If the euro strengthens to 1.1000, you do not exercise.

The buyer pays a premium for these rights. The seller (writer) collects the premium and accepts the obligation to deliver if exercised.

## American vs. European options

**American options** can be exercised anytime before expiration.

**European options** can be exercised only on the expiration date.

American options are more valuable (you have more flexibility) and therefore more expensive. Most over-the-counter (OTC) currency options are American; exchange-traded options are usually European.

## Intrinsic and time value

An option's price has two components:

**Intrinsic value:** The payoff if exercised immediately. A call on EUR/USD with strike 1.0800, with spot at 1.0900, has intrinsic value = 1.0900 − 1.0800 = $0.0100 per euro. A call with strike above the spot has zero intrinsic value.

**Time value:** Everything else. Even if an option has zero intrinsic value, it has value because the currency can move in the holder's favor before expiration. As expiration approaches, time value decays to zero.

Most of what traders pay for options is time value. Two weeks until expiration, the option is worth less than two months. On expiration day, an out-of-the-money option is worthless.

## Hedging vs. speculation

A company expecting a payment in euros three months away can hedge with either a forward or an option. With a forward (say, 1.0850), the rate is locked: if the euro moves to 1.1200, the company receives the locked 1.0850, missing the opportunity. If it falls to 1.0500, the company is protected.

With an option (say, a 1.0850 call), the company pays a premium (maybe 0.0050, or $50 per euro) but keeps upside. If the euro moves to 1.1200, the company exercises the call at 1.0850 and captures the move. If it falls to 1.0500, the company does not exercise and sells at spot, having lost only the premium paid.

A forward is a pure hedge: no premium, but no upside. An option is a costly hedge but with protection of downside and preservation of upside.

Speculators use options for leverage and payoff asymmetry. Buy an out-of-the-money call and risk only the premium; if the currency moves as predicted, the payoff is outsized. If it doesn't, the loss is capped at the premium paid.

## Vanilla vs. exotic options

**Vanilla options** are standard calls and puts, exercisable in the conventional way. Most currency options are vanilla.

**Exotic options** have special features: knockouts (cease to exist if a barrier is breached), lookbacks (payoff based on the best rate during the life, not just spot), etc. Exotics are used for bespoke hedging strategies but are less liquid and harder to price.

## See also

<div class="wiki-seealso">

### Closely related

- [FX Forward](/fx-forward) — binding alternative to options
- [Currency future](/currency-future) — exchange-traded alternative
- [Spot exchange rate](/spot-exchange-rate) — baseline for option pricing
- [FX Volatility Surface](/fx-volatility-surface) — determines option premiums
- [Vanilla FX Option](/vanilla-fx-option) — standard option types

### Wider context

- [Pip](/pip) — option premiums quoted in pips
- Interest rate parity — part of option pricing
- [Central bank](/central-bank) — sometimes uses options in intervention

</div>
