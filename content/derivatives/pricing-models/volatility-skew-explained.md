---
title: "Volatility Skew Explained"
description: "Volatility skew is the empirical pattern where out-of-the-money puts trade at higher implied volatility than equivalent calls, reflecting asymmetric crash risk in equity markets."
keywords:
  - volatility skew explained
  - skew in options
  - put-call volatility asymmetry
  - crash risk pricing
  - implied volatility patterns
  - tail risk
---

*The **volatility skew** is an observable market phenomenon where out-of-the-money puts on stock indices and individual equities consistently trade at higher implied volatility than out-of-the-money calls—even though returns should be symmetric. This skew reflects the market's pricing of asymmetric crash risk and underlies some of the richest trading opportunities in derivatives.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volatility Skew — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives pricing." />

<div class="wiki-infobox-caption">Puts are more expensive than calls; markets fear crashes more than rallies.</div>

|   |   |
|---|---|
| **Pattern** | OTM puts: 30–40% vol; ATM: 25% vol; OTM calls: 18% vol |
| **Cause** | Investors pay for crash protection; crashes are more frequent than rallies |
| **Effect** | Put spreads and volatility swaps profit when skew normalizes |
| **Measurement** | Skew slope or "skew volatility" (difference between put and call IV) |
| **Sector variation** | Equity skew > FX skew > Commodity skew |

</aside>

## The skew pattern

Imagine a stock trading at $100. Look at options expiring in 30 days:

| Strike | Type | Implied Vol |
|--------|------|-------------|
| $90 | Put (OTM) | 32% |
| $95 | Put (OTM) | 28% |
| $100 | Call (ATM) | 25% |
| $105 | Call (OTM) | 22% |
| $110 | Call (OTM) | 18% |

The volatility slopes downward as strikes increase: deep out-of-the-money puts are expensive; deep out-of-the-money calls are cheap. This pattern is called a **skew**, and it's the opposite of what a frictionless, symmetric model would predict.

[Black-Scholes](/black-scholes-model/) assumes returns are symmetric: the probability of a +10% move equals the probability of a −10% move. Under this assumption, a $90 put and a $110 call should have identical implied volatility if they're equidistant from the money. They don't. The put trades at 32%; the call at 18%. This 14% gap is the skew.

## Why does the skew exist?

The skew reflects **three economic realities** that symmetric models ignore:

### 1. Crashes are more frequent and severe than rallies

Historical return distributions for equities are negatively skewed: extreme downside moves happen more often and with greater magnitude than equivalent upside moves. A −20% single-day crash is more common than a +20% rally. The 1987 Black Monday, the 2008 financial crisis, and the COVID crash were all spectacular downside events. Equivalent upside explosions are rarer.

Because crashes are more likely, investors rationally bid up the price of downside protection. A put that protects against a 20% drop is more valuable than a call that profits from a 20% rise—even if the two were equally likely (which they're not).

### 2. Investors are willing to pay for insurance

A pension fund holding $1 billion of equities might buy 3-month puts as a portfolio hedge. They're willing to "lose money" on the puts if the market rallies (the premium is gone, and the puts expire worthless) because the benefit of protecting against a crash far outweighs that cost. This consistent demand for downside hedging drives put prices above their "fair" level under any symmetric model.

This is analogous to buying home insurance: you expect to lose money on the policy in expectation (the insurance company profits), but you buy it anyway for protection.

### 3. Leverage constraints and dealer carry

Option dealers carry inventory. When demand for puts surges (during market turmoil or just due to normal hedging), dealers accumulate puts and must hedge them by short-selling stock. Short-selling is costly (borrow fees, margin requirements, operational friction). As a dealer accumulates more puts, the cost of hedging that inventory rises, and they bid down put prices less aggressively. This naturally supports put prices at elevated levels.

Conversely, dealers accumulate calls slowly (fewer natural sellers), so they're more willing to undercut call prices to move inventory. This pushes call IV lower.

## How skew is measured and quoted

Traders quote skew in two main ways:

**Skew volatility (or skew slope):** The implied volatility of an out-of-the-money put minus the implied volatility of an at-the-money call. If a 90 put trades at 32% IV and the 100 ATM call trades at 25% IV, the skew is 32% − 25% = 7%. Higher skew = investors are paying more for downside protection.

**Risk reversal:** The IV of a 10-delta put minus the IV of a 10-delta call. (A 10-delta option has a 10% probability of finishing in the money, so it's far out of the money.) Risk reversals are actively traded strategies that allow investors to express a view on skew without owning the underlying stock.

## Skew and volatility surfaces

Volatility doesn't vary uniformly across strikes. The relationship between strike and IV is not linear; it has a characteristic shape:

- **Skew:** Most common on equities and equity indices. Deep OTM puts are much more expensive than OTM calls. The curve slopes downward and is asymmetric (steeper on the left / put side).
- **Smile:** Common on currencies and interest rates. Both deep OTM puts and deep OTM calls are more expensive than ATM options. The curve is U-shaped, symmetric.
- **Call skew (reverse skew):** Rare and usually temporary on commodities that face supply shocks. Calls become more expensive than puts as upside events (crop failure, geopolitical disruption) are feared.

For equities, the skew is persistent. Even when implied volatility overall is low and the market is calm, the pattern holds: puts are more expensive than calls.

## Changes in skew over time and states of the world

**During calm markets (low implied vol overall):**
Skew remains steep. Puts might trade at 20% vol; calls at 12%. The absolute difference is smaller (8%), but the relative skew is just as pronounced. Investors still value crash protection.

**During turmoil (high implied vol overall):**
Skew can flatten or even reverse temporarily. Puts might trade at 80% vol; calls at 70%. Both are expensive, but the gap narrows. Why? During panic, both puts and calls are in demand—everyone is hedging, and the market is pricing existential risk. The insurance premium (skew) becomes less important because the base level of fear is so high.

**Pre-earnings or pre-event:**
Skew often increases (steepens) in the days before an earnings announcement or political event. Traders want protection for both sides of the move, but they'll pay more for downside protection. A negative earnings surprise (40% drop) is a real possibility; a positive surprise (upside move) is positive but capped.

## Trading skew

Several strategies exploit skew directly:

**Reverse skew or put-call ratio trading:** Buy the relatively cheap calls and sell the relatively expensive puts. This isolates a bet that skew will flatten (normalize toward a more symmetric distribution). If the stock stays near the money, the cheap calls will outperform the expensive puts.

**Volatility swaps:** Structured trades that allow investors to bet on whether realized volatility will exceed implied volatility. Skew affects the pricing of these swaps because the market's expectation of realized vol is embedded in skew patterns. A steep skew suggests the market expects a high probability of a crash, which raises realized vol expectations.

**Earnings straddles with skew hedging:** Buy an at-the-money straddle (call + put) before earnings, but offset the skew risk by selling the expensive OTM puts, converting the position into a call-heavy portfolio. This profits from large moves in either direction but loses money on the expensive puts, creating a more balanced risk profile.

**Skew as a macroeconomic indicator:** Steeper skew correlates with periods of financial stress, flight to quality, and market uncertainty. Trading desks use skew levels as an early-warning signal for coming volatility spikes.

## The Black-Scholes failure

The [Black-Scholes model](/black-scholes-model/) cannot produce skew. It assumes log-normal returns (symmetric distribution of log returns), which implies that puts and calls equidistant from the money should have identical implied volatility. The skew's existence is one of the clearest proofs that real market returns violate Black-Scholes' core assumptions.

To match observed skew, practitioners use:
- **Local volatility models**, which allow volatility to vary by strike and spot price.
- **Stochastic volatility models**, which treat volatility itself as random, producing realistic return distributions with fat tails and skew.
- **Jump-diffusion models**, which add discrete jumps (crashes) to continuous price moves, naturally creating skew because sudden downward jumps are more frequent.

All three approaches can be calibrated to replicate observed skew and are used to price exotic options and calculate hedging Greeks correctly.

## Skew in different asset classes

**Equities:** Steep negative skew. OTM puts significantly more expensive than OTM calls. Reflects fear of crashes and portfolio insurance demand.

**FX (currency pairs):** Skew is smaller and can go either direction. A strong currency might show call skew (speculators betting on strength). Currencies don't typically "crash" like equities (central banks intervene), so the fear premium is weaker.

**Commodities:** Skew varies by commodity and supply dynamics. Agricultural commodities might show call skew (upside surprise from crop failure) or put skew (downside surprise from glut). Energy commodities show call skew before geopolitical events.

**Fixed income / Bonds:** Bonds don't have the same skew as equities. Interest rates can rise or fall, and crashes in bond prices are less feared than equity crashes (central banks can support them).

## See also

<div class="wiki-seealso">

### Closely related

- [Implied volatility vs historical volatility](/implied-volatility-vs-historical-volatility/) — why the gap reveals skew
- [Black-Scholes assumptions limitations](/black-scholes-assumptions-limitations/) — symmetry assumption that skew breaks
- [Volatility smile](/volatility-smile/) — related pattern in other markets
- [Option](/option/) — foundational derivative whose pricing reveals skew
- [Delta](/delta/) — hedging sensitivity affected by skew

### Wider context

- [Tail risk](/tail-risk/) — the downside events skew is pricing
- [Derivatives hedging](/derivatives-hedging/) — why investors demand crash protection
- Risk management — portfolio insurance strategies that support skew

</div>
