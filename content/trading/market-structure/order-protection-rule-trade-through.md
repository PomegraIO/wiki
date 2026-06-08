---
title: "What Is the Trade-Through Rule for Individual Investors"
description: "How the trade-through rule protects individual investors' limit orders from being executed at worse prices, and what brokers must do to comply with Reg NMS."
keywords:
  - trade through rule individual investors
  - trade-through rule protection
  - order protection rule
  - best execution
  - regulation nms
image: "/svg/trading.svg"
---

*Your limit order to buy 100 shares at $50.00 is valuable. If Apple is trading at $50.02 on the NASDAQ and $50.05 on a regional exchange, you don't want your broker routing your order to the exchange quoting $50.05 just because it pays the broker a rebate. The **trade-through rule**, part of Regulation NMS, prohibits brokers from executing your order at a worse price than the [National Best Bid and Offer](/bid-ask-spread/) (NBBO). For an individual investor, this means your broker must not "trade through"—execute you at an inferior price—when a better price is publicly available.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Trade-Through Rule — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading market structure." />

<div class="wiki-infobox-caption">A broker that executes you at a worse price than the NBBO violates Reg NMS, unless a specific exception applies.</div>

|   |   |
|---|---|
| **Rule name** | Order Protection Rule (Part of Reg NMS) |
| **Enforcer** | SEC and FINRA |
| **Core requirement** | Broker must execute at NBBO or better |
| **Applies to** | Equity trades in US-listed stocks |
| **Exception** | ATS interaction rules (rare; for ATSs only) |
| **Penalty for violation** | Fine + censure; customer restitution possible |

</aside>

## The Problem: Trade-Throughs Before Reg NMS

Before 2007 (when Regulation NMS took effect), a broker could legally send your order to a venue that paid the broker the best rebate, even if another venue had a better price. This was the norm.

Here's a concrete 1990s example:

- The NASDAQ is quoting Apple at 100.05 bid / 100.10 ask (spread of 5 cents).
- A regional exchange is quoting 100.06 bid / 100.11 ask (wider spread, but the exchange pays brokers a "liquidity rebate" of 2 cents per share).
- You submit a limit order to buy 100 shares at 100.08.
- Your broker routes you to the regional exchange, even though the NASDAQ would have filled you at 100.10.
- You end up at 100.11, paying 1 cent per share more than you should have.

The broker captured the rebate; you captured the cost. This was legal.

The trade-through rule was the SEC's response. It said: the first obligation is to the customer, not to the broker's profit.

## How the Trade-Through Rule Works

Under Regulation NMS, here's what a [broker](/broker/) must do:

1. **Check the NBBO.** Before routing your order, the broker checks the best bid and ask across all US equity venues. If you're selling, the NBBO ask is the highest bid available; if you're buying, the NBBO ask is the lowest ask available.

2. **Don't execute worse.** The broker cannot send your order to a venue where you would execute at a worse price than the NBBO, unless a specific exception applies.

3. **Route to best price.** If you place a market order (or a limit order that crosses the NBBO), the broker must route you to the venue offering the best price.

4. **If the venue can't fill you, keep trying.** If your order is routed to the best-priced venue and only partially filled, the broker may route the balance to the next-best venue (respecting price priority).

In the Apple example above, a broker today must route your buy order to the NASDAQ at 100.10, not the regional exchange at 100.11, unless the regional exchange's rules create an exception (very rare).

## Why This Protects Retail Investors

For individual investors, the trade-through rule is powerful protection:

- **Aligns broker incentive with your interest.** The broker can no longer profit by routing you to a worse venue.
- **Prevents bid/ask compression.** Without the rule, brokers would have an incentive to pay rebates to execute at wider spreads. The rule prevents this.
- **Transparency.** The rule makes it clear what price you should expect. If your order is executed worse than the NBBO, you know something is wrong.

Before Reg NMS, average spreads for large-cap stocks were 1–2 cents. After Reg NMS and the rise of [fragmented equity markets](/fragmented-equity-markets-explained/), spreads compressed to a fraction of a cent. The trade-through rule was a core driver of this compression.

## The NBBO and Latency

The trade-through rule depends on the accuracy and speed of the [National Best Bid and Offer](/bid-ask-spread/). The NBBO is calculated by the Securities Information Processors (SIPs) every few milliseconds, aggregating quotes from all US equity venues.

But latency is real. When your order reaches your broker, the NBBO at that microsecond may differ from the NBBO two microseconds ago. By the time the broker routes your order and the venue receives it, the NBBO has moved again.

For this reason, the SEC allows a small "grace period" called the **order protection level (OPL)**—typically 1–2 cents—within which a broker can execute you even if another venue has a better-posted quote by a tiny amount. This prevents technical glitches and latency from triggering constant violations.

In practice, the OPL is narrow enough that it doesn't materially harm retail investors, but it does give brokers some breathing room for legitimate latency.

## Exceptions: ATS Interaction Rules

The trade-through rule has one notable exception, designed for [alternative trading systems](/alternative-trading-system/):

If you submit an order to an ATS (a dark pool, a small exchange, or a broker's internal crossing system), and that ATS has its own "interaction rules" published in its rulebook, then the ATS may not be required to immediately trade through the NBBO. Instead, the ATS may hold your order, try to match it internally, and only send it out to the broader market if internal matching fails.

This exception is meant to allow ATSs to offer price improvement or unique services without instantly being gutted by trade-through rules. In practice, the exception is narrow and heavily scrutinized by the SEC.

## What Actually Happens in Your Broker's System

As a retail investor, you won't see the trade-through rule mechanics, but here's what happens behind the scenes:

1. You submit a buy limit order for 100 shares of Apple at $150.00 via your broker's app.

2. Your broker's order routing engine checks the current NBBO: $150.02 bid / $150.03 ask (for example).

3. Your limit order at $150.00 does not cross the NBBO ask, so it rests in the order book. Your broker (or the brokers of other investors) submit it to one or more venues.

4. If Apple's price later drops and someone posts an ask at $150.00 or better, your order is filled at $150.00.

5. Alternatively, if Apple moves higher and eventually bids reach $150.00, your order is filled.

Throughout this process, your broker is not executing you *worse* than available prices. The venues are linked via the NBBO, and any execution you receive respects the trade-through rule.

## Enforcement and Real-World Violations

The SEC and FINRA actively monitor for trade-through violations. Over the years, major brokers (including some of the largest) have been fined for Reg NMS violations.

Examples:

- **Fidelity** paid a $27 million fine (2015) for failing to execute customer limit orders at prices that complied with the trade-through rule.
- **Citigroup** paid $15 million (2016) for similar failures.
- **Interactive Brokers** paid restitution (2012) for non-compliant order routing.

Violations are usually discovered through pattern detection: the SEC reviews order execution records and identifies cases where customers were executed worse than the NBBO by amounts greater than the grace period. The company is then required to identify all affected customers and provide restitution.

## What About Dark Pools?

Your order in a dark pool or ATS is not directly subject to the trade-through rule in the same way, because dark pools do not report bids/asks to the NBBO. However, once your order executes in a dark pool, that execution price is added to the overall NBBO calculation a few milliseconds later.

More importantly, the SEC requires dark pools and ATSs to have "trade at" rules—they must offer prices that are at least as good as publicly available NBBO quotes, or route your order to the public market if they can't match it at the NBBO.

In effect, the rule is extended: you can't be executed worse than the NBBO anywhere, public or dark.

## Best Execution Beyond Trade-Through

The trade-through rule is the minimum standard. A broker's obligation to provide "[best execution](/best-execution/)" is broader and includes factors beyond price:

- **Execution speed.** Is your order filled immediately or does it languish?
- **Likely execution.** Will your order realistically fill, or is it routed to a venue where it will never match?
- **Market conditions.** In volatile markets, should the broker prioritize price certainty over marginally better pricing?

A broker must consider all these factors in total when deciding where to route your order. Trading through the NBBO is a violation; but receiving a slower, less likely execution at the NBBO price than an alternative venue might offer could also violate best execution standards.

## See also

<div class="wiki-seealso">

### Closely related

- [National Best Bid and Offer](/bid-ask-spread/) — the standard the trade-through rule enforces
- [Broker](/broker/) — the intermediary responsible for complying with the rule
- [Fragmented Equity Markets Explained](/fragmented-equity-markets-explained/) — why fragmentation made the rule necessary
- [Alternative Trading Systems](/alternative-trading-system/) — venues with interaction rule exceptions
- [Best Execution](/bid-ask-spread/) — broker obligation broader than trade-through
- [Central Counterparty Clearing Explained](/central-counterparty-clearing-explained/) — clearing after execution

### Wider context

- [Regulation NMS](/securities-and-exchange-commission/) — the SEC rule that created trade-through protection
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — enforces the rule
- [FINRA](/finra/) — co-enforcer of trade-through compliance
- [Market Maker Trading](/market-maker-trading/) — provides the liquidity the rule protects

</div>
