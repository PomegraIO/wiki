---
title: "How the Ratchet Mechanism Works in a Cliquet Option"
description: "Understand cliquet options: how periodic returns are locked in, reset, and how the ratchet structure affects pricing and hedge costs."
keywords:
  - cliquet option ratchet mechanism
  - ratchet options
  - cliquet options
  - structured products
  - periodic reset options
  - equity derivatives
image: "/svg/derivatives.svg"
---

*A cliquet option (also called a "ratchet" or "reset" option) is an exotic [option](/option/) that locks in periodic gains and resets the floor, protecting the investor against losses while capping upside. Instead of a single [strike price](/strike-price/) and expiration, a cliquet divides the option's life into intervals (e.g., quarters). At the end of each interval, the best-of-current-price-or-previous-floor becomes the new floor, and a fresh lookback period begins. This mechanism is why structured-product issuers use cliquets—they offer downside protection without outright put costs.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cliquet Options — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Lock in gains each interval; start fresh from a protected floor.</div>

|   |   |
|---|---|
| **Structure** | Multiple reset periods (e.g., quarterly) |
| **Floor mechanism** | Periodic high-water mark is locked; becomes new floor |
| **Leverage** | Typically 80–120% of index or equity return each period |
| **Call ratio** | Often 1:1, but caps can apply |
| **Payoff feature** | Gains compound at reset; losses reset to zero |
| **Typical issuer** | Investment banks (principal-protected notes, ETFs) |
| **Pricing complexity** | High; requires Monte Carlo simulation |
| **Typical cost** | 100–300 bps (1–3%) embedded cost, factored into indexing |

</aside>

## The Core Mechanic: Locking In and Resetting

A simple cliquet option works like this:

Suppose an investor buys a 4-year equity cliquet with annual resets, struck on a stock index at 100.

- **Year 1:** The index rises to 110. At the annual reset, the gain of +10% is locked in. The new floor becomes 110.
- **Year 2:** The index falls to 105. The investor is protected; the cliquet locks in max(105, 110) = 110, realizing zero return that period. The floor stays 110.
- **Year 3:** The index rises to 130. The gain from 110 to 130 is +18.2%, locked in. The new floor is 130.
- **Year 4:** The index falls to 120. The cliquet locks in max(120, 130) = 130, realizing zero return. The final floor is 130.

Over 4 years, the index returned 20% (100 → 120). The cliquet investor realized 10% + 0% + 18.2% + 0% = cumulative gains of roughly 29.3% (after compounding).

The mechanism is a series of digital options or lookback puts embedded within the structure. At each reset, the investor implicitly holds a put option that protects against any loss during that interval.

## Why Structured-Product Issuers Use Cliquets

For a bank issuing a principal-protected note or a buffer ETF, the cliquet structure is attractive because it:

1. **Reduces hedge cost.** A traditional put option covering the entire 4-year period is expensive. The cliquet spreads the protection across multiple short periods, and short-dated puts are cheaper than long-dated puts (because [volatility](/historical-volatility/) decays and there is less time for a large move). The bank's hedging cost is lower.

2. **Compresses investor payoff inflation.** A cliquet that locks in returns each period and resets the floor naturally caps investor wealth creation. An investor cannot realize a 100% gain in a single period if the structure only allows a 20% return per period with a cap. The issuer benefits from reduced tail-event payouts.

3. **Reduces reinvestment complexity.** If an investor received all gains at the end (not reset periods), the issuer would owe a larger terminal payout. The periodic reset forces an implicit "compounding" of returns at the issuer's chosen rate, rather than at the index's natural path.

## How the Ratchet Affects Premium and Pricing

The cliquet is cheaper than a European call with the same notional because the periodic reset and floor cap limit upside. Issuers typically pass on this cost savings as higher notional leverage (e.g., 110% of index return instead of 100%) to attract investors, while still retaining a spread.

Pricing a cliquet is computationally intensive. Because the option's payoff depends on the path of the index (not just the terminal price), [Monte Carlo simulation](/discounted-cash-flow-valuation/) is standard. The bank simulates thousands of price paths, applies the reset and floor logic at each interval, and calculates the expected discounted payoff.

A simplified formula for a single period is:

**Payoff = max(0, min(S_T - S_0, CAP)) + FLOOR**

where S_0 is the starting price, S_T is the ending price in that period, CAP is the limit on returns, and FLOOR is the protected floor. Over multiple periods, this logic compounds.

The [Black-Scholes model](/black-scholes-model/) cannot be directly applied to cliquets because it assumes a single exercise point. The cliquet's value depends on multiple decision points and path history, making simulation essential.

## Leverage and Cap Mechanics

A typical cliquet might offer:

- **100% leverage:** Investors capture the full index return each period, up to a cap.
- **Cap = 8% per period:** Any return above 8% in a single period is forfeited.
- **Floor = 0%:** Negative returns are capped at zero (the previous floor is protected).

Another variant:

- **120% leverage:** Investors get 1.2× the index return.
- **Cap = 12% per period:** Gains above 12% are forfeited.

The leverage and cap are tools the issuer uses to keep hedging costs manageable. Higher leverage increases the cost (the bank hedges a larger notional); higher caps reduce cost (the bank hedges less tail risk). Issuers adjust both to hit a target cost.

## Time Decay and Volatility Impact

The cliquet is sensitive to [implied volatility](/implied-volatility/). Higher volatility increases the value of the embedded put options (the periodic protection), which increases the issuer's hedging cost. In a high-volatility environment, issuers often reduce leverage or tighten caps to stay profitable.

Time decay ([theta](/theta/)) is not directional—it favors neither long nor short. Each reset period, the time value of the embedded options decays, which would normally reduce the option's value. But the periodic reset creates a "reset value" that partially offsets decay.

For investors, the key insight is that cliquets are most valuable when volatility is high (wider swings within periods mean a higher chance of capturing a larger gain before the reset) but least costly for the issuer (because the bank can reduce leverage).

## Comparison to Alternatives

**vs. a European call:** A cliquet is cheaper upfront but caps each period's return. An investor expecting a sharp, sustained rally prefers the call.

**vs. a levered index fund:** The cliquet has a defined cost and a termination date. A levered index fund has daily rebalancing and compounds gains (or losses) continuously. The cliquet's reset dampens both gains and losses compared to continuous compounding.

**vs. a barrier option:** Barrier options knock in or out at a price level. Cliquets reset at time, not price. A barrier is used for conditional hedging; a cliquet is used for periodic rebalancing and floor protection.

## Real-World Example: Structured Notes

A major bank issues a 5-year note linked to the S&P 500, offering:

- Quarterly resets
- 100% leverage on the index return each quarter
- 3% cap per quarter
- Principal protection at maturity

An investor buys $100,000 notional. If the S&P rises 12% in Q1, the cliquet locks in 3% (the cap). New floor: 103. If the S&P falls 5% in Q2, the cliquet locks in 0% (protected). Floor stays 103. Over 5 years with realistic returns, the investor might realize 25–35% total return (compounded), compared to perhaps 50% if they owned the index outright. The trade-off: downside is limited to the cap each period, and principal is guaranteed at maturity.

The bank sells the note at par ($100,000) and immediately hedges by buying index calls and selling index puts—a synthetic cliquet. The bank's profit is the bid-ask spread plus the embedded carry cost of the hedge (the difference between leverage offered and hedging costs incurred).

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — foundational option mechanics and terminology
- [Strike Price](/strike-price/) — the reference price for option payoffs
- [Call Option](/call-option/) — unlimited upside, defined cost
- [Put Option](/put-option/) — downside protection
- [Implied Volatility](/implied-volatility/) — how volatility affects option value
- [Monte Carlo Simulation](/discounted-cash-flow-valuation/) — pricing complex derivatives
- [Structured Product](/structured-product/) — how banks engineer retail-facing investments

### Wider context

- [Black-Scholes Model](/black-scholes-model/) — foundational option pricing theory
- [Derivatives Hedging](/derivatives-hedging/) — how banks manage option risk
- [Barrier Option](/barrier-option/) — conditional option payoffs
- Exotic Derivatives — non-standard option structures

</div>
