---
title: "Iron Condor Adjustments When Price Breaks Out"
description: "Defensive tactics to manage an iron condor when the underlying breaks past the short strike, including rolling, broken-wing conversion, and one-side closure."
keywords:
  - iron condor adjustment
  - iron condor breakout
  - option strategy adjustment
  - broken-wing condor
  - rolling options
  - iron condor management
image: /svg/derivatives.svg
---

*An **iron condor adjustment** is a defensive trade made when the underlying asset moves past one of the short strike prices before expiration, threatening a maximum loss on that side. Traders can roll the threatened spread to a new strike, convert it to a broken-wing by closing the long, or exit one side entirely to reduce exposure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Iron Condor Adjustments — when and how</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Broken-wing and roll tactics limit losses and cap new risk; exiting one side is the simplest reset.</div>

|   |   |
|---|---|
| **Signal to adjust** | Price reaches short strike; time remaining >14 days |
| **Primary goal** | Limit max loss below initial credit collected |
| **Rolling** | Moves both short and long strikes out in time; requires new capital |
| **Broken-wing conversion** | Closes the long; narrows range, caps loss, accepts risk |
| **One-side exit** | Closes entire call or put side; keeps other side alive |
| **Cost** | Typically $100–$300 net debit (partially offsets original credit) |
| **Best scenario** | Price reverses before adjustment; you keep original credit |

</aside>

## Why the Iron Condor Breaks Down

An [iron-condor](/iron-condor/) is a four-leg option strategy: sell an out-of-the-money (OTM) call, buy a further OTM call, sell an OTM put, and buy a further OTM put. You collect a credit upfront because the call spread and put spread generate premium. Maximum profit is the credit collected; maximum loss occurs if the underlying closes beyond either short strike at expiration.

The condor profits when the underlying stays between the two short strikes. It is a mean-reversion or low-volatility bet. The initial setup assumes the price will stay within a defined range.

When price breaches one short strike—say, the stock rallies past your short call strike with 3 weeks to expiration—two problems emerge:

1. **The broken side is now in-the-money (ITM).** The short call, which was OTM and had little time value remaining, now has intrinsic value. It will decay toward full loss if left unmanaged.

2. **The long call is still OTM (or just in-the-money).** Your protective long call is now more valuable, but it is still far from your max loss. If price keeps rising, you lose the full width of the call spread.

If you do nothing and let the position sit until expiration with price above the short call strike, you lose money on the call side up to the full width of the spread (usually $1–$5 per share, or $100–$500 on a typical 100-share position).

## Adjustment Tactic 1: Rolling the Broken Side

**Rolling** means closing the threatened spread and opening a new spread at a higher strike (if broken to the upside) or lower strike (if broken to the downside), usually in the same or a later expiration.

### Call Side Roll (Upside Breakout)

Suppose you sold a 105/110 call spread and the stock rallied to $108, with 21 days left to expiration.

1. **Close the existing 105/110 call spread.** Buy back your 105 short call and sell the 110 long call. This turns into a net debit (you pay out money). Because the 105 call is now ITM, you may pay $1.50 for the short call and collect $0.25 for the long call, netting a $1.25 debit, or $125 on 100 shares.

2. **Open a new 110/115 call spread.** Sell the 110 call and buy the 115 call for 21 days out. You collect a smaller credit—say, $0.50—because the strikes are higher and there is less premium. You net $0.50 credit, or $50 on 100 shares.

3. **Net on the roll:** Paid $125 to close the old spread, collected $50 on the new spread. Net debit: $75, or $0.75 per share.

The rolled position now has a new short call at 110 instead of 105. If the stock reverses and falls below 110 by expiration, you've "survived" the breakout. If it stays above 110, you lose money again—but you've bought more time and shifted the risk higher.

**Pros of rolling:**
- You can repeat the process multiple times, potentially salvaging a trade that would otherwise be a full loss.
- You stay long the condor framework and profit if price mean-reverts.
- Works well in choppy, sideways-drifting markets.

**Cons of rolling:**
- Each roll costs money (transaction fees + the debit of closing the ITM spread).
- You are committing new capital with each roll. If price keeps moving against you, you rack up losses across multiple adjustments.
- Psychological: rolling can turn a small loss into a large one if you keep doubling down.

## Adjustment Tactic 2: Converting to a Broken-Wing Condor

A **broken-wing** (or "lopsided" condor) is when you close the protective long strike on the broken side, leaving only the short strike. It sounds risky—you lose the max-loss cap on that side—but it is a strategic choice when you believe price will hold or reverse.

### Call Side Conversion Example

You sold 105/110 calls, price broke above 105. Instead of rolling, you:

1. **Sell the 110 long call.** You collect whatever premium remains (maybe $0.30).

2. **Keep the 105 short call.** Now you have a naked short call above 105, instead of a call spread. If price stays below 105, you profit by the full spread (now $500 for a 1-dollar width). If price goes above 105, your loss increases dollar-for-dollar with every point the stock rises (no cap).

The broken-wing is a bet: "I think price will stay below 105 by expiration, or I accept the risk of unlimited loss on this side."

**Pros of broken-wing:**
- You collect cash from the long strike sale (reduces your adjusted cost basis).
- If price reverses, you keep the full spread as profit instead of a smaller rolled credit.
- Fewer transaction costs than rolling repeatedly.

**Cons of broken-wing:**
- You lose the protective long strike. If price keeps rising, you lose more than the original spread width.
- Maximum loss is now theoretically unlimited (though practical loss caps when you close the trade).
- Psychologically harder to manage a naked short call.

**When to convert:**
- You have strong conviction price will revert within the remaining time.
- Your original credit collected is large enough that a 50% loss is still acceptable.
- You can monitor the position daily and close it if price accelerates further away.

## Adjustment Tactic 3: Close One Side Entirely

The simplest tactic is to **exit the broken side completely** and let the other side stand alone.

### Example: Call Side Breakout, Close Calls

Stock breaks above your 105 short call with 3 weeks to go. You:

1. **Buy back the 105 short call** (paying ITM premium).
2. **Sell the 110 long call** (collecting residual OTM premium).
3. **Net effect:** You exit the call side with a loss, but you've capped that loss. You no longer face further losses from the call side, even if the stock runs to $200.

You still have the put spread alive on the downside. If the stock reverses or stays flat, the put spread still profits.

**Pros of closing one side:**
- Simple, one decision. No rolling or monitoring needed on that side.
- You cap your loss immediately and stop the bleeding.
- You can focus on managing the remaining side (the put spread, in this example).
- If the stock reverses, the put side can still reach max profit.

**Cons of closing one side:**
- You take a loss on the broken side and lock it in.
- If price then reverses, you realize "I should have waited."
- You've given up the hedge from the two-sided structure. Now you have a one-sided naked short put (if you closed the call side), which has unlimited downside risk in that direction.

**When to close one side:**
- You want to minimize ongoing risk and losses.
- You do not have the capital or risk tolerance to keep rolling or adjusting.
- The broken side has moved so far ITM that the original credit is nearly wiped out anyway.

## Adjustment Timing and Trigger Points

**The sooner the better, but not immediately.**

Most traders adjust when the underlying **touches the short strike or moves 1–2% past it**. Adjusting immediately after a breakout is emotionally appealing but often premature. If the stock bounces back within hours or days, you've paid adjustment costs for nothing.

**Better practice:**
- Wait for price to hold **above (or below) the short strike for at least 1–2 days**, confirming the move is real.
- Adjust when the short strike is threatened but still has 14+ days to expiration. If there is only 1 week left, the position may be past the point of cost-effective adjustment; you might as well close it.
- Use [support-and-resistance](/support-and-resistance/) levels to anticipate breakouts. If price is approaching a key resistance, you can preemptively adjust before it breaks.

## Cost-Benefit: When NOT to Adjust

Sometimes, adjusting costs more than it helps.

**Example 1: Very close to expiration.** You sold a 105/110 call spread, price is at $107, and there are 2 days left. The short call is worth $2–$3. Rolling to a 110/115 spread might cost $2 after the sale credit. You're paying most of your max loss just to defer it 21 days. Better to let it expire or close it outright.

**Example 2: Price far beyond strike.** Stock breaks above your 105 short call and continues rallying to $120. Rolling requires paying $15 just to close the old spread. Rolling to 120/125 is too far out and collects almost no credit. Not worth it.

**Example 3: Volatility crush removes premium.** If [implied-volatility](/implied-volatility/) drops sharply after the breakout, option prices collapse. Rolling or adjusting yields almost no credit for the new spread. Better to close and move on.

## Sizing and Risk Management

The key to managing iron condor breakouts is **starting with smaller size.** A trader who sells 10 iron condors (1,000 shares of call spread + 1,000 shares of put spread) faces devastating losses if they have to adjust multiple contracts.

Better practice: **sell 2–4 iron condors per position**, which gives you room to adjust without the portfolio melting down. If one condor breaks, rolling or converting a 2-condor position costs less and feels more manageable than a 10-condor disaster.

## See also

<div class="wiki-seealso">

### Closely related

- [Iron-condor](/iron-condor/) — the full setup, max profit, max loss, and Greeks
- [Call-option](/call-option/) — short and long calls, strikes, and ITM/OTM dynamics
- [Put-option](/put-option/) — short and long puts in the condor structure
- [Delta](/delta/) — how much the position gains/loses per $1 move in the underlying
- [Theta](/theta/) — time decay, which is the iron condor's friend until price moves wrong

### Wider context

- [Option](/option/) — fundamental concepts of calls, puts, exercise, expiration
- [Strike-price](/strike-price/) — moneyness and why strikes matter for breakout risk
- [Implied-volatility](/implied-volatility/) — how [vega](/vega/) affects adjustment costs and rolled strikes
- [Support-and-resistance](/support-and-resistance/) — anticipating breakouts and setting adjustment levels
- [Covered-call](/covered-call/) — simpler one-sided directional option strategy for comparison

</div>
