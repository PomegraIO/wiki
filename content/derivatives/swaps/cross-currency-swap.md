---
title: "Cross-Currency Swap"
description: "A swap between two parties to exchange principal and interest payments in different currencies, used for financing and hedging."
---

*A cross-currency swap is a contract where two parties exchange principal and interest payments in two different currencies. One party borrows in their home currency cheaply (due to their credit rating or market conditions) and swaps the proceeds for the other currency, allowing both to finance at rates better than they could access directly.*

<aside class="wiki-infobox">
<div class="wiki-infobox-title">Cross-Currency Swap — key facts</div>
<table>
<tr><th>Principal exchanged</th><td>At inception and maturity, both notionals are exchanged at the agreed spot rate.</td></tr>
<tr><th>Interest legs</th><td>Typically fixed-fixed, fixed-floating, or floating-floating in the two currencies.</td></tr>
<tr><th>Typical use</th><td>Obtaining financing in a desired currency at a favorable all-in cost.</td></tr>
<tr><th>Duration</th><td>Often 5 to 30 years, matching long-term financing needs.</td></tr>
</table>
</aside>

## Why cross-currency swaps matter

Suppose a Japanese bank can borrow in Japanese yen at 1.5% (because the yen is a low-rate currency) but needs dollars for American investments. Instead of borrowing dollars at 5%, the bank can:

1. Borrow yen at 1.5%.
2. Enter a cross-currency swap to exchange yen cash flows for dollar cash flows.
3. Access dollars at an all-in cost of (1.5% yen rate) + (yen-dollar basis swap premium) ≈ 3.2%—better than 5%.

This is the core appeal: exploiting differences in [credit rating](/wiki/credit-rating/), market conditions, and currency-specific supply and demand to lower financing costs. The yen bank taps the yen bond market where it has an advantage; a dollar borrower taps the dollar market where *they* have an advantage; they swap the proceeds. Both win.

## Structure and cash flows

A cross-currency swap involves:

**At inception**: Both parties exchange principal amounts (in different currencies) at a pre-agreed exchange rate.

**During the life of the swap**: 
- Party A pays interest in Currency 1 (fixed or floating rate).
- Party B pays interest in Currency 2 (fixed or floating rate).

**At maturity**: Both parties exchange the principal amounts again, at the same exchange rate as at inception (even if the market exchange rate has moved). This locks in the currency conversion cost and is what distinguishes a cross-currency swap from a simple [FX swap](/wiki/fx-swap/).

Example: A U.S. company and a German company enter a 5-year cross-currency swap with a $100 million and €90 million notional. At inception, they exchange principals. The U.S. firm pays 3% fixed in dollars; the German firm pays 2% fixed in euros. Each year they exchange interest payments. At maturity, they exchange the principal amounts back.

## Drivers of the cross-currency basis

The spread (basis) that Party B pays to Party A is not simply determined by the difference in interest rates. It is driven by:

1. **Relative credit quality**: If the German firm has better credit than the U.S. firm, the German firm can borrow euros cheaply. The yen bank in the earlier example had a better credit rating in yen markets, so it could borrow yen cheaply.

2. **Relative demand**: If everyone wants to borrow in dollars, the dollar leg of the swap becomes expensive (the dollar payer has to pay more to incentivize the dollar receiver). If everyone wants to borrow in yen, the yen leg becomes cheap.

3. **Interest-rate differential**: The gap between dollar and yen rates affects the expected cash flows, which affects the swap's fair value.

4. **FX forward curve**: The [forward exchange rate](/wiki/forward-exchange-rate/) between the two currencies incorporates expected interest-rate and inflation differentials.

The basis is what makes the trade worthwhile. If the yen bank borrows yen at 1.5% and swaps into dollars, paying the dollar basis on top, it still ends up cheaper than borrowing dollars directly.

## Common types

**Fixed-for-fixed**: Party A pays fixed in Currency 1; Party B pays fixed in Currency 2. Common for long-term financing.

**Fixed-for-floating**: Party A pays fixed in Currency 1; Party B pays floating (SOFR, EURIBOR) in Currency 2. Common when one party wants to hedge floating-rate exposure.

**Floating-for-floating**: Both parties pay floating rates in their respective currencies. Less common but useful for basis trading and funding mismatches.

## Uses

**Synthetic financing**: A company that cannot borrow in a desired currency directly uses a cross-currency swap to synthetically create that exposure at a lower cost.

**Foreign subsidiaries**: A U.S. parent company needs to fund a Chinese subsidiary. Rather than borrowing dollars and converting to yuan at market rates (expensive), the parent borrows yuan via a cross-currency swap with a Chinese bank that has better access to yuan markets.

**Liability hedging**: A Japanese insurer holds dollar assets (U.S. bonds) but has yen liabilities. A cross-currency swap lets it exchange dollar cash flows for yen, matching assets to liabilities.

**Basis arbitrage**: A trader who believes the yen-dollar basis is mispriced can execute a profitable trade by borrowing cheaply in one currency, swapping into the other, and investing at a higher rate in that currency.

## Valuation

A cross-currency swap is valued as the sum of its discounted future cash flows:

1. Project future interest payments in both currencies using the respective [yield curves](/wiki/yield-curve/).
2. Project the principal repayment in both currencies (locked in at inception).
3. Discount using the appropriate [zero-coupon discount factors](/wiki/zero-coupon-bond/) for each currency.
4. Solve for the fixed rate or basis that equates the two legs in present value.

The valuation is complex because it requires two interest-rate curves and assumptions about [convexity](/wiki/convexity/) in each currency. Dealers must also risk-manage [currency risk](/wiki/currency-risk/) (the swap rate is sensitive to both interest-rate moves and FX moves).

## Risks

**Currency risk**: If the spot exchange rate moves sharply, the value of the swap can swing. Although principal is locked in at inception, the interim interest payments are affected.

**Interest-rate risk in both currencies**: A move in either the dollar or yen yield curve affects the swap's value. A dealer short yen interest-rate risk and long dollar risk must hedge both.

**Basis risk**: The basis (spread) between the two currencies can widen or tighten, affecting the all-in cost. If a company swapped into dollars at a 150 bps basis and the basis widens to 200 bps, the swap becomes less favorable.

**Counterparty risk**: Cross-currency swaps are long-dated and notional amounts are large, so [counterparty risk](/wiki/counterparty-risk/) is meaningful. Either party might default, leaving the other exposed.

**Liquidity risk**: If you need to exit early, dealers might quote a wide spread, especially if the swap is in less-liquid currency pairs.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the foundational derivative structure.</li>
<li><a href="/wiki/interest-rate-swap/">Interest-rate swap</a> — the single-currency cousin of a cross-currency swap.</li>
<li><a href="/wiki/fx-swap/">FX swap</a> — a simpler version that exchanges principal but no ongoing interest payments.</li>
<li><a href="/wiki/currency-option/">Currency option</a> — an alternative way to hedge currency risk.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/currency-risk/">Currency risk</a> — what cross-currency swaps are designed to hedge or create.</li>
<li><a href="/wiki/forward-exchange-rate/">Forward exchange rate</a> — used to lock in the conversion at inception.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the primary risk in long-dated swaps.</li>
<li><a href="/wiki/credit-rating/">Credit rating</a> — affects the rate at which each party can borrow.</li>
</ul>
</div>
