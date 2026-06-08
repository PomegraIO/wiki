---
title: "Over-the-Counter Option"
description: "Bilaterally negotiated option contracts traded directly between parties outside exchange infrastructure; offer customisation at the cost of counterparty risk."
keywords:
  - derivatives trading
  - customisable options
  - bilateral agreements
  - counterparty risk
  - over-the-counter markets
image: "/svg/derivatives.svg"
---

*An **over-the-counter (OTC) option** is an [option](/option/) contract negotiated directly between two parties—typically financial institutions, large corporates, or sophisticated investors—entirely outside exchange markets. The buyer and seller agree on the underlying asset, strike price, expiration, settlement method, and any other terms, then execute the trade bilaterally. This flexibility comes at a cost: the counterparty becomes your credit risk.*

<div class="wiki-hatnote">

For exchange-listed options with negotiated terms, see [FLEX Options](/flex-options/). For standardised exchange options, see [Option](/option/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Over-the-Counter Option — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Customisation without clearinghouse protection; credit becomes the limiting factor.</div>

|   |   |
|---|---|
| **What it is** | Bilaterally negotiated options traded directly between counterparties |
| **Clearing** | None; each party bears counterparty risk unless subject to CSA |
| **Customisation** | Unlimited—any strike, expiry, settlement, underlying |
| **Liquidity** | Depends entirely on relationship and negotiating leverage |
| **Primary participants** | Banks, hedge funds, multinational corporates, asset managers |
| **Regulation** | Post-2008: increasingly subject to central clearing and reporting mandates |

</aside>

## The bilateral world: full customisation

A multinational corporation wanting to hedge a foreign exchange exposure in exactly 73 days, or a private equity firm needing a floor on a portfolio at a precise level, cannot rely on standard [exchange](/stock-exchange/) [option](/option/) calendars. They turn to an OTC derivatives desk at a bank.

The corporation calls the desk and describes its need: "I need to hedge EUR/GBP at 0.8500 for exactly 11 weeks, with euros deliverable in London." The dealer prices the custom put option, quotes a [premium](/option-premium/), and if both parties agree, they execute. No regulatory approval, no clearinghouse, no publication to an exchange—just a legal contract between two entities.

This flexibility is OTC's defining feature. Strike prices, expirations, settlement locations, settlement methods, notional amounts, [exercise](/exercise-price/) styles, and even the underlying asset can be entirely bespoke. An exotics desk might structure a knockout option (cancels if the underlying breaches a barrier), a cash-or-nothing digital, or a custom basket of FX pairs.

## Counterparty risk: the friction cost

The price of this customisation is counterparty risk. In an exchange-traded option, the clearinghouse interposes itself: when you buy, the clearinghouse becomes your counterparty; when you sell, it becomes the buyer's counterparty. The clearinghouse's capital and guarantee back both sides. With OTC options, you have only the other party's promise to pay at expiry.

If the underlying moves sharply in your favour, your option becomes valuable, and the counterparty—which may now be sitting on a large loss—faces pressure to hedge, walk away, or default. This happened widely during the 2008 financial crisis: counterparties that looked creditworthy at inception failed or required government bailouts as derivative losses mounted.

Sophisticated OTC counterparties mitigate this via **Credit Support Annexes (CSAs)**, legal agreements that require daily posting of collateral as the option's value fluctuates. If your £10 million put moves to £12 million in your favour, the counterparty must post £2 million to you to cover the mark-to-market movement. This reduces credit exposure but introduces operational friction and reinvestment risk.

## Pricing and access

OTC options trade at [dealer quotes](/market-maker-trading/), not in a transparent order book. A desk quotes a mid-price and [bid-ask spread](/bid-ask-spread/) based on its own cost of capital, inventory, hedging capacity, and leverage. There is no continuous price auction as there is on an exchange. If you need a five-year out-of-the-money equity call, you might get just one or two quotes, from banks with deep exotic option books. Spreads are wider than exchange options—sometimes dramatically so—and the quote is often valid for seconds, not minutes.

Pricing is also relationship-dependent. A major asset manager with years of history and significant trading volume will negotiate better terms than a one-off client. Banks reward sticky, long-term relationships.

## Settlement and delivery

OTC options can settle in any manner the parties agree: physical delivery of shares, cash settlement, net settlement, or settlement into a specific currency or location. A multinational can specify that a GBP/USD option settle through its operating subsidiary's account in London, not New York. A pension fund buying equities via OTC call options can specify European delivery venues.

This flexibility becomes critical for international corporates managing multi-currency exposures or complex hedges.

## Regulatory evolution and mandatory clearing

For decades, OTC derivatives were the Wild West: unregulated, opaque, and subject only to bilateral credit discipline. The 2008 crisis exposed systemic risk—the sheer interconnectedness and leverage in OTC markets meant that one major counterparty failure (Lehman Brothers) nearly brought down the entire financial system.

Post-2008, regulation (notably the Dodd-Frank Act in the U.S., EMIR in Europe) mandated that most standardised OTC derivatives—including vanilla calls and puts on major underlyings—be cleared through central clearinghouses. This removes counterparty risk for the majority of OTC volume. Truly exotic or bespoke trades, lacking sufficient standardisation, remain bilateral but face reporting, margin, and capital requirements.

The effect is a blurring of the OTC-exchange line. Many large OTC derivatives are now centrally cleared, reducing their counterparty risk to that of exchange options. However, the customisation (non-standard strikes, expirations, or exotic payoffs) remains the OTC realm.

## Who uses OTC options and why

**Corporate treasurers** hedge specific exposures—foreign exchange, commodity prices, interest rates—with custom dates and strikes matching actual business flows rather than exchange calendars.

**Large asset managers** manage tail risk or rebalance portfolios on precise dates without waiting for standard option expirations.

**Banks and dealers** run proprietary trading desks that profit from quoting OTC prices wider than cost, exploiting information asymmetry and their privileged access to funding.

**Hedge funds** build complex payoff structures (exotics, basket options, conditional payoffs) impossible to assemble from exchange options.

**Insurance companies** and **pension funds** use OTC swaptions and interest-rate options to manage long-duration liabilities on specific schedules.

**Smaller corporates** with niche exposures (a single currency pair, a commodity of minor volume) find liquidity only in the OTC market, where a dealer's relationship desk will quote a price.

## Comparison to exchange options and FLEX

Exchange-traded options offer tight spreads, instant execution, and zero counterparty risk—but only in standard strikes and expirations. [FLEX options](/flex-options/) add customisation while keeping clearinghouse protection. OTC options are unlimited in structure but force you to manage bilateral credit and accept wider spreads.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — the foundational derivative right
- [Strike Price](/strike-price/) — customisable in OTC negotiation
- [Option Premium](/option-premium/) — bilaterally agreed, not posted by a market maker
- [Counterparty Risk](/counterparty-risk/) — the defining structural feature of OTC
- [FLEX Options](/flex-options/) — exchange alternative with custom terms
- [Option Series](/option-series/) — the standard pre-set alternative

### Wider context

- [Bid-Ask Spread](/bid-ask-spread/) — typically much wider in OTC than on exchanges
- [Dodd-Frank Act](/dodd-frank-act/) — mandated central clearing of standardised OTC derivatives
- [Credit Support Annex](/credit-risk/) — collateral agreement mitigating counterparty risk
- Securitisation — bundling technique for OTC derivatives

</div>
