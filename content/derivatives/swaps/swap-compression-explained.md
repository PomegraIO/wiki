---
title: "Swap Compression Explained"
description: "How swap compression reduces notional outstanding and counterparty risk by consolidating offsetting derivative positions without altering net market exposure."
keywords:
  - what is swap compression in derivatives
  - portfolio compression counterparty risk
  - swap compression notional
  - multilateral compression derivatives
  - derivative risk reduction
  - swap counterparty consolidation
---

*Swap compression is a post-trade portfolio optimization technique in which dealers or counterparties consolidate offsetting derivative positions into fewer, lower-notional contracts. The process reduces [counterparty risk](/counterparty-risk/) and collateral requirements without changing net market exposure—essentially cleaning up the ledger while keeping the same economic outcome.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Swap Compression — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Compression nets offsetting trades, lowering systemic risk and capital efficiency.</div>

|   |   |
|---|---|
| **What it solves** | Excess notional, collateral drag, counterparty risk proliferation |
| **Mechanics** | Identify offsetting legs; tear up old contracts; issue single consolidated trade |
| **Notional impact** | Reduced outstanding notional on books |
| **Mark-to-market P&L** | No change; net economic position remains identical |
| **Participants** | Bilateral (dealer-to-dealer) or multilateral (via compression services) |
| **Collateral benefit** | Lower notional = lower [margin call](/margin-call-forex/) exposure and reduced [counterparty risk](/counterparty-risk/) |
| **Regulatory driver** | Dodd-Frank and EMIR encourage compression to reduce systemic risk |

</aside>

## The Problem: Notional Bloat and Risk Opacity

When [interest rate swaps](/interest-rate-swap/), [currency swaps](/swap/), or [credit default swaps](/credit-default-swap/) are traded, each deal creates a new bilateral contract between two counterparties. Over years, large dealers and sophisticated investors accumulate hundreds or thousands of trades with the same counterparty, often with offsetting economic legs. One dealer may have a $100 million 5-year pay-fixed swap with a bank, and a separate $80 million 5-year receive-fixed swap with the same bank—both exist as live contracts, tying up [collateral](/risk-weighted-assets/), occupying settlement capacity, and creating redundant counterparty exposure.

From a market-wide perspective, this creates bloat. The global interest rate swap market has multi-hundreds of trillions in notional outstanding; much of it is economically redundant because of overlapping offsetting flows. This opacity makes it harder for regulators to measure systemic risk and for institutions to manage their own exposure efficiently.

## How Bilateral Compression Works

In a bilateral compression, two counterparties (usually dealers) identify all their trades and ask: "What is our true net economic position?" If dealer A owes dealer B $50 million on one swap and dealer B owes dealer A $40 million on another, the net is a single $10 million flow. Both can agree to tear up the old contracts and execute a single new trade reflecting the net position.

The process follows this sequence:

1. **Inventory phase**: Both sides reconcile their trade data and identify all outstanding positions.
2. **Netting analysis**: Counterparties calculate the mark-to-market value of each trade and net across [maturity](/expiration-date/), [strike](/strike-price/), and product type (interest rate, [currency](/currency-risk/), credit, etc.).
3. **Tear-up and novation**: Old trades are cancelled; a new single trade (or small set of trades) is executed to reflect the net position.
4. **Settlement**: Any cash adjustments reflect the difference in mark-to-market values between the old portfolio and the new one.

The cash adjustment is crucial: if the old $100 million pay-fixed and the old $80 million receive-fixed trades sum to a net $15 million of current economic value owed by dealer A to dealer B, that $15 million is paid as a lump sum. The new single contract reflects the residual net market exposure going forward.

## Multilateral Compression and Central Clearing

Bilateral compression between pairs of dealers works, but it does not capture the full benefit of netting across the entire market. A multilateral compression service (such as TriOptima for interest rate derivatives) collects trade data from dozens or hundreds of dealers and participants, then runs a network-wide matching algorithm to identify all possible offsetting flows.

Imagine 100 dealers in a ring. Dealer A owes B $10 million, B owes C $8 million, C owes D $12 million, and D owes A $5 million. Bilateral compression between pairs would still leave multiple contracts. But a multilateral algorithm can find the cycle and collapse it: A pays D $2 million (the net around the ring), and three trades are eliminated.

In practice, multilateral compression involves a central [custodian](/custodian/) or intermediary that acts as the facilitator (but not the counterparty). The intermediary:
- Collects encrypted trade details from participants
- Runs a netting algorithm (preserving privacy)
- Proposes the optimal set of tear-ups and new trades
- Calculates settlement amounts
- Executes the compression after all parties consent

This is different from a [central clearinghouse](/central-bank/), which becomes counterparty to every trade. A compression intermediary is purely administrative.

## Notional Reduction and Capital Efficiency

The headline metric for a compression event is notional eliminated. If a multilateral compression runs across $2 trillion in interest rate swap notional and reduces it by $400 billion, the savings are substantial:

- **Collateral release**: Lower notional typically means lower initial margin and variation margin, freeing up capital for other uses.
- **Counterparty concentration**: Fewer live contracts reduce the counterparty exposure matrix, making risk management and [stress testing](/stress-testing/) clearer.
- **Operational burden**: Fewer trades means fewer counterparty reconciliations, settlement instructions, and operational risk vectors.

For dealers, compression also improves capital efficiency under [risk-weighted asset](/risk-weighted-assets/) frameworks. A $1 billion notional interest rate swap with AAA counterparty may require much less risk weight than two $800 million and $300 million trades; netting reduces the risk weight.

## No Economic Impact on Existing Positions

A critical point: compression does not change the net economic position of any participant. An investor who is long 100,000 barrels of oil via a [futures contract](/futures-contract/) cannot be compressed away. If the investor simultaneously enters a compression, it is because they have offsetting hedges that can be netted. The compression simplifies the position, not the risk.

Traders and risk managers often worry: "Will compression move the market or trigger unexpected losses?" The answer is almost never. A compression is a purely bilateral or multilateral netting; no new liquidity is demanded, no one is forced to take a new position. The mark-to-market of the new portfolio equals the mark-to-market of the old one (up to rounding and timing of settlement).

## Regulatory and Systemic Drivers

Post-2008 financial crisis, [regulatory frameworks](/dodd-frank-act/) like Dodd-Frank (US) and EMIR (EU) have encouraged or mandated compression to reduce systemic risk. The rationale is clear: the more notional and counterparty entanglement, the harder it is to unwind a major dealer failure. If dealer X suddenly becomes insolvent, counterparties want the ability to quickly identify and transfer their trades. Thousands of redundant contracts with X make this much harder.

Dodd-Frank also imposes [capital adequacy](/capital-adequacy/) rules based on [risk-weighted assets](/risk-weighted-assets/), which penalize notional bloat. This creates a direct incentive for dealers to compress.

## Limitations and Practical Constraints

Compression is not a universal solution. Not all trades can be compressed:

- **Bespoke terms**: If a dealer has a unique, non-standardized swap, there may be no offsetting trade to compress it against. Compression works best for vanilla, actively traded products like 5-year or 10-year [interest rate swaps](/interest-rate-swap/).
- **Operational resistance**: Smaller dealers or less sophisticated counterparties may lack the systems to participate in regular compression runs. Buy-side firms with limited back-office infrastructure may skip compression to avoid operational complexity.
- **Timing and consent**: Compression requires consensus from all parties. If one counterparty refuses (e.g., for accounting or regulatory reasons), the compression cannot proceed for that pair.
- **Accounting treatment**: A tear-up and novation of trades can trigger accounting recognition of gains or losses under [ASC 606](/asc-606/) or IFRS 9, which some treasurers wish to defer.

## The Future: Automation and Real-Time Netting

Modern compression platforms are moving toward real-time or near-continuous netting. Rather than quarterly or annual compression events, dealers push for standing instructions to automatically compress offsetting flows within tolerance bands (e.g., compression is triggered when notional offset exceeds 10% of the pair's total outstanding). This further reduces collateral drag and simplifies the operational calendar.

Central clearing also partially replaces bilateral compression, since a central clearinghouse automatically nets flows between all its members, obviating the need for bilateral tear-ups. As more interest rate and [credit default](/credit-default-swap/) swaps move to central clearing, the demand for bilateral and multilateral compression may decrease—though for non-cleared derivatives, compression will remain essential.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-rate swap](/interest-rate-swap/) — primary product subject to compression
- [Counterparty risk](/counterparty-risk/) — the risk compression mitigates
- [Credit default swap](/credit-default-swap/) — another derivative compressed to reduce risk
- [Swap](/swap/) — general family of derivatives; compression applies broadly
- [Dodd-Frank Act](/dodd-frank-act/) — regulatory driver for compression adoption
- [Risk-weighted assets](/risk-weighted-assets/) — capital framework that encourages netting

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — compression preserves hedges while reducing notional
- [Repurchase agreement](/repurchase-agreement/) — alternative collateral-posting mechanism
- [Margin call forex](/margin-call-forex/) — collateral management; compression reduces margin exposure
- [Systemic risk](/systemic-risk/) — compression is a systemic risk mitigation tool

</div>
