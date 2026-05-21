---
title: "Assignment (Options)"
description: "The process of obligating a short option seller to fulfill their contract when a long option holder exercises."
---

*Assignment is the moment when theory becomes reality: a holder of a [call option](/wiki/call-option/) or [put option](/wiki/put-option/) chooses to [exercise](/wiki/exercise/) and the [clearinghouse](/wiki/options-clearing-corporation/) mandates that a short seller fulfill the obligation. The short seller is assigned the duty to deliver shares (call) or buy shares (put) at the [strike price](/wiki/strike-price/), usually within two business days.*

## How assignment works operationally

When an option holder submits an exercise notice, the clearinghouse runs assignment nightly. For call options, it randomly selects a short call seller from the pool and assigns them the obligation. That seller's account is notified that they've been assigned: if they sold a $100 call and it was exercised, they must deliver 100 shares at the strike, receiving $10,000 (100 × $100) in return. For puts, the process is reversed—the short seller must buy shares at the strike.

## Automatic exercise to prevent loss

If an option is in-the-money at expiration and the holder forgets to exercise, most brokers automatically exercise it to protect the holder from a total loss. This is why many retail investors—and sometimes even professional firms—experience unexpected assignments on the final expiration day without having explicitly requested it. The threshold for automatic exercise varies by exchange, but it's typically $0.01 of intrinsic value.

## Assignment risk for covered calls

A [covered call](/wiki/covered-call/) writer who is assigned must hand over the shares at the strike price. If the call is in-the-money and [American-style](/wiki/american-option/), this can happen any time, not just at expiration. This is often surprising: a trader writing a call that expires in a month might be assigned two weeks early if the underlying pays a large [dividend](/wiki/dividend/). The assignment locks the position and ends the trade.

## Assignment on puts and capital requirements

Short put sellers face assignment if [in-the-money](/wiki/in-the-money/) at expiration. They must buy 100 shares at the strike. A seller of a $100 put assigned at $100 per share must have $10,000 (or be margin-approved to borrow it) to buy the shares. This is called being "assigned" because you end up owning the stock even though you didn't intend to buy it—you intended to earn a premium for selling the put. Many brokers require cash to cover potential put assignments.

## Timing of assignment: American vs. European

[American options](/wiki/american-option/) can be assigned any time before expiration, so assignment risk exists every day. [European options](/wiki/european-option/) can only be assigned at expiration, making the timeline predictable. This is why professional traders often prefer European index options—they know the exact date they could be assigned, unlike American equity options where early assignment lurks.

## Post-assignment settlement

After assignment, the trade is settled. The seller receives shares (call assignment) or pays for shares (put assignment). Dividends are not adjusted—if a call is assigned before an ex-dividend date, the assignee captures the dividend; the writer misses it. This is a reason call writers sometimes get assigned early on high-dividend stocks.

## Tax implications and tracking

An assignment results in a taxable event. You've sold or bought shares at the strike price, establishing a cost basis and realizing any gain or loss. The IRS treats it the same as if you'd sold shares in the open market. Brokers track cost basis and assignment details automatically, but it's worth understanding how this affects your annual tax calculation, especially if you're using [specific identification](/wiki/specific-identification-basis/) or [FIFO](/wiki/fifo-tax/) for basis.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/exercise/">Exercise</a> — the act triggering assignment.</li>
<li><a href="/wiki/call-option/">Call option</a> — assignment obligation when in-the-money.</li>
<li><a href="/wiki/put-option/">Put option</a> — assignment obligation when in-the-money.</li>
<li><a href="/wiki/american-option/">American option</a> — can be assigned any time.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/options-clearing-corporation/">Options Clearing Corporation</a> — the entity managing assignment.</li>
<li><a href="/wiki/covered-call/">Covered call</a> — a strategy risking assignment.</li>
<li><a href="/wiki/strike-price/">Strike price</a> — the settlement price in an assignment.</li>
</ul>
</div>
