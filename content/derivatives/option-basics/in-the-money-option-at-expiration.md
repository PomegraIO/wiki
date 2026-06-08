---
title: "What Happens to an In-the-Money Option at Expiration"
description: "When an in-the-money option expires, the holder must decide: automatic exercise, cash settlement, or let it lapse—but brokers often exercise to protect holder value."
keywords:
  - what happens to in the money option at expiration
  - in the money option at expiration
  - option exercise at expiration
  - automatic option exercise
  - option assignment risk
image: /svg/derivatives.svg
---

*When an **in-the-money option expires**, the holder's broker typically exercises it automatically to preserve intrinsic value, but the rules and timing differ by exchange and brokerage. A call that's $1 in the money and expires tomorrow is worth at least that $1 of intrinsic value; surrendering it is a loss. Yet timing, cash requirements, and gap risk mean exercising at expiration is not always straightforward.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">In-the-money option at expiration — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Automatic exercise protects intrinsic value, but the holder must manage cash, assignment risk, and trading halts.</div>

|   |   |
|---|---|
| **Automatic exercise** | Most brokers auto-exercise ITM calls and puts; the holder receives no separate notice |
| **When it happens** | Typically Friday after-hours or Saturday morning if expiry is Friday; same-day morning for mid-week expiry |
| **Intrinsic value** | Exercised call: you buy shares at strike (must have cash or margin); put: you sell shares (or buy to cover) |
| **Assignment risk** | If short a call/put, you may be assigned before expiry; early assignment is possible on American-style options |
| **Cash or margin required** | Exercising a call ties up buying power; put exercise generates cash (or requires shares to deliver) |
| **Fees** | Exercise fees typically $0–$10 per contract; some brokers waive for retail customers |
| **Gap risk** | Stock gaps against you overnight or across a weekend; intrinsic value at expiry may be less than at market close |

</aside>

## How Automatic Exercise Works

When an option expires in the money, most US brokers **automatically exercise it** for retail and institutional customers unless the customer has explicitly requested "do not exercise" instructions. This happens on the [expiration date](/expiration-date/) itself, well after market close. For Friday expirations, the exercise window is typically Saturday morning (for settlement on Monday or Tuesday, depending on whether it's a call or put).

The automatic exercise process is straightforward:
- **Call is ITM**: your broker converts it to a long stock position at the strike price, charging your cash account or applying margin.
- **Put is ITM**: your broker converts it to a short stock position at the strike price, crediting your account with proceeds or immediately buying to flatten the short (depending on your margin availability).

The broker does this *automatically* because allowing an option to expire worthless when it has intrinsic value would be negligent. Regulators and industry standards expect brokers to protect customer assets. However, brokers *do* allow you to elect "do not exercise" in advance if you want to let the option expire; you must initiate that request, and some brokers charge a fee or limit when you can submit it.

## The Timing and Settlement

Expiration Friday (or the final trading day of each month) has specific rules:
- **Options stop trading** at 4:00 p.m. ET; the final settlement is determined by the official settlement price, which is usually the opening price (or volume-weighted opening price) of the underlying on expiration day.
- **Brokers have until Saturday morning** to decide which ITM options to exercise. Most exercise automatically unless instructed otherwise.
- **Stock settlement** for the exercise occurs 2 business days later (T+2): so a Friday expiration exercise results in stock delivery on Monday (if expiration is Thursday, delivery is Saturday, which rolls to Monday).

This timing matters because the stock can **gap substantially between Friday close and Monday open**. An option that is $0.50 ITM at Friday's 4:00 p.m. close might be $2 OTM by Monday's open if the company announces bad news over the weekend. You're still obligated to buy (or sell) at the strike; you cannot cancel after automatic exercise.

## Intrinsic Value and Assignment Mechanics

The **intrinsic value** of an ITM option at expiration is the only value remaining:
- **Call**: max(stock price − strike, 0). A $55 stock with a $50 call strike is $5 ITM.
- **Put**: max(strike − stock price, 0). A $45 stock with a $50 put strike is $5 ITM.

When your broker exercises, that intrinsic value is converted to a stock position. The intrinsic value is *yours to keep*—it's the profit or hedge you've locked in. But exercising requires you to settle the transaction:

| Option Type | Action | You Must | You Receive/Deliver |
|---|---|---|---|
| Long Call (ITM) | Exercised | Pay strike × 100 per contract | 100 shares at strike price |
| Long Put (ITM) | Exercised | Deliver 100 shares (or buy to cover) | Receive strike × 100 in cash |
| Short Call (ITM) | Assigned | Deliver 100 shares | Receive strike × 100 in cash |
| Short Put (ITM) | Assigned | Pay strike × 100 | Receive 100 shares |

If you are **short an ITM option**, the opposite happens: your position is assigned. You do not control the timing; assignment can happen anytime during the option's life (for American-style options), not just at expiration. If you're short a call and it's $2 ITM, you may be assigned early if the underlying pays a dividend—the long call holder exercises to capture the dividend, and you're forced to deliver shares. This is a real risk: you could be forced out of your position suddenly, potentially at an inopportune time.

## Gaps and Price Risk at Expiration

One often-underestimated risk at expiration is the **overnight or weekend gap**. An option might be solidly ITM at Friday's 4:00 p.m. close, but a market-moving announcement (earnings miss, geopolitical event, regulatory action) releases after hours, and the stock gaps down sharply at Monday's open. Your broker has already auto-exercised you; you're locked in at the strike, and the stock is now trading below it.

Example: You own a $100 call option on a $102 stock on Friday, 4:00 p.m. close. The option is $2 ITM. Your broker auto-exercises, assigning you the obligation to buy 100 shares at $100 on Monday. Over the weekend, the company receives a material warning letter from the FDA. The stock opens Monday at $88. You are required to buy at $100; you've now immediately lost $12 per share, or $1,200 per contract, despite holding an ITM option.

This is why many traders who expect volatility around expiration prefer to **close the option before market close on Friday** rather than hold to auto-exercise. You lock in the Friday close price and avoid weekend gap risk.

## Opting Out of Automatic Exercise

Most brokers allow you to elect "do not exercise" (DNE) or "liquidate on expiration" (LOE), which closes the option position instead of exercising it. The mechanics:
- **DNE**: the option expires worthless (if OTM) or is simply closed (if ITM), and you receive no stock position or cash.
- **LOE**: your broker automatically sells the option at market value in the final minutes of trading on expiration Friday.

Some brokers also offer a **cash settlement option** for broad-based index options, which are often cash-settled rather than physically delivered (e.g., the [SPX](/sp-500-index/) index options), eliminating the need to buy or sell shares.

You must request DNE or LOE *before* the close on expiration day, and some brokers have earlier deadlines (e.g., 2:00 p.m. ET). Check your broker's policy.

## Assignment Before Expiration

If you are **short an option**, you face the risk of **early assignment**, which can occur any trading day up until expiration (for American-style options; European-style options can only be exercised at expiration). This is most common for short calls on stocks paying a dividend: the long call holder exercises early to capture the dividend, and you are assigned shares.

Early assignment can be inconvenient if you wanted to let the position ride or were banking on theta decay to close out the option for a smaller loss. Unlike expiration, where your broker auto-exercises *your* long position, assignment of a short position happens at the discretion of the counterparty.

To avoid early assignment of a short call, many traders **buy to close** (repurchase) the short call before the dividend date or before expiration, locking in a profit (or loss) and eliminating assignment risk.

## Practical Considerations for Holders

If you hold a long ITM option, the decision to exercise or let your broker auto-exercise is usually **moot** (your broker exercises, you get the value). But if you're uncertain about the logistics, act early:
1. **Close the option in the market** if you want to avoid physical delivery or assignment risk. Selling a long call for its intrinsic value + any time value is usually simpler than exercising.
2. **Request DNE in advance** if you want to let it expire worthless (unlikely for a true ITM option, but possible if you're trying to tax-loss harvest or reposition).
3. **Ensure cash or margin availability** if you own long calls and expect auto-exercise; buying 100 shares per contract ties up capital.
4. **Monitor after-hours news** on expiration Friday; a gap can erase your intrinsic value over the weekend.

For short options, the only lever you have is to **buy to close before expiration** to eliminate assignment risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — Core mechanics of calls, puts, and time decay
- [Exercise Price](/exercise-price/) — The strike price and its role in ITM calculation
- [Intrinsic Value](/intrinsic-value/) — Why ITM options have value at expiration
- [Time Decay (Theta)](/time-decay-theta/) — Why the last day of trading is critical
- [Expiration Date](/expiration-date/) — When and how expiration unfolds

### Wider context

- [Call Option](/call-option/) — The specific contract type and exercise rights
- [Put Option](/put-option/) — Puts and their early assignment mechanics
- [Derivatives Hedging](/derivatives-hedging/) — Why traders use options and manage assignment
- [Volatility Smile](/volatility-smile/) — Option pricing on the final day

</div>
