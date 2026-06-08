---
title: "Exchange-Traded vs. OTC Derivatives"
description: "Comparison of centrally cleared listed contracts and bilateral over-the-counter deals, spanning standardisation, price discovery, and counterparty risk."
keywords:
  - exchange-traded derivatives
  - otc derivatives
  - centrally cleared
  - standardisation
  - price discovery
  - counterparty risk
image: "/svg/derivatives.svg"
---

*Exchange-traded derivatives are standardised contracts bought and sold on organised exchanges with central clearing, while **OTC derivatives** are bilateral agreements negotiated directly between counterparties. Each model trades convenience and transparency against customisation and dealer optionality, creating a structural divide in how risk is priced, discovered, and managed.*

<div class="wiki-hatnote">

For the general role of exchanges and OTC markets in broader trading, see [Stock Exchange](/stock-exchange/) and [Over-the-Counter Market](/over-the-counter-market/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Exchange-Traded vs. OTC Derivatives — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and financial instruments." />

<div class="wiki-infobox-caption">Two parallel ecosystems for derivatives, each with different rules, transparency, and counterparty structures.</div>

|   |   |
|---|---|
| **Exchange-traded** | Standardised contracts, central clearing, transparency, lower counterparty risk |
| **OTC** | Customised bilaterals, no central counterparty, opacity, higher counterparty risk |
| **Examples (exchange)** | [Futures](/futures-contract/), listed [options](/option/), index swaps |
| **Examples (OTC)** | [Interest rate swaps](/interest-rate/), [credit swaps](/credit-risk/), [forwards](/forward-contract/) |
| **Clearing** | Exchange → clearinghouse; OTC → [bilateral](/over-the-counter-market/) or bilateral with clearing opt-in |
| **Price discovery** | Exchange transparent; OTC dealer-quoted, variable |
| **Margin/collateral** | Exchange standardised; OTC negotiated ([bilateral](/counterparty-risk/) [CSA](/mark-to-market-derivatives/)) |
| **Regulation** | Post-2008: increased; many OTC swaps now mandatory clearing/reporting |

</aside>

## The exchange-traded model: standardisation and centrality

A futures contract traded on the Chicago Mercantile Exchange or [London Stock Exchange](/london-stock-exchange/) is standardised. All March crude oil contracts specify the same quantity, delivery point, and settlement terms. An investor can buy one or ten thousand contracts knowing exactly what they own. The exchange matches buyers and sellers, posts prices in real time for every transaction, and stands between them as the central counterparty through a clearinghouse.

When two parties trade a futures contract, they do not owe each other directly; instead, each owes the clearinghouse. This separation eliminates bilateral [counterparty risk](/counterparty-risk/). If one side defaults, the clearinghouse covers the loss using guarantee funds and member contributions. Participants post initial margin (a deposit) when they open a position and variation margin daily—extra cash if the contract moves against them. This daily [mark-to-market](/mark-to-market-derivatives/) settlement prevents large losses from accumulating.

**Price discovery** is automatic. Millions of participants quoting bids and offers create a [bid–ask spread](/bid-ask-spread/) that reflects supply, demand, and real-time valuations. A trader knows instantly what the most recent trade was and can view the order book. This transparency attracts traders who want liquidity and confidence in pricing.

Listed [options](/option/) work similarly—standardised strike prices, expiration dates, and sizes. Once the exchange publishes a [call option](/call-option/) on Apple stock, any broker can execute your order at the best posted price.

## The OTC model: customisation and opacity

An [interest rate swap](/interest-rate/) is rarely standardised. Party A might want to swap payments on EUR 47 million at a 3.2-year tenor with a specific reset schedule. Party B may have slightly different needs. They negotiate directly through dealers or brokers until they agree on every term: notional amount, coupon, currency, daycount convention, credit terms.

Once agreed, the swap is a bilateral contract. Only the two parties and their dealers know the terms. There is no central clearinghouse (though under post-2008 rules, many standardised swaps *must* now be cleared centrally, blurring the line). Pricing is opaque—only the dealer quoting to you knows what they're charging rivals or what the "market" price is. You cannot simply look up what the last trade was.

[Counterparty risk](/counterparty-risk/) is real and bilateral. If your swap dealer fails, you have a claim on their bankruptcy estate, competing with all other creditors. If your counterparty defaults before [marking-to-market](/mark-to-market-derivatives/), you could face a large loss. To mitigate this, OTC participants negotiate collateral agreements (credit support annexes, or CSAs) that require posting cash or bonds as positions move.

## Why OTC still dominates certain markets

Despite the post-2008 push to centralise clearing, OTC derivatives remain enormous—tens of trillions in notional value globally. Why?

**Customisation.** A bank financing a rare infrastructure project might need a 15-year [interest rate swap](/interest-rate/) in Brazilian reais with unusual reset dates. Exchanges will never standardise this; only OTC dealers can cobble it together. The ability to tailor terms is worth paying a dealer spread.

**Leverage and efficiency.** OTC bilateral agreements allow tighter credit terms between sophisticated counterparties. Two major banks might post lower collateral and give each other looser settlement schedules than any clearinghouse would permit. This efficiency lowers costs for large trades.

**Hedging uniqueness.** A pension fund holding Indonesian government bonds wants to hedge currency and inflation risks together—a non-standard swap. Dealers will custom-build it; an exchange cannot.

**Speed and discretion.** An OTC dealer can execute a large trade and manage it off-book (though increasingly reported). An exchange trade is public and immediate, sometimes undesirable for clients trying to enter or exit quietly.

## Post-2008 regulatory drift: mandatory clearing

The financial crisis exposed OTC opacity. When [Lehman Brothers](/goldman-sachs/) failed in 2008, the web of OTC derivative counterparty exposures froze. No one knew who owed whom. Regulators responded by mandating that standardised OTC derivatives (particularly [interest rate swaps](/interest-rate/) and [credit derivatives](/credit-risk/)) be cleared through central counterparties, reported to trade repositories, and subject to margin rules mimicking exchanges.

This created a hybrid. A "cleared OTC" swap—say, a vanilla 5-year USD [interest-rate swap](/interest-rate/)—now routes through a clearinghouse like a futures contract but is negotiated bilaterally like traditional OTC. The effect is more exchange-like transparency and counterparty safety, but still more customisable than a listed contract.

Uncleared OTC swaps (those too bespoke to standardise) remain bilateral. They face higher capital charges for banks, making them more expensive. This has shifted some marginal trades toward exchange or cleared venues.

## Costs and spreads

Exchange trading incurs transparent, published fees: per-contract commissions or exchange tariffs. Because volume is high, unit costs are often low. Bid–ask spreads are tight—sometimes fractions of a cent per contract.

OTC trading carries dealer spreads and custom fees. The spread reflects the dealer's [funding cost](/cost-of-debt/), risk management burden, and markup. For liquid [interest-rate swaps](/interest-rate/), dealer spreads are narrow (comparable to exchanges), but for exotic or illiquid products, spreads widen to 1–2% of notional value or more.

For long-term or illiquid positions, the OTC cost may be worth the bespoke protection; for plain-vanilla, high-volume hedging, exchanges are cheaper.

## Liquidity and exits

Exchange contracts are liquid by design. A [futures](/futures-contract/) position can be offset instantly—sell one contract to cancel the buy. The bid–ask spread is tight, and volume is visible.

OTC contracts are less liquid. To unwind a 10-year swap, you call your dealer; they may take time to find a counterparty or charge a wide exit spread. If you need to exit quickly or at an unfavourable time, you lose to slippage.

This matters for investors and hedgers holding long-dated hedges. Exchange-traded products offer more exit optionality; OTC offers customisation but less emergency liquidity.

## The structural divide today

The line between exchange and OTC has blurred since 2008, but a broad pattern holds. **Standardised, liquid, short-dated derivatives trend toward exchanges.** Crude oil [futures](/futures-contract/), equity index [options](/option/), short-dated interest rate futures—these belong on exchanges. **Bespoke, illiquid, long-dated derivatives trend toward OTC.** Exotic equity swaps, long-term inflation swaps, single-name credit swaps—dealers dominate these.

The regulatory evolution has made OTC safer (mandatory clearing, collateral rules, reporting) but also more expensive. Dealers now face capital and clearing charges that make small or illiquid OTC trades uneconomical. This is pushing some business toward exchanges or central clearing, though client demand for customisation ensures the OTC market will never disappear.

## See also

<div class="wiki-seealso">

### Closely related

- [Over-the-Counter Market](/over-the-counter-market/) — the bilateral trading infrastructure
- [Stock Exchange](/stock-exchange/) — exchange structure and regulation
- Derivative — the broad category of contracts
- [Futures Contract](/futures-contract/) — the exchange-traded standard
- [Option](/option/) — both exchange-traded and OTC forms exist
- [Mark-to-Market in Derivatives](/mark-to-market-derivatives/) — daily settlement and collateral calls
- [Counterparty Risk](/counterparty-risk/) — central to OTC structural risk

### Wider context

- [Interest Rate](/interest-rate/) — largest OTC derivatives market
- [Credit Risk](/credit-risk/) — credit derivatives mostly OTC
- [Dodd-Frank Act](/dodd-frank-act/) — major post-2008 clearing mandate
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator of exchange trading
- [Bid-Ask Spread](/bid-ask-spread/) — price discovery and liquidity

</div>
