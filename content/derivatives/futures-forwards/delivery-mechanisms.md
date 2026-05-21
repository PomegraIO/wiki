---
title: "Delivery Mechanisms"
description: "How futures and forward contracts handle the actual transfer of the underlying asset at expiration—cash settlement, physical delivery, or hybrid approaches."
---

*Most derivatives contracts are never exercised into physical delivery. Instead, traders close positions before expiration or settle in cash. But when a contract does reach its maturity, the mechanism determining who delivers what, where, and how becomes the law of the market.*

## The two paths: cash or physical

[Futures contracts](/wiki/futures-contract/) and [forwards](/wiki/forward-contract/) converge to the same underlying value at expiration, but their paths diverge sharply in execution. A cash-settled contract (like most stock index or currency futures) pays the difference in dollars. A physically deliverable contract (like wheat, crude oil, or copper) transfers actual barrels, bushels, or metric tons.

Each path exists for a reason. Cash settlement is cheaper to process and cleaner for [mark-to-market](/wiki/mark-to-market/) accounting. Physical delivery enforces price discipline—a futures contract that cannot be delivered into physical reality becomes a pure betting contract, not a true price-discovery mechanism. Wheat farmers need to know the contract represents real grain they can actually take possession of at harvest.

## Physical delivery: the settlement engine

When a futures contract specifies physical delivery, the exchange publishes a detailed **specification sheet** defining precisely what can be delivered:

- **Grade and quality standards.** Wheat must be a certain protein content and test weight. Crude oil must meet specific gravity and sulfur thresholds. Gold must be refined to 99.5% purity. The contract often permits "deliverable grades"—a range of products that satisfy the base specification, sometimes with an adjustment factor applied to price.
- **Location.** A corn futures contract specifies which approved warehouses or elevators are acceptable. The buyer cannot demand delivery to their back door; they accept it where the exchange says it will appear.
- **Timing.** The delivery month is often a window spanning several weeks, not a single day. The seller chooses *when* within that window to deliver, forcing the short side to stand ready.
- **Form of transfer.** Warehouse receipts, bills of lading, or certificates of ownership change hands, sometimes without the physical commodity moving. Modern crude oil settlements often occur via electronic book transfers at a central storage hub rather than truck movements.

The burden of managing logistics falls on the counterparties, not the exchange. This is a feature: it makes the contract live—the futures price reflects real supply, real demand, and the real cost of storing and transporting the asset until the contract matures.

## Cash settlement: pure financial clearing

A cash-settled contract, by contrast, fixes a cash amount payable at expiration. The [S&P 500 E-mini futures](/wiki/sp-500-index/) settles to the closing index value multiplied by the contract multiplier. The [interest-rate swap](/wiki/interest-rate-swap/) settles via floating-leg coupons. No warehouse receipt changes hands.

Cash settlement is economically equivalent to instant closure at fair value. It also:
- **Reduces operational risk.** No warehouse disputes, no shipping delays, no inspections of barrels or grain.
- **Scales to intangible underlyings.** You cannot deliver the S&P 500 or the Japanese yen forward curve; cash is the only honest mechanism.
- **Lowers basis risk for hedgers.** A farmer hedging next season's crop with physically deliverable wheat futures faces the risk that the delivered grade won't match their actual harvest. Cash settlement eliminates that friction.

But it also divorces the contract from reality. A cash-settled contract has no obligation to defend price discovery; once settlement is announced, traders have no skin in the game. This is why central banks sometimes mandate or encourage physical delivery for government bond futures—to keep traders grounded in the mechanics of actually funding debt.

## Convergence and arbitrage

Whether a contract settles cash or physically, its price must converge to the spot price (or a known basis) at expiration. If the September wheat futures close at $7.50 and the delivery grade wheat trades at $7.20 in Kansas City, an arbitrageur can buy physical wheat, store it until September, and deliver it at a $0.30 profit. This arbitrage keeps the futures price honest.

Cash settlement breaks this link. The S&P 500 futures can drift away from the spot index price before settlement, but once the settlement price is announced (using the opening print, the close, or a special auction), all positions close at that price. Traders who bet on divergence lose; the market has determined the final value with finality.

## The choice matters

For clearing houses and regulators, deciding whether a contract should settle physically or in cash is a major structural choice:

- **Physical is preferred when:** the underlying is storable, fungible, and actively traded in spot markets (commodities). It keeps price discovery tethered to production and consumption.
- **Cash is required when:** the underlying is an index, a rate, or an intangible. No one can deliver the unemployment rate or a basket of stocks.
- **Hybrid is common in:** energy and metals, where exchanges permit either party to settle physically *or* cash at index parity, giving flexibility without abandoning price discipline.

A contract that pretends to be physical but rarely gets delivered (because delivery is inconvenient or grades are hard to verify) becomes a broken mechanism. Traders face incentives to manipulate the final settlement because physical discipline is already gone. This is why energetic debate in commodity futures markets often centers on specifications—a tighter definition of what can be delivered makes the contract more honest.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/futures-contract/">Futures contract</a> — standardized derivatives traded on exchanges with [mark-to-market](/wiki/mark-to-market/) and daily settlement.</li>
<li><a href="/wiki/forward-contract/">Forward contract</a> — customized, over-the-counter agreement settled once at maturity, often with physical delivery.</li>
<li><a href="/wiki/cash-settlement/">Cash settlement</a> — resolving a contract by paying the difference in value rather than transferring the asset.</li>
<li><a href="/wiki/basis/">Basis</a> — the difference between spot and futures prices, especially important when [hedging](/wiki/hedging-with-futures/) with physical deliverable contracts.</li>
<li><a href="/wiki/mark-to-market/">Mark-to-market</a> — daily revaluation of futures positions with cash settlement of gains and losses.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/derivatives/">Derivatives</a> — overview of the broader asset class.</li>
</ul>
</div>
