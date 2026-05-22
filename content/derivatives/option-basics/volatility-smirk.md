---
title: "Volatility Smirk"
description: "Asymmetric implied volatility across strike prices; typically higher for out-of-the-money puts than calls, reflecting skew in return distributions."
keywords:
  - implied volatility
  - option skew
  - strike prices
  - volatility surface
---

*A **volatility smirk** is a departure from flat [implied volatility](/wiki/implied-volatility/) across option strike prices. Specifically, it is the asymmetric pattern where [out-of-the-money](/wiki/out-of-the-money/) put options (lower strikes) have higher implied volatility than [out-of-the-money](/wiki/out-of-the-money/) calls (higher strikes), reflecting market's greater fear of sharp downside moves than upside moves. The smirk is distinct from a [volatility smile](/wiki/volatility-smile/), which is symmetric around the [at-the-money](/wiki/at-the-money/) strike.*

<div class="wiki-hatnote">
For the symmetric variant, see [Volatility Smile](/wiki/volatility-smile/). For the behavior of volatility surfaces across multiple expirations, see [FX Volatility Surface](/wiki/fx-volatility-surface/).
</div>

<aside class="wiki-infobox">

| Feature | Description |
|---|---|
| **Shape** | Downward-sloping skew; put IV > call IV at same distance OTM |
| **Typical Pattern** | ATM IV ~20%; OTM put IV ~25%; OTM call IV ~18% |
| **Cause** | Negative skew in returns; tail risk and crash fears |
| **Market Effect** | Puts are expensive relative to calls; hedging demand drives skew |
| **Quantification** | Skewness of underlying return distribution; measured in [delta](/wiki/delta/)-adjusted IV |
| **Trading Use** | Sell OTM puts, buy OTM calls to profit from mean-reversion in skew |

</aside>

## Why the smirk exists: tail risk and hedging demand

Equity markets exhibit *negative skew*—the probability of a sharp downside crash is asymmetrically higher than a comparable upside spike. The 1987 crash, the 2008 financial crisis, and the 2020 March panic were all sudden, violent downside moves. By contrast, sustained equanimity or slow grinding upside is more common than a one-day 20% jump.

This asymmetry is rational: companies can go bankrupt (downside is capped at -100%), but gains are unlimited. The distribution of returns is not Gaussian; it has a left tail.

Investors hedge by buying out-of-the-money puts. A portfolio manager with a $10M stock position might buy puts at a 10% lower strike to protect against a crash. This consistent demand for downside protection drives put prices higher (and implied volatility higher) relative to calls, which are less frequently purchased for protection and more often used for speculation.

The smirk is thus the market's pricing of tail risk and hedging demand—the cost investors are willing to pay to sleep at night.

## Distinguishing the smirk from the smile

A **[volatility smile](/wiki/volatility-smile/)** is a U-shaped curve: both OTM puts and OTM calls have higher IV than ATM options. This pattern is common in foreign exchange and some commodity markets, where both extreme strengthening and extreme weakening of a currency or price are feared.

A **volatility smirk** is asymmetric: the downward slope is steeper, and puts are much more expensive than calls. This pattern dominates equity markets.

The reason is nuanced. In FX markets, both extreme currency moves are plausible (a currency can spike or crash with similar probability). In equities, downside is more feared, so the skew is pronounced.

## Quantifying skew: delta-adjusted IV vs. moneyness

Implied volatility varies by [moneyness](/wiki/moneyness/) (how far OTM an option is) and by [delta](/wiki/delta/). A common way to express skewness is to plot IV against delta:
- ATM calls and puts have delta of ~0.50 and 0.50 respectively.
- A 25-delta put is further OTM; a 25-delta call is further OTM in the opposite direction.
- If the 25-delta put IV is 5 percentage points higher than the 25-delta call IV, there is a pronounced smirk.

This delta-weighted approach controls for the different strikes at which puts and calls reach the same delta, isolating the skew effect.

## The lifecycle of the smirk: contraction and expansion

The smirk is not static. It expands and contracts depending on market regime:

**Low-volatility, optimistic markets.** When the VIX is low (say, 12-14%) and equity returns are positive, the smirk flattens. Investors are less concerned about tail risk; demand for puts moderates; put IV falls closer to call IV. In extreme bull markets, the smirk can even invert, with calls more expensive than puts (a "reverse skew"), though this is rare.

**High-volatility, fearful markets.** When the VIX is elevated (say, 25-35%) or there is acute geopolitical risk, the smirk steepens dramatically. Hedging demand surges; puts become extremely expensive relative to calls. In March 2020, the skew was at extreme levels—30-delta puts were trading 3x or more the IV of 30-delta calls.

**Earnings and event risk.** Before major corporate earnings announcements, the smirk typically widens as investors buy put protection against negative surprises. After the earnings are released, volatility collapses and the skew normalizes.

## The smile-to-smirk transition: liquidity and jumps

In some markets and periods, IV curves look more like smiles than smirks. The transition depends on the perceived tail-risk distribution:
- **Equity index options** (SPX, ES) tend toward a pronounced smirk.
- **Single-stock options** (AAPL, TSLA) sometimes have a smile shape, because single stocks can spike on good news (e.g., a major contract) as easily as crash.
- **Currency options** often show a smile because both directions of currency move are plausible.

The [beta](/wiki/beta/) of the underlying also matters: a high-beta, high-idiosyncratic-volatility stock may have a flatter skew than the market overall, because the stock's volatility is high in both directions.

## Trading the skew: selling puts, buying calls

A trader who believes the skew is *too steep* (puts overpriced relative to calls) might:
- **Sell OTM puts** (collecting high premium) and **buy OTM calls** (paying lower premium for upside), creating a [risk reversal](/wiki/collar/).
- Or, **sell put spread**, exploiting the steep IV gradient between further and nearer OTM puts.

If markets recover and the skew flattens, the put IV falls and the short put position profits. However, this strategy is a bet on normalization and carries tail risk itself—if the market crashes, the short puts blow up.

Conversely, a trader who believes the skew will steepen (or hedges an equity portfolio) might **buy OTM puts** and reduce them by **selling OTM calls**, accepting lower protection (the sold calls cap upside) but paying less for the downside insurance.

## Skew across expirations: term structure of skew

The skew is stronger in near-dated options and flattens in longer-dated expirations. A near-term put (1 month to expiration) might be 8 IV points above the call; a 6-month put might be only 3 IV points above the call.

This term structure exists because:
- **Hedging demand is concentrated in the near term.** Portfolio managers buy 1-3 month puts to protect against imminent crashes.
- **Long-term distributions are less skewed.** Over a 6-12 month horizon, the law of large numbers moderates; mean reversion and economic cycles attenuate tail risks.
- **Roll dynamics.** As near-term options expire, skew flattens; fresh far-dated options have less skew.

## Vol-of-vol and the stability of the smirk

The smirk is not perfectly stable. "Volatility of volatility" (vol-of-vol) is the extent to which IV itself fluctuates. A stable smirk has low vol-of-vol; a whippy market has skew that gyrates day-to-day.

In markets with stable skew, skew traders can size positions confidently. In choppy markets, the skew can reverse or amplify unexpectedly, making skew trades risky without dynamic hedging.

## Relationship to realized skewness and risk management

The smirk exists because realized returns have negative skewness. A value manager comparing option-implied skew to realized skewness of the underlying can identify mispricings:
- If realized skew is more negative than implied skew suggests, puts are underpriced (a value opportunity).
- If realized skew is less negative than implied skew, puts are overpriced (a fade opportunity).

Large institutional portfolios monitor this continuously, adjusting hedging ratios based on the skew term structure.

<div class="wiki-seealso">

### Closely related
- [Volatility Smile](/wiki/volatility-smile/) — The symmetric variant of skewed volatility surfaces.
- [Implied Volatility](/wiki/implied-volatility/) — The core concept; smirk is its cross-strike behavior.
- [Options Greeks](/wiki/options-greeks/) — [Vega](/wiki/vega-option-greeks/) measures sensitivity to IV; [gamma](/wiki/gamma-option-greeks/) is affected by the skew structure.
- [Out of the Money](/wiki/out-of-the-money/) — OTM options, where the smirk is most pronounced.
- [Volatility Surface](/wiki/fx-volatility-surface/) — The 3D space of IV across strikes and expirations; the smirk is one slice.

### Wider context
- [Option](/wiki/option/) — The instrument; smirk is an option-pricing phenomenon.
- [Black Scholes Model](/wiki/black-scholes-model/) — Assumes constant volatility; the smirk reveals the model's limitations.
- [Risk Management](/wiki/operational-risk/) — Understanding skew is critical for hedging portfolio tail risk.
- [Tail Risk](/wiki/tail-risk/) — The economic phenomenon underlying the smirk.

</div>
