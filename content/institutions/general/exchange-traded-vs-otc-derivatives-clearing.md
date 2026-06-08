---
title: "Exchange-Traded vs OTC Derivatives Clearing"
description: "How exchange-traded and OTC derivatives clear differently through central counterparties, affecting counterparty risk and transparency."
keywords:
  - exchange-traded derivatives clearing
  - otc derivatives clearing
  - central counterparty risk
  - derivatives settlement
  - counterparty risk management
  - ccp clearing
image: "/svg/institutions.svg"
---

*The mechanism by which a derivative contract settles — whether it clears automatically through a central counterparty (CCP) or remains a bilateral obligation — fundamentally alters how the two parties manage default risk and regulatory scrutiny. **Exchange-traded vs OTC derivatives clearing** represents the divide between the visible, backstopped market and the opaque, bilateral one.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Exchange-Traded vs OTC Clearing — Key Facts</div>

<img src="/svg/institutions.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">One clears automatically; the other may not clear at all.</div>

|   |   |
|---|---|
| **Exchange-traded** | Clears through a mandatory CCP; both parties protected by margin and insurance |
| **OTC (pre-2008)** | Bilateral only; counterparty risk between dealer and client sits unhedged |
| **OTC (post-2008 rules)** | Standardized swaps mandated to a CCP; bespoke deals remain bilateral |
| **CCP role** | Becomes the buyer to every seller; absorbs counterparty default through default fund |
| **Margin requirement** | Exchange-traded: daily mark-to-market; OTC cleared: variation margin, initial margin |
| **Transparency** | Exchange: price and volume public; OTC: bilateral negotiation, limited disclosure |
| **Cost difference** | CCP clearing adds fees; bilateral OTC may be cheaper upfront but riskier |

</aside>

## The core difference: who stands in the middle

When you buy a futures contract on an exchange, your broker's clearinghouse steps between you and the seller. You never actually owe the seller money; you owe the clearinghouse, and the seller collects from the clearinghouse. If the seller defaults, the clearinghouse absorbs the loss using the seller's margin deposit and, if needed, a mutualised default fund. You are shielded.

In bilateral OTC markets before clearing mandates, a bank might sell you a custom interest-rate swap with a five-year maturity. No intermediary stood between you. If the bank failed before the contract expired, you could lose your entire unrealised gain on that swap — or be forced to replace it at much worse terms. The bank, in turn, bore your default risk.

This distinction shaped two parallel financial systems: one visible and risk-managed, one opaque and concentrated.

## Why exchange clearing emerged

Centralised clearing developed because bilateral risk is expensive and fragile. In the 1980s and 1990s, each major dealer maintained a web of derivative exposures to hundreds of counterparties. If one counterparty defaulted, the dealer faced a chain of losses and was forced to cover its own derivatives at market prices — which had often moved against it. Banks kept large [credit-risk](/credit-risk/) reserves against counterparty failure.

A CCP strips out the chain. Instead of tracking exposure to each counterparty, you face only the CCP. The CCP, as a utility, is designed to be bullet-proof: it holds margin from all participants, manages its own default fund, and is often backstopped by the exchange or regulators.

Standardised derivatives — [futures contracts](/futures-contract/), listed options, [index-based swaps](/swap/) — moved to CCP clearing because they had common specifications that a clearinghouse could handle at scale.

## The post-2008 regulatory shift

The 2008 financial crisis exposed the fragility of bilateral OTC derivatives. Lehman Brothers had entered thousands of custom derivatives contracts. Its counterparties could not get out without negotiating with a bankruptcy estate, facing years of delay and uncertainty. The risk was real: Lehman owed and was owed billions across thousands of distinct contracts.

In response, regulators mandated CCP clearing for standardised [interest-rate swaps](/interest-rate-swap/), [credit-default swaps](/credit-default-swap/), and other liquid derivatives. The U.S. Dodd-Frank Act, the European Market Infrastructure Regulation (EMIR), and equivalent regimes globally required that swaps meeting certain liquidity and standardisation thresholds clear through a registered CCP.

Bespoke derivatives — a custom equity derivative, a weather swap, a highly structured cross-currency contract — remained bilateral because no CCP could operate at a loss on non-standard contracts. The solution was compromise: bespoke OTC trades could remain uncleared if the two parties posted sufficient [variation margin](/cash-conversion-cycle/) to each other daily. This way, neither party accumulated large unrealised losses that could trigger a cascade of default.

## How clearing actually works

An exchange-traded derivative clears in near-real time. At the end of each trading day, the clearinghouse marks all positions to market price. If your position loses value, you post additional cash — initial margin plus variation margin — by the next morning or face forced liquidation. If it gains, the clearinghouse credits you.

When a participant defaults, the clearinghouse liquidates its entire portfolio immediately, using its margin deposit to cover any shortfall. If the default is large, the clearinghouse draws from the default fund, which is contributed by all members. In rare cases, surviving members share losses under contractual waterfall rules.

For mandated [clearing via a central counterparty](/counterparty-risk/), bilateral OTC swaps follow a similar process. A swap dealer and client agree on terms, then both parties send the swap to the CCP. The CCP novates the contract — legally replaces the original two-party obligation with two one-party obligations: dealer to CCP, client to CCP. From that moment, the client and dealer no longer owe each other; they each owe the CCP. Variation margin flows daily based on the market value of the swap.

## Remaining bilateral OTC exposure

Not all OTC derivatives clear, and [counterparty risk](/counterparty-risk/) in bilateral derivatives has not disappeared. A bank that is not a major swap dealer may conduct OTC derivatives business in uncleared instruments: exotic equities, commodities swaps, or very bespoke interest-rate structures. These rest on the bank's credit standing and the collateral both parties post to each other.

For bilateral OTC instruments, the regulatory requirement is to post initial and variation margin. But the mechanics are negotiated contract-by-contract. A bank might require a client to post collateral when the swap is underwater (from the bank's perspective), but the client might negotiate a threshold — say, only if the mark-to-market loss exceeds $1 million. This threshold is an area of hidden fragility: if the market moves sharply against the client, the client may be required to post large margin quickly, and if it cannot, the bank has the right to terminate the contract.

## Transparency and pricing

Exchange-traded derivatives trade in the open. Every futures contract price and volume are broadcast to the market. Buyers and sellers see where the market clears, which makes price discovery efficient and fraud harder.

OTC derivatives are priced in bilateral negotiation. A dealer quotes a price to a client; the client negotiates; they agree or move to another dealer. Prices are not visible to the market. This opacity has trade-offs: it allows for customisation and long-term relationship pricing, but it also allows dealers to widen spreads against less-informed clients. The bid-ask spread on a custom OTC swap can be two to three times wider than on an exchange-traded equivalent.

For mandated cleared swaps, regulators now require trade reporting: both parties must report the executed swap to a trade repository within one day. This allows regulators to see systemic concentrations, but the data is not public in real time. Dealers and large asset managers see the flow data; retail investors do not.

## Cost to the end user

CCP clearing is not free. The clearinghouse charges a membership fee and a per-trade fee. For a standardised interest-rate swap, the total fee might be 10 to 50 basis points, depending on volume and the clearinghouse. Over the lifetime of a long-dated swap, this is material.

Bilateral OTC is often cheaper upfront because there is no clearinghouse intermediary. A dealer can quote tighter on an uncleared swap, knowing it avoids CCP fees. The client saves on fees but bears the counterparty risk: if the dealer fails, the client loses unrealised gains.

The choice between exchange-traded (cleared) and uncleared OTC has become less a choice for large institutions and more a regulatory mandate. Standardised derivatives clear because they must. Bespoke derivatives remain bilateral because they cannot clear. Smaller firms and retail investors have essentially no access to uncleared OTC; banks reserve that for institutional clients, where the counterparty risk is both larger in size and acceptable in principle.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty risk](/counterparty-risk/) — the credit exposure created when a party fails to perform on a contract
- [Derivatives hedging](/derivatives-hedging/) — the mechanics and purpose of using derivatives to offset market risk
- [Futures contract](/futures-contract/) — standardised exchange-traded contract that clears daily
- [Credit-default swap](/credit-default-swap/) — an OTC derivative that hedges credit risk and was a key target of clearing mandates
- [Interest-rate swap](/interest-rate-swap/) — most common cleared OTC derivative
- [Dodd-Frank Act](/dodd-frank-act/) — U.S. law that mandated clearing for standardised derivatives

### Wider context

- [Swap](/swap/) — the broad category of OTC derivatives that exchange cash flows
- [Option](/option/) — another class of derivatives that can trade exchange-listed or OTC
- [Broker](/broker/) — the intermediary that executes derivatives trades and holds margin
- [Securitization](/securitization/) — the process by which derivatives sometimes embed other financial instruments
- [Financial crisis](/great-depression/) — the 2008 event that prompted regulatory shifts toward mandatory clearing

</div>