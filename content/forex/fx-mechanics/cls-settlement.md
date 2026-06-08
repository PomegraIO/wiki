---
title: "Continuous Linked Settlement"
description: "A multilateral netting and settlement service operated by CLS Bank that eliminates Herstatt risk by synchronising payment-versus-payment settlement for major currency pairs."
keywords:
  - cls bank settlement
  - payment versus payment
  - herstatt risk
  - settlement risk forex
image: /svg/forex.svg
---

*[Continuous Linked Settlement](/cls-settlement/) (CLS) is a multilateral clearing system operated by CLS Bank, a BIS-owned entity, that nets FX trades and settles them on a [payment-versus-payment](/cls-settlement/) basis for 18 of the world's most-traded currencies. By requiring both legs of the currency exchange to settle simultaneously and irrevocably, CLS eliminates [counterparty risk](/counterparty-risk/) during the settlement window and has become the gold standard for managing [Herstatt risk](/cls-settlement/).*

<div class="wiki-hatnote">

For the historical Herstatt Bank incident, see [herstatt-risk](/cls-settlement/). For immediate settlement without netting, see [same-day-settlement-forex](/same-day-settlement-forex/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">CLS Settlement — key facts</div>

<img src="/svg/forex.svg" alt="A symbolic representation of forex settlement mechanics." />

<div class="wiki-infobox-caption">The safest way to settle FX trades in major currencies; eliminates settlement risk via atomic, synchronised payment.</div>

|   |   |
|---|---|
| **What it is** | Multilateral payment-versus-payment settlement system for 18 major currencies |
| **Operator** | CLS Bank International (owned by BIS-member central banks) |
| **Currencies covered** | USD, EUR, GBP, JPY, CHF, CAD, AUD, NZD, SEK, NOK, DKK, SGD, HKD, INR, BRL, MXN, ZAR, AED |
| **Settlement timing** | Near-real-time netting; settlement over 3–4 hours of the deal date |
| **Risk eliminated** | [Herstatt risk](/cls-settlement/) (counterparty failure during settlement window) |
| **Participation** | ~70 banks as settlement members; ~2000+ banks via indirect connection |

</aside>

## The Herstatt Bank disaster and why it changed everything

On 26 June 1974, Herstatt Bank in Cologne collapsed mid-trading day. European banks had already paid out deutschmarks to settle FX trades with Herstatt; American counterparties were waiting for dollars to arrive. Those dollars never came. Dozens of US banks lost substantial sums because they had no way to freeze the mark transfers once the bank failed.

This scenario—where one leg of the trade settles but the other doesn't because the counterparty defaults in between—became known as [Herstatt risk](/cls-settlement/) or settlement risk. For decades, banks bore this risk as a cost of doing business. The only mitigation was to limit [counterparty exposure](/counterparty-risk/) and shorten settlement times. By the 1990s, the scale of daily FX settlement was so large (trillions of dollars per day) that any major default could cascade, so central banks and the largest dealers created CLS.

## How payment-versus-payment eliminates the risk

CLS operates as a multilateral clearing and settlement hub. Instead of Bank A sending marks to Bank B and Bank B sending dollars to Bank C on a bilateral, sequential basis, all parties submit their trades to CLS. CLS nets all of Bank A's obligations and receivables in each currency, calculates its position, and then executes settlement in a single, atomic transaction: it debits Bank A's account in marks and credits it in dollars *simultaneously*. Either both legs settle, or neither does.

This atomicity is the crucial innovation. The settlement is "linked"—dollars and marks move together, not sequentially. A bank cannot find itself having paid out one currency and failed to receive the other. The [counterparty risk](/counterparty-risk/) that Herstatt exposed evaporates.

## The logistics: who participates and how

CLS Bank is housed in the United States and is owned by the world's major central banks (Federal Reserve, ECB, Bank of England, Bank of Japan, and others). Only very large banks are settlement members; they maintain accounts at CLS in each of the 18 settlement currencies and connect via dedicated networks (historically proprietary, now increasingly SWIFT).

A smaller bank that wants to use CLS must use an agent—a settlement member who acts as intermediary. The agent submits the small bank's trades to CLS, manages the netting, and ensures funds flow in and out of the small bank's nostro account at the agent.

The daily process unfolds in windows:

1. Trading day (any time zone): Bank A and Bank B execute an FX trade.
2. Settlement day morning (New York time): Both banks submit the trade to CLS via SWIFT.
3. CLS matching window (early morning): CLS confirms both sides of the trade agree.
4. CLS netting and funding: CLS calculates net positions for all members in each currency.
5. Settlement (late morning to early afternoon NY time): Banks fund their CLS account with the currencies they owe; settlement happens in real time.

Once settlement occurs, the transfer is irrevocable. There is no window in which a bank can walk away or fail partway through. This certainty is why CLS settlement is so prized.

## Why 18 currencies, not all of them

The 18 currencies in CLS cover approximately 90% of daily FX turnover. Including every minor currency would add operational complexity and make the system slower. For emerging and frontier currencies (Turkish lira, Thai baht, Philippine peso), banks still settle bilaterally or via regional hubs. This is where [Herstatt risk](/cls-settlement/) still exists—smaller FX markets have not yet moved to payment-versus-payment infrastructure.

## CLS fees and adoption

CLS charges settlement members a fee per trade (usually a few cents) plus account maintenance fees. For high-volume dealers, the cost is trivial; for smaller banks, it can add up. But the elimination of [counterparty risk](/counterparty-risk/) is so valuable that CLS now handles roughly 2 trillion dollars in FX settlement per day. Most institutional FX trades in major currencies settle via CLS by default.

Some banks use CLS only for large deals or when counterparty risk is acutely felt (during financial stress or when dealing with riskier counterparties). For internal or trusted intra-group trades, some may still use bilateral settlement. But market convention strongly favours CLS for any material FX trade.

## CLS vs bilateral settlement and same-day settlement

A bilateral FX settlement means Bank A and Bank B agree to settle one another directly, without a clearinghouse intermediary. This is faster but reintroduces [counterparty risk](/counterparty-risk/). If Bank B defaults after receiving currency but before paying out, Bank A loses.

CLS takes longer (3–4 hours versus 30 minutes) but guarantees atomicity. For any deal where [counterparty credit risk](/counterparty-risk/) matters—which is nearly all of them in a real market—the extra 3 hours is a bargain.

[Same-day settlement](/same-day-settlement-forex/) is true T+0; you deal and settle within hours. CLS is near-same-day (T+0 in practical effect) with the safety guarantee. For most institutional traders, CLS is sufficient and cheaper than demanding true same-day settlement with a premium spread.

## Impact on market structure

CLS has fundamentally reshaped FX market infrastructure. It standardised settlement procedures, reduced dealer capital requirements by eliminating settlement-window exposures, and allowed central banks to monitor and stress-test the system. During the 2008 financial crisis, when [counterparty risk](/counterparty-risk/) spiked, CLS settlement continued smoothly because the atomicity meant no cascading failures.

The system is also a model for other asset classes. Equity and bond clearing houses (like Euroclear and Clearstream) adopted similar ideas. CLS proved that a multilateral, centralised settlement hub, backed by strong governance and central bank oversight, can eliminate a major class of systemic risk.

## See also

<div class="wiki-seealso">

### Closely related

- [Herstatt risk](/cls-settlement/) — settlement risk during the FX settlement window
- [Counterparty risk](/counterparty-risk/) — credit risk borne when trading with another bank or institution
- [Same-day settlement in FX](/same-day-settlement-forex/) — alternative approach: trade and settle within hours
- [FX rollover rate](/fx-rollover-rate/) — financing charge when positions are not settled on their original date
- [Bid-ask spread](/bid-ask-spread/) — dealer margin; may narrow once settlement risk is eliminated

### Wider context

- Settlement date — standard T+2 timeline for FX trades
- Foreign exchange — market structure and participants
- Correspondent banking — network of banks executing cross-border payments
- SWIFT — messaging standard for international payment instructions
- [Systemic risk](/systemic-risk/) — risk of cascading failures in the financial system

</div>
