---
title: "Debit Spread vs Credit Spread: Breakeven and Risk Compared"
description: "Compare debit spreads and credit spreads: how breakeven, max profit, and margin requirements differ for bullish and bearish positions."
keywords:
  - debit spread vs credit spread
  - spread breakeven point
  - bull call spread
  - bear call spread
  - option strategy comparison
  - spread risk management
---

*A **debit spread** and a **credit spread** with the same strikes but opposite flows have mirror-image breakevens, maximum profits, and capital requirements. The debit spread costs cash upfront and profits if the [underlying](/stock/) moves in your direction; the credit spread collects premium upfront and profits if the underlying stays within a range, but the max loss is larger and requires margin.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Debit vs Credit Spread — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Debit spreads cost money and have defined max loss; credit spreads earn money and have larger max loss.</div>

|   |   |
|---|---|
| **Debit spread** | Buy near-the-money option, sell out-of-the-money; net debit (cash paid) |
| **Credit spread** | Sell near-the-money option, buy out-of-the-money; net credit (premium received) |
| **Max profit (debit)** | Width of strikes minus debit paid |
| **Max profit (credit)** | Credit received (width minus the long hedge) |
| **Max loss (debit)** | Debit paid (the premium you spent) |
| **Max loss (credit)** | Width of strikes minus credit received; much larger |
| **Breakeven (bull call)** | Long strike + net debit, or short strike − net credit |
| **Margin required** | Debit: none (paid in full); credit: max loss (set aside by broker) |

</aside>

## Debit Spread Mechanics and Breakeven

A **bull call spread** (the most common debit spread) pairs a long call and a short call at higher strike. Example: stock trades at $100.

- Buy the $100 call for $5
- Sell the $105 call for $2
- **Net debit: $3** (you pay $3 upfront)

Your breakeven is $100 + $3 = **$103**. If the stock lands at $103 at [expiration](/expiration-date/), the $100 call is worth $3 and the $105 call is worthless, so your spread is worth $3, offsetting the $3 paid. Below $100, both calls expire worthless and you lose the full $3. Above $105, the spread is worth the max $5 (the strike width), so your profit caps at $5 − $3 = $2.

The **debit paid upfront** is your entire risk. You have [defined max loss](/derivatives-hedging/). This is why debit spreads appeal to traders with limited capital: no margin call, and you know your ceiling loss on day one.

Bullish breakeven is **long strike + net debit**. The debit — the price of the hedge (your long call's cost minus the short call's credit) — is added to the long strike to find the exact price where P&L turns positive.

## Credit Spread Mechanics and Breakeven

A **bear call spread** (the most common credit spread) flips the structure: sell the lower call, buy the higher call as protection.

- Sell the $100 call for $5
- Buy the $105 call for $2
- **Net credit: $3** (you receive $3 upfront)

Your max loss is the strike width minus the credit: $5 − $3 = $2. Your breakeven is $100 + $3 = **$103**. 

Wait—that is the same breakeven as the bull call spread, but the **logic inverts**. In a credit spread, you *profit* if the stock stays below your breakeven. At $103, the short $100 call loses $3, but you received $3 in premium, so net P&L is zero. Below $100, both calls expire worthless and you keep the full $3 credit. Above $105, the spread loses the max $2.

The critical difference: in a **debit spread, you need the stock to move favorably for profit**. In a **credit spread, you profit if the stock does nothing or moves slightly against you**.

## Breakeven Formula Generalized

For any [spread](/derivatives-hedging/) with strikes S₁ (long) and S₂ (short):

- **Bull call (debit)**: Breakeven = S₁ + (long cost − short credit)
- **Bear call (credit)**: Breakeven = S₁ + (short credit − long cost)
- **Bear put (debit)**: Breakeven = S₂ − (long cost − short credit) — buying put protection is a debit
- **Bull put (credit)**: Breakeven = S₂ − (short credit − long cost) — selling put premium is a credit

In all cases, the width (S₂ − S₁) sets the max profit for a debit spread and the max loss for a credit spread.

## Capital and Margin Consequences

**Debit spreads** require no margin. You pay the debit upfront and own the position outright. A $3 debit on a 100-share contract costs $300 cash. Your broker holds no additional capital against the position.

**Credit spreads** tie up margin. A broker must reserve capital equal to the maximum loss. In the bear call example, max loss is $2 per share, or $200 on a contract. Your broker freezes $200 of margin for the duration. If you sell ten bear call spreads, you lock up $2,000. This can become a significant constraint if you trade many simultaneous credit positions.

Some brokers allow "portfolio margin" — a more sophisticated calculation that nets long and short offsets — lowering the margin required. But standard margin typically ties up the full max-loss width.

## Profit Profile and Volatility Sensitivity

**Debit spreads** have a one-sided profit zone. A bull call spread profits only if the stock rallies above breakeven. It does not benefit from [volatility](/implied-volatility/) drops; you are paying for volatility in your long call and selling it in your short call, often netting to a small [vega](/vega/) exposure.

**Credit spreads** profit in a two-sided zone: if the stock stays in the middle and [volatility](/implied-volatility/) falls, the short call loses value faster than the long call, widening your margin of safety. High volatility helps credit spreads at entry (you sell expensive premium) but hurts them closer to expiration if the stock has moved far.

A trader bullish on a stock but short on volatility should consider debit spreads. A trader bullish on *non-movement* — whether neutral or expecting range-bound chop — prefers credit spreads.

## Adjustments and Assignment Risk

**Debit spreads** have no early assignment risk on the short side: you are short a call above the current price, and nobody exercises a call worth less than the strike. At expiration, if the stock is between strikes, your short call expires worthless and only your long call might be in the money.

**Credit spreads** can face early assignment if the short call goes deep in the money (usually when [dividends](/dividend/) are imminent). Brokers may assign your short call, forcing you to sell the stock — and if the long call hasn't moved proportionally, you are left with an unhedged short position momentarily. Most brokers handle this automatically, but it is a risk to understand.

## Choosing Between Them

Prefer **debit spreads** if you have high conviction in direction, want defined max risk, or have limited margin. Prefer **credit spreads** if you profit on range-bound action, have ample margin, and want to capture [theta decay](/time-decay-theta/).

The breakeven, max profit, and max loss are not better or worse — they match the two sides of a zero-sum bet. One trader's sold debit spread is another's bought credit spread.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Option](/call-option/) — the long and short legs in these spreads
- [Put Option](/put-option/) — similar spreads exist for puts (bull put, bear put)
- [Option Premium](/option-premium/) — what you pay or receive
- [Time Decay (Theta)](/time-decay-theta/) — credit spreads benefit, debit spreads are neutral
- [Implied Volatility](/implied-volatility/) — affects the initial cost/credit and edge for each strategy
- [Derivatives Hedging](/derivatives-hedging/) — spreads as a structured risk management tool
- [Strike Price](/strike-price/) — the two prices that define the width and risk

### Wider context

- [Option](/option/) — foundational instrument
- [Volatility Smile](/volatility-smile/) — why different strikes have different implied vols
- [Expiration Date](/expiration-date/) — when the spread settles
- [Value at Risk](/value-at-risk/) — quantifying max loss for position management

</div>
