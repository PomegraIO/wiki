---
title: "Reg NMS Access Fee Cap Explained"
description: "Reg NMS Rule 610 caps exchange access fees at 30 cents per 100 shares. Learn how the 30-mil cap shapes market structure and order routing."
keywords:
  - reg nms access fee cap
  - regulation nms access fees
  - 30 mil per share cap
  - exchange access fee cap
image: "/svg/regulation.svg"
---

*Regulation NMS Rule 610, adopted by the SEC in 2007, imposes a maximum fee that stock exchanges can charge to execute orders: 30 cents per 100 shares (0.3 mills per share, or 30 mils). This cap, known as the **access fee cap**, constrains the profits exchanges can extract from trading and shapes how [brokers](/broker/) route orders, where they route them, and how the broader market microstructure is financed.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Reg NMS Access Fee Cap — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation." />

<div class="wiki-infobox-caption">The 30-mil cap limits exchange revenue and forces trade-offs in exchange-offered liquidity incentives.</div>

|   |   |
|---|---|
| **Rule** | SEC Regulation NMS Rule 610(c) |
| **Cap level** | $0.0030 per share (0.3 mills) |
| **Effective** | January 2008 |
| **What it covers** | Fees to execute orders matched on an exchange |
| **Rebate cap** | Liquidity-provision rebates capped at fee level |
| **Exceptions** | None; applies uniformly across all markets and security types |
| **Enforcement** | SEC oversight; non-compliance can trigger deregister action |

</aside>

## The Rule's Scope and Intent

Rule 610(c) stipulates that no exchange shall charge more than $0.0030 per share (30 mils, or three-tenths of a cent) to execute an order that is matched on that exchange. When you submit a market order to buy 100 shares at your broker, and the broker routes that order to, say, NASDAQ, NASDAQ may charge no more than 3 cents total (0.0030 × 100 shares).

The SEC's intent was to prevent exchanges from using their position as primary listing venues to extract monopoly rents. Before the cap, large exchanges could charge high access fees, knowing that brokers had limited alternatives. The cap forces exchanges to be price-competitive and helps ensure that brokers will route to the best venue by price, not be forced there by lack of alternatives.

## The 30-mil Number: Why This Cap?

The 30-mil figure emerged from SEC analysis of trading costs and a judgment that this level would constrain monopoly pricing while still allowing exchanges to operate and invest. It is not derived from some natural market price; it was an administrative choice. The SEC revisited the cap several times in subsequent years, proposing raises or adjustments, but ultimately left it at 30 mils.

In absolute terms, 30 mils is small—less than a penny per share. On a $100 stock, it represents 0.003% of the stock price. But aggregated across millions of shares traded daily, it is material: a $10 billion notional market in a liquid stock might incur tens of thousands of dollars in access fees in a single day.

## How Exchanges and Makers Navigate the Cap

Exchanges cannot charge more than 30 mils to access (execute against) orders on their books, but they can—and do—offer rebates or "maker rebates" to firms that *provide* liquidity (i.e., place orders that others execute against). A typical exchange might charge an "access fee" of, say, 30 mils and offer a "maker rebate" of 20 mils, netting the exchange 10 mils.

This structure creates an incentive for market participants to provide liquidity on that exchange (and leave standing orders waiting to be executed against). In principle, a broker executing a buy order on Exchange A might face a net cost of 30 mils; a broker *placing* a sell order there faces a 20-mil rebate, earning them money.

The rule does *not* cap maker rebates explicitly, but the SEC interprets Rule 610(c) to imply that rebates should not exceed the access fee cap. In practice, rebates are usually *less* than 30 mils, so the exchange profits on the spread.

## Impact on Market Structure

The 30-mil cap has reshaped how exchanges compete and how brokers route. Rather than competing solely on fees (all capped at the same level), exchanges compete on execution quality, order types, and rebate structures. A fast exchange with low latency might attract more order flow than a slower competitor, even if both charge 30 mils, because speed affects the rebate advantage.

The cap also constrained exchanges' ability to become virtual monopolies through pricing power. In the 1990s and early 2000s, the NYSE and NASDAQ could threaten brokers who didn't send sufficient order flow; with the cap, they lost that lever. The rise of alternative trading systems (ATSs) and regional exchanges became feasible partly because fee pressure was lightened; a broker could route to them without facing a price premium.

## The Rebate Wars and Tiered Pricing

To work around the access fee cap, exchanges have developed elaborate rebate tiers. A market-maker that provides 1 million shares of liquidity per day might earn a 15-mil rebate; one providing 10 million shares might earn 20 mils. These "volume tiers" technically comply with the 30-mil access fee cap (the rebate, paid by the exchange to the liquidity provider, is not constrained to 30 mils), but they create a de facto rebate structure that can exceed the cap from the perspective of a high-volume market participant.

The SEC has scrutinized these practices, viewing some tiered rebates as potentially problematic, but has not banned them outright. The line between a legal rebate tier and an illegal kickback is contested and continues to evolve.

## Rebates and Maker-Taker Economics

The maker-taker model (access fee for takers, rebate for makers) emerged as *the* dominant exchange pricing model post-Rule 610. It fundamentally changed who pays and who is compensated in equity trading.

Before the cap, exchanges charged flat fees and did not distinguish between liquidity makers and takers. After the cap, they inverted: liquidity providers (makers) receive compensation (rebates) from the exchange, while liquidity consumers (takers) pay the access fee. This shift affected broker behavior—brokers now want their client limit orders to rest on the exchange earning rebates—and shaped the rise of high-frequency trading firms that specialize in capturing rebates through rapid order-placement strategies.

## Exceptions and Limitations

Rule 610(c) applies uniformly to all securities listed on national securities exchanges. There are no carve-outs for certain stock types, order sizes, or market conditions. Even in a market crash or high-volatility period, the 30-mil cap remains in force.

The rule does distinguish between "regular" exchange access fees and fees for certain specialized services (such as co-location or proprietary data feeds), which are not subject to the 30-mil cap. An exchange can charge higher fees for its premium data feed or for placing servers near the exchange's matching engine. This creates a subsidiary revenue stream that partially offsets the access fee constraint.

## Proposal to Adjust the Cap

The SEC has proposed increases to the 30-mil cap multiple times (e.g., to 35 mils or 40 mils), arguing that costs to operate exchanges have risen and the cap, fixed in nominal terms for 15+ years, no longer reflects reality. Exchanges argue that a higher cap would fund better technology and innovation. But brokers and consumer advocates oppose increases, contending that higher access fees would widen spreads and raise trading costs for end investors.

These proposals have repeatedly stalled in the political process. The cap remains at 30 mils as of 2024, even as exchange costs have inflated.

## Order Routing and the Connection to Reg NMS Best Execution

Rule 610(c) is part of the broader Reg NMS framework, which also requires brokers to find the best price for customers ([Rule 606](/regulation-nms/), best execution rule). In practice, a broker's order-routing algorithm must balance the access fee charged by different exchanges against the prices they offer. An exchange offering a slightly worse price but with a lower access fee might still be the best execution once fees are factored in.

This creates complex routing decisions. A broker executing a customer buy order must choose between Venue A (best displayed price, highest access fee) and Venue B (slightly worse price, lower access fee). The broker must consider the combined impact to demonstrate best execution.

## See also

<div class="wiki-seealso">

### Closely related

- [Regulation NMS](/regulation-nms/) — the SEC's broader framework for fair and efficient trading
- [Stock Exchange](/stock-exchange/) — the venues subject to Rule 610 access fees
- [Market Maker (Trading)](/market-maker-trading/) — liquidity providers who benefit from rebates
- [Bid-Ask Spread](/bid-ask-spread/) — affected by exchange fee and rebate structures
- [Alternative Trading System](/alternative-trading-system/) — non-exchange venues not subject to the access fee cap

### Wider context

- [Broker](/broker/) — entity responsible for routing orders and deciding between venues
- [Market Microstructure](/market-microstructure/) — the structural factors that shape how trades occur
- [Execution Risk](/execution-risk/) — tied to order routing choices and venue fees

</div>
