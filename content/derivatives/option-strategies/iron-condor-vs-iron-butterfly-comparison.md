---
title: "Iron Condor vs Iron Butterfly: Key Differences"
description: "Compare iron condor and iron butterfly risk/reward profiles, breakeven widths, and when each fits expected volatility."
keywords:
  - iron condor vs iron butterfly difference
  - iron condor strategy
  - iron butterfly strategy
  - option spreads
  - vertical spread comparison
image: "/svg/derivatives.svg"
---

*Both the **iron condor and iron butterfly** are neutral income strategies built from two vertical spreads, but they differ in the width between the short strikes and the range of price stability they require. The iron condor tolerates wider price swings; the iron butterfly bets on tighter containment. Understanding the trade-offs between their maximum payoff, breakeven widths, and volatility assumptions determines which fits your outlook.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Iron Condor vs Iron Butterfly — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Same structure, different width; choose based on expected price range and volatility regime.</div>

|   |   |
|---|---|
| **Iron Condor strike width** | 5–15 points (or 1–2 standard deviations) |
| **Iron Butterfly strike width** | 1–2 points (narrow, at-the-money) |
| **Max profit condor** | Premium collected minus cost of long legs |
| **Max profit butterfly** | Smaller absolute dollars; collected at midpoint |
| **Breakeven range** | Condor: wide; butterfly: tight near short strikes |
| **Volatility outlook** | Condor: low-to-moderate; butterfly: very low |
| **Capital required** | Butterfly typically lower per contract |

</aside>

## The Structure: Same Framework, Different Distances

Both strategies combine one [call spread](/option/) and one [put spread](/option/) to cap profit and limit loss on both sides:

**Iron Condor**
- Sell an out-of-the-money (OTM) call at strike A
- Buy a further OTM call at strike B (as a hedge)
- Sell an OTM put at strike C
- Buy a further OTM put at strike D (as a hedge)

**Iron Butterfly**
- Sell an at-the-money (ATM) or near-ATM call at strike X
- Buy a further OTM call at strike Y (tight collar)
- Sell an ATM or near-ATM put at strike Z
- Buy a further OTM put at strike W (tight collar)

The mechanical difference: in the iron butterfly, the short call and short put are (or are nearly) at the current stock price, and the distance to the long legs is minimal. In the iron condor, both short strikes sit well away from current price, and the width is wider.

## Risk and Reward: The Central Trade-Off

**Iron Condor: Smaller Premium, Wider Safety Margin**

A condor collects less [premium](/option-premium/) per contract because the short strikes are far from where traders expect the stock to trade. If you sell a call 20 points above the stock and a put 20 points below, you're betting on calm—not zero movement, but not chaos. A $1.50 credit might be typical.

Your maximum profit is $1.50 per contract (or $150, since options standardly cover 100 shares). But you keep it if the stock stays anywhere between the two short strikes at expiration. The range is generous: perhaps 40 points wide.

**Iron Butterfly: Larger Premium, Razor-Thin Safety Zone**

A butterfly collects more premium per contract because the shorts sit right at expected price. You might collect $3.00 on a narrow 2-point butterfly. Your max profit is higher in absolute terms—$300 per contract.

But—and this is the catch—you lose money the moment the stock drifts beyond the short strikes. If the stock rallies 3 points, you still own only 2 points of call spread width. The long call at +2 is now 1 point in-the-money, reducing your profit by $100. At 4 points, you've lost half your profit. At 5 or higher, you're down money.

The breakeven is tighter. On a 2-point butterfly, your profit zone might be just 2–4 points. Venture further, and losses mount quickly.

## Volatility Regime and Stock Behavior

**Iron Condor for Elevated Volatility**

Condors thrive when you expect the stock to meander—the classic post-earnings pattern or a period of indecision. Elevated [volatility](/volatility-smile/) actually *helps* the condor: it inflates the price of the long hedges you buy, improving your cost. High-volatility names allow you to space the short strikes far apart while still collecting decent premium.

If the stock then sits tight, you profit from decay in the [theta](/theta/) (time value) you sold. If it drifts slowly toward one side but stops before hitting your long strike, you still profit.

**Iron Butterfly for Very Low Volatility**

Butterflies target periods of expected calm—after a major announcement, or when a stock settles into a tight consolidation. You assume very little movement and collect premium accordingly.

In a low-volatility environment, the ATM options are cheap, so your long hedges cost less. That spreads the margin between credit collected and cost paid.

However, any unexpected volatility spike or surprise earnings beat will punish the butterfly. You're short gamma; [gamma risk](/gamma/) (the rate at which delta changes) accelerates losses if the stock accelerates.

## Breakeven Width and Margin of Safety

Suppose Apple trades at $150.

**Iron Condor Example:**
- Sell 150 call, buy 155 call
- Sell 145 put, buy 140 put
- Collect $1.50
- Profit zone: $143.50 to $151.50 (8-point buffer on the downside, 5.50 on the upside)

**Iron Butterfly Example:**
- Sell 150 call, buy 152 call
- Sell 150 put, buy 148 put
- Collect $3.00
- Profit zone: $147.00 to $153.00 (3-point buffer on each side)

The butterfly's tighter margin means it requires higher conviction—or a much shorter holding period to reduce time decay. The condor's wider zone means you can be more wrong and still profit, but you collect less per contract.

## Greeks and Risk Management

**Iron Condor Greeks**

The net [delta](/delta/) of a condor is near zero (neutral). [Gamma](/gamma/) is also mildly negative. [Vega](/vega/) is short (you benefit from falling volatility). Theta is positive (you collect daily decay).

The key: gamma risk is gradual. If the stock moves 3 points, your delta begins to shift noticeably, but losses are still modest. You have room to adjust (close the losing side early, roll strikes higher or lower).

**Iron Butterfly Greeks**

The butterfly is also delta-neutral and short gamma, but gamma is much steeper near the short strikes—the core of the position. A 2-point move can flip your [theta](/theta/) from positive to negative if the stock overshoots.

Vega is similarly short, but a volatility spike has a faster impact on a butterfly's profitability because the shorts are at-the-money, where vega is highest.

## Choosing Between Them

**Use the Iron Condor if:**
- You expect the stock to be calm but not frozen
- Implied volatility is elevated or you want a wide safety margin
- You can tolerate collecting smaller premium in exchange for lower maintenance
- You're managing the position over days or weeks

**Use the Iron Butterfly if:**
- You're confident the stock will barely move
- Implied volatility is very low and ATM options are cheap
- You're willing to monitor the position closely (or planning a short duration)
- You want maximum absolute profit on a contained range

## Adjustments and Exit Timing

**Condor adjustments** are forgiving. If the stock rallies toward your short call, you can close that call spread early for a small profit, leaving the put side open. The position flexes.

**Butterfly adjustments** are more binary. If the stock drifts toward a short strike, rolling or closing is often cleaner than trying to repair the skew. The narrow margin makes partial exits less intuitive.

Most traders exit condors at 50% of max profit (good efficiency) and sometimes let them ride closer to expiration. Butterflies are often closed once they hit 75% profit or at 7–14 days before expiration, to avoid a gamma event.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — foundational structure and terminology
- [Call Option](/call-option/) — definition and mechanics
- [Put Option](/put-option/) — definition and mechanics
- [Delta](/delta/) — direction sensitivity of option price
- [Gamma](/gamma/) — curvature and acceleration of delta
- [Theta](/theta/) — time decay of option value
- [Vega](/vega/) — volatility sensitivity of option price
- [Implied Volatility](/implied-volatility/) — market's forecast of future price swings

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — risk management via options and spreads
- [Vertical Spread](/option/) — two-leg [option](/option/) structure
- [Volatility Smile](/volatility-smile/) — how implied volatility varies across strikes
- [Options Expiration](/expiration-contracts/) — settlement and time decay dynamics

</div>
