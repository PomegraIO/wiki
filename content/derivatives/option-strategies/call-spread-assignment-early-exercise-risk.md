---
title: "Early Assignment Risk in a Call Spread"
description: "Early assignment risk in call spreads: when the short call gets exercised before expiration, especially around dividend dates, and how to manage the resulting gap."
keywords:
  - call spread early assignment
  - short call assignment
  - dividend early exercise
  - call spread dividend risk
  - option assignment
---

*A **call spread** exposes the short call leg to early [exercise](/exercise-price/), particularly around dividends, potentially capping profit while leaving the long call unexercised and vulnerable to losses. Early assignment transforms a hedged position into an unhedged short call, forcing position management or losses.*

<div class="wiki-hatnote">

This article assumes a bull call spread (long lower-strike call, short higher-strike call). For put spreads or other structures, assignment dynamics differ.

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Early Assignment in Call Spreads — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Early assignment happens when your short call is exercised before expiration, usually to capture a dividend or when the option is deep in the money.</div>

|   |   |
|---|---|
| **Primary trigger** | Stock dividend ex-date; short call is deep in the money |
| **Why it happens** | Call holder captures the dividend by exercising and owning shares |
| **Your exposure** | Short 100 shares at the strike; long call cannot be exercised early |
| **The risk** | Stock gaps down on ex-date; long call now protects a loss you didn't authorize |
| **Typical outcome** | Forced to close early at a loss or roll to adjust |
| **When it's rare** | Out-of-the-money calls or calls far from ex-dates; American options only |

</aside>

## Why early assignment happens: the dividend effect

American [call options](/call-option/) (not European) can be exercised at any point before expiration. A rational call holder exercises early only if the benefit exceeds what they'd get holding the option to expiration. The most common trigger: a large dividend.

Consider this scenario. XYZ stock trades at $105. You sold a 100 call and bought a 110 call (a call spread). The next day, the company announces a $2 dividend payable to shareholders of record on a date three weeks away. The ex-date—when the stock price adjusts downward by roughly the dividend amount—is in two weeks.

A trader holding your short 100 call now faces a choice:

1. Hold the option, wait for ex-date, and the stock drops $2 (they lose $2 per share on an existing position, if they hold stock).
2. Exercise the call, own 100 shares at $100, collect the $2 dividend, and sell the stock after ex-date.

If the call is in the money and the dividend is large, option (2) is optimal. The call holder exercises. You are assigned and own 100 shares short at $100 strike price.

## The mechanics of assignment

When assignment occurs, you are obligated to deliver 100 shares at the strike price. For a short call, this means you sell shares at $100. If you do not already own the shares, you go short the stock (borrowing and selling).

The core issue: your long call (the 110 strike) is now orphaned. It no longer hedges you. You are short 100 shares of XYZ and holding a 110 call—a protective put on a short position—but you never intended to be short stock outright.

**Scenario unfolds:**

- XYZ at $105 pre-assignment, your spread makes max profit at expiration if XYZ stays $100–$110.
- Assignment on ex-date; you sell 100 shares at $100 to fulfill the short call.
- Stock drops $2 on ex-date to $103 (dividend payout).
- You are now short 100 shares at $100, with XYZ at $103. Your $110 long call is worthless protection.
- Stock then rallies to $112. You incur a $12 loss per share ($1,200 on the 100 shares short), constrained only by the $110 call.

Without the call, you'd lose $12 per share. The call saves you; it limits loss to $2 per share. But you never wanted to be short stock in the first place—the spread was designed to cap risk at the difference between strikes minus the net debit paid.

## When early assignment is most likely

**Dividend timing.** Assignment risk peaks around ex-dates. If your short call is in the money and the ex-date is approaching, assume assignment will occur. Traders holding ITM calls for dividend capture are highly motivated to exercise.

**Depth in the money.** A call that is $5 in the money (intrinsic value $5 per share) has little time value left. The holder has nothing to lose by exercising—they get the dividend, own shares, and the option expires worthless anyway.

**Interest rates.** If risk-free rates are high, the cost to borrow money to hold stock (instead of buying the call) increases. A holder might prefer to exercise and own shares rather than hold the call through ex-date.

**American vs European.** Early assignment is only possible on American-style options. European options can only be exercised on the final day. Most index options (SPX, RUT) are European; stock options are American. Futures options are often European or have limited early exercise windows.

## Managing assignment before it happens

**Close the spread early.** If you see dividend ex-dates approaching and your short call is in the money, close both legs of the spread and take your profit before assignment risk materializes. This eliminates the gap.

**Roll the short call.** Sell a call at a later expiration date (one that expires after the ex-date) and use the premium to buy back the current short call. You push assignment risk into the future and adjust the strike if needed.

**Leg out strategically.** Some traders close the short call only, pocketing the rebate and accepting unlimited upside risk temporarily. This is risky and should only be used if you plan to close the long call immediately or believe the stock will not spike.

**Let it happen and rebalance.** If you have cash or dry powder, you can accept assignment, buy back the 100 shares immediately (closing your short position), and keep the long call. You've converted the spread into a long call. This works if you still believe in upside.

## What happens after early assignment

You are assigned on a Wednesday afternoon. Your broker delivers 100 shares short on your account. Your long 110 call is still alive and active.

**Your choices:**

1. **Buy 100 shares immediately.** You realize a loss equal to the difference between your short strike and the current stock price, minus the long call's intrinsic value. If short at $100 and stock is at $105, you lose $5 per share ($500 total), but your 110 call saves you from worse loss if stock rallies.

2. **Hold the short position through expiration.** This is risky. Stock volatility can exceed the width of the spread. Your 110 call caps loss, but you are exposed to stock lending costs, dividend obligations on short shares, and potential forced buybacks if the stock becomes hard to borrow.

3. **Let your long call cushion you and hope for mean reversion.** If you have conviction the stock will fall back below $100, you can hold short 100 shares protected by the 110 call. But this abandons your original spread strategy.

## Calculating the damage

**Pre-assignment spread PnL assumption:**
- Bought 110 call for $0.50
- Sold 100 call for $2.00
- Net debit: $0.50 ($50 per contract)
- Max profit at $100–$110: $5 − $0.50 = $4.50 per share ($450 total)

**Assigned at $105 with long call at $2.00 ITM:**
- You are short 100 shares at $100.
- Long 110 call is worth $2.00 intrinsic.
- Stock is $105.
- Intrinsic loss on short call: $5 per share ($500).
- Long call covers up to $2 of that ($110 strike − $100 strike − debit).
- If you close immediately: lose $5 per share, net $3.50 after the long call's protection.
- vs. expected max profit of $4.50 pre-assignment: you've surrendered $8 per share.

## How to avoid it entirely

**Trade European-style options:** Sell call spreads on European-style indices (SPX, RUT) or on stocks with near-term expirations. European options cannot be exercised early, so assignment risk is zero before expiration.

**Use expirations after ex-dates.** If the ex-date is in two weeks, use a four-week expiration for the short call. The option holder is less motivated to exercise early if the ex-date is far away and time value remains.

**Out-of-the-money spreads.** If your short call is OTM, the probability of early assignment is near zero. The assignment risk is directional: it rises sharply as the short call moves ITM.

**Earnings dates.** Many traders avoid holding spreads through earnings because volatility and big moves can trigger unwanted assignment. Close spreads 2–3 days before earnings.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — the instrument being exercised early
- [Option assignment](/option/) — what happens when your sold option is exercised
- [Call spread assignment early exercise risk](/call-spread-assignment-early-exercise-risk/) — this article
- [Dividend](/dividend/) — the trigger for most early assignments
- [Exercise price](/exercise-price/) — the strike at which assignment occurs

### Wider context

- [Option strategy](/option/) — spreads and hedges
- [American vs European options](/option/) — exercise windows and early assignment
- [Greeks and theta](/theta/) — time decay and dynamic management
- [Risk management](/option/) — position management around corporate events

</div>
