---
title: "Exercise (Options)"
description: "The act of invoking the right embedded in an option contract to buy (call) or sell (put) the underlying asset at the strike price."
---

*To exercise an option is to use the right it grants—a call holder exercises to buy the underlying at the [strike price](/wiki/strike-price/), and a put holder exercises to sell at the strike price. Exercise converts the option into a cash or physical settlement, locking in the economic outcome and ending the contract.*

## How exercise works in practice

When a holder decides to exercise, they notify their broker, who sends an exercise notice to the option's clearinghouse ([OCC](/wiki/options-clearing-corporation/) in the U.S.). The clearinghouse randomly assigns the exercise obligation to a short seller of that contract. That seller then either delivers shares (for a short call) or receives shares (for a short put) at the strike price, usually within two business days. The exercise is final—there is no cancellation.

## In-the-money vs. out-of-the-money

A rational holder only exercises when it makes economic sense. An [in-the-money](/wiki/in-the-money/) call—where the stock trades above the strike—is worth exercising because you buy stock below market. An [out-of-the-money](/wiki/out-of-the-money/) call—where stock trades below the strike—would be foolish to exercise; you'd buy high. Still, holders of worthless out-of-the-money options sometimes exercise anyway, either by mistake or because the transaction cost is negligible and they want to settle the position. The clearinghouse will not force exercise; it only happens when the holder requests it.

## Automatic exercise of expiring options

On the [expiration date](/wiki/expiration-date/), the clearinghouse automatically exercises any option that closed [in-the-money](/wiki/in-the-money/) by at least $0.01. This protects negligent holders who forget to manually exercise a profitable contract. The threshold varies by contract type and exchange rules, but the point is the same: expiring money should not evaporate due to procedural mishap.

## Assignment and the short side

When a holder exercises, a short seller is assigned the obligation and must settle. A writer of a covered call that gets exercised hands over shares in exchange for the strike price. A seller of a cash-secured put that gets exercised must buy the shares at the strike. Neither party can refuse; assignment is mandatory and final. This is why careful position monitoring and hedge planning matter for short options.

## Early exercise risk for Americans

[American options](/wiki/american-option/) can be exercised any time before expiration, not just on the final day. This early-exercise risk is a headache for short sellers. A deep-in-the-money call on a dividend-paying stock might be exercised weeks early so the holder captures the dividend. The writer must be prepared to deliver shares, sometimes earlier than expected. [European options](/wiki/european-option/) eliminate this uncertainty by fixing the exercise date to expiration.

## Settlement after exercise

In equity options, exercise typically results in physical delivery of shares: a call holder receives 100 shares per contract (the standard multiplier) at the strike price; a put holder delivers 100 shares and receives strike price × 100 in cash. Some contracts, like index options, are cash-settled instead—no shares change hands, only the difference between the index level and strike is paid in cash.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/early-exercise/">Early exercise</a> — exercising an option before expiration.</li>
<li><a href="/wiki/strike-price/">Strike price</a> — the fixed price at which exercise occurs.</li>
<li><a href="/wiki/expiration-date/">Expiration date</a> — the date by which or on which exercise must occur.</li>
<li><a href="/wiki/in-the-money/">In-the-money</a> — when exercise would be economically favorable.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/call-option/">Call option</a> — the right to buy via exercise.</li>
<li><a href="/wiki/put-option/">Put option</a> — the right to sell via exercise.</li>
<li><a href="/wiki/options-clearing-corporation/">Options Clearing Corporation</a> — the clearinghouse handling exercise and assignment.</li>
</ul>
</div>
