---
title: "Quanto Hedging"
description: "Hedging instruments whose payoffs are delivered in a currency different from their underlying, eliminating FX-asset correlation risk."
keywords:
  - quanto hedge
  - quanto derivative
  - FX-equity correlation
  - dual-currency payoff
  - cross-currency derivative
image: "/svg/risk.svg"
---

*A **quanto hedge** protects an investor from the correlation between an asset's return and changes in the [exchange rate](/currency-risk/) through a specially structured derivative. Unlike a traditional [currency hedge](/currency-risk/), which separates asset risk from FX risk, a quanto product bakes in both simultaneously, delivering payoffs in a domestic currency even when the underlying asset is foreign. The result: FX volatility vanishes, and the investor is left only with asset [idiosyncratic-risk](/idiosyncratic-risk/) and global market risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Quanto Hedging — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark denoting risk and hedging strategies." />

<div class="wiki-infobox-caption">Quanto products eliminate currency risk by fixing the exchange rate in advance.</div>

|   |   |
|---|---|
| **What it is** | A derivative whose payoff is in the investor's home currency but tied to a foreign asset's performance |
| **Also called** | Dual-currency option, quantity-adjusted option, fixed-FX derivative |
| **Key advantage** | Eliminates both [currency-risk](/currency-risk/) and [currency-volatility](/currency-volatility/) from a foreign position |
| **Measured in** | Home currency; the [exchange rate](/currency-risk/) is locked at inception |
| **Used by** | International [equity fund](/growth-fund/) managers, [pension funds](/traditional-ira/), corporates with global operations |
| **Related instruments** | [Cross-currency swap](/cross-currency-swap/), [forward contract](/forward-contract/), [call-option](/call-option/) |

</aside>

## The fundamental problem: FX-asset correlation

An investor in Frankfurt who buys US [equities](/common-stock/) faces two sources of uncertainty: the equity market moves, and the [dollar](/us-dollar/) strengthens or weakens against the euro. If she buys a [call-option](/call-option/) on Apple shares, she wins if Apple rallies and loses if it falls—that is ordinary [market-risk](/market-risk/). But she also wins if the dollar strengthens (converting dollar gains into more euros) and loses if the dollar weakens. The two risks are intertwined, and their [correlation](/correlation-hedging/) matters.

Empirically, FX-asset correlations are often negative during crises: foreign equities crash and the currency weakens together (both representing risk-off moves). This double hit is catastrophic for hedging. A standard [forward contract](/forward-contract/) on the dollar gives you a one-way currency hedge, but it does not adapt if the equity trade moves against you—you still owe the forward, regardless of what the underlying asset did. A quanto structure, by contrast, internalises the FX logic into the derivative itself, creating a payoff that depends on both but is delivered in a single currency without separate FX settlement.

## How a quanto option works

A quanto [call option](/call-option/) on Apple, struck in euros, works like this: the German investor buys the right to buy Apple shares at a fixed price in dollars (say, $150). The option pays off if Apple rises above $150—standard so far. But the payout is *not* converted back to euros at the spot FX rate on expiration. Instead, it is converted at a *fixed FX rate agreed at inception*, say 1.10 USD/EUR. 

If Apple rises to $165 and the dollar has strengthened to 1.15 USD/EUR, a traditional dollar call converted at spot would give EUR 150/1.15 = EUR 130. But the quanto call converts at the fixed 1.10 rate, yielding EUR 150/1.10 = EUR 136. The investor pockets the extra because the dollar strengthened—but *only* if the option was profitable. If Apple falls to $135, the option expires worthless, and the FX rate is irrelevant. The fixed FX rate acts as an embedded [forward contract](/forward-contract/) that cushions the FX impact without creating a standalone exposure.

## Why investors use quantos: decoupling risk

The practical appeal is enormous. A [pension fund](/traditional-ira/) in the UK that wants to gain exposure to Japanese [equities](/common-stock/) could buy yen-denominated [index-fund](/index-fund/) shares, but then it faces both Japanese equity [volatility](/historical-volatility/) and yen-dollar [currency-volatility](/currency-volatility/). Alternatively, it can buy quanto calls on the Nikkei, receiving payoffs in sterling at a locked exchange rate. The fund now has pure equity-market exposure to Japan, with FX volatility removed. If the fund's liability structure is sterling-based, this is ideal: the hedge ratio becomes much simpler to calculate because FX does not jump around.

Similarly, a large [asset manager](/asset-allocation/) in the US with a massive allocation to European [equities](/common-stock/) may fear that a euro crisis would simultaneously tank European stocks and weaken the currency, producing a double loss. By using quanto options (or futures), the manager can buy European equity exposure at a fixed USD/EUR rate, eliminating the correlation tail-risk.

## Quanto forwards and futures

Quanto hedging is not limited to [options](/option/). A quanto [forward contract](/forward-contract/) is straightforward: you agree to buy German DAX index shares in six months at a fixed DAX level (say, 18,000) and a fixed exchange rate (say, 1.10 EUR/USD). At expiration, you pay the agreed dollar amount and receive the DAX shares, converted to dollars at 1.10, regardless of the actual spot rate. A [futures contract](/futures-contract/) listing is similar; many exchanges offer quanto futures on major foreign indices, popular with emerging-market fund managers hedging their international exposures.

## The cost: quanto premium and correlation pricing

Quanto hedges are not free. The [option premium](/option-premium/) on a quanto call is higher than on a vanilla call because the embedded [forward contract](/forward-contract/) (the fixed FX rate) has value. The quanto premium depends on the [correlation](/correlation-hedging/) between the asset and the currency. If equities and the currency are negatively correlated (as they often are), the fixed FX rate is valuable insurance, and the premium is higher. If they are positively correlated, the investor is paying for protection it does not need, and the premium is lower or even a discount.

During calm markets, when asset-currency correlations are near zero, quanto options can be cheaper than vanilla options plus a separate FX forward, because the correlation is priced optimistically. In stressed markets, when negative correlation spikes (risk-off moves slam both assets and currencies), quantos become expensive insurance—exactly when you most want to buy them. This is the eternal insurance dilemma: protection is cheapest when you do not need it.

## Quanto swaps and structured notes

A corporate with long-term foreign-currency debt might enter a quanto [interest-rate swap](/interest-rate/): it pays fixed euros and receives fixed dollars (not floating dollars, but fixed), locked in via a quanto structure. The corporation's liability is now in euros, without FX exposure, and it has effectively taken on a euro [cost-of-debt](/cost-of-debt/) without needing to convert currencies. 

[Structured notes](/securitization/) often embed quanto logic, too. A German investor buys a note that pays based on the Nikkei's performance, converted to euros at a fixed rate. If the Nikkei rises 10 per cent and the yen stays flat, the note delivers a 10 per cent euro return. If the Nikkei falls 10 per cent, the note loses 10 per cent, regardless of yen moves. The simplicity is powerful, but it comes with [counterparty-risk](/counterparty-risk/) (the bank issuing the note) and [illiquidity](/liquidity-risk/); you cannot easily exit before maturity.

## Limitations: when quanto hedges fail

Quanto hedges assume the fixed FX rate is fair and the correlation does not blow out to extremes. In a severe currency crisis, the fixed FX rate can become wildly out-of-the-money, and the investor regrets locking it in. Additionally, if the underlying foreign asset is illiquid or thinly traded, the quanto derivative may not exist or may be extremely expensive to exit.

There is also a subtle accounting and risk-management issue: quanto products can obscure the true [market-risk](/market-risk/) and [currency-risk](/currency-risk/) in a portfolio. A fund manager who holds many quanto derivatives may think FX risk is gone but has instead taken on counterparty risk and [operational-risk](/operational-risk/) from the derivatives themselves. During a [liquidity](/liquidity-risk/) crisis, when both equity and FX markets seize up, unwinding a large position in quanto derivatives can be painful.

## See also

<div class="wiki-seealso">

### Closely related

- [Correlation hedging](/correlation-hedging/) — hedging changes in asset-asset correlations; quantos fix asset-currency correlation
- [Cross-currency basis hedging](/cross-currency-basis-hedging/) — hedging foreign-currency funding costs
- [Currency risk](/currency-risk/) — the FX risk that quantos aim to eliminate
- [Forward contract](/forward-contract/) — the simpler single-currency version; quantos embed forwards
- [Call option](/call-option/) — the underlying instrument often structured as a quanto
- [Futures contract](/futures-contract/) — exchange-listed quanto futures exist for major indices
- [Exchange rate](/currency-risk/) — the fixed rate embedded in quanto structures

### Wider context

- [Asset allocation](/asset-allocation/) — international portfolios often use quantos to simplify hedging
- [Hedge fund](/hedge-fund/) — sophisticated users of bespoke quanto derivatives
- [Counterparty risk](/counterparty-risk/) — the main risk of OTC quanto swaps and options
- [Systemic risk](/systemic-risk/) — correlated asset-currency moves during crises
- [Liquidity risk](/liquidity-risk/) — quanto derivatives can be illiquid in stressed markets

</div>
