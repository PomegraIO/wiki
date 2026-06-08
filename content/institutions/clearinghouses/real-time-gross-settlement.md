---
title: "Real-Time Gross Settlement"
description: "Payment architecture that settles each transaction individually and immediately, eliminating intraday credit risk between payer and the system."
keywords:
  - real-time gross settlement
  - rtgs
  - payment system
  - settlement finality
  - intraday credit
  - central bank money
image: /svg/institutions.svg
---

*A **real-time gross settlement** (RTGS) system settles payment transactions one at a time, as they arrive, using [central bank money](/central-bank/). When you send a payment via an RTGS system, it is final and irrevocable the moment it leaves your account; the recipient's account is credited immediately. Contrast this with batch clearing systems, which hold transactions for hours and process them in bulk. RTGS eliminates the intraday credit risk that arises when transactions are pending.*

The word "gross" is crucial. A typical bank-to-bank payment is gross—the full amount is transferred—not netted against other payments. The moment a transaction is settled, it is final. No recall, no reversal (unless both parties explicitly agree later). This finality is expensive to achieve in real time, which is why RTGS systems are used only for the highest-value, most time-sensitive payments: [central bank](/central-bank/) operations, large interbank transfers, and securities settlement.

## Intraday credit and why real-time matters

Before RTGS, most payments were settled in batches. A bank would collect outgoing payments throughout the day and submit them to a clearing house in bulk at 3 p.m. The clearing house would net them, calculate each bank's position, and settle the next morning using overnight credit lines. During that gap, every bank ran a credit exposure: a sender had sent money but the recipient had not yet received it. If a bank failed before settlement, these intraday exposures could default.

RTGS eliminates that window. When Bank A sends $1 million to Bank B:
1. Bank A's [central bank](/central-bank/) account is debited immediately.
2. Bank B's central bank account is credited immediately.
3. The payment is final and irrevocable.

There is no intermediate state in which the money is "in transit" and unsettled. This removes systemic risk: a bank cannot fail and strand billions in intraday exposures.

## How RTGS systems work

An RTGS system is typically operated by the central bank itself. It maintains real-time accounts for thousands of financial institutions—mostly banks but also brokers, custodians, and other large intermediaries. These accounts are denominated in central bank money (the currency itself, not a bank deposit). 

When a payment arrives, the system checks whether the sender has sufficient funds. If yes, it debits the sender's account and credits the receiver's account, both in real time. If no, it queues the payment (in some systems) or rejects it, depending on the rules.

The central bank effectively becomes the counterparty to every transaction. Banks do not settle directly with each other; they settle with the central bank. This makes the central bank responsible for guaranteeing payment integrity—a function central banks treat with extreme seriousness.

## The cost of real-time finality

RTGS systems are expensive to run and to participate in. A bank must maintain a sufficient balance at the central bank to cover outgoing payments, which means keeping idle cash reserves rather than deploying them in lending or investments. For a global bank making thousands of payments per day, this can mean tens of millions in central bank deposits sitting unused.

To reduce this cost, most RTGS systems implement **liquidity-saving mechanisms**. One common approach is **netting windows**: the system holds payments for a brief window (a few seconds to a few minutes), searches for offsetting payments, and settles the net position in real time. This preserves finality (within the window) while reducing the amount of central bank balance required.

Some RTGS systems also enable intraday credit lines: a bank can temporarily have a negative balance if it has pre-arranged credit with the central bank. The bank must repay by the end of the day, but this allows smoother management of intraday liquidity.

## RTGS and securities settlement

RTGS is particularly important in securities settlement because it is coordinated with [delivery versus payment](/delivery-versus-payment/). When a security is sold, the seller requires simultaneous transfer of cash and the buyer requires simultaneous transfer of the security. If the [central securities depository](/central-securities-depository/) debits the seller's securities account but the RTGS system has not yet credited the seller's cash account, the seller is at risk.

Most modern securities markets use **synchronised settlement**: the [CSD](/central-securities-depository/) and the RTGS system communicate in real time, ensuring both legs settle together. If one leg fails, both are reversed. This requires tight integration between the CSD and the RTGS operator (typically the central bank).

## Global variation in RTGS design

Different central banks operate RTGS systems with distinct architectures. The US Federal Reserve operates **Fedwire**, which settles payments throughout the business day with continuous real-time settlement. The European Central Bank operates **TARGET2**, which is a pan-European system connecting national RTGS systems. Japan's **BOJ-NET** settles JGP payments, and so on.

These systems differ in the degree of netting allowed, the availability of intraday credit, the pricing model, and the scope of eligible participants. But the core principle—settlement finality in real time—is universal.

## RTGS and retail payments

RTGS systems traditionally settled only large-value interbank payments. But in recent years, central banks have extended RTGS to retail payments, enabling faster consumer transfers. In some markets, payments now settle in seconds or minutes rather than days. The UK, the EU, and others have established **fast payment systems** that use RTGS principles for retail-scale transfers.

This shift has major implications for banking and payments. If all payments are settled in real time with finality, the incentive to maintain large settlement buffers vanishes, and the opportunity for overnight credit diminishes. Banks must adjust their liquidity management and capital structures accordingly.

## Regulation and oversight

RTGS systems are regulated as critical financial infrastructure. The Bank for International Settlements (BIS) and the [International Organization of Securities Commissions](/iosco/) (IOSCO) jointly set the **Principles for Financial Market Infrastructures** (PFMI), which establish standards for RTGS design, risk management, and operational resilience.

Most central banks operate their RTGS systems with redundancy, encryption, and extensive testing to prevent outages. A failure of an RTGS system can grind derivatives settlement or foreign exchange settlement to a halt; the systemic importance is obvious.

## See also

<div class="wiki-seealso">

### Closely related

- [Central Bank](/central-bank/) — operates the RTGS system and maintains the accounts
- [Delivery Versus Payment](/delivery-versus-payment/) — settlement principle coordinated with RTGS
- [Central Securities Depository](/central-securities-depository/) — institution that synchronises with RTGS to settle securities and cash together
- Settlement Infrastructure — broader ecosystem of which RTGS is the core payment layer
- [Multilateral Netting](/multilateral-netting/) — CCP process that reduces RTGS volumes
- Payment System — broader category that includes RTGS

### Wider context

- Systemically Important Institution — RTGS operators are designated as such
- [Liquidity Risk](/liquidity-risk/) — RTGS design trades off finality against intraday liquidity cost
- [Counterparty Risk](/counterparty-risk/) — eliminated by real-time settlement
- Securities Settlement — primary use case for RTGS systems

</div>
