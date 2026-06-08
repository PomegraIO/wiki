---
title: "Cross Currency Pairs: Trading Without the US Dollar"
description: "Cross currency pairs exclude the USD and derive rates from two underlying USD pairs. Learn how indirect FX quotes work."
keywords:
  - cross currency pair
  - cross-currency pair no usd
  - indirect quote forex
  - eur-gbp exchange rate
image: /svg/forex.svg
---

*A **cross currency pair** brings together two currencies, neither of which is the US dollar. The EUR/GBP rate, for example, tells you how many British pounds one euro costs—but that rate isn't quoted independently; it's calculated from the euro-to-dollar and pound-to-dollar pairs. Understanding how this derivation works is essential for spotting pricing anomalies and understanding the mechanics of global currency markets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross Currency Pairs — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex." />

<div class="wiki-infobox-caption">Cross pairs are calculated from two dollar-based pairs; no USD appears in the quotation itself.</div>

|   |   |
|---|---|
| **Definition** | An [FX exchange rate](/stock-exchange/) between two non-dollar currencies |
| **How priced** | Derived from EUR/USD and GBP/USD (or equivalent pairs) |
| **Common crosses** | EUR/GBP, GBP/JPY, AUD/NZD, EUR/CHF |
| **Liquidity tiers** | Major crosses (EUR/GBP) > emerging crosses (BRL/MXN) |
| **Quote calculation** | Divide one USD rate by the other (e.g., EUR/USD ÷ GBP/USD) |

</aside>

## Why Cross Pairs Exist

The dollar dominates global currency trading. Nearly 90% of all FX trades involve the USD on one side. Banks and platforms quote dollar-based pairs as the primary source of liquidity: EUR/USD, GBP/USD, JPY/USD, and so on. For traders or corporates who need to move money between, say, euros and Australian dollars, quoting an AUD/EUR pair directly would be inefficient—the underlying trades would happen in two legs anyway: sell AUD for USD, then sell USD for EUR.

Cross currency pair quotations sidestep the middle step in appearance by bundling that calculation into a single rate. The market-maker or platform does the math behind the scenes, but the end user sees only the cross pair.

## How Cross Currency Pairs Are Calculated

The arithmetic is straightforward. If EUR/USD trades at 1.0800 and GBP/USD trades at 1.2700, the EUR/GBP [cross-currency pair](/cross-currency-pair-no-usd/) rate is:

**EUR/USD ÷ GBP/USD = EUR/GBP**  
**1.0800 ÷ 1.2700 = 0.8504**

This means one euro buys 0.8504 pounds. The calculation is mechanical: one dollar costs 1.2700 pounds, so a euro (which costs 1.0800 dollars) costs fewer pounds.

The order matters. If you want GBP/EUR instead, you invert it:

**GBP/USD ÷ EUR/USD = GBP/EUR**  
**1.2700 ÷ 1.0800 = 1.1759**

One pound buys 1.1759 euros.

Traders working with exotic crosses might see the calculation done differently. If dealing with currencies like the Swiss franc or Mexican peso, a bank might calculate the cross from spot rates that flow through other intermediaries or through [forward-contract](/forward-contract/) rates, but the principle remains: no direct quote exists; it's always derived.

## Liquidity and Bid-Ask Spreads in Crosses

Major crosses—EUR/GBP, EUR/JPY, GBP/JPY, AUD/USD (which is dollar-based but worth noting)—have tight [bid-ask spreads](/bid-ask-spread/) because both underlying pairs are heavily traded. The major banks quote these continuously, and retail platforms pass through competitive pricing.

Exotic crosses (e.g., BRL/MXN, NOK/SEK) are illiquid. The bid-ask spread widens sharply because a dealer must leg into both underlying pairs to hedge, and some of those pairs themselves are thinly traded. If a client asks for a BRL/MXN quote, the dealer might mark up the synthetic rate to cover the cost of executing in both directions.

## Arbitrage and Mispricing in Crosses

If a cross is ever mispriced relative to its component USD pairs, an alert trader can exploit the gap.

Imagine EUR/GBP is quoted at 0.8510, but the math says it should be 0.8504 (as calculated above). A trader can:

1. Sell EUR/GBP at 0.8510 (sell euros, buy pounds)
2. Buy EUR/USD at 1.0800 (buy euros, sell dollars)
3. Sell GBP/USD at 1.2700 (sell pounds, buy dollars)

The synthetic trade locks in a profit because the cross price exceeded its fair value. Real-time pricing data and algorithmic systems hunt for these opportunities constantly, keeping cross rates tight in liquid pairs.

## Common and Liquid Cross Pairs

**EUR/GBP**: One of the most traded crosses. Both the euro and pound are [reserve currencies](/sovereign-debt/) with deep markets; spreads are typically 1–2 pips.

**GBP/JPY**: The pound and yen carry different [interest-rate](/interest-rate/) environments, making this cross popular for [carry-trade](/carry-trade/) strategies.

**EUR/JPY**: Another carry-trade favorite, combining the euro's higher yields with the yen's lower rates.

**AUD/NZD**: The two antipodean currencies trade closely together because of regional [economic cycles](/business-cycle/); spreads are tight.

**Exotic pairs** (BRL/MXN, TRY/ZAR, KRW/THB) are dealer-quoted and rarely see electronic prices. Spreads widen dramatically, and execution quality depends on the dealer's inventory and appetite.

## Why Cross Pairs Matter for Traders and Hedgers

A multinational company operating in the eurozone and the UK needs GBP/EUR [exchange rates](/spot-exchange-rate/). Rather than converting euros to dollars and then to pounds, they trade the cross directly (or via their bank). The calculation is the same, but execution is simpler.

Hedge funds and [currency trading](/algorithmic-trading/) desks monitor crosses for [mispricings](/relative-valuation/), [correlation](/factor-investing/) shifts, and relative [volatility](/implied-volatility/) across related pairs. A sudden shift in EUR/GBP relative to EUR/USD might signal a [credit event](/credit-event-sovereign/) in Britain or a change in [monetary policy](/monetary-policy/) flows.

Retail [forex](/stock-market/) platforms often allow cross-pair trading but may offer worse spreads than direct banking channels. The platform quotes the cross, but if the underlying USD pairs aren't in perfect equilibrium, the cross quote lags or drifts.

## See also

<div class="wiki-seealso">

### Closely related

- [Spot Exchange Rate](/spot-exchange-rate/) — the current rate between two currencies, the foundation for cross calculations
- [Bid-Ask Spread](/bid-ask-spread/) — the cost of trading, typically wider in illiquid crosses
- [Forward Contract](/forward-contract/) — pre-agreed future rates, including cross-currency forwards
- [Carry Trade](/carry-trade/) — trading pairs with different interest rates, popular in crosses like GBP/JPY
- [Interest Rate](/interest-rate/) — influences the [forward-guidance](/forward-guidance/) and [currency-risk](/currency-risk/) premium in crosses

### Wider context

- [Currency Risk](/currency-risk/) — why firms hedge exchange-rate exposure across currencies
- [Central Bank](/central-bank/) — sets rates that indirectly influence cross valuations
- [Market Maker Trading](/market-maker-trading/) — how dealers quote and hedge cross pairs
- [Algorithmic Trading](/algorithmic-trading/) — identifying cross-pair arbitrage opportunities

</div>
