---
title: "Overlay Currency Program"
description: "A dedicated hedging mandate that separates currency risk management from asset management."
keywords:
  - currency hedging
  - fx overlay
  - currency risk management
  - asset allocation
  - portfolio hedging
image: "/svg/risk.svg"
---

*An **overlay currency program** is a separate, dedicated hedging function that manages [currency risk](/currency-risk/) independently from the underlying [asset allocation](/asset-allocation/) decisions. Rather than embedding FX hedges within each country's asset manager, a central overlay team takes responsibility for translating aggregate currency exposures into hedging positions—typically using [forwards](/forward-contract/), [options](/option/), or other [derivatives](/), leaving asset managers free to focus on security selection.*

## The separation of concerns

Traditional multi-asset portfolios hold stocks and bonds in multiple currencies. When a UK fund owns Japanese equities, it carries both equity risk and [currency risk](/currency-risk/). Historically, portfolio managers decided both: where to buy and how much FX hedging to apply. This bundling became inefficient at scale. A single manager cannot easily distinguish currency views from asset views, and different managers may inadvertently double-hedge or leave gaps.

An overlay program inverts the structure. Asset managers pursue their best stock and bond ideas in any currency, without worrying about hedging. The overlay team sits at the fund level, observes the aggregate [currency exposure](/currency-risk/) flowing from all the regional mandates, and executes a strategic hedging plan. It is separation of concerns: asset managers buy what they think will outperform; the overlay team controls how much currency risk the fund bears.

## Mechanics: from exposure mapping to execution

A typical overlay programme begins with daily or weekly exposure reporting from each regional asset manager. The overlay team aggregates these positions by currency—how much yen exposure, how much euro exposure, and so on. Against this map, the overlay team runs its hedging logic, which might be simple (hedge 80 per cent of all foreign exposures back to the home currency) or sophisticated (hedge only high-volatility currencies, or take tactical views on currency pairs).

Execution is typically delegated to specialist currency traders, often via [forwards](/forward-contract/) on the [over-the-counter market](/over-the-counter-market/) or exchange-traded [futures](/futures-contract/). The team may also deploy [options](/option/) if they want to preserve upside while capping downside risk, though options are more expensive.

## Why dedicated overlay beats embedded hedging

Embedded hedging—where each regional manager controls their own FX—creates redundancy and inefficiency. Two managers might both hedge their euro exposure, creating a double hedge. Or one might miss hedging a small position that compounds into something material. Overlay programmes detect and eliminate these overlaps.

They also reduce operational cost. Instead of training every asset manager in [currency derivatives](/currency-risk/), the fund employs a specialist overlay team. Centralised execution on large notional amounts—thousands of forwards traded as a block—yields better [bid-ask spreads](/bid-ask-spread/) and lower [counterparty risk](/counterparty-risk/).

Furthermore, overlay programmes allow the fund to take *strategic* currency views. If the overlay team believes the pound will depreciate, it can choose to leave sterling foreign exposure unhedged (or under-hedged) across the portfolio. Individual managers would not coordinate such a bet.

## Governance and mandate scope

An overlay mandate must be clearly defined. The most common structure is **percentage-of-exposure hedging**: hedge 100 per cent, 80 per cent, 50 per cent, or zero of foreign currencies, with specific rules for each. Some programmes introduce tactical flexibility: the overlay team may shift the hedge ratio between 50 per cent and 100 per cent based on [implied volatility](/implied-volatility/) or forward points, within guardrails set by the investment committee.

A few programmes go further, permitting the overlay team to take *net* directional bets—overweighting or underweighting a currency relative to the portfolio's exposure. This is more aggressive and requires strong governance. Many funds limit such discretion to exclude tail risks.

## The cost of hedging: contango versus tailwinds

Hedging foreign currency exposure incurs costs. When [interest rate](/interest-rate/) differentials favour hedging (e.g., hedging yen back to dollars costs almost nothing because Japanese rates are low), the fund benefits. When they penalise hedging (e.g., locking in a forward at unfavourable rates), the cost accumulates. Over long periods, these costs can be substantial, shaving 20–50 basis points annually from returns if the portfolio is heavily hedged in an unfavourable rate environment.

Some programmes dynamically hedge, reducing hedges when costs spike and increasing when rates align favourably. This introduces timing risk—the fund might under-hedge right before a currency moves sharply—but can improve outcomes if executed with discipline.

## Tactical versus strategic hedging

Overlay programmes can be **strategic** (consistent, rules-based, with little discretion) or **tactical** (actively managed, responding to market conditions). Strategic programs appeal to indexing or passive-allocation funds that want predictable, low-maintenance hedging. Tactical programmes suit active managers who believe they can add alpha through currency timing.

In practice, most large institutional programmes blur the line: they run a strategic core hedge (say, 80 per cent of foreign exposure) and permit the overlay team tactical room to shift ±10 per cent based on forward curves and volatility conditions.

## When overlay programmes fail or get unwound

Overlay programmes sometimes fail spectacularly when the mandate drifts. If a committee approves tactical currency bets without clear limits, an overlay team can rack up massive losses during a sharp reversal—say, a sudden 10 per cent depreciation of a currency the team was betting would strengthen. High-profile incidents (the UK pension fund hedging blow-up during rate volatility, for example) have often stemmed from ill-disciplined currency overlays.

They are also sometimes unwound by new investment committees that believe hedging is wasteful or that the fund should take full currency exposure for diversification. Withdrawing a mature overlay programme requires careful sequencing—liquidating hedge positions can itself move prices or incur costs, and asset managers need time to adjust their own FX assumptions if overlay hedges suddenly disappear.

## See also

<div class="wiki-seealso">

### Closely related

- [Currency Risk](/currency-risk/) — the underlying exposure that overlay programmes manage
- [Forward Contract](/forward-contract/) — primary tool for FX overlay execution
- [Option](/option/) — used when overlay teams want convex payoffs or preserve upside
- [Bid-Ask Spread](/bid-ask-spread/) — better spreads are one benefit of centralized, large-scale execution
- [Interest Rate Risk](/interest-rate-risk/) — cost of FX hedging depends on interest rate differentials
- [Over-the-Counter Market](/over-the-counter-market/) — where most FX forwards are traded

### Wider context

- [Asset Allocation](/asset-allocation/) — overlay programmes sit atop allocation decisions
- [Counterparty Risk](/counterparty-risk/) — FX forwards introduce counterparty exposure to banks
- [Implied Volatility](/implied-volatility/) — influences cost of option-based overlays
- Portfolio Hedging — broader concept encompassing all derivatives-based risk management
- [Operational Risk](/operational-risk/) — overlays introduce model and execution risk

</div>
