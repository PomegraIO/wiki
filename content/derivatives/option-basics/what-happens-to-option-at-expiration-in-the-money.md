---
title: "What Happens to an In-the-Money Option at Expiration"
description: "When an in-the-money option reaches expiration, automatic exercise, cash or stock settlement, and margin impact depend on contract rules and broker handling."
keywords:
  - in the money option expiration
  - option automatic exercise at expiration
  - option settlement at expiration
  - what happens option expires in the money
  - cash settlement vs physical delivery
  - option exercise mechanics
image: "/svg/derivatives.svg"
---

*When an [option](/option/) reaches its [expiration date](/expiration-date/) and ends in-the-money, it does not simply vanish; instead, it is automatically exercised under exchange rules, triggering either a cash or physical settlement that affects the buyer's and seller's accounts and margin requirements.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">In-the-Money Option at Expiration — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Expiration brings automatic settlement, converting the option's intrinsic value into cash or shares.</div>

|   |   |
|---|---|
| **Default outcome** | Automatic exercise if in-the-money by one cent or more (per exchange rules) |
| **Buyer action** | Can surrender the [option](/option/) to avoid exercise (rare, usually expensive) |
| **Settlement type** | Cash (index [options](/option/)) or [physical delivery](/option/) (stock [options](/option/)) |
| **Settlement date** | Same day or T+1 depending on exchange and contract type |
| **Buyer cash impact** | Receives intrinsic value if call, pays intrinsic value if [put](/put-option/) |
| **Seller/Writer obligation** | Must deliver cash or stock; margin tied up until settlement clears |
| **Commission costs** | Broker fees for exercise and settlement apply automatically |

</aside>

## Automatic exercise and how it works

When a call [option](/option/) closes in-the-money—meaning the stock price is above the [strike price](/strike-price/)—the exchange and clearing house do not wait for the buyer to decide. U.S. options exchanges (NYSE Arca, CBOE, NASDAQ-OMX) enforce a rule: **any [option](/option/) closing at [expiration date](/expiration-date/) with [intrinsic value](/intrinsic-value/) of $0.01 or more is automatically exercised**. The buyer takes the position; the seller is assigned the obligation.

This rule exists because the [option](/option/) has real, liquidatable economic value. A call [option](/option/) on a stock trading at $52 with a $50 [strike price](/strike-price/) is worth at least $2 of [intrinsic value](/intrinsic-value/). If the exchange allowed it to expire worthless, the buyer would suffer a real loss; the seller would pocket unearned profit. Automatic exercise prevents that injustice and ensures the [option](/option/) settles at economic reality.

A few edge cases exist. The buyer can voluntarily **surrender the [option](/option/)** before expiration to avoid automatic exercise and the associated [commission costs](/expense-ratio/). But this is rare and expensive if the [option](/option/) is far in-the-money; you would be forfeiting real value to avoid a small fee. Some brokers offer "do-not-exercise" instructions, allowing the buyer to explicitly reject automatic exercise, but most institutions discourage this because it creates operational risk and tax complexity.

## Equity options: physical delivery

When an equity [call option](/option/) on 100 shares of stock ends in-the-money, automatic exercise triggers **assignment**. The buyer is long 100 shares at the [strike price](/strike-price/); the seller is short 100 shares at the same [strike price](/strike-price/).

**For the buyer:** Cash leaves the account immediately to pay for the shares. If the call had a $50 [strike price](/strike-price/) and 100 shares are purchased, $5,000 flows out. The buyer now owns the stock, with a [cost basis](/cost-basis/) of $50 per share (plus [commission](/expense-ratio/) fees). If the stock is trading at $52, the buyer has a $200 unrealized gain on the shares, but has also paid the exercise [commission](/expense-ratio/), which offsets some of that gain.

**For the seller (writer):** The seller is obligated to deliver 100 shares. If the seller already owns the shares (a covered call), they are sold; the cash is credited to the seller's account. If the seller does not own the shares (a naked call), the seller is short 100 shares and must borrow them. This triggers a short-sale obligation, [margin](/margin-call-forex/) is tied up, and the seller incurs borrowing costs until the short is covered.

A **put option** works in reverse. If a put call is in-the-money at expiration, the buyer has the right to sell; the seller has the obligation to buy. If the put buyer exercises (automatically), the buyer delivers 100 shares and receives the [strike price](/strike-price/) in cash. The seller receives the shares and pays the [strike price](/strike-price/).

Settlement is typically same-day (in the U.S., via the Options Clearing Corporation), though some brokers settle T+1. The buyer's account is debited for the share purchase (or credited for a put sale); the seller's account is credited/debited for the corresponding sale/purchase.

## Index options: cash settlement

[Index options](/option/) on the [S&P 500](/sp-500-index/), [VIX](/volatility-smile/), or currency indices do not settle by delivering the underlying index—you cannot buy a basket of 500 stocks in one transaction. Instead, **index [options](/option/) settle in cash**.

When an index call option is in-the-money at expiration, the buyer receives cash equal to (spot index level – [strike price](/strike-price/)) × multiplier. Most U.S. index [options](/option/) have a $100 multiplier, so a $10 difference is $1,000 in cash. The seller pays that cash.

Settlement is typically same-day or next business day, and no margin remains tied up after settlement. The position is flat; both buyer and seller have converted the [option](/option/) into its cash value.

## Margin and collateral impact

For the **option buyer**, automatic exercise has little margin consequence. You already paid the [option premium](/option-premium/) upfront to buy the [option](/option/). Upon exercise, the account is debited for the stock purchase (or credited for a put sale) and the [option](/option/) is closed. If you are on [margin](/margin-call-forex/), the new stock position now counts against your buying power and margin maintenance requirements.

For the **option seller (writer)**, the impact is more pronounced. If you sold a call and the stock rallies past the [strike price](/strike-price/), assignment means you are now short the stock (if unhedged). If you sold a put and the stock falls, you are assigned shares and must pay for them out of cash or margin. In both cases, margin requirements jump. A broker will freeze some or all of your available margin to ensure you can meet the settlement obligation.

Example: You sell 10 calls on XYZ stock, [strike price](/strike-price/) $50, with 10 cents of premium each ($1,000 total credit). XYZ rallies to $53 and your calls are assigned at expiration. You are short 1,000 shares at $50 per share, requiring $50,000 in margin to maintain (or more if the broker's requirement is 40% instead of 50%). Your margin account swings from cash-rich (you pocketed the $1,000 premium) to margin-constrained (you owe $50,000 in settlement). If you do not have enough buying power, your broker may force a buy-to-close on some of the call contracts before expiration to prevent this outcome.

## Cash vs. intrinsic value: what the buyer receives

When a call [option](/option/) expires in-the-money, the buyer receives the **[intrinsic value](/intrinsic-value/)**, not the current market value of the stock.

Example: A $50 call on a stock trading at $60 is $10 in-the-money. At expiration, the buyer receives 100 shares with a [cost basis](/cost-basis/) of $50 (the [strike price](/strike-price/)), for a total cash outlay of $5,000 (plus fees). The stock is immediately worth $6,000 at market; the buyer has $1,000 of unrealized gain (ignoring [commission](/expense-ratio/) costs). But the buyer does not "receive $6,000 in cash." The buyer owns stock; the cash payment is the [strike price](/strike-price/) times shares, always.

This matters for tax purposes. The [cost basis](/cost-basis/) of the shares acquired is the [strike price](/strike-price/) plus any [commission](/expense-ratio/) paid. If the buyer later sells the shares at $62, the capital gain is $12 per share ($62 – $50), not $2 per share ($62 – $60).

## Expiration day scenarios and timing

**Regular market hours expiration (3 p.m. ET, U.S. equities):** Most equity [options](/option/) expire at 4 p.m. ET on the third Friday of the month (or the business day before if Friday is a holiday). If the stock is trading in-the-money at 4 p.m., it is automatically exercised. The buyer is assigned by 5 p.m.; settlement (money or shares transfer) occurs the next business day.

**After-hours moves:** If a stock rallies or falls after the 4 p.m. market close, the [option](/option/) is evaluated at the 4 p.m. close price only, not the after-hours price. An [option](/option/) out-of-the-money at 4 p.m. expires worthless, even if the stock soars in after-hours trading. Conversely, an [option](/option/) in-the-money at 4 p.m. is exercised, even if the stock crashes after-hours before settlement.

**Broker notification:** Most brokers notify account holders of in-the-money [options](/option/) one day before expiration. This is a courtesy, not a guarantee. Some brokers will automatically exercise; others allow a surrender window (e.g., before 5:30 p.m. on the day before expiration) for the buyer to cancel exercise if desired. Always verify your broker's rules.

## Common pitfalls

**Forgetting settlement costs.** Exercise is not free. Most brokers charge $0.50–$1.00 per [contract](/expiration-contracts/) (100 shares) to execute exercise, plus any standard stock trading [commission](/expense-ratio/). For a buyer who wanted to own the stock anyway, the [commission](/expense-ratio/) is the cost of being assigned instead of buying shares on the open market. If you were just playing for the [option](/option/) gain, the [commission](/expense-ratio/) erodes your profit.

**Unintended short positions.** Sellers who are assigned on naked (uncovered) calls or puts may not realize they are now short and liable for borrowing costs and [margin](/margin-call-forex/) pressure. Covered call sellers (short calls, long stock) have no surprise, but naked-put sellers who suddenly hold 100 shares they did not budget for may face forced liquidation.

**Tax complications from assignment.** If a call is assigned, the shares acquired have a [cost basis](/cost-basis/) of the [strike price](/strike-price/), with [holding period](/holding-period/) that resets if you later sell. A [put option](/put-option/) assignment can create a [wash-sale](/wash-sale/) violation if you are trying to harvest a loss on a related stock position. Document the exercise and resulting [cost basis](/cost-basis/) carefully.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the parent concept, including how expiration times are set
- [In-the-Money](/in-the-money/) — the condition that triggers automatic exercise
- [Strike Price](/strike-price/) — the price at which exercise occurs
- [Expiration Date](/expiration-date/) — the date on which exercise and settlement occur
- [Intrinsic Value](/intrinsic-value/) — the cash value the buyer receives
- [Option Premium](/option-premium/) — the cost of the [option](/option/) paid upfront
- [Call Option](/option/) — for equity purchase; settlement by stock delivery
- [Put Option](/put-option/) — for equity sale; settlement by stock delivery
- [Cost Basis](/cost-basis/) — the acquisition price of shares, critical for tax reporting after exercise
- [Margin Call](/margin-call-forex/) — the risk sellers face when margin requirements jump post-exercise

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — the broader category of [option](/option/) strategies
- Settlement — the mechanics of transferring cash and securities
- [Exercise Price](/exercise-price/) — synonym for [strike price](/strike-price/)
- [Holding Period](/holding-period/) — matters for [long-term capital gains tax](/long-term-capital-gain-tax/) treatment of assigned shares
- [Wash Sale](/wash-sale/) — a tax rule that can be triggered by assignment and repurchase
- [Volatility](/historical-volatility/) — affects [option](/option/) value and assignment risk

</div>