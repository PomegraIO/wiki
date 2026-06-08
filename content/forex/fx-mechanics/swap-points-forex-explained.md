---
title: "Swap Points in Forex: How Forward Pricing Works"
description: "Swap points adjust spot exchange rates to create forward rates based on interest rate differentials between two currencies, pricing the cost of borrowing one currency to fund another."
keywords:
  - swap points forex
  - forex forward pricing
  - interest rate differential forex
  - swap points calculation
  - forward exchange rate
  - currency carry cost
image: "/svg/forex.svg"
---

*In currency trading, **swap points** (or forward points) are the percentage adjustments added to or subtracted from the spot exchange rate to calculate the forward rate. They derive from the interest rate differential between two currencies: if one currency's interest rates are higher than the other's, the currency with higher rates trades at a forward discount (to reflect that borrowing it costs more).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap Points in Forex — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The mechanism that links interest rates to currency forwards, ensuring arbitrage-free pricing.</div>

|   |   |
|---|---|
| **Definition** | Pip adjustments to spot rate that reflect interest rate differentials |
| **Primary driver** | Interest rate differential between the two currencies |
| **Typical range** | 10 to 500+ pips for 1-year forwards, depending on rates |
| **Direction of adjustment** | Currency with higher rates trades at a forward discount |
| **Measurement period** | Quoted for overnight, 1-week, 1-month, 3-month, 6-month, 1-year forwards |
| **Key formula** | Forward rate ≈ Spot rate × (1 + domestic interest rate) / (1 + foreign interest rate) |
| **Example** | EUR/USD with higher EUR rates: EUR forward discount (swap points subtract from spot) |

</aside>

## The Foundation: Interest Rate Parity

Swap points are the mathematical embodiment of interest rate parity, one of the cornerstones of currency economics. The principle is simple: if you can earn 5% per year in the US and only 2% in the eurozone, investors would all flock to US assets. But that arbitrage is blocked by currency risk. When you invest dollars at 5% instead of euros at 2%, you're exposed to dollar depreciation. If the dollar falls 3% against the euro in a year, your 5% return is reduced to a 2% net return (in euro terms).

To prevent this arbitrage, the currency market must adjust the forward exchange rate to offset the interest rate difference. If you lock in today's forward rate, the higher interest rate in dollars is exactly balanced by a weak dollar forward rate. You end up with the same expected return whether you invest in dollars or euros—no arbitrage opportunity.

That adjustment—the difference between today's spot rate and the locked-in forward rate—is priced in terms of swap points.

## How Swap Points Are Calculated

The relationship is governed by the interest rate parity formula (in simplified form):

**Forward rate = Spot rate × (1 + r_domestic) / (1 + r_foreign)**

Where r_domestic and r_foreign are the interest rates for the two currencies over the forward period.

Let's work through a concrete example. Suppose:
- EUR/USD spot rate: 1.0800
- US interest rate (1 year): 5.00%
- EUR interest rate (1 year): 2.00%

The forward rate would be:
1.0800 × (1.0500 / 1.0200) = 1.0800 × 1.0294 = 1.1118

So the USD/EUR forward rate would be higher (1.1118 vs. 1.0800 spot). In swap points, the EUR trades at a discount. The USD, which has higher interest rates, appreciates in the forward market—but that appreciation is offset by the interest rate advantage.

In real trading, this isn't how brokers quote forwards. Instead, they quote the spot rate and separately quote swap points (e.g., "+200 pips" or "-50 pips"). You add or subtract those pips from spot to derive the forward rate. The direction (positive or negative) depends on which currency's rates are higher.

## Why Swap Points Move: The Interest Rate Link

Swap points are not static. As central banks change [interest rates](/interest-rate/), swap points adjust immediately in forward markets. If the [Federal Reserve](/federal-reserve/) raises US rates while the [European Central Bank](/european-central-bank/) holds steady, EUR/USD swap points for all forward tenors shift to reflect the wider interest rate gap.

On any given day, the swap points for EUR/USD across all maturities (overnight, 1-week, 1-month, 3-month, 6-month, 1-year) form a curve. A steep curve (large pips for longer maturities) typically signals a substantial interest rate differential. A flat curve suggests rate expectations are converging.

When interest rate differentials are wide (e.g., a 3% gap between USD and JPY rates), swap points can be massive—hundreds of pips—making the forward yen much stronger than the spot rate. When differentials are small (e.g., 0.25% between EUR and GBP), swap points are tiny, and forward rates are close to spot.

## Swap Points vs. Currency Carry and Overnight Swaps

Swap points are often confused with overnight swaps or carry costs, but they're distinct concepts.

Swap points are the forward premium or discount built into the forward exchange rate itself—a one-time adjustment when you lock in a forward.

An overnight swap (or rollover charge) is the daily interest that accrues when you hold a forex position overnight. If you're long EUR/USD and hold it from 5 p.m. to 5 p.m. the next day, your broker charges or credits you interest based on the interest rate differential. The direction (charge or credit) depends on which currency's rates are higher.

The two are related: overnight swaps, when accumulated over months or years, are driven by the same interest rate differential that drives swap points. But the mechanics differ. Swap points are built into the forward market price upfront; overnight swaps accrue daily.

A trader using swap points in a forward contract locks in the rate today. A trader rolling a spot position overnight incurs a daily charge (or credit) based on the overnight rate differential.

## Practical Application: Locking in Forwards

Currency traders and exporters/importers use swap points to lock in forward rates. A US exporter expecting to receive EUR 1 million in 3 months doesn't want to wait and risk USD depreciation. The exporter's bank quotes a 3-month EUR/USD forward rate, which is calculated as:

Spot (1.0800) + 3-month swap points (say, +150 pips = +0.0150) = 1.0950 forward rate.

The exporter locks in 1.0950. No matter where EUR/USD trades in the next 3 months, the exporter will receive 1.0950 USD per EUR received. The forward rate embedded the interest rate differential at the time of the quote.

## Why Central Banks and Carry Traders Watch Swap Points

Swap points are a leading indicator of interest rate expectations. If swap points suddenly widen, it often signals that the market is pricing in a larger future interest rate gap. Carry traders (who profit by borrowing in low-rate currencies and investing in high-rate currencies) watch swap points obsessively because they directly affect carry costs and returns.

In the [carry trade](/carry-trade/), a trader might short low-interest-rate JPY and long higher-yielding AUD. The daily overnight swap is a credit (the carry benefit). But if the [Reserve Bank of Australia](/federal-reserve/) signals future rate cuts, swap points compress, and the forward AUD weakens—a potential loss if the trade needs to be unwound early.

During periods of monetary tightening (rising [interest rates](/interest-rate/)), swap points often widen rapidly as rate differentials increase. During easing, they compress.

## See also

<div class="wiki-seealso">

### Closely related

- [Carry Trade](/carry-trade/) — strategies that exploit interest rate differentials between currencies
- [Interest Rate](/interest-rate/) — the fundamental driver of swap points and forward pricing
- [Forward Contract](/forward-contract/) — the contracts in which swap points are embedded
- [Spot Exchange Rate](/spot-exchange-rate/) — the current rate to which swap points are added
- [Currency Risk](/currency-risk/) — the risk that swap points are meant to hedge

### Wider context

- Foreign Exchange (Forex) — the market where swap points are quoted and traded
- [Central Bank](/central-bank/) — institutions that set rates and indirectly drive swap points
- [Interest Rate Differential](/interest-rate/) — the economic principle underlying swap-point pricing
- [Basis Risk](/basis-risk/) — the risk that the forward rate doesn't perfectly hedge currency exposure

</div>
