---
title: "FX Option Premium Currency Choice: Base vs Quote"
description: "Why FX option premiums are quoted in base or quote currency matters to cost and delta. Explains dealer conventions and effective pricing."
keywords:
  - fx option premium in base or quote currency
  - currency option premium quotation
  - fx option pricing conventions
  - option delta and premium currency
---

*When you buy a currency option, the **FX option premium** you pay can be quoted in either the base or quote currency—and that choice reshapes your effective cost, your delta, and how you compare prices across dealers. Understanding why dealers choose one convention or the other is essential to avoiding hidden costs and mispricing risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Option Premium Currency — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Premium currency choice changes effective cost and delta visibility.</div>

|   |   |
|---|---|
| **Premium quoted in** | Base currency or quote currency, per dealer convention |
| **Effect on cost** | Same notional premium, different home-currency equivalents |
| **Effect on delta** | Base-currency delta ≠ quote-currency delta for same strike |
| **Market convention** | Varies by pair: EUR/USD commonly quote/currency; exotics base |
| **Why it matters** | Misreading premium currency leads to cost misjudgment and delta misguidance |
| **Adjustment factor** | To convert: multiply or divide by spot exchange rate |

</aside>

## What "Premium Currency" Means

An FX option's **premium** is the upfront fee the buyer pays the seller for the right to exchange currencies at a set strike price. That premium has a monetary value—but it must be denominated in *some* currency. Dealers quote it in the base currency of the pair (the numerator) or the quote currency (the denominator), and that choice affects how you calculate your true cash outlay and how you interpret the option's sensitivity (delta).

Example: A EUR/USD call option struck at 1.0800 might carry a premium of 0.015 cents. But 0.015 what? If quoted in euros (the base), you pay 0.015 per euro of notional. If quoted in dollars (the quote), you pay 0.015 per dollar of notional. The same option, quoted two different ways.

## Why Base vs Quote Currency Matters for Cost

Your effective cost—measured in your home currency—depends on the premium currency and the spot rate. Suppose you are a U.S. investor buying a EUR/USD call and the spot is 1.0800.

**Scenario A: Premium in euros**  
You are quoted a premium of 0.0050 per euro on a contract for €1,000,000 notional.  
Total premium due: €1,000,000 × 0.0050 = €5,000  
Cost in dollars: €5,000 × 1.0800 = $54,000

**Scenario B: Premium in dollars**  
You are quoted the same economic premium as 0.0054 per dollar.  
Total premium due: $1,000,000 × 0.0054 = $5,400  
Cost in dollars: $5,400

The numbers differ because the conversion point is different. In Scenario A, you convert the euro premium to dollars at spot. In Scenario B, the premium is already in dollars. For the same economic option, the dealer adjusts the quoted premium rate to account for the currency of denomination.

This matters to your P&L tracking: if you pay in euros and spot moves against you, your dollar cost rises. If the dealer quotes in dollars, you know your exact dollar outlay upfront.

## How Delta Shifts with Premium Currency

[Delta](/option/) for an FX option measures how much the option's value changes when the spot rate moves. But the direction and magnitude of delta depend on whether you measure it in base-currency terms or quote-currency terms.

**Base-currency delta** answers: "If spot moves 1 unit, how much does the option gain or lose, measured in base currency?"

**Quote-currency delta** answers: "If spot moves 1 unit, how much does the option gain or lose, measured in quote currency?"

For a EUR/USD call option, base-currency delta and quote-currency delta are *not* the same number, even for an at-the-money option with delta ≈ 0.5. This is because a one-unit move in spot (e.g., 1.0800 to 1.0801) is a different percentage change in base terms than in quote terms.

Formally:
- **Quote-currency delta** ≈ Base-currency delta ÷ Spot rate

If a EUR/USD call has a base-currency delta of 0.45 (on a contract quoted in euros), its quote-currency delta is approximately 0.45 ÷ 1.0800 ≈ 0.042 (on the same contract quoted in dollars).

Dealers specify which delta they are reporting. If you assume quote-currency delta when they've given you base-currency delta, your risk estimate will be wildly off. For instance, you might think a 0.042 delta is tiny and immaterial, when the true (base-currency) delta is 0.45—a major exposure.

## Dealer Conventions: Why They Vary

Different currency pairs and dealer groups follow different conventions. There is no universal standard, which is why every quote sheet and term sheet spells out the premium currency explicitly.

**Majors (EUR/USD, GBP/USD, USD/JPY)**  
Conventions differ by dealer and region. U.S. traders often see premiums quoted in the quote currency (dollars for USD pairs). European dealers may quote base-currency premiums. Always check the term sheet.

**Emerging-market and exotic pairs**  
Premiums are more commonly quoted in the base currency, partly because the base is often the stronger, more liquid currency, and partly by regional habit.

**Cross-pairs (e.g., EUR/GBP)**  
Again, no universal rule. Confirm with the dealer on every trade.

The practical lesson: every FX option quote must include the premium currency. If it does not, ask. A 0.01 premium quoted in different currencies is not the same economic price.

## Converting Between Premium Currencies

If you need to compare two quotes and they use different premium currencies, you can normalize them:

**From quote-currency premium to base-currency premium:**
Base premium = Quote premium × Spot rate

**From base-currency premium to quote-currency premium:**
Quote premium = Base premium ÷ Spot rate

Example: You are quoted a USD/JPY call at a premium of 0.80 yen per dollar (base-currency). Spot is 150.00. To express this in dollar terms (quote-currency):  
Dollar premium = 0.80 ÷ 150.00 ≈ 0.0053 dollars per yen

Now you can compare this to a competing dealer's quote in dollars on the same contract.

## Why Premiums Don't Cancel Out Across Legs

Suppose you are building a [spread](/option/) — say, a call spread to reduce premium cost. You buy a call at strike 1.0800 and sell a call at strike 1.0900. The premiums are naturally quoted in the same currency (by the same dealer) unless you explicitly cross dealers. But if you are comparing price from two different banks, you must convert premiums to the same currency before netting them. Otherwise, you will think you are getting a 0.002 euro debit when you are actually paying 0.003 dollars.

## Practical Tip: Always Confirm in Writing

Before entering any FX option trade:
- Ask the dealer to quote total premium in your home currency or in a currency you specify.
- Require the term sheet to state explicitly: "Premium quoted in [currency]."
- Convert multi-currency spreads manually before executing.

This removes ambiguity and prevents post-trade disputes about cost.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — Buyer's right to buy or sell at a fixed price; vanilla and exotic varieties.
- [Delta](/option/) — How much an option's value moves when the underlying price moves.
- [Spot Exchange Rate](/spot-exchange-rate/) — Current rate at which two currencies trade; reference point for option strike and premium comparison.
- [Carry Trade](/carry-trade/) — Borrowing in one currency and investing in another; option premiums reduce net carry yield.
- [Currency Volatility](/currency-volatility/) — Higher volatility raises option premiums across strike prices.
- [Strike Price](/strike-price/) — Fixed exchange rate at which the option can be exercised; determines intrinsic value and delta.

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — Using options and forwards to reduce currency and price risk.
- [Volatility Smile](/volatility-smile/) — Out-of-the-money options command different implied volatility; affects premium shape across strikes.
- [Over-the-Counter Market](/over-the-counter-market/) — FX options trade OTC with dealer quotes tailored to client needs.
- [Bid-Ask Spread](/bid-ask-spread/) — Dealer markup on currency options; premium currency choice can obscure true spread.

</div>
