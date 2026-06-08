---
title: "Odd Lot Order"
description: "An order for fewer shares than the standard round lot, historically subject to different execution rules and pricing."
keywords:
  - odd lot
  - round lot
  - order size
  - trading mechanics
  - execution pricing
image: "/svg/trading.svg"
---

*An **odd lot order** is an instruction to buy or sell a quantity of securities that falls short of the market's standard trading unit, known as a round lot. Historically, a round lot in US equities is 100 shares; any order for 1 to 99 shares is an odd lot. Odd lot orders have long been treated differently by exchanges and brokers—subject to separate routing rules, wider spreads, and execution delays—making them costlier and slower to fill than round-lot trades.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Odd Lot Order — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading mechanics." />

<div class="wiki-infobox-caption">Size discount reversed: small orders pay a liquidity penalty.</div>

|   |   |
|---|---|
| **What it is** | An order for fewer than the standard round lot (typically 1–99 shares in equities) |
| **Also called** | Fractional order, small order |
| **Round lot** | Standard trading unit (100 shares in US equities) |
| **Typical spreads** | Wider [bid-ask spreads](/bid-ask-spread/) than round-lot orders |
| **Execution venue** | Historically routed to separate odd-lot markets; now often consolidated with standard markets |
| **Cost impact** | Higher per-share commission or wider spread, creating a "small order penalty" |

</aside>

## Historical context: the odd-lot infrastructure

For much of the 20th century, exchanges operated separate odd-lot markets, often run by dealers who specialized in matching small orders. On the New York Stock Exchange, odd-lot orders were handled by *odd-lot dealers*—intermediaries who would buy and sell fractional lots from public investors and then offset their positions in round lots on the main market. This arrangement meant that odd-lot prices were set with a markup or discount to the latest round-lot trade—a transparent but costly friction for small investors.

The rationale was straightforward: consolidating 1-share, 15-share, and 43-share orders into standard 100-share bundles required intermediation. Dealers undertook this work, accepting the inventory risk and the operational cost, and passed the expense to retail traders through wider spreads or explicit commissions.

## The modern odd-lot landscape

Today, market structure has changed significantly. Decimalization in 2001, the rise of electronic markets, and the proliferation of [alternative trading systems](/alternative-trading-system/) have blurred the distinction between round and odd lots. Many brokers now route all orders—round or odd—to the same electronic venues, and modern market data systems handle fractional shares just as efficiently as they handle 100-share blocks.

However, the terminology persists, and odd lots retain certain operational characteristics. Many professional [market makers](/market-maker-trading/) still quote spreads that are asymmetric between round and odd lots. A dealer might quote a 1-cent spread for a round-lot order but a 5-cent or 10-cent spread for an odd lot, reflecting the operational cost of managing small positions and the lower priority they receive in routing and execution.

Additionally, some venues impose minimum order sizes or surcharges on orders below a certain quantity, effectively imposing an odd-lot penalty at the execution layer.

## Pricing and execution mechanics

When an odd-lot order hits the market, it typically faces one of three fates. First, it may be matched against another odd-lot order at one of the consolidated venues. Second, it may sit in the order book until a [market maker](/market-maker-trading/) or broker's algorithmic system can bundle it with other small orders to execute as a round lot, then split the fill back to the client. Third, it may be routed to a specialized odd-lot dealer or to an internalization desk at a broker, where it is executed against the firm's inventory or crossed with another client.

In all cases, the economics are less favourable than a round lot. A retail investor buying 25 shares of a stock may see a [bid-ask spread](/bid-ask-spread/) of 0.05 dollars per share, while a 100-share order might see only 0.02 dollars. The difference, multiplied by the share count, means the odd-lot buyer pays a meaningful liquidity premium.

## Why odd lots persist and when they matter

Odd lots are most relevant to **retail investors** making small trades, whether from behavioural reasons (buying "a few shares" rather than a round lot) or necessity (limited capital). For someone purchasing a single share or a handful of shares, the odd-lot penalty is a real drag on returns, especially when buying and selling repeatedly.

Institutionally, odd lots are rarely a primary concern. A [hedge fund](/hedge-fund/) or [mutual fund](/mutual-fund/) with millions to deploy thinks in round lots or larger blocks. Odd lots become relevant only at the margin—when a fund is liquidating a small remaining position or rebalancing into a fractional number of shares.

Fractional shares, enabled by brokers offering "share slices" for ETFs and stocks, have blurred the line further. A broker might allow an investor to buy exactly $500 worth of a stock, which rarely corresponds to a whole number of shares. These fractional orders are now processed through the broker's internal systems, often without the execution friction historically associated with odd lots.

## Regulatory and market structure implications

The SEC has long monitored odd-lot execution as a consumer protection issue. In the pre-decimalization era, odd-lot dealers were required to report their trades, and oversight bodies ensured they were not exploiting retail investors through egregiously wide spreads.

The consolidation of odd and round-lot markets through Regulation SHO and subsequent market microstructure reforms (most notably the Order Protection Rule) has improved execution quality for small orders. However, the fundamentals remain: a 25-share order still imposes higher per-share operational cost than a 100-share order, and that cost is reflected in the execution price.

Some brokers have addressed this by offering "zero-commission" trading on stocks and ETFs, effectively absorbing the odd-lot friction internally. This has made small-position trading more accessible to retail investors, though it raises questions about how brokers offset the cost—typically through [payment for order flow](/payment-for-order-flow/) or internalization spreads.

## Odd lots in algorithmic and index-tracking contexts

[Algorithmic trading](/algorithmic-trading/) systems sometimes generate odd-lot orders at the end of rebalancing cycles, when bringing a portfolio back to target weights results in a final fractional position. Modern algorithmic systems handle these automatically, either by holding the remainder as cash or by rounding to the nearest whole share and adjusting cash accordingly.

Index funds and [passive ETFs](/index-fund/) also contend with odd lots when managing inflows and outflows. A new investor adding $1,000 to a diversified index fund might end up with odd-lot positions in dozens of component securities. Fund managers typically consolidate these via internal crossing or external execution, abstracting away the odd-lot cost from the investor's experience.

## The future of odd-lot distinctions

As fractional share trading becomes standard and market infrastructure becomes more efficient, the distinction between odd and round lots is likely to fade. Already, most retail brokers allow orders for any quantity, and electronic systems route them seamlessly. The remaining distinction is largely a matter of market-maker convention and the risk that some venues may maintain different priority rules or spreads for sub-100-share orders.

For a trader or investor, the practical lesson is this: small orders do carry a cost, but that cost is increasingly reflected in the broker's internal pricing rather than in explicit odd-lot dealer fees. Shopping for brokers with tight spreads and transparent pricing is the best defence against odd-lot friction.

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the price difference between buy and sell quotes, typically wider for odd lots
- [Market Order](/market-order/) — immediate execution; odd lots may execute with slippage
- [Limit Order](/limit-order/) — price-constrained order; odd lots may not execute if spread is wide
- [Market Maker Trading](/market-maker-trading/) — how dealers provide liquidity and set prices for small orders
- [Alternative Trading System](/alternative-trading-system/) — venues that may consolidate odd and round-lot orders

### Wider context

- [Price Discovery](/price-discovery/) — how small orders contribute to and are affected by market pricing
- [Broker](/broker/) — intermediaries managing execution of odd-lot orders
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — regulator overseeing market fairness for retail investors
- [Over-the-Counter Market](/over-the-counter-market/) — markets where odd-lot distinction is less relevant

</div>
