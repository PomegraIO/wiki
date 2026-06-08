---
title: "Synthetic FX Forward Using Options"
description: "How buying a call and selling a put at the same strike creates a synthetic FX forward, replicating forward contract economics using options."
keywords:
  - synthetic fx forward using options
  - fx options replication
  - call put parity
  - currency forward equivalence
  - options arbitrage
  - fx derivatives
---

*A **synthetic FX forward using options** is constructed by simultaneously buying a currency call option and selling a currency put option at the same strike price and expiration date. This two-legged option position replicates the payoff and economic effect of an outright forward contract, locking in a future exchange rate without using a bilateral forward agreement.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Synthetic FX Forward — Key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for FX derivatives." />

<div class="wiki-infobox-caption">Options-based replication of forward contract obligations and economics.</div>

|   |   |
|---|---|
| **What it is** | Buy call + sell put at same strike = synthetic long forward |
| **Strike selection** | Usually set to the ATM forward rate or desired rate lock |
| **Expiration** | Matches the hedging or speculation horizon |
| **Payoff profile** | Linear, identical to a forward contract at expiration |
| **Key advantage** | Flexibility; can be unwound or adjusted via secondary market |
| **Key drawback** | Requires two separate transactions; higher costs upfront |
| **Who uses it** | Traders, hedgers lacking clearing access, or exploiting bid-ask spreads |

</aside>

## How the structure replicates a forward

When you buy a call on a currency pair and sell a put at the same [strike price](/strike-price/) and expiration, you lock in the right to buy at that strike and the obligation to buy if the put is exercised. The result: at expiration, you must deliver cash and receive the foreign currency at the pre-agreed strike rate—exactly as a forward contract would function.

To see this concretely, suppose EUR/USD is trading at 1.10 spot and you want to lock in a rate for a payment due in three months. Instead of entering a forward at the market forward rate of 1.1050, you might:

- **Buy** a EUR call at strike 1.10 (the right to buy EUR at 1.10)
- **Sell** a EUR put at strike 1.10 (the obligation to buy EUR at 1.10 if the buyer exercises)

At expiration, if EUR/USD is above 1.10, your call is in the money and you exercise it, buying EUR at 1.10. If EUR/USD is below 1.10, the put buyer exercises, forcing you to buy EUR at 1.10. Either way, you receive EUR at 1.10—the strike you chose. No intermediate optionality remains; the payoff is linear across all final spot rates.

This economic equivalence is a corollary of [call-put parity](/option/), the fundamental relationship governing option pricing across all markets.

## When traders use this structure instead of a plain forward

**No clearing relationship.** In FX, not all participants have direct access to interbank forward markets. A corporate treasurer or small bank might use options on an exchange or OTC through a broker where they have an options trading relationship but lack a forward agreement framework. The synthetic forward becomes the practical substitution.

**Bid-ask arbitrage.** Market-makers sometimes notice that the call and put are priced at levels that, when combined, offer a forward rate cheaper than the spot forward market. A trader buys the underpriced call, sells the overpriced put, and effectively locks in a favorable all-in rate compared to a direct forward quote.

**Unwinding optionality.** Unlike a forward—which is bilaterally binding and usually closed only by entering an offsetting reverse forward—a synthetic forward can be unwound by separately selling the call and buying back the put in the secondary options market. This flexibility appeals to traders who may change their hedge horizon or want to lock in interim gains.

**Regulatory or capital treatment.** Different jurisdictions or internal risk frameworks may classify options and forwards differently for capital or collateral purposes. Some participants prefer the option structure for accounting or regulatory reasons.

**Leveraged or speculative entry.** A speculator betting on currency direction might construct a synthetic forward because the options market offers better liquidity in certain pairs than the forward market, or because options provide a defined risk entry point (unlike a cash forward, which has unlimited loss exposure once entered).

## Cost structure and upfront premium

A plain forward contract typically carries no upfront cash payment; cost accrues only as mark-to-market changes in value. A synthetic forward, by contrast, requires two option trades, each with a bid-ask spread and brokerage commission.

When you buy the call, you pay its premium; when you sell the put, you collect its premium. The net cost is the difference. If both options are at the same strike and expiration, and if that strike is near the [at-the-money forward](/strike-price/) rate, the call and put premiums should be close to offsetting. In a perfectly frictionless market with no [skew](/volatility-smile/), they would cancel exactly.

In practice, bid-ask spreads and credit quality differences between the buyer and seller of the put mean the net cost is usually slightly positive—you pay a small all-in premium to establish the synthetic forward. This is your cost of optionality (the ability to exit or adjust early). A direct forward, locked for the full horizon, would typically be cheaper if you intend to hold to maturity.

## The no-arbitrage relationship

If the call premium minus the put premium exceeds or falls short of the price of a direct forward at the same strike and expiration, an arbitrage exists. A bank or trader can:

- **If synthetic is cheap:** Buy the synthetic (buy call, sell put) and sell the forward at the current forward rate, pocketing the spread cost-free at maturity.
- **If synthetic is expensive:** Sell the synthetic and buy the forward, again locking in a riskless profit.

In liquid FX markets, these arbitrages are competed away instantly. The synthetic forward rate and the listed forward rate remain in lockstep. This parity ensures that neither structure is systematically advantageous in a frictionless, competitive market.

## Practical considerations and limitations

**Counterparty credit.** A forward is a single bilateral agreement with one counterparty. A synthetic forward splits the credit exposure: you are long the call (receiver risk if the counterparty fails), short the put (obligor risk if you must deliver on a failed counterparty). Managing two credit relationships can be operationally messier.

**Liquidity mismatch.** Forward and option liquidity are not always synchronized. In exotic currency pairs, options may be less liquid than forwards, forcing you to accept wider spreads or smaller sizes when synthetically constructing a forward.

**Early unwind slippage.** If you want to exit the synthetic forward before expiration—say, the client cancels the underlying FX need—you must sell both the call and buy back the put. If the market has moved sharply, the bid-ask spreads on both legs may be much wider, and you could realize a loss even though a direct forward would have a loss too. The flexibility cuts both ways.

**Margin and collateral.** Options positions often attract more collateral calls than forwards under standard agreements. Depending on your counterparty's CSA, a synthetic forward might require more daily margin posting than a plain forward.

## See also

<div class="wiki-seealso">

### Closely related

- [Call Option](/call-option/) — the long call leg of the synthetic forward
- [Put Option](/put-option/) — the short put leg
- [Strike Price](/strike-price/) — the rate at which both legs are struck
- [Forward Contract](/forward-contract/) — the direct instrument being replicated
- [Volatility Smile](/volatility-smile/) — pricing asymmetries that affect call-put premiums
- [Option Premium](/option-premium/) — the upfront cost of the structure
- [Currency Volatility](/currency-volatility/) — drives option premium and hedge costs
- [Counterparty Risk](/counterparty-risk/) — dual exposure in a synthetic structure

### Wider context

- [Currency Risk](/currency-risk/) — the underlying exposure being hedged
- [Derivatives Hedging](/derivatives-hedging/) — common applications of synthetic forwards
- [Bid-Ask Spread](/bid-ask-spread/) — determines execution cost of each leg
- [Interest Rate Parity](/interest-rate-parity/) — economic foundation for forward pricing

</div>
