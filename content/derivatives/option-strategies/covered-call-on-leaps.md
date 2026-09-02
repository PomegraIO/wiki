---
title: "Covered Call on LEAPS"
description: "How to sell short-term calls against long-dated LEAPS options, with margin mechanics and roll strategies that differ from standard covered calls."
keywords:
  - covered call on leaps options
  - leaps covered call strategy
  - writing calls against leaps
  - short call against leaps
image: /svg/derivatives.svg
---

*A **covered call on LEAPS** means selling short-term call options against a long-dated LEAPS (Long-Term Equity Anticipation Securities) contract you own, rather than against shares. The mechanics shift the margin treatment and open rolling windows that don't exist when covering with stock.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Covered Call on LEAPS — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Writing short calls against a long-dated call option changes the margin math and creates a unique roll-down opportunity.</div>

|   |   |
|---|---|
| **Underlying** | Your long LEAPS call (not shares) |
| **Mechanic** | Sell 30–60-day calls; repeat or roll |
| **Margin** | LEAPS serves as collateral; typically lower req. than naked call |
| **Upside cap** | Pinned to short call's strike; LEAPS delta provides leverage |
| **Gamma risk** | High near expiry; must roll proactively |
| **Assignment scenario** | Shares appear in account; must handle roll or close |

</aside>

## How the Strategy Works

In a classic [covered call](/covered-call/), you own 100 shares and sell one call contract. If the stock rises and the call finishes in-the-money, you deliver the shares at the strike price.

With a covered call on LEAPS, you reverse the leverage: instead of owning stock, you own a LEAPS call (often 12–36 months out, struck at or near the current price). You then repeatedly sell shorter-dated calls (30–60 days) against that LEAPS position. Each time the short call expires, you either let it expire worthless (and sell another) or roll it to a new strike and date.

The key difference is collateral. Your LEAPS call—not cash or shares—secures the short call position. Brokers treat the LEAPS as having some or all of its delta and notional value available for margin, so the buying power requirement is usually lower than selling a naked call or even lower than selling a call against stock. You are essentially using the leverage *within* the LEAPS to fund the premium collection from the short calls.

## Margin Treatment and Buying Power

When you sell a covered call against **shares**, the margin requirement is minimal—the broker treats your 100 shares as fully offsetting the short call obligation.

When you sell a covered call against a **LEAPS call**, margin treatment depends on your broker and the LEAPS's delta. If the LEAPS is near-the-money with a delta of ~0.70, most brokers will recognize part or all of that value toward covering the short call. You may need only 20–30% of the notional capital that a naked short call would demand, or occasionally even less.

However, this is not free leverage. If the underlying stock drops sharply, your LEAPS decays (losing [time value](/time-decay-theta/) and intrinsic value), potentially weakening the collateral position. A broker margin call is rare but possible in a severe downside move. Always maintain a buffer above your margin threshold.

## Roll Mechanics and Timing

The main tactical advantage is the roll window. With a covered call on LEAPS, you have a calendar spread: the long LEAPS sits far in the future, and the short call expires in weeks. As each short call nears expiry, you have three choices:

1. **Let it expire** — if it finishes out-of-the-money, keep the premium and sell another call the following week.  
2. **Roll up and out** — close the current short call, sell a new one at a higher strike (if the stock has risen) and a later date. This locks in gains on the short call and resets your premium-collection window.  
3. **Close both** — if the stock has risen sharply and you no longer want the position, sell the LEAPS and short call to exit cleanly.

The key insight is that rolling a short call against LEAPS is simpler than rolling against shares, because you are not dealing with [assignment](/assignment/) of stock (unless you *intend* to) and the LEAPS still sits in the background, gathering time value at a slower pace than the short-dated call is losing it.

## Delta and Assignment Risk

If your short call expires in-the-money, assignment follows the normal rules: you are obligated to deliver shares at the strike price. But you have only the LEAPS call, not shares. What happens?

Most brokers will automatically exercise the LEAPS call (converting it to 100 shares) and then deliver those shares to satisfy the short call assignment. This happens in seconds and is invisible to you—you end up short premium, and the shares are gone. However, if this scenario troubles you, you can prevent it by rolling or closing the short call before expiry.

Assignment is less of a worry in a covered call on LEAPS because the LEAPS's delta ensures you *can* be assigned without forced buying. Many traders deliberately allow assignment to roll into the next cycle of covered calls on new LEAPS.

## Comparing to Standard Covered Calls

| Aspect | Covered Call (Stock) | Covered Call (LEAPS) |
|--------|----------------------|----------------------|
| **Collateral** | 100 shares | 1 LEAPS call |
| **Margin req.** | Minimal | 20–30% of notional |
| **Leverage** | 1:1 | ~0.70:1 (depends on LEAPS delta) |
| **Roll friction** | No assignment of new shares | Exercise/delivery handled by broker |
| **Theta decay** | None on shares | LEAPS loses time value slowly |
| **Capital efficiency** | Lower | Higher (less buying power used) |
| **Complexity** | Low | Medium |

The covered call on LEAPS uses leverage to magnify both gains and losses. If the stock rises, your LEAPS gains delta value while the short call premium offsets losses. If the stock falls, the LEAPS decays, eroding collateral.

## Balancing Cost and Upside

The covered call on LEAPS is a credit strategy: you collect premium from the short calls. Each cycle, you pocket the difference between the short call premium and any increase in [strike price](/strike-price/) if you roll up.

However, because the LEAPS itself has [time value](/option-premium/), you are "paying" for the strategy through decay of that long option. Viewed holistically, the net profit or loss depends on whether the short-call premiums outpace the LEAPS's time decay.

For example:
- You buy a one-year LEAPS call, 100 strikes, for $5.00 (total debit: $500).
- You sell 30-day calls at 105 strike for $1.50 each (repeat monthly, nine times).
- If you collect $1.50 × 9 = $13.50 in premium but the LEAPS decays $10 by expiry, your net is $3.50 profit (before commissions).

The attraction is capital efficiency: you deploy less margin and capital-at-risk than owning 100 shares outright, while still capturing upside if the stock stays bounded.

## When This Strategy Works Best

This approach shines when:
- You have a moderate bullish outlook and expect the stock to drift higher or sideways over the next 12 months.
- You want to collect monthly income but cannot tie up the capital required to own shares.
- The LEAPS is priced attractively (low [implied volatility](/implied-volatility/) means cheap long calls and cheap short premiums, so choose timing carefully).
- You have experience rolling options and are comfortable with assignment events.
- You understand your broker's margin calculation and maintain adequate buffer.

It underperforms if the stock soars beyond your long LEAPS strike (capped upside), or if the stock crashes and your LEAPS becomes underwater, forcing you to decide whether to hold and wait for recovery or close the loss.

## Common Pitfalls

**Overleverage.** The leverage can be seductive. Treating the LEAPS margin benefit as "free money" and over-sizing positions leads to forced liquidations in sharp downturns.

**Rolling too far out.** If you keep rolling short calls to higher strikes without collecting enough premium to justify the risk, you effectively cap your upside while still holding downside.

**Ignoring the back-month decay.** The LEAPS is still losing time value. Some traders forget to account for this drag when calculating net profitability.

**Assignment surprises.** If you are unfamiliar with how your broker handles LEAPS exercise on assignment, you may face an unwanted stock position or forced close.

## See also

<div class="wiki-seealso">

### Closely related

- [Covered Call](/covered-call/) — the classic single-leg version with shares
- LEAPS — long-term options fundamentals
- [Option Wheel Strategy Explained](/options-wheel-strategy-explained/) — repeating put-and-call cycle
- [Protective Put vs Collar](/protective-put-vs-collar-strategy/) — alternative downside strategies
- Delta — how much an option price moves with the stock

### Wider context

- [Option Premium](/option-premium/) — time value and decay mechanics
- [Assignment](/assignment/) — what happens at expiry
- [Margin](/margin-call-forex/) — collateral and leverage rules
- Options Strategies — overview of common tactics
- [Implied Volatility](/implied-volatility/) — pricing and premium timing

</div>
