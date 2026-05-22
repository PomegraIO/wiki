---
title: "Quanto Derivative"
description: "Cross-currency derivative that locks in a fixed exchange rate for converting payoffs from one currency to another."
keywords:
  - cross-currency
  - quanto swap
  - currency fixing
  - exchange rate hedge
---

*A **quanto derivative** is a cross-currency instrument in which the payoff is denominated in one currency but tied to an underlying asset priced in another, with the exchange rate fixed at inception.*

Investors often need to hedge or gain exposure to foreign assets without taking currency risk. A standard solution would be to buy the foreign asset and sell a forward in that currency. But a quanto takes a different path: instead of two separate legs, it packages both into a single hybrid security. The exchange rate is locked in at contract launch — no matter where the currency trades later, the conversion happens at that fixed rate.

<aside class="wiki-infobox">

| Aspect | Detail |
|--------|--------|
| **Fixed rate** | Locked at initiation; never changes |
| **Payoff** | Denominated in domestic currency |
| **Underlying** | Foreign asset (equity, index, rate) |
| **Primary use** | Eliminate currency noise from foreign exposure |
| **Risk remaining** | Only the underlying asset risk |
| **Cost** | Embedded in the strike or premium |

</aside>

## Why a fixed rate costs money

When you buy a quanto, the dealer knows they must deliver foreign currency exposure without you bearing currency risk. They hedge by selling forward currency at that fixed rate. If interest rates differ between the two currencies, the forward will trade at a premium or discount. That cost is baked into the quanto's price — you pay it whether you realize it or not. 

In most currency pairs, the [interest-rate-parity](/wiki/interest-rate-parity/) relationship ensures the forward is at a predictable level. If the foreign interest rate is higher, the forward trades weaker (fewer units of foreign currency per home currency), but the quanto absorbs that differential, and you pay less upfront than you would for a plain foreign exposure plus a hedge.

## Common structures: equities and indices

A quanto on a foreign stock index is the most frequent use. Say an American investor wants exposure to the Nikkei 225 without yen risk. A Nikkei quanto fixes the yen–dollar rate at, say, 150. If the Nikkei rises 10% and the yen weakens to 160, the investor still gets paid as if the rate is 150. The yen's weakness is invisible to them. Conversely, if the yen strengthens to 140, they still get 150 — the yen strength does not amplify their gains.

[Equity-linked](/wiki/equity-linkage/) quantos work the same way: the payout is tied to a foreign stock, but the conversion happens at the fixed rate. Banks and asset managers use these to offer domestic investors a clean bet on foreign company performance.

## Interest rate quantos: hedging floating-rate exposure

A floating-rate note issued by a foreign borrower might carry [LIBOR](/wiki/libor/) or [SOFR](/wiki/sofr/) plus a spread. For a foreign lender, the interest rate risk and the currency risk are intertwined. A quanto wrapper lets them hedge the currency while keeping the rate risk, or vice versa. The dealer locks in the exchange rate, and the floating rate still floats in its home currency — the lender receives the full economic exposure to rate moves, just in their own currency.

## Pricing and the volatility smile

Because the quanto fixes two things at once — the underlying level and the currency rate — its value depends not only on each alone, but on how they move together. If the foreign asset rises when the currency is weak, and falls when strong, that negative [correlation](/wiki/correlation-coefficient/) is valuable to the quanto holder. Dealers price that in via a correlation adjustment.

More subtly, the [volatility smile](/wiki/volatility-smile/) for quanto equity options is steeper than for plain equity options, because currency moves introduce a second source of tail risk. Deep out-of-the-money quantos are relatively expensive.

## Contrast with a standard cross-currency swap

A [cross-currency-swap](/wiki/cross-currency-swap/) also involves two currencies, but neither is fixed. Both legs float; the parties exchange notional in both currencies at prevailing rates, and both streams are exposed to currency moves. A quanto is one-sided: the domestic investor is insulated from currency, while the dealer (who hedges with a forward) bears it.

## Where quantos appear in practice

The most liquid quantos are equity index contracts. American, European, and Japanese funds all offer quanto versions of foreign indices to retail clients. In institutional markets, quantos appear embedded in structured notes: a note might promise "[dividend-adjusted](/wiki/dividend-adjustment/) Nikkei returns in dollars, with the yen-dollar rate locked at 150." Insurance companies and pension funds use quanto swaps to manage foreign bond holdings without currency hedges.

For traders, quanto [options](/wiki/option/) offer a way to take directional bets on foreign equities while eliminating carry costs and day-to-day currency noise. A speculator convinced that German auto stocks will outperform might buy a DAX call quanto rather than a standard call plus a euro forward.

## Risks and limits

The payoff is capped at the fixed rate. If the foreign currency strengthens dramatically, the quanto holder does not participate in that upside. For an investor betting on both currency strength *and* asset appreciation, a quanto is a poor choice — they would use [currency-hedging](/wiki/currency-hedging/) instead.

Quantos also embed [basis-risk](/wiki/basis-risk/): if the underlying asset moves in a way that is perfectly [cointegrated](/wiki/cointegration-strategy/) with its currency, and that cointegration breaks, the fixed rate no longer feels fair. This is rare but can matter in emerging markets where capital flows tie the currency and the stock market.

<div class="wiki-seealso">

### Closely related
- [Cross-currency swap](/wiki/cross-currency-swap/) — Both currencies float, full bilateral exposure
- [Equity-linkage](/wiki/equity-linkage/) — Payoff tied to a foreign equity; quanto is one form
- [Currency hedging](/wiki/currency-hedging/) — Ways to isolate currency risk
- [Interest-rate-parity](/wiki/interest-rate-parity/) — Why forward rates differ, a key input to quanto pricing

### Wider context
- [Derivative](/wiki/derivatives-exchange-crypto/) — Exchange-traded and OTC derivatives broadly
- [Option](/wiki/option/) — Plain vanilla options, whose quanto variant adds FX fixing
- [Basis risk](/wiki/basis-risk/) — Risk that the hedge does not perfectly offset the exposure

</div>
