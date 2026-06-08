---
title: "Sovereign CDS Settlement: How Credit Default Swaps Pay Out After a Default"
description: "Sovereign CDS settlement follows ISDA rules: a credit event is declared, the ISDA Determinations Committee meets, and a cash auction determines the recovery payout. This process determines payouts for billions in protection."
keywords:
  - sovereign credit default swap settlement
  - ISDA credit event determination
  - CDS auction mechanism
  - sovereign default CDS payout
  - credit event definition
---

*When a sovereign defaults, holders of [credit default swaps](/credit-default-swap/) on that country do not automatically receive payment. Settlement requires a formal **credit event determination** by the ISDA Determinations Committee, followed by a cash settlement auction that fixes the payout price. This multi-stage process takes weeks and creates a gap between market expectation and actual payment.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Sovereign CDS Settlement — key facts</div>

<img src="/svg/fiscal.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A rules-based process that formalizes whether a default occurred and calculates the cash payout through a binding auction.</div>

|   |   |
|---|---|
| **Trigger** | Failure to pay, debt restructuring, moratorium, or [selective default credit rating](/selective-default-credit-rating/) |
| **Determiner** | ISDA Determinations Committee (16 members: dealers and end-users) |
| **Timeline** | 3–5 business days after event for preliminary discussion; 30–60+ days for final determination |
| **Settlement method** | Cash auction; physical delivery in some older contracts |
| **Payout calculation** | (Par value – Auction settlement price) × Notional protection amount |
| **Reference entity** | Usually the sovereign central government; sometimes specific sub-entities |
| **Market impact** | Auction price discovery helps establish recovery expectations |

</aside>

## What triggers a credit event

The ISDA Master Agreement, used in virtually all [credit default swap](/credit-default-swap/) contracts on sovereigns, defines five potential credit events:

**Payment failure** is the clearest trigger. If a sovereign misses a payment on any material external debt obligation—principal or interest—within a grace period (typically 3 or 30 days, depending on contract terms), a credit event has occurred. A single missed payment on one bond can trigger payout on all CDS contracts on that sovereign.

**Restructuring** is triggered when a sovereign announces that existing creditors must accept new terms—lower coupons, extended maturities, principal reduction, or other amendments—that are worse than the original contract. Restructuring does not require actual non-payment; the mere announcement that terms will be forced on creditors counts as a credit event. This is the most litigated trigger; sovereigns and creditors often dispute whether a modification is truly a "restructuring" or a consensual amendment.

**Repudiation/moratorium** occurs when a sovereign explicitly rejects or suspends payment on external debt, even if no payment is yet due. For instance, if a government announces "we will not pay external debt" but the next payment is three months away, a credit event is triggered immediately.

**Acceleration** is triggered if a sovereign fails to pay any financial obligation in excess of a threshold (typically $10 million–$50 million, depending on the contract) and that failure is not remedied within a grace period. This catches non-debt obligations—lease payments, insurance claims, or other contracts—that might signal broader insolvency.

**Rating downgrade** in some older contracts (now rare) triggered a credit event if a rating agency downgraded the sovereign to a specific low rating level. Modern contracts rarely use this trigger, as it was abused.

The reference obligation—the specific bond or loan contract that the CDS references—must be clearly identified. A CDS on "Argentina" might reference a specific 2030 dollar eurobond. If that bond defaults but other Argentine obligations do not, the CDS on that specific bond triggers, but broader Argentine CDS (on the country as a whole) may not trigger unless the contract specifies otherwise.

## The ISDA Determinations Committee process

When a potential credit event occurs, market participants can submit a "Credit Event Notice" to the ISDA Determinations Committee. The notice states that a credit event has occurred under the contract, names the reference entity (the sovereign), and cites the specific contract clause.

The ISDA Determinations Committee is a standing body of 16 voting members: five major derivatives dealers (JP Morgan, Goldman Sachs, Bank of America, Morgan Stanley, Citi), five end-users (major institutions like bond funds or pension funds), and six alternates. The chair is a neutral third party. The committee meets informally to discuss potential credit events and formally votes to determine whether a credit event has occurred.

The committee does not have judicial authority. It is a contractual body, created by the ISDA Master Agreement itself. Its role is to interpret contract language and determine whether the facts on the ground satisfy the definition of a credit event. If the committee cannot reach consensus (a simple majority of 9 out of 16 votes), the matter reverts to the contract's fallback provision—typically, the triggering party can force the determination through arbitration.

In practice, the committee has remarkable authority because market participants have chosen to use ISDA contracts almost universally. A committee determination is, in effect, the market's determination; going to arbitration is rare and costly.

The committee typically meets 3–5 business days after a notice is submitted to discuss the preliminary question: has there been a potential credit event? Then, over 30–60 days, the committee gathers information, reviews statements by the sovereign, and issues a decision. Once a credit event is determined, the committee also sets the settlement date for the auction (typically 30–45 days after determination, to allow market formation and trading).

## Restructuring determinations and creditor disputes

Restructuring is the most contentious credit event definition because sovereigns and creditors often dispute whether a modification is truly forced.

A sovereign might announce a debt exchange: existing bondholders are invited to exchange their old bonds for new ones with better terms (lower coupons, cleaner covenants). If participation is consensual, this is not a restructuring and does not trigger CDS. But if the government announces that non-participating bondholders will be treated worse (or if participation is so heavily incentivized that refusal is impractical), the distinction blurs.

The ISDA definition requires that the modification be **"materially more onerous."** This means the new terms must be objectively worse than the original: lower present value, longer maturity, reduced coupon, or principal reduction. But "materially" is judged by the committee, and reasonable people disagree.

In **Greece 2011–2012**, the government forced a massive debt exchange on private creditors (roughly 50% haircut) after initially claiming it was consensual. The committee determined that it was a restructuring and triggered CDS. Greek CDS holders received cash settlement based on auction-determined recovery. This was contentious; some creditors argued the exchange was voluntary, and the determination split the market.

In **Ukraine 2015**, the government restructured external bonds, extending maturities and reducing coupons. The committee determined this was a credit event and CDS settled. However, Ukraine signed exceptions into the settlement, meaning some creditors were exempt, complicating the cash auction.

## The cash settlement auction

Once a credit event is determined, settlement proceeds via **cash auction**. The committee publishes a list of "deliverable obligations"—the bonds and loans that will be used to determine recovery. For a sovereign, this typically includes a range of external dollar bonds issued by the central government.

The auction works as follows: on settlement day, banks and major market participants submit bids for how much they will pay for one unit of the deliverable obligation (per dollar of face value). For instance, if Greece's principal bonds are trading at 30 cents on the dollar, bidders might offer 30–32 cents.

The auction determines a **"settlement price"** as the weighted average of bids. If the settlement price is 30 cents, CDS protection payers receive (100 cents – 30 cents) = 70 cents per dollar of notional protection. A bank that bought $10 million of protection on Greece at 50 basis points annually receives a payout of 70% of $10 million = $7 million.

The auction serves two crucial functions. First, it fixes the recovery price in a transparent, market-based mechanism, preventing manipulation by a single dealer or institution. Second, it allows the committee to "settle" the notional amount by reference to real, traded instruments, rather than by a subjective estimate of value.

## Physical delivery versus cash settlement

Older CDS contracts on sovereigns allowed **physical delivery**: protection sellers delivered the deliverable obligation bonds to protection buyers in exchange for par value. Under this mechanism, if a CDS buyer owned protection on Argentina and Argentina defaulted, the seller would deliver Argentine bonds to the buyer, and the buyer would pay par (100 cents per dollar of face value) in exchange.

This created an incentive for protection sellers to obtain cheap bonds before settlement and deliver them. If Argentina bonds were trading at 30 cents, a protection seller could buy them for $3 million and deliver them to the protection buyer (who paid $10 million par), pocketing a $7 million gain. This arbitrage was possible but involved operational risk and delivery logistics.

Modern sovereign CDS contracts use **cash settlement**. No physical bonds change hands; instead, the protection seller pays the protection buyer the difference between par and the auction settlement price in cash. This eliminates delivery logistics and manipulation.

## Timing and market dislocation

The gap between a credit event occurrence and cash settlement creates **basis risk** for CDS buyers.

When a sovereign defaults or restructures, the market immediately reprices the debt. Bonds might drop from 90 cents to 30 cents in a single day. But CDS protection does not pay out immediately; the ISDA committee must first determine that a credit event occurred (3–60 days). Then the settlement date is set, usually 30–45 days after determination. The protection payout settles on that date.

During this gap, a protection buyer who also holds the underlying bonds faces a loss: the bonds have dropped 60 cents, and the CDS payout will eventually recover some of this, but the protection buyer may have faced margin calls, portfolio pressure, or liquidity needs in the interim.

Additionally, the auction settlement price can surprise the market. If creditors negotiate a better restructuring deal than markets expected, the settlement price might be higher (say, 50 cents instead of 30 cents), reducing the CDS payout. Conversely, if the situation deteriorates, the settlement price drops, increasing the payout.

This variability has led some institutions to hedge CDS by buying bonds; the combination locks in a synthetic floating rate but requires careful management across the credit-event window.

## Special cases and complications

**Multiple reference obligations** complicate settlement. A sovereign might issue bonds in dollars, euros, and local currency, with different covenants and seniority. A CDS contract typically references one specific bond as the "reference obligation," but allows substitution to other obligations with similar characteristics if the reference obligation is redeemed or matures. Disputes arise over whether a restructured bond qualifies as a deliverable obligation for a CDS that referenced the original bond.

**Selective default** on one tranche but not others creates ambiguity. If a sovereign defaults only on external dollar bonds but continues paying domestic or bilateral debt, is there a credit event on the sovereign as a whole? The answer depends on the CDS contract language. A contract that references "any financial obligation" of the sovereign might be triggered; one that specifies "external debt" might not.

**Holdout creditors** can affect the auction. If creditors refuse to accept a restructuring and instead litigate, the settlement price may reflect only the subset of creditors who accepted. This creates **fragmentation**: CDS holders may receive a payout based on a 50% recovery (for creditors who accepted the deal), while holdout litigation might eventually deliver 30% or 80%, distorting the original protection value.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit Default Swap](/credit-default-swap/) — the instrument whose settlement is described here
- [Sovereign Default](/sovereign-default/) — the credit events that trigger CDS settlement
- [Selective Default Credit Rating](/selective-default-credit-rating/) — rating agency designations that can trigger CDS
- [Sovereign Debt Seniority](/sovereign-debt-seniority/) — creditor priority affects which debts trigger CDS
- [Domestic vs External Default](/domestic-vs-external-default/) — CDS typically cover external, not domestic, defaults
- [Debt Restructuring](/debt-restructuring/) — the restructuring event that triggers CDS determination

### Wider context

- [Bond](/bond/) — the underlying obligation that CDS protects
- [Credit Spread](/credit-spread/) — related measure of sovereign default risk
- [Counterparty Risk](/counterparty-risk/) — the risk that the CDS protection seller fails to pay
- [Derivatives Hedging](/derivatives-hedging/) — how CDS are used to hedge portfolio risk
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator of CDS disclosure

</div>
