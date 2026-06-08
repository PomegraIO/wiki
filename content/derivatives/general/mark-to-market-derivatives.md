---
title: "Mark-to-Market in Derivatives"
description: "Daily revaluation of derivative positions to current market prices and associated collateral flows that manage counterparty and market risk."
keywords:
  - mark-to-market
  - daily settlement
  - variation margin
  - fair value
  - collateral
  - counterparty risk
image: "/svg/derivatives.svg"
---

*In derivatives trading, **mark-to-market** means repricing each position daily to its current market value and settling profit or loss immediately. This continuous valuation and cash settlement prevents large losses from building up undetected, limits [counterparty risk](/counterparty-risk/), and is the operational heartbeat of modern derivatives markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Mark-to-Market in Derivatives — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and financial instruments." />

<div class="wiki-infobox-caption">Real-time repricing keeps derivative books aligned with market conditions and forces collateral settlement.</div>

|   |   |
|---|---|
| **What it is** | Daily revaluation of derivative positions to [fair value](/fair-value/) and cash settlement of gains/losses |
| **Also called** | Daily settlement, variation margin, mark-to-market settlement |
| **Applied to** | [Futures](/futures-contract/), [options](/option/), swaps, [forwards](/forward-contract/), clearinghouse contracts |
| **Key mechanism** | Close of business: revalue; next day: transfer cash |
| **Who uses it** | [Futures](/futures-contract/) exchanges mandatory; OTC swaps increasingly under CSA agreements |
| **Collateral posted** | Variation margin (P&L settlement) + initial margin (loss buffer) |
| **Accounting** | Derivatives marked-to-market in P&L (unrealised gains/losses are earnings) |
| **Risk mitigation** | Prevents surprise defaults; forces early margin calls |

</aside>

## Why daily settlement matters

Imagine a [forward contract](/forward-contract/) to buy gold in six months at a price agreed today. For months, no cash changes hands—just a promise. If gold prices soar, you profit on paper but your counterparty is deeply underwater and may face bankruptcy before settlement date. If you wait until delivery, the loss crystallises and you discover they cannot pay.

Mark-to-market solves this by requiring the underwater party to post cash *now*. Each day, the contract is revalued at the market price. If prices moved against you, you pay variation margin to your counterparty (or clearinghouse) immediately; if prices moved in your favour, they pay you. This daily reckoning prevents one party from drifting into insolvency undetected.

The effect is dramatic. Instead of a six-month risk exposure, both parties face only a one-day exposure at any moment—they know today's price, settle today's profit or loss, and reset tomorrow. The risk of not getting paid shrinks to the overnight duration between settlement and the next revaluation.

## Futures: the gold standard

Exchange-traded [futures](/futures-contract/) use mark-to-market as their standard. When you buy one crude oil [futures](/futures-contract/) contract at USD 85 per barrel, and the close-of-day price is USD 85.50, you have a USD 500 gain (1,000 barrels × USD 0.50). The clearinghouse credits your account that evening.

If you hold the position and the next day the price drops to USD 85.20, you owe USD 300 (USD 0.30 × 1,000). Your account is debited. If your account balance falls below a threshold (the **maintenance margin**), you receive a **margin call** and must deposit cash or close your position.

This daily settlement has two effects. First, it forces loss recognition immediately—there is no hiding underwater positions. Second, it makes the clearinghouse's counterparty risk extremely small. Because every participant posts margin daily, the clearinghouse's largest exposure to any one defaulting member is at most one day's price move. If a member fails, the clearinghouse has collateral to cover the loss and can close positions quickly without cascading defaults.

## OTC swaps and CSAs

[Interest-rate swaps](/interest-rate/) and other OTC derivatives traditionally had no daily mark-to-market. The swap dealer and client would reset the contract annually or at maturity, with no interim settlement. The dealer faced years of counterparty risk; the client faced years of dealer risk. When markets moved large amounts, the underwater party could rack up hundreds of millions in losses before anyone settled.

The credit crisis of 2008 exposed this danger. When [Lehman Brothers](/goldman-sachs/) failed, it had massive unsettled swap positions—trillions in notional value—and counterparties faced uncertainty about payouts. After 2008, regulatory mandates and market practice shifted.

Today, most OTC derivatives are covered by **Credit Support Annexes (CSAs)**, which are collateral agreements appended to swap contracts. A CSA specifies that parties must post collateral daily to cover unrealised losses (variation margin). For a large USD [interest-rate swap](/interest-rate/) that moves USD 10 million in the client's favour, the dealer posts USD 10 million cash or bonds overnight.

The threshold above which collateral must be posted varies by counterparty strength. A major bank might have a USD 5 million threshold (no posting below that); a smaller counterparty might start at USD 1 million or zero. The better your credit, the less collateral you post.

## Accounting and P&L recognition

From an accounting standpoint, mark-to-market derivatives are re-valued every financial reporting period (quarterly or annually) and changes in [fair value](/fair-value/) hit the income statement as unrealised gains or losses. If you hold a [call option](/call-option/) worth USD 100,000 today and USD 120,000 tomorrow, you record a USD 20,000 gain immediately—even though you have not sold the option.

This is **accrual accounting** for derivatives. Under [GAAP](/generally-accepted-accounting-principles/) and [IFRS](/international-financial-reporting-standards/), derivative gains and losses are typically realised (in P&L) rather than deferred until settlement. For hedge accounting, some gains may be deferred and matched against the hedged item's losses, but the default is immediate recognition.

This creates a distinction: a dealer holding a swap book shows daily swings in profit, even though no cash has changed hands. Investors sometimes misunderstand this, seeing large unrealised losses and assuming the firm is in distress when in fact those losses are merely mark-to-market notional moves.

## Pricing: from last trade to model value

Mark-to-market sounds simple—revalue to "market price"—but for derivatives, there is often no single market price. [Futures](/futures-contract/) are liquid and have a clear closing price. But an exotic interest-rate swaption (an option on a swap) with a one-of-a-kind strike and tenor may not have traded in weeks.

For illiquid derivatives, traders use models to estimate [fair value](/fair-value/). A [Black–Scholes](/black-scholes-model/)-style model ingests the current spot price, volatility, interest rates, and time to expiration and outputs a theoretical [option](/option/) price. A dealer marks their book using this computed value.

The risk: if the model assumptions are wrong, the mark is too high or too low. If volatility is overstated, you are marking [call options](/call-option/) above what they would fetch in a real trade. When you try to exit, you learn the hard way. Regulators now require dealers to disclose **valuation reserves**—adjustments to model prices that reflect uncertainty, bid-ask spreads, and the illiquidity of their inventory.

## Initial margin and variation margin

Two types of collateral flow from mark-to-market. **Variation margin** is the daily P&L settlement—the winner receives cash from the loser each evening. **Initial margin** is a separate deposit posted upfront, a buffer to cover potential losses over the next N days if your counterparty defaults.

For a [futures](/futures-contract/) contract, the exchange sets both. Initial margin might be 10% of notional value; variation margin settles daily. For OTC swaps, initial margin is negotiated or set by regulatory formula (under [Dodd-Frank](/dodd-frank-act/) rules, non-cleared swaps now require initial margin too).

Initial margin is not a cost per se—you recover it when you close the position. But it ties up capital. A trader posting USD 1 million in initial margin loses the opportunity cost of deploying that cash elsewhere. This makes the upfront cost of a derivative position real, even before variation margin kicks in.

## When mark-to-market breaks down

During extreme market dislocations, mark-to-market can paradoxically create instability. If a derivative position is very large and moves sharply against you, a sudden margin call can force hasty selling elsewhere to raise cash. This forced selling can cascade, pushing other assets down and triggering more margin calls. The 1998 Long-Term Capital Management crisis and some aspects of the 2008 crisis involved such feedback loops.

Also, in illiquid derivatives, the "market" price used for mark-to-market can be speculative. If no one has traded a particular swaption in a month and a dealer marks it using a model that assumes lower volatility than realised, the mark understates risk. When realized volatility spikes, the unrealised loss becomes realized and the collateral buffer proves insufficient.

For this reason, dealers now often use a **bid side** valuation—marking illiquid positions at the more conservative (lower) price they could sell at, not the theoretical model price. This inflates reserves but better reflects true economic risk.

## Regulatory evolution post-2008

The Dodd-Frank Act and international accords (Basel III, EMIR, Dodd-Frank) mandated that standardised OTC derivatives be cleared through central counterparties with mark-to-market and margin rules. This forced OTC swaps—even bilaterals—into a more exchange-like ecosystem.

The upshot: derivatives markets today are far more transparent and collateralised than pre-2008. Most standardised [interest-rate swaps](/interest-rate/), [credit derivatives](/credit-risk/), and equity swaps now go through clearinghouses with daily settlement. Only the most exotic, illiquid derivatives remain fully bilateral and uncleared.

This increased collateral demand also inflated the cost of derivatives. Dealers pass margin costs to clients; clients bear initial and variation margin as ongoing operating expenses. The upside is reduced [systemic risk](/systemic-risk/) and more predictable counterparty exposures.

## See also

<div class="wiki-seealso">

### Closely related

- Derivative — the underlying contract type
- [Fair Value](/fair-value/) — the valuation target in mark-to-market
- [Futures Contract](/futures-contract/) — daily settlement is standard
- [Option](/option/) — often marked daily via models
- [Counterparty Risk](/counterparty-risk/) — mark-to-market mitigates it
- [Valuation](/fair-value/) — models and pricing logic

### Wider context

- [Interest Rate](/interest-rate/) — largest OTC derivatives market affected
- [Dodd-Frank Act](/dodd-frank-act/) — mandated clearing and margin
- [Credit Risk](/credit-risk/) — credit derivatives subject to mark-to-market
- [Liquidity Risk](/liquidity-risk/) — arises when mark-to-market values differ from tradeable prices
- [Leverage Ratio](/leverage-ratio-forex/) — initial and variation margin reduce leverage available

</div>
