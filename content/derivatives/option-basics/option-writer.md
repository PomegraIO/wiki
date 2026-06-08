---
title: "Option Writer"
description: "The seller of an option contract who receives a premium and assumes the obligation to buy or sell the underlying asset if the buyer exercises."
keywords:
  - option seller
  - covered call
  - naked call
  - premium received
  - obligation
image: "/svg/derivatives.svg"
---

*An **option writer** is the seller of an [option](/option/) contract—the party who collects the [option premium](/option-premium/) upfront and accepts the obligation to buy or sell an underlying asset if the buyer chooses to exercise. While writers earn steady income from premiums, they bear asymmetrical risk if prices move sharply against their position.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Writer — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and financial contracts." />

<div class="wiki-infobox-caption">The party who takes the short side of an options trade, collecting premium in exchange for obligation.</div>

|   |   |
|---|---|
| **What it is** | Seller of a call or put option; receives premium; assumes obligation to perform if exercised |
| **Also called** | Option seller, naked writer (if unhedged) |
| **Profit potential** | Limited to the premium collected |
| **Loss potential** | Unlimited (call writer) or substantial (put writer) if price moves unfavourably |
| **When used** | Income generation, hedging long positions, or directional bearish views |

</aside>

## The mechanics of writing an option

When an [option writer](/option-writer/) sells an option, they receive cash immediately—the option premium. That payment is non-refundable; the writer keeps it whether or not the buyer exercises. The obligation, however, is real. If the buyer holds the option until [expiration](/expiration-date/) and exercises, the writer must perform: deliver the underlying asset (for a call writer) or purchase it (for a put writer). The writer has no choice in the matter.

Consider a writer who sells a call option on shares they own. The buyer pays $3 per share upfront. If the stock price stays below the [strike price](/strike-price/), the option expires worthless, and the writer keeps the premium—a clean win. If the stock rallies past the strike, the buyer exercises, and the writer must sell their shares at the strike price, forgoing any gain above that level. The premium partially cushions that loss, but it does not fully offset it if the stock rises sharply.

## Covered vs. naked writing

The line between prudent income generation and reckless speculation lies in whether the writer owns or has secured the underlying asset. A **covered writer** holds the asset (or cash, in the case of a put) before selling the option. They are insured against extreme loss because they already possess what might be taken from them. Writing covered calls against a stock portfolio is a common strategy to extract income from a position you do not mind selling.

A **naked writer** has no such hedge. They have sold an obligation to deliver (or purchase) an asset they do not own. If the market moves catastrophically, they can face unlimited losses—forced to buy shares at any price to fulfil the call, or to absorb enormous losses on a deeply in-the-money put. Regulatory frameworks and brokers typically restrict naked writing to sophisticated traders with adequate capital.

## Profit and loss dynamics

The writer's profit is **capped** at the premium received. No matter how far the underlying asset falls (for a call writer) or rises (for a put writer), the writer earns no more than that initial payment. This is the structural trade-off: guaranteed income, limited upside. In a calm market or one moving in the writer's favour, this is ideal. In a volatile or adversarial market, it becomes a straightjacket.

The writer's losses, by contrast, have no ceiling. A call writer who sold at $50 strike for a $3 premium faces a $2 loss if the stock rallies to $51, even after the premium. A call writer suffers a $7 loss at $60 (=$60−$50−$3). At $100, the loss is $47. The premium shrinks in significance as the stock climbs. Put writers face similar, though opposite, losses if the underlying asset collapses.

## When writers take on risk

Option writers accept these asymmetries for different reasons. **Income traders** use covered writing on positions they hold anyway; the premium supplements their return, and early exercise means they sell at a price they already found acceptable. **Hedgers** write options to offset downside risk elsewhere in their portfolio. A farmer who worries about falling grain prices might sell call options on cattle futures, locking in a floor while collecting premium.

**Naked writers** typically work with indices, currencies, or heavily capitalised securities where the standard deviation of price moves is predictable. A [market maker](/market-maker-trading/) or professional trader might write options to capture the [bid-ask spread](/bid-ask-spread/) or exploit [implied volatility](/implied-volatility/) they believe is too high. These are not passive activities; they require tight [risk management](/operational-risk/) and constant monitoring.

## The premium reflects risk

The [strike price](/strike-price/), time to [expiration](/expiration-date/), and the [volatility](/historical-volatility/) of the underlying all affect what premium a writer can collect. Out-of-the-money options fetch lower premiums but pose less risk. In-the-money options carry higher premiums but bind the writer tighter. Longer expiries mean more time for prices to move, so writers collect fatter premiums—but also absorb more risk. High-volatility assets attract higher premiums because buyers will pay more for the right to bet on big moves.

A writer who sells options expecting a calm market is betting against volatility. That position is profitable if markets remain stable, but it inverts to catastrophic loss if a shock hits. Many institutional blow-ups stem from writers who systematically underpriced tail risk.

## Writer obligations and early exercise

A writer cannot force the buyer to wait until expiration. An [American option](/option/) can be exercised at any point. A writer who sold a call on a stock about to go ex-dividend may face early exercise even if the option was out-of-the-money—the buyer exercises just to lock in the [dividend](/dividend/). Writers must keep their positions properly margined and their cash or securities ready. A surprise early exercise, miscalculated for, has ended many trading accounts.

## See also

<div class="wiki-seealso">

### Closely related

- [Option Buyer](/option-buyer/) — the counterparty who purchases the right and pays the premium
- [Covered Call](/covered-call/) — a conservative strategy where the writer owns the underlying asset
- [Option Premium](/option-premium/) — the price paid to the writer for the option
- [Strike Price](/strike-price/) — the price at which the writer must perform
- [Naked Call](/option/) — writing calls without owning the underlying; unlimited risk
- [Early Exercise](/expiration-date/) — the buyer's right to exercise before expiration, which binds the writer

### Wider context

- [Option](/option/) — the underlying contract type
- [Futures Contract](/futures-contract/) — an alternative derivative obligating both parties
- [Volatility Smile](/volatility-smile/) — how implied volatility shapes option premiums across strikes
- [Greeks](/delta/) — measures (delta, gamma, theta) that quantify a writer's exposure

</div>
