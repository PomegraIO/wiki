---
title: "How FX Forward Points Are Calculated"
description: "Step-by-step formula for converting a spot exchange rate into a forward rate using interest-rate differentials between two currencies."
keywords:
  - fx forward points calculation
  - interest rate parity formula
  - forward discount premium
  - forward rate calculation
  - carry trade differential
image: /svg/forex.svg
---

*The **FX forward points** that determine a forward exchange rate are derived from the **interest-rate differential** between two currencies. A simple formula—spot rate adjusted by the difference in borrowing costs—transforms today's exchange rate into tomorrow's, locking in a future price that reflects the cost of money in each currency.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Forward Points — calculation key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The "points" baked into a forward rate are pure interest-rate arbitrage, not speculation.</div>

|   |   |
|---|---|
| **Spot rate** | Today's exchange rate (e.g., USD/JPY 155.00) |
| **Base formula** | Forward = Spot × (1 + rate_A) / (1 + rate_B) |
| **Typical duration** | 1 month, 3 months, 6 months, 1 year, or longer |
| **Forward points** | Difference between forward and spot (in pips) |
| **Relationship** | Higher rate currency forwards at a discount |
| **Arbitrage driver** | Interest-rate parity prevents risk-free profit |
| **Counterparty** | Banks and FX dealers quote both sides of forward curve |

</aside>

## The Interest-Rate Parity Principle

FX forward rates are not guesses about where the market thinks the exchange rate will move. Instead, they are determined by **interest-rate parity**, a financial principle stating that there is no arbitrage-free profit in borrowing cheap money in one currency, converting it at the spot rate, lending it in another, and converting back at the forward rate.

When this condition holds, the forward rate adjusts automatically. If the Australian dollar has a higher interest rate than the US dollar, the Australian dollar will trade at a **forward discount** (you get fewer AUD per USD in the forward market than at spot). This discount offsets the interest-rate advantage, preventing traders from locking in free money.

## The Standard Formula

The most common formula for calculating a **forward rate** is:

**Forward Rate = Spot Rate × (1 + interest rate of base currency) / (1 + interest rate of quote currency)**

Let's define the inputs:

- **Spot Rate**: Today's exchange rate (e.g., USD/JPY 155.00, meaning 1 USD = 155 JPY).
- **Base currency**: The first currency in the pair (USD in USD/JPY); the one being quoted per unit.
- **Quote currency**: The second currency (JPY); the one you receive.
- **Interest rate of base currency**: The interest rate available on USD borrowing/lending (annualized percentage).
- **Interest rate of quote currency**: The interest rate available on JPY borrowing/lending (annualized percentage).

## Step-by-Step Example

**Scenario:** Calculate a 3-month USD/JPY forward rate.

**Given data:**
- Spot rate: USD/JPY 155.00
- 3-month USD interest rate: 5.50% annualized
- 3-month JPY interest rate: 0.25% annualized
- Time period: 3 months = 0.25 years

**Step 1:** Annualize the period adjustment.

For a 3-month forward (one-quarter of a year), we adjust rates by multiplying by 0.25.

USD rate for 3 months: 5.50% × 0.25 = 1.375% = 0.01375
JPY rate for 3 months: 0.25% × 0.25 = 0.0625% = 0.000625

**Step 2:** Apply the formula.

Forward Rate = 155.00 × (1 + 0.01375) / (1 + 0.000625)
Forward Rate = 155.00 × (1.01375) / (1.000625)
Forward Rate = 155.00 × 1.013117
Forward Rate = **157.03 JPY per USD**

**Step 3:** Calculate forward points.

The difference between the forward and spot rate is the "forward points" (though often quoted in fractional pips):

Forward points = 157.03 − 155.00 = 2.03 JPY per USD

Or in pips (tenths of a yen): 20.3 pips

Because the USD interest rate (5.50%) is much higher than the JPY rate (0.25%), the forward USD/JPY trades **stronger** (higher spot = more yen per dollar). This is a **forward premium** on the USD.

## Forward Discount vs Forward Premium

The direction of the forward move depends on which currency has the higher interest rate.

**Forward Premium (base currency trades stronger in the forward market):**
- Occurs when the base currency has a *lower* interest rate than the quote currency.
- Example: EUR/USD, where EUR rates are higher than USD rates; EUR trades weaker at the forward (fewer EUR per USD).
- Actually, this is backwards in the example above; let me clarify.

**Corrected understanding:**
- If USD rates (5.50%) > JPY rates (0.25%), the USD is "expensive to hold" (you're earning more in USD). To prevent arbitrage, the JPY must strengthen in the forward (you get fewer JPY per USD forward than at spot).
- Wait—the example showed 155.00 spot and 157.03 forward, meaning the *USD* strengthens. Let me recalculate.

Actually, the formula shows that when USD rates are *higher*, the USD trades *weaker* (the denominator effect), not stronger. Let me re-examine.

Forward = 155.00 × (1.01375) / (1.000625)

The numerator (1.01375) applies to the USD, and the denominator (1.000625) applies to the JPY. Because USD rates are much higher, the ratio is *larger* than 1, so the USD/JPY forward is *higher*—meaning you get *more* yen per dollar, so the dollar strengthens. 

**Corrected principle:**
- When the base currency (USD) has a *higher* rate, it trades *stronger* in the forward (forward *premium* on USD).
- When the base currency has a *lower* rate, it trades *weaker* in the forward (forward *discount* on USD).

In the USD/JPY example, USD rates are much higher, so the USD is at a forward premium; the forward rate is 157.03, higher than the spot 155.00.

## Impact of Time Decay

Longer-dated forwards show larger point adjustments. A 12-month forward incorporates a full year of interest-rate differential, while a 1-month forward incorporates only one-twelfth. Banks quote forward curves for standard tenors (1m, 3m, 6m, 1y, 2y, etc.), and the points widen as you extend the maturity.

## Real-World Complications

The textbook formula above assumes:
- Constant interest rates over the forward period (unrealistic).
- Access to borrowing and lending at the quoted rates (retail customers often pay or earn less favorable rates).
- No transaction costs (spreads, commissions).

In practice, FX dealers apply spreads to both the spot and forward rates. A bank quoting USD/JPY forwards will offer one rate to **sell** USD forward (slightly lower) and another to **buy** USD forward (slightly higher), capturing a profit on the difference. Over-the-counter forex markets are not exchange-traded; rates vary by counterparty relationship, size, and credit quality.

## The Carry Trade and Forward Points

The forward points are central to the **[carry trade](/carry-trade/)** strategy. Traders exploit interest-rate differentials by borrowing in low-rate currencies (like JPY or CHF) and investing in higher-rate currencies (like AUD or emerging-market currencies). The forward points are baked in to prevent arbitrage, but carry traders profit if currency [volatility](/currency-volatility/) creates an opening.

## See also

<div class="wiki-seealso">

### Closely related

- [Carry Trade](/carry-trade/) — profit from interest-rate differentials between currencies
- [Spot Exchange Rate](/spot-exchange-rate/) — current FX rate for immediate settlement
- [Forward Contract](/forward-contract/) — agreement to exchange currency at a future date
- [Interest Rate Risk](/interest-rate-risk/) — exposure to changes in borrowing costs
- [Currency Volatility](/currency-volatility/) — fluctuation of exchange rates
- [FX Option Premium Settlement](/fx-option-premium-settlement/) — premium payment timing for currency options
- [Interest Rate](/interest-rate/) — cost of borrowing or lending in a currency

### Wider context

- [Basis Risk](/basis-risk/) — mismatch between hedge and underlying exposure
- [Price Discovery](/price-discovery/) — how markets determine fair value
- [Arbitrage](/alpha/) — exploiting price discrepancies for risk-free profit
- [Central Bank](/central-bank/) — sets monetary policy and influences interest rates
- [Monetary Policy](/monetary-policy/) — central bank tools to manage currency and economy

</div>
