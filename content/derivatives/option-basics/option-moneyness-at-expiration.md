---
title: "Option Moneyness at Expiration"
description: "What happens to an in-the-money option at expiration: automatic exercise, pin risk, cash settlement, and holder outcomes."
keywords:
  - option moneyness at expiration
  - in the money option expiration
  - automatic exercise options
  - pin risk
  - option settlement
image: /svg/derivatives.svg
---

*When an option reaches its expiration date, **what happens to an in the money option** at expiration is determined by automatic exercise rules, the [intrinsic value](/intrinsic-value/) at that moment, and whether settlement is cash or physical delivery—mechanics that can create hidden risk even after the option expires.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Moneyness at Expiration — settlement outcomes</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Automatic exercise is standard for in-the-money options, but pin risk and settlement delays can still surprise holders.</div>

|   |   |
|---|---|
| **In-the-money at expiry** | Automatically exercised for intrinsic value |
| **Out-of-the-money at expiry** | Expires worthless; no exercise |
| **At-the-money at expiry** | Expires worthless; no exercise (0 intrinsic value) |
| **Exercise deadline** | Typically 5:30 p.m. ET for US equity options, same day |
| **Settlement delay** | T+2 (2 business days) after exercise or expiration |
| **Cash settlement** | Index/cash options; received in brokerage account |
| **Physical settlement** | Equity options; shares bought or sold at strike price |
| **Pin risk** | Stock drifts near strike as expiration approaches; difficult to manage |

</aside>

## The moneyness threshold at expiration

An option's [moneyness](/in-the-money/) is a simple concept: a call is [in the money](/in-the-money/) if the stock price is above the strike; a put is in the money if the stock price is below the strike. [Time value](/time-value/) disappears at expiration, leaving only [intrinsic value](/intrinsic-value/)—the amount by which the option is in the money.

On expiration day, the decision to exercise is automatic. The option exchanges and your broker have rules designed to protect you: if your option is in the money by even a penny at the close of trading, it is automatically exercised. If it is out of the money, it expires worthless and you lose your premium. This automation prevents you from accidentally losing an option's remaining value because you forgot to act.

## Automatic exercise mechanics

For US equity options, the expiration deadline is typically 5:30 p.m. ET on the third Friday of the expiration month (or a business day nearby if Friday is a holiday). Your broker must notify the exchange of your election to exercise (or not) by that deadline. If you do nothing and the option is in the money, most brokers automatically exercise on your behalf.

The catch: automatic exercise happens after the market close, based on the official closing price. If you wanted to manage your position manually—perhaps selling the option in the final minutes to capture remaining premium—the window closes at 4 p.m. ET when the stock market closes. Any trade after that is too late.

## Intrinsic value and settlement

The moment an in-the-money call is exercised, the holder receives 100 shares per contract at the strike price. A put holder receives the difference between the strike and the stock price in cash, multiplied by 100. Index options and cash-settled products work differently—they deliver cash equal to the index level times the contract multiplier, without buying or selling the underlying.

Settlement does not happen immediately. Equity option exercise follows T+2 settlement—you own the shares two business days after expiration. If expiration falls on Friday, settlement is Tuesday. This delay matters: if you exercised a call expecting to hold the stock, you own it for two days without having made the purchase decision yourself. If you exercised a put expecting cash, the cash arrives two days later, not instantly.

## Pin risk: the hidden danger

**Pin risk** is the most commonly overlooked hazard at expiration. It occurs when a stock closes very near (pinned to) the strike price. A call holder expecting to own shares at $50 might find the stock closes at $50.05—technically in the money, so it is automatically exercised. But if the holder then cannot sell those shares immediately (or only at a loss), holding over the weekend creates unwanted exposure. Similarly, a put holder might be surprised to receive 100 shares via automatic exercise if the stock ticks below the strike by 1 cent at closing.

Pin risk is highest for far-out-of-the-money options that unexpectedly come near the money, and for thinly traded stocks where the closing price is volatile. Large traders often avoid holding short positions (sold puts or calls) very close to strike prices at expiration precisely to avoid this risk.

## The decision to exercise or let expire

Ordinarily, letting an option expire worthless is passive—it simply happens. But an option holder can choose to let an in-the-money option expire by instructing the broker to not exercise. Why would you do this? Perhaps the bid-ask spread is wide and exercise would incur poor pricing; perhaps you do not want to own the stock or pay the settlement. However, giving up exercise of an in-the-money option is almost always a mistake—you are throwing away intrinsic value.

Similarly, a call holder deep in the money before expiration might choose to sell the option in the market rather than hold for exercise, to avoid the T+2 settlement delay or to lock in a price. But once expiration passes, your choice is gone.

## Cash vs. physical settlement

Equity options settle via physical delivery of stock. You exercise a call, you get 100 shares; you exercise a put, the shares leave your account. Index options (e.g., the S&P 500 index) are cash-settled—there is no underlying stock to buy or sell, so you receive or pay cash equal to the intrinsic value times the multiplier (typically $100). Currency and commodity options vary; some settle physical, others cash.

Cash settlement eliminates pin risk and the complications of sudden stock ownership, but it means you cannot actually own the asset if you were banking on taking delivery. This is why index options are popular for portfolio [hedging](/derivatives-hedging/)—pure leverage and downside protection without stock logistics.

## Early assignment and the holder's perspective

Option holders cannot be assigned early; they can only exercise (call holders) or be exercised against (if they sold the option and are assigned). Only holders of sold options face assignment risk. A put seller, for example, can be assigned at any time, forcing them to buy 100 shares at the strike price. This risk is highest just before [ex-dividend](/dividend/) dates, when the call seller (or deep in-the-money call buyer) has an incentive to capture the dividend by exercising early.

## Tax implications and record-keeping

Exercise creates a clear buy or sell event. If you bought a call and exercised it, you are deemed to have bought the stock at the strike price on the exercise date, setting your cost basis. This is important for [cost basis](/cost-basis/) tracking and later [capital gains](/capital-gains-tax-investor/) calculation. [Schedule D](/schedule-d/) reporting requires accurate exercise dates and strike prices.

## Practical planning for expiration day

Do not assume your broker will handle everything correctly. Log in on expiration day, confirm whether your options are in or out of the money, and make an explicit decision: exercise (if in the money), sell (to capture any remaining premium), or let it expire. Do not rely on automatic exercise to manage your portfolio. If an option is slightly out of the money and could flip in the final minutes, monitor the stock price closely—or simply close the position beforehand to avoid guesswork.

## See also

<div class="wiki-seealso">

### Closely related

- [In the Money](/in-the-money/) — definition and implications at any point in an option's life
- [Intrinsic Value](/intrinsic-value/) — the cash value of an option if exercised immediately
- [Time Value](/time-value/) — how much premium remains beyond intrinsic value, eroding to zero at expiry
- [Option Expiration Date](/expiration-date/) — when options cease to exist and settlement occurs
- [Call Option](/call-option/) — the right to buy; exercise mechanics for call holders
- [Put Option](/put-option/) — the right to sell; exercise mechanics for put holders
- [Cost Basis](/cost-basis/) — tax treatment of exercised options and resulting stock purchases

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — why hedgers use options and how exercise affects the position
- [Options](/option/) — overview of contracts, strike prices, and settlement rules
- [Stock Market](/stock-market/) — the underlying equity market where most option exercise results in stock transactions
- [Schedule D](/schedule-d/) — tax reporting of option exercises and capital gains

</div>
