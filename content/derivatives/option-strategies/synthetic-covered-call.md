---
title: "Synthetic Covered Call"
description: "An options strategy that replicates a covered call payoff using long deep-in-the-money call and short out-of-the-money call, without holding the underlying stock."
keywords:
  - covered call
  - synthetic position
  - option strategy
  - call options
  - replication
image: "/svg/derivatives.svg"
---

*A **synthetic covered call** is an options strategy that mimics the payoff of a traditional [covered call](/covered-call/) entirely through options, using a long [deep-in-the-money](/in-the-money/) call and a short [out-of-the-money](/out-of-the-money/) call, eliminating the need to own shares. It appeals to traders who want the premium income and upside cap of a covered call without the capital and opportunity cost of holding stock.*

## The covered call dilemma

A standard covered call requires you to own the underlying stock. You sell an [out-of-the-money](/out-of-the-money/) [call option](/call-option/), pocket the [premium](/option-premium/), and keep the dividends and modest upside. In exchange, you cap your gains at the [strike price](/strike-price/) and tie up capital in the shares themselves.

For some investors, the capital commitment is too heavy. A trader might lack the funds to buy 100 shares—or a round lot—of a stock they mildly like, or they may prefer deploying that capital elsewhere. The synthetic covered call replaces the stock leg with a [deep-in-the-money](/in-the-money/) call, achieving nearly identical payoff and greeks without the share purchase.

## Structure and mechanics

The synthetic covered call consists of:

- Buy one deep-in-the-money call at strike K₁ (e.g., $10 below current price)
- Sell one out-of-the-money call at strike K₂ (e.g., $5 above current price)

Both contracts typically have the same [expiration date](/expiration-date/), chosen to match your view of when you want capital returned. The deeper the long call is in the money, the closer its [delta](/delta/) approaches 1.0, and the more closely it mirrors owning the stock directly.

The net cash outlay is the difference between what you pay for the long call and what you collect from the short call. Because the long call is deep in the money, it's expensive; but the [option premium](/option-premium/) from the short call reduces that cost. Depending on strike separation and current [implied volatility](/implied-volatility/), you might pay a net debit, breakeven, or even receive a credit.

## Why it mirrors a covered call

A covered call against 100 shares delivers a payoff that rises with the stock until the short call's [strike price](/strike-price/), then flattens. Buy at $80, sell a call at $90, and your profit rises dollar-for-dollar as the stock climbs from $80 to $90, then stays flat above $90.

The synthetic version does the same. The long deep-in-the-money call gains a dollar for every dollar the stock rises (delta ≈ 1). The short out-of-the-money call loses a dollar for every dollar above its strike. Below the short strike, the synthetic and the covered call track identically. Above it, both cap out.

The subtle difference: the deep-in-the-money call has [gamma](/gamma/) and [theta](/theta/) properties that differ slightly from outright stock ownership. But when chosen deep enough in the money, these differences are negligible for most holding periods.

## Advantages

**Capital efficiency**: You control the same notional exposure with a fraction of the cash. A $10,000 stock position might require only $3,000–$5,000 in options premiums and collateral.

**Flexibility**: You can close the position by selling (or closing) either leg independently. Want to capture more upside? Buy back the short call. Want to reduce exposure? Sell the long call. You're not married to holding shares.

**No dividends**: You don't receive dividends on a deep-in-the-money call the way you would on shares, but you also avoid the tax complications and volatility of [dividend capture](/dividend/).

**Sector or company switching**: If you rotate out of one stock into another, you simply close both legs and redeploy, rather than transacting shares which might incur larger commissions or slippage.

## Disadvantages

**Cost**: Buying a deep-in-the-money call is expensive. The long premium often exceeds the short premium, requiring a net debit upfront. Over time, your [cost basis](/cost-basis/) erodes only by the [theta](/theta/) of the short call, which is slower than directly owning shares and collecting dividends.

**Complexity**: Options have expirations, [bid-ask spreads](/bid-ask-spread/), and liquidity constraints that shares don't. Rolling or adjusting a synthetic covered call requires more operational overhead.

**Greeks drift**: The [delta](/delta/) of a deep-in-the-money call isn't exactly 1.0, and it erodes over time. The [gamma](/gamma/) is positive, meaning large moves against you become more painful.

**Financing costs**: Implicitly, you're borrowing capital to fund the long call. The [cost of debt](/cost-of-debt/) compounds over longer holding periods, reducing returns.

## When to use it

A synthetic covered call works best if:

- You lack capital to buy shares outright or prefer not to deploy that much cash.
- You expect modest upside, want to collect premium, and are comfortable capping gains.
- You plan to hold for weeks to a few months, not years (shorter timeframes minimise the financing drag).
- The underlying has rich [implied volatility](/implied-volatility/), making short-call premiums fat.
- You want the optionality to close one leg without closing the other—e.g., to rotate into a different strike or underlying.

It's less suitable for long-term dividend-paying stocks where share ownership and regular tax-advantaged dividend receipts make more sense, or for underlying assets with illiquid or wide-spread options markets.

## Managing the position

Roll early. As [time decay](/time-decay-theta/) works in your favour on the short call, close it and sell a new one at a different strike or expiration. This harvests decay in steps and lets you adjust your strike-sell discipline.

If the underlying rallies and breaches your short strike significantly, decide whether to buy it back (accepting a loss) or let assignment occur (selling your synthetic long position). Most traders buy back early rather than face assignment mechanics, which can be finicky with options.

If the underlying collapses, your loss is pinned by the long call's strike (minus premium paid). You can close both legs and redeploy, or hold, knowing your maximum loss is defined.

## Greeks and sensitivity

**Delta**: Approximately +0.95 to +1.0 if the long call is deep in the money, making it behave almost like owning stock.

**Gamma**: Positive but muted (less than owning shares). Large moves against you will require a larger absolute loss.

**Theta**: Slightly positive (the short call decays faster than the long call). You benefit from time passage as long as price stays quiet.

**Vega**: Near zero to slightly negative. If [volatility](/historical-volatility/) spikes, the long call gains more than the short, so you see a modest positive vega effect.

## See also

<div class="wiki-seealso">

### Closely related

- [Covered Call](/covered-call/) — the traditional version using stock
- [Call Option](/call-option/) — the building block
- [In-the-Money](/in-the-money/) — the long leg's status
- [Out-of-the-Money](/out-of-the-money/) — the short leg's starting zone
- [Delta](/delta/) — governs how the synthetic mirrors stock ownership
- [Theta](/theta/) — the time decay you harvest
- [Synthetic Position](/synthetic-position/) — the general principle

### Wider context

- [Option Premium](/option-premium/) — what you buy and sell
- [Strike Price](/strike-price/) — the anchors of your position
- [Implied Volatility](/implied-volatility/) — drives the premiums you collect
- Derivatives — the broader asset class

</div>
