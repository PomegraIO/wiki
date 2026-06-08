---
title: "Using Put Options to Hedge a Long Stock Position"
description: "How a protective put option limits downside risk on individual stock holdings, with guidance on strike selection, cost-benefit trade-offs, and expiry timing."
keywords:
  - put option hedge long stock
  - protective put
  - downside protection
  - strike price selection
  - hedge cost trade-off
image: "/svg/risk.svg"
---

*A **put option hedge** on a long stock position gives an owner the right to sell that stock at a predetermined price, locking in a floor below which losses cannot fall—and paying an upfront premium for that insurance. The choice of strike price and expiration date determines both the cost of protection and how much upside you retain.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Protective Put — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Buy the stock, buy the put; losses halt at the strike; premium paid upfront.</div>

|   |   |
|---|---|
| **What it protects** | Downside below the strike price |
| **Cost** | [Option premium](/option-premium/) paid to acquire the put |
| **Upside impact** | None—stock gains above strike are unlimited |
| **Maximum loss** | Premium + (Stock price − Strike) |
| **Breakeven** | Stock price = Acquisition cost + Premium paid |
| **Common use case** | Concentrated equity positions held before announced events |
| **Expiration risk** | If stock falls after put expires, protection vanishes |

</aside>

## How a Protective Put Works

When you own 100 shares of a stock trading at $50, you hold the profit if it rises but absorb losses if it falls. Buying a put option—specifically, a put with a $45 strike and 60-day expiration—means you've paid a premium (say, $1 per share) to guarantee you can sell those 100 shares at $45 per share anytime in the next 60 days, regardless of market price.

If the stock crashes to $30, your put is now "in the money" by $15 per share. You exercise it, sell your shares for $45, and your loss is limited to the premium paid ($1 per share) plus the $5 gap between your original purchase price and the strike. Without the put, you'd have lost $20 per share.

If the stock rises to $60, the put expires worthless—you simply don't use it. You keep the stock and profit from the $10 gain, minus the $1 premium you paid. The put has cost you $1 per share in return for peace of mind.

This is not a short-term trade; it is insurance. You bought the stock intending to hold it, and the put is a one-time premium to protect that holding from a tail-risk event (a earnings miss, sector collapse, or geopolitical shock).

## Choosing the Strike Price and Cost Trade-Off

The lower the put strike, the cheaper the premium. A $40 strike put on that $50 stock costs less than a $48 strike put, because the $40 put is further out of the money and less likely to be used. The trade-off is how much downside you are willing to absorb before the hedge kicks in.

Consider three scenarios for a $50 stock:

| Strike | Premium | Break at $35 | Breakeven | Max Loss |
|--------|---------|--------------|-----------|----------|
| $48 | $2.50 | Limited to $5.50 loss + $2.50 premium = $8 | $47.50 | $10.50 |
| $45 | $1.00 | Unhedged, lose $15 | $46 | $11 |
| $42 | $0.40 | Unhedged, lose $18 | $49.60 | $18.40 |

A $48 put is "close to the money" and costs more but gives early protection. A $42 put is cheaper but leaves you exposed to a $8 per share drop before protection begins. The right choice depends on how volatile the stock is, how long you plan to hold, and your risk appetite.

One rule of thumb: if you're hedging a single holding that represents 20% or more of your portfolio and you're especially nervous about the next earnings season, the higher strike (closer to current price) often makes sense, even at higher cost. If you're hedging a position you're reasonably confident in, a lower strike lets you pay cheaper insurance.

## Expiration and Rolling

A put option expires on a set date. If you buy a 30-day put and the stock hasn't moved much in 25 days, your put is losing [time decay](/time-decay-theta/). If you want to extend protection beyond the original 30 days, you must buy another put—you cannot simply hold the first one.

This is crucial: the protection window is fixed. If you bought a put expiring in March and the stock is still elevated in June, you need to buy a June put to stay hedged. Some investors "roll" puts continuously, buying a new one just before the old one expires. Others set a specific date—before a quarterly earnings announcement, for instance—and accept that the hedge vanishes once that risk event passes.

Rolling the put can be expensive. If you roll every 30 days on a $50 stock paying 2% per month in premium, you've paid 24% per year. On a stock you expect to hold for years, that compounds. Alternatively, you might buy a longer-dated put (6 months or a year out), which is more expensive upfront but spreads the cost over a longer period and avoids repeated rolling.

## When a Put Hedge Makes Sense

A protective put is most common in two situations:

**Concentrated equity positions:** An employee with a large block of restricted stock or founder shares faces significant downside if the company stumbles. A put provides insurance against a sudden drop in valuation without forcing a sale (and triggering [capital gains taxes](/capital-gains-tax-investor/)).

**Known catalysts:** If you expect an announcement—a [merger](/merger/), restructuring, or court decision—within the next few months and you fear a sharp decline, a put lets you hold through the uncertainty. The premium is the cost of that optionality.

**Downturns and volatility spikes:** When the market is turbulent and [implied volatility](/implied-volatility/) is high, puts are more expensive, so hedging costs more. Paradoxically, that is when many investors hedge—they feel the need for insurance most acutely. A more tactical investor might hedge only when volatility is low (and premiums are cheap), accepting the risk that a decline might happen without protection in place.

## Combining Puts with Dividends and Other Considerations

If the stock pays a [dividend](/dividend/), you still receive it while holding the put. The put simply gives you an insurance policy. If you exercise the put and sell your shares, you no longer own the stock, so you stop receiving dividends. This is a minor point for monthly or quarterly dividends, but if you're hedging into a large special dividend, it's worth factoring in—the put strike price is fixed, so the dividend cushions your downside relative to the strike.

Options are contracts on standardized terms: they trade in 100-share contracts (one "contract" = 100 shares), and expiration dates are limited to a fixed set (usually monthly, sometimes quarterly or longer). If you own 250 shares, you'd buy 2 or 3 puts depending on how you want to cover them. If you own a thinly traded stock, put options might not exist, so this strategy is unavailable.

## The Real Cost: Opportunity and Complexity

The stated cost is the premium. The hidden cost is opportunity: you've paid cash upfront that could have been invested elsewhere. Over a decade, repeated hedging against risks that never materialize becomes a drag on returns. This is why many long-term investors avoid continuous hedging and instead reserve it for specific high-conviction edge cases—a major event, a concentrated position too large to hold comfortably, or a window of time when downside feels unusually severe.

There is also behavioral risk. A put can make a losing position feel safer psychologically, which can lock you into an underwater holding longer than you should. The put is not a reason to hold a fundamentally broken investment—it is only insurance against temporary volatility.

## See also

<div class="wiki-seealso">

### Closely related

- [Option premium](/option-premium/) — how option prices are set and what drives them higher
- [Protective put](/protective-put/) — definition and mechanics of the strategy
- [Call option](/call-option/) — the opposite right: to buy at a fixed price
- [Collar hedge strategy](/collar-hedge-strategy/) — pairing a put with a covered call to reduce cost
- [Implied volatility](/implied-volatility/) — why put premiums spike when fear rises
- [In-the-money](/in-the-money/) — when an option has immediate value relative to the stock price
- [Time decay theta](/time-decay-theta/) — why option value erodes as expiration approaches

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — using contracts to offset financial risk
- Risk management — framework for identifying and protecting against tail risks
- [Volatility smile](/volatility-smile/) — why out-of-the-money puts trade at elevated prices

</div>
