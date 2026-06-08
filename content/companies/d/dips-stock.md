---
title: "YieldMax Short NVDA Option Income Strategy ETF (DIPS)"
description: "A single-stock covered-call ETF that sells short call options on Nvidia shares to generate income, resetting daily and creating a leveraged income-and-decline bet."
keywords:
  - covered call
  - option income
  - Nvidia
  - single-stock ETF
  - income strategy
  - volatility capture
handwritten: true
---

<aside class="wiki-infobox">
<div class="wiki-infobox-title">DIPS at a glance</div>

|   |   |
|---|---|
| **Underlying** | Nvidia Corp. (NVDA) stock |
| **Strategy** | Sells short calls on NVDA and buys the stock |
| **Structure** | Daily-reset covered call ETF |
| **Payout mechanism** | Monthly distributions from option premiums |
| **What you own** | Shares of NVDA + a short call position |
| **Expense ratio** | ~0.75% (high due to options overhead) |
| **Volatility decay** | Yes — daily rebalancing erodes returns in choppy markets |
| **Best case** | Stock flat or down; you keep premiums collected |
| **Worst case** | Stock soars; gains are capped and you lag NVDA |

</aside>

## The core mechanism

DIPS holds shares of [Nvidia](/nvda-stock/) (NVDA) and continuously sells short-term [call options](/call-option/) against those shares. When an investor buys a call option, they are paying the seller (in this case, the fund) for the right to buy the stock at a set price before expiration. The fund pockets that premium and passes most of it to shareholders as monthly income distributions. In exchange, if NVDA rallies above the [strike price](/strike-price/) of the short call, the stock will be called away — the buyer of the call exercises it and takes the shares at that strike, and the fund buys back the called-away shares with the cash to start the cycle again.

On the surface, this sounds clean: collect premium, distribute income, manage downside. In practice, DIPS is a bet on **Nvidia going sideways or down.** If NVDA stays flat, the monthly [option premiums](/option-premium/) compound into respectable annualized yields — anywhere from 10% to 25% depending on volatility and strike selection. If NVDA falls, the short call position actually benefits (the option expires worthless, and the fund keeps the full premium). But if NVDA soars 50% in a year, the short calls cap the fund's upside, and DIPS will trail a simple buy-and-hold of NVDA stock by the full amount of the premium income it collected. You have traded away participation in a rally for higher current income — a bet, not a gift.

## Why daily resets, and why they matter

DIPS resets its options positions daily, rolling out call contracts and restarting the income cycle. This is done primarily for tax efficiency and operational flexibility, but it creates a mechanical drag in sideways or choppy markets. Here is the issue: if NVDA bounces around between $120 and $130 over a year, the daily resetting of positions means the fund sells calls at different strike levels on different days. Some of those calls get called away when the stock rallies, only to be repurchased the next day at a loss. Other calls expire worthless and are replaced. The cumulative effect of this constant churning is that in a volatile, range-bound market, the fund's performance trails what a simple once-per-month [covered call](/covered-call/) strategy would have achieved. This is called **volatility decay** — the cost of daily rebalancing in a noisy market.

## The payoff structure and who it suits

DIPS creates a truncated return profile. Nvidia holders get full upside (minus volatility decay from options); DIPS holders get capped upside but higher current income. Think of it as trading potential capital gains for a steady income stream. If you believe NVDA will grind sideways or decline — or if you own NVDA already and want to generate income against it while willing to give up some upside — the strategy is coherent. If you expect NVDA to be a 50%+ winner over your [holding period](/holding-period/), DIPS will hurt relative to just holding the stock.

The risk profile is also unusual. Downside is partially cushioned — the premium income offsets a portion of any decline in the stock. But in a sharp NVDA sell-off (say, a 30% drop), the income does not fully compensate, and you still lose significantly. The psychological challenge is that you are holding a concentrated, volatile single stock (NVDA) and getting a partial hedge via premiums, but it is not a real downside hedge — just a modest income cushion.

## Costs and tax considerations

The [expense ratio](/expense-ratio/) is roughly 0.75%, higher than a plain NVDA position or a broad-based covered-call ETF, reflecting the options trading and rebalancing overhead. More important for taxable accounts: covered-call strategies often generate short-term capital gains and option-exercise realized losses, both tax-inefficient. DIPS is structured to minimize this, but the daily trading and potential for called-away positions (realized gains every time shares are called and repurchased) can create tax drag in taxable accounts. In a retirement account where tax does not matter, that burden is lifted.

## The real risks

The core risk is **Nvidia concentration**. This is not a diversified bet on the semiconductor sector or technology broadly; it is a one-company wager. If NVDA faces fundamental trouble — competition, slowdown in AI chip demand, regulatory action — there is no portfolio [diversification](/diversification/) to dampen it. The second risk is **options blow-ups**. Option strategies can move in unexpected ways during market dislocations. If NVDA gaps down sharply on earnings or news, the short calls the fund sold might be far out of the money, and the income stream dries up until volatility normalizes and premiums widen again. The third risk is **the drag from daily resets**. In a sideways market, you will underperform a simpler approach. And the fourth risk is **the cap on upside**. If AI-powered Nvidia becomes as dominant as investors hope, DIPS will underperform significantly.

## How to think about it

DIPS is not a "free income" machine. It is a way to monetize the belief that Nvidia will trade in a range or decline, and that the income from collected premiums is a better use of capital than waiting for appreciation. It is appropriate only if you have a specific view on NVDA's near-to-medium-term direction and are willing to cap upside. If you think NVDA is a generational compounder, this strategy is a poor fit, regardless of the attractive yield. If you think NVDA is fairly valued and choppy for the next couple of years, collecting premium income while waiting for clarity is a rational bet. The prospectus and fact sheet explain the daily-reset mechanics and the historical performance in various NVDA price scenarios — study those carefully before committing.
