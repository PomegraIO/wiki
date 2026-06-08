---
title: "Last Look Execution in FX Markets"
description: "Last look execution in forex allows a liquidity provider to reject a trade after the client hits the quote, raising fairness concerns and reducing fill certainty."
keywords:
  - last look execution
  - forex execution
  - fx liquidity
  - trade rejection
  - market microstructure
  - currency trading
---

*A **last look** in forex execution is a brief window (typically a few milliseconds) during which a liquidity provider can cancel or reject a trade request after a client has clicked to accept the quoted price. The provider uses this window to hedge risk and screen for adverse selection. It is legal and industry-standard, yet controversial—critics argue it amounts to selective order rejection and tilts the execution advantage toward the dealer.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Last Look Execution — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A mechanism that lets dealers refuse trades after client acceptance.</div>

|   |   |
|---|---|
| **Typical window** | 10–50 milliseconds after client clicks |
| **Rejection rate** | Often 5–20% of incoming trades, depending on market conditions |
| **Primary use** | Risk hedging and adverse selection filtering |
| **Regulatory stance** | Permitted under MiFID II and US rules; disclosure encouraged |
| **Impact on traders** | Lowers fill certainty; quoted prices may not execute |
| **Fee consequences** | Some brokers disclose rejection rates; others do not |

</aside>

## How last look works in practice

When a retail or institutional client trades currency through a broker or electronic [counterparty](/counterparty-risk/), the dealer quotes a two-way price (bid and ask). The client hits the ask to buy or hits the bid to sell. Normally, the trade executes immediately. With last look, a fractional delay is introduced.

After the client's click reaches the dealer's system, the dealer's algorithm has a window—typically 10 to 50 milliseconds—to review the trade before final confirmation. During this window, the dealer may:
- **Hedge the trade**: Lock in an offsetting position in the interbank market to neutralize risk.
- **Screen for adverse selection**: Check whether the client's order matches a suspicious pattern (e.g., front-running detection, unusually large size relative to market depth).
- **Reject the trade**: Send a "last look rejection" message, and the deal fails.

If the dealer approves, the trade settles at the original quoted price. If rejected, the client is offered an alternative price (often one that has moved against them) or the trade is cancelled entirely.

## Why dealers use last look

The core motivation is hedging and cost control. In the 2–10 milliseconds before the dealer can offset the position in the interbank market, the dealer is "short duration risk." Market prices move. A 10-pip move in EUR/USD during that window costs the dealer money. Last look lets the dealer back out of trades where the market has moved sharply during transmission latency.

Adverse selection filtering is the secondary reason. Some clients engage in strategies that are profitable at the dealer's expense—for instance, trading spoofed prices or following predictable intraday patterns that the dealer's machine learning detects. Last look allows the dealer to refuse these orders without closing the account.

## The fairness controversy

Critics argue last look violates the spirit of price transparency. The client sees a quoted price and clicks, expecting execution. But the dealer retains a unilateral right to cancel. This creates an asymmetry: clients cannot "last look" the dealer, and the dealer bears no penalty for rejections beyond the client's potential frustration.

The fairness argument has two prongs:

**Information asymmetry**: The dealer's algorithm sees the client's order and has microseconds to decide whether it is profitable or adverse. The client cannot see the dealer's hedging execution or algorithm state. This imbalance can be exploited.

**Selective rejection**: A dealer might reject large winning trades and accept small losing ones, effectively skimming the client's best opportunities. Regulators have cautioned against this behavior, though proving it requires trade-by-trade audit data.

## Regulatory and market-wide responses

By the early 2020s, last look had become common in the spot forex market, and regulatory concern mounted. The Financial Conduct Authority (FCA) in the UK and the European Securities and Markets Authority (ESMA) began requiring disclosure of last look practices and rejection rates.

Under [MiFID II](/dodd-frank-act/), best execution guidelines recommend that brokers disclose whether last look is used and report rejection statistics. Similarly, US [FINRA](/finra/) rules and SEC guidance have emphasized transparency, though last look itself is not banned.

Some institutions responded by eliminating last look or capping rejection rates (e.g., 5%). Others bundled last look into tiered service offerings: premium clients receive faster, last-look-free execution; standard clients accept last look as the cost of tighter spreads.

## Impact on fill rates and spreads

Traders typically experience the trade-off between tighter spreads and fill certainty. A dealer offering 1-pip [bid-ask-spread](/bid-ask-spread/) on EUR/USD *with* last look may guarantee fill only 80–95% of the time. A dealer offering a 1.5-pip spread *without* last look guarantees fill 99%+.

For algorithmic traders and high-frequency strategies, rejection uncertainty increases slippage. If an order is rejected 15% of the time, the trader must assume a 15% chance of having to re-quote and re-execute at a worse price. Over thousands of trades, this compounds.

For casual traders, last look is often invisible. They quote a price, click, and the trade appears filled. Rejections happen on volatile days or with unusually large orders, and are attributed to "market volatility" rather than dealer discretion.

## The latency advantage asymmetry

Last look amplifies the inherent latency advantage of the dealer. A retail client connects via the internet (tens of milliseconds of latency). The dealer's systems sit in co-located data centers, where market data and liquidity pools are microseconds away. Last look gives the dealer a second chance to hedge at superior prices if the market has moved. The client has no equivalent option.

This is distinct from the market-maker function per se. Market makers need the ability to widen spreads when volatility spikes, and they do face real risk. But last look, in effect, lets them unwind risk *after* seeing the client's order, rather than before. The dealer and client are not on equal footing.

## Modern alternatives and trends

Some electronic venues and brokers have opted for "non-last-look" execution models as a competitive differentiation. Direct-access platforms and institutional MTFs sometimes offer pricing with explicit post-trade reporting and no dealer rejection window.

Others have introduced *"last look with price improvement"*: if the market moves in the client's favor during the last-look window, the client receives the improved price; if it moves against them, the dealer can reject. This softens the asymmetry.

As [algorithmic trading](/algorithmic-trading/) and automated execution systems evolve, the debate continues. Technology now allows sub-millisecond hedging on some pairs, reducing the dealer's genuine risk window. Whether last look persists as a tool or becomes a relic depends on continued regulatory scrutiny and competitive pressure from last-look-free venues.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-ask spread](/bid-ask-spread/) — the dealer's margin on forex quotes
- [Market maker trading](/market-maker-trading/) — how dealers manage inventory and risk
- [Algorithmic trading](/algorithmic-trading/) — automated execution strategies vulnerable to rejection uncertainty
- [Counterparty risk](/counterparty-risk/) — dealer credit risk in currency trading

### Wider context

- [Over-the-counter market](/over-the-counter-market/) — structure of the forex market and dealer networks
- [Execution risk](/execution-risk/) — broader sources of slippage and failure to fill
- [Currency volatility](/currency-volatility/) — what drives intraday price moves
- [Regulation A](/regulation-a/) — disclosure and fairness rules in securities markets

</div>
