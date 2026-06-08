---
title: "Target Redemption Forward (TARF) Explained"
description: "A TARF is a structured currency forward that accumulates gains until a profit target is hit, then terminates—creating asymmetric risk for hedgers who benefit from favorable moves but face capped upside."
keywords:
  - target redemption forward
  - how does a target redemption forward work
  - TARF currency hedge
  - structured forwards
  - forex derivatives
  - currency hedging risks
image: /svg/forex.svg
---

*A target redemption forward (TARF) is a structured currency hedge that converts a series of forward contracts into a single accumulated position, automatically terminating when the cumulative gain reaches a predetermined profit target. The contract offers lower upfront costs and predictable gain ceilings, but at the cost of asymmetric risk: gains are capped while losses can accumulate indefinitely, a combination that caught many Asian and European exporters off-guard during volatile currency episodes.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">TARF Structure — Key Mechanics</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Profit target-triggered auto-termination creates winners in calm markets, losers in volatile ones.</div>

|   |   |
|---|---|
| **Underlying** | Currency pair (e.g., USD/JPY, EUR/USD) |
| **Strike price** | Fixed forward rate locked at inception |
| **Target profit** | Cumulative gain threshold (e.g., 500 basis points) |
| **Settlement** | Daily, weekly, or monthly accrual until target hit |
| **Typical tenor** | 1–3 years with multiple measurement dates |
| **Upside** | Capped at target profit; terminates if target reached |
| **Downside** | Uncapped losses if currency moves against hedger |
| **Counterparty** | Bank (seller of TARF) |

</aside>

## How Accumulation Works

Imagine a Japanese exporter selling goods in U.S. dollars and hedging currency risk. Instead of buying a standard [forward contract](/forward-contract/) locking in a single exchange rate, the exporter enters a TARF with a strike price of 105 JPY/USD over 24 monthly observations. On each observation date, the bank calculates the gain or loss on that day's contract: if the spot rate is 106 JPY/USD (stronger dollar, favorable for the exporter), the gain is 1 yen per dollar hedged. These daily or monthly gains accumulate in a "bucket."

The TARF specifies a target—say, a cumulative gain of 500 basis points (5 yen per dollar). Once cumulative gains hit 500 basis points, the contract terminates automatically and the exporter has locked in that target profit. If the yen weakens every month and spot drifts to 108 JPY/USD by month three, the accumulated gain reaches the target faster, and the contract ends. The exporter's maximum profit is known and capped.

The appeal is clear: compared to buying 24 separate forward contracts or an exchange-traded option, a TARF typically costs less upfront (no premium or minimal fees). The exporter knows exactly what the best-case profit will be and when they'll exit. For a treasurer managing currency budgets, knowing the ceiling is valuable.

## The Asymmetric Risk Trap

The catch is the asymmetric payoff. While gains are capped and terminate the contract, losses accumulate without limit. If the yen unexpectedly strengthens (spot moves to 104, 103, 102 JPY/USD), the exporter loses on each measurement date. These losses compound. Unlike a standard forward, the exporter cannot cap downside loss through early termination—the contract keeps running, and the accumulation bucket can swing deeply negative.

During the 2008–2009 financial crisis, the yen surged as risk-averse investors fled to perceived safety. Japanese exporters who had bought TARFs found themselves locked into losses that mounted daily, with no exit mechanism except renegotiation (often at unfavorable terms, and sometimes impossible if the counterparty faced distress). A TARF with a 500 basis point profit target and no loss limit can easily produce a 1,000 or 2,000 basis point loss if the currency moves dramatically. The exporter gets the upside cap for free (essentially) but pays for it in unlimited downside.

## Pricing and Counterparty Economics

Banks sell TARFs because they can hedge their risk and extract value from the asymmetry. The bank buys a forward at 105 JPY/USD and sells a TARF at 105 JPY/USD, receiving a margin. The bank then dynamically hedges its exposure as the contract accrues gains. On favorable days (for the exporter), the bank is short the exporter's gain and buys hedges. On unfavorable days, the bank is long the exporter's loss and sells hedges.

When the exporter's accumulated gain hits the target and the contract terminates, the bank's dynamic hedge is in place and the bank pockets its margin. But if the currency moves dramatically against the exporter—and in unpredictable ways—the bank's hedge can become mismatched, leading to its own losses. During crises, many banks faced large TARF portfolios with counterparties underwater and unable or unwilling to post margin. Some banks ended up in disputes over valuation and settlement.

The bank's incentive is to price the target threshold so that it is hit often enough in normal markets (giving the bank routine margin) but is still achievable for the customer (maintaining the customer's willingness to buy). If the bank sets the target too aggressively, customers will not buy; too low, and the contract terminates too early, limiting the bank's upside. This pricing tension means that TARFs are most commonly sold to exporters (importers prefer importing, minimizing currency loss risk, so they are less interested in hedges with unlimited downside).

## Historical Losses and Market Evolution

TARFs peaked in popularity in the early 2000s, especially among Asian exporters. South Korean and Japanese companies heavily used them to hedge won and yen exposure. In 2008–2009, many of these positions blew up. The yen rallied sharply (strengthening against the dollar) as a risk-off trade, and TARF holders found themselves underwater with no escape hatch. Counterparties faced writedowns or disputes over what "fair value" meant for deeply underwater contracts.

The crisis exposed a fundamental flaw in the instrument: the customer does not control early termination. In a standard option or forward, the buyer can exit any time (though at market-determined price). A TARF hedger is locked in unless they renegotiate with the counterparty or close the position by offsetting it (entering an equal and opposite TARF, effectively doubling their derivatives exposure). Many corporate hedgers lacked the sophistication to understand this risk ex-ante. The term "TARF blow-up" entered the lexicon of cautionary tales in corporate finance.

Regulatory and accounting scrutiny increased post-crisis. Many TARFs require mark-to-market treatment under ASC 815 (derivatives accounting), forcing corporations to record unrealized losses quarterly, which can swing earnings or trigger covenant violations. The reputational damage to banks selling TARFs also mounted, as some faced litigation or regulatory criticism for selling opaque derivatives to unsophisticated corporates.

## Modern Usage and Alternatives

TARFs are much less common now, but still available from large derivatives dealers for specialized hedging. A multinational corporation with high-conviction that a currency will weaken gradually over 2–3 years might use a TARF instead of a series of forwards if it wants to cap upside cost while accepting downside risk. Some companies layer them (buy a TARF but cap maximum loss via an offsetting option), reducing but not eliminating the asymmetry.

More often, corporates now use standard [forwards](/forward-contract/), [options](/option/) (putting a floor on losses), or currency swaps for medium-term hedging. Options cost premium but offer defined downside. Forwards lock in a rate but offer no upside. Swaps allow floating rate funding in one currency against fixed in another, providing operational flexibility. For exporting companies seeking protection against weakening of their home currency, standard put options (buying the right to sell the foreign currency at a floor price) are more transparent and symmetric.

The decline of TARFs reflects both post-crisis distrust of opaque derivatives and improved corporate awareness of asymmetric risk. However, the instrument persists in markets with less sophisticated regulation or where banks face pressure to generate higher margins; emerging-market corporates, some of which have less exposure to crisis memories, occasionally enter TARF positions with less due diligence than their developed-market peers.

## Valuation and Unwinding

Valuing a TARF requires Monte Carlo simulation or lattice models that project currency paths and calculate the probability of hitting the target within the contract life. The value to the bank (TARF seller) is sensitive to [volatility](/volatility-smile/) assumptions. High volatility increases the probability of hitting the target quickly (shortening the bank's average revenue life) and increases the probability of very deep losses if currency moves dramatically (increasing the bank's downside risk). Low volatility increases the time to target and can increase the bank's overall profit on the contract.

Unwinding a deeply underwater TARF is difficult. The corporate cannot simply cancel; cancellation requires compensating the bank for the fair value of the embedded derivatives (which is negative to the corporate). Renegotiating the target or strike can work but typically involves the corporate paying the bank or agreeing to worse terms. Some TARFs from the 2000s took years to unwind, with ongoing disputes over valuation and settlement mechanics.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward Contract](/forward-contract/) — standard currency hedge that locks in an exchange rate
- [Option](/option/) — grants the right but not obligation to buy or sell at a strike; offers defined downside
- [Currency Risk](/currency-risk/) — the core exposure TARFs attempt to hedge
- [Derivatives Hedging](/derivatives-hedging/) — principles and instruments for managing financial risk
- [Swap](/swap/) — currency swap or interest rate swap, alternative medium-term hedging vehicle

### Wider context

- [Volatility Smile](/volatility-smile/) — how options pricing reflects market perception of extreme moves
- Mark-to-Market Accounting — how unrealized derivative losses are recognized quarterly
- [Counterparty Risk](/counterparty-risk/) — the risk that the bank cannot settle or faces distress
- Foreign Exchange — the market and mechanics of currency trading
- Corporate Treasury — function that manages hedging and financial risk

</div>
