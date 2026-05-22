---
title: "Vega (Option Greeks)"
description: "The sensitivity of an option's price to changes in underlying asset volatility, measuring the rate of price change per 1% change in volatility."
keywords:
  - vega option greek
  - options volatility sensitivity
  - implied volatility
  - vega hedging
---

*The **Vega** (one of the [option Greeks](/wiki/options-greeks/)) measures the sensitivity of an option's price to changes in the [implied volatility](/wiki/implied-volatility/) of the underlying asset. Specifically, vega quantifies the dollar change in option price for each 1% change in volatility. Higher volatility increases the value of both calls and puts (because wider price swings create greater upside potential for long options), so vega is always positive for both option types.*

<aside class="wiki-infobox">

| Item | Detail |
|---|---|
| **Definition** | Change in option price per 1% change in implied volatility |
| **Symbol** | ν (Greek letter nu, pronounced "vega" colloquially) |
| **Sign** | Always positive for both calls and puts |
| **Magnitude** | Highest for at-the-money options; declines as options go deep ITM or OTM |
| **Time dependence** | Vega is highest for medium-term options; declines for very short or very long dated |
| **Relationship** | Higher vega = higher option value sensitivity to volatility changes |
| **Practical use** | Volatility traders, portfolio hedging, options risk management |
| **Units** | Dollar change per 1% volatility; sometimes expressed as "vega per percent" |

</aside>

## How vega works

Imagine a stock trading at $100 with a $100 call option expiring in 3 months, priced at $5. If the option's vega is 0.20, then a 1% increase in implied volatility (from, say, 20% to 21%) will increase the option's price by approximately $0.20, to $5.20.

The economic logic is straightforward: higher volatility means the underlying asset has a wider range of likely outcomes at expiration. For a call option buyer, this is beneficial—a wider range of outcomes increases the probability of large gains (upside surprise). Similarly, a put option buyer benefits from volatility: wider downside potential increases the value of downside insurance. Conversely, option writers (sellers) face larger potential losses in a volatile environment, so they charge higher premiums—reflected in higher option prices.

This contrasts with the intuition of stock investing: for equity holders, volatility is unwelcome because it increases downside risk. But for optionality (the right, not obligation, to buy or sell), volatility is an asset—it increases the value of the embedded option.

## Vega across the Greeks

Vega is one of five key option Greeks:
- **Delta**: Sensitivity to underlying price changes.
- **Gamma**: Rate of change of delta (convexity).
- **Vega**: Sensitivity to volatility changes.
- **Theta**: Sensitivity to time decay (negative for long options).
- **Rho**: Sensitivity to interest rate changes.

Each Greek measures a different risk dimension. A portfolio manager hedging options must monitor all five. For example, a short call option position has:
- Negative delta (loses if stock rises).
- Negative gamma (delta becomes more negative as stock rises, increasing losses).
- Negative vega (loses if volatility rises, increasing the call's value).
- Positive theta (gains from time decay, as the option loses value).
- Negative rho (loses if rates rise, increasing the option's value).

Hedging such a position requires buying delta, reducing gamma exposure (e.g., buying back some of the short call), reducing vega exposure (e.g., buying volatility), and accepting the theta decay as a cost of leverage.

## Vega's relationship to moneyness and time to expiration

**At-the-money (ATM) options** have the highest vega because the outcome is most uncertain; a 1% volatility change has a big impact on the probability of finishing in or out of the money. For example, a $100 call on a stock at $100 has vega ~0.20; a $110 call on the same stock has vega ~0.05.

**Deep in-the-money or out-of-the-money** options have low vega. If a call is $20 in the money ($100 strike, $120 stock), raising volatility slightly does not change its value much—it is likely to finish in the money regardless. Similarly, a far-out-of-the-money call has low vega.

**Time to expiration** affects vega in a nonlinear way. Options with 3–6 months to expiration typically have the highest vega (most uncertainty, biggest volatility sensitivity). Very short-dated options (expiring in days) have low vega because volatility has little time to matter. Very long-dated options also have moderate vega because the discount rate and long-term growth rate matter more than short-term volatility.

## Implied volatility and vega

**Implied volatility** is the market's expectation of future realized volatility, backed out from option prices using models like Black-Scholes. When implied volatility is high (say, 40%), options are expensive, reflecting expectations of large price moves. When implied volatility is low (say, 15%), options are cheap.

Vega's practical importance lies in volatility trading. Traders can:

1. **Buy volatility** (by buying calls and puts, or straddles/strangles): If you expect volatility to rise, you profit from vega exposure. As volatility rises, your option position gains value beyond the underlying asset's price move.

2. **Sell volatility** (by selling calls and puts, or short straddles): If you believe implied volatility is elevated and will decline, you can sell options (pocket the premium) and profit if volatility drops and the options lose value.

3. **Volatility arbitrage**: Compare implied volatility (from option prices) to expected realized volatility (from historical data or models). If implied volatility is much higher than realized, sell options (sell volatility). If implied is much lower, buy options.

## Vega and the [VIX](/wiki/fear-index/)

The **VIX** (Volatility Index) is a market gauge of implied volatility, derived from S&P 500 index options. When the VIX spikes (e.g., from 15 to 30), implied volatility has risen sharply, and all long option positions benefit from positive vega exposure. Portfolio managers holding index put options for tail-risk hedging see their hedge's value rise with the VIX.

Conversely, when the VIX collapses (from 30 to 15), long option positions suffer from negative vega realizations (volatility contraction) even if the underlying index is flat.

## Vega hedging and gamma scalping

**Vega hedging** involves offsetting volatility exposure. A portfolio manager with a large short option position (short vega) might buy volatility (e.g., long straddle) to hedge. The long straddle has positive vega, offsetting the short call's negative vega.

**Gamma scalping** is a dynamic hedging strategy where a dealer:
1. Sells an option (receives premium, goes short vega).
2. Dynamically buys and sells the underlying to hedge delta.
3. Profits from the difference between realized volatility (actual price moves) and implied volatility (the premium received).

Gamma scalping works best when realized volatility exceeds implied volatility—the dealer profits from the difference, collecting a volatility spread. If realized volatility drops below implied, the dealer loses.

## Practical limitations

Vega assumes that volatility changes uniformly across all strike prices and times to expiration, which is not true in practice. The **volatility surface** and **volatility smile** show that implied volatility varies by strike and expiration. OTM puts often have higher implied volatility than ATM options (reflecting tail-risk hedging demand), so a 1% change in overall volatility does not hit all options equally.

Also, vega is a linear approximation (like all Greeks). Large volatility changes require **vega gamma** (the convexity of vega) to be added back for accuracy.

<div class="wiki-seealso">

### Closely related
- [Options Greeks](/wiki/options-greeks/) — Framework encompassing all Greeks
- [Delta (Option Greeks)](/wiki/delta-option-greeks/) — Sensitivity to underlying price
- [Gamma (Option Greeks)](/wiki/gamma-option-greeks/) — Sensitivity of delta to price
- [Implied Volatility](/wiki/implied-volatility/) — What vega measures sensitivity to

### Wider context
- [Option Pricing](/wiki/option/) — Valuation framework using vega
- [Black-Scholes Model](/wiki/black-scholes-model/) — Model for computing Greeks
- [Volatility Index (VIX)](/wiki/fear-index/) — Market gauge of implied volatility
- [Volatility Hedging](/wiki/volatility-hedging/) — Use of vega in portfolio protection

</div>
