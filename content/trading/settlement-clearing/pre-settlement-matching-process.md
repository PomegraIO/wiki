---
title: "Pre-Settlement Matching: How Trades Are Confirmed Before Settlement"
description: "Pre-settlement matching confirms trade details at a repository or central securities depository before funds and shares change hands, stopping settlement failures."
keywords:
  - pre-settlement matching process
  - trade matching confirmation
  - settlement matching rules
  - trade repository matching
  - settlement failure prevention
image: /svg/trading.svg
---

*The **pre-settlement matching process** is the post-trade workflow in which buyer and seller confirm that they agree on price, quantity, and settlement terms before cash and securities actually move. If buyer says "100 shares at $50" but seller says "100 shares at $49," the mismatch blocks settlement until both parties correct their records. Most developed markets use a central trade repository or depository to conduct this matching, turning potential settlement failures into exceptions rather than routine events.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Pre-Settlement Matching — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Matching ensures buyer and seller agree before settlement, preventing failures and losses.</div>

|   |   |
|---|---|
| **When it happens** | T+0 (trade date) through T+1, before settlement at T+2 or later |
| **Who performs it** | Central counterparty, trade repository, or central securities depository |
| **What gets matched** | Price, quantity, counterparty IDs, settlement instructions, corporate actions |
| **Mismatch outcome** | Trade status becomes "unmatched"; settlement cannot proceed |
| **Correction window** | Usually 24–48 hours; manual intervention if automatic correction fails |
| **Cost of failure** | Fails-to-deliver, buy-ins, penalty interest, operational friction |

</aside>

## The matching workflow from trade to settlement

Immediately after a trade executes on an exchange or [over-the-counter market](/over-the-counter-market/), both the buyer's and seller's clearing firms submit trade details to a central authority—typically a trade repository, central counterparty (CCP), or central securities depository (CSD). The submitted details include:
- Price per share
- Total quantity
- Settlement date (often T+2)
- Settlement instructions (wire details, depository account numbers)
- Counterparty identifiers (clearing firm codes)
- Any special conditions (e.g., cash on delivery, corporate action adjustments)

The repository or depository runs an automated matching engine that compares the buyer's submission against the seller's. If they agree on all material terms, the trade is marked "matched" and proceeds toward settlement. If they differ on any field, the trade is flagged "unmatched."

## Mismatch scenarios and resolution

Common mismatches include:
- **Price discrepancy** — Buyer submitted $50, seller submitted $49.50. Someone entered the wrong figure.
- **Quantity discrepancy** — Buyer claims 1,000 shares; seller claims 900 shares.
- **Settlement instructions** — Buyer's bank details do not match seller's depository records.
- **Settlement date mismatch** — Buyer requested T+3; seller set T+2.
- **Corporate action adjustments** — Ex-dividend trades may have different quantity adjustments depending on local rules.

When a mismatch is flagged, the systems typically alert both clearing firms immediately. The responsible trader or settlement officer manually reviews the original trade ticket (the exchange record or dealer confirmation) to determine the correct figure. If the mismatch is a clerical error—e.g., the price was entered wrong in the depository but correct on the exchange—the party corrects their submission and resubmits. The automated engine re-matches.

Most mismatches are resolved within 24 hours. If not corrected within the defined window (usually T+1 evening), the trade remains unmatched and cannot settle. The clearing firms must then escalate the issue, and settlement delays or fails-to-deliver occur.

## Why matching matters: Prevents fails-to-deliver

Before mandatory pre-settlement matching (which emerged fully in major markets in the 1990s), mismatches went undetected until settlement day itself. On settlement morning, the buyer's cash would be ready, but the seller's securities would not appear—or the quantities would be wrong—because the seller had no idea the buyer expected a different amount or settlement date.

The result was a "fail-to-deliver" (often shortened to "fail")—a broken settlement that could take days or weeks to unwind. During those days, the buyer held cash but no securities, and the seller held securities but no cash. Fails created operational friction, tied up collateral, and sometimes led to forced buy-ins or sales at unfavorable prices.

Pre-settlement matching eliminates most fails by forcing agreement upfront. If buyer and seller have not aligned on the terms before settlement date, the mismatch is immediately visible and correctable.

## Role of the central counterparty (CCP)

In many developed markets, a [central counterparty](/central-bank/) stands between buyer and seller, meaning both parties settle with the CCP, not directly with each other. The CCP conducts matching on behalf of both and assumes counterparty risk.

For the buyer, the CCP is the seller; for the seller, the CCP is the buyer. The CCP's matching process is the same—it receives submissions from both sides and compares them—but its role as guarantor means that once the CCP confirms a match, settlement is virtually certain. The CCP will deliver or receive securities and cash, even if one of the original parties fails.

This intermediation shifts risk from operational (will the trade settle?) to credit-based (will the CCP stay solvent?). Most CCPs are heavily regulated and capitalized precisely because their role is so critical.

## Matching timelines and market variations

Matching timing varies by market:
- **US equities** — Settlement is T+2; matching usually completes by T+1 evening. Most mismatches are resolved same-day.
- **Forex and money markets** — Same-day or next-day settlement is common. Matching must happen within hours.
- **Treasuries and bonds** — Settlement may be same-day (same-day accrued) or T+1. Matching is similarly compressed.
- **Emerging markets** — Some use T+3 or T+5 settlement, allowing a longer matching window but also creating more settlement delay risk.

In faster-settlement markets (forex, same-day treasuries), any mismatch immediately blocks settlement, so the incentive to get details right is acute. In T+2 or T+3 markets, traders have some buffer but still face penalties or operational issues if they leave mismatches unresolved.

## Manual interventions and exception handling

Not all mismatches are simple clerical errors. Some arise from:
- **Network delays** — A trader's submission did not reach the repository; the original trade is missing.
- **System differences** — Buyer's system and seller's system use different settlement account codes for the same depository.
- **Legal entity ambiguity** — A large bank trading in multiple legal entities may submit trades under the wrong entity code.
- **Corporate actions** — A stock split or dividend adjustment may cause quantity mismatches on trades that settled across the ex-date.

These require human investigation. Clearing firms employ settlement specialists who pull the original trade ticket from the exchange, call the other party's settlement team, and negotiate a resolution. The resolution might be a correction, a cancellation, or an agreement that both sides made a mistake and will execute a new trade at a new price.

The goal is always to resolve within the window (T+1 for T+2 settlement) and avoid a fail. If resolution is impossible, the trade fails to settle and both parties incur penalties.

## See also

<div class="wiki-seealso">

### Closely related

- Settlement clearing — The broader mechanics of how trades settle and money moves
- [Central counterparty](/central-bank/) — The institution conducting matching and standing as guarantor
- [Counterparty risk](/counterparty-risk/) — Why CCP intermediation shifts risk from operational to credit
- [Trade repository](/securities-and-exchange-commission/) — The database where trades are reported and matched
- Fails to deliver — What happens when settlement does not occur on time

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulator of trade reporting and settlement standards in the US
- [Over-the-counter market](/over-the-counter-market/) — Where OTC trades must also submit to matching via DTCC or similar
- [Execution risk](/execution-risk/) — The broader category of risks that orders may not complete as intended
- [Operational risk](/operational-risk/) — System failures and human error in settlement workflows

</div>
