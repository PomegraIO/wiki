---
title: "Last Look"
description: "A contested practice in FX trading where a liquidity provider retains the right to accept or reject a trade after seeing a client's order."
keywords:
  - forex trading
  - liquidity provider
  - order rejection
  - market manipulation
  - counterparty risk
  - execution risk
image: /svg/forex.svg
---

*Last look is the right reserved by a liquidity provider (usually a [bank](/forex.svg) or [FX prime broker](/fx-prime-brokerage/)) to accept or reject a client's order after observing the full trade details—including price, size, and currency pair. In practice, it creates an asymmetric window during which the provider can cancel the deal if market conditions have shifted, placing the risk of adverse movement entirely on the client.*

## The mechanics of last look

When a client submits an order for a currency pair at a quoted price, last look allows the counterparty a brief moment (typically 100 milliseconds to 1 second) to review the trade before confirming it. During this window, if the [bid-ask spread](/bid-ask-spread/) has widened, if volatility has spiked, or if the underlying rate has moved materially, the liquidity provider can walk away.

From the provider's perspective, this is risk management: the cost of hedging an immediate trade might have risen, or the client's order might have been placed just as an unfavourable news event moved the market. From the client's perspective, the trade they thought they had locked in vanishes, forcing them to re-quote and often execute at a worse price.

The technical implementation varies. Some systems use explicit buttons or terminal commands that only the provider can activate. Others embed rejection into algorithmic execution logic—the system evaluates the trade against internal risk models and automatically cancels if thresholds are breached. In all cases, the client sees "order rejected" after committing mentally to the trade.

## Why last look exists

Last look emerged in the 1990s and 2000s as a response to technology and competition. Retail and semi-retail traders could place orders electronically, but the provider still needed to hedge those trades in the interbank market or with other liquidity sources. The time to source that hedge was non-zero; last look plugged that gap.

It also served (and still serves) as a crude guard against what providers call "fishing"—placing large orders at tight spreads, then cancelling the parts that don't execute favourably. A client who knows the provider will accept the trade will behave differently than one who suspects rejection.

For smaller market participants without direct [interbank market](/forex.svg) access, the alternative to accepting last look was often no liquidity at all. Prime brokers and electronic communication networks (ECNs) used it as a licensing fee of sorts: to access tight spreads, the client had to accept the provider's right of first refusal.

## The controversy

Last look remains fiercely debated. Critics argue it is a form of order manipulation disguised as risk control. A provider who rejects unfavourable trades while accepting profitable ones is, in effect, taking the client's alpha—capturing the trades that work and shedding the ones that don't.

Empirical studies have found that last look rejection rates correlate with market volatility and, more damningly, with the profitability of the order to the client. Providers with discretionary last look have been shown to reject orders more frequently when the client stands to gain, suggesting the rejection is not purely mechanical.

The practice is also vulnerable to abuse through timing. A provider with intentionally slow systems (or deliberately induced latency) can create a wider window for last look decisions, increasing the chance to cancel unfavourable trades. This is harder for clients to detect than outright refusal.

## Regulatory response

In the mid-2010s, regulatory bodies began scrutinising last look. The UK Financial Conduct Authority (FCA) and the European Securities and Markets Authority (ESMA) took the position that last look must be transparent and, in some cases, banned outright in retail FX contexts.

Under ESMA rules (which apply in the EU), last look on retail clients was prohibited in 2018 for most currency pairs. However, it persists for professional and institutional clients, where it is deemed acceptable if properly disclosed. The FCA similarly distinguishes between different client types: retail clients must not face last look; professional firms may accept it with explicit consent.

In the United States, the [Commodity Futures Trading Commission](/forex.svg) (CFTC) did not ban last look but required platforms offering it to disclose the practice and rejection statistics. This transparency push, applied to some larger venues, has forced providers to be explicit about when and why they invoke the right.

## The evolution toward automation

Many modern FX platforms have moved to algorithmic last look—rules-based rejection that triggers when price moves beyond a set threshold or when [volatility](/fx-liquidity-aggregation/) exceeds tolerance levels. This is technically more defensible than a trader's subjective decision, as it appears more objective.

However, the threshold can be set tightly or loosely at the provider's discretion, recreating the same asymmetry. A provider can set the band so narrow that rejection is almost guaranteed on volatile orders, or so wide that it becomes largely symbolic.

Some platforms have experimented with time-weighted last look, where the window shrinks as the trade ages, or with ranked last look, where the client chooses upfront how much rejection risk to accept in exchange for better pricing.

## Practical impact on execution

For active traders and hedge funds, last look adds a "phantom slippage" cost. On a day when you expect to execute 100 orders, 5 or 10 may be rejected, forcing you to re-quote, often at a worse price. Over time, this compounds.

The rejection rate also depends on client profile. A large hedge fund with a sticky relationship (and significant volume) may face lower rejection rates than a small account that can walk away. This creates a hidden tiered pricing structure: tight spreads come with high rejection risk; wider spreads come with rare rejection.

For [FX prime brokerage](/fx-prime-brokerage/) relationships, last look on the prime broker's internal trades is separate from last look offered to the end client. A prime broker may give a client a prime brokerage tier without last look, while reserving last look for trades it re-prices to itself.

## See also

<div class="wiki-seealso">

### Closely related

- [FX Prime Brokerage](/fx-prime-brokerage/) — How prime brokers extend credit and distribute trades to multiple dealers
- [Give-Up in FX](/give-up-forex/) — The process of transferring an executed trade from dealer to prime broker
- [FX Liquidity Aggregation](/fx-liquidity-aggregation/) — Combining price streams from multiple liquidity sources
- [Bid-Ask Spread](/bid-ask-spread/) — The difference between the quoted buy and sell prices
- [Counterparty Risk](/counterparty-risk/) — The risk that the other party to a trade defaults or fails to settle
- [Over-the-Counter Market](/over-the-counter-market/) — Decentralized trading outside formal exchanges

### Wider context

- [Broker](/broker/) — Intermediary connecting buyers and sellers
- [Currency Risk](/currency-risk/) — Risk of loss due to adverse currency moves
- [Market Maker Trading](/market-maker-trading/) — Liquidity providers who profit from spreads
- [Price Discovery](/price-discovery/) — The process by which markets establish fair prices

</div>
