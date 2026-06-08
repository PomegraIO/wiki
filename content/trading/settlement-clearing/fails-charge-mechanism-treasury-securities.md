---
title: "Fails Charge Mechanism in Treasury Securities"
description: "Understand the fails charge mechanism mandated by the Federal Reserve to prevent persistent delivery failures in US Treasury markets."
keywords:
  - fails charge mechanism
  - treasury fails charge
  - fails charge calculation
  - treasury settlement
  - delivery failure
  - federal reserve treasury
---

*The **fails charge mechanism** is a penalty imposed by the Federal Reserve on parties that fail to deliver US Treasury securities by the settlement deadline. The charge is calculated per day of delay and is designed to make persistent failures economically painful, thereby discouraging strategic non-delivery and keeping the Treasury market functioning smoothly.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Fails Charge — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A fee that punishes delays and keeps settlement discipline intact.</div>

|   |   |
|---|---|
| **What it penalizes** | Failure to deliver Treasury securities by the settlement deadline (T+1) |
| **Who pays** | The party that fails to deliver |
| **Rate** | Based on the current federal funds rate; typically 0.5% per annum or the federal funds target rate, whichever is lower |
| **Calculation** | Daily accrual on the dollar amount of the failed delivery |
| **Trigger** | Automatic after T+1 settlement; applies each business day the failure persists |
| **Waiver conditions** | Fed can suspend charges during extreme market stress or public policy emergencies |

</aside>

## Why Fails Matter in Treasuries

The US Treasury market is the deepest, most liquid market in the world—roughly $27 trillion in outstanding securities. Trillions of dollars move daily through this market. When a seller agrees to deliver Treasuries to a buyer, both parties expect the securities to arrive on the settlement date, usually one business day after the trade (T+1).

A "[fail](https://example.com)" occurs when the seller does not deliver on time. This might happen by accident—a miscommunication, a system glitch, a lost broker confirmation—but it can also be strategic. A sophisticated trader might deliberately fail to deliver if interest rates have risen sharply, making the security more valuable. Failing to deliver and buying back at a lower price later can lock in a profit. Without a penalty, fails would become a form of free optionality: keep the Treasuries if the trade goes your way, deliver them if it does not.

This would break the market. Counterparties would lose trust in delivery commitments. Sellers would demand higher yields to compensate for delivery risk. The Fed could not reliably drain or inject liquidity through repurchase agreements (repos). The entire plumbing of US financial markets depends on Treasury settlement being certain.

## How the Charge Is Calculated

The fails charge is a daily accrual computed on the principal amount of the failed delivery at an interest rate tied to the [federal funds rate](https://example.com). The precise formula set by the Fed is:

**Daily charge = Principal amount × (Federal funds rate or 0.5%, whichever is lower) ÷ 360**

For example, suppose a dealer fails to deliver $10 million of a 10-year Treasury note. The [federal funds rate](https://example.com) is 2.5%. The daily charge is:

$10,000,000 × 0.5% ÷ 360 = $1,389 per day

If the failure persists for 10 days, the total charge is $13,890. If it stretches to a month, it is roughly $41,700. The longer the failure persists, the more painful it becomes.

The charge accrues daily while the fail is open and is typically applied to the failing party's clearing account. The funds go to the Fed's general account; they are not paid to the buyer who is owed delivery. The mechanism is purely punitive—designed to make the cost of not delivering exceed any profit from holding the securities.

## The "Cheapest to Deliver" Interaction

Fails charges matter most in the context of Treasury [futures contracts](https://example.com), where sellers have a "[cheapest to deliver](https://example.com)" (CTD) option. When a seller delivers against a Treasury futures contract at expiration, they can choose from a basket of eligible Treasury securities. They naturally choose the cheapest eligible security at that moment.

If the cheapest security is in short supply—perhaps because another trader has engineered a squeeze—its price can spike. A short seller might be tempted to deliver a more expensive substitute and pocket the difference, then fail on the supposed delivery and hold out for a better price. The fails charge prevents this. If the profit from the squeeze is less than the accumulated fails charge, the game is not worth playing.

Before the Fed implemented the fails charge regime in 2009, fails were endemic in Treasuries—parties would fail strategic delivery, hold the securities, and occasionally settle at a discount. The fails-charge mechanism has largely eliminated this form of manipulation.

## Relationship to Delivery Mechanics

A fail does not automatically breach a contract or trigger a lawsuit, though it does create legal exposure. The buyer has a claim against the seller but must pursue it through the clearing house or through courts. In the meantime, the buyer does not have the securities and cannot use them in other trades or [repo](https://example.com) transactions.

The clearing house (typically the Depository Trust & Clearing Corporation, or DTCC) tracks fails and reports them to the Fed. If a fail is reported at settlement time and the failing party does not cure it, the fails charge kicks in automatically. The failing dealer faces both the daily charge *and* the operational headache of managing a fail on its books.

Most fails in modern Treasuries markets are genuinely accidental—a late input, a failed system, a miscommunication between floors. These resolve within a day or two. The fails charge is low (typically 0.5% annual, a few dozen dollars per day on a multi-million-dollar fail), but it is enough to motivate urgent correction.

## Fed Authority and Emergency Suspensions

The Fed has the authority to suspend or adjust the fails-charge regime in emergencies. During the 2008–2009 financial crisis, when Treasury settlement infrastructure was strained and fails spiked, the Fed suspended fails charges temporarily to allow dealers breathing room to work through backlogs without accumulating massive penalty bills.

In March 2020, when COVID-19 caused extreme Treasury market volatility and function disruption, the Fed again suspended fails charges for a brief period. The suspension signaled that the focus was on restoring orderly settlement and liquidity provision, not punishing technical failures.

These suspensions are rare and temporary, intended only for genuine financial stress. They are not a routine relief valve. The default regime—the fails charge always on—is the discipline that keeps fails rare.

## Relationship to [Repo](https://example.com) and Money Markets

The fails-charge mechanism indirectly supports the [repurchase agreement](https://example.com) market, where Treasuries are the primary collateral. If fails were chronic and unpunished, repo buyers would face counterparty risk that the securities they are supposedly holding would never arrive. The [cost of repo](https://example.com) would rise (demand for insurance against fails would bid up rates), and the Fed's ability to manage [monetary policy](https://example.com) through repo operations would be compromised.

By making fails expensive, the mechanism ensures that repo counterparties can rely on settlement and bid-ask spreads stay tight. This benefits the entire fixed-income market, not just Treasuries.

## Impact on Dealers and Custodians

For large dealers and custodians (investment banks, asset managers with clearing seats), the fails-charge regime is a known cost of business. Operations teams are trained to track settlement status, flag potential fails early, and deploy back-office resources to cure fails before they trigger charges.

A dealer who chronically fails—perhaps because of poor systems or chaos on the trading floor—will accumulate noticeable fails charges, sometimes tens of thousands of dollars per month. That becomes a line item on the business unit's P&L, visible to senior management and regulation. Peer dealers also notice and may raise counterparty haircuts or risk limits. The reputational and operational cost is large enough that systematic failure is essentially unheard of.

For small, non-dealer participants (e.g., a hedge fund clearing through a prime broker), fails are typically invisible—the prime broker absorbs the charge and might pass it through to the hedge fund if it is the systematic failer. Most clients never see a fails charge; they are handled behind the scenes.

## The Broader Discipline Ecosystem

The fails charge is one tool in a suite that keeps the Treasury market functioning. Other tools include:

- [Reserve requirements](https://example.com) on dealer inventories, which encourage dealers to hold adequate buffer stock
- [Haircuts](https://example.com) on Treasury collateral in repo transactions, which adjust if fails surge
- Real-time gross settlement systems (RTGS), which reduce the window for unintended fails
- Intraday monitoring by the Fed, which flags emerging fails patterns

Together, these create a system where a single missed settlement is a minor inconvenience, easily corrected, and chronic fails are economically untenable. The fails charge is the key disciplinary lever.

## See also

<div class="wiki-seealso">

### Closely related

- Settlement and clearing — the broader infrastructure for moving securities and cash between parties
- [Treasury bill](/treasury-bill/), [Treasury bond](/treasury-bond/) — the securities subject to fails-charge discipline
- [Repurchase agreement](/repurchase-agreement/) — Treasury repo, where fails-charge discipline protects counterparties
- Delivery failure — the operational event that triggers the charge
- [Federal funds rate](/federal-funds-rate/) — the basis for the fails-charge rate calculation

### Wider context

- [Federal Reserve](/federal-reserve/) — the central bank that enforces fails discipline
- [Counterparty risk](/counterparty-risk/) — the settlement risk that fails charges help mitigate
- [Monetary policy](/monetary-policy/) — Fed operations that depend on reliable Treasury settlement
- Central clearinghouse — the infrastructure that tracks and enforces fails charges

</div>
