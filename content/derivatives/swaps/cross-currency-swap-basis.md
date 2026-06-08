---
title: "Cross-Currency Swap Basis Explained"
description: "The cross-currency swap basis measures the deviation from covered interest parity between currencies. Persistent negative basis signals strong dollar funding demand."
keywords:
  - cross-currency swap basis
  - covered interest parity
  - cross-currency basis spread
  - dollar funding demand
  - forex swaps
  - interest rate parity
---

*The **cross-currency swap basis** is the spread between the actual interest rate differential in a cross-currency swap and the rate implied by covered interest parity theory. A persistent negative basis—especially in dollars—reflects real-time pressure in offshore dollar funding markets and reveals gaps between theoretical and market-observed pricing.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Currency Swap Basis — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The basis measures how far swaps deviate from what interest rate arbitrage suggests they should cost.</div>

|   |   |
|---|---|
| **Definition** | Spread between actual swap rate and covered interest parity prediction |
| **Sign convention** | Negative basis common in dollars; positive in other currency pairs |
| **What it signals** | Imbalances in offshore funding supply and demand |
| **Key driver** | [Counterparty risk](/counterparty-risk/), balance-sheet constraints, regulatory arbitrage |
| **Typical range** | −100 to +50 basis points (currency and market condition dependent) |
| **Market participants** | Corporate [swap](/swap/) traders, banks, [hedge funds](/hedge-fund/), central banks |

</aside>

## How Covered Interest Parity Sets the Baseline

Covered interest parity (CIP) is the theoretical anchor. It says that if you borrow euros at 3%, convert them to dollars at the spot rate, lend dollars at 5%, and lock in your return conversion to euros using a forward contract, the two paths should yield the same return. If they don't, arbitrage would close the gap.

Formally, the formula is:

**Forward rate ÷ Spot rate = (1 + r_domestic) ÷ (1 + r_foreign)**

In practice, the forward premium built into a currency should exactly offset the interest rate difference. If euros pay 2% and dollars pay 4%, the euro should trade forward at a premium—making your future dollar income cheaper to convert back.

The **cross-currency swap basis** quantifies the real deviation from this relationship. It exists because traders face frictions—balance-sheet limits, [credit spreads](/credit-spread/), capital charges, and political risk—that CIP doesn't account for.

## The Negative Dollar Basis Puzzle

For much of the post-2008 period, and especially during stress, the dollar basis has turned sharply negative. This means borrowing euros and swapping into dollars costs *more* than CIP predicts; the dollar is scarce and expensive relative to theory.

A negative basis of −50 basis points means a euro borrower paying 2.00% in euros and swapping to dollars might pay 2.50% in effective dollar cost—not the 2.45% that CIP would imply. The extra 5 basis points is the "basis."

This happens when:

- **Foreign banks and corporates need dollars urgently.** An EU exporter with a dollar asset sale coming needs to hedge; a Japanese bank funding a US subsidiary needs dollars now.
- **Dollar funding is constrained.** Banks' dollar liabilities exceed their dollar assets; they're unwilling to part with dollars.
- **Balance-sheet costs are high.** Post-2008 regulations ([Basel III](/capital-adequacy/), leverage ratios) make swap intermediation expensive, especially for risky counterparties.
- **Safe-haven demand spikes.** In crises, the dollar becomes refuge; the basis turns very negative.

## Reading Positive and Negative Signals

A **negative basis**—common in the dollar—tells you that non-dollar borrowers are willing to pay a premium to access dollars via the swap market. It signals genuine scarcity.

A **positive basis** suggests the opposite: the currency is abundant relative to funding need. The Swiss franc, for example, often trades with a positive basis because Swiss exporters generate franc earnings and don't urgently need francs.

The basis is also forward-looking. Before the 2008 crisis deepened, the dollar basis began to collapse. Traders saw dollar demand rising and priced it in before it became obvious.

## Why the Basis Persists (and Why It Violates Theory)

Classical CIP says arbitrage should eliminate basis gaps instantly. But modern cross-currency swap markets face real constraints:

**Counterparty risk.** The [swap](/swap/) counterparty—often a bank—can default. A borrower paying 2.50% in dollars accepts [credit risk](/credit-risk/); theory assumes risk-free rates.

**Balance-sheet arbitrage limits.** Intermediary banks have [leverage ratios](/leverage-ratio-forex/) and [risk-weighted assets](/risk-weighted-assets/) caps. Even if a swap is profitable in isolation, the capital it consumes may be too costly relative to profit.

**Regulatory charges.** Clearing requirements and [capital adequacy](/capital-adequacy/) rules make intermediation expensive for marginal trades.

**Term mismatch.** A one-year swap quotes differently than a five-year swap. The basis varies across the [yield curve](/yield-curve/).

Together, these frictions create a band within which the basis can drift without triggering full arbitrage. This band has widened significantly since 2008.

## Monitoring the Basis in Practice

Market participants watch the basis constantly:

- **Funding managers** use it to decide whether to raise dollars directly or via the swap route.
- **Corporate treasurers** compare the all-in cost of borrowing foreign currency and swapping versus direct dollar issuance.
- **Macro traders** watch for basis spikes as signals of funding stress; a sharp negative dollar basis often precedes broader market turmoil.
- **Central banks** intervene in swap markets during crises to ease dollar funding—the Federal Reserve's standing [repurchase agreement](/repurchase-agreement/) facility and bilateral swap lines with foreign central banks are designed partly to flatten the basis.

The basis is quoted in basis points and tracked in real time across multiple platforms. A widening basis warns of imbalance; tightening signals relief.

## The Basis and Systemic Risk

The cross-currency swap basis is more than a pricing oddity—it's a window into global dollar supply dynamics. When it turns sharply negative, it flags that offshore dollar funding is tight. This can presage broader stress: if foreign banks and corporates can't easily get dollars, capital flows tighten, and [volatility](/historical-volatility/) rises.

During the COVID-19 panic in March 2020, the dollar basis plummeted. The Fed rapidly widened its swap lines, and the basis recovered. The episode underscored that when the basis breaks, policy makers treat it as a systemic issue.

## See also

<div class="wiki-seealso">

### Closely related

- [Swap](/swap/) — fundamental mechanics of interest rate and currency swaps
- Covered interest parity — the theoretical relationship the basis measures against
- [Counterparty risk](/counterparty-risk/) — key reason basis deviates from theory
- [Interest rate swap](/interest-rate-swap/) — domestic version; basis analogue exists but is smaller
- [Repurchase agreement](/repurchase-agreement/) — related funding mechanism and alternative to swaps

### Wider context

- [Federal Reserve](/federal-reserve/) — intervention tool in dollar funding crises
- [Central bank](/central-bank/) — role in managing cross-currency funding
- [Leverage ratio](/leverage-ratio-forex/) — regulatory constraint driving basis persistence
- [Risk-weighted assets](/risk-weighted-assets/) — another capital constraint on intermediaries
- [Systemic risk](/systemic-risk/) — why the basis matters beyond traders

</div>
