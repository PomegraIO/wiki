---
title: "Bull Put Spread for Income Generation"
description: "How to use a bull put spread for income: strike selection, risk management, and return-on-capital calculation for conservative traders."
keywords:
  - bull put spread
  - bull put spread for income
  - income option strategies
  - defined risk options
  - call spread income
image: /svg/derivatives.svg
---

*A **bull put spread** is an option income strategy where you sell an out-of-the-money put and buy a further out-of-the-money put, capping your maximum loss while collecting the difference in premiums as income. The strategy profits when the stock stays above the short put strike at expiration.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Bull Put Spread — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and options." />

<div class="wiki-infobox-caption">A mildly bullish, limited-risk, defined-profit income trade.</div>

|   |   |
|---|---|
| **Max profit** | Premium collected |
| **Max loss** | Width of strikes − premium collected |
| **Break-even** | Short put strike − premium collected |
| **Ideal market** | Flat to moderately rising |
| **Time decay works** | In your favor (you're selling) |
| **Vega exposure** | Negative (benefits from lower volatility) |

</aside>

## What a Bull Put Spread Is

A bull put spread is a two-leg option strategy where you simultaneously sell a put at one strike and buy a put at a lower strike in the same expiration month. Both are out-of-the-money (OTM), meaning you believe the stock will stay above the sold strike before expiration.

You pocket the difference in premiums (short put premium minus long put premium). That's your maximum profit. The long put you buy acts as insurance: it caps your loss if the stock plunges. You'll never lose more than the width between the two strikes, minus the premium you collected.

For example, on a $100 stock, you might sell a $95 put for $2.50 and buy a $90 put for $0.50. You keep $2.00 per share ($200 per contract, since one equity option contract covers 100 shares). If the stock stays above $95 at expiration, you keep the full $200. If it drops below $90, you lose $500 ($500 strike width minus $200 premium collected).

## Strike Selection and Probability

The success of a bull put spread hinges on choosing strikes where the probability of profit is comfortable.

Most traders target a 50–70% probability that the stock will stay above the sold strike at expiration. A probability closer to 70% means you're selling a put deep out-of-the-money, collecting less premium but with a higher win rate. A 50% probability puts you at a nearer strike, collecting more premium but with roughly even odds of assignment.

You can estimate this probability using the [Greeks](/delta/) or an option pricing model. The delta of the short put is a rough proxy: a −0.30 delta put implies a 30% probability the stock closes below that strike (so a 70% chance it stays above). Most income traders prefer shorts around −0.20 to −0.35 delta.

The spread width also matters. Common widths are $5 (on a stock trading $100+) or $2.50 (on lower-priced stocks). Wider spreads collect more premium but have larger maximum losses. Narrower spreads reduce loss but also reduce income per spread.

## Return on Capital and Position Sizing

Your return on the bull put spread isn't just the premium collected—it's that premium divided by your maximum loss, which is the real amount at risk.

Say you sell a $95 put for $2.50, buy a $90 put for $0.50, and the width is $5. You keep $2.00 premium. Your maximum loss is $5.00 − $2.00 = $3.00 per share, or $300 per contract. So your return on capital is $200 / $300 = 66% if the stock stays above $95 at expiration.

That 66% return happens over weeks or months. Annualized, it's material—but it assumes the trade goes to max profit and you let it run to expiration (which invites [assignment](/exercise-price/) risk and holding costs).

Many traders close bull put spreads at 50% of maximum profit, well before expiration. This locks in the win faster and frees up buying power for the next trade. Closing a $200 max-profit spread at 50% ($100 gain) on a $300 risk reduces your position time and compounds faster.

## When and Why This Strategy Works

A bull put spread works best in a sideways or gently rising market. You profit from the passage of time (your sold put decays) and any decline in [implied volatility](/implied-volatility/).

Time decay, or [theta](/theta/), is your ally. As expiration nears, the sold put loses value faster than the bought put (because it's closer to the current stock price). Theta accelerates in the final two weeks, so many traders hold spreads through that window.

Lower volatility also helps. If implied volatility drops, all puts—especially the sold one—become cheaper, allowing you to close the spread early for a profit. Conversely, a [volatility](/volatility-smile/) spike early in the trade can turn a winning position into an underwater one temporarily, which is why many traders use wider spreads in high-volatility environments.

This strategy is least suited to strongly bearish conditions. If the stock gap-downs below your long put strike, you absorb the full loss immediately and can't salvage the trade.

## Risks and the Assignment Hook

The main risk is [assignment](/exercise-price/) on the short put. If the stock closes below your sold strike at expiration, you'll be assigned stock at that strike. That means you'll own 100 shares per contract at a price above the current market.

For a $95 / $90 spread on a stock at $94, assignment means you own stock at $95 when it's worth $94—a $100 loss right away. But you still have the long $90 put, which you can exercise to sell at $90, locking in a net $500 loss (the maximum).

Some traders don't mind assignment; they view it as "getting paid to own stock." Others hate holding overnight volatility risk on the long put. If you want to avoid assignment entirely, close the spread before expiration—even if you forgo the final 10% of max profit.

Another risk is [liquidity](/bid-ask-spread/). Narrow spreads on micro-cap stocks may be hard to execute at decent prices, or may gap unexpectedly at expiration. Stick to stocks with active option chains.

## Comparing Bull Put to Other Income Strategies

A bull put spread is similar to a [covered call](/covered-call/), but without owning the stock. You don't have to front $10,000 to sell a covered call on a $100 stock; you only tie up $300 (your max loss). That's cheaper buying power.

The downside: covered calls give you the full upside above the strike if the stock soars. A bull put spread caps your profit at the premium you collect, period. And covered calls let you keep the stock if it rises; bull puts expire worthless (no additional gain if the stock jumps 20%).

For pure income without directional conviction, a bull put spread offers better capital efficiency than a covered call. For steady equity ownership with a "hidden" income boost, the covered call wins.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — the right to buy, and how [Greeks](/delta/) apply
- [Put option](/put-option/) — the right to sell, which you're selling naked and buying protected
- [Covered call](/covered-call/) — a similar income strategy using long stock instead of a spread
- [Delta](/delta/) — how to read the probability of profit in an option's delta
- [Theta](/theta/) — time decay working in your favor each day the spread holds
- [Implied volatility](/implied-volatility/) — the volatility expectation baked into the premium you collect

### Wider context

- [Option](/option/) — the mechanics of all derivative contracts
- [Derivatives hedging](/derivatives-hedging/) — when and why traders use options
- [Risk-weighted assets](/risk-weighted-assets/) — how institutions measure option risk
- [Volatility smile](/volatility-smile/) — why out-of-the-money options are priced differently

</div>