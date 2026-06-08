---
title: "Total Return Swap vs Credit Default Swap"
description: "Total return swaps transfer all economic exposure to an asset; credit default swaps transfer only credit risk. The choice between them determines whether you hedge price risk, default risk, or both."
keywords:
  - total return swap vs credit default swap
  - total return swap cds difference
  - credit default swap vs total return
  - hedging credit vs price risk
  - swap structures comparison
---

*When you own a risky bond or loan and want protection, you must choose between two instruments: a **total return swap** transfers all economic risk (price, credit, currency, duration) to a counterparty; a **credit default swap** transfers only the credit risk. The decision hinges on whether you are hedging against the bond falling in value, defaulting, or both.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">TRS vs CDS — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Two instruments, one goal—different risks transferred to different buyers.</div>

|   |   |
|---|---|
| **Total Return Swap (TRS)** | Payer transfers 100% of asset returns (price + yield); receiver bears mark-to-market risk |
| **Credit Default Swap (CDS)** | Payer transfers only [credit risk](/credit-risk/); receiver paid only on default or credit event |
| **Price/duration risk** | TRS hedges it; CDS does not (you keep mark-to-market exposure) |
| **Credit risk** | Both hedge it, but CDS is pure credit; TRS is bundled with price |
| **Typical user** | TRS: hedge fund wanting to short synthetically; investor wanting full cash flow transfer |
| **Typical user** | CDS: bond investor accepting mark-to-market but buying default protection |
| **Upfront cost** | TRS: financing spread (LIBOR+X); CDS: quoted as basis points per year |
| **Counterparty risk** | Both; TRS exposes you if payer defaults; CDS exposes you if protection seller fails |

</aside>

## Total Return Swap: Full Economic Transfer

A [total return swap (TRS)](/swap/) is a contract where one party (the receiver of total return) transfers all economic exposure of an asset to the other party (the payer of total return). The receiver keeps the asset on their balance sheet but economically has sold it. The payer economically owns the asset but never takes physical possession.

Here is how it works in practice. Suppose you own a $10 million loan to a borrower rated BB+, and you worry that the market might mark it down if the company's credit deteriorates. You enter a one-year TRS:

- **You (receiver of TRS):** you own the loan and continue collecting interest.
- **Payer (counterparty bank or investor):** pays you LIBOR + 200 basis points (the financing cost), and you pay the payer the total return on the loan.

At the end of the year, if the loan still trades at par, you net out even—you've paid LIBOR+200 and received the loan's interest, which is roughly the same. But if the loan has fallen to $9.5 million (marking down 5%), you pay the payer an additional $500,000, and they pay you in full. The net effect is that the payer bears the $500,000 loss.

Conversely, if the loan rises to $10.5 million, you collect the $500,000 gain from the payer. Every dollar of price movement flows to the payer; you are hedged.

This is why TRS is the instrument of choice for hedge funds shorting credit. A hedge fund that believes a BB+ loan is mispriced and will fall 10% can enter a TRS as a receiver, paying financing costs and receiving the loan's total return. If the loan falls, the payer's loss is the fund's gain. No short selling required; no need to borrow the loan; just a bilateral swap.

## Credit Default Swap: Credit Risk Only

A [credit default swap (CDS)](/credit-default-swap/) is narrowly designed to transfer only [credit risk](/credit-risk/). The buyer of protection pays an annual fee (quoted in basis points, e.g., 150 bp = 1.5% per year) to the seller. If a credit event occurs—typically defined as default, restructuring, or bankruptcy—the seller pays the buyer the loss.

Using the same $10 million BB+ loan example, suppose you buy one-year CDS protection at 150 basis points:

- **You pay:** $150,000 per year to the CDS seller.
- **You receive:** If the borrower defaults and recovers only 40 cents on the dollar (a 60% loss), the CDS seller pays you $6 million.
- **Net:** You own the loan, collect its interest (say, 6%), and pay the CDS premium (1.5%). Your net yield is 4.5%, and you are protected against default.

Critically, if the loan simply marks down 5% due to credit-rating pressure, tightening spreads, or sentiment—but does not default—the CDS seller pays you nothing. You still own a $9.5 million loan. The CDS hedges only the default event, not the mark-to-market loss.

## Key Differences Summarized

| Dimension | TRS | CDS |
|-----------|-----|-----|
| **What is hedged** | All price and yield changes | Only credit events (default, restructure, etc.) |
| **Protection triggers** | Immediately on any mark-to-market move | Only on credit event or default |
| **Cost** | Financing spread (LIBOR+X), varies with asset and duration | Fixed bp/year, varies with credit quality |
| **Balance sheet** | Receiver keeps asset but transfers economic risk | Buyer keeps asset and economic upside; seller bears credit loss only |
| **Use case** | Synthetic short; leverage play; hedge for mark-to-market volatility | Default protection; risk transfer without losing upside |
| **Who uses it** | Hedge funds, dealers, banks using loans/bonds as collateral | Bond investors, loan syndicators, risk managers |

## When to Choose TRS

A total return swap is the right tool when:

- **You want to shed all economic exposure.** You own an asset but do not want any mark-to-market or credit risk. TRS transfers both instantly.
- **You are managing a short position.** Shorting a bond or loan outright is costly (borrow it, post collateral, manage fails). A TRS as receiver mimics a short with less friction.
- **You are hedging valuation drift.** If your accounting or risk system marks a portfolio daily, TRS protects you from end-of-day mark-to-market swings that you do not want to pass through.
- **You want financing.** The payer of a TRS is implicitly financing your asset purchase. If you cannot borrow the cash, a TRS lets you own the asset's yield without capital.

The downside: TRS is typically available only to institutional counterparties (banks, hedge funds, large investors). You need a dealer willing to quote it. Also, you still bear [counterparty risk](/counterparty-risk/)—if the payer defaults, you lose protection and regain the asset's full risk.

## When to Choose CDS

A credit default swap is the right tool when:

- **You accept mark-to-market risk but fear default.** You own a high-yield bond and can tolerate a 10% price move if spreads widen, but not a 50% loss from default. CDS covers the tail.
- **You want to preserve upside.** A bond might offer fat coupons and capital appreciation if credit improves. CDS protects downside while keeping upside. TRS hedges the upside away.
- **You need simple execution.** CDS is standardized (single-name, index, tranched). Bid-ask spreads are tighter. You can get a quote in seconds.
- **You are a debt capital markets participant.** Loan syndicators, CLO managers, and structured product issuers routinely use CDS to hedge portfolio credit risk. It is the industry standard.

The catch: CDS does not protect you from mark-to-market volatility. If your bond falls from par to $95 due to spread widening, and no default has occurred, CDS will not compensate you. You have a floating unrealized loss on the bond itself.

## Basis Risk and Practical Differences

In theory, owning a bond and buying CDS protection should behave like owning a risk-free bond (yielding LIBOR or the risk-free rate). In practice, the "basis"—the difference between the bond's spread and the CDS premium—widens and narrows, creating a basis trade.

A hedge fund might buy a bond, short it via CDS, and pocket the basis if it converges. But if basis diverges, the fund loses money even though the credit has not moved.

TRS has no basis risk in the same way, because the TRS payer's return equals the asset's total return. But TRS introduces [counterparty risk](/counterparty-risk/)—the payer's creditworthiness becomes your new risk.

## Regulatory and Collateral Dynamics

Since the 2008 financial crisis, central clearing for CDS has improved transparency and reduced dealer-side concentration risk. Most single-name CDS on major corporates clear through central counterparties (CCPs), which means variation margin is exchanged daily and counterparty risk is mitigated.

TRS remains largely bilateral and uncleared, so you and your counterparty exchange collateral manually, and you bear greater counterparty risk if the payer defaults. However, TRS is more flexible and can be tailored to any underlying asset.

## Real-World Example: The Choice

Imagine you syndicated a $50 million loan to a mid-market company rated BB. You want to hedge your credit exposure. You can:

**Option A: Sell via TRS.** Find a hedge fund or bank willing to pay LIBOR+180bp to receive the loan's total return. You transfer the loan economically for one year. You keep the asset on the balance sheet but have no credit or price risk. The counterparty gets the economics.

**Option B: Buy CDS.** Pay 120bp per year to a CDS seller. You keep the loan, collect the interest (say 5%), and if the company defaults, the CDS seller covers your loss. If the company's rating improves and the loan trades up to 102, you keep the gain and continue to own it.

In Option A, you are out of risk entirely but have counterparty risk to the TRS payer. In Option B, you keep upside but pay CDS premium and retain mark-to-market drawdown risk.

The choice depends on whether you believe the credit will improve (favor CDS) or you want to free up capital and risk budget (favor TRS).

## See also

<div class="wiki-seealso">

### Closely related

- [Credit Default Swap](/credit-default-swap/) — the pure credit hedge
- [Swap](/swap/) — the broader instrument category
- [Total Return Swap](/total-return-swap/) — the full-economic-risk hedge
- [Credit Risk](/credit-risk/) — what both instruments transfer
- [Counterparty Risk](/counterparty-risk/) — the hidden risk in both
- [Interest Rate Swap](/interest-rate-swap/) — a related swap structure

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — why these instruments exist
- [Basis Risk](/basis-risk/) — why CDS and bond spreads diverge
- [Corporate Bond](/corporate-bond/) — the typical underlying of CDS and TRS
- [High Yield Bond](/high-yield-bond/) — where CDS is most active
- [Securitization](/securitization/) — where TRS is used to transfer asset cash flows
- [Credit Rating](/credit-rating/) — how credit quality drives CDS pricing

</div>
