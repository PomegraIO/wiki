---
title: "Synthetic Option"
description: "Replicating option payoff profiles using combinations of underlying stock and bonds or other derivatives."
keywords:
  - synthetic option
  - synthetic long
  - synthetic short
  - put-call parity
---

*A **synthetic option** is a portfolio of simpler instruments—stock, bonds, or other derivatives—that replicates an [option's](/wiki/option/) payoff. Synthetic long stock (buy a [call](/wiki/call-option/), sell a [put](/wiki/put-option/)) mimics owning stock; [put-call parity](/wiki/put-call-parity/) relates these synthetic relationships.*

<aside class="wiki-infobox">

| Position | Components | Net Payoff |
|----------|-----------|-----------|
| **Synthetic long stock** | Buy call + sell put (same strike) | Same as owning stock |
| **Synthetic short stock** | Sell call + buy put (same strike) | Same as shorting stock |
| **Synthetic long call** | Buy stock + buy put | Same as owning call |
| **Synthetic short put** | Short stock + sell call | Same as selling put |
| **Risk reversal** | Buy call + sell put (different strikes) | Leveraged directional bet |

</aside>

## Put-call parity: the foundation of synthetic relationships

**[Put-call parity](/wiki/put-call-parity/)** is the mathematical relationship binding calls, puts, stock, and bonds at a given strike and expiration:

**Call Price − Put Price = Stock Price − Present Value of Strike**

Rearranging: **Call = Put + Stock − Bond**

This means a **synthetic long call** equals owning stock *and* buying a [protective put](/wiki/protective-put/) (downside insurance). If you buy a stock at $100 and buy a $100 put, you've locked in a floor—you own the stock, but if it crashes to $50, you exercise the put and sell at $100. This synthetic call position has the same payoff as owning the call outright. The parity holds (approximately) in efficient markets; violations create [arbitrage](/wiki/arbitrage-pricing-theory/) opportunities for traders willing to buy cheap puts and sell expensive calls.

## Synthetic long stock: buying a call and selling a put

The **synthetic long** is the most common synthetic position. Buy a 6-month $100 call and sell a 6-month $100 put on the same stock. At expiration:
- If the stock is at $110: call is in-the-money (+$10), put expires worthless (you sold it, so you gain the premium). Net: +$10 (same as owning the stock at $100).
- If the stock is at $90: call expires worthless (you lose the cost), put is in-the-money (you're forced to buy at $100), net cost $100 (same as owning the stock at $100).

This replicates owning the stock but requires no upfront capital (the call premium and put premium offset if the options are fairly priced). Traders use this when stock lending is unavailable or when borrowing is expensive—a synthetic long costs the same as stock but avoids short borrow fees. Hedge funds execute synthetics to maintain portfolio deltas while reducing balance-sheet usage.

## Synthetic short stock: selling a call and buying a put

The inverse: sell a 6-month $100 call and buy a 6-month $100 put. At expiration:
- If the stock is at $110: the call is in-the-money (buyer exercises, you deliver stock at $100, losing $10). The put expires worthless. Net: −$10 (same as shorting at $100).
- If the stock is at $90: the call expires worthless (you profit from the premium). The put is in-the-money (you exercise, buying at $100). Net: you bought at $100, sold (implicitly) at $100, net zero (same as shorting at $100).

Synthetic shorts are used to establish short positions without borrowing shares (which can be hard to borrow in illiquid stocks). However, they still require put premium capital upfront, so they're not cheaper than stock short-selling, just an alternative.

## Synthetic calls and puts: owning stock + puts

A **synthetic long call** = buy stock + buy put (same strike). This is a [protective put](/wiki/protective-put/)—you own the stock and insure it with a put. If the stock crashes below the put strike, you exercise the put and sell at the strike price, capping losses. If the stock rises, you keep the gains. The cost is the put premium. This synthetic call has the same payoff as buying the call outright (you have unlimited upside and protected downside), but the mechanics are different—one uses puts and stock, the other uses a call.

Similarly, **synthetic short call** = short stock + short put. You've shorted the stock and accepted a put being exercised on you, which forces you to buy at the strike. This has the payoff of a short call (limited upside, unlimited downside risk if you short naked). These less common synthetics are mainly used in hedge fund replication or when certain instruments are unavailable.

## Risk reversals: synthetic leverage and directional bets

A **risk reversal** (also "collar" without long stock) = buy a call at a higher strike + sell a put at a lower strike. Example: buy a $105 call and sell a $95 put, both 6-month expiration. This positions you as bullish: you benefit from upside (buy the call), hedge downside partially (the put you sold limits your loss), but you're short the $95 put (exposed to being forced to buy at $95 if stock crashes). Risk reversals are used to express a bullish view with reduced premium cost (sold put finances the bought call). They're popular in forex and currency options, where traders use them to take directional bets cheaply.

## Volatility implications and dynamic replication

A synthetic long call (buy stock + buy put) has the same *payoff* as a call at expiration, but not the same *risk profile* before expiration. If [implied volatility](/wiki/implied-volatility/) spikes 10%, the put you own appreciates while the stock may decline—the gains offset. But if you own a call outright, the call appreciates massively because of [gamma](/wiki/gamma-option-greeks/) and [vega](/wiki/vega-option-greeks/). This is why synthetics are useful for **replication** in [dynamic hedging](/wiki/dynamic-hedging-algorithm/)—a dealer who sells a call can hedge it by owning stock (and borrowing to finance it at the risk-free rate), rebalancing as [delta](/wiki/delta-option-greeks/) changes. The synthetic hedge is cheaper than buying a call to hedge (because the stock's delta changes more predictably), but it requires constant rebalancing.

## Arbitrage: when synthetics fail to hold parity

If a call trades at $7, the put at $3, the stock at $100, and [interest rates](/wiki/interest-rate/) are 5% (2.5% to expiration), then [put-call parity](/wiki/put-call-parity/) implies: $7 − $3 = $100 − PV($100) = $100 − $97.5 = $2.5. But we observe $4, so the call is overpriced relative to the synthetic. An arbitrageur shorts the call ($7), buys the put ($3), buys the stock ($100), and borrows $97.5 at 5%. At expiration, the position is flat, profit is $7 − $3 − $100 + $97.5 = $1.50 (risk-free). In efficient markets, these arbitrages are closed by traders in microseconds, so parity usually holds.

## Practical use: hedge funds and market-makers

[Market-makers](/wiki/market-makers/) who trade options routinely use synthetics to hedge. If they sell a call, they buy stock + borrow to delta-hedge. If volatility is expensive, they might buy stock + sell puts instead (synthetic call hedge) to save on put premium. Hedge funds use synthetics to maintain [notional exposure](/wiki/enterprise-value/) with less capital. A leveraged long position (buy stock on margin) can be replicated with synthetic longs (low capital, same delta), freeing capital for other strategies. Equity derivatives desks at investment banks generate profits by scalping parity violations—continually buying cheap synthetics and selling expensive options, locking in small arbitrage spreads.

---

<div class="wiki-seealso">

### Closely related
- [Put-Call Parity](/wiki/put-call-parity/) — Relationship tying calls, puts, stock, and bonds
- [Call Option](/wiki/call-option/) — Right to buy underlying at strike price
- [Put Option](/wiki/put-option/) — Right to sell underlying at strike price
- [Protective Put](/wiki/protective-put/) — Buying put to insure stock holdings

### Wider context
- [Dynamic Hedging](/wiki/dynamic-hedging-algorithm/) — Continuously rebalancing to maintain delta hedge
- [Options Greeks](/wiki/options-greeks/) — Delta, gamma, vega sensitivity of derivatives
- [Arbitrage](/wiki/arbitrage-pricing-theory/) — Exploiting parity violations between synthetics and options
- [Option Pricing](/wiki/black-scholes-model/) — Models for valuing options and detecting mispricing

</div>
