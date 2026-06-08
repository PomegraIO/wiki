---
title: "Clearing vs Settlement: What Is the Difference"
description: "Clearing and settlement are two distinct post-trade steps: clearing nets and guarantees obligations; settlement delivers cash and securities."
keywords:
  - clearing vs settlement
  - difference between clearing and settlement
  - clearing house
  - securities settlement
  - post-trade processing
  - counterparty risk
image: /svg/markets.svg
---

*The **difference between clearing and settlement** is that clearing is when a third party (the clearinghouse) nets trades, becomes the counterparty to both sides, and guarantees performance; settlement is when cash and securities actually change hands. Clearing happens nearly instantly; settlement typically takes one or two business days.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Clearing vs Settlement — key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for market mechanics." />

<div class="wiki-infobox-caption">Two consecutive steps that together transform a trade into a final delivery.</div>

|   |   |
|---|---|
| **Clearing** | Netting, novation, and guarantee of trade obligations |
| **Settlement** | Physical or electronic delivery of cash and securities |
| **Timing** | Clearing is near-instant; settlement is T+1 or T+2 |
| **Clearinghouse role** | Interposing itself as counterparty; managing risk |
| **Settlement agent role** | Holding assets; executing the actual transfer |
| **Counterparty risk** | Eliminated by clearing; final transfer managed by settlement |
| **Common systems** | DTCC (U.S. equities), Eurex, LCH (interest rates/FX) |

</aside>

## The single trade becomes two

When you buy 100 shares from another trader, you don't actually trade directly. Instead, your broker trades on your behalf with a broker on the other side. At that instant, two separate obligations exist: you owe cash; the seller owes shares. This is where clearing enters.

The clearinghouse steps between them. It becomes the buyer to every seller and the seller to every buyer. In doing so, it eliminates bilateral [counterparty risk](/counterparty-risk/)—you no longer have to worry that the person who sold you shares will fail to deliver. The clearinghouse guarantees both sides of every transaction it clears, backed by financial safeguards and access to central bank liquidity.

This transformation is called **novation**. Your original contract with the seller is torn up and replaced with two new contracts: you buy from the clearinghouse; the seller sells to the clearinghouse. The clearinghouse then nets all trades across the market—if you bought 100 shares and also sold 100 shares on the same day, the clearinghouse may cancel both out and owe you nothing.

## Netting reduces the flow of cash and securities

Without clearing and netting, imagine a [stock exchange](/stock-exchange/) where 10,000 trades happen daily. Each trade would require a separate settlement of cash and shares between buyer and seller. The volume of physical transfers and payment instructions would be staggering. Instead, netting consolidates them.

If Trader A buys 500 shares at $50 and sells 300 shares at $52 on the same day, the clearinghouse nets them: Trader A owes 200 shares net and receives a net payment. This massive simplification keeps the financial plumbing from exploding. For large derivatives dealers, netting across hundreds of daily trades cuts settlement volumes by 80–90%.

## Settlement is the actual handoff

Clearing happens almost instantly when the trade is executed. Settlement is the following step: the actual movement of cash from buyer to seller and securities from seller to buyer. In most U.S. equity markets, settlement occurs on **T+2** (two business days after the trade), though some securities markets operate on T+1.

Settlement involves:

- **The buyer's bank** sending cash to the clearinghouse or settlement agent.
- **The seller's bank** sending securities (via electronic registration or book entry) to the clearinghouse or settlement agent.
- **The settlement agent** (often a subsidiary of the clearinghouse, like the Depository Trust Company in the U.S.) holding the assets briefly and confirming that both sides have delivered.
- **Final transfer:** Cash goes to the seller's account; securities appear in the buyer's account.

Throughout settlement, the clearinghouse's guarantee is still active. If either side fails to deliver, the clearinghouse steps in to find replacement securities or cash at its own risk.

## Why two steps instead of one?

A natural question: why not combine clearing and settlement? Why not have the buyer and seller transfer cash and securities on the same day in one step?

The answer lies in feasibility and risk management. Clearing must happen instantly (or within seconds) to provide market participants with certainty that their trade is locked in. Settlement, by contrast, requires time. Banks and custodians need a day or two to verify balances, confirm instructions, and actually move large quantities of cash and securities across accounts and borders.

More fundamentally, clearing is about **novation and guarantee**; settlement is about **execution**. The clearinghouse can guarantee performance almost immediately because it can borrow cash or securities if needed and rely on its members' capital cushions. But it cannot guarantee physical delivery until the wheels of settlement are actually turning.

## Collateral and margin during the gap

Between clearing and settlement, participants post **margin** (collateral) to the clearinghouse. This margin acts as a buffer: if a member defaults, the clearinghouse can seize the margin and use it to cover losses. For exchange-traded derivatives (futures, options), variation margin changes hands daily to reflect mark-to-market moves. For equities, initial margin is typically collected at clearing; additional margin may be called if prices move against a position.

This margin framework is how the clearinghouse finances its risk guarantee. It's also why clearing provides such powerful protection—the threat of margin calls and default penalties keeps market participants disciplined.

## Different clearinghouses for different assets

Not all trades clear through the same house. U.S. equities clear through the **National Securities Clearing Corporation (NSCC)**, part of the Depository Trust Company. Interest-rate [swaps](/swap/) and many other derivatives clear through the **Intercontinental Exchange (ICE)** or **LCH Group**. **Eurex** handles European equities and derivatives. Each clearinghouse manages its own member base, margin rules, and settlement procedures, though all follow similar principles: novation, netting, and guarantee.

## The role of the settlement agent

Once clearing is done, a separate entity—often called the settlement agent or depository—takes over to execute the mechanics of settlement. In the U.S., the **Depository Trust Company (DTC)** is the primary settlement agent for equities and corporate bonds. It holds securities in "book entry" form (meaning they exist as electronic entries, not physical certificates) and coordinates the transfer between broker accounts.

Settlement agents maintain accounts for all [custodians](/custodian/) and brokers involved in the trade. When settlement arrives, they debit the buyer's account (removing cash) and credit the seller's account (adding cash); they do the opposite for securities.

## Risk reduction in numbers

The clearinghouse's guarantee is backed by:

- **Member capital:** Each clearinghouse member must maintain minimum capital reserves. A typical clearinghouse requires $10–100 million per member depending on activity.
- **Guaranty fund:** Clearinghouse members also contribute to a shared fund that can cover losses if one or more members default.
- **Insurance and credit lines:** Most major clearinghouses also carry insurance and maintain credit lines with central banks.

Because of these safeguards, the default of a clearing member is extraordinarily rare. The last major instance in the U.S. was in 1987, and even then the clearinghouse protected the counterparties.

## T+2 and beyond

Until 2024, most U.S. equities cleared T+2 and settled T+2. Regulators have been pushing for faster settlement (T+1 or even same-day) to reduce counterparty risk and unlock capital more quickly. The U.S. began transitioning to T+1 settlement in 2024. The motivation is simple: the shorter the window between trade and settlement, the lower the risk that one party defaults before the final handoff.

## When clearing and settlement misalign

In normal markets, clearing and settlement work smoothly. But during stress—market crashes, liquidity crises, or participant failures—gaps appear. For instance, if a major derivatives dealer defaults after clearing but before settlement, the clearinghouse must find replacement counterparties to offset the defaulter's positions. This is expensive and can take days. Regulators require clearinghouses to run "stress tests" to ensure they can handle multiple simultaneous member defaults.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty Risk](/counterparty-risk/) — The credit risk that clearing eliminates
- [Custodian](/custodian/) — The entity holding securities for settlement
- [Stock Exchange](/stock-exchange/) — Where trades originate before clearing
- [Central Bank](/central-bank/) — Lender of last resort to clearinghouses during stress
- [Margin Call Forex](/margin-call-forex/) — How collateral works during the clearing window

### Wider context

- [Swap](/swap/) — A derivative asset class that clears and settles differently than equities
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulates clearinghouses and settlement timelines
- [Systemic Risk](/systemic-risk/) — Why fast, reliable clearing is critical to financial stability

</div>
