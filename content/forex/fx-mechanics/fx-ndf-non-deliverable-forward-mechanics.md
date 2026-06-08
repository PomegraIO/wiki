---
title: "Non-Deliverable Forward (NDF): How FX Settlement Works Without Currency Delivery"
description: "Non-deliverable forward (NDF) contracts settle currency trades in USD rather than exchanging the underlying restricted currency."
keywords:
  - non-deliverable forward
  - ndf forex
  - ndf mechanics
  - currency settlement
  - restricted currency trading
  - emerging market forex
  - cash settlement
image: /svg/forex.svg
---

*A **non-deliverable forward** (NDF) is a [forward contract](/forward-contract/) that settles in a single currency (almost always USD) rather than requiring physical delivery of the underlying currencies. NDFs allow traders to bet on restricted or illiquid currencies—like the Chinese renminbi or Indian rupee—without actually needing to receive or deliver those currencies at maturity. This article explains how the settlement math works, why central banks restrict currency delivery, and when NDFs are used.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Non-Deliverable Forward — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex mechanics." />

<div class="wiki-infobox-caption">A forward contract that settles in cash (USD), not in the underlying currencies.</div>

|   |   |
|---|---|
| **Settlement type** | Cash settlement in USD only; no delivery of the restricted currency |
| **Typical tenor** | 1 month to 2 years; liquid out to 12 months |
| **Underlying currencies** | CNY (Chinese renminbi), INR (Indian rupee), BRL (Brazilian real), RUB (Russian ruble), many others |
| **Pricing basis** | [Interest rate differentials](/interest-rate/) between the two countries; similar to covered interest parity |
| **Settlement reference rate** | Spot rate at maturity, often defined as the central bank fixing or an average rate over the final days |
| **Why it exists** | Country capital controls or central-bank restrictions on currency movement |
| **Counterparty risk** | Typically lower than OTC [forwards](/forward-contract/) because settlement is via clearinghouse or major bank; [credit default swap](/credit-default-swap/) spreads track NDF basis |
| **Liquidity** | Most liquid in major emerging markets (CNY, INR); wider [spreads](/bid-ask-spread/) than vanilla forwards in less-traded pairs |

</aside>

## Why Currencies Become Non-Deliverable

Most developed currencies (USD, EUR, GBP, JPY, CHF) are freely convertible: anyone can exchange them at any [exchange rate](/spot-exchange-rate/), and there are no restrictions on taking the currency out of the country. A [forward contract](/forward-contract/) on such currencies typically settles by actual delivery—you pay USD and receive EUR, or vice versa.

But many countries, especially in Asia, emerging markets, and jurisdictions with capital controls, restrict the ability to exchange their currency. China limits CNY delivery to residents and approved entities. India restricts USD/INR trading to certain purposes and market participants. Russia, Brazil, and other countries have periodic restrictions. These restrictions exist to:

- Preserve central-bank forex reserves.
- Control capital flight.
- Support exchange-rate stability by restricting supply and demand for the currency.
- Tax or monitor cross-border flows.

Because these currencies cannot be freely delivered offshore, forwards on them would be impossible to settle normally. A non-deliverable forward solves this problem by never requiring delivery at all.

## The NDF Mechanics: Pricing and Settlement

Suppose a US investor believes the Indian rupee (INR) will strengthen against the dollar. The investor wants to buy INR forward, but India restricts INR delivery offshore. Instead, the investor enters a non-deliverable forward with a bank:

**Terms of the contract:**

- Notional: 10 million INR  
- Agreed NDF rate: 80.00 INR/USD (locked in today)  
- Settlement date: 3 months from today  
- Settlement: Cash in USD only  

At settlement, the bank observes the actual spot rate for USD/INR—say, 78.00 INR/USD (the rupee has strengthened, as the investor predicted).

**Settlement calculation:**

The investor is long INR and short USD at the locked rate of 80.00. The market rate is 78.00, which is better for the investor (fewer rupees per dollar). The profit is:

**Profit = Notional × (1 / Locked Rate − 1 / Spot Rate)**  
**Profit = 10,000,000 × (1/80.00 − 1/78.00)**  
**Profit = 10,000,000 × (0.0125 − 0.01282)**  
**Profit = 10,000,000 × (−0.00032) = −$3,200**

Wait—the math above assumes the investor was short INR (betting it would weaken). Let me recalculate for the investor being *long* INR (betting it would strengthen):

If the investor is **long INR** at the forward rate of 80.00, they profit when the spot rate is *lower* (fewer rupees per dollar means each rupee is worth more in USD). At 78.00 spot:

The investor has the right to convert INR to USD at 80.00, but can convert at 78.00. The benefit per rupee is:

**(1 / 78.00 − 1 / 80.00) × 10,000,000 = (0.01282 − 0.0125) × 10,000,000 = 0.00032 × 10,000,000 = $3,200**

The investor receives a $3,200 cash settlement.

Conversely, if the rupee had weakened (spot rate rises to 82.00), the investor would owe:

**(1 / 80.00 − 1 / 82.00) × 10,000,000 = (0.0125 − 0.01220) × 10,000,000 = −0.0003 × 10,000,000 = −$3,000**

The investor pays $3,000 to the bank.

## Pricing NDFs: Interest Rate Parity

The bank pricing the NDF does not actually deliver currency; instead, it hedges its exposure using deliverable forwards or by borrowing and lending in the two currencies. The NDF price is derived from **interest-rate parity:** the difference in interest rates between the two countries should equal the forward premium or discount.

If USD interest rates are 5% and INR interest rates are 7%, the rupee trades at a *forward discount* (it should trade cheaper in the forward market to compensate for the interest-rate difference). The formula:

**(F − S) / S ≈ r_INR − r_USD**

Where:
- **F** = forward rate (INR/USD)  
- **S** = spot rate (INR/USD)  
- **r_INR** = Indian interest rate  
- **r_USD** = US interest rate  

If spot is 80 and rates are as above, the 1-year forward should trade at approximately:

**F ≈ 80 × (1.07 / 1.05) ≈ 81.52**

The bank builds this into the NDF quote. The wider the interest-rate differential, the more the forward deviates from the spot rate.

## Settlement Reference Rate: A Crucial Detail

The NDF contract specifies *which* spot rate is used for settlement. This is critical because:

1. **Spot can jump:** On the settlement date, the spot rate might spike due to news or market moves. The counterparties need to agree on a single reference.
2. **Multiple quotes exist:** Different sources (central bank fixing, bank dealer rates, exchange rates) may quote slightly different spot rates.

Most NDFs use:

- The **central bank fixing** (e.g., the Reserve Bank of India's official USD/INR rate at 12:00 IST on the settlement date).
- An **average of dealer quotes** over a time window (e.g., the midpoint of the 4 p.m. London close rate for USD/CNY).
- The **spot rate on a specific exchange** (e.g., the Shanghai Foreign Exchange Centre for CNY).

The contract specifies this precisely to avoid disputes.

## Why Traders Use NDFs

**Hedge currency exposure:** A US multinational with a subsidiary in India that repatriates dividends in INR can use NDFs to lock in the USD equivalent without needing to navigate India's currency controls.

**Speculation:** A trader betting on rupee appreciation can buy INR NDFs for leverage without touching actual rupees.

**Relative-value trades:** Comparing the NDF rate to the deliverable forward rate (for currencies that have both) can reveal valuation mismatch, because the NDF rate should track the forward rate if interest rates and expectations are aligned.

**Emerging-market strategies:** Hedge funds and emerging-market traders use NDFs as core tools to trade currency views in restricted jurisdictions.

## NDF Basis and Credit Signals

In some currencies, both deliverable forwards and NDFs trade. The **NDF basis** is the difference between the two rates. Normally, they should be nearly identical, but they can diverge if:

- **Credit concerns:** If traders fear a country's [sovereign default](/sovereign-default/) or currency restrictions tightening, they may demand a larger discount in the NDF, pushing it lower than the deliverable forward.
- **Liquidity:** If the NDF is less liquid, bid-ask [spreads](/bid-ask-spread/) widen, creating a basis.

Central bankers and traders monitor NDF bases as a signal of market stress. A widening NDF basis for a country's currency is often a red flag.

## Risks and Limitations

- **Counterparty risk:** The bank paying you at settlement must not default. Most major banks have low default risk, but NDF dealers can be smaller, regional banks.
- **Basis risk:** If the reference rate used for settlement is not the same as your actual exposure rate (e.g., you actually receive rupees at a provincial bank rate, not the RBI fixing), you face a mismatch.
- **Forced settlement:** You cannot defer settlement or take delivery; the contract forces cash settlement on the maturity date.
- **Liquidity in longer tenors:** NDFs are most liquid out to 12 months. Beyond that, quotes widen, and some currencies have no NDF market at all.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward contract](/forward-contract/) — The deliverable version; NDF is the cash-settled variant
- [Interest rate](/interest-rate/) — The economic driver of NDF pricing via interest-rate parity
- Covered interest parity — The principle linking [spot rates](/spot-rate/), forward rates, and interest rates
- [Currency risk](/currency-risk/) — The exposure NDFs are used to hedge
- [Spot exchange rate](/spot-exchange-rate/) — The reference rate used to calculate NDF settlement
- [Bid-ask spread](/bid-ask-spread/) — Wider in NDFs than in deliverable forwards

### Wider context

- [Swap](/swap/) — An alternative way to hedge currency exposure over longer periods
- [Over-the-counter market](/over-the-counter-market/) — Where NDFs are traded (not on exchanges)
- [Credit risk](/credit-risk/) — The bank counterparty risk in NDF settlement
- Emerging markets — Where capital controls and NDFs are most prevalent
- [Capital flows](/capital-flows/) — Why countries restrict currency delivery

</div>
