---
title: "Locked and Crossed Market Rules Under Reg NMS"
description: "What locked and crossed markets are and how Reg NMS Rule 610(d) prohibits them to protect price discovery."
keywords:
  - locked crossed market rules
  - locked market regulation
  - crossed market
  - reg nms rule 610
  - market quality rules
  - price protection rule
  - trading halts
---

*A **locked market** occurs when the best ask price on one exchange equals the best bid price on another, eliminating any spread. A **crossed market** is even worse: the best ask is higher than the best bid, an obvious arbitrage. Under **Reg NMS Rule 610(d)**, exchanges and market makers are required to prevent locked and crossed markets through automated procedures—quoting conservative prices, routing orders, or pausing trading. These rules exist because locked and crossed markets undermine price discovery and create opportunities for sophisticated traders to exploit retail investors.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Locked and Crossed Markets — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation." />

<div class="wiki-infobox-caption">Rule 610(d) bans market dislocations that indicate exchange fragmentation.</diva>

|   |   |
|---|---|
| **Locked market** | Best ask (on Exchange A) = Best bid (on Exchange B); zero spread |
| **Crossed market** | Best ask (on Exchange A) > Best bid (on Exchange B); prices inverted |
| **Who must prevent it** | Exchanges, self-regulatory organizations, and market makers |
| **Regulatory basis** | Reg NMS Rule 610(d), adopted by the SEC in 2005 |
| **Consequences of violation** | Market maker fine or trading suspension; exchange censure or loss of self-regulatory authority |
| **Modern frequency** | Rare due to automated systems; occur mainly during volatility or technical failure |
| **Remedy if it happens** | Exchange must halt trading, cancel affected trades, or activate manual intervention |

</aside>

## What Is a Locked Market?

A **locked market** emerges when the best ask price on one exchange precisely equals the best bid price on another. Suppose Apple stock has a best bid of $149.50 on Nasdaq and a best ask of $149.50 on the NYSE. No spread exists. An alert trader could theoretically buy on the NYSE at $149.50 and immediately sell on Nasdaq at $149.50, earning zero profit. But the locked market itself is a signal of market dysfunction: why would quotes be so tightly aligned that no arbitrage profit exists?

The answer is usually that one exchange is stale or lagging in updating quotes. Bid and ask prices should continuously adjust as new information arrives. If two venues show the same price with zero spread, it suggests one or both are not trading actively, or data is flowing in from one venue to another with a delay.

## What Is a Crossed Market?

A **crossed market** is the pathological extreme: the best ask price on one exchange exceeds the best bid price on another. For example, the NYSE's best ask is $149.52, while Nasdaq's best bid is $149.50. Arbitrage is immediately profitable: buy at $149.50, sell at $149.52, pocket $0.02. But a crossed market is so obviously broken that it screams of data latency, a quote error, or a failure of a market maker to update prices.

Crossed markets are rarer than locked markets because the profit opportunity is instantly visible to algorithmic traders, and any routed order will immediately execute and uncross the market. But they still occur, especially during periods of extreme volatility when different venues' data feeds fall temporarily out of sync, or when a market maker's quote is stale.

## Why Rule 610(d) Prohibits Them

Regulation SHO Rule 610(d) was adopted by the SEC in 2005 as part of the Regulation National Market System (Reg NMS). The rule prohibits exchanges and market makers from displaying bids and offers that create locked or crossed markets. The regulatory rationale is twofold.

**First, they undermine price discovery.** Prices are supposed to continuously update to reflect new information and the balance of supply and demand across all venues. A locked or crossed market suggests prices are inaccurate or lagging. If a retail investor sees a $149.50 bid on one venue and places a sell order there, not knowing that another venue is already trading at $149.52, they leave money on the table. Locked and crossed markets create mispricing that harms price discovery.

**Second, they invite manipulation and harm retail traders.** A sophisticated trader with access to all venue data can spot a locked or crossed market faster than a retail investor can act. The professional can buy on the low-priced venue and sell on the high-priced venue, or route orders to exploit the dislocation. Retail investors, by contrast, are slower and less informed, so they bear the costs of liquidity fragmentation.

## How Market Makers Must Prevent Locked and Crossed Markets

Reg NMS Rule 610(d) imposes an affirmative duty on market makers and exchanges to prevent locked and crossed markets. In practice, this means:

**Quote adjustment.** A market maker must not display a bid or ask if doing so would lock or cross the market. If a market maker is a buyer at $149.50 and sees that the best ask elsewhere is also $149.50, the market maker must either pull its bid or lower it to $149.49. Similarly, if the market maker's ask would cross a bid on another venue, it must raise the ask or withdraw it.

**Order routing.** Many market makers use **order routing rules** that automatically check multiple venues before executing a trade. If a customer order would trigger an execution that locks or crosses the market, the routing algorithm avoids that venue and routes instead to a venue with a better price or accepts the customer order at a better price than the locked/crossed level.

**Trading pauses.** Exchanges are required to suspend trading when a locked or crossed market is detected and cannot be quickly corrected. The halt gives market makers time to adjust quotes and allows data feeds to resynchronize.

**Technical infrastructure.** Modern exchanges operate with microsecond-precision clock synchronization and high-speed data feeds to detect and prevent locked and crossed markets almost instantly. A market maker's quote system is programmed to reject any quote that would trigger a lock or cross.

## Real-World Occurrences

Locked and crossed markets were more common in the early 2000s, shortly after exchanges fragmented and the multi-venue landscape emerged. Before electronic systems were optimized, quote delays between venues were common, and traders saw opportunities to profit from dislocations.

Since 2005, automation has made locked and crossed markets very rare. However, they still occur under specific conditions:

**Market volatility.** During flash crashes, rapid news, or geopolitical shocks, volatility can outpace the speed at which quotes update across venues. In the 2010 flash crash, several locked and crossed market conditions were briefly observed as the market dislocated.

**Technical failures.** If an exchange's data feed is delayed or a market maker's quoting system fails to account for quotes on a competing venue, locked or crossed markets can result. The FINRA and SEC monitor for these and typically fine the responsible party.

**Low-volume times.** For less-liquid stocks (especially small-cap or microcap equities), gaps between bid and ask can be wide, but liquidity is sparse. Locked or crossed markets can briefly occur when orders are small and don't fully clear across venues.

## The Order Protection Rule (Rule 610(c))

Reg NMS Rule 610(d) works hand-in-hand with the **Order Protection Rule (Rule 610(c))**, which requires that when a trade would execute at a price that locks or crosses another venue's quote, the order must be routed to that better-priced venue instead. Rule 610(c) ensures that orders are not filled at stale or worse prices when better prices are available, even if those prices are on a competing venue.

Together, Rules 610(c) and 610(d) create a system of mutual policing: venues and market makers can't display bad quotes (610(d)), and orders can't execute against bad quotes if better ones exist (610(c)).

## Impact on Market Fragmentation

The prohibition on locked and crossed markets reflects a broader regulatory philosophy: acknowledge that markets are fragmented across multiple venues (since no single exchange dominates equity trading) and impose rules to ensure that fragmentation doesn't harm price discovery or retail investors. By requiring market makers to quote conservatively and by routing orders to the best available prices, Reg NMS tried to preserve the benefits of competition and speed while avoiding the worst harms of fragmentation.

Critics argue that the strict enforcement of these rules has led to very narrow spreads and rapid trading, which benefits algorithmic traders and market makers but doesn't directly translate to lower transaction costs for retail investors. Supporters counter that the rules have improved price quality and reduced the incidence of bad executions.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — locked and crossed markets eliminate or invert the spread
- [Market Maker Trading](/market-maker-trading/) — market makers bear the duty to prevent locks and crosses
- Order Protection Rule — Reg NMS Rule 610(c) complements 610(d)
- [Alternative Trading System](/alternative-trading-system/) — ATS venues must also follow Rule 610(d)
- [Price Discovery](/price-discovery/) — locked and crossed markets harm it
- [Regulation SHO](/regulation-sho/) — Reg NMS is part of the broader SHO framework

### Wider context

- [Stock Exchange](/stock-exchange/) — regulated venues subject to Reg NMS
- Fragmentated Market — the multi-venue ecosystem that Rule 610(d) governs
- [High Frequency Trading](/high-frequency-trading/) — algorithmic traders quickly exploit any dislocation
- 2010 Flash Crash — an incident where locked and crossed markets briefly occurred

</div>
