---
title: "Physically Settled Option"
description: "An option that results in the delivery of the actual underlying asset when exercised, rather than a cash payment."
keywords:
  - physical delivery
  - settlement
  - underlying asset
  - stock options
  - commodity options
image: "/svg/derivatives.svg"
---

*A **physically-settled option** is an [option](/option/) contract that delivers the underlying asset itself upon exercise—not cash. When an [option buyer](/option-buyer/) exercises a call, the [option writer](/option-writer/) transfers the shares, commodity, or currency agreed in the contract. When an option buyer exercises a put, the writer purchases the asset at the [strike price](/strike-price/). This is the standard settlement mechanism for equity options, commodity [futures](/futures-contract/), and currency options in most jurisdictions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Physically Settled Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and financial contracts." />

<div class="wiki-infobox-caption">Settlement by delivering the underlying asset; requires the writer to own or acquire the actual commodity or securities.</div>

|   |   |
|---|---|
| **What it is** | Option that transfers the underlying asset, not cash, upon exercise |
| **Also called** | American option (common form), physical delivery settlement |
| **Settlement** | Asset transfer; buyer acquires ownership; writer loses control |
| **Common on** | Equity options, commodity options, currency options |
| **Advantage** | Buyer gains actual ownership and control; flexibility for holders |
| **Disadvantage** | Complex logistics; writer must source/deliver the asset; delivery risk |

</aside>

## The fundamental difference: asset vs. cash

In a [physically-settled option](/physically-settled-option/), the outcome is not a cash payment but a **swap of ownership**. An [option buyer](/option-buyer/) who exercises a call on Apple stock receives 100 shares of Apple and must pay the [strike price](/strike-price/) in cash. An [option writer](/option-writer/) who receives an exercise notice must deliver those 100 shares and collect the strike price. The asset itself—not its value, but the asset—changes hands.

This is fundamentally different from [cash-settled options](/cash-settled-option/), where the writer pays the buyer the difference between the strike and the market price, and no securities ever move. With physical settlement, the [option buyer](/option-buyer/) can hold the underlying indefinitely, sell it, receive [dividends](/dividend/) (if a stock), or use it in other contracts. The buyer is now an owner, not just a profit-taker.

## Call buyer and call writer obligations

A [call buyer](/option-buyer/) who exercises a call option buys the underlying at the strike price and receives delivery. If the buyer bought a call on crude oil and exercises, the buyer must take possession (or arrange storage and financing) of the crude. If the buyer bought a call on euros and exercises, the buyer receives euros and must either convert them, use them, or hold them. The buyer cannot exercise casually; they must intend to take ownership or quickly resell.

The [call writer](/option-writer/) faces the opposite obligation. Upon exercise notice, the writer must **deliver** the underlying within a specified timeframe (typically 1–2 business days). If the writer does not own the shares or commodity, the writer must buy them in the market at whatever price they fetch—a catastrophic outcome if prices have moved sharply. A naked call writer who sold calls on shares they do not own is exposed to unlimited loss, because the cost of acquiring the shares can be arbitrarily high.

## Put buyer and put writer obligations

A [put buyer](/option-buyer/) who exercises a put option **sells** the underlying at the strike price. The buyer is happy to do this when the market price has fallen below the strike; the put locks in a higher price than selling outright would yield. Upon exercise, the put buyer must deliver the underlying to the put writer and collect the strike price in cash.

The [put writer](/option-writer/) who receives an exercise notice must **buy** the underlying from the put buyer at the strike price. If the market price has plummeted below the strike, the writer has acquired a now-underwater asset. Put writers often hold cash reserves or other positions to absorb this loss, or they use puts as a [hedging](/hedge-fund/) tool—accepting the obligation because it offsets losses elsewhere in their portfolio.

## American vs. European style

Most [physically-settled options](/physically-settled-option/) are American style, meaning the buyer can exercise anytime up to expiration. This flexibility is valuable because the buyer can lock in a transaction at a moment of their choosing. If a stock gaps up sharply overnight, a call buyer can exercise before the market opens and lock in the overnight gain. If a commodity crashes intraday, a put buyer can exercise and offload it at the pre-crash level.

European-style [physically-settled options](/physically-settled-option/) (less common) require the buyer to wait until expiration to exercise. They are often cheaper because the writer has less risk—they have time to prepare delivery or find the cheapest way to source the underlying.

## Delivery logistics and cost

For equity options, delivery is straightforward: the writer transfers shares via the clearinghouse, and the buyer receives them electronically. For commodities, delivery can be complex. If a buyer exercises a crude oil option, the buyer might receive warehouse receipts or a bill of lading granting ownership of physical barrels. Storage, insurance, and financing costs fall on the buyer. Some commodity options allow the buyer to choose among several types of delivery (light sweet crude vs. heavy crude, or spot vs. forward), giving the buyer a delivery option within the option itself.

Currency delivery is also clearer than commodities but still nontrivial; the buyer and writer must arrange for the transfer of foreign currency, often through a settlement bank. Delays or differences in exchange rates between dealing and settlement can create small losses, but they are minor compared to commodity delivery risk.

## The "in-the-money" decision

An option buyer holding a [physically-settled option](/physically-settled-option/) must decide whether to exercise if the option is [in-the-money](/in-the-money/) as expiration approaches. If the buyer does not want to take delivery, the buyer can sell the option itself in the secondary market instead, capturing the [intrinsic value](/intrinsic-value/) and some remaining [time value](/time-value/) as profit without ever owning the underlying. This is the most common path: the buyer sells the option contract, not the underlying.

Alternatively, the buyer might exercise to take ownership because they need the asset. A farmer who bought call options on seed might exercise to receive the seed at a locked-in price, plant it, and grow crops. A manufacturer who bought call options on nickel might exercise to receive the metal and use it in production. The option is not a financial side bet but a real procurement tool.

## Early exercise and dividends

Early exercise is most valuable just before an underlying stock's [ex-dividend date](/dividend/). If a call buyer is holding in-the-money calls, exercising before the ex-date allows the buyer to own the stock and receive the upcoming dividend. A writer might therefore face unexpected early exercise, forcing them to sell their shares and miss the dividend. This is a real risk that [covered call](/covered-call/) writers must monitor; it can turn a lucrative premium into a missed dividend.

## Margin and financing

A [call writer](/option-writer/) who does not own the underlying shares must maintain margin—a cash deposit or bond guarantee—with their broker to cover the potential cost of delivery. A writer who sold 10 calls on $100 stock might be required to hold $100,000 in margin. This capital is locked up and cannot be deployed elsewhere. For large portfolios, margin costs can be substantial.

Similarly, a put buyer who exercises receives the underlying and must pay the strike price, which might require borrowing if cash is not on hand. The buyer incurs [interest](/interest-rate/) costs on the borrowed amount until they sell the underlying or repay the loan.

## Settlement failures and squeezes

In rare cases, a [call writer](/option-writer/) fails to deliver on an exercise notice. The clearinghouse intervenes, but squeezes can occur in thin or manipulated markets. A trader who corners a stock and forces all short call sellers to cover at inflated prices is the nightmare scenario. Regulatory safeguards (short-sale restrictions, position limits) exist to prevent this, but physical settlement retains more settlement risk than cash settlement.

## See also

<div class="wiki-seealso">

### Closely related

- [Cash-Settled Option](/cash-settled-option/) — the alternative, settling via cash payment
- [Option](/option/) — the underlying contract type
- [Option Buyer](/option-buyer/) — the buyer who receives the underlying asset
- [Option Writer](/option-writer/) — the seller who delivers the asset
- [Covered Call](/covered-call/) — a writer strategy using physical settlement
- [Exercise Price](/strike-price/) — the price paid at settlement

### Wider context

- [American Option](/option/) — commonly physically settled, allowing early exercise
- [European Option](/option/) — can be physically or cash settled
- [Futures Contract](/futures-contract/) — another physical-delivery derivative
- [Forward Contract](/forward-contract/) — similar concept, settled at a future date
- [Dividend](/dividend/) — a key trigger for early exercise decisions
- [Margin Call](/margin-call-forex/) — used to secure writer obligations

</div>
