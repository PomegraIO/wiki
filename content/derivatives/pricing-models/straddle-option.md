---
title: "Straddle"
description: "A long call and put at the same strike price and expiration, betting on large price volatility regardless of direction."
keywords:
  - straddle option
  - long straddle
  - volatility trade
  - option strategy
  - call put strategy
---

***A straddle** is an options strategy combining a long [call option](/wiki/call-option/) and a long [put option](/wiki/put-option/) at the same [strike price](/wiki/strike-price/) and expiration date. The trader profits if the underlying price moves sharply in either direction, betting that [volatility](/wiki/volatility-smile/) is higher than the market's implied price.*

<div class="wiki-hatnote">
For a similar but tighter strategy, see [Strangle](/wiki/strangle-option/). For the inverse (short straddle), see [Iron condor](/wiki/iron-condor/).
</div>

<aside class="wiki-infobox">

| Attribute | Detail |
|-----------|--------|
| **Components** | 1 long call + 1 long put, same strike & expiration |
| **Max profit** | Unlimited (call side) if price rises sharply; large (put side) if crashes |
| **Max loss** | Premium paid for both options |
| **Breakeven** | Strike ± (call premium + put premium) |
| **Best scenario** | Large move in either direction (high realized volatility) |
| **Worst scenario** | Price stays near strike (volatility low, theta decay) |
| **Greeks** | Positive vega, negative theta, zero delta at initiation |

</aside>

## How a straddle works

Suppose a stock is trading at $50 and implied volatility is 20%. An earnings announcement is due, creating uncertainty. A trader thinks 20% IV is too low and expects a sharp move.

**The setup**:
- Buy 1 call @ $50 strike, 1 month expiration: costs $2.
- Buy 1 put @ $50 strike, 1 month expiration: costs $1.50.
- **Total cost**: $3.50.

**Profit scenarios**:
1. **Stock rises to $60**: Call is in-the-money by $10, put expires worthless. Profit = $10 − $3.50 = $6.50.
2. **Stock falls to $40**: Put is in-the-money by $10, call expires worthless. Profit = $10 − $3.50 = $6.50.
3. **Stock stays at $50**: Both options expire worthless. Loss = $3.50 (entire premium).
4. **Stock rises to $53.50**: Call is up $3.50, put down $3.50. No profit or loss (breakeven).

**Breakeven levels**: Strike ± premium paid = $50 ± $3.50, or $46.50 and $53.50.

## When to use a straddle

Straddles are deployed when:

1. **Earnings surprises**: A company reports unexpectedly strong or weak earnings, moving the stock sharply. Before earnings, implied volatility is elevated but not always enough.

2. **FDA approvals / regulatory events**: A biotech stock awaits a drug approval. On the announcement, the stock may move 20%+ in either direction.

3. **Central bank decisions**: Interest-rate announcements cause swings. Before the decision, IV is high; if the move is larger, the straddle wins.

4. **Merger or acquisition rumors**: Uncertainty drives volatility; the deal may or may not happen, creating optionality.

5. **Macro catalysts**: A jobs report, inflation print, or geopolitical shock can move markets sharply in either direction.

In each case, the trader believes realized volatility will exceed implied volatility priced into the options.

## Greeks and risk management

A long straddle has specific Greeks:

| Greek | Sign | Meaning |
|-------|------|---------|
| **Delta** | ~0 | Neutral directional exposure (call +0.5, put −0.5) |
| **Gamma** | + | Positive gamma; benefits from large moves |
| **Vega** | + | Long volatility; benefits if IV rises |
| **Theta** | − | Time decay works against the holder (owns premium) |

**Gamma and theta are in conflict**: Gamma says "I want volatility;" theta says "Time decay hurts me." As expiration approaches:
- If the stock is still near the strike, theta dominates and the position decays.
- If the stock has moved, gamma dominates and the position is profitable.

## Straddle vs. strangle

A **strangle** is similar but cheaper:
- Buy a call at a higher strike (e.g., $52).
- Buy a put at a lower strike (e.g., $48).

Compared to a straddle:
- **Cost**: Lower (both options are out-of-the-money).
- **Breakeven range**: Wider (needs a larger move to profit).
- **Risk/reward**: More directional risk, but lower entry cost.

A straddle is preferred if the trader expects a very large move (e.g., earnings with earnings guidance change). A strangle is preferred if the move is expected but might be moderate.

## Moneyness and strike selection

An **at-the-money straddle** has both options at the current stock price. This maximizes delta neutrality and is the standard setup.

An **out-of-the-money straddle** (buying calls at a higher strike and puts at a lower strike) is cheaper but less likely to profit significantly. This is actually a strangle.

An **in-the-money straddle** is expensive (both options have intrinsic value) but has a narrower breakeven range, suitable if the trader wants to reduce downside while keeping upside.

## Implied vs. realized volatility

The straddle's profitability hinges on realized volatility (actual price movement) exceeding implied volatility (priced into the options). If IV = 20% and realized is 25%, the straddle profits; if realized is 15%, it loses.

Before major events (earnings, Fed decision), IV typically spikes ahead of time. The straddle is often most profitable if:
1. IV is moderate (not yet fully spiked).
2. The event happens and the stock moves >2 standard deviations.
3. IV doesn't collapse after the move (sometimes it does, offsetting gains).

## Pricing and Black-Scholes

A straddle's value is the sum of the call and put premiums:

$$\text{Straddle Price} = C(S, K, r, \sigma, T) + P(S, K, r, \sigma, T)$$

Where:
- C = call price (Black-Scholes or binomial)
- P = put price
- σ = implied volatility

The straddle is long vega, so it increases in value if IV rises.

## Short straddle (the inverse)

A **short straddle** sells both the call and put, collecting the premium. It profits if the stock stays near the strike and IV declines. However:
- **Max profit**: Premium collected (limited).
- **Max loss**: Unlimited (if stock moves sharply).
- **Risk**: Defined but large; suited only for experienced sellers.

Short straddles are used by [market makers](/wiki/market-makers/) and volatility traders who manage dynamic hedges.

## Common mistakes

1. **Underestimating time decay**: Holding a straddle into the final week of expiration, hoping for a move that doesn't materialize, leads to steep losses as theta accelerates.

2. **Ignoring skew**: Some assets have [volatility skew](/wiki/volatility-smile/) (puts are more expensive than calls due to crash risk). A "fair" straddle may be misprice if skew is extreme.

3. **Selling into a crush**: After a big event (e.g., earnings), realized volatility may fall sharply even if the stock moved. IV collapses, and a straddle buyer's gains evaporate. This is the **volatility crush**.

4. **Over-leveraging**: A straddle costs less than buying shares outright, tempting traders to buy many straddles. Losses compound quickly if multiple positions decay.

<div class="wiki-seealso">

### Closely related

- [Strangle option](/wiki/strangle-option/) — Similar strategy with wider breakevens.
- [Call option](/wiki/call-option/) — One half of the straddle.
- [Put option](/wiki/put-option/) — The other half.
- [Option greeks](/wiki/options-greeks/) — Delta, gamma, vega, theta framework.
- [Implied volatility](/wiki/implied-volatility/) — The IV the straddle trader bets against.

### Wider context

- [Volatility trading](/wiki/long-volatility/) — Broader context of vol strategies.
- [Iron condor](/wiki/iron-condor/) — The short-volatility inverse.
- [Binary option](/wiki/binary-option/) — Event-driven options (related theme).
- [Barrier option](/wiki/barrier-option/) — Another volatility-dependent strategy.

</div>
