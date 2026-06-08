---
title: "Long Call Butterfly vs Iron Butterfly"
description: "Understand the cost, risk profile, and assignment mechanics of call-only butterflies versus iron butterflies for limited-risk directional trades."
keywords:
  - long call butterfly vs iron butterfly
  - call butterfly vs iron butterfly
  - butterfly spread options
  - iron butterfly strategy
image: /svg/derivatives.svg
---

*A **long call butterfly** and an **iron butterfly** are both limited-risk trades designed to profit when a stock stays near a middle strike. The call butterfly costs cash upfront (debit); the iron butterfly earns a credit. The assignment and margin mechanics differ sharply, and each suits a different trading style.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Long Call Butterfly vs Iron Butterfly — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Two ways to bet on low volatility and range-bound stocks; one costs cash, one sells premium.</div>

|   |   |
|---|---|
| **Structure** | 1 long lower call, 2 short middle, 1 long upper | 1 short lower put, 2 short middle, 1 long upper put |
| **Leg count** | 4 legs (all calls) | 4 legs (puts on bottom, calls on top) |
| **Cost type** | Net debit (cost cash) | Net credit (receive cash) |
| **Max profit** | Width between strikes minus debit | Width between strikes minus credit received |
| **Max loss** | Initial debit paid | Width between strikes minus credit |
| **Margin** | Lower (debit paid) | Higher (credit exposure) |
| **Assignment** | 1 leg (short middle call) | 2 legs possible (short middle put/call) |
| **Theta decay** | Positive (owns wings, shorts middle) | Positive (short middle legs decay faster) |

</aside>

## Structure and Setup

**Long call butterfly:** You buy one far out-of-the-money call, sell two at-the-money calls, and buy one deep out-of-the-money call, all with the same [expiration date](/expiration-date/). Example: Stock at $100. Buy 95 call, sell 100 call (twice), buy 105 call. Each strike is $5 apart. Cost: suppose the 95 call costs $4, each 100 call sells for $2, and the 105 call costs $0.50. Net cost = $4 – $4 + $0.50 = $0.50, or $50 per butterfly.

**Iron butterfly:** You sell one out-of-the-money put, sell two at-the-money puts or calls (the middle legs), and buy one further out-of-the-money put or call. It is typically two puts on the downside and two calls on the upside. Example: Buy 90 put, sell 95 put, sell 105 call, buy 110 call. If premiums are rich, this might credit $3, or $300 per butterfly.

The call butterfly is debit-funded; the iron butterfly is credit-funded. This single difference cascades into different margin requirements, assignment risk, and decision trees.

## Cost and Capital Efficiency

A **long call butterfly** requires you to spend cash. In a favorable scenario (low premiums or wide strikes), the net debit can be small—$25 to $100 per butterfly. But you are paying something, and that cost directly reduces your profit potential. You keep 100% of whatever premium remains at expiry within the middle strike boundaries.

An **iron butterfly** generates income. If volatility is high, the two middle legs sell for fat premiums, and the cost is minimal (a small debit to buy the wings). In a $100 stock example, you might collect $3–$4 per butterfly, or $300–$400 total. However, you are now short premium, and that debt is your risk. If the stock moves sharply, that short middle leg can lose money fast.

| Metric | Long Call Butterfly | Iron Butterfly |
|--------|---|---|
| **Capital deployed** | $50–$150 per butterfly | $0–$100 margin requirement per butterfly |
| **Upfront cost** | Spent immediately | Credit received immediately |
| **Profit realization** | At expiry, from theta decay | During trade, from decay; sold to lock gains |
| **Buying power used** | Minimal (debit paid) | Significant (credit short legs exposed) |

For a trader with limited capital, the call butterfly is more accessible: you risk only what you spend. For a trader with margin and conviction, the iron butterfly offers higher returns on capital.

## Profit and Loss Zones

Both butterflies profit most when the stock finishes *exactly* at the middle strike. The profit zone widens between the middle legs' strike prices.

**Long call butterfly example:** Buy 95, sell 100 (×2), buy 105. The maximum profit is $5 (the width of the outer strikes) minus the $0.50 debit = $4.50, or $450 per butterfly. This maximum profit occurs if the stock finishes anywhere between 100 and 100 at expiry. Outside this zone, profits decline. If the stock finishes below 95 or above 105, you lose the full debit ($50).

**Iron butterfly example:** Buy 90 put, sell 95 (×2), sell 105 call, buy 110 call. The maximum profit is the $5 width minus the $3 credit received = $2, or $200 per butterfly. But this is also the maximum loss if the stock moves far out-of-the-money in either direction: the short 95 put or short 105 call will blow through the long wing, and the loss is capped at $5 – $3 = $2 per butterfly, or $200.

Wait—that's not right. Let me recalculate. The width is typically $5. Iron butterfly width = $300 maximum loss minus $300 credit received = $0, if strikes are evenly spaced. But practically, the credit is less. If credit = $200, max loss = $300 – $200 = $100. The long wing costs money that the short wing doesn't recoup, so the max loss on an iron butterfly is wider than the width minus credit.

Actually, for clarity: **On an iron butterfly, max loss = width of outer strikes minus net credit received.** For the wings: if the stock crashes below the long put strike or rises above the long call strike, the entire width is lost, minus what you collected in credit.

## Assignment Risk and Management

**Long call butterfly:** Only the two short middle calls can be assigned. If the stock rises above 100 before expiry and the calls are assigned, you must deliver shares. But you don't own shares—you only own the 95 and 105 calls. The assignment forces you to exercise your long calls to cover, turning a nice closed trade into a stock position (or closed position in the long call) you didn't plan. This is manageable if you act fast; most brokers auto-exercise longs to cover shorts. But it disrupts your P&L and timing.

**Iron butterfly:** Both the short put (if stock crashes) and the short call (if stock soars) can be assigned. The short put assignment forces you to buy 100 shares; the short call assignment forces you to deliver 100 shares (if assigned, you must cover the put first or it will create a short stock position). Iron butterflies have *higher* assignment friction because they are half puts and half calls.

To avoid assignment, both strategies require active management near expiry. You can roll the middle legs to a future month if you want to extend, or close the entire butterfly to lock in gains before expiry chaos.

## Margin and Leverage

**Long call butterfly:** You paid the debit upfront, so margin is modest. Brokers require only the debit amount (maybe with a small buffer). If you fund 10 butterflies for $500 total, you need $500 cash + a tiny cushion.

**Iron butterfly:** You received a credit, so the broker views this as short premium you owe. The margin requirement is the maximum loss—the width of the strikes minus the credit. If the width is $10 and you collected $3, the margin requirement is $7 per share, or $700 per butterfly. For 10 butterflies, you need $7,000 in margin buying power available. This can balloon your exposure and force a liquidation if other positions decline.

## Tax Treatment and Wash Sales

Both strategies are complex for tax reporting. Each leg is a separate [option contract](/option/) and trades are reported on [Schedule D](/schedule-d/). If you close the butterfly before expiry, you realize a gain or loss immediately. If it expires, assignment can trigger stock sales (long calls exercised, short calls assigned) that carry [capital gains](/long-term-capital-gain-tax/) implications.

Be aware of [wash-sale](/wash-sale/) rules if you close a losing butterfly and immediately reopen a similar position. The IRS considers these related trades.

## When to Use Each

**Choose a long call butterfly if:**
- You have limited capital or margin availability.
- You want a clear, defined maximum loss (the debit paid).
- You believe the stock will move to the middle strike but want to avoid the margin overhead of iron butterflies.
- You are selling near-the-money premium to finance the outer legs (collecting credits on the wings is a bonus).
- You prefer to think in terms of debit cost rather than credit exposure.

**Choose an iron butterfly if:**
- You have good margin availability and want to maximize return on capital.
- You believe volatility will contract and the stock will settle near the middle strike.
- You want to collect premium upfront and are comfortable with active management.
- You can afford the higher margin requirement and potential assignment.
- You prefer to harvest theta decay by selling the middle legs short, betting on contraction.

## Comparing Across Conditions

| Market Condition | Long Call Butterfly | Iron Butterfly |
|---|---|---|
| **Rising volatility** | Debit costs less to open; wings gain value | Credit shrinks; harder to close profitably; risk rises |
| **Falling volatility** | Debit grows; theta help slower | Credit shrinks more; max profit capped; easy win if range-bound |
| **Stock soars** | Limited loss (outer call); whole spread losable | Lose entire width minus credit |
| **Stock crashes** | Limited loss (outer call); whole spread losable | Lose entire width minus credit |
| **Stock stalls at middle** | Max profit (width – debit) | Max profit (width – credit); easier to reach |

## Rolling and Early Exit

Both strategies benefit from closing early rather than holding to expiry. If the stock sits near the middle strike by the second or third week, theta decay (especially of the short middle leg) creates profit. You can close the entire butterfly for a gain and redeploy the capital to a new position.

Rolling is possible on both: you can close the current position and open a new one at different strikes and dates. This is especially useful if your original middle strike is no longer the target.

## Common Errors

**Overstaying expiry.** Holding a butterfly into the final days of expiry creates assignment ambiguity and execution risk. Professionals usually close by day 3 to 7 before expiry.

**Underestimating margin on iron butterflies.** A 10-butterfly iron butterfly can lock up $10,000+ in margin, leaving you vulnerable if your other positions decline.

**Setting the middle strike wrong.** If you are wrong about where the stock will trade, the butterfly's profit zone is entirely off-target, and you lose the full cost (call butterfly) or max loss (iron butterfly).

**Ignoring implied volatility.** A rising volatility environment eats iron butterfly profits and inflates call butterfly costs. Selling iron butterflies into rising vol is dangerous; buying call butterflies into high vol is pricey.

## See also

<div class="wiki-seealso">

### Closely related

- Option Strategies — overview of spreads and multi-leg trades
- [Iron Condor](/iron-condor/) — wider butterfly with four different strikes
- [Covered Call on LEAPS](/covered-call-on-leaps/) — alternative income strategy
- [Options Wheel Strategy Explained](/options-wheel-strategy-explained/) — cyclical premium collection
- [Protective Put vs Collar](/protective-put-vs-collar-strategy/) — hedge alternatives

### Wider context

- [Option Premium](/option-premium/) — theta decay and time value
- [Implied Volatility](/implied-volatility/) — pricing and trade setups
- [Theta](/theta/) — time decay mechanics
- [Assignment](/assignment/) — exercise and obligation rules
- [Margin](/margin-call-forex/) — leverage and capital requirements

</div>
