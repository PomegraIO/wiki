---
title: "Non-Deliverable Forward (NDF) Explained"
description: "A non-deliverable forward (NDF) hedges exposure to restricted or illiquid currencies where physical delivery is prohibited, settling in cash instead."
keywords:
  - non-deliverable forward
  - ndf
  - currency hedging
  - restricted currency
  - offshore settlement
  - non-convertible currency
---

*A **non-deliverable forward (NDF)** is a currency [forward contract](/forward-contract/) that settles in cash rather than requiring the actual delivery of the underlying currency pair. It exists because many countries restrict international money flows or peg their currencies, making normal forwards impossible or illegal. An investor or company with exposure to the Chinese yuan, Indian rupee, or Brazilian real can use an NDF to lock in an exchange rate today without ever needing to exchange physical currency—the profit or loss is simply settled in a convertible currency like U.S. dollars.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Non-Deliverable Forward — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for foreign exchange." />

<div class="wiki-infobox-caption">A settlement mechanism for hedging currencies that can't be freely moved across borders.</div>

|   |   |
|---|---|
| **Underlying** | Currency pair with at least one restricted or illiquid currency |
| **Settlement** | Cash only, in a freely convertible currency (usually USD) |
| **Maturity** | Typically 3 months to 5 years; highly liquid out to 2 years |
| **Counterparties** | Major banks and FX dealers; rare for retail |
| **Pricing** | Forward rate based on spot, interest-rate differentials, and [implied volatility](/implied-volatility/) |
| **Examples** | CNY/USD (China), INR/USD (India), BRL/USD (Brazil) |
| **Advantage** | Hedges real economic exposure despite capital controls |

</aside>

## Why NDFs exist: the restricted-currency problem

Not all currencies trade freely. Many countries impose capital controls—laws that limit or ban the movement of money in and out of the country, or that peg their currency to an artificial rate. The People's Bank of China manages a tight lid on the yuan. India restricts the rupee to registered users. Russia, Turkey, and Argentina have all gone through periods of strict control.

A normal [forward contract](/forward-contract/) requires that at maturity, one party physically delivers the currency to the other. But if you can't legally move the currency, or you can't convert it at the official rate, a normal forward becomes worthless. Enter the NDF: it does the same job—locking in an exchange rate for a future date—but sidesteps delivery entirely. The profit or loss is paid in cash in a convertible currency, usually U.S. dollars.

This matters to multinationals with exposure to restricted markets. A U.S. company with a subsidiary in Shanghai that earns yuan profits faces a dilemma: the yuan can't be freely converted at market rates, and rules often require earnings be repatriated at an official rate favorable to the Chinese government. An NDF lets the company lock in its economic exposure to yuan/USD changes without trying to physically move the currency.

## How an NDF is priced and settled

An NDF is quoted just like a forward: a spot rate today, and a forward rate for a future date (say, three months out). The forward rate is set by interest-rate [parity](/basis-risk/): if U.S. dollar interest rates are higher than yuan rates, the forward will quote yuan as stronger (fewer yuan per dollar), because investors would otherwise just borrow dollars, lend them in yuan, and pocket the interest differential. The [forward rate](/forward-contract/) is calculated to prevent this arbitrage.

At maturity, if the NDF's fixed forward rate was, say, 6.50 CNY/USD, and the spot rate on settlement date is 6.55 CNY/USD (the yuan has weakened), the seller of the forward (who bet on strength) has lost. The loss is: (6.55 − 6.50) × notional amount in USD. If the notional is $10 million, the loss is $50,000, paid in U.S. dollars.

This is the key difference from a deliverable forward: no one tries to exchange physical yuan and dollars. The counterparties simply calculate the difference between the agreed rate and the actual spot rate on settlement date, and one party pays the other that difference in dollars.

## Comparison to deliverable forwards and NDCs

**Deliverable forward:** Physical delivery of the currency pair occurs. Possible only if both currencies are fully convertible and no laws forbid the exchange. Uncommon for major emerging-market currencies.

**Non-deliverable forward (NDF):** Cash settlement in a convertible currency. Used when physical delivery is impossible, illegal, or impractical. Most common structure for restricted currencies.

**Non-deliverable swap (NDS):** Similar to NDF but involves periodic interest payments, not just a final settlement.

**Onshore and offshore rates:** Some restricted currencies have two rates—an official "onshore" rate used within the country and an "offshore" rate used in free markets outside. The NDF typically settles using the offshore rate (or a published fixing, like the Reuters or Bloomberg rate), which is more reflective of true supply and demand.

## Practical uses and risks

**Hedging:** A multinational exporting goods to India in rupees can hedge the rupee/dollar exposure with a 6-month NDF. It locks in the rate it will receive for those rupees, removing [currency risk](/currency-risk/).

**Speculation:** Traders use NDFs to bet on future exchange rates without needing access to the restricted currency. If you think the Brazilian real will strengthen (fewer real per dollar), you can buy a BRL/USD NDF forward at today's quoted rate, and profit if the real actually strengthens.

**Carry trade variants:** The [carry trade](/carry-trade/) sometimes involves emerging-market currencies with high interest rates. NDFs allow traders to express these bets even on restricted currencies.

**Basis risk:** The NDF settles against a spot rate published on settlement day. If that rate doesn't perfectly match your actual transaction rate (e.g., you have a real rupee transaction that settles at a slightly different rate), your NDF hedge is imperfect.

**Counterparty risk:** NDFs are over-the-counter derivatives, meaning they are traded bilaterally with a bank. If your bank counterparty fails, you lose the hedge. Large institutions use collateral agreements (CSA) to mitigate this.

**Liquidity:** NDF markets are deep for major emerging markets (CNY, INR, BRL) and major currency pairs out to 2 years. Beyond that, or for less-traded pairs, bid-ask spreads widen and depth thins.

## NDF markets in practice

Most NDFs trade between banks and institutional clients (hedge funds, multinationals, pension funds). Retail investors rarely access them directly. The market is largest for:

- **CNY/USD (Chinese yuan):** The onshore yuan is tightly controlled; the NDF is the main hedging tool for foreign exporters and investors.
- **INR/USD (Indian rupee):** India restricts rupee flows; the NDF is essential for multinational operations.
- **BRL/USD (Brazilian real):** Brazil has periods of capital-control tightness; NDFs are common for long-term hedges.

Trading volumes in these pairs are substantial—daily turnover in NDFs can exceed that in deliverable forwards—but the market is still less liquid than major currency forwards (EUR/USD, GBP/USD).

## Regulatory context

Regulators treat NDFs like other derivatives for leverage and risk. Banks must hold capital against NDF positions. Hedge funds and financial institutions report NDF exposure to regulators. The International Swaps and Derivatives Association (ISDA) has standard contracts for NDFs.

Some countries have occasionally tried to restrict or ban NDF trading, viewing it as a way to circumvent capital controls. China, for instance, has periodically tightened rules on NDF trading. But the economic need—hedging real exposure to restricted currencies—means NDFs persist wherever significant offshore operations occur.

## Alternatives and substitutes

When NDFs are unavailable or expensive, traders use alternatives:

- **Proxy hedges:** Using a highly correlated freely traded currency. Hedging Asia-Pacific exposure with USD/CNY volatility can be approximate.
- **Equity hedges:** Shorting stocks of exporters to the restricted-currency country, if the stock markets are open.
- **Deliverable forwards in less-restricted pairs:** Some emerging markets have weaker restrictions; forwards may be available.
- **Options:** An NDF option (swaption) can give the right, but not obligation, to enter an NDF at a future date.

But none of these is as clean or precise as a direct NDF. For companies with genuine exposure to restricted currencies, NDFs remain the standard tool.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward contract](/forward-contract/) — the deliverable version; underlying structure of NDFs
- [Currency risk](/currency-risk/) — the risk NDFs hedge
- [Carry trade](/carry-trade/) — a speculative strategy sometimes using NDFs
- [Interest rate swap](/interest-rate-swap/) — similar structure to non-deliverable swaps
- [Futures contract](/futures-contract/) — exchange-traded alternative to forwards, though less common for restricted currencies
- [Implied volatility](/implied-volatility/) — affects NDF pricing, especially in volatile emerging markets

### Wider context

- Chinese yuan — the restricted currency for which NDFs are most heavily used
- [Indian rupee](/indian-rupee/) — another major NDF market due to capital controls
- [Brazilian real](/brazilian-real/) — common in EM NDF trading
- [Over-the-counter market](/over-the-counter-market/) — the market structure in which NDFs trade
- [Derivatives hedging](/derivatives-hedging/) — the broader framework for NDF use
- [Capital flows](/capital-flows/) — the real-world constraint that makes NDFs necessary

</div>
