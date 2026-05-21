---
title: "Lookback Option"
description: "An exotic option whose payoff depends on the lowest or highest price the underlying reached during the option's life, not just the final price."
---

*A lookback option is an exotic derivative where the strike or payoff is determined by the extreme price (high or low) reached during the option's lifetime. Instead of comparing the final price to a fixed strike, the payoff is based on the most favorable price seen at any point.*

## How lookback options work

A **lookback call** lets you buy at the lowest price seen during the option's lifetime. Suppose you enter a three-month lookback call on a stock currently at $100. If the stock declines to $90, rallies to $120, then settles at $105, you exercise the call at $90 (the low), capturing the $15 gain.

Contrast this with a standard call at $100. If the stock settles at $105, you gain $5. The lookback call gains $15 by exercising at the lowest point, a significant advantage.

A **lookback put** lets you sell at the highest price seen during the option's life. If the stock ranges from $90 to $120 and settles at $105, the put holder exercises at $120, gaining $15.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Lookback Option — key facts</div>
  <table>
    <tr><th>Type</th><td>Exotic, path-dependent option</td></tr>
    <tr><th>Payoff</th><td>Call: max(highest price − strike, 0); Put: max(strike − lowest price, 0)</td></tr>
    <tr><th>Comparison</th><td>Always beats a standard option with the same strike and expiration</td></tr>
    <tr><th>Cost</th><td>Significantly higher than standard options</td></tr>
    <tr><th>Liquidity</th><td>OTC markets only; illiquid</td></tr>
    <tr><th>Typical use</th><td>Speculation or hedging when capturing best/worst case is critical</td></tr>
  </table>
</aside>

## Why lookback options exist

Lookback options eliminate the "timing" problem in standard options. With a standard call, if the stock rallies to $120 but you don't sell, then it falls to $105, you regret not selling at $120. A lookback call holder doesn't face this regret: they can sell at $120, the best price seen.

This makes lookback options valuable to traders who believe a price will move significantly but are uncertain about timing. They're also useful for hedgers with historical data: if you're worried about a price decline, a lookback put lets you sell at the worst (best for protection) price that actually happened.

## The cost of insurance

Lookback options are dramatically more expensive than standard options. A standard call on a $100 stock with a $100 strike might cost $3. A lookback call (using the current price as the initial reference) might cost $8–$12.

The premium reflects the option's inherent advantage. Lookback calls and puts always payoff at least as much as standard options at the same strike. The extra premium compensates the seller for that advantage. The pricing requires sophisticated models because the payoff depends on the entire price path, not just the terminal price.

## Fixed vs. floating lookbacks

There are two variants:

- **Fixed lookback**: The strike is fixed at entry (e.g., $100 call). The payoff is max(lowest price seen − 100, 0). Common.
- **Floating lookback**: The strike is the price at entry, but you can exercise at the best price seen. The payoff is max(highest − lowest price, 0) for a call or (lowest − highest) × (−1) for a put. These are extremely expensive and rare.

Most OTC lookback options use the fixed variant. Floating lookbacks are mostly theoretical.

## Valuation and pricing challenges

Lookback options are priced using Monte Carlo simulation or closed-form models (if available). The payoff depends on the entire path of prices over the option's life, not just the endpoint. This path-dependency makes them harder to price than plain vanilla options and introduces model risk.

Brokers and dealers often use models like the Garman-Kohlhagen formula (an extension of Black-Scholes) or simulation to price lookbacks. Different models can yield significantly different prices, creating arbitrage opportunities for sophisticated traders.

<div class="wiki-hatnote">For standard options, see <a href="/wiki/call-option/">call options</a> and <a href="/wiki/put-option/">put options</a>. For other exotic options, see <a href="/wiki/barrier-option/">barrier options</a> or <a href="/wiki/asian-option/">Asian options</a>.</div>

## Where lookback options trade

Lookback options are OTC derivatives, typically offered by investment banks and brokers to institutional clients. Retail investors rarely encounter them. They're common in forex markets (currency options) and commodity markets (oil, metals), where price paths matter strategically.

Counterparty risk is significant. You're buying from a specific dealer, and if the dealer defaults, you lose. The lack of exchange standardization and central clearing also means bid-ask spreads are wide (2–5% of the option value is common).

## Comparisons with exotics

**Asian options** use the average price during the option's life instead of the extreme. They're cheaper than lookbacks because averaging smooths volatility.

**Barrier options** have a trigger price that knocks the option in or out. They're simpler than lookbacks and more liquid.

**Lookbacks** give the holder the best-case price seen, making them the most generous exotic option and the most expensive.

## When lookbacks fail

The primary risk is that the path you expect never occurs. If you buy a lookback call expecting the stock to crash then recover, but it never crashes, you're holding an expensive option that performs no better than a standard option.

Lookbacks are also sensitive to model risk and pricing disagreement. Two dealers might quote significantly different prices, and you might pay too much. With illiquid markets, getting out early at a fair price can be difficult.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/asian-option/">Asian option</a> — uses average price instead of extreme.</li>
  <li><a href="/wiki/barrier-option/">Barrier option</a> — activates at a trigger price.</li>
  <li><a href="/wiki/call-option/">Call option</a> — the standard reference for comparison.</li>
  <li><a href="/wiki/put-option/">Put option</a> — the standard downside reference.</li>
  <li><a href="/wiki/exotic-fx-option/">Exotic FX option</a> — where lookbacks often trade.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/option/">Option</a> — foundational contract.</li>
  <li><a href="/wiki/derivatives/">Derivatives</a> — asset class overview.</li>
  <li><a href="/wiki/monte-carlo-options-pricing/">Monte Carlo options pricing</a> — valuation method.</li>
</ul>
</div>
