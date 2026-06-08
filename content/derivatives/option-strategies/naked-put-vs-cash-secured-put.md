---
title: "Naked Put vs Cash-Secured Put: Margin and Risk"
description: "The key difference between naked puts and cash-secured puts: margin requirements, capital efficiency, and what happens when assignment occurs."
keywords:
  - naked put vs cash secured put
  - margin requirement put option
  - cash-secured put strategy
  - put option capital requirement
image: /svg/derivatives.svg
---

*A **naked put** ties up less capital than a **cash-secured put** because it relies on margin borrowing instead of idle cash—but the margin broker can demand that capital in an instant if the stock tumbles. A cash-secured put park the full strike price in cash beforehand, eliminating margin calls but forfeiting returns on that locked-up money.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Naked Put vs Cash-Secured Put — Key Differences</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for options and derivatives." />

<div class="wiki-infobox-caption">Both strategies profit when puts expire worthless, but differ radically in how much capital sits idle and what triggers a margin call.</div>

|   |   |
|---|---|
| **Capital at risk** | Naked put: margin requirement (e.g., 20%); cash-secured: full strike price |
| **Margin call risk** | Naked put: yes, if stock drops; cash-secured: no |
| **Capital efficiency** | Naked put: higher; cash-secured: lower |
| **Broker discretion** | Naked put: broker controls requirement; cash-secured: none (cash is held) |
| **Who uses this** | Naked put: margin-approved traders; cash-secured: retirement accounts, risk-averse sellers |
| **Assignment impact** | Both: receives stock at strike; naked put incurs margin debt, cash-secured converts cash to shares |

</aside>

## What Distinguishes the Two Strategies

The core separation hinges on *how much you must have on hand before entering the trade*.

A **naked put** relies on [margin](http://glossary-link-example) from your broker. You sell a put contract and the broker sets a margin requirement—typically 20–50% of the strike price times 100 shares—as collateral. If you sell a $50 put, your broker might demand $1,000–$2,500 of your account equity, depending on the stock's [volatility](http://glossary-link-example) and how much margin the broker allows. The other $3,500 (or more) of the strike price remains the broker's implicit bet on you; they're lending you purchasing power.

A **cash-secured put** locks up the full strike price in cash *before* you sell the contract. Selling that $50 put requires $5,000 in liquid, uninvested cash sitting idle in your account. The exchange or clearinghouse knows that capital is there, so there's no margin call risk.

## Why Margin Matters: The Call Mechanism

The critical vulnerability of a naked put is the [margin call](http://glossary-link-example). If the underlying stock drops sharply, your equity account can shrink faster than your margin requirement. The broker then demands you deposit more cash or liquidate holdings to restore the collateral ratio. A single severe gap down can trigger an unexpected funding crisis.

A cash-secured put never triggers a margin call because the cash earmark is fixed and separate from daily account swings. Your put obligation is mathematically fully funded from day one.

Consider a real example:
- You sell a naked $50 put on a stock trading at $52, with a 20% margin requirement ($1,000).
- The stock crashes to $40 in three days.
- Your account equity may have fallen, but more importantly, the option's [intrinsic value](http://glossary-link-value) is now $10 per share ($1,000 total), and the margin req often scales with moneyness. Your broker calls and demands additional margin.

If you're running multiple naked puts, a flash crash can wipe out your entire margin cushion in minutes, forcing liquidations at the worst prices.

With $5,000 in cash secured, the same drop just means the put gains value on paper—you sleep; no margin call, no forced selling.

## Assignment and What Happens Next

Both strategies sit on the same foundational risk once assignment occurs: you end up owning 100 shares at the strike price.

**Naked put assignment:** You receive stock and immediately have a long position financed via margin debt. You owe the broker whatever amount you initially didn't put up—in our example, the $4,000 you didn't fund yourself. This debt now accrues interest at the margin rate (typically 5–12%, depending on your broker and account size). You must either sell the stock, cover the margin debt with new deposits, or carry the position long-term as a financed holding.

**Cash-secured put assignment:** The $5,000 in cash converts to a $5,000 stock purchase (100 shares @ $50). You own the shares debt-free; no interest accrual. You can hold, sell, or immediately write calls against them.

The cash-secured route avoids leverage costs, but you've sacrificed five thousand dollars of opportunity—that cash could have been earning 4–5% in a money market [fund](http://glossary-link-example) instead of sitting dormant.

## Capital Efficiency and Returns

The naked put wins on *capital efficiency*. If you have $10,000, you might sell five naked $50 puts (requiring ~$5,000 in margin), and still have $5,000 free to deploy elsewhere—perhaps in dividend stocks, [bonds](http://glossary-link-value), or additional naked puts on other names. Your account works harder.

The cash-secured put ties up $25,000 to sell five $50 puts. If your account is only $10,000, you can't do it at all. But once you're in the trade, you sleep better; there's no liquidity spike that ruins your evening.

This efficiency trade-off explains why institutional [hedge funds](http://glossary-link-value) and professional option traders run naked strategies—they have risk management disciplines, margin monitoring, and the capital to absorb a margin call. Retail investors and [retirement accounts](http://glossary-link-example) (which often restrict margin) gravitate to cash-secured puts; the simplicity and elimination of forced selling outweigh the locked-up opportunity cost.

## Regulatory and Account Restrictions

Not all brokers permit naked puts. Margin accounts carrying naked puts require explicit options approval (usually "level 2" or higher on broker forms). Retirement accounts—[401k plans](http://glossary-link-example), [IRAs](http://glossary-link-example)—almost universally ban naked puts because retirement rules disallow margin lending. Cash-secured puts, framed as "covered" by cash reserves, are often allowed in IRAs at level 1 (basic options).

Brokers also differ in margin requirements. A volatile biotech stock might trigger a 50% requirement (naked put on a $50 strike requires $2,500), while a stable large-cap might sit at 20% ($1,000). This flexibility lets brokers calibrate risk, but it also means your naked put's capital demand can change without warning.

## Which Strategy Fits Your Situation

**Choose naked puts if:**
- You have margin approval, significant account size, and daily monitoring discipline.
- You want to maximize returns on limited capital.
- You're seasoned with [options Greeks](http://glossary-link-example) and can size positions to avoid forced liquidation.
- The underlying is liquid and moves predictably.

**Choose cash-secured puts if:**
- You're in a retirement account or margin is unavailable.
- You want to sleep undisturbed; margin calls create unplanned stress.
- You're building an income-generating strategy and can afford the locked-up cash.
- The underlying is volatile or thinly traded, and you want guaranteed stability.

Both strategies profit identically when the put expires worthless. The path to that outcome—and what happens if it goes wrong—is where the split widens.

## See also

<div class="wiki-seealso">

### Closely related

- [Covered Call](/covered-call/) — selling calls against owned stock to reduce capital lockup
- [Put Option](/put-option/) — the fundamental right to sell at a strike price
- [Protective Put](/protective-put/) — buying a put to hedge downside, the mirror image of put-selling
- [Option Premium](/option-premium/) — what you collect upfront for naked and secured puts
- [Strike Price](/strike-price/) — the price at which assignment occurs under both strategies
- [Margin Call](/margin-call-forex/) — how brokers enforce margin maintenance

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — broader strategies for managing risk
- [Leverage Ratio](/leverage-ratio-forex/) — how margin affects portfolio leverage
- Options Greeks — Delta and Theta drive put-selling profitability
- [Risk Weighted Assets](/risk-weighted-assets/) — regulatory capital standards that apply to institutions

</div>
