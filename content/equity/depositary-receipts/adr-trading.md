---
title: "ADR Trading"
description: "Mechanics of buying and selling American Depositary Receipts on US stock exchanges."
keywords:
  - adr trading
  - american depositary receipt
  - cross-border equity
  - depositary bank
---

*An [American Depositary Receipt](/wiki/american-depository-receipt-adr/) (ADR) is a security that represents shares of a foreign company, traded on a US stock exchange as if it were a domestic stock.* Rather than owning the underlying foreign shares directly, investors own a receipt issued by a US custodian—typically a major US bank—that certifies ownership of those shares held in a foreign vault. Trading an ADR is as simple as trading any US equity: place an order, pay in US dollars, and settle in the standard US [settlement cycle](/wiki/settlement-cycles/). The complexity lies in the mechanics linking the ADR price to the underlying foreign share price and the role of the depositary.

<aside class="wiki-infobox">

| Key fact | Detail |
|----------|--------|
| **What it is** | Receipt for foreign shares held in custody |
| **Denominated in** | US dollars |
| **Trading venue** | US exchanges (NYSE, NASDAQ, OTC) |
| **Parties** | Investor, US depositary bank, foreign custodian |
| **Ratio** | 1 ADR may equal 1, 5, 10, or more foreign shares |
| **Settlement** | T+2 US clearing; underlying stock settles abroad |
| **Dividend flow** | Depositary collects, converts, distributes in USD |
| **Listing types** | Level 1 (OTC), Level 2 (NASDAQ/NYSE), Level 3 (sponsored) |

</aside>

## How an ADR order flows

When you buy 100 ADRs of a Japanese company listed on NASDAQ, your broker routes the order to the NASDAQ market maker or exchange floor. A transaction occurs at a quoted price, say $45.00 per ADR. Your broker receives 100 ADRs; the seller transfers them away.

Behind the scenes, the depositary bank (often JP Morgan, Bank of New York Mellon, or Citigroup) tracks this ownership. The bank does not physically move shares; it adjusts entries in its ledger. Your name is recorded in the bank's system as the owner of the ADR equivalent. The underlying Japanese shares remain in a vault in Tokyo, held by a Japanese custodian on behalf of the US depositary bank.

Selling is the reverse. You instruct your broker to sell 100 ADRs. Your broker submits a sell order, finds a buyer, and the transaction settles. The depositary updates its ledger to remove the ADRs from your account and add them to the buyer's.

## The [ADR issuance](/wiki/adr-issuance/) chain and ratios

The link between an ADR and the underlying foreign share is set at [issuance](/wiki/adr-issuance/). The depositary bank declares a **ratio**: one ADR may represent one foreign share, or five, or even 100. This ratio is chosen by the foreign company and the depositary to keep the ADR price in a desired range.

If Nestlé's Swiss shares are very expensive, the depositary might set the ratio at 1 ADR = 5 Swiss francs worth of shares, making each ADR cheaper and more liquid. Conversely, for a lower-priced foreign stock, the ratio might be 1:1.

The ratio is fixed until the foreign company or the depositary bank decides to change it (a rare event called a **consolidation** or **split**). Knowing the ratio is essential: when news breaks, you must convert the foreign share price to ADR terms using the ratio, then account for [currency translation](/wiki/currency-risk/).

## Currency conversion and the exchange rate impact

When a Japanese company reports its earnings in yen, the ADR investor faces currency risk. An ADR that trades at $45 today might be worth $40 in a month if the yen weakens against the dollar, even if the company's share price rises in yen terms.

The depositary bank handles dividend conversion but does not hedge currency for shareholders. When a Japanese company pays a yen dividend, the depositary receives it in yen, converts to dollars (at the depositary's chosen exchange rate), deducts its fee, and pays shareholders in USD. The conversion rate applied to dividends is typically published in advance; investors should check it to understand the net dividend received.

Trading the ADR itself does not directly trigger currency conversion—you are trading in dollars on a US exchange. However, the ADR's price is driven by the underlying foreign share price and the [exchange rate](/wiki/foreign-exchange-risk-bonds/). A trader comparing the ADR price to the foreign share price must always [cross-convert](/wiki/cross-rate/).

## Market makers and [ADR trading](/wiki/adr-trading/) liquidity

For [Level 2](/wiki/level-2-adr/) and [Level 3](/wiki/level-3-adr/) ADRs (those listed on major exchanges), professional [market makers](/wiki/market-makers/) provide [bid-ask spreads](/wiki/bid-ask-spread/). These [market makers](/wiki/market-makers/) profit by buying ADRs slightly below fair value and selling slightly above it.

The [market maker](/wiki/market-makers/) watches both the ADR price and the underlying foreign share price in real time. If the foreign share jumps 2%, the [market maker](/wiki/market-makers/) adjusts the ADR bid-ask quotes to prevent [arbitrage](/wiki/arbitrage-pricing-theory/). Sophisticated traders may exploit temporary mispricings by, for example, buying ADRs and simultaneously selling the foreign stock, pocketing the spread if prices reconverge.

[Level 1](/wiki/level-1-adr/) ADRs trade over-the-counter and often have wider spreads and lower volume because no [market maker](/wiki/market-makers/) is obligated to provide liquidity.

## Dividends and corporate actions

When a foreign company pays a [dividend](/wiki/dividend/), the depositary bank collects it from the foreign custodian, converts it to dollars, subtracts its fee (typically 0.5% but varies), and deposits the remainder to investors' US brokerage accounts.

The process is slow. If a Japanese company pays a dividend on May 1, the depositary may not credit US investors' accounts until late May or early June—a 3-4 week delay is typical. This lag is priced into the [ADR](/wiki/adr/) during the [ex-dividend](/wiki/ex-dividend-date/) window.

Corporate actions such as [stock splits](/wiki/stock-split/), [stock dividends](/wiki/stock-dividend/), and rights offerings are also the depositary bank's responsibility to administer. For a stock split in the underlying stock, the depositary notifies holders and adjusts the number of ADRs or the ADR ratio.

## [Arbitrage](/wiki/arbitrage-pricing-theory/) and the ADR-to-underlying spread

Because [ADRs](/wiki/adr/) trade in dollars on US exchanges and the underlying shares trade in foreign currency on foreign exchanges, a spread can open between the two. If the ADR is quoted at $45 and the underlying foreign share (at current exchange rates) is worth $46, sophisticated traders can buy the ADR, deliver it to the depositary for redemption, and sell the resulting foreign shares abroad for a profit.

Redemption is the inverse of [issuance](/wiki/adr-issuance/). A holder can instruct the depositary to convert ADRs back into the underlying foreign shares and request transfer to an account abroad. This option keeps [arbitrage](/wiki/arbitrage-pricing-theory/) opportunities in check: if [ADRs](/wiki/adr/) trade at a significant discount to the underlying shares, arbitrageurs will redeem, driving the [ADR](/wiki/adr/) price up until the spread closes.

## Settlement and the T+2 cycle in the US

[ADR trading](/wiki/adr-trading/) settles on a T+2 basis in the US: you buy on Monday, the trade settles Wednesday. Your broker's clearing firm exchanges cash for [ADRs](/wiki/adr/) with the seller's clearing firm through the [Depository Trust Company](/wiki/depository-trust-company/).

The depositary bank (which maintains the ledger of [ADR](/wiki/adr/) ownership) is notified of the settlement and updates its records. The underlying foreign shares remain abroad in the foreign custodian's vault and follow the foreign market's [settlement cycle](/wiki/settlement-cycles/)—which may be T+2, T+1, or same-day depending on the foreign exchange.

---

<div class="wiki-seealso">

### Closely related
- [American Depositary Receipt](/wiki/american-depository-receipt-adr/) — Foundational concept: what an ADR is
- [ADR Issuance](/wiki/adr-issuance/) — How depositary banks create ADRs
- [Level 1 ADR](/wiki/level-1-adr/) — Unsponsored, over-the-counter trading
- [Level 2 ADR](/wiki/level-2-adr/) — Sponsored, listed on NASDAQ or NYSE

### Wider context
- [Depository Trust Company](/wiki/depository-trust-company/) — Central clearing and settlement hub
- [Bid-Ask Spread](/wiki/bid-ask-spread/) — Price difference between buy and sell quotes
- [Currency Risk](/wiki/currency-risk/) — Impact of exchange rate changes
- [Cross-Rate](/wiki/cross-rate/) — Computing exchange rates between two foreign currencies
- [Dividend](/wiki/dividend/) — Cash distribution to shareholders
- [Settlement Cycles](/wiki/settlement-cycles/) — Time between trade and final transfer

</div>
