---
title: "Option Lot Size"
description: "The standard contract multiplier in equity options—one contract controls 100 shares—and how it translates quoted premiums into real dollar exposure."
keywords:
  - option lot size
  - option contract multiplier
  - option premium calculation
  - option notional value
image: "/svg/derivatives.svg"
---

*An option [contract](/option/) controls 100 shares of the underlying [stock](/stock/). When you see a call quoted at 2.50, you're not paying $2.50 total—you're paying $2.50 × 100 = $250 per contract. This [lot size](/option-lot-size/) (or multiplier) is standardized across all US equity options, baked into exchange rules. It means a "small" position in options is often substantial in leverage: buying ten contracts on a $50 stock ties up $50,000 notional value (10 × 100 × $50) with a fraction of that in cash outlay.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Lot Size — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives markets." />

<div class="wiki-infobox-caption">The standard multiplier that scales option premiums into real exposure.</div>

|   |   |
|---|---|
| **Standard multiplier** | 100 shares per contract (US equity options) |
| **Premium to cash** | Quoted price × 100 = dollar cost per contract |
| **Example** | Call at 3.00 bid / 3.10 ask = $300–$310 per contract |
| **Notional exposure** | Number of contracts × 100 × share price |
| **Also called** | Contract multiplier, option multiplier, standard size |
| **Applies to** | All [call](/call-option/) and [put](/put-option/) contracts on US-listed stocks and [ETFs](/etf/) |
| **Unusual sizes** | Some index options ([SPX](/sp-500-index/)) use multiplier of 250; micro contracts use 10 |

</aside>

## The 100-share standard

The [lot size](/option-lot-size/) rule is simple: one equity option contract always controls exactly 100 shares. Buy a call, and you have the right to buy 100 shares. Sell a put, and you're obligated to buy 100 shares if [exercised](/exercise-price/). This isn't a choice—it's the [exchange](/stock-exchange/) standard, set by the Options Clearing Corporation (OCC) and enforced by brokers.

That means when a quote says a Tesla $250 call is trading at 5.00 bid / 5.10 ask, the buyer pays $510 (5.10 × 100) per contract, not $5.10. Sell ten contracts and collect $5,100 in premium (assuming you get the ask). A tiny-looking 0.10 spread between 5.00 bid and 5.10 ask is actually a $10 difference per contract, or $100 on ten contracts—a 2% slippage on each round-trip trade.

This multiplier is why even "cheap" options—those trading in cents—represent real capital deployment. A penny option (0.01 bid / 0.02 ask) on a $5 stock is still $1 to $2 per contract. Buying 100 contracts (the minimum order size at many brokers) ties up $100–$200.

## How the multiplier affects leverage

The [lot size](/option-lot-size/) creates leverage naturally. To own 100 shares of a $100 stock outright, you'd pay $10,000. To control the same 100 shares via one call, you might pay $300–$500 in premium (depending on [strike](/strike-price/), time, and [volatility](/historical-volatility/)). That's leverage of 20–33x on capital at risk.

A trader must be disciplined about position sizing when leverage is this large. Buying 100 option contracts (10,000 shares notional) when you've sized your portfolio for 1,000 shares is a common fatal error. The [lot size](/option-lot-size/) makes the notional huge before a trader realizes it; a single cent move in the underlying can swing the contract's value by 100 cents, wiping gains or cutting losses catastrophically.

Professional traders hedge this mentally by always converting quoted prices back to dollar exposure. They ask: "What's my real dollar at-risk per contract?" A 0.50 quoted premium × 100 = $50. A 1.00 stop-loss = $100 per contract. Ten contracts = $1,000 at-risk. If portfolio risk is $5,000 per trade, only five contracts fit. This habit prevents leverage spirals.

## Why 100 and not another number?

The 100-share multiplier is historical accident, not optimization. When equity options launched on US exchanges in the 1970s, a standard trading unit (a "round lot") was 100 shares. Options inherited that convention. Had it been a different era with different conventions, the multiplier might be 50 or 200 or 1,000. But 100 stuck, and every option [exchange](/stock-exchange/), broker, and trader now operates within that frame.

There are exceptions. Index options—like those on the [S&P 500](/sp-500-index/) (SPX) or VIX—use a multiplier of 250 or 100 depending on the product. [Micro options](/option/) (a newer product) use a 10-share multiplier, designed to lower the absolute dollar cost per contract for retail traders. But the standard workhorse—options on individual [stocks](/stock/) and broad [ETFs](/etf/)—is 100.

## Adjusted options after splits and special events

The 100-share multiplier usually holds firm. But after a [stock split](/stock-split/), the contract may adjust. If a company issues a 2-for-1 split, an existing call contract for 100 shares becomes a call for 200 shares (to maintain the same dollar value pre- and post-split). This is called an "adjusted option."

Adjusted options are rare and often illiquid—most traders close them and shift to the new standard contract. But they illustrate the point: the [lot size](/option-lot-size/) can flex in exceptional circumstances. Dividend special handling, mergers, and corporate reorganizations sometimes trigger adjustments too. The OCC publishes rules governing these edge cases; brokers and traders must track them to avoid confusion.

## Impact on [bid-ask spreads](/bid-ask-spread-options/) and [open interest](/option-open-interest/)

The [lot size](/option-lot-size/) has a subtle but real impact on market structure. Because each contract is worth 100 shares, a strike with 10,000 open contracts represents 1,000,000 shares of notional exposure—enough to matter to a [market maker](/market-maker-trading/). The [market maker](/market-maker-trading/) can afford to warehouse small positions and tighten [bid-ask spreads](/bid-ask-spread-options/).

By contrast, a micro option (10-share multiplier) with the same 10,000 open interest represents only 100,000 shares notional. [Market makers](/market-maker-trading/) may demand wider spreads to compensate for the smaller effective volume. This is why micro options, despite their appeal to retail traders, sometimes have worse [liquidity](/liquidity-risk/) characteristics than standard contracts.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — The foundational derivative contract
- [Strike Price](/strike-price/) — How the multiplier applies across strikes
- [Option Volume](/option-volume/) — How [lot size](/option-lot-size/) shapes trading volume counts
- [Option Open Interest](/option-open-interest/) — How [lot size](/option-lot-size/) relates to notional exposure
- [Bid-Ask Spread in Options](/bid-ask-spread-options/) — How [lot size](/option-lot-size/) affects [market maker](/market-maker-trading/) economics
- [Exercise Price](/exercise-price/) — The right to buy or sell at the multiplier-adjusted quantity

### Wider context

- [Call Option](/call-option/) — The right to buy 100 shares at a set price
- [Put Option](/put-option/) — The right to sell 100 shares at a set price
- [Futures Contract](/futures-contract/) — Derivatives with their own standard multipliers
- [Over-the-Counter Market](/over-the-counter-market/) — Where non-standard [lot sizes](/option-lot-size/) trade

</div>
