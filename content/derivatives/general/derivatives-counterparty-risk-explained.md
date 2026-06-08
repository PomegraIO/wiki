---
title: "Counterparty Risk in Derivatives Explained"
description: "How counterparty risk in derivatives arises between OTC parties, how credit valuation adjustment (CVA) measures it, and how collateral, netting, and clearing reduce it."
keywords:
  - counterparty risk derivatives
  - credit valuation adjustment
  - otc derivatives default risk
  - derivative collateral agreements
image: /svg/derivatives.svg
---

*In **counterparty risk in derivatives**, one party worries that the other will default and leave them unable to unwind a losing position. This risk exists for both parties simultaneously—the winner and loser on any given trade—and is priced into derivatives via a credit adjustment spread called CVA. The tools to manage it include collateral agreements, netting, and central clearinghouses.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Counterparty Risk — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Risk that the other party in a derivatives contract defaults before settlement.</div>

|   |   |
|---|---|
| **Nature** | Two-sided: both long and short are exposed |
| **Measurement** | Credit valuation adjustment (CVA) as a spread |
| **Peak exposure** | When the derivative is most profitable to you |
| **Main mitigant** | Collateral posted by both parties |
| **Secondary control** | Netting agreements and central clearing |

</aside>

## How Counterparty Risk Arises in Over-the-Counter Derivatives

When you buy a [forward contract](/forward-contract/), [interest rate swap](/interest-rate-swap/), or other custom derivative from a dealer, you're entering into a bilateral agreement with no central intermediary. The dealer is your counterparty. If the derivative moves in your favor—say, you locked in a favorable rate and rates fall further—the dealer owes you money. But if the dealer defaults, you lose that claim and must enter a new trade at worse rates to replace your hedge.

The subtlety: risk is two-sided. If the trade moves against you, your dealer is the creditor exposed to *your* default. Neither party is risk-free. A bank quoting you a five-year swap is not just guessing future rate moves; it's also pricing in the probability that you, the counterparty, might go bust before the final payment.

Before central clearing became standard, large dealers carried billions in potential counterparty exposure. The 2008 financial crisis exposed how tightly these webs were woven: when Lehman Brothers collapsed, counterparties across markets found themselves holding derivative claims on a failed entity. That shock prompted regulators to mandate clearing for standardized derivatives and tighter collateral rules for the rest.

## Measuring Risk with Credit Valuation Adjustment

Banks price counterparty risk using a metric called **credit valuation adjustment (CVA)**. It is the credit spread—the extra return—the dealer demands to compensate for the risk that you default. Think of it as an insurance cost.

CVA depends on three factors:

1. **Probability of default**: Inferred from the counterparty's credit rating, bond yields, or credit default swap spreads.
2. **Exposure at default**: The mark-to-market value of the derivative when default occurs. A swap worth $10 million is a larger exposure than one worth $1 million.
3. **Loss given default**: The fraction of exposure not recovered through bankruptcy proceedings or collateral sales. High-quality collateral reduces this sharply.

For a long derivative position (you're owed money if rates move in your direction), your maximum exposure grows when the underlying rates move your way. A bank might compute CVA by projecting forward the possible future values of the derivative at each date and weighting by the counterparty's default probability in that period. The wider the default probability, or the higher the expected positive exposure, the larger the CVA spread.

In practice, CVA is dynamically hedged. A dealer who has written you a swap will often enter an offsetting swap with another dealer, or buy protection via a [credit default swap](/credit-default-swap/), to cap its net exposure to you. That hedge has its own cost, which gets baked into the derivative's price.

## Collateral Agreements and Bilateral Netting

The primary tool to reduce counterparty risk is collateral. Most OTC derivatives are now governed by an International Swaps and Derivatives Association (ISDA) Master Agreement, which includes a Credit Support Annex (CSA). The CSA specifies:

- **Daily mark-to-market settlement**: The losing party posts cash or securities equal to the change in the derivative's value each day.
- **Threshold amounts**: Small changes don't trigger a margin call; only moves beyond an agreed threshold do.
- **Eligible collateral**: Usually Treasury bonds, highly rated corporate bonds, or cash.
- **Haircuts**: Illiquid collateral might be discounted by 5–20% to account for fire-sale risk.

For example, if you're long a five-year swap that rises in value by $500,000 overnight (because rates fell), the dealer posts $500,000 or equivalent securities to you. If it falls $400,000, you post to them. This daily settling shrinks the peak exposure to a couple of days' worth of market moves—far below the notional amount.

Netting amplifies this protection. If you have ten swaps with the same counterparty—five in which you're owed money and five where you owe—most CSA agreements allow you to net them. Your exposure to them becomes the net value across all ten, not the sum of the five where you win. This is massive: it can cut exposure by 50–90% for active dealers.

## Central Clearing and Standardized Derivatives

For standardized derivatives traded on exchanges—[futures contracts](/futures-contract/), listed options, exchange-traded swaps—central counterparties (CCPs) like the Depository Trust & Clearing Corporation (DTCC) sit in the middle. The CCP becomes the buyer to every seller and the seller to every buyer. Your counterparty is no longer the dealer; it's the CCP.

This eliminates bilateral counterparty risk *between you and the dealer*. Instead, you face *CCP credit risk*—the chance the CCP fails. But CCPs are heavily capitalized, backed by government safeguards, and are typically safer than any single dealer. They also use:

- **Variation margin** (daily settling, like CSA).
- **Initial margin** (a reserve posted upfront, sized to cover mark-to-market moves over a few days even if the counterparty defaults).
- **Mutualized default funds** (if a CCP member blows up, other members contribute to cover the loss before the CCP's own capital is tapped).
- **Mandatory novation rules** (all standardized derivatives must be cleared, eliminating the option to settle bilaterally).

Central clearing reduces but does not eliminate counterparty risk; it redistributes it and shrinks it. Dealers still face each other on bespoke OTC swaps, which remain bilateral.

## Why Peak Exposure Matters

A critical insight: your counterparty exposure on a derivative is not constant. It peaks when the derivative's value is most favorable to you.

For a long forward contract on crude oil, your exposure to the dealer is highest when oil prices have spiked. You're owed millions, and the dealer might default at the worst moment. Conversely, when oil prices have plummeted and you're underwater, your exposure to the dealer is near zero—they're the creditor, not you.

Banks use "peak exposure" scenarios in stress tests. They compute the 95th or 99th percentile future value of each derivative under adverse moves in rates, currencies, or commodities, then sum across all contracts with each counterparty, applying netting and haircuts. That peak figure drives capital reserve requirements and collateral demands.

For exotic derivatives—say, a barrier option or swaption—the exposure profile can be complex. You might be slightly owed money early in the contract's life, with exposure exploding years out if volatility spikes. Risk managers must plot these profiles carefully.

## Impact on Pricing and Available Terms

Counterparty risk is a real economic cost. A dealer will quote a tighter spread (higher rate, lower price) to a creditworthy counterparty and a wider spread to a weaker one. A AA-rated corporation might get a swap rate 5 basis points tighter than a BB-rated peer on the same underlying.

In periods of financial stress, CVA can spike. During the 2008 crisis, dealers demanded enormous spreads because uncertainty about counterparty survival was acute. The inability to sell derivatives or roll them over led to forced liquidations and cascading losses.

For retail traders, counterparty risk is usually immaterial because they don't post collateral bilaterally; they trade through brokers and exchanges with central clearing. But for large institutions, funds, and corporations entering bespoke OTC derivatives, understanding CVA and collateral is non-negotiable to negotiation of contract terms.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate Swap](/interest-rate-swap/) — the most common OTC derivative and a key source of counterparty exposure for banks and corporations
- [Credit Default Swap](/credit-default-swap/) — a tool banks use to hedge counterparty risk on other derivatives
- [Forward Contract](/forward-contract/) — a simple bilateral derivative with peak exposure at maturity
- [Futures Contract](/futures-contract/) — exchange-cleared alternative that eliminates bilateral counterparty risk
- [Credit Rating](/credit-rating/) — the input used to estimate a counterparty's default probability and CVA

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — the broader framework of using derivatives to manage financial risk
- [Counterparty Risk](/counterparty-risk/) — general definition and role across financial markets
- [Dodd-Frank Act](/dodd-frank-act/) — the post-2008 regulation that mandated clearing and margin for standardized derivatives

</div>
