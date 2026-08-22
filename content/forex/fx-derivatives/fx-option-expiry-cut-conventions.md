---
title: "FX Option Expiry Cut Conventions: New York vs Tokyo"
seo_title: "FX Option Expiry Cuts: New York 10am vs Tokyo 3pm"
description: "The NY 10 am and Tokyo 3 pm cuts fix when an FX option stops trading and exercise locks in. How the two conventions differ and which cut to choose."
keywords:
  - fx option expiry cut
  - new york 10 am cut
  - tokyo 3 pm cut
  - fx derivatives expiry
  - option cut-off time
image: /svg/forex.svg
---

*The **FX option expiry cut** is the moment when an option stops trading and becomes exercised or expires worthless. The New York 10 am and Tokyo 3 pm cuts are the two standard conventions that dominate global FX markets — and choosing between them changes both the cost of your hedge and when your decision to exercise must be made.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">FX Option Expiry Cut — Key Facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for forex derivatives." />

<div class="wiki-infobox-caption">Most FX options expire at either New York 10 am ET or Tokyo 3 pm JST, locking in the intrinsic value at that moment.</div>

|   |   |
|---|---|
| **New York cut** | 10:00 am ET (calendar day of expiry) |
| **Tokyo cut** | 3:00 pm JST (calendar day of expiry) |
| **Time span** | ~19 hours apart (Tokyo cut comes first, globally) |
| **Who uses which** | Corporates, [asset managers](/active-etf/), central banks all use both—depends on their exposure |
| **Effect on price** | Earlier cut = fewer hours of volatility left = cheaper [option premium](/option-premium/) |
| **Exercise mechanism** | Automatic if [in-the-money](/in-the-money/) at cut; many systems default to exercise |

</aside>

## Why Two Cuts Exist

FX markets span the globe. When New York bankers are awake, Tokyo has already closed. When Tokyo opens, New York is asleep. A single expiry time would force either European corporates to wait until midnight, or Asian firms to cut decisions in the early morning.

The New York 10 am ET and Tokyo 3 pm JST conventions split the difference. Both are major financial centers where FX volumes peak. Tokyo 3 pm is also the European morning, when London and Frankfurt traders are active. New York 10 am is mid-morning in North America and evening in Europe. By offering both, the market lets hedgers choose a cut that aligns with their business day and risk-management window.

## Time Ordering and Fixing

Tokyo 3 pm JST arrives *first* on the calendar. By UTC:

- **Tokyo 3 pm JST** = 6:00 am UTC (same calendar day)
- **New York 10 am ET** = 2:00 pm or 3:00 pm UTC (depending on daylight saving)

If a contract specifies Tokyo cut, the option expires at 6:00 am UTC. A few hours later, New York cut happens. This ordering matters: a Tokyo-cut option locks in the spot rate hours before the New York cut, capturing different market conditions.

The fixing—the official [spot exchange rate](/spot-exchange-rate/) at the cut—is usually taken from a real-time market feed (Bloomberg, Reuters, ECB) or a poll of dealer prices. The reference is often the midpoint of the [bid-ask spread](/bid-ask-spread/), taken at the exact moment. No manual averaging; it's mechanical.

## How the Cut Affects Pricing

An FX option's premium reflects the risk that spot will move before expiry. A cut that comes *sooner* gives less time for the underlying to move. Fewer hours of volatility = lower [option premium](/option-premium/).

Compare two otherwise identical USD/JPY calls, both expiring on the same calendar date:

- **Tokyo 3 pm cut**: Expires at 6 am UTC.
- **New York 10 am cut**: Expires ~8 hours later, at 2–3 pm UTC.

The New York cut option costs slightly more, all else equal, because it has 8 more hours of market action to run. Over a month or quarter, this difference is modest. But for short-dated options (3–7 days), the spread widens noticeably—a 3-day option with an extra 8 hours of life can be 5–15% pricier.

## Hedging: Which Cut Should You Choose?

**Operational alignment** is the primary rule. If you collect invoice proceeds at 5 pm Tokyo time, you want to exercise your option *after* you know the payment amount. A Tokyo 3 pm cut expires before you even know your final yen balance. A New York 10 am cut gives you the whole Tokyo afternoon and evening to confirm your exposure.

Conversely, if your payable is due at noon New York time, the Tokyo 3 pm cut doesn't help—you've locked in your rate hours after your payment cleared. You'd want the New York 10 am cut to coincide with your cash outflow.

**Cost-benefit**: If matching your business process perfectly costs a material premium, you might settle for the cheaper, misaligned cut and accept the small FX slippage between your actual trade and the option cutoff.

**Counterparty convention**: In some currency pairs, one cut dominates. EUR/USD options in the interbank market historically traded more New York cuts; Asian exporters and importers in USD/JPY often prefer Tokyo. Your dealer may quote tighter spreads on the standard cut, nudging you toward the market convention.

## Automatic vs. Manual Exercise

At the cut, most [option contracts](/option/) exercise automatically if [in-the-money](/in-the-money/). The clearing house or settlement system checks the spot rate at the cut moment. If your call is above the [strike price](/strike-price/), it gets exercised without further instruction. If it's [out-of-the-money](/out-of-the-money/), it expires worthless.

Some contracts allow "American-style" exercise, where you can choose to exercise before the cut. FX options are often European-style—exercise only at expiry, at the official cut. This removes ambiguity: the cut time is the single decision point.

Banks typically send a settlement notification after the cut, confirming exercise and the cash flows due. For London-based treasury teams managing USD/JPY, a Tokyo 3 pm cut means a message arrives very early in their morning (around 6:30 am London time), letting them reconcile before market opens. A New York 10 am cut doesn't arrive until late afternoon UK time.

## Implications for Exotic Options and Strategies

**Knocked-out barriers**: If your option has a [barrier](/barrier-option/) (e.g., becomes void if spot touches 105.00), the monitoring typically runs through the cut. Some barriers monitor continuously up to the cut; others have discrete observation points. The cut time defines the final observation window.

**Quanto options**: A [quanto FX option](/quanto-fx-option-explained/) with a Tokyo 3 pm cut uses the 3 pm JST spot rate *and* interest-rate fixings at that moment to settle the FX leg. The cut pins down both—change the cut, and you may change the cashflow slightly if rates moved between the two cut times.

**Multi-leg spreads**: If you buy a New York 10 am call and sell a Tokyo 3 pm put on the same currency, you have *two different expiry times*. The put expires first, locking in your short strike. Hours later, the call expires long. This mismatch is unusual but possible in bespoke structures, and it can create intraday hedging gaps.

## Market Mechanics and Liquidity

Spot trading in FX never stops—it's 24-hour. But option trading does concentrate around Asian and US business hours. The Tokyo 3 pm cut means Tokyo traders can *see* the official rate at their cut and know immediately whether they're exercised. New York 10 am is the same for US teams.

A 3 pm Tokyo cut expiry that falls on a Friday is also a "Tokyo close" for the week. FX [volatility](/volatility-smile/) often tightens into an end-of-week Tokyo cut, because hedgers are squaring large positions ahead of the weekend. New York Friday cuts, by contrast, can see scattered volatility as US traders position heading into the US weekend (which overlaps the Asian start of the next week).

Dealers price both cuts simultaneously, but the Tokyo cut is often cheaper and tighter in spreads because volume is highest. If a corporate can afford to miss true operational alignment, the cost savings from going with the market-standard Tokyo cut can be meaningful.

## See also

<div class="wiki-seealso">

### Closely related

- [Option Premium](/option-premium/) — What determines whether you pay 2% or 5% for your hedge
- [Strike Price](/strike-price/) — The exchange rate at which your option converts into profit or loss
- [In-the-Money](/in-the-money/) — Why your option's value at the cut determines automatic exercise
- [FX Collar Option Strategy](/fx-collar-option-strategy/) — How to combine calls and puts with different cuts to reduce cost
- [NDF Settlement and Fixing Date](/ndf-settlement-fixing-date/) — Non-deliverable forwards use similar fixing mechanisms but different settlement logic
- [Spot Exchange Rate](/spot-exchange-rate/) — The rate locked at the cut moment

### Wider context

- [Foreign Exchange Derivatives](/derivatives-hedging/) — Overview of the full toolkit
- [Currency Risk](/currency-risk/) — Why corporations and investors hedge with options
- [Interest Rate Swap](/interest-rate-swap/) — Parallel tool for rates; uses similar fixing-date mechanics
- [Quanto FX Options Explained](/quanto-fx-option-explained/) — Options where the FX cut also determines the conversion rate

</div>