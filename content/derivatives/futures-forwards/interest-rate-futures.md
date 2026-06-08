---
title: "Interest Rate Futures"
description: "Exchange-traded derivatives on short-term interest rates or bond prices, used to hedge borrowing costs and interest-rate risk."
keywords:
  - interest rate futures
  - rate hedging
  - bond futures
  - Eurodollar futures
  - treasury futures
  - price discovery
  - interest rate risk
image: "/svg/derivatives.svg"
---

*An **interest rate future** is an [exchange-traded](/stock-exchange/) [derivative contract](/futures-contract/) whose value is tied to an [interest rate](/interest-rate/) (such as [LIBOR](/libor/) or [SOFR](/sofr/)) or to the price of a debt instrument (a treasury bond or corporate bond). Unlike a [forward rate agreement](/forward-rate-agreement/), which is bespoke and settled over-the-counter, interest rate futures are standardised, trade on exchanges like the Chicago Mercantile Exchange (CME), settle daily via [mark-to-market](/mark-to-market/), and allow large institutions and traders to hedge [interest rate risk](/interest-rate-risk/), lock in funding costs, or speculate on where rates will move.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Rate Futures — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Standardised, liquid, exchange-traded bets on where short-term rates will go.</div>

|   |   |
|---|---|
| **What it is** | A futures contract on an [interest rate](/interest-rate/) or bond price, traded on an exchange |
| **Common types** | Short-term rate futures (e.g., Eurodollar), treasury bond futures (US, UK, Germany) |
| **Exchange** | Chicago Mercantile Exchange (CME), ICE, Eurex, and other global exchanges |
| **Settlement** | Daily [mark-to-market](/mark-to-market/) with variation margin; most contracts settle cash, not by delivery |
| **Typical notional** | $1 million (Eurodollar), $100,000–$200,000 (treasury bonds) |
| **Liquidity** | High for major US and German government bonds; lower for corporate rate futures |
| **Purpose** | Hedging [interest rate risk](/interest-rate-risk/), managing debt costs, price discovery, speculation |
| **Multiplier** | Each basis point (0.01%) move produces a standardised dollar gain or loss |

</aside>

## The two main types

**Short-term rate futures** reference overnight index swap rates, [SOFR](/sofr/), or (historically) [LIBOR](/libor/). The classic example is Eurodollar futures (the CME contract on three-month US dollar [LIBOR](/libor/), though the contract has been transitioning to [SOFR](/sofr/)). A Eurodollar future that expires in three months with a notional of $1 million will pay or receive cash based on the actual three-month [LIBOR](/libor/) fix on the settlement date, compared to the price implied by the contract. Each basis point move is worth $25 (1% × $1 million ÷ 100 ÷ 4 quarters).

**Bond (or treasury) futures** reference the price of actual government debt. The CME and other exchanges list contracts on US Treasury bonds (the 30-year "bond contract"), 10-year notes, and five-year notes. The CME also lists contracts on German government bonds (Bunds), UK Gilts, and Japanese Government Bonds (JGBs). These contracts are deliverable: at maturity, the seller can choose from a basket of eligible bonds to deliver, allowing for some price flexibility. Most contracts, however, are closed out before maturity rather than delivered.

## Why exchanges, not over-the-counter?

[Exchange-traded futures](/futures-contract/) offer standardisation and liquidity that [over-the-counter](/over-the-counter-market/) contracts like [forward rate agreements](/forward-rate-agreement/) do not. The CME publishes contract specifications (maturity, notional amount, settlement method) that never change, allowing buyers and sellers to trade anonymously without needing to assess [counterparty risk](/counterparty-risk/). An investor can buy 100 two-year Eurodollar futures in seconds; finding a bank willing to quote a bespoke FRA for the exact same amount takes longer and may carry a wider [bid-ask spread](/bid-ask-spread/).

Exchange trading also means daily settlement and margin requirements. A trader who is short rate futures (betting rates will fall and bond prices will rise) must post margin and will suffer daily losses, settled in cash, if rates rise. This daily cash flow can be onerous for large positions but also ensures that neither party bears the full [counterparty risk](/counterparty-risk/) of a large adverse move—the exchange and clearing house are in the middle.

## Short-rate futures and borrowing costs

A bank or large corporation planning to issue short-term debt in the future can hedge its funding cost by selling short-rate futures. If a company knows it will borrow $100 million at [SOFR](/sofr/) plus a spread in three months' time, and it wants to lock in the [SOFR](/sofr/) component, it can sell 100 three-month [SOFR](/sofr/) futures. If [SOFR](/sofr/) rises by 50 basis points before the borrowing date, the company loses on the futures trade—but it saves that loss because the actual borrowing cost has also risen, so it breaks even on the hedge.

These short-term rate futures are also heavily used for [carry trade](/carry-trade/) strategies, where traders borrow short-term and invest long-term, hoping to profit from the steepness of the [yield curve](/yield-curve/). A trader might short Eurodollar futures expiring in one year and simultaneously buy five-year bond futures, betting that the curve will steepen (short-term rates will fall or stay stable while long-term rates rise).

## Bond futures and [interest rate risk](/interest-rate-risk/)

Bond futures, such as the 10-year US Treasury note futures contract, move inversely to [interest rates](/interest-rate/). If rates fall, bond prices rise (because existing bonds with higher coupons become more valuable), and the futures contract gains. If rates rise, bond prices fall, and the futures contract loses.

A financial institution holding a large portfolio of long-term bonds faces [interest rate risk](/interest-rate-risk/): if rates rise sharply, the value of the portfolio falls. Rather than sell the bonds (which might be core investments), the institution can sell bond futures to hedge some of that risk. The notional amount of futures sold should roughly match the [duration](/duration/) of the bond portfolio to create an effective hedge.

Bond futures are also used for [basis](/basis/) trading, where traders simultaneously buy or sell the actual bond and take the opposite position in futures, arbitraging small price differences between the cash market and futures market.

## Price discovery and market expectations

One crucial role of interest rate futures is price discovery. Because the contracts are liquid and transparent, the prices at which they trade reveal the market's collective expectation of future interest rates. If the September Eurodollar futures contract is trading at a price implying a three-month rate of 5.50%, market participants are betting that [SOFR](/sofr/) will average 5.50% in September. Policymakers at the central bank, investors, and corporate treasurers all use futures prices as real-time reads of rate expectations, making it easier to gauge how the market perceives [monetary policy](/monetary-policy/) risks.

## Daily settlement and variation margin

Unlike a [forward rate agreement](/forward-rate-agreement/), which settles once at maturity, a futures contract is marked to market every day. The clearing house computes the daily profit or loss and transfers cash between the long and short positions. This means a trader in a large long position that moves against them must continuously post margin (collateral) or close the position to avoid forced liquidation. For large hedges, this daily variation margin can create significant cash-flow timing mismatches—a hedger might be "right" in the long run but forced to withdraw cash or liquidate mid-course because short-term losses on the futures exceed available margin.

## From LIBOR to SOFR: contract evolution

For decades, interest rate futures were based on [LIBOR](/libor/), particularly three-month [LIBOR](/libor/) in Eurodollar contracts. As [LIBOR](/libor/) was phased out globally, exchanges and the CME introduced parallel contracts on [SOFR](/sofr/) and other [risk-free rates](/risk-free-rate/). The CME's three-month [SOFR](/sofr/) futures contracts are becoming the new standard, though the transition has created some fragmentation in trading activity and basis relationships between old and new contracts.

## Speculation and the leverage advantage

Because futures require only a small margin upfront (often 2–5% of the notional value), they provide substantial leverage. A trader betting that rates will fall can control $1 million of interest rate exposure with $50,000 of capital. This leverage amplifies both gains and losses and is one reason that futures markets are preferred by speculators and proprietary trading desks. A company hedging an actual interest rate exposure, however, views the futures contract purely as a risk-management tool.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward rate agreement](/forward-rate-agreement/) — the over-the-counter equivalent
- [Futures contract](/futures-contract/) — the standardised, exchange-traded structure
- [Interest rate risk](/interest-rate-risk/) — what these contracts hedge
- [SOFR](/sofr/) — the modern reference rate for short-term futures
- [LIBOR](/libor/) — the historical reference rate
- [Bond](/bond/) — the underlying for bond futures
- [Treasury bond](/treasury-bond/) — often the deliverable instrument
- [Yield curve](/yield-curve/) — a key driver of relative futures prices

### Wider context

- [Central bank](/central-bank/) — whose [monetary policy](/monetary-policy/) drives rate expectations
- [Mark-to-market](/mark-to-market/) — the daily settlement method
- [Counterparty risk](/counterparty-risk/) — eliminated by exchange clearing
- [Hedge fund](/hedge-fund/) — a major trader of rate futures
- Arbitrage — between futures and cash bond markets
- Leverage — a key feature of futures trading
- [Variation margin](/variation-margin/) — the daily cash adjustment

</div>
