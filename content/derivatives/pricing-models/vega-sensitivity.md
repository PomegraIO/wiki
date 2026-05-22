---
title: "Vega Sensitivity"
description: "The option Greek measuring price change per 1% volatility shift; key risk measure for options traders."
keywords:
  - vega
  - option greeks
  - volatility sensitivity
  - options trading
  - risk management
---

*[Vega](/wiki/vega/) is the [Greek](/wiki/options-greeks/) that measures how much an [option](/wiki/option/) price changes when [implied volatility](/wiki/implied-volatility/) shifts by 1 percentage point (e.g., from 20% to 21%). A call or put with high vega is sensitive to volatility moves; a trader who buys options is long vega (profits if volatility rises).*

<aside class="wiki-infobox">

| Scenario | Effect on Vega |
|---|---|
| **At-the-money (ATM) option** | Highest vega |
| **Deep in-the-money (ITM)** | Lower vega |
| **Deep out-of-the-money (OTM)** | Lower vega |
| **Short-dated option (1 day to expiry)** | Near-zero vega |
| **Long-dated option (2+ years)** | High vega |
| **Rising IV** | Increases option value (long vega profit) |
| **Falling IV** | Decreases option value (long vega loss) |
| **Numerical example** | Call vega = 0.05 means +1% IV → +$0.05/share |

</aside>

## Vega definition and intuition

An [option](/wiki/option/) price consists of:
- **Intrinsic value** (the in-the-money amount; e.g., $2 for a call with strike $100 and stock at $102)
- **Time value** (the premium above intrinsic, reflecting time to expiry and uncertainty)

Vega measures the sensitivity of time value to changes in [implied volatility](/wiki/implied-volatility/). Higher volatility means greater uncertainty, which makes options more valuable (both calls and puts become more expensive).

**Example:**
- Call option: strike $100, stock at $100 (at-the-money), 30 days to expiry
- Implied volatility: 20%
- Current price: $2.00

If implied volatility rises to 21% (all else equal):
- New price: $2.05 (roughly)
- Vega: approximately 0.05

## Why at-the-money options have highest vega

Vega peaks when an option is [at-the-money](/wiki/at-the-money/) (strike = stock price) because:

1. **Time value is greatest** — an ATM option is 100% time value (no intrinsic), so any volatility change hits pure time value.
2. **Probability of profit is highest** — small stock moves (in either direction) have the biggest impact on an ATM option's payoff, so volatility matters most.
3. **Moneyness is symmetric** — both upside and downside moves from the strike have equal value; an OTM or ITM option has asymmetric payoffs and lower vega.

An [in-the-money](/wiki/in-the-money/) call has lower vega because a lot of its value is intrinsic (the current spread between stock and strike), which doesn't change with volatility. An [out-of-the-money](/wiki/out-of-the-money/) call has lower vega because the option is less likely to finish in-the-money, so volatility changes have less impact.

## Time decay and vega decay

Vega decays as the option approaches expiry. A 90-day call has higher vega than a 10-day call (all else equal) because the 90-day option has more time value to be affected by volatility changes.

The relationship between [theta](/wiki/theta-option-greeks/) (time decay) and vega is complex:
- **Near expiry** — vega approaches zero (little time value left) and theta accelerates (the remaining time value bleeds away)
- **Early in life** — vega is high (lots of time value) and theta is smaller (time decay is slow)

A trader who buys an option early captures high vega exposure; holding it to expiry forces vega to collapse (and theta to accelerate).

## Vega as a directional bet on volatility

Long options (long call, long put) are implicitly a bet that [implied volatility](/wiki/implied-volatility/) will rise:

**Long call, vega = +0.05:**
- If IV rises 10 percentage points (e.g., 20% → 30%), the call gains roughly $0.50/share (0.05 × 10).
- This happens *even if the stock price stays flat*—the option is worth more simply because uncertainty increased.

**Short call, vega = −0.05:**
- If IV falls, the short call benefits (the seller pocketed the premium and the premium shrinks).
- Traders who sell options are betting volatility will fall or stay low.

Many traders distinguish between:
- **[Volatility](/wiki/implied-volatility/) trading** — betting on IV changes (pure vega position)
- **Directional trading** — betting on stock price moves ([delta](/wiki/delta-option-greeks/) position)

A trader can isolate vega risk by [hedging](/wiki/hedging-with-futures/) delta (using stock or [futures](/wiki/futures-contract/)), leaving pure volatility exposure.

## Vega hedging and volatility derivatives

Options desks hedge vega using:

1. **[Variance swaps](/wiki/variance-swap/)** — swap contract where one party pays fixed variance and receives realized variance. A large vega position can be hedged with a variance swap paying the same notional.

2. **[Volatility swaps](/wiki/volatility-swap/)** — simpler: one party receives fixed volatility, the other receives realized volatility. Direct vega hedge.

3. **[VIX futures](/wiki/volatility-index-futures/)** — bets on the [VIX index](/wiki/fear-index/) (equity volatility). Don't perfectly hedge options vega (because VIX is a broad index, not specific stock vega), but provide a directional hedge.

4. **Offsetting options** — sell options to offset vega from long positions. A trader long 100 calls (vega = +1.00) can sell 50 calls elsewhere to hedge vega to +0.50.

## Realized vs. implied volatility and vega profit

A trader who buys a call (long vega) profits if:
- **Implied volatility rises** — the call is worth more (vega P&L is positive)
- **Realized volatility rises** — if the trader is delta-hedged, realized moves allow frequent rebalancing at lower prices (realized vega profit)

If implied volatility is 20% but realized volatility turns out to be 30%, a delta-hedged long option position profits from the "vol disparity"—the gap between what the trader paid for volatility (20% IV) and what actually occurred (30% realized vol).

Conversely, a trader who sells options (short vega) profits if realized volatility is *lower* than the implied volatility they sold.

## Vega and leverage

High vega positions can be leveraged:
- A trader with $100k buys 10 call contracts (each covering 100 shares), gaining $1 exposure to a 1-point IV move.
- A $10 move in IV generates $10,000 in P&L—a 10% return on the initial capital (or loss, if IV falls).

The leverage is embedded in the option's time value. This is why retail investors can be devastated by IV crashes (their leveraged long option positions implode) or IV spikes (short option positions explode).

## Vega and the [volatility smile](/wiki/volatility-smile/)

Volatility is not uniform across strike prices. The **volatility smile** (or **smirk**) means different strikes have different implied volatilities. A trader holding ATM calls may have high vega, but out-of-the-money puts have different vega (and their own IV level).

Complex vega risk involves:
- **Vega exposure across strikes** — the sensitivity of the whole portfolio to a parallel shift in the IV curve
- **Vega skew** — sensitivity to changes in the shape of the smile (OTM puts becoming more or less volatile than ATM calls)

A trader may be hedged to overall vega but exposed to vega-skew risk.

## Vega in portfolio management

A bond-fund manager or equity-fund manager may monitor vega indirectly:
- **Bond funds with embedded options** — [callable bonds](/wiki/callable-bond/) have negative vega (as rates fall, interest-rate volatility falls, and the callable feature becomes more likely to be exercised). The fund manager must understand this risk.
- **Equity funds holding [convertible bonds](/wiki/convertible-bond/)** — convertibles are vega-positive (higher stock volatility increases the value of the embedded [call option](/wiki/call-option/)).

For most buy-and-hold investors, vega is not a primary concern. For derivatives traders and dynamic portfolio managers, it is critical.

<div class="wiki-seealso">

### Closely related
- [Vega](/wiki/vega/) — the Greek itself (brief entry)
- [Options Greeks](/wiki/options-greeks/) — broader framework (delta, gamma, theta, rho)
- [Implied volatility](/wiki/implied-volatility/) — what vega measures sensitivity to
- [Volatility smile](/wiki/volatility-smile/) — non-uniform IV across strikes
- [Delta option Greeks](/wiki/delta-option-greeks/) — directional sensitivity (compare to vega)

### Wider context
- [Option](/wiki/option/) — the instrument vega applies to
- [Volatility swap](/wiki/volatility-swap/) — vega hedging instrument
- [Variance swap](/wiki/variance-swap/) — alternative vega hedge
- [Realized volatility](/wiki/historical-volatility/) — actual moves vs. implied
- [Hedging with futures](/wiki/hedging-with-futures/) — risk management strategy

</div>
