---
title: "Box Spread"
description: "An advanced option strategy combining a bull call spread and bear call spread with overlapping strikes, designed to lock in a risk-free profit if entry and exit prices are favorable."
---

*A box spread pairs a [bull call spread](/wiki/bull-call-spread/) and [bear put spread](/wiki/bear-put-spread/) at the same strike boundaries. In theory, it's a risk-free arbitrage: you profit if the spread's cost is less than the intrinsic value of the box at expiration.*

## What a box spread is

A classic box spread buys a $90 call, sells a $100 call, sells a $90 put, and buys a $100 put—all same expiration. At expiration, one of two things happens:

- Stock below $90: you exercise the $90 put to buy stock, then sell it via the $100 call at a $10 loss. But you sold the $90 put and bought the $100 put, netting $10 credit. Perfect hedge.
- Stock above $100: you exercise the $100 call to sell stock, having bought it via the $90 call at a $10 loss. But you sold the $100 call and bought the $90 call, netting $10 credit. Perfect hedge.

In all cases, your payoff is exactly $10 (the width of the box) minus the net cost paid. If you paid less than $10, you profit.

## Why to use a box spread

The primary reason is **theoretical arbitrage**. In an efficient market, a box spread should cost exactly its intrinsic value (width of box). In practice, inefficiencies arise—supply/demand imbalances, liquidity premiums, volatility skew. A trader can exploit these by buying underpriced boxes and selling them later.

A second reason is **capital efficiency for traders comfortable with complexity**. A box spread replaces buying stock outright with a lower-cost synthetic position that replicates the same payoff.

Box spreads also suit **synthetic lending**. Instead of lending cash at the risk-free rate, you can buy a box, lock in the rate for a few months, and arbitrage the difference to the actual borrowing rate.

## When a box spread works

Box spreads work when **the market misprices the box relative to the risk-free rate**. If the box costs $8 and should cost $10, you lock in a $2 profit per spread.

They also work when **spreads are wide**. Market-making spreads (the gap between bid and ask) can hide arbitrage opportunities. A wide spread on each component might sum to a profitable box cost.

Box spreads excel for **traders with institutional-quality execution**. Professional traders with tight commissions and real-time market data can profitably deploy box spreads; retail traders face wider spreads and higher commissions that eliminate the edge.

## When a box spread loses money

If the transaction costs (commissions, spread costs on four legs) exceed the arbitrage opportunity, you lose money. A $2 theoretical profit can evaporate if commissions and slippage cost $3.

Box spreads also suffer from **execution risk**. By the time you've bought two spreads and positioned correctly, market prices may have moved. You're exposed to slippage on each leg.

Early exit is risky. If you're forced to close before expiration, liquidity might be terrible; you could face 20-cent spreads on options that should be worth 50 cents, erasing gains.

## Mechanics and adjustment

You pay a net debit to enter—the sum of the two spread costs. Maximum profit is `(box width) – (net debit)`. Maximum loss is the net debit paid (if you over-paid for the box).

Unlike most strategies, box spreads don't require active management. You hold to expiration, where the payoff is deterministic.

**Adjustment** is rare. You might close early if the profit opportunity evaporates or if you need capital for a better trade elsewhere.

## Box spread arbitrage reality

Box spreads are a textbook arbitrage only in institutional, liquid markets. Retail options markets have wide spreads and high commissions that usually consume any edge. Professional traders deploy them; retail traders rarely see a profitable edge after costs.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/bull-call-spread/">Bull Call Spread</a> — one half of a box spread.</li>
<li><a href="/wiki/bear-put-spread/">Bear Put Spread</a> — the other half of a box spread.</li>
<li><a href="/wiki/synthetic-long-stock/">Synthetic Long Stock</a> — economically similar payoff.</li>
<li>Arbitrage — the pricing principle underlying boxes.</li>
<li><a href="/wiki/strike-price/">Strike Price</a> — defines the box boundaries.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — contract type underlying box spreads.</li>
<li><a href="/wiki/expiration-date/">Expiration Date</a> — when the box payoff is deterministic.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — largely irrelevant for boxes (payoff is fixed).</li>
</ul>
</div>
