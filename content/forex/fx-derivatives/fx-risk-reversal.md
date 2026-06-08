---
title: "FX Risk Reversal"
description: "A directional volatility strategy that measures the premium gap between out-of-the-money calls and puts at equal delta, revealing market skew."
keywords:
  - fx risk reversal
  - currency option skew
  - call-put spread fx
  - delta-neutral volatility
  - currency derivatives
image: "/svg/forex.svg"
---

*An **FX risk reversal** (or **risk reversal**) is a directional volatility trade that simultaneously sells an [out-of-the-money](/in-the-money/) put and buys an [out-of-the-money](/in-the-money/) call at equal [delta](/delta/) strikes, creating a zero or low-premium structure that profits when implied volatility in one direction exceeds the other. It is equally a gauge of market skew — a measure of how much traders believe the currency will move in one direction rather than staying flat, and where the marginal [option premium](/option-premium/) lies across the [strike-price](/strike-price/) ladder.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Risk Reversal — key facts</div>

<img src="/svg/forex.svg" alt="An editorial mark for foreign exchange instruments." />

<div class="wiki-infobox-caption">A skew-sensitive trade that reveals where currency premium is most expensive.</div>

|   |   |
|---|---|
| **What it is** | Long a call and short a put at equal delta, creating a bullish (or bearish) directional position in volatility space |
| **Also called** | Call spread, risk reversal, skew trade, volatility directional |
| **Typical delta** | 25-delta or 10-delta calls and puts (equidistant from at-the-money in probability terms) |
| **Cost structure** | Often zero or minimal premium if strikes are chosen symmetrically |
| **Payoff driver** | Directional realized [volatility](/currency-volatility/), realized [skew](/volatility-smile/), and [gamma](/gamma/) tail risk |
| **Key users** | [Hedge funds](/hedge-fund/), options traders, corporates, central banks |

</aside>

## The mechanics of a simple reversal

Suppose EUR/USD trades at 1.0900, and the market is pricing 25-delta calls at 80 basis points of [implied volatility](/implied-volatility/) while 25-delta puts are at 85 basis points. A trader buys the call (pays a small premium for upside) and sells the put (receives a smaller premium for downside), netting a small credit or minimal debit.

If EUR/USD rallies sharply, the call gains value faster than the put loses value — the call holder profits. If the currency collapses, the put seller is hit hardly. The payoff is asymmetrical: unlimited upside profit, capped downside profit (the premium collected), and large downside loss below the put strike.

The trade works best when the trader believes:
- The currency will move strongly in one direction (the call direction).
- Realized [volatility](/currency-volatility/) will exceed the premium paid for that directional move.
- The market is overpricing the [downside](/volatility-smile/) (the put) relative to the [upside](/in-the-money/) (the call).

Alternatively, a *reverse* risk reversal — short call, long put — flips the bias, betting on depreciation or downside volatility.

## Skew and the basis of the trade

In theory, a currency's volatility curve should be symmetric: a 25-delta call and a 25-delta put should have equal [implied volatility](/implied-volatility/), since the currency is equally likely to move 2% up or 2% down. But markets routinely price them differently. This difference is **skew** or **smile** — and risk reversals are the trade that directly bets on skew.

Why does skew exist? Several reasons:

**Crash risk and hedging demand.** During episodes of geopolitical tension or rising rates, traders demand cheap put protection. They're willing to pay high [implied volatility](/implied-volatility/) for puts, pushing put prices up relative to calls. A USD appreciation scare drives CHF puts expensive relative to CHF calls — capital flows to safety bid the currency and its downside hedges simultaneously.

**Central-bank jawboning.** When a central bank signals rate hikes, the currency tends to rally, and traders shift to buying call protection instead of puts. Calls become expensive relative to puts, creating a positive skew (calls trade rich).

**Carry traders and one-way bets.** Systematic carry traders consistently long high-yielding currencies (like AUD or NZD). Their hedging bias — they all want downside protection — makes puts expensive. AUD puts trade richer than calls, creating negative skew (puts expensive).

**Volatility regime.** In low-volatility "risk-on" environments, puts are cheap and calls are expensive. In stressed "risk-off" regimes, the opposite: puts are expensive and calls are cheap.

## Using reversals as a skew gauge

Central banks, options brokers, and hedge funds track *risk reversal levels* as a barometer of sentiment. A large positive reversal (calls much more expensive than puts) suggests the market is bracing for appreciation. A large negative reversal (puts much more expensive) suggests depreciation fears.

In practice, a trader might buy the 25-delta call and sell the 25-delta put, and the *premium difference* (or the *cost* if the call is more expensive) becomes the price of that directional skew bet. When skew narrows, the position loses value. When skew widens in your favor, you profit — even if the currency barely moves.

This makes reversals a favorite of **relative-value** traders. They don't need the currency to actually move; they just need the market's expected skew to change.

## Real-world example: USD/JPY crisis skew

During a sharp dollar rally, USD/JPY calls (betting on further dollar strength) become expensive relative to puts. Traders sell this expensive call skew and buy the cheaper put skew, initiating a short reversal (bearish on the dollar). If the rally exhausts and the market begins to price in dollar weakness, that skew inverts — calls cheapen, puts cheapen even more or become expensive — and the short reversal position profits. The currency might still be up, but skew profit overwhelms spot loss.

Conversely, when the yen strengthens and panic selling hits, JPY puts become extremely expensive and calls cheap. A long reversal (bullish on the dollar, betting that the yen panic is overdone) shorts the expensive put skew and longs the cheap call skew. If the panic subsides, skew normalizes and the position profits.

## The gamma trap

Risk reversals carry significant [gamma](/gamma/) risk — the cost of protecting yourself dynamically if the market moves against you. A long call / short put reversal has positive gamma: as the currency rallies, the long call profits and the short put loses less (it's further out-of-the-money). But if the currency collapses, gamma works in reverse: the short put suffers exponentially, and the long call expires worthless. A trader must manage this dynamic hedging burden or risk catastrophic loss if [volatility](/currency-volatility/) spikes and the currency reverses.

## Reversals in correlation space

In [currency-volatility](/currency-volatility/) markets with multiple pairs, reversals can be stacked. A trader might be long USD risk reversals (bullish dollar skew) across EUR/USD, GBP/USD, and AUD/USD simultaneously, betting that the dollar skew across the board will steepen. This is a **USD skew long** — a higher-level directional play on the dollar's perceived safety bid.

## See also

<div class="wiki-seealso">

### Closely related

- [Delta](/delta/) — the strike-selection criterion for matched calls and puts
- [Implied volatility](/implied-volatility/) — the input that determines call and put option premiums
- [Volatility smile](/volatility-smile/) — the skew curve across strike prices that risk reversals isolate
- [Gamma](/gamma/) — the dynamic hedging cost as the currency moves
- [Option premium](/option-premium/) — the cost structure that determines reversal profitability

### Wider context

- [Hedge fund](/hedge-fund/) — professional managers who run systematic reversal strategies
- [Currency volatility](/currency-volatility/) — the macro regime driving skew shifts
- [Theta](/theta/) — time decay, which risk reversals gradually lose

</div>
