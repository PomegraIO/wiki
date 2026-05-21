---
title: "Options (Cryptocurrency)"
description: "Derivatives granting the right to buy or sell a cryptocurrency at a predetermined price and time."
---

*A cryptocurrency option is a derivative contract that grants the holder the right—but not the obligation—to buy (call option) or sell (put option) a specified amount of cryptocurrency at a predetermined price (strike price) by a certain date (expiration). Options are popular tools for hedging, speculation, and arbitrage. Unlike [futures-contract](/wiki/futures-contract/), which require settlement, options allow the holder to walk away if the underlying asset moves against them.*

<aside class="wiki-infobox">
<div class="wiki-infobox-title">Cryptocurrency Options — key facts</div>
<table>
<tr><th>Type</th><td>Calls (right to buy) or puts (right to sell)</td></tr>
<tr><th>Strike price</th><td>Predetermined exercise price</td></tr>
<tr><th>Expiration</th><td>Fixed date after which the option expires worthless</td></tr>
<tr><th>Premium</th><td>Cost to buy the option</td></tr>
<tr><th>Payoff</th><td>Asymmetric: limited loss, unlimited gain (calls)</td></tr>
</table>
</aside>

## Call and put options

A Bitcoin call option with a $40,000 strike price expiring in one month gives you the right to buy 1 Bitcoin at $40,000 any time before expiration. You pay a premium upfront (say, $2,000) for this right. If Bitcoin rises to $45,000, you exercise the option, buy at $40,000, and immediately sell at $45,000, pocketing a $3,000 profit minus the $2,000 premium = $1,000 net profit. If Bitcoin falls to $35,000, you let the option expire worthless and lose only the $2,000 premium (not the full downside to $35,000).

A Bitcoin put option works the opposite way. A put with a $40,000 strike gives you the right to sell Bitcoin at $40,000. If Bitcoin falls to $35,000, you exercise the put, buy at $35,000, and sell at $40,000, pocketing $5,000 minus the premium. Puts are commonly used as hedges: if you own Bitcoin but fear a price crash, you can buy a put option to limit your downside.

## Leveraged speculation

Options allow traders to gain leveraged exposure to cryptocurrency with limited capital. Buying a call option is cheaper than buying the underlying asset outright but offers similar upside if the price appreciates. A trader might allocate $1,000 to call options instead of buying 0.025 Bitcoin directly. The call option gives them exposure to Bitcoin's full upside (if it rises above the strike), but the maximum loss is limited to $1,000.

This leverage is double-edged. If Bitcoin rises, the option buyer wins big. If Bitcoin falls or stays flat, the option buyer loses the entire premium. Option buyers are usually betting on large moves (either up or down); option sellers (who pocket the premium) are usually betting on small moves.

## Implied volatility and option pricing

The price of an option (the premium) depends on several factors:

- **Time to expiration.** Options with more time are more valuable because there is more time for the underlying asset to move.
- **Implied volatility.** How much the market expects the asset to move between now and expiration. Higher volatility = higher premiums, because options are more likely to be "in the money" (exercised).
- **Strike price distance.** Options that are farther "out of the money" (less likely to be exercised) are cheaper.
- **Interest rates.** (Minor factor in crypto.)

Implied volatility is not the actual volatility; it is the market's forecast. If Bitcoin volatility is higher than the market expects, call and put buyers profit. If volatility is lower than expected, option sellers profit. Volatility trading is a major profit source for sophisticated traders.

## American vs. European options

American options can be exercised any time before expiration. European options can be exercised only at expiration. Most traded cryptocurrency options are American-style because they offer more flexibility. However, most crypto options exchanges are decentralized and lack the infrastructure to support early exercise, so American and European options trade at very similar prices.

## Options on crypto exchanges and protocols

Cryptocurrency options are traded on several venues:

- **Centralized exchanges.** Deribit (which specializes in Bitcoin and Ethereum options) is the largest venue. They offer order books where traders post bids and asks. Settlement is in cryptocurrency, and trading is 24/7 (unlike traditional stock options markets).
- **Decentralized protocols.** Opyn, Lyra, and Thales issue options as smart contracts. Traders can trade directly from their own wallets without depositing into a centralized exchange. These protocols often use automated market makers to price options rather than order books.
- **Over-the-counter (OTC).** Large traders negotiate bilateral options with dealers, similar to traditional finance.

## Hedging and arbitrage

Options are widely used for hedging. A Bitcoin holder can buy a put option to protect against downside (insurance). The cost of the insurance is the premium paid for the put. An options seller (who receives the premium) is essentially providing insurance—they pocket the premium in exchange for bearing the downside risk.

Arbitrage opportunities arise when options are mispriced relative to the underlying asset. If a call option is too cheap, a trader can buy the call, short the underlying asset, and lock in a risk-free profit. These opportunities are quickly exploited by quantitative traders, keeping prices fairly efficient.

## Volatility and tail risk

During normal times, cryptocurrency options prices reflect historical volatility and market expectations. But during crises, volatility can spike, and options prices can move dramatically. A trader holding call options during a crash sees the options lose value rapidly (both because Bitcoin fell and because expected volatility decreased post-crisis). Conversely, a trader holding put options profits handsomely if they bet correctly on the direction and severity of the crash.

Tail-risk hedges—out-of-the-money put options purchased well in advance—can be very expensive during normal times but invaluable during crises. Determining whether the cost is justified is a difficult decision that depends on how much tail risk you believe is priced in.

## Regulatory status

Most countries have not explicitly regulated cryptocurrency options. In the US, the CFTC has allowed trading of Bitcoin and Ethereum options under certain conditions, but retail access is limited. Some jurisdictions ban derivatives on cryptocurrency entirely. Regulatory uncertainty is a barrier to options market growth.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — the traditional finance equivalent.</li>
<li><a href="/wiki/futures-contract/">Futures Contract</a> — another crypto derivative used for hedging and speculation.</li>
<li><a href="/wiki/forex-option/">FX Option</a> — options on currency pairs, conceptually similar.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/bitcoin/">Bitcoin</a> — the most-traded cryptocurrency for options.</li>
<li><a href="/wiki/ethereum/">Ethereum</a> — the second most-traded cryptocurrency for options.</li>
<li><a href="/wiki/cryptocurrency-exchange/">Cryptocurrency Exchange</a> — platforms where options are traded.</li>
</ul>
</div>
