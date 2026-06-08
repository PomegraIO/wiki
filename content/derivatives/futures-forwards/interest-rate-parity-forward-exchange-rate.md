---
title: "Interest Rate Parity and the Forward Exchange Rate"
description: "How interest rate parity determines the forward exchange rate and ensures arbitrage-free pricing between spot and future currency values."
keywords:
  - interest rate parity forward exchange rate
  - covered interest rate parity
  - forward premium
  - currency arbitrage
  - foreign exchange derivatives
  - spot-forward relationship
---

*The **interest rate parity and forward exchange rate** relationship explains why the forward price of a currency differs from its spot rate by an amount equal to the difference between the two countries' interest rates. This principle prevents pure arbitrage and locks in the true cost of borrowing in one currency to invest in another.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Interest Rate Parity — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The forward rate adjusts to eliminate riskless profit from cross-currency borrowing and lending.</div>

|   |   |
|---|---|
| **Definition** | Forward exchange rate reflects the interest rate differential between two currencies |
| **Formula** | F = S × (1 + r₁) / (1 + r₂) |
| **Prevents** | Covered interest arbitrage (buy low-rate country's currency, invest in high-rate country) |
| **Key assumption** | No transaction costs, capital controls, or credit-risk differences |
| **Practical consequence** | A higher foreign interest rate means the foreign currency trades at a forward discount |
| **Named as** | Covered interest rate parity (when forward contract locks in the exchange rate) |

</aside>

## Why the Forward Rate Must Differ from the Spot Rate

Imagine two countries: Country A with a 2% annual interest rate, and Country B with 5%. A dollar invested in Country B earns more, so there's a natural temptation to borrow cheap in Country A and lend expensive in Country B. But if the forward exchange rate were identical to the spot rate, an investor could execute that arbitrage with zero currency risk—locking in a 3% profit on the interest differential alone.

That opportunity cannot exist in a market with rational participants and deep [liquidity-risk](/liquidity-risk/). Instead, the forward rate adjusts downward (the currency of the high-interest country trades at a discount in the forward market). The discount exactly offsets the interest advantage, leaving no arbitrage profit. That relationship is **interest rate parity**.

## The Covered Interest Rate Parity Formula

The mathematical relationship is:

**F = S × (1 + r₁) / (1 + r₂)**

Where:
- **F** = forward exchange rate (units of domestic currency per unit of foreign currency)
- **S** = spot exchange rate
- **r₁** = domestic interest rate
- **r₂** = foreign interest rate

For concreteness, suppose the spot USD/EUR rate is 1.10 (one euro costs 1.10 dollars), US interest rates are 3%, and eurozone rates are 1%. The one-year forward rate should be:

F = 1.10 × (1 + 0.03) / (1 + 0.01)  
F = 1.10 × 1.03 / 1.01  
F ≈ 1.122

The euro appreciates forward (costs more dollars), counteracting the US interest-rate advantage.

## The Logic: Why Arbitrage-Free Pricing Matters

Suppose a trader borrows $110,000 at 3% in the US, converts it to euros at 1.10 (getting €100,000), invests that in a eurozone bond at 1%, and simultaneously sells euros forward at the forward rate. At maturity (one year):

- USD debt costs: $110,000 × 1.03 = $113,300
- EUR investment returns: €100,000 × 1.01 = €101,000
- EUR converted back at the locked forward rate (F ≈ 1.122): €101,000 × 1.122 ≈ $113,322

The profit is negligible (cents on $113,000)—precisely what interest rate parity predicts. If F were 1.10 (the spot rate), the profit would be €101,000 × 0.01 = €1,010 ≈ $1,111, and every trader would execute the same trade, driving the forward rate up until parity was restored.

## Deviations from Parity: When Real Markets Break the Rule

Academic studies find that interest rate parity holds closely in deep, liquid markets (major currencies, short horizons), but deviations exist in practice:

**Transaction costs and bid-ask spreads.** A trader pays to borrow, pays the forex bid-ask spread twice, and pays to invest. These frictions consume small arbitrage profits.

**Credit risk and counterparty differences.** If one country's risk premium rises (or falls), [default-rate](/default-rate/) expectations shift, and rates move independently of monetary policy, breaking the tight parity link.

**Capital controls and restrictions.** Some countries limit currency conversions or foreign investment, preventing arbitrageurs from executing the trade.

**Expectations and long-dated contracts.** For forwards longer than a few weeks, expectations about future spot rates, central bank policy, and inflation diverge. Traders may violate parity if they believe the market is pricing in incorrect rate expectations.

**Covered vs. uncovered parity.** Covered parity (using forward contracts to eliminate currency risk) is testable and mostly holds. Uncovered parity—the claim that the forward rate predicts the future spot rate—has failed repeatedly, particularly during currency crises and when interest-rate differentials reflect risk premiums rather than monetary fundamentals.

## Forward Premium and the Interest Rate Differential

The **forward premium** is the percentage difference between the forward and spot rates:

Forward Premium = (F − S) / S ≈ r₁ − r₂

In our EUR/USD example:
(1.122 − 1.10) / 1.10 ≈ 0.02 = 2%

This equals the 3% US rate minus 1% eurozone rate. The currency of the higher-interest country trades at a forward discount (its forward premium is negative); the lower-interest currency trades at a forward premium. Over time, this forward premium should approximate the interest rate differential, assuming stable policy and inflation.

## Practical Use: Hedging and Forward Pricing

For multinational corporations and international investors, [covered-call](/covered-call/) analysis and interest rate parity determine the true cost of foreign currency debt. A US company borrowing euros via a bond issue must evaluate:

1. The euro interest rate it will pay
2. The forward rate at which it will convert euros back to dollars to service debt
3. Whether the total cost exceeds a direct USD borrowing

If the forward market is efficient, the euro borrowing (including currency hedge) should cost roughly the same as USD borrowing—the lower euro interest rate is offset by the euro's forward appreciation. Deviations, when they appear, signal either market inefficiency or unpriced risks.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward Contract](/forward-contract/) — an agreement to exchange currencies at a locked rate on a future date
- [Currency Risk](/currency-risk/) — the exposure to gains or losses from changes in exchange rates
- [Spot-Exchange-Rate](/spot-exchange-rate/) — the current market rate for immediate currency conversion
- [Carry Trade](/carry-trade/) — borrowing in low-interest currencies and investing in high-interest currencies
- Covered Interest Arbitrage — exploiting interest rate differentials with hedged forex positions

### Wider context

- [Interest Rate](/interest-rate/) — the cost of borrowing across all currencies and markets
- [Monetary Policy](/monetary-policy/) — central bank actions that affect interest rates
- Foreign Exchange — the global market for currency trading
- [Derivatives Hedging](/derivatives-hedging/) — using contracts to reduce financial risk

</div>
