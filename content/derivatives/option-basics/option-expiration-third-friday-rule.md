---
title: "The Third-Friday Option Expiration Rule Explained"
seo_title: "Third Friday Option Expiration: Why and How It Works"
description: "Standard monthly options expire the third Friday because CBOE set the convention in 1973. Last trading day, settlement, and assignment timing explained."
keywords:
  - option expiration third friday rule
  - third friday option expiration
  - option last trading day
  - monthly option expiration date
  - option settlement mechanics
image: /svg/derivatives.svg
---

*Standard monthly equity [options](/?option/) expire on the **third Friday of each month**. This is not a natural law—it is a deliberate market convention, codified by options exchanges decades ago. Traders must understand the distinction: the third Friday is the **last day on which an option can be exercised or traded**; settlement and assignment occur on the following Monday or Tuesday, after the market close and the [underlying](/?stock/) asset's final price is set.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Third-Friday Expiration — Key Facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A convention, not a law. Know the difference between last trading day and settlement.</div>

|   |   |
|---|---|
| **Expiration day** | Third Friday of every month, 4:00 PM ET market close |
| **Last trading day** | Same as expiration day; after close, no trading in that month's contract |
| **Settlement day** | Next business day (Monday if Friday is followed by a weekend, or the next trading day after a holiday) |
| **Assignment timing** | After-hours; assigned parties notified by the following day |
| **Historical origin** | Set by CBOE in 1973; copied by all major U.S. options exchanges |
| **Cash or physical settlement** | Equity options settle in cash; assignment transfers shares or cash to/from the account |
| **Weekly options** | Expire every Friday (introduced 2005); not subject to the third-Friday rule |

</aside>

## Why the Third Friday?

When the Chicago Board Options Exchange (CBOE) launched equity options trading in 1973, exchange operators needed to choose a uniform [expiration date](/?expiration-date/). A single expiration per month simplifies clearing, reduces operational risk, and ensures that all market participants are trading the same contract specifications. They settled on the **third Friday of each month** because:

1. **Avoiding month-end chaos.** The last Friday of the month would conflict with quarterly earnings announcements, dividend distributions, and other month-end corporate events, creating volatile conditions for options sellers and settlements.

2. **Mid-month equilibrium.** The third Friday provides enough calendar cushion between expiration and month-end, reducing the risk that a single economic event (like a jobs report or Fed announcement) would coincide with expiration and amplify volatility.

3. **Convenience.** The third Friday is easy for traders to remember and calculate (no need to look up exact dates).

4. **International precedent.** The choice aligned with conventions used in some European options markets.

Once CBOE adopted the third Friday, all other U.S. options exchanges—[NYSE Arca](/?nyse-arca/), Nasdaq, etc.—adopted the same convention to ensure unified [price discovery](/?price-discovery/) and prevent arbitrage between venues.

## Last Trading Day vs. Settlement Day

The **last trading day** is Friday, 4:00 PM ET (market close). After that moment, no trader can open or close a position in that month's contract. Orders to buy or sell that specific option contract are rejected.

**Settlement** occurs the next business day. If the third Friday is followed by a weekend, settlement is Monday. If a holiday intervenes, settlement is the following trading day. During settlement:

- **Exercised calls and puts** are honored: the [underlying](/?stock/) shares are transferred, and cash flows are paid.
- **Assignments** are randomly distributed among traders who are short (sold) calls or puts.
- **Price lockdown** occurs: the [stock](/?stock/) price used to determine which options are in-the-money is set at the close of the [underlying](/?stock/) market on Friday.

For example, if you own a Microsoft call [option](/?option/) with a [strike price](/?strike-price/) of $400, expiring on the third Friday, and Microsoft closes at $410, your call is in-the-money. On Friday at 4:00 PM, you can exercise; the exchange will assign a short seller to deliver 100 shares of Microsoft at $400 on Monday. You pay $40,000 (100 shares × $400 strike), and the assigned seller receives $40,000 and must hand over the shares.

## The Impact on Implied Volatility

As the third Friday approaches, options behavior changes. In the final hours of trading, options with prices very close to the [underlying](/?stock/) asset's current price (at-the-money options) see sharp increases in [implied volatility](/?implied-volatility/). This is called **gamma risk** at expiration.

At-the-money options are sensitive to every tick in the [stock](/?stock/) price; tiny moves in the [underlying](/?stock/) translate to large percentage moves in the option's value. Market makers widen [bid-ask spreads](/?bid-ask-spread/) to account for this gamma exposure. Traders holding short [options](/?option/) positions often unwind or hedge them the day before expiration to avoid the chaos.

Also on the third Friday, **open interest** (the number of outstanding contracts) often declines sharply as positions are exercised, assigned, or closed out. The following Monday, trading in the fourth-Friday (or following third-Friday) contracts typically surges as traders rebalance.

## Mechanics of Assignment

When an option holder exercises a call or put, the exchange uses a random number generator to select a short seller (an option writer) to fulfill the obligation. The assignment happens **after the market closes** on Friday. The assigned seller is notified by their broker no later than the following morning.

**Assignment timing matters for dividends.** If a [call option](/?call-option/) holder exercises before the ex-dividend date, they receive the upcoming dividend. Sellers are aware of this and may close positions before ex-dividend dates if dividends are large. This creates a "dividend risk" for short calls.

**For put options**, assignment means the buyer will deliver shares and the seller will pay cash. A put seller who is assigned must be prepared to receive shares and pay the [strike price](/?strike-price/) in full by settlement (Monday or the next business day). A margin account with sufficient buying power is required.

## Weekly Options and Other Expirations

The third Friday rule applies to **standard monthly [options](/?option/)**. However, since 2005, exchanges also offer **weekly [options](/?option/)**, which expire every Friday (not just the third). Weeklies are now available on many widely traded stocks and indexes and have become popular for traders seeking shorter-duration positions and lower [time decay](/?time-decay-theta/).

Additionally, some stocks offer **quarterly [options](/?option/)** (expiring on the third Friday of March, June, September, December) and **long-dated [options](/?option/)** called LEAPS (Leap Expectancy Anticipation Securities), which expire annually in January. These all follow specific calendars but are less liquid than monthly [options](/?option/).

[Index options](/?option/), like those on the S&P 500, also expire on the third Friday of the month, but settlement is cash-based (not physical share delivery) because an index cannot be physically traded.

## Practical Implications for Traders

**Avoid holding short [options](/?option/) through expiration.** The final hour of trading on the third Friday is chaotic; implied volatility spikes, and liquidity can vanish. A seller who needs to unwind should close positions by Wednesday or Thursday to ensure an orderly exit.

**Understand assignment risk.** Short call and put sellers must keep enough cash and margin to handle assignments. A seller of 10 calls at a $100 strike must have $100,000 available (plus margin requirements) to be assigned and forced to pay.

**Plan around dividends.** Call sellers face early assignment risk if a large dividend is paid between now and expiration. If you are short calls on a dividend stock, the [call option](/?call-option/) holder may exercise early (on or just before the ex-dividend date) to capture the dividend. This is economically rational for them and unfavorable for you.

**Roll positions before expiration.** Most institutional and sophisticated traders close expiring positions a few days before the third Friday and open new positions in the next month. This avoids the expiration-day chaos and reduces the probability of unwanted assignment.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — Fundamental derivative contract structure
- [Call Option](/call-option/) — Right to buy an underlying asset
- [Put Option](/put-option/) — Right to sell an underlying asset
- [Strike Price](/strike-price/) — The fixed price at which an option is exercised
- [Implied Volatility](/implied-volatility/) — Option pricing and expiration behavior
- [Time Decay (Theta)](/time-decay-theta/) — How options lose value as expiration nears

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — Broader use of options
- [Expiration Date](/expiration-date/) — General concept
- [Volatility Smile](/volatility-smile/) — Option pricing patterns at expiration
- [Option Premium](/option-premium/) — What an option costs

</div>