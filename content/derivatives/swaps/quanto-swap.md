---
title: "Quanto Swap"
description: "A derivative that swaps cash flows in one currency while referencing an index in another, hedging foreign exchange exposure."
keywords:
  - quanto swap
  - currency hedging
  - cross-currency derivatives
  - fx hedge
image: "/svg/derivatives.svg"
---

*A **quanto swap** is a derivative where cash flows are denominated and settled in one currency—typically the investor's home currency—while the underlying index or rate reference is in another. This structure eliminates foreign exchange risk entirely, allowing investors to take a pure position on an asset's performance without bearing currency volatility.*

## The dual-currency problem

Investors holding foreign assets face two sources of return: the asset itself and the currency it trades in. A stock index might rise 10% in euros, but if the euro weakens against the dollar, a US-based investor sees a smaller gain—or even a loss. Managing these two exposures separately is cumbersome. A quanto swap bundles them into a single contract.

The structure works like a standard [interest rate swap](/interest-rate-swap/): two parties exchange periodic cash flows. One leg is typically fixed; the other floats. The twist is that the floating leg references an index in a different currency, yet both legs settle in a single currency (the investor's domestic one). The dollar amount owed in each period is determined entirely by the foreign index—not by any USD/EUR exchange rate observed later.

## Mechanics and pricing

Suppose a US pension fund wants exposure to the [EURO STOXX 50](/stock-exchange/) (a eurozone equity index) without currency risk. Instead of buying the index in euros and hedging, the fund enters a quanto swap. Each quarter, it receives a payment based on how the index performed that quarter, in dollars. It pays a fixed rate on a notional amount, also in dollars.

The dealer pricing the swap must account for three variables: the foreign index volatility, the exchange rate volatility, and the correlation between them. A perfectly quanto contract fixes the [strike price](/strike-price/) in the foreign currency, then converts it to domestic currency at a predetermined rate. This conversion rate—the "quanto forward rate"—differs from the spot [exchange rate](/interest-rate/) because of the correlation adjustment.

If eurozone equities and the EUR/USD rate are positively correlated (both move up together), the quanto forward rate will be higher than a simple currency-forward rate would suggest. The dealer takes on additional risk when the index rallies at the same time the euro strengthens, amplifying the dollar-denominated payout. They compensate by widening the quoted strike or fee.

## Who uses quantos and why

Asset managers with offshore mandates use quantos to isolate performance of foreign markets from currency speculation. A Japanese pension fund betting on US tech stocks might enter a quanto swap denominated in yen, paying a floating rate and receiving a fixed return tied to the Nasdaq, all in yen.

Corporate treasurers sometimes use quantos in the opposite direction: a US multinational earning euros might lock in a floor on euro revenues by swapping euro cash flows for dollar payments at a fixed rate, regardless of the actual EUR/USD spot.

Hedge funds exploit quantos when they have a strong view on relative value between two assets across currencies. By decomposing the position into the asset return and the currency return separately—or ignoring currency altogether—the fund can compare apples to apples.

## The cost of the currency elimination

Removing currency risk is not free. Dealers price quanto contracts tighter than a straightforward [forward contract](/forward-contract/) on the foreign index plus a separate currency hedge would cost, but the compression is only modest—roughly 10–50 basis points in fees, depending on the index and currency pair. The real expense lies in the quanto forward rate adjustment: if equity and currency correlations are unfavourable to you at inception, the strike will be set wider, raising your effective entry cost.

Quantos are also less liquid than plain index forwards or spot index purchases. If you need to exit early, the bid-ask [spread](/bid-ask-spread/) is wider, and dealers require larger notional amounts to make markets. This is especially true for emerging-market quantos; a Japanese index quanto is much easier to trade than a Thai equity quanto.

## Quanto exotics and complications

A basic quanto is straightforward, but variations proliferate. A *quanto call option* gives the holder the right to enter a quanto position. A *quanto swaption* is an option on a quanto swap itself. These nested structures compound pricing complexity and can hide considerable optionality.

Implied [volatility](/implied-volatility/) in the foreign market and correlation between that volatility and the currency can shift dramatically during market stress. During the 2008 financial crisis, correlations between equity indices and currencies reversed, leaving some quanto positions badly mispriced by their dealers.

Another quirk: quanto contracts are settled in a single currency, which means [counterparty risk](/counterparty-risk/) is concentrated in that currency. If the underlying dealer fails, the investor has to recover in one currency only—a simpler legal claim, but no diversification of credit risk.

## Alternatives and when to choose quantos

If your only goal is currency hedging, buying the index and buying a [currency forward](/forward-contract/) separately might be cheaper. This approach is transparent and easier to unwind. A quanto is best when you want a completely seamless package: no rebalancing needed, no basis risk between the two legs, and a counterparty to absorb that integration work.

Quantos are also preferred when you want to express a long-dated view. Currency forwards beyond 5 years become expensive and illiquid; a 10-year quanto swap might offer better pricing by bundling equity and currency exposure implicitly.

For retail investors, quantos are rarely accessible directly. They're institutional derivatives, available mainly through large banks. Some emerging-market ETFs use quantos internally to hedge currency exposure, but this is usually hidden from the fund holder.

## See also

<div class="wiki-seealso">

### Closely related

- [Dividend Swap](/dividend-swap/) — A swap exchanging fixed payments for realised dividends on an index.
- [Volatility Swap](/volatility-swap-derivatives/) — A forward on realised volatility with a fixed strike.
- [In-Arrears Swap](/in-arrears-swap/) — A floating-rate swap where the reference rate is set at period end.
- [Currency Risk](/currency-risk/) — The exposure to exchange rate movements on foreign assets.
- [Forward Contract](/forward-contract/) — An unlisted derivative locking in a future price.
- [Counterparty Risk](/counterparty-risk/) — The risk that a swap dealer defaults on its obligations.

### Wider context

- Derivative — A financial instrument whose value depends on an underlying asset or rate.
- [Interest Rate Swap](/interest-rate-swap/) — The standard swap, exchanging fixed and floating interest rates.
- [Hedge Fund](/hedge-fund/) — A privately managed fund using derivatives and short selling extensively.
- Securitisation — Bundling cash flows and selling them as tradeable securities.

</div>