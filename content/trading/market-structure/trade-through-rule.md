---
title: "Trade-Through Rule"
description: "A regulatory prohibition on executing trades at inferior prices when better quotes are available on other venues."
keywords:
  - trade-through rule
  - best execution
  - market regulation
  - consolidated tape
  - price protection
  - order routing
image: "/svg/trading.svg"
---

*The **trade-through rule** is a regulatory mandate that forbids a broker or exchange from executing a customer's trade at a price worse than the best price currently displayed on any competing venue. Enforced by the SEC's Regulation SHO and national market system rules, it functions as the cornerstone of modern equity market fragmentation—ensuring that investors' limit orders sitting on one exchange cannot simply be jumped by an execution at an inferior price elsewhere.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trade-Through Rule — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">The regulatory mandate protecting investors from inferior-price execution.</div>

|   |   |
|---|---|
| **What it is** | A prohibition on executing a trade at a price worse than a better quoted price on another venue |
| **Enforcer** | SEC, via Regulation SHO and national market system rules |
| **Core protection** | Prevents "trade-through": jumping a displayed limit order by executing at worse price elsewhere |
| **Key data source** | [Securities Information Processor](/securities-information-processor/) consolidates best bid/ask across venues |
| **Venues covered** | National exchanges, [alternative trading systems](/alternative-trading-system/), certain OTC markets |
| **Practical effect** | Forces broker order routing to find best displayed price |

</aside>

## Why fragmentation created the need for a trade-through rule

For most of the 20th century, the New York Stock Exchange was not truly fragmented. Nearly all equities traded on a single venue, and execution was straightforward: your order found the best bid or ask quote on the NYSE. When electronic communication networks and regional exchanges emerged in the 1990s, the market structure became fractured across dozens of venues. On any given moment, the best bid on NASDAQ might be $50.10, while a better asking price sits resting on an alternative trading system at $50.05. Without a rule to prevent it, a broker executing your sell order might fill it at the inferior $50.00 price on yet another venue, pocketing the spread.

The [trade-through rule](/trade-through-rule/) emerged to protect investors from this exact scenario. It mandates that before executing a trade, a broker must check whether a better price is currently displayed anywhere in the national market system, and either execute at that better price or wait.

## The consolidation problem: how do brokers know the "best" price?

The rule's teeth depend entirely on real-time price discovery. If a broker cannot quickly see every price displayed across all venues, the rule becomes unenforceable. That is why the SEC created a [Securities Information Processor](/securities-information-processor/)—a central utility that gathers bids, asks, and last-sale data from every eligible marketplace and republishes them as the official consolidated tape. Before a broker routes an order, they consult the consolidated tape to verify no better price exists. This millisecond-scale lookup is now automated and embedded in order-management systems.

Yet the rule has always carried exceptions. A broker may trade through a better price if that price is not yet reflected in the consolidated feed (a data lag), or if the better-quoted venue cannot execute the full order size, or if the broker uses an internalization model with established "firm" quotes. These carve-outs generate endless regulatory debate—critics argue they erode investor protection, while brokers contend they enable competitive execution strategies.

## When brokers can (and cannot) ignore the rule

The rule is not absolute. If a venue's best bid is $50.10 but only for 100 shares, and you have an order for 500 shares, a broker may execute the full order at $50.05 on another venue rather than splitting execution across both venues. This "partial execution exception" reflects market realism—traders often value speed and certainty of fill over sub-cent improvements. Similarly, orders routed to internalizers—brokers' proprietary systems—are held to a slightly weaker standard: they must match the national best bid and ask, but need not wait for a venue to display it if there is a fractional delay.

The 2005 Regulation National Market System modernized the rule's mechanics, replacing the old paper-based system with electronic requirements for automatic updates and faster notification of trade executions. Yet loopholes remain. Brokers may use [alternative trading systems](/alternative-trading-system/) as execution venues that operate under different transparency and reporting rules, sometimes obscuring whether a true trade-through has occurred.

## The economic debate: investor protection versus execution quality

Conventional wisdom holds that the rule protects retail investors from sloppy or self-interested execution. A broker cannot cheap out and fill your order at a worse price just because that venue pays the broker higher rebates. But critics—especially high-frequency traders and academic researchers—argue the rule impedes innovation and market efficiency. They contend that strict price-matching rules create fragmentation, prevent meaningful competition on non-price dimensions (speed, information), and lead brokers to split orders unnecessarily, reducing the ability to execute large trades seamlessly.

Most economists and regulators have sided with investor protection: the rule persists and has been tightened several times. But the debate resurfaces regularly as new market structures—dark pools, exchanges abroad, cryptocurrency networks—test the rule's boundaries.

## How technology enforcement changed the game

Enforcement of the trade-through rule requires sub-second monitoring. The SEC and [FINRA](/), the industry regulator, run surveillance systems that scan millions of trades daily to identify violations. A broker caught executing a customer's order at a worse price when a better price was displayed faces fines and restitution to customers. The largest cases have involved major brokers: Citadel Securities, Virtu Financial, and others have paid multi-million-dollar settlements for reported trade-through violations. Automated checking has made violations rarer, but arbitrage-seeking algorithms sometimes discover microsecond windows where prices move faster than the consolidated tape can update.

## See also

<div class="wiki-seealso">

### Closely related

- [Securities Information Processor](/securities-information-processor/) — the utility that consolidates prices across venues so trade-through enforcement is possible
- [Alternative Trading System](/alternative-trading-system/) — venues that operate under different transparency rules, sometimes testing trade-through boundaries
- [Market Microstructure Theory](/market-microstructure-theory/) — the framework explaining how trading rules and information shape price formation
- [Best Execution](/best-execution/) — the broker obligation to obtain optimal execution, of which trade-through protection is a part
- [Price Discovery](/price-discovery/) — the mechanism by which prices incorporate all available information across markets

### Wider context

- [Stock Exchange](/stock-exchange/) — centralized venue; trade-through rule applies across all venues in a national system
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator that enforces the trade-through rule
- [Bid-Ask Spread](/bid-ask-spread/) — the gap between best bid and ask; trade-through rule prevents arbitrage of this spread against customers
- [Market Maker Trading](/market-maker-trading/) — dealers who post quotes subject to the rule's protections

</div>
