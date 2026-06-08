---
title: "Currency Fixing"
description: "Official benchmark exchange rates set daily by central banks and market panels, used to value international contracts and settle trades."
keywords:
  - exchange rate fixing
  - benchmark rate
  - WM/Reuters
  - central bank fixing
  - price discovery
  - contract valuation
image: /svg/forex.svg
---

*A **currency fixing** is an official benchmark exchange rate published daily (usually once or twice per day) by a central bank, market consortium, or administrator for a specific [currency pair](/currency-pair-spread-determinants/). Multinational corporations use fixings to convert foreign-currency earnings into domestic currency on their financial statements; pension funds and asset managers use fixings to value international portfolios; and courts use them to settle disputes over payments in foreign currency. Despite their importance, fixings are set mechanically from market data and are surprisingly vulnerable to manipulation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Currency Fixing — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for currency benchmarks." />

<div class="wiki-infobox-caption">Fixings are designed to be objective, but they are set from a narrow sample of trades during a short window, leaving them exposed to gaming.</div>

|   |   |
|---|---|
| **What it is** | An official daily (or intra-day) reference exchange rate for a currency pair |
| **Also called** | Fixing rate, reference rate, benchmark rate, official rate |
| **Set by** | Central banks, market consortiums (e.g., WM/Reuters), or national regulators |
| **Timing** | Usually once (often at 16:00 London time for major pairs) or twice daily |
| **Usage** | Valuing international [cash flow](/cash-flow-statement/)s, hedging contract value, portfolio accounting |
| **Precision** | Typically 4–5 decimal places for major pairs |

</aside>

## How fixings are calculated

The most widely used fixing for major currency pairs is the WM/Reuters rate, administered jointly by the World Bank and Thomson Reuters. This fixing is set daily at 16:00 London time (a 4 p.m. fix) for about 150 currency pairs. The methodology is: sample executable bid and ask prices from a panel of major dealing banks and electronic communication networks over a one-minute window (for major pairs) or a wider window (for less liquid pairs), then calculate the median bid and ask, average them, and publish.

Other fixings exist for specific purposes or jurisdictions. Central banks set their own official fixings (the Federal Reserve publishes rates; so does the European Central Bank and others) to provide a point of reference for domestic markets. The Thomson Reuters Benchmark Administration (TRBA) also publishes fixings. In emerging markets, local central banks often set the fixing for the domestic currency against major currencies, which becomes the reference rate for all foreign-exchange trading within that country.

The logic behind the fixing methodology is sound: by sampling from multiple dealers across a short window, the hope is to exclude outlier trades and settle on the "true" rate at that moment. But a one-minute window is narrow, and if the largest banks coordinate or if volume is light, the sample can be gamed.

## Why fixings matter: three domains

### 1. Corporate accounting and reporting

A multinational corporation earning revenue in euros but reporting in dollars must convert those euros to dollars on its financial statements. The question: at what rate? Using the spot rate on the day of receipt would be most accurate, but if a corporation receives dozens of payments daily, using actual spot rates is impractical. Instead, most corporations use the official WM/Reuters fixing or their central bank's official rate, applying it to all foreign-currency cash inflows and outflows on a periodic basis (usually weekly or monthly). This standardises reporting and makes financial statements comparable.

The same applies to portfolio valuation. A US pension fund holding European equities must convert the euro value of those positions to dollars each day for reporting. Most use the WM/Reuters fix rather than live spot prices, which provides a clean, auditable benchmark.

### 2. Derivatives and forwards

When a corporation hedges currency exposure, it often uses a forward contract that matures on a specific date. The question at maturity: at what rate does the corporation buy or sell currency? If the contract specifies "at the fixing," it means both parties are bound to use the officially published rate. This removes basis risk and ensures the contract value cannot be contested—the fixing is definitive by fiat.

For instance, a US exporter expecting to receive 100 million euros in three months might sell a forward contract to lock in dollars at today's rate. The contract will specify a rate (typically the forward rate implied by current spot and interest rate differentials), and at maturity, the two parties will exchange at the fixing or at a rate derived from the fixing.

### 3. Legal and dispute settlement

When a court or arbitration panel needs to determine the value of a foreign-currency payment in a lawsuit, it typically uses the fixing on the date of the transaction (or the date of judgment, depending on the jurisdiction's rules). Using the fixing prevents either party from claiming the "true" rate was different; the fixing is treated as evidence of the market rate.

## The London Fix and its history

The WM/Reuters 4 p.m. London fix became the global standard partly by network effect and partly by timing: 4 p.m. London is during both the European and North American trading days, so volume is typically high. Once most corporations and portfolios adopted it, dealers and central banks built systems around it, and switching became impractical.

But this concentration made the fix a target. In 2013, major banks including Barclays, Royal Bank of Scotland, and Citigroup were caught submitting false rates to the fixing panel during the narrow one-minute window, in coordination with their own trading desks. Traders in these banks knew in advance what trades they wanted to execute at the fix and would submit rates that steered the final fixing in their favour. Since trillions of dollars of contracts referenced the fix, even a small bias could generate huge profits.

The scandal triggered criminal convictions, substantial fines, and a overhaul of fixing administration. In 2015, the International Organization of Securities Commissions (IOSCO) published principles for benchmark administration, and WM/Reuters tightened the window, changed the methodology, and separated the data collectors from the publishing agent. Most major fixings now are set by independent administrators with input from multiple data sources and more opacity around individual contributor submissions.

## Emerging-market fixings and capital controls

In many emerging markets, the currency is not freely tradable in the offshore market, and the central bank sets the official fixing unilaterally or via a narrow set of onshore banks. This fixing becomes the only legal rate for international transactions: corporations must use it to report earnings, importers must use it to settle bills. The central bank can thereby control the effective [exchange rate](/currency-risk/) without explicitly imposing capital controls (though the effect is similar).

In some cases—Venezuela, Argentina, Turkey, and others—the official fixing has diverged wildly from the parallel (black market) rate, creating two-tiered currencies. Corporates in these countries face a dilemma: use the official fix and report at an unrealistic rate, or use the parallel rate and risk legal exposure.

## Current regime and digital alternatives

After the 2013 fixing scandal and subsequent IOSCO reforms, fixing reliability has improved but remains imperfect. The fixing window is now wider for most pairs, submissions are vetted for outliers, and data is sourced from multiple venues. However, the fundamental risk persists: a fixing set from a narrow sample during a specific window is always less reliable than a flow of continuous pricing.

Some argue that blockchain and distributed-ledger technologies could eventually replace fixings by creating an immutable record of traded prices, with the fixing calculated in real time from a transparent, decentralised source. But as of now, fixings remain centralised, administrator-dependent, and subject to operational and governance risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Price Discovery](/price-discovery/) — how market prices, including fixings, reveal information
- [Currency Pair Spread Determinants](/currency-pair-spread-determinants/) — spread variation that can persist around fixing times
- [Forward Contract](/forward-contract/) — derivatives that reference fixings at maturity
- [Over-the-Counter Market](/over-the-counter-market/) — where fixing-referenced contracts are settled
- [Safe-Haven Currencies](/safe-haven-currencies/) — major pairs with reliable, heavily-sampled fixings

### Wider context

- [Currency Risk](/currency-risk/) — the exposure that fixings help corporates manage
- [Credit Risk](/credit-risk/) — counterparty risk in fixing-referenced derivatives
- [International Financial Reporting Standards](/international-financial-reporting-standards/) — accounting standards that reference fixings
- [Spot Exchange Rate](/spot-exchange-rate/) — the live rate from which fixings are derived

</div>
