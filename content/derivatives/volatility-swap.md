---
title: "Volatility Swap"
description: "A volatility swap is a derivative contract that exchanges realized volatility for implied volatility, allowing traders to bet directly on volatility levels."
keywords:
  - volatility swap
  - realized volatility
  - volatility bet
  - derivatives
  - volatility trading
image: "https://picsum.photos/seed/volatility-swap/900/600"
---

*A **volatility swap** is a [swap](/swap) contract where one party bets that realized [volatility](/historical-volatility) will exceed a predetermined strike (the swap rate), while the other party takes the opposite side. Unlike [options](/option), which have optionality (the right but not obligation), volatility swaps create symmetric payoffs: both parties have obligations based on how realized [volatility](/historical-volatility) compares to the strike. Volatility swaps are used by traders to express pure volatility views independent of direction.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Volatility Swap — key facts</div>

<img src="https://picsum.photos/seed/volatility-swap/900/600" alt="Realized vs. implied volatility comparison" />

<div class="wiki-infobox-caption">Vol swaps bet on realized volatility outcomes.</div>

|   |   |
|---|---|
| **Payoff** | Notional × (realized vol − strike vol) |
| **Strike vol** | Implied volatility at initiation |
| **Realized vol** | Actual stock volatility over term |
| **No optionality** | Symmetric payoff both directions |
| **Direction-neutral** | Long vol or short vol; no delta |
| **Convexity** | Different from variance swaps |
| **Settlement** | Cash settlement at maturity |
| **Hedging use** | Hedge against volatility changes |
| **Speculation** | Pure volatility bets |
| **Liquidity** | Lower than options; mostly OTC |

</aside>

## How volatility swaps work

A trader believes [implied volatility](/implied-volatility) at 20% is too low; realized [volatility](/historical-volatility) will exceed 25%. The trader enters a 1-year volatility swap with a counterparty:

**Terms:**
- Notional: $100,000
- Strike volatility: 20%
- Realized volatility (measured at expiration): X%

**Payoff at maturity:**
If realized volatility is 28%:
- Payoff = $100,000 × (28% − 20%) = $800,000

If realized volatility is 18%:
- Payoff = $100,000 × (18% − 20%) = −$200,000

The trader gains if realized > strike; loses if realized < strike.

## Realized vs. implied volatility

**[Implied volatility](/implied-volatility)** is the market's forecast of future [volatility](/historical-volatility) at option initiation.

**Realized [volatility](/historical-volatility)** is what actually occurs over the contract's life.

Volatility swaps bet on the gap: if you believe the market overestimates future volatility, you sell realized volatility (bet it will be lower than implied).

## Advantages vs. options

Options are complex: they have [delta](/delta), [gamma](/gamma), [theta](/theta), [vega](/vega). Volatility swaps are pure volatility bets with no directional exposure and no time decay.

Buying a volatility swap (long realized vol) is simpler than buying a straddle (buy call and put), which also has gamma and theta complications.

## Strike determination

The strike is typically set at the [implied volatility](/implied-volatility) at initiation (par value = 0 to both parties). But strikes can be negotiated; a trader might buy realized vol at a strike of 18% (lower than the current implied of 20%), accepting less upside for protection if realized vol falls.

## Variance swaps

Related but distinct are **variance swaps**, which pay on the square of volatility (variance). Variance swaps have different convexity than volatility swaps and are more sensitive to extreme moves.

## Use cases

**Hedging:** A portfolio manager long volatility exposure (short gamma) can hedge via long realized volatility swap.

**Speculation:** A trader bullish on [volatility](/historical-volatility) buys realized vol to profit if [volatility](/historical-volatility) spikes.

**Relative value:** Buy realized vol at 20 strike, sell another volatility swap at 25 strike, betting realized vol will settle between them.

## Counterparty risk

Volatility swaps are OTC contracts with counterparty risk. The seller must pay if realized volatility exceeds the strike by a large amount. Some swaps require collateral or are cleared.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — general contract structure
- [Historical volatility](/historical-volatility/) — realized vol measurement
- [Implied volatility](/implied-volatility/) — strike benchmark
- [Variance swap](/volatility-swap/) — related; pays on variance
- VIX — implied vol index

### Strategies and comparisons

- Straddle — alternative vol bet via options
- Strangle — alternative vol bet
- Gamma scalping — managing vol exposure
- [Volatility trading](/volatility-smile/) — pure vol plays

### Pricing

- [Volatility smile](/volatility-smile/) — affects option pricing
- [Volatility term structure](/volatility-smile/) — near vs. far term vol
- [Mean reversion](/stock-market/) — vol tends to revert

### Deeper context

- [Derivative](/option/) — the family of instruments
- [Risk management](/hedge-fund/) — volatility hedging
- [OTC market](/stock-market/) — where swaps trade

</div>
