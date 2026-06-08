---
title: "Deliverable FX Forward"
description: "A forward contract settled by physical delivery of both currencies, as opposed to non-deliverable forwards (NDFs) settled in cash."
keywords:
  - fx forward
  - deliverable forward
  - physical settlement
  - non-deliverable forward
  - fx derivatives
  - counterparty settlement
  - fx market
image: "/svg/forex.svg"
---

*A **deliverable FX forward** is a forward contract in which both counterparties are obligated to physically deliver the agreed-upon amounts of each currency at settlement. Unlike non-deliverable forwards (NDFs), which settle in cash, a deliverable forward involves actual transfer of funds across banking systems.*

## Settlement mechanics

In a deliverable forward between a bank and a corporate client:

**Trade date**: USD/JPY forward, six-month tenor, strike 110.00. Client agrees to sell USD 10 million and buy JPY 1.1 billion in six months.

**Settlement date**: The client and bank exchange:
- Client delivers USD 10 million to the bank's USD account.
- Bank delivers JPY 1.1 billion to the client's JPY account.

Both legs settle via CHIPS (for dollars) or local clearing systems (for foreign currency), typically on the same day or within T+2 (two business days). The physical movement of money is absolute; there is no "option" to net out or cash-settle unless the contract explicitly permits novation.

This is the **default mode** for major currency pairs (EUR/USD, GBP/USD, USD/JPY, USD/CHF) and any pair where the local central bank permits free onshore trading and deposit-taking by foreign entities. It is also the standard for trade finance, where an importer physically needs foreign currency to pay suppliers.

## Why deliverable forwards dominate for liquid pairs

**Central bank accessibility**: Corporates can maintain or open onshore bank accounts in major currencies because central banks (Federal Reserve, ECB, Bank of England) allow it. Settlement infrastructure is mature and regulated. For USD, deposits are FDIC-insured up to limits; the counterparty risk is the commercial bank, not the central bank.

**No regulatory arbitrage**: The forward price reflects the true [interest rate](/interest-rate/) differential between USD and foreign rates. If three-month USD LIBOR is 5% and EUR rates are 4%, the three-month forward premium reflects exactly that 1% differential. No hidden ceilings or non-resident restrictions distort pricing.

**Cost efficiency**: Physical settlement avoids the bid-ask spread that cash-settled NDFs incur. A USD/JPY deliverable forward is quoted at a tight spread (0.01 yen on a 100-yen pair); NDFs on the same pair might have a 0.05-yen spread because banks are pricing both settlement risk and convertibility risk.

**Liquidity and depth**: The deliverable forward market is vastly larger and more liquid than NDF markets. Banks can easily warehouse deliverable forwards, hedge them against other clients, or offload them to the cash market via the relationship between [spot](/spot-exchange-rate/), forward, and interest-rate [parity](/currency-risk/).

## Contrast with non-deliverable forwards (NDFs)

An NDF is a cash-settled contract used when the foreign currency is not freely convertible or the local central bank forbids deliverable transactions. For example, India's rupee is heavily restricted. A corporate needing USD/INR protection buys an NDF from a bank: they agree on an exchange rate, and at settlement, only the difference (the profit or loss) is exchanged in dollars. No rupees are physically delivered.

Deliverable forwards, by contrast, involve actual rupees *if* an onshore rupee account is available and regulations permit. Multinationals with Indian subsidiaries and rupee-earning operations often settle deliverable forwards. Foreigners without onshore access or facing exchange restrictions use NDFs.

**Key differences**:

| Feature | Deliverable | NDF |
|---------|------------|-----|
| **Settlement** | Both currencies delivered physically | Cash settlement in single currency (usually USD) |
| **Currencies** | Major pairs; onshore access required | Restricted, emerging-market pairs |
| **Counterparty** | Commercial bank or central counterparty | Usually major international bank |
| **Pricing** | Reflects interest-rate parity | Reflects counterparty risk + convertibility premium |
| **Liquidity** | Deep and interbank-traded | Deeper than OTC options but less deep than deliverable |
| **Cost** | Tight spreads (majors) | Wider spreads; higher hedging costs |

## Regulatory and operational requirements

A deliverable forward requires:

1. **Onshore bank accounts** in both currencies, held by the receiving party (or their local subsidiary).
2. **Central bank approval** or exemption from restrictions on foreign-currency conversion and cross-border movement.
3. **Nostro and vostro arrangements** (correspondent banking relationships) between the settlement banks in each currency.
4. **Confirmation and settlement instructions** specifying the exact accounts, amounts, and settlement dates.

For example, a Japanese importer buying a USD/JPY deliverable forward must:
- Hold a dollar account at a US bank (directly or via a Japanese bank's correspondent).
- Confirm to the counterparty the dollar account number.
- Ensure the Federal Reserve and the Bank of Japan both permit settlement through their respective clearinghouses.

Emerging-market corporates often cannot settle deliverable forwards because onshore dollar accounts are unavailable or restricted. They resort to NDFs or hold hard-currency deposits through offshore subsidiaries.

## Pricing and interest-rate parity

The deliverable forward price is derived from [interest-rate parity](/interest-rate/):

**Forward rate = Spot rate × (1 + domestic interest rate) / (1 + foreign interest rate)**

If spot USD/EUR is 1.10, the US 6-month rate is 5%, and the euro rate is 4%, the six-month forward is:

1.10 × (1.05 / 1.04) ≈ 1.1105

This reflects the fact that a dollar investor can lend at 5% for six months or sell dollars forward at a premium to lock in the same rate in euros, earning the euro 4% rate plus the forward premium. Arbitrage keeps the rates aligned. The relationship is airtight for deliverable forwards because arbitrage is frictionless for major banks.

NDFs, lacking this arbitrage path, often deviate from interest-rate parity, especially in currency-restricted countries. An NDF forward might be 1.10 × 1.03 if counterparty risk and convertibility fears push the rate wider.

## Counterparty risk and settlement finality

A deliverable forward is only as safe as the settlement infrastructure. For major currencies, this is highly regulated:

- **FEDWIRE** (US dollars) settles intraday; the Federal Reserve guarantees finality. Default risk is minimal.
- **TARGET** (euros) is similarly robust; ECB oversees settlement.
- **Smaller pairs** may settle through weaker clearing systems (e.g., some emerging-market central banks lack 24/7 processing).

If a counterparty becomes insolvent after a deliverable forward trade but before settlement, the receiving party may lose access to the currency it paid but never received. This is why counterparty [credit rating](/credit-rating/) and settlement guarantees matter.

Large banks mitigate counterparty risk by:
- Settling through central counterparties (clearing houses).
- Using netting agreements that offset multiple forwards bilaterally.
- Posting collateral (variation margin) daily.

Retail corporates typically accept the credit risk of their bank, which is usually investment-grade.

## Common use cases

**Trade finance**: An exporter with a confirmed euro invoice uses a deliverable forward to lock in USD proceeds. They sell EUR forward, receive the quoted rate, and know exactly how many dollars they will receive in 90 days.

**Cash flow forecasting**: A multinational with regular dividend repatriations uses deliverable forwards to hedge known foreign-currency inflows. Predictable and tax-transparent.

**Interest-rate speculation**: A trader expecting US rates to rise relative to sterling buys a six-month USD/GBP deliverable forward at a premium. If rates diverge as expected, the forward appreciates and the trader can unwind it at a profit before settlement.

**Carry funding**: A Japanese exporter with euro receivables might short a three-month USD/JPY deliverable forward as part of a carry trade, borrowing cheap yen to fund a long euro position.

## When deliverable forwards are not available

Corporates face deliverable forward restrictions in:

- **Capital-controlled economies**: China (CNY), India (INR before reforms), Russia (RUB post-2022 sanctions), Venezuela.
- **Hyperinflation regimes**: Zimbabwe, Argentina (often); local currency forwards are priced through NDFs instead.
- **Sanctioned countries**: Settlement infrastructure for certain currencies may be blocked (e.g., Russian ruble after 2022).

In these cases, NDFs are the only available hedging tool, and they trade at a significant premium to what interest-rate parity would predict.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward contract](/forward-contract/) — the generic instrument; this article covers the deliverable variant
- [Non-deliverable forward](/forward-contract/) — cash-settled alternative for restricted currencies
- [Spot exchange rate](/spot-exchange-rate/) — the starting point for forward pricing
- [Counterparty risk](/credit-risk/) — settlement counterparty solvency affects safety
- [Interest rate](/interest-rate/) — fundamental input to forward pricing via interest-rate parity

### Wider context

- [Currency risk](/currency-risk/) — the underlying exposure being hedged
- [Interest-rate risk](/interest-rate-risk/) — affects forward premium and fair value
- [Central bank](/central-bank/) — oversees settlement infrastructure and may restrict deliverable forwards
- [Hedge fund](/hedge-fund/) — common traders of deliverable forwards for speculation
- Trade finance — primary use case for corporates
- [Price discovery](/price-discovery/) — deliverable forwards are key price anchors in FX markets

</div>
