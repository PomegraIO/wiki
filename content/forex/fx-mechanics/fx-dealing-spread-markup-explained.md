---
title: "How Brokers Mark Up the Forex Spread"
description: "How retail forex brokers widen the interbank spread before passing it to clients, the economics behind the markup, and how to estimate effective costs."
keywords:
  - forex spread markup broker
  - how brokers mark up spread
  - retail forex spread cost
  - interbank spread vs retail
  - forex dealing spread
image: "/svg/forex.svg"
---

*Retail [forex brokers](/broker/) take the wholesale [bid-ask spread](/bid-ask-spread/) they pay at the interbank market and widen it before quoting prices to clients—a markup that is the broker's primary revenue source and a hidden cost that erodes returns.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">How Brokers Mark Up the Forex Spread — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">The gap between what brokers pay and what they charge clients is their profit.</div>

|   |   |
|---|---|
| **Interbank spread** | Major [currency pairs](/currency-volatility/) (EUR/USD, GBP/USD) trade at 1–2 pips wholesale; brokers quote 2–5 pips retail |
| **Markup** | Brokers widen the spread by 50–200% depending on pair liquidity, client account size, and volatility regime |
| **Broker revenue** | The spread markup is often the only fee; many retail brokers advertise "zero commissions" but profit entirely from the spread |
| **Liquidity tiers** | Major pairs have tighter spreads; exotic pairs ([emerging market currencies](/currency-risk/)) have 5–20+ pip spreads |
| **Market stress** | Spreads blow out during [volatility](/currency-volatility/) spikes (central bank announcements, geopolitical shock) because interbank [liquidity](/liquidity-risk/) dries up |

</aside>

## The Interbank Market vs. Retail Quotes

The interbank [foreign exchange](/currency-risk/) market is where banks, institutional investors, and central banks trade currencies. In this market, a major pair like EUR/USD might have a [bid-ask spread](/bid-ask-spread/) of 1 pip (0.0001 for EUR/USD). A buyer can sell euros at 1.0850 and a seller can buy at 1.0851—a 1 pip difference. Large institutional [currency traders](/currency-risk/) and hedge funds access this pricing through prime brokers or electronic communication networks (ECNs).

Retail [brokers](/broker/) do not have direct access to the interbank market in the way large banks do. Instead, they aggregate liquidity from multiple sources—interbank dealers, ECNs, and other brokers—and then mark up the resulting spread before quoting it to retail clients. A retail trader logging into their broker's platform sees a bid of 1.0850 and an ask of 1.0854—a 4 pip spread—even though the underlying interbank spread is only 1 pip.

The difference—the 3 pips between the interbank quote and the retail quote—is the broker's markup and profit.

## Why Brokers Mark Up Spreads

Brokers mark up spreads for several rational economic reasons:

**Risk absorption.** When you trade with a broker, the broker becomes your counterparty. If you buy EUR/USD at their ask price, the broker sells euros to you. The broker is now long USD and short EUR. To hedge this position, the broker must offset it in the interbank market, which takes time and costs money (the broker must buy back EUR at the market's ask, paying the full interbank spread). If the market moves against the broker in the interim, the broker absorbs the loss. By widening the retail spread, the broker builds a buffer to absorb this [counterparty risk](/counterparty-risk/).

**Operating costs.** Brokers maintain technology infrastructure, customer support, regulatory compliance, and trading desks. These costs must be recovered from clients. Some brokers claim to pass "direct market access" (DMA) to the interbank market, but they still incur operational expenses that must come from somewhere.

**Inventory and hedging costs.** If a broker receives more client buy orders for EUR/USD than sell orders, the broker accumulates long EUR exposure. Holding this inventory is risky; the broker must hedge dynamically, and hedging incurs costs. During periods of one-sided order flow, the broker widens spreads to discourage additional imbalanced orders.

**Client acquisition and retention.** Brokers offer trading accounts, deposit bonuses, and customer support—services financed by the spread. A broker with lower spreads but better educational resources may generate more trading volume, offsetting tighter margins.

## The Markup Varies by Pair and Market Condition

Not all currency pairs have the same markup. Major pairs (EUR/USD, GBP/USD, USD/JPY) have tight interbank spreads and minimal retail markups, often 1–3 pips. These pairs have deep [liquidity](/liquidity-risk/), so the broker's hedging costs are low and risk is minimal.

Exotic pairs—currencies from emerging markets or smaller developed economies—have far wider spreads. A pair like USD/BRL (Brazilian real) might trade at 5–10 pips interbank and 15–30 pips retail, because the underlying [liquidity](/liquidity-risk/) is thin and [currency risk](/currency-risk/) is elevated. The broker must post wider quotes to compensate for the difficulty of hedging quickly.

During volatile periods—announcements from the [Federal Reserve](/federal-reserve/) or [European Central Bank](/european-central-bank/), geopolitical shocks, or sudden [inflation](/inflation/) reports—interbank spreads widen dramatically, and retail spreads widen even more. On a calm day, EUR/USD might trade at 2 pips interbank and 3 pips retail (1 pip markup). During a volatile announcement, the interbank spread might spike to 5 pips, and the retail spread to 15 pips. The markup percentage stays consistent or widens, depending on how stressed the broker's liquidity is.

## Estimating the Effective Cost of Trading

For a retail [forex trader](/currency-risk/), the spread is a direct drag on returns. Every trade incurs a cost equal to the spread times the notional amount traded.

Example: You trade 1 standard lot (100,000 units) of EUR/USD at a 4 pip retail spread. The spread cost is:

- 4 pips × 100,000 units = 4,000 units (of the counter-currency, USD)
- At EUR/USD ~1.08, that is approximately $4,320 in cost

If you make 20 round-trip trades per month (buy and sell), you pay the spread 40 times. At $4,320 per spread, that is $172,800 per month in spread costs on a single lot of notional exposure. Over a year, $2 million in friction alone. This assumes the trades break even before costs—a break-even trade loses money after spreads.

Professional traders who trade frequently must account for this rigorously. A strategy with a 52% win rate might look profitable until spread costs are deducted, at which point it becomes a loser. This is why [algorithmic trading](/algorithmic-trading/) in forex often requires very tight spreads (1–2 pips) to be economically viable; without them, even low-latency [execution](/execution-risk/) becomes unprofitable.

## How Clients Can Reduce Spread Costs

**Compare brokers.** Different brokers quote different spreads for the same pair at the same moment. Shopping around can reveal brokers offering tighter markups on major pairs. Online forex broker comparison tools display real-time spreads from multiple providers.

**Trade major pairs.** EUR/USD, GBP/USD, and USD/JPY have tight spreads because liquidity is abundant. Exotic pairs incur far higher costs.

**Trade during high-liquidity hours.** The [forex market](/currency-risk/) is a 24-hour global market, but liquidity concentrates during overlaps of major financial centers. When London (08:00 GMT) and New York (13:00 GMT) overlap, spreads tighten. Trading during Asian hours (minimal overlap) results in wider spreads.

**Use limit orders.** A [market order](/market-order/) to buy at the ask price incurs the full quoted spread. A [limit order](/limit-order/) to buy at a lower price may fill at a tighter spread (or fail to fill). For frequent traders, limit orders reduce average spread cost, though they introduce [execution risk](/execution-risk/).

**Opt for commission-based pricing.** Some institutional-grade brokers charge a commission (e.g., $5–10 per million traded) instead of a spread markup. For high-volume traders, a fixed commission is cheaper than paying a variable markup on every trade.

## The Markup and Profit Motive

The spread markup is the broker's economic engine. In an unregulated or loosely regulated market, some brokers employ predatory tactics: they widen spreads during high-impact news announcements, deliberately slowing order execution to catch traders on bad fills, or refusing to close profitable positions ("no dealing desk" brokers sometimes practice this). Regulated brokers in developed jurisdictions are subject to [anti-manipulation rules](/finra/) and are more transparent about spreads.

A key hidden cost emerges with "market maker" brokers (also called dealing desk brokers): these firms take the opposite side of client trades, betting that clients lose money. The wider the spread, the more the broker profits if clients lose. This creates a perverse incentive: the broker makes money when clients lose. Some dealing desk brokers deliberately quote worse spreads to clients with high profitability, hoping to recover losses by widening their edge.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — The fundamental mechanic of how spreads are quoted and why they widen
- [Foreign Exchange (Currency Risk)](/currency-risk/) — Overview of forex markets and the instruments traded
- [Broker](/broker/) — The role of brokers in currency trading and their economic model
- [Liquidity Risk](/liquidity-risk/) — How thin liquidity in exotic pairs causes wider spreads
- [Execution Risk](/execution-risk/) — The cost and timing risks of trading in live markets
- [Currency Volatility](/currency-volatility/) — How volatility spikes widen spreads during crises

### Wider context

- [Algorithmic Trading](/algorithmic-trading/) — Automated strategies that minimize spread costs through speed and volume
- [Market Order](/market-order/) — How immediate execution incurs full spread cost
- [Limit Order](/limit-order/) — An alternative to market orders that can reduce effective spread
- [Counterparty Risk](/counterparty-risk/) — Why brokers require a markup to absorb the risk of being your counterparty
- [Central Bank](/central-bank/) — Announcements that spike volatility and widen spreads
- [Spot Exchange Rate](/spot-rate/) — The reference rate used in forex trading

</div>
