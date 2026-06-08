---
title: "ADR Arbitrage"
description: "The practice of exploiting price discrepancies between an ADR and its underlying ordinary shares by simultaneously trading both to lock in a riskless profit."
keywords:
  - adr
  - arbitrage
  - price differential
  - statistical arbitrage
  - market efficiency
image: "/svg/equity.svg"
---

*[ADR](/adr/) arbitrage** is the simultaneous trading of an American Depositary Receipt and its underlying [ordinary shares](/common-stock/) to exploit price gaps between the two markets. When the ADR trades at a premium or discount to its fair value—calculated from the ordinary share price, the [exchange rate](/currency-risk/), and the [depositary ratio](/depositary-ratio/)—arbitrageurs buy the cheaper form and sell the expensive one, pocketing the spread.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ADR Arbitrage — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for equity and shareholder matters." />

<div class="wiki-infobox-caption">Profiting from temporary pricing misalignments across markets.</div>

|   |   |
|---|---|
| **What it is** | Simultaneous buy-sell across ADR and ordinary share markets to capture price gaps |
| **Typical spread** | 0.5%–3% per trade (net of transaction costs) |
| **Arbitrageurs** | Algorithmic traders, hedge funds, principal traders, market makers |
| **Trade direction** | "Long the cheap, short the expensive" — buy the market offering better value |
| **Settlement risk** | Currency exposure and timing mismatches during execution and settlement |
| **Transaction costs** | Trading fees, bid-ask spreads, currency conversion, custody transfers |
| **[Depositary ratio](/depositary-ratio/)** | Critical for pricing equivalence; ratio mismatch enables arbitrage |
| **Time horizon** | Hours to days; faster execution = lower execution risk |

</aside>

## How the arbitrage works

An ADR's fair value should equal the ordinary share price (converted to dollars at the current [exchange rate](/currency-risk/)) multiplied by the [depositary ratio](/depositary-ratio/). If an ordinary share trades for £8 and the GBP/USD rate is 1.25, the dollar equivalent is £8 × 1.25 = $10. If the ADR is a 1:1 receipt (one ADR = one share), the ADR should trade near $10. If the ADR instead trades at $9.80, it is cheap. If it trades at $10.30, it is expensive.

An arbitrageur spotting a $0.20 gap on a $10 ADR ($9.80 actual vs. $10 fair value) executes a "cash-and-carry" trade:

1. **Buy the ADR at $9.80** (U.S. market).
2. **Short the ordinary shares at £8** (London market).
3. **Hold to the future trade settlement date.**
4. **[Cancel](/adr-cancellation/) the ADR** to receive one ordinary share (per the 1:1 ratio).
5. **Deliver that share to close the short position.**
6. **Realize the $0.20 spread, net of costs.**

Conversely, if the ADR is expensive at $10.30, the arbitrageur reverses the trade: buys ordinary shares, sells the ADR, and later [creates](/adr/) new ADRs to replace the sold ADRs.

## Why gaps exist

Arbitrage opportunities exist because markets are not perfectly synchronized. The ordinary shares and ADR trade on different exchanges, at different times of day (if the home country is in a different time zone), with different [bid-ask spreads](/bid-ask-spread/), and in different liquidity conditions. The [exchange rate](/currency-risk/) itself fluctuates continuously.

A sudden currency move is a classic catalyst. If the pound weakens from 1.25 to 1.24 while the ordinary share price holds at £8, the fair ADR value drops from $10 to $9.92. If the ADR price lags and still trades at $10, a gap opens instantly. An arbitrageur can capture it before the market corrects.

Differences in market maker participation also matter. The U.S. ADR market may have dozens of [market makers](/market-maker-trading/); the home market may have fewer or less active ones. A block trade in one market can temporarily move the price without an immediate reaction in the other.

## Costs and practical constraints

ADR arbitrage looks simple in theory but is expensive in practice. Executing an arbitrage involves:

- **Bid-ask spreads** on both the ADR and the ordinary shares, plus spreads on any currency forwards or spot trades to hedge [currency risk](/currency-risk/).
- **Broker commissions** and post-trade fees in both markets.
- **Currency conversion costs**, including the spread on converting pounds to dollars or vice versa.
- **Custody fees** if shares must be held in a local custodian while awaiting [cancellation](/adr-cancellation/) or creation.
- **Settlement timing mismatches**—the U.S. and home markets may settle on different dates, forcing the arbitrageur to finance a short position or an unsettled purchase for extra days, which costs money.

A 0.5% spread sounds profitable on a $10 ADR ($50 profit per 1,000 shares), but add 0.3% in bid-ask slippage, 0.1% in commissions, and 0.05% in custody costs, and the profit margin shrinks to 0.05%. On a large position, that still adds up, but on a small trade it is barely worth the operational effort.

## Who arbitrages ADRs

**Algorithmic traders and hedge funds** dominate ADR arbitrage because they can execute trades at machine speed across multiple markets and currencies. They have the technology, the capital, and the infrastructure to absorb the transaction costs and manage settlement risk across borders.

**Principal traders** (firms that trade their own capital) often arbitrage ADRs opportunistically. Some specialize in "stat arb" (statistical arbitrage), using historical patterns and pricing models to spot temporary mispricings.

**Market makers** sometimes arbitrage as part of their regular inventory management. If an ADR and ordinary shares become too far apart, a market maker holding both can lock in a riskless profit while tightening spreads.

**Retail investors** rarely arbitrage ADRs because the transaction costs and complexity overwhelm small position sizes. A retail investor would need to coordinate trades across two continents, manage currency hedging, arrange custody in a foreign country, and handle currency conversion—all of which costs money and time.

## Impact on market efficiency

ADR arbitrage is a powerful force for [price discovery](/price-discovery/). By continuously exploiting gaps, arbitrageurs force the ADR and ordinary share prices toward equivalence. If the ADR drifts expensive, arbitrageurs sell it and buy the ordinary shares, pushing the ADR price down and the ordinary price up until the gap closes. This is efficient: it ensures investors cannot exploit an obvious profit opportunity indefinitely.

On the flip side, very tight arbitrage margins can be a sign that the market is highly efficient—so many arbitrageurs chase the gaps that they disappear in milliseconds. Larger gaps suggest friction (high costs, illiquidity, or time zone constraints) that make arbitrage harder.

## Currency hedging and basis risk

Because the ADR and ordinary shares are denominated in different currencies, an arbitrageur typically hedges [currency risk](/currency-risk/) using a [forward contract](/forward-contract/) or currency futures. Instead of betting on the exchange rate, the arbitrageur locks in an exchange rate at trade initiation, ensuring that the profit (or loss) comes purely from the price gap, not from currency moves.

However, hedging is not free. The [forward](/forward-contract/) rate incorporates [interest-rate differentials](/interest-rate/) between the two countries. If sterling interest rates are higher than U.S. rates, the forward pound is cheaper than the spot rate, eroding the arbitrage profit. This "carry cost" is one more friction that forces arbitrage spreads to widen.

## Systemic role in ADR programs

Arbitrageurs are essential to the health of ADR markets. Without them, ADRs could trade at wild premiums or discounts. With arbitrageurs active, the ADR stays tethered to economic reality. For [sponsored ADR](/adr/) issuers (typically large, well-known companies), arbitrage is constant and tight. For obscure [unsponsored](/adr/) ADRs, arbitrage may be rare, and wider spreads are the result.

## See also

<div class="wiki-seealso">

### Closely related

- [ADR](/adr/) — the fundamental structure of American Depositary Receipts
- [Depositary Ratio](/depositary-ratio/) — how the conversion ratio is set and determines pricing equivalence
- [ADR Cancellation](/adr-cancellation/) — the process of converting ADRs back to ordinary shares, used to close arbitrage trades
- [Exchange Rate](/currency-risk/) — currency fluctuations that create arbitrage opportunities
- [Bid-Ask Spread](/bid-ask-spread/) — transaction costs that constrain arbitrage profits

### Wider context

- [Price Discovery](/price-discovery/) — how arbitrage improves market efficiency and pricing
- [Forward Contract](/forward-contract/) — hedging currency risk in international arbitrage trades
- [Interest Rate](/interest-rate/) — how rate differentials affect forward pricing and arbitrage carry costs
- [Market Maker Trading](/market-maker-trading/) — how dealers manage inventory across markets
- [Liquidity Risk](/liquidity-risk/) — how illiquidity in home markets constrains arbitrage activity
- [Currency Volatility](/currency-volatility/) — unexpected FX moves that can disrupt arbitrage trades

</div>
