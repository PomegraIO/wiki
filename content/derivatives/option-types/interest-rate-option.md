---
title: "Interest Rate Option"
description: "An option whose underlying is an interest rate or bond, used to hedge or speculate on changes in borrowing costs and bond prices."
---

*An interest rate option is a derivative that gives the holder the right to lock in a rate or protect against rate changes. Examples include swaptions, bond options, and caps and floors on floating rates.*

## How interest rate options work

An interest rate option's payoff depends on where rates settle at maturity. A **rate cap** gives you the right to exchange a floating rate for a fixed rate if rates exceed a certain level. A **rate floor** gives the right to a minimum fixed rate if rates fall below a level.

For example, a borrower with a floating-rate loan might buy a cap: if LIBOR exceeds 3%, the borrower pays 3% + spread instead of the floating rate. If LIBOR stays below 3%, the borrower pays the floating rate. The cap is insurance against rising rates; it costs upfront premium but protects against the worst case.

A **bond option** is the right to buy or sell a bond at a fixed price. Similar to stock options, but the underlying is a bond rather than a stock. If you buy a bond call and rates decline (bond prices rise), the option gains value.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Interest Rate Option — key facts</div>
  <table>
    <tr><th>Type</th><td>Derivative on rates or bonds</td></tr>
    <tr><th>Common forms</th><td>Caps, floors, collars, swaptions, bond options</td></tr>
    <tr><th>Payoff driver</th><td>Changes in interest rates</td></tr>
    <tr><th>Liquidity</th><td>OTC for most; some trading in options on bond futures</td></tr>
    <tr><th>Notional exposure</th><td>Often large; caps/floors are usually on multi-million loans</td></tr>
    <tr><th>Typical use</th><td>Hedging rate risk, protecting borrowing costs</td></tr>
  </table>
</aside>

## Why corporations and investors use them

A corporation with a floating-rate debt facility faces rising rate risk. If the Federal Reserve raises rates, interest expense increases. A rate cap locks in the maximum rate the corporation pays, providing budget certainty. The cost is the cap premium, typically 0.5–2% of notional.

An investor owning long-term bonds faces price risk if rates rise (bond prices fall). A bond put option protects against this decline. If rates rise 2%, the bond declines in value, but the put gains value and offsets some loss.

Interest rate options are also used speculatively. A trader believing rates will fall might buy bond calls or caps. If rates decline, bond prices surge and the option profits.

## Caps, floors, and collars

A **rate cap** is a series of call options on rates, typically covering three, five, or ten years. Each quarterly or semi-annual reset, if the floating rate exceeds the cap strike, the borrower receives a payment equal to the difference × notional.

A **rate floor** is the mirror: a put on rates. If rates fall below the floor, the lender (or the floor buyer) receives a payment.

A **collar** combines a cap and floor, capping both the upside and downside on rates. The borrower benefits if rates stay within the collar range. A collar's net cost is lower than a cap alone because the floor premium (collected) offsets cap cost.

## Swaptions and options on swaps

A **swaption** is an option to enter into an [interest rate swap](/wiki/interest-rate-swap/). For example, a payer swaption gives you the right to enter a swap paying fixed and receiving floating. If you expect rates to rise but aren't ready to commit yet, a swaption lets you reserve that right and decide later.

Swaptions are complex because their payoff depends on the swap rate at expiration, which reflects both current rates and market expectations. A swaption that's out-of-the-money at inception might become profitable if the yield curve steepens.

<div class="wiki-hatnote">For the underlying, see <a href="/wiki/interest-rate-swap/">interest rate swap</a>. For bond-specific options, see <a href="/wiki/bond/">bonds</a>.</div>

## Valuation models

Interest rate options are priced using specialized models like the **Black model** (for futures), the **Black-Derman-Toy model** (for bonds), or the **Vasicek model** (for short rates). These models assume rate changes follow a stochastic process and use Monte Carlo simulation or tree-building to value options.

The key inputs are:

1. **Current rate or bond price**: The starting point.
2. **Volatility**: How much rates might move.
3. **Mean reversion**: The tendency for rates to revert to a long-term average.
4. **Yield curve shape**: Current term structure of rates.

Different models can produce different prices, introducing model risk. A cap priced under one model might differ from a cap priced under another by 10–20%.

## Greeks of interest rate options

Interest rate options have Greeks, but the interpretation differs:

- **Delta**: Change in option price per basis point (0.01%) change in rates.
- **Vega**: Change per 1% change in rate volatility.
- **Theta**: Time decay (usually small for long-dated options).
- **Rho**: Change per 1% change in the swap curve level (less relevant; often delta captures this).

For bond options, delta measures change per dollar move in the bond price. A bond call with delta = 0.6 gains $0.60 for each dollar the bond rallies.

## Cap and floor conventions

Caps and floors are typically quoted as all-in rates. If the current floating rate is LIBOR + 100 bps and you buy a 3% cap, the all-in rate you're capping is 3.00%. You pay upfront premium.

The notional amount is significant. A cap on a $100 million loan at 100 bps cap width (e.g., rate capped at 3%, currently 2%) might cost $200K–$500K depending on volatility and term. This is typically 0.2–0.5% of notional per year.

## When interest rate options disappoint

If rates move opposite to what you expected, the option expires worthless. A borrower who buys a cap and rates fall doesn't benefit—the cap is never in-the-money. The premium is lost.

They're also sensitive to the yield curve's shape. A cap priced when the curve is flat might be overpriced if the curve inverts (long rates fall below short rates). Model assumptions also matter: if realized volatility is much lower than implied, the option is overpriced at inception.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/interest-rate-swap/">Interest rate swap</a> — the underlying for swaptions.</li>
  <li><a href="/wiki/bond/">Bond</a> — underlying for bond options.</li>
  <li><a href="/wiki/callable-bond/">Callable bond</a> — embeds interest rate options.</li>
  <li><a href="/wiki/federal-funds-rate-target/">Federal funds rate</a> — a key rate for options.</li>
  <li><a href="/wiki/yield-curve/">Yield curve</a> — shapes rate option values.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational concept.</li>
  <li><a href="/wiki/derivatives/">Derivatives</a> — asset class overview.</li>
  <li><a href="/wiki/interest-rate/">Interest rate</a> — the underlying driver.</li>
</ul>
</div>
