---
title: "Non-Deliverable Forwards and Restricted Currency Pairs"
description: "Non-deliverable forwards (NDFs) allow offshore trading of restricted currencies like Indian rupee and Brazilian real; settlement occurs in USD rather than physical delivery."
keywords:
  - non deliverable forward ndf
  - ndf currency pairs trading
  - emerging market restricted currencies
  - usd inr usd brl ndf
  - onshore offshore currency pairs
image: "/svg/forex.svg"
---

*A **non-deliverable forward (NDF)** is a cash-settled [forward contract](/forward-contract/) on a currency that cannot be freely traded or delivered offshore. NDFs allow traders and corporates to hedge exposure to restricted currencies like the Indian rupee (USD/INR), Brazilian real (USD/BRL), and South Korean won (USD/KRW) without violating capital controls or ownership restrictions. Settlement happens in USD, not the restricted currency itself—a workaround that has become the global standard for emerging-market forex risk.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Non-Deliverable Forwards — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex pairs." />

<div class="wiki-infobox-caption">An offshore rate-lock for currencies that can't be freely exported or delivered.</div>

|   |   |
|---|---|
| **Definition** | Forward contract settled in USD, not the restricted currency |
| **Common NDFs** | USD/INR, USD/BRL, USD/KRW, USD/TWD, USD/CNH (offshore yuan) |
| **Why they exist** | Capital controls limit onshore currency conversion and export |
| **Settlement** | Difference between NDF rate and spot at maturity, paid in USD |
| **Typical tenor** | 1 week to 2 years (most liquid at 1, 3, 6, 12 months) |
| **Market** | Decentralized interbank + electronic platforms (e.g., Bloomberg, Reuters) |

</aside>

## Why Restricted Currencies Require NDFs

Many emerging-market governments impose capital controls to prevent currency outflows, protect foreign-exchange reserves, or manage [inflation](/inflation/) and external debt. These controls limit who can convert the local currency to USD and in what amounts.

For example:

- **India** restricts rupee convertibility on the capital account. Non-residents cannot freely buy large quantities of rupees and convert them back without approval.
- **Brazil** limits offshore repatriation of real profits and restricts foreign-currency derivative positions for some investors.
- **China** does not allow physical delivery of onshore yuan (CNY) to overseas accounts; only the offshore yuan (CNH) circulates internationally, and that is also managed.

Without NDFs, a US company with an Indian subsidiary could not hedge its rupee earnings back to dollars—the rupee cannot be freely exported and converted. An NDF solves this: it is a cash-settled contract, requiring no actual movement of rupees out of India.

## Mechanics of Settlement

An NDF contract specifies:

- **Base currency** and **counter currency** (e.g., USD/INR)
- **NDF rate** (e.g., 83.50 rupees per dollar, agreed today)
- **Maturity** (e.g., 6 months)
- **Notional amount** (e.g., $1 million)

At maturity, the parties do not exchange the currencies. Instead, they compare the agreed NDF rate to the spot rate on settlement day. Whoever is out-of-the-money pays the difference to the in-the-money party, in USD.

**Example: USD/INR NDF**

- Today: NDF rate agreed at 83.50
- Notional: $1 million = 83.5 million rupees (conceptually)
- At maturity (6 months): spot rate is 84.00
- Settlement: Since 84.00 is weaker for the USD (more rupees needed per dollar), the USD-long party is out-of-the-money. They pay the difference: (84.00 − 83.50) × 1,000,000 = $500,000 (paid in USD)

If the spot rate had moved to 83.00 instead, the USD-long party would receive: (83.50 − 83.00) × 1,000,000 = $500,000.

No rupees are ever exchanged. The contract is purely a rate-lock on USD, paid in cash.

## NDF vs. Onshore Forward

Most currency pairs have deliverable forwards—the seller can actually deliver the currency at maturity. For example, a EUR/USD forward is deliverable: you can demand actual euros and deliver dollars, or vice versa.

Restricted currencies have two rates:

1. **Onshore forward** (CNY, INR, BRL onshore): A forward contract traded on domestic exchanges, often with strict rules about who can participate (usually banks and large corporates, not retail traders).
2. **Offshore NDF** (CNH, offshore INR, offshore BRL): A non-deliverable forward traded in international markets (London, Singapore, Hong Kong) with no physical delivery requirement.

The onshore rate is typically lower volatility and tighter [bid-ask spread](/bid-ask-spread/), because it can be arbitraged against deliverable spot transactions within the country. The NDF rate is wider and more volatile because it reflects purely offshore demand and supply, with no risk-free arbitrage backstop.

## The Onshore–Offshore Basis

Because the two markets operate independently (offshore traders cannot freely convert to onshore rates), the NDF rate and onshore forward often diverge. This difference is called the **onshore–offshore basis**.

| Scenario | Implication |
|---|---|
| NDF > onshore forward | Offshore investors are more bearish on the currency than onshore participants |
| NDF < onshore forward | Offshore investors are more bullish than onshore |

A widening basis can signal shifting expectations about capital-account liberalization, or simply a liquidity crunch in one market. Companies deciding whether to hedge onshore or offshore will choose based on the basis and their counterparty credit quality.

## Common NDF Pairs

The most liquid NDFs are:

- **USD/INR**: Indian rupee; very liquid, 1–2 pip [spreads](/bid-ask-spread/) on major tenors
- **USD/BRL**: Brazilian real; highly liquid
- **USD/KRW**: South Korean won; actively traded despite South Korea's liberalization efforts
- **USD/TWD**: Taiwan dollar; restricted, even though Taiwan is developed
- **USD/CNH**: Offshore Chinese yuan; the primary vehicle for offshore yuan exposure
- **USD/THB**: Thai baht; moderately liquid NDF market

Emerging-market corporates, hedge funds, and investors use these to hedge earnings, lock in funding costs, and speculate on currency moves without violating local regulations.

## Pricing and Interest-Rate Parity

Like deliverable forwards, NDFs should theoretically obey [interest-rate parity](/interest-rate/): the forward rate reflects the interest-rate differential between the two countries.

**NDF rate ≈ spot rate × (1 + domestic interest rate) / (1 + foreign interest rate)**

However, NDFs often trade at a discount or premium to this theoretical rate because:

- **Liquidity premium**: If onshore rates are tightly controlled and offshore NDFs are the only way to hedge, offshore investors pay a premium.
- **Credit-risk premium**: An NDF is an unsecured obligation; counterparty risk drives pricing.
- **Capital-control expectations**: If investors expect capital controls to loosen, they demand a premium to lock in the current NDF rate before it aligns with spot.

During crises (e.g., emerging-market currency crashes), NDF basis can blow out to 5–10% annualized, reflecting panic selling and counterparty-risk concerns.

## Regulatory Status

NDFs are legal and standardized. The International Swaps and Derivatives Association (ISDA) publishes a standard master agreement. Major banks, investment banks, and some brokers trade NDFs. Retail traders and some smaller corporates may not have direct access to NDF markets and instead use leveraged NDF products offered by brokers.

However, using an NDF to circumvent a country's capital controls can be illegal for residents of that country. A Brazilian resident using an offshore USD/BRL NDF to move money out of Brazil may violate Brazilian law. Institutional investors and multinational corporates typically have exemptions or licenses; retail traders do not.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward Contract](/forward-contract/) — the deliverable cousin of NDFs
- [Interest Rate](/interest-rate/) — what drives NDF rates
- [Currency Risk](/currency-risk/) — why corporates use NDFs to hedge
- [Bid-Ask Spread](/bid-ask-spread/) — typically wider on NDFs than spot
- [USD/SGD: The Dollar–Singapore Dollar Pair](/usd-sgd-dollar-singapore-pair/) — contrast with freely traded pairs
- [Currency Pair Half-Spread Cost Calculation](/currency-pair-half-spread-cost-calculation/) — NDF pricing mechanics

### Wider context

- [Capital Flows](/capital-flows/) — restrictions that create NDF demand
- [Central Bank](/central-bank/) — enforces capital controls
- [Forex Trading](/stock-exchange/) — market structure
- [Monetary Policy](/monetary-policy/) — why some countries restrict currencies

</div>
