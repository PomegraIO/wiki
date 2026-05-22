---
title: "Variation Margin Daily"
description: "Daily mark-to-market cash flows on derivatives and futures positions, settling realized gains and losses without waiting for contract expiration."
keywords:
  - variation margin
  - mark-to-market daily
  - futures settlement
  - derivatives cash flow
---

*A **variation margin** (or daily [mark-to-market](/wiki/mark-to-market/)) payment is the daily cash settlement between a futures trader and the clearinghouse, reflecting the unrealized gain or loss on an open [futures contract](/wiki/futures-contract/). Each trading day, positions are re-valued at settlement prices, and cash flows from winners to losers, ensuring no trader carries overnight [counterparty](/wiki/counterparty-credit-risk/) [risk](/wiki/counterparty-risk/).*

[Futures](/wiki/futures-contract/) and [cleared derivatives](/wiki/central-counterparty-clearing/) differ sharply from [forward contracts](/wiki/forward-contract/) in this respect. A [forward](/wiki/forward-contract/) buyer and seller face each other directly; if one side goes insolvent, the other loses everything. A [futures](/wiki/futures-contract/) contract is guaranteed by the clearinghouse, which forces daily cash settlement, eliminating accrued losses that could cascade if a trader defaults.

This daily settlement mechanism is one reason [futures](/wiki/futures-contract/) are safer and more standardized than [forwards](/wiki/forward-contract/), and why variation margin is essential to modern derivatives infrastructure.

<aside class="wiki-infobox">

| Item | Detail |
|---|---|
| **Timing** | Daily, after markets close; settlement usually next business day |
| **Who pays** | Trader with unrealized loss pays; trader with unrealized gain receives |
| **Clearinghouse role** | Acts as [central counterparty](/wiki/central-counterparty-clearing/), guarantees settlement |
| **Amount** | Change in contract value from prior day's settlement price to current settlement price |
| **Margin call** | If account balance falls below [initial margin](/wiki/initial-margin/), broker demands additional [maintenance margin](/wiki/maintenance-margin/) |
| **[Futures](/wiki/futures-contract/) vs. [forwards](/wiki/forward-contract/)** | Futures settle daily; forwards settle at maturity (or OTC, with less frequency) |

</aside>

## How daily mark-to-market works

A trader buys a crude oil [futures](/wiki/futures-contract/) contract at $75/barrel. The contract is standardized at 1,000 barrels = $75,000 notional value.

**Day 1 settlement**: Oil rises to $75.50/barrel. The contract is now worth $75,500. The trader's unrealized gain is $500. The clearinghouse credits $500 to the trader's account and debits it from the seller's account (or the aggregate seller account). The seller receives a [margin call](/wiki/margin-call-forex/) for that amount.

**Day 2 settlement**: Oil falls to $75.20/barrel. The contract is now worth $75,200. The trader's unrealized gain relative to $75.50 is −$300. The clearinghouse debits $300 from the trader and credits the seller. The trader's account now shows a net gain of $200 ($500 − $300).

**Day 3 settlement**: Oil rises to $76/barrel. The contract is now worth $76,000. The trader's unrealized gain relative to $75.20 is +$800. The clearinghouse credits $800. The trader's cumulative unrealized gain is now $1,000 ($200 + $800).

This continues daily until the trader closes the position or the contract expires. At expiration, the final variation margin settles, and the position is closed.

## Variation margin vs. initial and maintenance margin

The trader must also post **[initial margin](/wiki/initial-margin/)** upfront—typically 5–20% of the contract notional value, depending on [volatility](/wiki/volatility-index-futures/) and regulatory rules. For the crude contract above, initial margin might be $3,000–$4,000.

As variation margin drains the account daily, the balance falls. Once it drops below a defined **[maintenance margin](/wiki/maintenance-margin/)** threshold (often 75% of initial margin), the broker issues a **[margin call](/wiki/margin-call-forex/)**. The trader must deposit cash to bring the account back to initial margin level, or the broker will forcibly close the position.

**Example**: Initial margin $4,000, [maintenance margin](/wiki/maintenance-margin/) $3,000. If variation margin losses reach $1,500, the account balance is $2,500, below the $3,000 threshold. The trader must deposit $1,000 immediately, or lose their position.

This daily reconciliation prevents losses from accruing. A trader cannot owe $100,000 on a failed [futures](/wiki/futures-contract/) position because the clearinghouse would have forced liquidation long before losses approached that magnitude.

## Risk mitigation: the clearinghouse guarantee

The variation margin system protects the financial system. In the 1987 [stock market crash](/wiki/black-monday-1987/), equity markets seized because settlement [risk](/wiki/settlement-risk/) exploded; trades executed but settlement was delayed, creating massive [counterparty](/wiki/counterparty-credit-risk/) [risk](/wiki/counterparty-risk/). [Futures](/wiki/futures-contract/) markets, by contrast, continued functioning because daily variation margin kept clearing houses solvent.

When MF Global collapsed in 2008, the firm had not misappropriated customer [futures margin](/wiki/forex-margin/), so [futures](/wiki/futures-contract/) accounts were protected. The lesson: daily settlement prevents [principal](/wiki/principal-trading/) risk buildup.

However, variation margin can also **procyclically increase stress** during sharp moves. In March 2020, oil futures collapsed from $50 to negative territory, and traders faced extreme variation margin demands. Some faced [forced liquidation](/wiki/liquidation/). A trader with a short position who had meant to hold for months was hit with massive gains, requiring deposits they did not have, forcing them to sell at the worst moment.

## Initial margin requirements: the newer regulatory push

Since the 2008 crisis, regulators have pushed for **higher initial margin** on [uncleared derivatives](/wiki/derivative-accounting-hedging/). The Dodd-Frank Act mandated that [cleared](/wiki/central-counterparty-clearing/) [swaps](/wiki/swap/) have both initial margin (to cover tail-risk moves over a few days) and variation margin (daily settlement).

For [uncleared swaps](/wiki/derivative-accounting-hedging/), banks must now exchange initial margin with counterparties, mimicking the [futures](/wiki/futures-contract/) model. This has made [OTC derivatives](/wiki/over-the-counter-market/) more expensive and liquid because of the [capital](/wiki/capital-allocation-activism/) tied up in margin collateral.

## Operational mechanics: T+1 and T+2

Most [futures](/wiki/futures-contract/) exchanges settle variation margin **T+1** (next business day). A trade executed Wednesday settles Thursday. For some contracts (especially index futures and options), settlement is **T+2** (two days).

Real-world flow:

1. **Market close** (4 PM Eastern for NYMEX oil): Exchange calculates settlement prices.
2. **After hours** (5–6 PM): Clearinghouse calculates variation margin for all accounts.
3. **Broker notification** (evening): Your broker tells you if you owe or are owed.
4. **Next morning** (T+1): Cash transfers via the [Federal Reserve](/wiki/federal-reserve/) wiring system (FEDWIRE).
5. **Account update**: Your broker updates your balance.

A trader who loses heavily can face a [margin call](/wiki/margin-call-forex/) on Thursday morning, requiring a deposit by Friday close or forced liquidation on Monday.

## Currency and cross-border variation margin

[Futures](/wiki/futures-contract/) traded on non-domestic exchanges complicate variation margin. A US trader buying a [crude oil](/wiki/crude-oil/) contract on the [ICE](/wiki/ice-intercontinental-exchange/) (London) must post margin in pounds sterling or US dollars. If sterling depreciates, the trader's margin in pounds is worth less in dollars, triggering a currency margin call. [Futures](/wiki/futures-contract/) brokers handle currency conversion, but the trader bears [currency risk](/wiki/currency-risk/).

## Historical context: why daily settlement emerged

Before clearinghouses enforced daily settlement, [forwards](/wiki/forward-contract/) and early [futures](/wiki/futures-contract/) accumulated accrued losses. The [1929 stock crash](/wiki/wall-street-crash-of-1929/) exposed the danger: traders owed vast sums they could not pay, and the failures cascaded. The creation of the [CBOT](/wiki/cme-group/) clearinghouse in the 1920s pioneered daily settlement to prevent this.

## Variation margin in modern electronic trading

Today's [algorithmic traders](/wiki/algorithmic-trading/) and [high-frequency trading](/wiki/high-frequency-trading/) firms are acutely aware of variation margin. A firm might hold thousands of positions and face swings of millions daily. They use **real-time margin monitoring** systems that forecast daily P&L and [margin calls](/wiki/margin-call-forex/) to stay ahead of liquidity needs.

A poorly managed algorithm that accumulates a large loss can burn through margin faster than a trader can deposit capital, forcing forced [liquidation](/wiki/liquidation/). This happened to Knight Capital in 2012, when a rogue algorithm took a $7 million position that swung to $460 million in losses; the firm's margin account could not absorb the loss.

## Practical implications for traders

1. **Size your positions for margin capacity.** If you have $50,000 in margin and a [crude oil](/wiki/crude-oil/) [futures](/wiki/futures-contract/) contract has initial margin of $4,000 and can swing ±$500/day in volatile markets, you can afford ~10 contracts before variation margin risk becomes acute.

2. **Expect forced liquidation.** If you refuse or cannot meet a [margin call](/wiki/margin-call-forex/), your broker will liquidate positions—often at the worst moment.

3. **Manage [leverage](/wiki/leverage-ratio-forex/) conservatively.** [Margin](/wiki/forex-margin/) lets you trade larger notional amounts, but variation margin can wipe out smaller accounts in a day or two of adverse moves.

4. **Understand contract roll risk.** As a contract approaches expiration, variation margin can spike because implied delivery becomes real. Rolling into a later contract incurs transaction costs and [liquidity risk](/wiki/liquidity-risk/).

<div class="wiki-seealso">

### Closely related
- [Futures Contract](/wiki/futures-contract/) — Standardized derivative contract traded on exchanges with daily settlement
- [Initial Margin](/wiki/initial-margin/) — Upfront margin required to enter a position
- [Maintenance Margin](/wiki/maintenance-margin/) — Minimum account balance required to hold a position
- [Mark-to-Market](/wiki/mark-to-market/) — Daily revaluation of positions at settlement prices

### Wider context
- [Central Counterparty Clearing](/wiki/central-counterparty-clearing/) — Clearinghouse as intermediary guaranteeing settlement
- [Counterparty Risk](/wiki/counterparty-risk/) — Risk that the other party to a trade will default
- [Settlement Risk](/wiki/settlement-risk/) — Risk during the period between trade execution and settlement
- [Derivatives Exchange](/wiki/derivatives-exchange-crypto/) — Platform trading standardized derivative contracts

</div>
