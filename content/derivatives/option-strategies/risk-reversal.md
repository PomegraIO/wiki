---
title: "Risk Reversal"
description: "An options strategy that combines a long out-of-the-money call and short out-of-the-money put at different strikes to gain directional exposure while minimizing upfront premium."
keywords:
  - option strategy
  - call option
  - put option
  - directional trading
  - volatility
image: "/svg/derivatives.svg"
---

*A **risk reversal** is a directional options strategy combining a long [out-of-the-money](/out-of-the-money/) [call](/call-option/) and a short [out-of-the-money](/out-of-the-money/) [put](/put-option/) at different strikes, typically designed to reduce or eliminate the net [premium](/option-premium/) outlay. It's a cost-efficient way to express bullish conviction, trading downside protection for uncapped upside potential.*

## The directional bet at low cost

A straightforward bullish bet via options—buying an [out-of-the-money](/out-of-the-money/) call—requires paying premium upfront. The higher your conviction and longer your timeframe, the more capital gets locked in the call's [theta decay](/time-decay-theta/).

A risk reversal flips this economics. You still buy the bullish call, but you simultaneously sell a [put](/put-option/) at a lower [strike price](/strike-price/), collecting premium that offsets (or entirely funds) the call's cost. In ideal conditions, the trade executes for zero net debit or even a small credit.

The catch: by selling the put, you're obligating yourself to buy the underlying at that lower strike if it falls below it at expiration. In effect, you've capped your downside risk—you can't lose more than the difference between your put's strike and zero, minus any credit received. But you've eliminated or greatly reduced the cost of directional bullish leverage.

## Structure and payoff

Suppose the stock trades at $100.

- Buy one call at $105 strike, paying $2 premium
- Sell one put at $95 strike, collecting $2 premium

Net debit: $0. At expiration:

- **If stock > $105**: You profit dollar-for-dollar on the call; the put expires worthless. Profit = stock price − $105.
- **If stock between $95 and $105**: Both options expire worthless. You break even (net zero premium paid/received).
- **If stock < $95**: The call expires worthless; the put is [in-the-money](/in-the-money/), and you're assigned stock at $95. Your loss = $95 − stock price.

The strategy delivers an asymmetric payoff: unlimited upside, capped downside. The exact downside cap depends on strike selection and the premium collected on the put.

## Why traders favour it over directional calls alone

Buying a straight call costs all its premium upfront. If the stock drifts sideways or even modestly higher, the call's [theta decay](/time-decay-theta/) erodes gains. A risk reversal shifts this burden. The put's [theta](/theta/) is negative (your favour), partially offsetting the call's decay.

It also democratises leverage. Instead of saving $1,500 to buy a $1,500 call, you can set up a risk reversal for a nominal debit or credit, controlling the same notional upside while your capital is deployed elsewhere.

Traders in [bull markets](/bull-market/) and those preparing for earnings announcements or [corporate actions](/acquisition/) often favour this structure. The zero-debit variant is especially popular in sideways-to-bullish regimes where [implied volatility](/implied-volatility/) is stable or declining.

## Variations

**Call spread + put**: If you buy an [out-of-the-money](/out-of-the-money/) call and sell a lower call, plus sell a put, you create a "collar with teeth"—a more complex variant that locks in a range.

**Ratio adjustments**: Some traders sell two puts for every call purchased, or reverse the ratio, depending on their conviction and risk appetite. This skews the payoff and requires careful margin management.

**Different expirations**: Selling a put at a closer expiration and buying a call at a longer one ("calendar risk reversal") lets you harvest put decay quickly while maintaining long-dated upside.

## When to deploy it

**Bullish outlook, capital efficiency**: You expect the underlying to rise but want to minimize cash outlay.

**Earnings or catalyst events**: Before a major announcement, [implied volatility](/implied-volatility/) is often high. Selling the put collects fat premium; the call is expensive but is offset. After the event, volatility collapses, and both legs lose value, but the asymmetry favours the trade if the catalyst was favourable.

**Stock downgrades or sector malaise**: If a stock has fallen and consensus is bearish, but you see value, a risk reversal lets you express conviction cheaply. If the market re-rates it upward, you profit; if it falls further, you have a defined point to buy (the put strike) rather than catching a falling knife indefinitely.

**Rotating out of downside hedges**: If you've been holding protective puts (paying theta) and the market outlook improves, selling calls and keeping the puts creates a risk reversal, offsetting hedge cost.

## Risks and management

**Unlimited max loss on the put side is the main pitfall**: If you sold a $95 put and the stock crashes to $50, you're assigned and now underwater. However, your max loss is capped at the strike minus any credit; you won't lose more than that unless you sell additional puts at lower strikes.

**Early assignment risk**: If the put goes deep [in-the-money](/in-the-money/) and carries significant [intrinsic value](/intrinsic-value/), the seller might exercise it early, forcing you to buy shares before you're ready.

**Whipsaw volatility**: A sharp drop followed by a recovery can leave you holding assigned shares at the put strike while watching the stock rise. Rolling or closing early becomes essential.

**Bid-ask spread drag**: Unwinding a risk reversal requires closing both legs. If liquidity is thin or you're forced to unwind, the [bid-ask spread](/bid-ask-spread/) on each leg compounds.

To manage, set clear exit rules: close the position if the stock breaches a support level you've defined, or when [theta](/theta/) decay slows and you've harvested the bulk of the edge.

## Greeks and sensitivity

**Delta**: Positive (bullish). The long call delta minus the short put delta gives net directional exposure. A typical risk reversal might have +0.6 to +0.8 delta.

**Gamma**: Usually negative because you're short gamma from the put. Large rallies are good; large declines hurt acceleratingly. Manage gamma carefully in choppy markets.

**Theta**: Slightly positive. The put's [theta decay](/time-decay-theta/) typically exceeds the call's, giving you a small daily time-decay advantage.

**Vega**: Often near zero. If the long call and short put have similar [vega](/vega/) magnitudes, [implied volatility](/implied-volatility/) moves offset. In a rising-volatility environment, the put might gain more than the call loses, eroding your position.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Option](/call-option/) — the long leg
- [Put Option](/put-option/) — the short leg
- [Out-of-the-Money](/out-of-the-money/) — the starting zone for both legs
- [Bull Call Spread](/bull-call-spread/) — another bullish low-cost strategy
- [Collar](/collar/) — a protective variant using stock
- [Implied Volatility](/implied-volatility/) — drives the premiums
- [Delta](/delta/) — governs directional exposure

### Wider context

- Option Strategy — the broader category
- Derivatives — the asset class
- [Volatility Smile](/volatility-smile/) — explains put–call premium asymmetry
- [Bull Market](/bull-market/) — the typical environment

</div>
