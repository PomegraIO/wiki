---
title: "Synthetic Stock"
description: "An options strategy that replicates the economic payoff of owning stock using a long call and short put at the same strike and expiration."
---

*A synthetic stock combines a long call and short put at identical strikes and expirations to create a position economically identical to owning the underlying stock. It offers the same P&L but uses leverage and derivatives instead of equity capital.*

## How synthetic stock works

If you own 100 shares of a $100 stock, you have a $10,000 position with full downside loss and unlimited upside gain.

Alternatively, you can create the same P&L by buying one $100 call and selling one $100 put, both with the same expiration. If the stock rallies to $110, the call is worth $10 and the put is worthless, netting a $10 gain. If the stock falls to $90, the put is worth $10 and the call is worthless, netting a $10 loss. The payoff is identical.

The difference: synthetic stock requires less capital upfront (just the net premium paid or received) and uses leverage via the options. You control the full position with a fraction of the capital required to buy stock.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Synthetic Stock — key facts</div>
  <table>
    <tr><th>Type</th><td>Options replication strategy</td></tr>
    <tr><th>Legs</th><td>Long call + short put (same strike and expiration)</td></tr>
    <tr><th>Payoff</th><td>Identical to owning stock at the strike price</td></tr>
    <tr><th>Capital required</th><td>Much less than owning stock; mainly margin for short put</td></tr>
    <tr><th>Leverage</th><td>High; small moves in stock create large percentage gains or losses</td></tr>
    <tr><th>Typical use</th><td>Speculation with less capital; replication for market makers</td></tr>
  </table>
</aside>

## Why use synthetic stock

Synthetic stock appeals to traders with strong directional conviction who want leverage. Instead of buying $10,000 of stock, you control $10,000 of exposure with $2,000–$5,000 in margin. If the stock rallies 10%, your margin gains 20–50%.

It's also used in **arbitrage** and **market making**. If a stock option is mispriced relative to the stock, a market maker can trade synthetic stock against the stock to capture the mispricing. For example, if the call is overpriced and the put is correctly priced, you sell the overpriced call and buy the stock, or you sell the call and buy the put (converting to short synthetic stock).

Synthetic stock also appears in **risk management**. A trader holding a short put can hedge by buying a synthetic stock (or equivalently, buy the stock and sell the call against it). This converts a naked put into a covered position.

## Net debit or credit

The cost of synthetic stock depends on the call and put premiums:

- If the call costs more than the put credit, you pay a net debit. This occurs when the call is out-of-the-money and the put is in-the-money (stock is below the strike).
- If the put credit exceeds the call cost, you collect a net credit. This occurs when the call is in-the-money and the put is out-of-the-money (stock is above the strike).
- If both are at-the-money, the call and put cost roughly the same, and net cost is near zero (plus commissions).

<div class="wiki-hatnote">For owning stock directly, see <a href="/wiki/stock/">stocks</a>. For leveraged positions, see <a href="/wiki/margin/">margin buying</a>.</div>

## Synthetic stock vs. owning stock

The economics are identical, but risks differ:

1. **Capital efficiency**: Synthetic stock requires less capital, creating leverage.
2. **Dividend**: Synthetic stock doesn't entitle you to dividends. If the stock pays a dividend before expiration, the put's owner (short put seller) receives the dividend benefit, not you. This is a cost.
3. **Assignment**: If the put is exercised (before expiration, if it's American), you're forced to "buy" stock at the strike. If the stock has rallied, this is a loss relative to what you expected.
4. **Liquidity**: Synthetic stock requires liquid options. On illiquid stocks, bid-ask spreads might widen synthetics unfavorably.
5. **Margin calls**: Holding synthetic stock via margin means you face margin calls if the stock declines. Owning stock outright has no margin calls.

## Reverse synthetic stock

A **reverse synthetic stock** (short synthetic) uses a short call and long put at the same strike, replicating a short stock position. If you're bearish and want to short 100 shares without borrowing the stock, reverse synthetic does it. The payoff is identical to short stock: you profit $1 per share if the stock falls $1.

Reverse synthetics avoid short-squeeze and borrowing costs but have similar risks: unlimited loss if the stock rallies.

## Dividends and corporate actions

Synthetic stock doesn't capture dividends. If you own actual stock and it pays a $1 dividend, you receive $100 in cash. With synthetic stock, the call and put values adjust to reflect the dividend ex-date, but the adjustment is usually less than the cash dividend (call drops, put rises, but net is a loss to the synthetic owner).

Stock splits and other corporate actions also affect synthetics: the strike and multiplier adjust, but the economics change in subtle ways.

## Used by market makers and arbitrageurs

Market makers create synthetic stock constantly. If they own shares of stock and sell call options against it, they've essentially created a [covered call](/wiki/covered-call/) or short synthetic call. If they are short stock and sell puts, they've created short synthetic stock.

Convertible bond traders use synthetics to hedge. A convertible bond is similar to a straight bond plus a call option on the stock. The trader might buy the bond, then sell a synthetic call to hedge the embedded call, leaving pure credit exposure.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/call-option/">Call option</a> — the long leg of synthetic stock.</li>
  <li><a href="/wiki/put-option/">Put option</a> — the short leg of synthetic stock.</li>
  <li><a href="/wiki/covered-call/">Covered call</a> — stock + short call (related strategy).</li>
  <li><a href="/wiki/protective-put/">Protective put</a> — stock + long put (related strategy).</li>
  <li><a href="/wiki/stock/">Stock</a> — the replication target.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational contract.</li>
  <li><a href="/wiki/derivatives/">Derivatives</a> — asset class overview.</li>
  <li><a href="/wiki/put-call-parity/">Put-call parity</a> — the principle underlying synthetic stock.</li>
</ul>
</div>
