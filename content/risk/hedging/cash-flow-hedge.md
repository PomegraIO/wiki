---
title: "Cash Flow Hedge"
description: "Risk management strategy that locks in the cash flows of a future variable-rate or forecasted transaction using derivatives."
keywords:
  - cash flow hedge
  - interest-rate swap
  - forecast transaction
  - variable-rate debt
  - accounting hedge
image: "/svg/risk.svg"
---

*A **cash flow hedge** is a [derivative](/forward-contract/) contract that fixes the actual or expected cash flows of a future transaction, neutralising the risk that rates or prices will move before the cash actually flows. A company borrowing at a [floating rate](/interest-rate/) might swap into a fixed rate; an exporter expecting foreign currency revenue might lock in today's exchange rate. The hedge protects the cash that will change hands, not the balance-sheet fair value of an asset or liability.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cash Flow Hedge — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for financial risk and protection." />

<div class="wiki-infobox-caption">Fixing future cash flows to prevent price or rate movements from disrupting actual receipts or payments.</div>

|   |   |
|---|---|
| **What it is** | A derivative strategy (swap, forward, option) that locks in the cash amount of a future variable transaction |
| **Typical use** | Floating-rate borrowers, companies with foreign-currency revenue, commodity producers, regulated utilities |
| **Hedging instrument** | [Interest-rate swaps](/interest-rate/), [forwards](/forward-contract/), [call](/call-option/) and [put options](/put-option/), [futures](/futures-contract/) |
| **Accounting treatment** | Gains/losses on the hedge offset losses/gains on the forecasted transaction; reported in [OCI (Other Comprehensive Income)](/interest-rate-risk/) |
| **Effectiveness required** | Under [GAAP](/generally-accepted-accounting-principles/), the hedge must be 80–125% effective to qualify for hedge accounting |
| **Time horizon** | Days to several years; matches the maturity of the underlying forecast |

</aside>

## Why companies lock in future cash flows

Most businesses face cash-flow uncertainty. A manufacturer buys raw materials in dollars but sells in euros; profit depends on the exchange rate at settlement. An electric utility borrows at a floating rate, tethered to [LIBOR](/libor/) or [SOFR](/sofr/); rising rates erode net income. An airline books fuel for future flights but cannot predict oil prices. These are not fancy financial bets—they are the ordinary friction of doing business across borders, currencies, and time.

A cash flow hedge lets a company decide: "We will accept market risk on sales volume, product quality, and competition. But we will not accept the risk that rates or exchange rates blow up our margin." The company enters a derivative contract today that will offset tomorrow's adverse price move.

## The mechanics: forwards and swaps

**Interest-rate swaps** are the workhorse. A company has floating-rate debt, paying [SOFR](/sofr/) + 2% quarterly. It enters a [swap](/interest-rate/) with a bank, agreeing to pay a fixed 5% to the bank in exchange for receiving SOFR + some amount from the bank. The net result: the company pays a locked-in fixed rate. Economically, it has exchanged the floating-rate cash flows for fixed ones. The swap does not appear on the balance sheet as a liability (the original debt remains unchanged); instead, the company recognises unrealised gains or losses in [OCI](/interest-rate-risk/) as rates move, and those gains or losses are reclassified into net income when the actual interest payments are made.

**Foreign-exchange forwards** lock in the conversion rate. An exporter with €1 million due in 90 days enters a forward contract to sell euros at, say, 1.10 USD/EUR. In 90 days, regardless of the spot rate, the company receives exactly $1.1 million. The risk—that the euro weakens and the company loses out—is transferred to the bank counterparty. The company's future cash receipt is certain.

**Commodity futures** work similarly. An airline expecting to buy 100,000 barrels of jet fuel in three months might buy crude oil futures today at, say, $80/barrel (locking in cost at $8 million). If prices rise to $100/barrel by settlement, the airline saves $2 million; if they fall to $60, the airline loses $2 million on the futures but saves that amount on the physical purchase. The hedge leaves the airline's fuel cost stable, regardless of market moves.

## The accounting logic

Under [IFRS](/international-financial-reporting-standards/) and [GAAP](/generally-accepted-accounting-principles/), cash flow hedges receive special accounting treatment called "hedge accounting." Without it, the company would mark the swap or forward to fair value every quarter, creating volatile earnings that have nothing to do with the actual business. Hedge accounting lets the company defer gains and losses on the derivative until the underlying transaction settles.

Here's the flow:
1. Company enters a swap or forward to hedge forecasted cash flows.
2. Each quarter, the derivative moves in fair value (say, the swap gains $100,000 because rates fell).
3. That $100,000 gain is recorded not in net income but in [Other Comprehensive Income (OCI)](/interest-rate-risk/), a separate section of the income statement.
4. When the forecasted transaction actually occurs (the company makes the floating-rate payment, or the exporter receives the foreign revenue), the gain in OCI is "reclassified" to net income, offsetting the loss on the transaction itself.
5. The net effect: the company's reported earnings reflect only the hedged, certain cash flow, not the gyrations of the derivative.

This treatment requires the hedge to be "effective"—meaning the derivative's gains and losses must move in step with the underlying forecast transaction. [GAAP](/generally-accepted-accounting-principles/) requires 80–125% correlation; if the hedge is less effective, some of the derivative gain lands in net income, not OCI, creating earnings volatility.

## Real-world example: a European manufacturer

A German car-parts maker sells 70% of output to US customers, earning dollars. It pays suppliers in euros. In January, it forecasts Q2 export revenue of $10 million (due in late June). The [USD/EUR](/us-dollar/) spot rate is 1.10; the company worries the dollar will weaken to 1.00 by June, shrinking euro proceeds from €9.09 million to €10 million equivalent.

The company enters a forward contract to sell $10 million at 1.10 (locking in €9.09 million). Over the next five months:
- If the dollar weakens to 0.95, the company loses on the export revenue (lower euro-denominated proceeds) but wins on the forward (which locked in 1.10). The forward gain offsets the transaction loss.
- If the dollar strengthens to 1.20, the company wins on revenue but loses on the forward. Again, the derivative loss offsets the transaction gain.
- The company's euro-denominated cash receipt is €9.09 million no matter what.

For accounting purposes, the forward gain or loss sits in OCI until June; then it is reclassified into net income alongside the revenue. The net income reported reflects the hedged, certain amount.

## When cash flow hedges are not available

Some transactions cannot be hedged. A retailer forecasting Q4 sales cannot enter a derivative contract on future store traffic (no liquid market). A tech startup expecting venture-capital funding in six months cannot hedge the dollar amount (the round hasn't been negotiated). Hedges exist only for transactions with liquid, observable prices: interest rates, major currencies, major commodities, equity indices.

For unhedgeable risks, companies rely on [diversification](/diversification/) (selling in multiple currencies, locking in costs differently) or simply accept the volatility.

## Hedging vs. speculation

The line between a cash flow hedge and a bet is intent. A European exporter selling $10 million of goods in June and buying a forward to lock in the rate is hedging. An investor who owns no dollars but buys the same forward hoping the dollar strengthens is speculating. The derivatives are identical; the context changes everything. Regulators and auditors scrutinise cash flow hedges to ensure they are genuine offsets of business exposure, not hidden bets.

## See also

<div class="wiki-seealso">

### Closely related

- [Fair Value Hedge](/fair-value-hedge/) — offsetting changes in the fair value of recognised assets or liabilities, distinct from cash flow hedges
- [Net Investment Hedge](/net-investment-hedge/) — hedging the equity value of a foreign subsidiary, another variant of accounting hedges
- [Macro Hedging](/macro-hedging/) — portfolio-level protection against broad economic shocks, versus transaction-level hedging
- [Interest-Rate Swap](/interest-rate/) — the primary tool for locking in fixed rates on floating-rate debt
- [Forward Contract](/forward-contract/) — customised agreement to exchange at a future date at a locked price
- [Futures Contract](/futures-contract/) — standardised, exchange-traded version of a forward
- [Currency Risk](/currency-risk/) — the exchange-rate exposure cash flow hedges protect against
- [Other Comprehensive Income (OCI)](/interest-rate-risk/) — accounting category where unrealised hedge gains/losses sit until realisation

### Wider context

- [Derivative](/forward-contract/) — general category of financial instruments used in hedging
- [Generally Accepted Accounting Principles (GAAP)](/generally-accepted-accounting-principles/) — US standard that defines hedge accounting rules
- [International Financial Reporting Standards (IFRS)](/international-financial-reporting-standards/) — global standard with similar but distinct hedge accounting
- [Risk Management](/operational-risk/) — broader discipline; cash flow hedging is one tactic
- [Counterparty Risk](/counterparty-risk/) — risk that the bank providing the swap or forward fails

</div>
