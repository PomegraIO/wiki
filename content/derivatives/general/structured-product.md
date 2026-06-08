---
title: "Structured Product"
description: "A security combining a bond with embedded derivatives, engineered to deliver custom risk-return payoffs linked to underlying assets."
keywords:
  - structured note
  - structured bond
  - hybrid security
  - equity-linked bond
image: "/svg/derivatives.svg"
---

*A **structured product** is a pre-packaged security in which a bank combines a [bond](/bond/) with one or more [embedded derivatives](/embedded-derivative/) to create a custom payoff linked to equities, currencies, commodities, or other assets. The investor buys a single instrument but gains exposure to a bespoke formula, while the issuer transfers risk via derivatives.*

## The bond-plus-derivative formula

The simplest structured product is a bond with an attached option. A bank might issue a note maturing in three years: investors receive a guaranteed coupon of 2% per year, plus an upside linked to the [S&P 500](/sp-500-index/). The coupon component is the bond; the index-linked kicker is a [call option](/call-option/) the bank has issued to the investor.

The bank finances the option by issuing the bond at a discount or by borrowing at a rate that covers both the guaranteed coupon and the option's cost. From the investor's perspective, they own a single security: one trading code, one settlement, one issuer. From an accounting and risk standpoint, the security bifurcates into a host bond and an [embedded derivative](/embedded-derivative/).

This structure allows banks to engineer bespoke payoffs. An investor might want equity upside but a floor beneath their principal. A structured product can deliver: principal protected, plus 80% participation in index gains. The math: a zero-coupon bond priced to mature at face value, plus a leveraged call option (80% delta, say) financed by the bond's yield. The issuer hedges the call via [futures](/futures-contract/) or [swaps](/interest-rate/), locking in its margin.

## Why corporates and investors use them

Structured products appeal to retail and institutional investors seeking custom risk-return profiles that vanilla [bonds](/bond/) and [equities](/stock/) don't offer. An insurance company might buy a reverse-floater note: a bond paying a coupon that falls as [interest rates](/interest-rate/) rise, offsetting the decline in value of their longer-duration assets. An exporter worried about [currency](/currency-risk/) strength might buy a note whose return depends on a currency pair, hedging operational risk in a single instrument.

Issuers (usually [investment banks](/jpmorgan-chase/)) profit from the bid-ask spread on the derivatives they embed and from the credit spread on the bond itself. The issuer is long the embedded derivative (it receives the [option premium](/option-premium/) from the investor indirectly), then hedges that long derivative exposure in the market. The spread between the hedge cost and the embedded option's notional cost is the bank's profit.

Structured products also bypass regulatory constraints. Some pension funds are restricted from holding derivatives directly but can hold structured notes. A bond with an embedded equity option may pass compliance review, while a direct [call option](/call-option/) might not. The wrapper is often the loophole.

## Common structures

**Equity-linked notes** are the most liquid. An investor buys a note offering principal protection and a percentage of index gains. If the index rises 40%, the note's return might be 30% (80% of gains captured). If the index falls, the investor recovers principal at maturity.

**Commodity-linked structures** tie payoffs to oil, metals, or agricultural prices. A note might offer a fixed coupon plus gains if [crude oil](/crude-oil/) prices rise above a strike level. Banks hedge these via [commodity futures](/crude-oil/) and [swaps](/interest-rate/).

**Reverse floaters** embed a [cap](/call-option/) on coupon rates. A floating-rate note normally pays LIBOR + 2%; a reverse floater might pay 8% − LIBOR, capping the coupon if [interest rates](/interest-rate/) rise. The issuer hedges via a [payer swaption](/option/) (a bet that rates won't spike).

**Auto-callable notes** include an embedded [path-dependent option](/expiration-contracts/). If an index closes above a barrier level on annual observation dates, the note redeems early at face value plus accrued coupon. If the barrier is never breached, the note runs to maturity and returns a knockout participation in index gains. The embedded feature is a [knock-in call](/call-option/).

**Worst-of / best-of notes** link to multiple assets. A worst-of structure returns the performance of whichever of three stocks or indices performed worst; a best-of returns the best. These embeds multiple [call options](/call-option/) with correlation risk: if assets move together, the payoff pools reduce.

## Accounting and bifurcation

Under [IFRS](/international-financial-reporting-standards/), a structured note must be bifurcated: the host bond is accounted for under the amortised-cost rules (if held to maturity), and the [embedded derivative](/embedded-derivative/) is marked to fair value each period. Changes in the derivative's fair value flow through the [income statement](/income-statement/) (P&L impact), even if the host bond would be accounted for at amortised cost.

This bifurcation can create accounting volatility. A reverse floater linked to interest rates will see its embedded derivative revalued sharply if rate expectations shift, even if the investor plans to hold to maturity. The issuer, holding the short derivative position, records an offsetting gain. But the investor sees mark-to-market losses on their books each quarter.

## Risks to investors

**Issuer credit risk**: A structured note is a [bond](/bond/), so investors bear the issuer's default risk. If a bank issues a highly leveraged equity-linked note and fails, investors are unsecured creditors, recovering only cents on the dollar. Unlike a traded [call option](/call-option/) on a clearinghouse, where [counterparty](/counterparty-risk/) risk is mutualized, the structured note investor faces single-issuer risk.

**Liquidity risk**: Most structured products are illiquid. An investor cannot easily sell a three-year auto-callable note in the secondary market; bid-ask spreads are wide. Early exit often requires the issuer to reprice the embedded derivative, capturing most of any interim gains.

**Model risk**: The payoff depends on how the underlying assets evolve and whether barriers are breached. Worst-of notes are exposed to [correlation](/concentration-risk/) assumptions baked into the pricing model. If correlations change, the note's value can diverge sharply from the initial pricing.

**Leverage**: Some structures embed leveraged [options](/option/), amplifying losses. A 3× leveraged note on a small-cap index can lose more than 100% of principal if the index crashes. The bond wrapper offers no real protection; it is merely an unsecured promise to repay at maturity.

## Hedging and risk transfer

The issuer's primary job is to hedge the embedded derivatives. A bank issuing an equity-linked note immediately buys [call options](/call-option/) (or enters variance swaps) to offset its short exposure. Hedging is continuous: as the underlying asset's volatility or price changes, the hedge ratio must be rebalanced. Transaction costs and [bid-ask spreads](/bid-ask-spread/) erode the issuer's margin, so issuers employ sophisticated [algorithmic trading](/algorithmic-trading/) to minimize slippage.

During market stress, hedges can fail to move in lockstep with the embedded derivative. A bank short a jump-heavy [call option](/call-option/) on a stock might own far OTM protective puts for hedging; but if the stock gaps through the option's strike, the mismatch crystallizes as a loss. This is why structured product issuers are often among the largest users of [options](/option/) and variance swaps in the market.

## Market growth and regulation

Structured products are popular in Europe and Asia, where retail investors have greater appetite for derivatives and banks offer a broader range of structures. In the US, the market is smaller, with tighter [SEC](/securities-and-exchange-commission/) disclosure rules and a cultural preference for simpler [mutual funds](/mutual-fund/) and [ETFs](/etf/).

Regulators scrutinize structured products for consumer protection. Many jurisdictions require explicit risk warnings and suitability assessments. Some ban the most exotic structures (e.g., reverse-reverse floaters) or cap leverage. The underlying principle is that the payoff formula must be understandable to the buyer; opaque structures attract regulatory crackdowns.

## See also

<div class="wiki-seealso">

### Closely related

- [Embedded Derivative](/embedded-derivative/) — the derivative component bifurcated from the bond host
- [Bond](/bond/) — the debt wrapper that funds the structure
- [Call Option](/call-option/) — the upside mechanism in many equity-linked notes
- [Option Premium](/option-premium/) — the cost of the embedded option, priced into the bond's coupon
- [Put Option](/put-option/) — often embedded to protect principal floors

### Wider context

- Derivative — the family of instruments backing the payoff formula
- [Counterparty Risk](/counterparty-risk/) — credit exposure to the issuing bank
- Variance Swap — a related derivative often used to hedge structured payoffs
- [Interest Rate Swap](/interest-rate/) — structures linking to [LIBOR](/libor/) or other rate indices
- [Algorithmic Trading](/algorithmic-trading/) — used by issuers to hedge dynamically
- [ETF](/etf/) — simpler passive alternative to structured notes for gaining custom exposures

</div>
