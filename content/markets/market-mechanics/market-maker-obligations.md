---
title: "Market Maker Obligations"
description: "Regulatory requirements and contractual duties for providing continuous liquidity in securities markets."
keywords:
  - market maker
  - liquidity provision
  - bid-ask spread
  - regulatory obligation
  - market obligation
---

*A **market maker** is a securities firm or individual that stands ready to buy and sell a given security at publicly quoted prices, maintaining [bid-ask spreads](/wiki/bid-ask-spread/) and absorbing inventory risk. **Market maker obligations** are the regulatory requirements and contractual duties that require continuous quoting, minimum spread widths, position limits, and other provisions that ensure market liquidity.*

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Primary duty** | Continuous two-sided quotation (bid and ask) |
| **Spread constraint** | Tied to volatility; typically less than 1% in normal markets |
| **Minimum order size** | Often 100 shares (standard lot) or contractual minimum |
| **Inventory limit** | Position size caps to limit risk |
| **Tier** | Exchange-listed, [OTC](/wiki/over-the-counter-market/), or [ATS](/wiki/alternative-trading-system/)-specific |
| **Compensation** | Bid-ask spread + rebates or fees from exchange |
| **Enforcement** | Exchanges, [FINRA](/wiki/finra/), [SEC](/wiki/securities-and-exchange-commission/) |

</aside>

## Core obligations

Market makers have two primary regulatory obligations:

1. **Continuous quotation**: Display firm bid and ask quotes during regular market hours (9:30 AM–4:00 PM EST for equities). A market maker cannot simply withdraw and wait for better conditions; they must remain present even when the market is moving against them.

2. **Minimum spread width**: The difference between bid and ask must not exceed regulatory or self-regulatory limits. For highly liquid stocks, spreads are capped at one penny ($0.01). For less liquid stocks, spreads may be wider (e.g., $0.05–$0.25).

Beyond these, market makers typically agree to:

- **Minimum size**: Quote for at least a standard lot (100 shares) at the quoted price
- **Order priority**: Execute orders at the quoted price when presented by [brokers](/wiki/broker/) or the market
- **Position limits**: Not hold inventory exceeding contractual thresholds (to limit risk and ensure they can absorb new flow)

## Why these obligations exist

Continuous quotation and tight spreads serve the public interest by reducing [trading costs](/wiki/market-impact-cost/). In a market without obligations, market makers would only appear when they saw profitable opportunities. The result would be wide spreads, long waits to trade, and higher costs for investors.

By requiring continuous quotation, regulations ensure that investors can trade quickly at tight prices. The [SEC](/wiki/securities-and-exchange-commission/) and [FINRA](/wiki/finra/) enforce this through surveillance and penalties.

## Market maker exemptions and exceptions

Even with obligations, market makers have limited exemptions:

- **Volatility halts**: During extreme market swings (e.g., stock up 20% in minutes), market makers can suspend quotation under Regulation SHO provisions. But this is rare and monitored.
- **News-driven pauses**: If material news is pending, spreads may widen (not narrower) and quotation may be limited. Still, the obligation to display bids and asks persists.
- **Technical failure**: If a market maker's systems fail, they must notify the exchange and can be excused temporarily, but service restoration is expected quickly.

## Compensation models

Market makers are compensated through:

1. **Bid-ask spread**: The difference between what they buy and sell at. Buying at $99.50 and selling at $99.75 on a 100-share order yields $25. Over thousands of trades, this accumulates.

2. **Exchange rebates**: Exchanges pay market makers per share quoted or filled, typically $0.001–$0.003 per share. This subsidizes the role and incentivizes participation.

3. **Order flow revenue**: Some market makers sell order flow to high-frequency traders. The [payment for order flow](/wiki/payment-for-order-flow/) (PFOF) model is controversial; the SEC has scrutinized it for potential conflicts of interest.

Compensation is tight: net spreads (spread minus exchange fees) on liquid stocks is 0.5 basis points to 1 basis point (0.005%–0.01%). Market makers rely on high volume to be profitable, which incentivizes them to quote tightly and execute efficiently.

## Options and derivatives obligations

Options and derivatives markets have their own market maker obligations. In [options](/wiki/option/), market makers must quote bids and asks for all strikes and expirations. The [CBOE](/wiki/cboe-options-exchange/) requires participation in the "crowd" (collective term for all market makers in a given product).

[Futures markets](/wiki/futures-contract/) (managed by the CME and other exchanges) also impose liquidity requirements: members must post orders in the order book or face penalties.

## Technology and algorithms

Modern market making relies on algorithms that automatically adjust quotes based on:

- **Volatility**: Wider spreads when implied volatility spikes
- **Inventory**: Tighten bids (buy more) when inventory is low; tighten asks (sell more) when inventory is high
- **Correlation**: Adjust prices based on related securities (e.g., a market maker in IBM will adjust quotes based on [S&P 500 futures](/wiki/sp-500-index/))

Algorithms are monitored by exchanges and the SEC to ensure they comply with obligations. "Quote stuffing" (posting and canceling orders to manipulate prices) and "layering" (creating false liquidity) are violations.

## Market maker failure and contagion

When market makers fail or withdraw, market liquidity dries up. The [flash crash of 2010](/wiki/flash-crash-2010/) saw a brief but severe withdrawal of market making, resulting in extreme spreads and a temporary market collapse. This prompted new circuit-breaker rules and better surveillance.

The March 2020 COVID-19 panic saw similar liquidity pressures, prompting emergency Fed measures to support market function.

## Distinction from [principal trading](/wiki/principal-trading/)

A market maker acting as principal (risking their own capital) differs from a broker acting as agent (facilitating trades for clients without taking positions). Market makers are principals; they must be willing to own positions and absorb losses. This distinction matters for regulation and liability.

## Global variations

Market maker obligations vary internationally:

- **U.S. equities**: Automated market makers on [NASDAQ](/wiki/nasdaq/) with strict spread and quotation rules.
- **U.S. options**: Designated market makers on the CBOE with crowd participation requirements.
- **European equities**: Market makers under [MiFID II](/wiki/mifid-ii/) regulations with similar spread and liquidity obligations.
- **Crypto exchanges**: Many crypto exchanges claim no market maker obligations, leading to wider spreads and lower liquidity for smaller altcoins.

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/wiki/bid-ask-spread/) — The compensation mechanism for market makers
- [Market maker trading](/wiki/market-maker-trading/) — The mechanics of how market makers operate
- [Payment for order flow](/wiki/payment-for-order-flow/) — Controversial compensation model
- [Price improvement](/wiki/price-improvement/) — When broker improves on market maker quotes

### Wider context

- Market microstructure — Broader study of trading mechanics
- [Flash crash 2010](/wiki/flash-crash-2010/) — Event that exposed liquidity fragility
- [Regulation SHO](/wiki/regulation-sho/) — Framework governing short selling and market maker conduct
- [Best execution](/wiki/best-execution/) — Broker obligations that interact with market maker obligations

</div>