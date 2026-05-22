---
title: "In-The-Money Settlement"
description: "Automatic or manual settlement of profitable options at expiration, by cash payment or stock delivery."
keywords:
  - option settlement
  - in-the-money
  - expiration
  - cash settlement
  - stock delivery
---

*An **in-the-money settlement** occurs when an [option](/wiki/option/) that is profitable at expiration is exercised and settled. A call option that is in-the-money (stock price above the [strike](/wiki/strike-price/)) at expiration can be settled either by cash payment of the intrinsic value, or by physical delivery of the underlying stock. A put that is in-the-money settles by delivering the stock and receiving cash.*

<div class="wiki-hatnote">
For out-of-the-money options that expire worthless, see <a href="/wiki/out-of-the-money-expiration/">/wiki/out-of-the-money-expiration/</a>. For the general definition of in-the-money, see <a href="/wiki/in-the-money/">/wiki/in-the-money/</a>.
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Call Expiration** | Calls ITM: holder pays strike price, receives stock or cash equivalent |
| **Put Expiration** | Puts ITM: holder delivers stock, receives strike price |
| **Settlement Method** | Varies by exchange and option contract specifications |
| **Cash Settlement** | Intrinsic value paid; holder does not take delivery |
| **Physical Settlement** | Stock or commodity physically transferred; cash adjusted for fractional shares |
| **Expiration Mechanics** | Automatic exercise by OCC; manual exercise request available |
| **Notification Deadline** | Exercise instructions must be given by specified cutoff (typically 5:30 p.m. ET) |
| **Tax Implication** | Holding period and exercise timing affect short-term vs. long-term gains |

</aside>

## The mechanics of automatic exercise

When an option expires, the clearinghouse (Options Clearing Corporation, or OCC, in the U.S.) determines which options are [in-the-money](/wiki/in-the-money/) and initiates settlement automatically. For equity options, the determination is made at the official [closing print](/wiki/closing-print/). An Apple call option with a $150 strike expires at 4 p.m. ET; if Apple closes at $155, the option is $5 in-the-money and the OCC marks it for automatic exercise.

Automatic exercise is a default rule designed to protect option holders from losing money. A holder of an in-the-money call who forgets to exercise would otherwise lose the intrinsic value; the OCC's automatic exercise prevents this disaster. The holder can renounce the exercise by specifying non-exercise instructions to their broker before the cutoff time (typically 5:30 p.m. ET on expiration day, though this varies by broker and contract).

For a stock option on a $155 close with a $150 strike, the holder's gain is $5 per share, or $500 per standard equity option contract (which covers 100 shares). This $500 is due to the option seller, paid through the clearinghouse and the seller's broker.

## Cash versus physical settlement

The default settlement method for equity options is **cash settlement**. The OCC computes the intrinsic value (stock price minus strike for calls; strike price minus stock price for puts) and transfers cash equal to that amount. For the Apple $150 call closing at $155, the holder receives $500 cash and does not take delivery of Apple shares. This is administratively simple and liquidity-efficient, especially for options on stocks with significant position sizes.

**Physical settlement** is used for some option contracts, particularly index options and commodity futures options. For a call on a futures contract, exercise results in assignment of the futures contract. The option holder becomes the owner of a long position in the underlying futures contract, and the option seller becomes the owner of a short position.

Equity options are overwhelmingly cash-settled in modern markets, but some options, particularly older or less liquid contracts, may still specify physical delivery of shares. For these, a holder of an in-the-money call is assigned 100 shares per contract; the holder's cash account is debited by the strike price times 100, and the shares are credited to the holder's stock account. The process is administrative but creates complications for brokers managing fractional share amounts.

## Timing and cutoffs

The option expiration date is standardized: equity options expire on the third Friday of the month at 11:59 p.m. ET (though for trading purposes, they become "expired" after the close on that day). The exercise cutoff is earlier: typically, a holder must notify their broker of intention to exercise by 5:30 p.m. ET on the expiration date.

For index options and other exotic instruments, expiration times and settlement prices vary. An SPX (S&P 500 Index) option might settle to the opening price on the Monday after expiration, or to a specially calculated settlement value. Investors must verify the contract specifications of any option before expiration.

The rationale for early cutoff is operational: brokers and the clearinghouse need time to process exercise instructions and settle positions before the end of the business day. An investor who realizes at 7 p.m. ET on expiration day that they own in-the-money calls may be unable to exercise them, depending on their broker's policies.

## Tax consequences of settlement

[In-the-money settlement](/wiki/in-the-money-settlement/) has tax implications tied to the exercise date and the holding period of the underlying stock. For a call option exercised (or automatically exercised) on expiration, the holder's cost basis in the acquired shares is the strike price, and the holding period for [long-term capital gains](/wiki/long-term-capital-gain-tax/) purposes begins on the exercise date.

If a holder purchased a $150 call on Apple and exercised it (via automatic settlement) on expiration, their cost basis is $150 per share. If they sell those shares the next day, the gain is short-term capital gain, taxed at ordinary income rates. If they hold for more than one year, the gain qualifies for long-term treatment, taxed at preferential rates (0%, 15%, or 20% depending on income level).

For a put option exercised at in-the-money expiration, the holder receives the strike price in cash and surrenders the stock. The holding period of the stock is relevant for [long-term capital gains](/wiki/long-term-capital-gain-tax/): if the holder had owned the stock for more than a year before exercising the put, the loss is long-term. If they had hedged the stock with a put that expires in-the-money, the loss is treated as arising from the stock, not the put.

## Manipulation and the settlement price

Because large in-the-money settlements can transfer substantial cash, the settlement price (the closing print) is occasionally subject to manipulation. A trader with a large position of out-of-the-money calls might attempt to push the stock price above the strike by market close, triggering automatic exercise and a transfer from the option seller to the option holder.

The SEC and regulatory agencies have brought enforcement actions for "closing print manipulation" tied to option expiration. A 2010 case involved traders manipulating the closing print to benefit their options positions. These abuses are increasingly detected through surveillance algorithms that flag unusual trading activity near the close on option expiration dates.

## American versus European options

American-style options (which include most U.S. equity options) allow exercise at any time through expiration. An American call can be exercised early if the holder chooses, or left alone to settle at expiration. European-style options (common on indices and some commodities) allow exercise only at expiration. For European options, there is no choice: the option settles on expiration day based on the [closing print](/wiki/closing-print/).

Many option holders avoid early exercise of in-the-money calls, because early exercise forfeits the remaining time value of the option. It is usually better to sell the in-the-money call in the market (capturing remaining time value) than to exercise it early. This is a well-known principle in option pricing: the early exercise feature is valuable for the option holder primarily in the case of call options on dividend-paying stocks, where early exercise can capture a dividend that would otherwise be forgone.

<div class="wiki-seealso">

### Closely related
- <a href="/wiki/in-the-money/">/wiki/in-the-money/</a> — Options with intrinsic value
- <a href="/wiki/option-expiration/">/wiki/option-expiration/</a> — The mechanics of expiration
- <a href="/wiki/out-of-the-money-expiration/">/wiki/out-of-the-money-expiration/</a> — Options that expire worthless
- <a href="/wiki/cash-settlement-equity/">/wiki/cash-settlement-equity/</a> — Settlement methods for derivatives

### Wider context
- <a href="/wiki/strike-price/">/wiki/strike-price/</a> — The option exercise price
- <a href="/wiki/intrinsic-value/">/wiki/intrinsic-value/</a> — The in-the-money profit component
- <a href="/wiki/long-term-capital-gain-tax/">/wiki/long-term-capital-gain-tax/</a> — Preferential tax treatment for holding periods
- <a href="/wiki/american-option/">/wiki/american-option/</a> — Options exercisable before expiration
- <a href="/wiki/closing-print/">/wiki/closing-print/</a> — How settlement price is determined

</div>