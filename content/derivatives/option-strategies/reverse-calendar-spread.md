---
title: "Reverse Calendar Spread"
description: "An option strategy that buys near-term options and sells longer-dated options at the same strike to profit from short-term volatility spikes."
keywords:
  - calendar spread
  - option strategy
  - time decay
  - volatility trading
  - directional options
image: "/svg/derivatives.svg"
---

*A **reverse calendar spread** inverts the typical calendar spread logic: you buy a near-term [option](/option/) and sell a longer-dated option at the same [strike price](/strike-price/). Instead of betting on [time decay](/time-decay-theta/), you are betting that implied volatility will spike in the short term, and you want to harvest that spike before your near-term contract expires.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reverse Calendar Spread — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A volatility-first strategy that profits when short-term IV jumps while longer-dated IV remains calm.</div>

|   |   |
|---|---|
| **What it is** | Buy short-term option; sell longer-dated option at the same strike |
| **Also called** | Reverse time spread, short calendar spread, front-month spread |
| **Max profit** | Premium collected minus premium paid; capped at strike difference for directional moves |
| **Max loss** | Limited to initial debit if both legs expire worthless |
| **Ideal market** | IV spike imminent; long-dated vol stays low or only rises moderately |
| **Key risk** | If IV collapses, the long option value erodes faster than the short |
| **Legs** | Two (long short-term, short long-term) |

</aside>

## Why reverse the calendar structure

A standard [calendar spread](/option/) sells the near-term contract (high theta decay) and buys the far-term contract (slower decay). This works when you expect calm markets: the near-term option expires, you keep the premium, and the long option still has months of life left.

A reverse calendar spread flips this: you buy the 30-day contract and sell the 90-day contract at the same strike. You pay a debit initially—the near-term option is always cheaper, but you're buying the one with less time value. This seems backwards until you understand the volatility play.

The bet is that volatility will spike sharply in the near term. When [implied volatility](/implied-volatility/) jumps, all options at all expiration dates gain value. But the near-term option, having less time left, is hypersensitive to IV changes. A 10-point jump in IV can double a 20-day option's value; the same jump moves a 120-day option only marginally.

If the spike hits while you hold both legs, your short long-term option gains value slowly (or loses value as IV falls back), while your long short-term option gains sharply. You can close the short leg for a tighter cost or let both expire, pocketing the difference.

## The volatility timing trigger

Reverse calendar spreads are inherently event-driven. The catalyst is usually an earnings announcement, economic data release, or a geopolitical shock expected to roil the markets. Traders set up the reverse calendar 1–3 weeks before the event.

In the days leading up to earnings, implied volatility typically rises. The reverse calendar benefits from this rise, especially if the rally is faster in the near-term options. On the day of earnings itself, if the stock gaps sharply (up or down), the near-term option's intrinsic value balloons, capturing the move. The longer-dated option benefits from the spike too, but less acutely.

The ideal outcome is: stock moves sharply on the announcement, IV stays elevated or rises further, you close or let the near-term expire deep in the money, and the long-dated option still has months of value left to sell or let decay.

## Directional optionality and the strike choice

Unlike a neutral calendar spread, which is often placed at the money, a reverse calendar can be placed at any strike depending on your directional bias. Buy and sell a $100 call for a volatility spike that you expect to be bidirectional. Buy and sell a $105 call if you think the spike will tilt upside. Buy and sell a $95 put if you expect downside shock.

If the stock moves past your strike in the direction you favoured, the intrinsic value of the near-term option grows, adding to your profit from volatility. If it moves the opposite direction, the near-term option's intrinsic value becomes a drag, and you rely on the volatility spike to offset it.

This is where reverse calendars differ sharply from standard calendars: they are not truly neutral trades. They carry directional gamma, meaning they profit both from a volatility spike and from the stock moving in the direction of your chosen strike.

## The collapse risk

The biggest threat to a reverse calendar is not a quiet market but a volatility collapse post-event. If the stock is expected to gap sharply on earnings but instead drifts sideways and IV implodes, both your legs lose value. The near-term option loses value faster (smaller gamma buffer), and the long-dated option holds value longer but still decays.

If IV falls sharply after the event, the long-dated option's value drops slower than the near-term's, inverting the profit picture. You're short volatility indirectly: you sold the contract that holds volatility for longer. A calm market is a reverse calendar's enemy.

This risk is why reverse calendars are not suitable as outright volatility speculation tools. They work only if you have conviction about a specific catalyst and confidence that the event will trigger volatility.

## Rolling and adjustment before expiration

Most traders don't hold a reverse calendar to expiration. Instead, they monitor the trade closely and take profits or adjust as soon as the catalyst arrives and the volatility spike manifests.

If the spike is muted, you can close the near-term leg early (before decay erodes all its value) and hold the long-term option for a second move. If the spike is aggressive, you might close both legs simultaneously and lock in the profit.

Some traders roll the near-term leg forward by a week or two, converting the trade into a series of short-term bets against a longer-dated short position. This keeps you in the volatility-spike trade longer, but adds complexity and transaction costs.

## Cost and probability of profit

A reverse calendar is typically set up for a debit (you pay more for the near-term than you receive from the long-dated sale). This debit limits your maximum loss: if both legs expire out of the money and IV is low, you lose the full debit.

Because you're betting on a specific event and a specific volatility move, the win rate is lower than a standard calendar's. But when the event triggers volatility and the stock moves your way, the payoff can be 2:1 or better—turning a small debit into a meaningful gain.

The strategy rewards conviction and timing but punishes indecision. Holding a reverse calendar past the catalyst with no volatility spike is usually a mistake.

## When to deploy a reverse calendar spread

Use a reverse calendar when you anticipate a significant volatility event—earnings, merger announcement, regulatory decision, sector crisis. You have a reasonable directional bias (or are willing to bet bidirectionally) and expect implied volatility to jump sharply for a short window.

Avoid reverse calendars on quiet, low-conviction trades. If you're not sure the event will move the market, the debit cost is not worth the theta decay during the waiting period.

The strategy also works on highly volatile securities where IV swings are pronounced. A stable utility stock is a poor fit; a biotech stock in a clinical trial or a meme stock in a volatile period is ideal.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Backspread](/ratio-spread-backspread/) — exploits directional upside moves with debit-based leverage
- [Put Backspread](/put-backspread/) — the downside equivalent for bearish directional catalysts
- [Double Diagonal Spread](/double-diagonal-spread/) — sells time on both sides while managing direction
- [Implied Volatility](/implied-volatility/) — the core driver of reverse calendar profitability
- [Time Decay (Theta)](/time-decay-theta/) — the enemy of reverse calendars; works against the trade when IV is calm
- [Option Premium](/option-premium/) — the debit paid and the spike-driven gain harvested

### Wider context

- [Option](/option/) — the foundational contract for all time-based strategies
- [Delta](/delta/) — directional exposure that compounds the volatility spike profit or loss
- [Vega](/vega/) — the IV sensitivity measure that determines spread payoff
- [Volatility Smile](/volatility-smile/) — the pattern of IV across strikes that affects reverse calendar design

</div>
