---
title: "Straddle vs Strangle: Breakeven Points and Cost Tradeoffs"
description: "Compare at-the-money straddles and out-of-the-money strangles: how breakeven distances and premium costs differ for the same move expectation."
keywords:
  - straddle vs strangle breakeven difference
  - straddle vs strangle cost
  - straddle breakeven calculation
  - strangle breakeven points
  - volatility strategies comparison
  - long straddle vs strangle
image: /svg/derivatives.svg
---

*Comparing a **straddle vs strangle breakeven** reveals a fundamental cost-benefit tension: a straddle buys an at-the-money [call](/call-option/) and [put](/put-option/), paying high premium but needing only a small move to break even; a strangle buys out-of-the-money options, paying less premium but requiring a larger move. Both compete for the same bet—that the stock will move—but at different price points and cost.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Straddle vs Strangle — Breakeven and Cost</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives strategies." />

<div class="wiki-infobox-caption">Straddles cost more; strangles need bigger moves. Both profit from volatility, but at different thresholds.</div>

|   |   |
|---|---|
| **Straddle Entry** | Buy ATM call + ATM put (same strike) |
| **Strangle Entry** | Buy OTM call + OTM put (different strikes) |
| **Typical Premium (Straddle)** | 3–6% of stock price (higher) |
| **Typical Premium (Strangle)** | 1.5–3% of stock price (lower) |
| **Lower Breakeven (Straddle)** | ATM strike minus total premium paid |
| **Upper Breakeven (Straddle)** | ATM strike plus total premium paid |
| **Lower Breakeven (Strangle)** | Lower strike minus total premium paid |
| **Upper Breakeven (Strangle)** | Upper strike plus total premium paid |
| **Move Required (Straddle)** | Total premium (%) ÷ 2 = % move needed either direction |
| **Move Required (Strangle)** | Half the move, but starting from wider strikes |
| **Best For** | Straddle: known event (earnings); Strangle: gentle conviction move |
| **Win Scenario** | Both: large moves either direction; Strangle also wins on small moves if you close early |

</aside>

## The Straddle: Buy Symmetry at the Center

A **straddle** buys a call and put at *the same strike*, typically the current stock price (at the money, or ATM). You pay the call's [premium](/option-premium/) and the put's premium; that's your total debit.

**Example:** Stock at $100. ATM $100 call costs $3, ATM $100 put costs $3. Total straddle cost: $6 per share, or $600 per contract. 

Breakevens:
- Lower: $100 – $6 = $94.
- Upper: $100 + $6 = $106.

The stock must move at least $6 (6%) in either direction to break even. If it stays between $94 and $106, you lose money.

The beauty is symmetry: a $94 close and a $106 close both break even. You don't care which way the stock moves—you just need *movement*. The call profits on upside, the put on downside, and [theta](/theta/) (time decay) is your enemy because *both* options lose value every day.

## The Strangle: Buy Asymmetry Cheaper

A **strangle** buys a call and put at *different strikes*, both out of the money. If the stock is at $100, you might buy the $105 call and the $95 put.

**Example:** $105 call costs $1.50, $95 put costs $1.50. Total strangle cost: $3.00 per share, or $300 per contract—*half* the straddle cost.

Breakevens:
- Lower: $95 – $3 = $92.
- Upper: $105 + $3 = $108.

The stock must move $5 to $8 in either direction to break even. That sounds worse, but the upside is: you paid half the premium, so the "move per dollar paid" is actually comparable or better.

## The Move-Per-Dollar Comparison

This is the critical metric. How much move must you get per dollar (or percentage) of premium paid?

**Straddle:** $6 premium, need $6 move (same direction required = either direction). Move per dollar of cost: $6/$6 = 1.0x.

**Strangle:** $3 premium, need $5–8 move (wider because strikes are further out). Move per dollar of cost: $5.50/$3 ≈ 1.83x.

The strangle demands a bigger *absolute* move, but per dollar paid, it's not dramatically worse. Often, it's comparable after [implied volatility](/implied-volatility/) and days to expiration are factored in.

## Time Decay and the Theta Problem

Both strategies are *long* [vega](/vega/) (volatility increases both options' value) and *short* theta (each day, both options decay).

For a straddle, you bought expensive options. Theta is a bigger absolute drag: $0.15 per day on a $6 straddle is 2.5% daily loss just from time. The strangle's $0.07 per day on a $3 position is 2.3% daily loss—nearly the same percentage, but smaller dollar amount.

**The key:** Both require the stock to move *quickly*, or you lose money just waiting. The strangle's lower cost buys you some flexibility—you can hold longer and still break even on a smaller move, if it comes.

## Earnings and Known Events

Straddles shine before *earnings*. You expect a large, directional move, and implied volatility is sky-high. Selling earnings straddles is also popular (short strangle earnings for defined risk). 

A straddle before earnings might cost $8 on a $100 stock (8% of price). If earnings surprise and the stock moves $10 (10%), the straddle breaks even and then profits. After earnings (volatility collapse), the straddle's value might halve even if the stock is 5% higher—a "volatility crush."

A strangle bought before earnings might cost $3, and the breakeven is a $6 move. The same earnings move plus volatility crush scenario is more favorable on the strangle because you're not paying for the ATM certainty.

## Strike Selection and Probability

Straddles at the exact ATM strike are the most expensive and have the highest probability of profit if the stock moves—because you're symmetric. Strangles let you choose: buy the 1-sigma or 2-sigma OTM strangle.

**1-sigma strangle:** Strikes roughly 1 standard deviation out. Example: $95 put, $105 call (±5 points on a $100 stock). Costs less than ATM, but the move required is a 1-sigma event (~68% probability it stays inside the strangle). Win rate: only the extreme 16% tail moves.

**2-sigma strangle:** $90 put, $110 call. Costs even less, but only extreme moves (5% probability) break even immediately. However, if the stock moves 3–4% (more likely), a 2-sigma strangle can still profit at expiration due to decay of the out-of-money side.

Most small traders buy 1-sigma or 1.5-sigma strangles expecting decent probabilities. Straddles are 0-sigma (at the money), the tightest strike pair.

## Practical Comparison: Earnings Example

Stock at $100. Earnings in 30 days. IV is elevated.

**Straddle:** Buy $100 call for $4, buy $100 put for $4. Cost: $8. Breakevens: $92 and $108.

**1-sigma Strangle:** Buy $105 call for $1.50, buy $95 put for $1.50. Cost: $3. Breakevens: $93.50 and $106.50.

**Expected move before earnings:** 6%. 

If earnings cause exactly a 6% move (stock to $106):
- Straddle: Call ITM by $6, put worthless. Profit: $6 – $8 = –$2 (loss).
- Strangle: Call ITM by $1, put worthless. Profit: $1 – $3 = –$2 (loss).

Both lose because 6% is less than the breakeven. But if the stock moves 8% (to $108):
- Straddle: Call ITM by $8, put worthless. Profit: $8 – $8 = break-even.
- Strangle: Call ITM by $3, put worthless. Profit: $3 – $3 = break-even.

If it moves 12% (to $112):
- Straddle: Call ITM by $12, put worthless. Profit: $12 – $8 = +$4.
- Strangle: Call ITM by $7, put worthless. Profit: $7 – $3 = +$4.

Both deliver the same absolute profit. The strangle's advantage is lower cost; if the move is 6–8%, the strangle loses less in dollar terms ($200 vs $800 on the straddle). If the move is 12%, both profit equally.

## Volatility Crush and Exit Strategy

After earnings, implied volatility often collapses by 30–50%, even if the stock moved significantly. A $112 stock might have been priced for a 12% move. Post-earnings, the ATM premium drops dramatically, pulling your options' extrinsic value down.

**Straddle:** You paid for high IV extrinsic value. Volatility crush is devastating. You might profit on delta (the move) but lose on [vega](/vega/) (IV drop), netting a small loss despite the big move.

**Strangle:** You paid less extrinsic value, so vega impact is smaller in absolute terms. Volatility crush still hurts, but proportionally less.

**Pro strategy:** Close straddles and strangles *before* earnings (or the event) if they've already profited from the buildup. Let the move happen post-event; you pocket the pre-event premium expansion. Re-enter a strangle *after* earnings if you still expect a move, at a much lower cost.

## Closing Positions Early

Both straddles and strangles benefit from closing at 50–75% of max profit if the stock moves quickly.

**Straddle:** Max profit is unlimited in theory. If you bought for $8 and the stock moves 10%, close at $4 profit early. The remaining theta decay isn't worth the seat-of-pants risk.

**Strangle:** Similar logic. Max profit is the difference between strike width and premium, but closing at 50% profit locks in gains and frees capital for the next trade.

## Tax and Assignment

Both are open-ended ([long](/option/) options), so assignment is not an issue. At expiration, the ITM side is exercised and you gain or lose. Most brokers auto-exercise, but confirm with yours. Losses are [capital losses](/long-term-capital-gain-tax/); gains are short-term unless held >1 year.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Option](/call-option/) — the call leg
- [Put Option](/put-option/) — the put leg
- [Option Premium](/option-premium/) — what you pay upfront
- [Theta](/theta/) — time decay working against both
- [Vega](/vega/) — volatility exposure in both strategies

### Wider context

- [Implied Volatility](/implied-volatility/) — determines premiums
- [In the Money](/in-the-money/) — profit trigger
- [Rolling Options Position Explained](/rolling-options-position-explained/) — managing straddles and strangles over time
- [Derivatives Hedging](/derivatives-hedging/) — broader context for volatility bets
- [Strike Price](/strike-price/) — the structural choice in both strategies

</div>
