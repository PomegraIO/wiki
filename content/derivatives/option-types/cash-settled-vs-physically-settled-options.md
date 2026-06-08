---
title: "Cash-Settled vs Physically Settled Options"
description: "Understand the difference between cash-settled and physically settled options, which markets use each method, and what this means for option holders at expiration."
keywords:
  - cash settled options
  - physically settled options
  - option settlement
  - cash settlement expiration
  - physical delivery options
image: "/svg/derivatives.svg"
---

*The defining difference between **cash-settled and physically settled options** comes down to what happens at expiration: one sends money, the other sends the actual asset. While physical delivery once dominated equity options, cash settlement now dominates index options, equity index futures, and foreign exchange derivatives—a shift driven by efficiency, scale, and reduced operational risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Settlement Method — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">How the option holder receives profit depends on the settlement mechanism written into the contract.</div>

|   |   |
|---|---|
| **Physical settlement** | Underlying asset delivered to holder; original equity options standard |
| **Cash settlement** | Difference between strike and spot price paid in cash; now the global standard for indices |
| **Determines** | Counterparty risk, liquidity needed, operational burden, margin requirements |
| **Who uses which** | Equities: mostly physical; indices, forex, commodities: mostly cash |
| **Arbitrage risk** | Cash-settled derivatives can break link to physical market in extreme conditions |

</aside>

## How physical settlement works

When an option is physically settled, the holder receives the actual underlying asset—or the writer must deliver it. An equity call option physically settled means the holder can demand 100 shares per contract at the strike price. A commodity option physically settled means the holder gets barrels of oil, bushels of wheat, or live cattle, depending on the contract.

This sounds straightforward, but it carries real costs. The holder must arrange storage, insurance, and logistics. The writer must source the asset or manage a short position against delivery. For large institutional trades, physical delivery was once unavoidable—it anchored option prices to the real spot market and prevented indefinite divergence. Yet for small retail traders and for index-based derivatives where the "underlying" is abstract, physical delivery becomes a liability.

Equity options in the United States are still technically eligible for [physical delivery](/common-stock/), though most institutional traders close positions or roll them forward before expiration to avoid the operational burden. Individual equity options held to expiration can still physically settle, but exchanges and brokers have increasingly favored cash settlement or early exercise.

## Why cash settlement emerged

Cash settlement solves the logistics problem. Instead of transferring the asset, the holder and writer settle by paying the difference between the strike price and the spot price at expiration. A call option struck at 150 on an index trading at 160 results in the writer paying the holder \$10 per contract unit (often \$100 cash, since equity index options represent 100 units of the index).

For index options—which underlie the majority of option volume globally—physical settlement is impossible. There is no way to deliver "the S&P 500." Thus, [index options](/sp-500-index/) are always cash-settled. The same applies to options on interest rates, foreign exchange, and broad commodity indices.

Cash settlement also reduces margin requirements. A broker lending to a client can trust a cash obligation better than the logistics of holding and transferring shares. It flattens the playing field for retail traders, who would otherwise face prohibitive costs to take or give physical delivery.

## Market structure and settlement standards

The settlement method varies by market and asset class.

**Equity options** trade on exchanges like the NASDAQ and NYSE. In the U.S., equity options are permitted to settle physically, but the industry standard has drifted toward cash settlement or closure before expiration. Individual stock options can still be assigned and physically settled if held through expiration, but most institutional volume closes out or rolls forward.

**Index options**, including options on the [S&P 500](/sp-500-index/), NASDAQ-100, and VIX, are cash-settled exclusively. There is no other practical choice.

**Futures and futures options**, which trade on exchanges like the CME, split between physical and cash settlement depending on the underlying. Energy futures (crude oil, natural gas) typically settle physically, giving producers and refiners a way to lock in prices for actual supply and demand. Agricultural futures (corn, soybeans) also allow physical delivery. But equity index futures are cash-settled, as are interest rate futures.

**Equity options on foreign exchanges** vary: some European and Asian exchanges use cash settlement widely; others preserve physical settlement traditions.

**Over-the-counter options** negotiated between a bank and a client can be either, depending on the deal structure.

## Implications for the option holder

The holder must understand which settlement applies, because it affects strategy and risk.

**With physical settlement**, the holder who exercises deep-in-the-money calls must be prepared to either take delivery or immediately sell the stock, paying transaction costs. If an investor holds a call on 1,000 shares of a company and exercises, they now own 100,000 shares and must manage that position. For some strategies—such as covered calls or protective puts—this is the intended outcome. For others, it is a trap.

**With cash settlement**, the holder avoids logistics but loses the option to own the asset. If an investor wanted to accumulate shares using options, a cash-settled structure defeats that purpose. An index call option cannot be used to "own the index"; it exists only as a hedge or a directional bet. 

The holder also bears counterparty risk differently. A physically settled equity option ultimately rests on the exchange's clearing house; the exchange guarantees delivery of shares. A cash-settled derivative rests on the clearing house's ability to collect and deliver cash, which is lower-friction but still carries systemic risk in a financial crisis.

## Pricing and arbitrage considerations

The settlement method affects pricing, particularly in stressed markets. In normal conditions, a cash-settled index option should price the same as if it were physically settled—because arbitrageurs would exploit any gap. But when markets seize up, liquidity dries up, and the link can break.

A notable example: in March 2020, equity index futures and options pricing diverged significantly from spot prices as margin requirements spiked and cash hoarding intensified. Cash-settled derivatives, which require no physical transfer, became cheaper relative to physically settled positions, because the cash settlement avoided liquidity bottlenecks.

Covered arbitrage—buying the [call](/call-option/), selling the [put](/put-option/), and shorting the stock—exposes the difference between strike, spot, and rates through [put-call parity](/put-call-parity-explained/). When a contract is cash-settled, this arbitrage becomes tighter and more reliable, because there is no delivery friction.

## Settlement procedures and ex-expiration

Equity options typically expire on the third Friday of the month. At close of business, the exchange's clearing house marks all in-the-money options for assignment or exercise.

For **physically settled equity options**, the clearing house randomly assigns out-of-the-money puts and calls to counterparties, who must then deliver or accept shares on the settlement date (typically T+1 or T+2). For **cash-settled index options**, the clearing house simply credits or debits the holder's account on the next business day.

An option holder who wants to avoid any settlement hassle can simply close the position by selling the option before expiration—a choice that applies equally to physical and cash-settled contracts.

## Practical considerations for traders

For retail traders, the distinction rarely matters, because most brokers close out or cash-settle positions automatically before expiration. But for institutional traders with large positions or multi-leg strategies, settlement method shapes everything from margin requirements to hedging efficiency.

If you are using options for income—such as writing covered calls—you need to know whether you will receive cash or shares. A covered call writer on a physically settled option will have shares called away if the call expires in the money. A cash-settled call writer receives cash payment instead.

For directional bets on indices or broad markets, cash settlement is the only option and its mechanics are transparent. For single-stock strategies or speculative positions, understanding whether settlement is physical or cash can help avoid unplanned asset transfers and cost surprises.

## See also

<div class="wiki-seealso">

### Closely related

- [Call option](/call-option/) — one of the two basic option types
- [Put option](/put-option/) — the opposite side of the risk
- [Put-call parity explained](/put-call-parity-explained/) — the no-arbitrage relationship linking both
- [Futures contract](/futures-contract/) — related forward-looking derivatives with their own settlement styles
- [Derivatives hedging](/derivatives-hedging/) — practical use of options to manage risk
- [Exercise price](/exercise-price/) — the strike at which settlement occurs
- [Expiration date](/expiration-date/) — when settlement is triggered

### Wider context

- [Option](/option/) — the umbrella concept
- [Over-the-counter market](/over-the-counter-market/) — where non-standard settlement terms are negotiated
- [Stock exchange](/stock-exchange/) — regulated venue setting settlement standards
- [Clearing house](/federal-deposit-insurance-corporation/) — institution guaranteeing settlement

</div>
