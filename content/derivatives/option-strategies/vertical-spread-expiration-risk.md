---
title: "Vertical Spread Expiration Risk and Pin Risk"
description: "Explore vertical spread pin risk at expiration—when the underlying closes at or near a short strike, creating unexpected assignment exposure and forced adjustments."
keywords:
  - vertical spread expiration
  - pin risk
  - short strike assignment
  - option assignment
  - call spread
  - put spread
  - expiration day risk
image: /svg/derivatives.svg
---

*When the underlying asset closes at or very near a short strike at [expiration](/expiration-date/), a **vertical spread faces pin risk**: the short leg may be assigned while the long leg remains unexercised, forcing the trader into an unexpected and potentially costly position. This is one of the most underestimated risks in options trading.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Pin Risk — Vertical Spread Hazard</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">At expiration, assignment of the short strike can leave the trader unhedged.</div>

|   |   |
|---|---|
| **Risk Occurs** | Underlying closes at or within a few cents of the short strike |
| **Problem** | Short leg assigned, long leg expires worthless or is exercised separately |
| **Result** | Unintended position: short stock, short call, long put, or naked short |
| **Timing** | Can happen over the weekend if assignment is processed after-hours |
| **Cost Impact** | Stock may gap against the trader; adjustment costs spike near expiration |
| **Call Spread Example** | Short 100 call, long 105 call, underlying closes at 100.50 → assignment risk |
| **Put Spread Example** | Short 50 put, long 45 put, underlying closes at 50.25 → assignment risk |
| **Probability** | Highest when the underlying is within the strike width and near expiration |

</aside>

## What Pin Risk Is

**Pin risk** refers to a unique hazard in [vertical spreads](/vertical-spread/): the "pinning" of the underlying at or near a strike price at expiration, which can leave the trader with a lopsided exposure.

A vertical spread has two legs: a sold (short) option and a bought (long) option at a different strike. For example:
- **Call spread**: Sell 1 call at $100, buy 1 call at $105.
- **Put spread**: Sell 1 put at $50, buy 1 put at $45.

At expiration, if the underlying closes in the money for the short leg but out of the money for the long leg, or at a price where one leg is exercised and the other is not, the trader ends up with an unintended position.

**Call spread example:** Suppose you've sold a $100 call and bought a $105 call on a stock. At expiration, the stock closes at exactly $100.50. The short $100 call is in the money and is assigned; you're forced to sell 100 shares at $100 (or deliver stock you don't own, requiring a forced purchase). The long $105 call is out of the money and expires worthless. You're now short 100 shares—the call spread has collapsed into a naked short position. If the stock gaps up 5% overnight, your loss on that short position balloons.

**Put spread example:** You've sold a $50 put and bought a $45 put. At expiration, the stock closes at $49.50. The short $50 put is assigned; you're forced to buy 100 shares at $50. The long $45 put is out of the money and expires worthless. You've been assigned and own 100 shares at $50 without the downside protection you expected from the $45 put.

The trader's original thesis was a defined-risk spread; the risk was capped by the long leg. But due to pin risk, the trader ends up with unlimited or very high exposure.

## Why Pin Risk Happens

Pin risk is created by the mechanics of [assignment](/exercise-price/) and expiration:

1. **Discrete strikes.** Options only exist at discrete strike prices (typically $1 apart for stocks, tighter for indices). The underlying can close anywhere in the continuum, but option exercises only occur at those specific strikes.

2. **Assignment is binary.** A short in-the-money option is assigned; a short out-of-the-money option is not. There's no partial assignment or deferral. If the underlying closes at $100.01 when you're short the $100 call, you're assigned. If it closes at $99.99, you're not.

3. **Legs don't move in sync.** The trader's intention is that both legs of the spread expire together—either both in the money, both out, or the long leg protects the short leg. But near the strike price, tiny price movements can cross one leg into the money while leaving the other out.

4. **Weekend and after-hours risk.** Expiration occurs on a Friday. If the stock closes at $99.50 Friday afternoon with you short the $100 call, you assume the call is safe. But over the weekend, company news causes a $2 gap up Monday morning. You're assigned, and you're short 100 shares at the worst possible price—and the long leg still can't protect you because it's already expired.

5. **Liquidity and closing prices.** If the underlying stock or ETF is thinly traded, prices can be volatile in the final moments of trading. A sudden bid spike in the last minute could spike the underlying from $99.80 to $100.20, crossing a strike and triggering assignment.

## Call Spreads and Pin Risk

In a bullish [call spread](/call-spread/) (e.g., sell $100 call, buy $105 call), pin risk is most severe if the underlying closes above the short strike but below the long strike. 

- Underlying at $100.25 at close → Short call is assigned; long call expires out of the money. You're short 100 shares.
- Underlying at $100.25 at close → Short call is **ITM**. assigned; long call is **OTM**, expires. You have no hedge.
- Next Monday, stock opens at $106 → Your short is now a $6 loss per share (before you can even buy to close).

Conversely, if the underlying is well below the short strike (e.g., $98) or well above the long strike (e.g., $106), both legs behave predictably, and there's no pin risk.

## Put Spreads and Pin Risk

In a bearish [put spread](/put-spread/) (e.g., sell $50 put, buy $45 put), pin risk arises if the underlying closes below the short strike but above the long strike.

- Underlying at $49.75 at close → Short put is assigned; you're forced to buy 100 shares at $50. The long $45 put expires worthless, offering no downside buffer.
- You now own 100 shares at $50, but if the stock opens Monday at $45 (a $5 crash), your "protected" position was never actually protected.

The spread was supposed to cap loss at $500 (the $5 difference times 100). But because of the pin, you absorbed the full $5 decline.

## Probability of Pin Risk

Pin risk probability is highest when:

1. **Underlying is very close to the short strike.** Within $0.10 or $0.25, assignment is nearly certain.
2. **Near expiration.** With just hours until market close, little time remains for price to move away from the strike.
3. **Illiquid underlying.** Thinly traded stocks and ETFs see volatile price action in the final minutes; pinning to a strike is more likely.
4. **After earnings or events.** If expiration coincides with earnings, economic data, or Fed announcements, gaps and rapid moves can pin the stock to a strike.

Conversely, pin risk is negligible if the underlying is far from the short strike (e.g., $10 above a short call, or $10 below a short put).

## Strategies to Mitigate Pin Risk

**Close early:** The safest approach is to close the vertical spread 1–7 days before expiration, capturing most of the theta decay and avoiding expiration mechanics entirely. A spread that was defined-risk is now locked in as a defined profit or loss.

**Monitor closely:** If the underlying drifts near the short strike in the final two days before expiration, be prepared to adjust. Closing a short call spread where the stock is approaching the short strike from below requires buying back the short call (locking in loss) or rolling it up.

**Adjust before pinning:** If the underlying is within the strike width and expiration is tomorrow, take action now. Close the spread, roll it, or widen it. Don't wait for Monday morning.

**Widen the spread:** If the underlying is between your strikes, consider rolling the short leg further away to increase cushion, or buying back the short and selling a further call or put to move the short strike.

**Use tighter strikes:** Some traders use spreads with strikes very close apart (e.g., $1) for call spreads on expensive stocks, or $0.50 apart on leveraged ETFs. This reduces pin risk because the maximum width to the long leg is smaller—even if pinned, losses are capped tighter.

**Exercise the long leg actively:** Some traders manually exercise their long leg before expiration if the short leg is about to be assigned. This converts the pined position into the desired outcome (e.g., exercising the long call to sell 100 shares instead of being forced to deliver shares you don't own). This requires active monitoring and immediate execution, but it works.

**Roll the position:** Rolling a vertical spread forward in time and adjusting strikes can reset the risk. If a call spread is pinned below the short strike, roll the short call up and out one or two months, collecting premium and moving away from pin risk.

## Assignment and Forced Positions

One often-overlooked aspect of pin risk is **early assignment**. The short option in a spread can be assigned before expiration if it's deep in the money and carries [dividend risk](/dividend/) (for calls) or credit risk (for puts). This can pin the trader to a position even earlier than expiration.

For example, a call spread on a high-dividend stock might see the short call assigned three days before expiration because the dividend is paid tomorrow. The trader loses the long call's protection and is now short stock unexpectedly.

Similarly, some traders fail to realize that holding through expiration in a spread may trigger weekend assignment risk. The stock exchange is closed Friday night through Sunday, and the clearing house processes assignments over the weekend. If news causes a gap Monday morning, the trader is now positioned against that gap with no chance to react.

## The Role of [Time Decay](/time-decay-theta/)

Pin risk exists partly because the long and short legs of a vertical spread decay at different rates as expiration approaches. Near expiration (the final few days), the time value of the long leg can collapse faster than the short leg if the long strike is far out of the money. This leaves the trader with minimal cushion.

For example, a $100/$105 call spread with the stock at $99 one day before expiration: the short $100 call has almost no time value left (it's OTM), and the long $105 call is deeply OTM and worthless. The trader has already collected the spread's maximum profit. But if the stock closes at exactly $100.01, the short is assigned, and the trader's "profit" becomes a short position.

## See also

<div class="wiki-seealso">

### Closely related

- [Vertical Spread](/vertical-spread/) — the spread structure and basic mechanics
- [Call Spread](/call-spread/) — bullish vertical spread using calls
- [Put Spread](/put-spread/) — bearish vertical spread using puts
- [Exercise Price](/exercise-price/) — strike at which assignment occurs
- [Time Decay](/time-decay-theta/) — theta; acceleration near expiration

### Wider context

- Option Assignment — mechanics of when and how assignment happens
- [Call Option](/call-option/) — long and short call behavior at expiration
- [Put Option](/put-option/) — long and short put behavior at expiration
- [Expiration Date](/expiration-date/) — final day of trade; assignment and settlement
- [Protective Put](/protective-put/) — long put as a hedge; similar mechanics to spread long legs

</div>