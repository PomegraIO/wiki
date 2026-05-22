---
title: "Interest Rate Parity"
description: "A relationship between spot and forward exchange rates and interest rates in two currencies, ensuring no arbitrage profit from interest-rate differentials."
keywords:
  - interest rate parity
  - covered interest arbitrage
  - forward premium
  - currency hedging
  - forex valuation
---

*A fundamental principle of foreign exchange markets, **interest rate parity (IRP)** states that the difference in [interest rates](/wiki/interest-rate/) between two currencies must equal the difference between the spot and forward exchange rates. If this relationship breaks down, an arbitrageur can exploit the gap with a "covered" transaction — borrowing in one currency, converting to another, investing, and locking in a [forward rate](/wiki/fx-forward/) to convert back — capturing a risk-free profit.*

<aside class="wiki-infobox">

| Key Fact | Detail |
|----------|--------|
| **Core principle** | Forward premium offsets interest rate differential |
| **Formula** | Forward rate = Spot rate × (1 + r_domestic) / (1 + r_foreign) |
| **Arbitrage** | Covered interest arbitrage exploits IRP deviations for near-riskless profit |
| **Market efficiency** | IRP typically holds within transaction costs; deviations are small/brief |
| **Exceptions** | Capital controls, credit risk, illiquidity can cause persistent deviations |
| **Implications** | Spot rates embed expectations of future interest rate changes |
| **Historical context** | Validated empirically for developed markets since the 1970s |

</aside>

## The mechanics: forward premium and interest differential

The relationship can be stated simply: **If country A has higher interest rates than country B, the forward exchange rate will show A's currency trading at a discount (weaker) relative to the spot rate.** This discount offsets the interest advantage, preventing arbitrage profit.

Example with numbers:

- **Spot rate:** 1 USD = 0.95 EUR (USD is strong).
- **US interest rate:** 5% per annum.
- **Eurozone interest rate:** 2% per annum.
- **The differential:** US rates are 3% higher.

If the forward rate doesn't adjust, an arbitrageur could:
1. Borrow €100 at 2%.
2. Convert at spot (1 USD = 0.95 EUR) → receive ~$105.26.
3. Invest at 5% US → have $110.52 in one year.
4. Lock in a forward to convert back to EUR.

If the forward rate were still 0.95, the arbitrageur would convert $110.52 back to ~€104.98, netting ~€4.98 profit on €100 borrowed — a risk-free 5% gain. Markets don't allow this for long. The forward rate must weaken (USD trades at a discount), so the forward might be 1 USD = 0.93 EUR. This discount offsets the interest advantage, leaving no profit.

## The formula: covered interest rate parity

The precise formula is:

**Forward Rate / Spot Rate = (1 + r_domestic) / (1 + r_foreign)**

Rearranged:

**Forward Rate = Spot Rate × (1 + r_domestic) / (1 + r_foreign)**

Using 1-year rates and the example above:

**Forward = 0.95 × (1.05 / 1.02) ≈ 0.95 × 1.0294 ≈ 0.9779 EUR/USD**

The USD forward rate is now weaker (0.9779 vs. 0.95 spot), reflecting the forward premium for the higher-yielding currency (EUR).

## Spot rate expectations and uncovered interest parity

A closely related concept is **uncovered interest parity (UIP)**: the expectation that the spot rate will depreciate by the interest rate differential, with no forward contract locked in. Under UIP, if a currency has a higher interest rate, market participants expect it to depreciate over time, offsetting the yield advantage for foreign investors.

This is why a high-yielding emerging-market currency often depreciates against low-yielding currencies over medium-term periods — investors expect this to happen and demand the higher yield as compensation for depreciation risk.

## Why IRP usually holds: arbitrage and market efficiency

IRP holds (within small transaction costs) because of **covered interest arbitrage**. If the forward rate deviates from the IRP-predicted level, a trader can execute a perfectly hedged transaction (covered) to lock in a profit. Since the profit is locked in and riskless, competitive traders flood the market, driving prices back into line with IRP.

The only reason deviations persist is transaction costs (bid-ask spreads, borrowing premiums, bid-ask in forwards) that are large enough to swallow the arbitrage profit.

## Exceptions and deviations: when IRP breaks down

**Capital controls.** If a government restricts currency convertibility or cross-border flows, IRP may not hold because investors can't freely execute the arbitrage. Emerging markets with capital controls sometimes show IRP deviations because arbitrageurs can't freely access covered trades.

**Credit risk and counterparty risk.** If borrowing in one currency is risky (e.g., borrowing in a high-default-risk emerging-market currency), the borrowing rate reflects a [credit premium](/wiki/credit-spread/). The spot and forward markets may not fully adjust for this premium, creating apparent IRP deviations.

**Illiquidity in forward markets.** For exotic currency pairs or long-dated forwards, forward markets can be thin. Bid-ask spreads are wide, preventing arbitrage from bringing prices in line with IRP.

**Deviations post-2008.** After the 2008 financial crisis, researchers observed persistent covered interest rate parity deviations in developed-market currency pairs (USD-EUR, USD-GBP) even as spreads fell. One explanation: banks' reduced appetite to leverage arbitrage trades, combined with balance-sheet constraints and regulatory capital requirements, meant fewer traders were executing the arbitrage. The deviations persisted until central bank coordination and balance-sheet repair reduced bank caution.

## Implications for spot rate determination

IRP implies that spot exchange rates are forward-looking. If US interest rates rise relative to eurozone rates, the USD forward is priced stronger (in premium) relative to the EUR. But the spot rate may not immediately move; instead, the market prices in the expectation that the USD will appreciate in the future to offset the interest differential. Over time, as interest differentials persist, the spot rate does depreciate (or the high-yielding currency appreciates), aligning with the forward premium.

This is why forex traders monitor central bank policy and interest rate expectations closely — they drive IRP adjustments, which in turn drive spot rates.

## Hedging applications

**Importers and exporters.** A US exporter expects to receive EUR in 3 months. If US rates are higher than EUR rates, the forward EUR rate will be stronger than spot. The exporter can lock in that stronger rate via a [forward contract](/wiki/forward-contract/), locking in more USD proceeds than the spot rate would provide at settlement.

**International investors.** A US investor buys a eurozone bond yielding 2%. If US rates are 5%, the EUR will depreciate over time (per UIP) to offset the yield difference. The investor faces depreciation risk. Buying a [currency forward](/wiki/fx-forward/) to lock in a conversion rate back to USD hedges this risk, though at a cost — the forward is stronger than spot, reflecting the interest differential.

**Arbitrage traders.** The tiny mispricings in IRP (basis points) are the domain of high-frequency traders using algorithms to spot and exploit deviations in microseconds.

## Cross-currency basis

Related to IRP is the **cross-currency basis** — the difference between borrowing in one currency directly vs. borrowing in another and swapping back to the original currency. Even though IRP suggests these should be equal, [swap markets](/wiki/interest-rate-swap/) sometimes show deviations, reflecting supply/demand imbalances or credit differentiation between currencies.

## Integration with forex trading models

Sophisticated forex forecasting models combine IRP with other factors:

- **Purchasing power parity (PPP).** Long-term exchange rates should align with relative price levels.
- **Current account balances.** A large deficit may signal depreciation pressure.
- **Growth differentials.** Faster growth in one country may support currency appreciation.

IRP is the mechanistic underpinning; these other models add longer-term, structural perspectives.

<div class="wiki-seealso">

### Closely related
- [Forward Exchange Rate](/wiki/forward-exchange-rate/) — Rate locked in for future settlement
- [FX Forward](/wiki/fx-forward/) — Contract hedging future currency need
- [Interest Rate Swap](/wiki/interest-rate-swap/) — Fixed-floating or cross-currency rate exchange
- [Purchasing Power Parity](/wiki/purchasing-power-parity-forex/) — Long-term exchange rate relationship

### Wider context
- [Currency Risk](/wiki/currency-risk/) — Exposure to exchange rate changes
- [Currency Hedging](/wiki/currency-hedging/) — Strategies to manage FX exposure
- [Carry Trade](/wiki/carry-trade/) — Strategy exploiting interest differentials and depreciation expectations
- [Central Bank Policy](/wiki/central-bank-interest-rates/) — Sets baseline rates driving IRP

</div>
