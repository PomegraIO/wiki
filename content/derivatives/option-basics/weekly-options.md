---
title: "Weekly Options"
description: "Short-dated options contracts expiring every Friday; accelerated time decay and high gamma create rapid profit-and-loss swings suitable for tactical trading."
keywords:
  - weekly options
  - short-dated derivatives
  - theta decay
  - gamma
  - expiration
image: "/svg/derivatives.svg"
---

*A **weekly option** is an [option](/derivatives/option-basics/) contract that [expires](/expiration-date/) every Friday, rather than on the standard third Friday of each month. Weeklies compress the entire arc of an [option's](/derivatives/option-basics/) life—from high [time value](/option-premium/) to zero—into seven days. This creates extreme [time decay](/theta/) (also called [theta](/theta/)), explosive [gamma](/gamma/), and violent P&L swings suitable only for traders comfortable with high friction and rapid decision-making.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Weekly Options — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives and contracts." />

<div class="wiki-infobox-caption">Seven-day expiration cycles with ferocious time decay; a trader's tool, not an investor's.</div>

|   |   |
|---|---|
| **What it is** | An [option](/derivatives/option-basics/) contract expiring each Friday instead of monthly |
| **Expiration cycle** | Every Friday; multiple weekly series exist simultaneously |
| **Typical daily [theta](/theta/)** | 5–20% of [premium](/option-premium/) per day near expiration |
| **Liquidity** | Good for major indices and mega-cap stocks; thin elsewhere |
| **Primary use** | Tactical directional bets; income generation; hedging short-term volatility |
| **Risk profile** | Extreme [time decay](/theta/); rapid profits and losses; [assignment risk](/exercise-price/) |
| **Trading horizon** | Days to one week; unsuitable for position holding |

</aside>

## The violent arithmetic of seven-day decay

A standard monthly [option](/derivatives/option-basics/) expires on the third Friday of the month, roughly 30 days away. A weekly [option](/derivatives/option-basics/) expires the following Friday—seven days away. This compression of time creates proportionally extreme [time decay](/theta/).

Consider a call option on a large-cap stock, struck slightly out-of-the-money. One week before [expiration](/expiration-date/), the [option](/derivatives/option-basics/) might be worth $0.50. The [theta](/theta/) ([daily](/expiration-date/) time decay rate) could be $0.08 per day. This means the [option](/derivatives/option-basics/) loses 16% of its value every single day without any move in the stock. On the last two days before [expiration](/expiration-date/), [theta](/theta/) accelerates; the [option](/derivatives/option-basics/) might lose 20–30% per day.

For an out-of-the-money weekly call, the [theta](/theta/) burn is even fiercer. An [option](/derivatives/option-basics/) worth $0.10 might lose $0.03 per day—30% decay per day. This is not a slow erosion; it is an onslaught. The trader is racing against the calendar.

The payoff is that weeklies are cheap to buy. An out-of-the-money weekly call costs a fraction of what the equivalent monthly call costs, because there is less time for the stock to move into profit. This attracts speculators chasing leverage: $200 in buying power can control 1,000 shares of notional exposure if the call is far out-of-the-money. But that leverage evaporates in days if the stock does not move decisively.

## Gamma explosion: why weekly options move so fast

[Gamma](/gamma/) measures the acceleration of [delta](/delta/)—the rate at which an [option's](/derivatives/option-basics/) sensitivity to the stock changes. A standard [option](/derivatives/option-basics/) has modest [gamma](/gamma/). A weekly [option](/derivatives/option-basics/) has ferocious [gamma](/gamma/), especially near [expiration](/expiration-date/).

Here is the practical effect: suppose a stock is at $100 and a weekly call at a $100 strike (at-the-money) has [delta](/delta/) of 0.50. You own one contract (100 shares notionally). The stock rallies $1 to $101. Normally, an out-of-the-money option might gain $0.50 (the [delta](/delta/)). But with a weekly, the [delta](/delta/) surges—maybe to 0.70—and the option gains $0.70. The next $1 rally moves the option another $0.85 (because [delta](/delta/) is now 0.85). 

This explosive sensitivity works both ways. A $1 drop vaporizes the [delta](/delta/)—maybe to 0.20—and the option loses $0.70. Your $1 bearish move cost you $70 per contract. One bad day can wipe out a week's worth of careful analysis.

Professional traders exploit this [gamma](/gamma/). Market makers hold [gamma](/gamma/) positions and scalp the [bid-ask](/bid-ask-spread/) spread throughout the week, profiting from the fact that [gamma](/gamma/) is priced into the [option's](/derivatives/option-basics/) [premium](/option-premium/). But retail traders usually get scalped: they buy a weekly, a small adverse move crushes them, and they exit at a loss before the thesis can play out.

## Liquidity and the hidden cost of spreads

Weekly [options](/derivatives/option-basics/) are liquid for large-cap stocks and broad indices. SPY (S&P 500 ETF) has massive weekly volume; Apple, Amazon, and Tesla do as well. But for smaller-cap stocks, weeklies may not exist at all, or if they do, the [bid-ask spread](/bid-ask-spread/) is brutally wide.

This matters more than it seems. A monthly call might have a $0.10 [spread](/bid-ask-spread/) (bid $1.00, ask $1.10). A weekly on the same stock might have a $0.30 [spread](/bid-ask-spread/) (bid $0.45, ask $0.75). You buy at $0.75 and the position must move just to get back to breakeven when you exit at the bid. By the time you factor in commissions and slippage, the [option](/derivatives/option-basics/) needs to move sharply to profit.

This is why professional weekly traders focus on mega-cap names and indices: the [spread](/bid-ask-spread/) is tight enough that [gamma](/gamma/) scalping is viable. For other securities, the [spread](/bid-ask-spread/) is the enemy.

## Tactical uses: hedging and directional bets

Weeklies shine in narrow use cases. A hedge fund manager holding a large position in a stock can buy weekly out-of-the-money puts to hedge Friday's jobs report or Fed announcement. The [premium](/option-premium/) is cheap because there is only six days to [expiration](/expiration-date/). If the announcement tanks the stock, the puts spike in value and offset the loss. If the announcement is neutral, the puts expire worthless—a cheap insurance cost.

Similarly, a trader with a conviction bet on a specific catalyst—an earnings miss, a regulatory ruling, a geopolitical event—might buy weekly calls or puts. If the event happens and the stock gaps, the weekly explodes upward in value, turning a $300 investment into $3,000. If the event does not happen, the trader loses the $300 and moves on. This is the slot-machine logic of weeklies: small frequent losses, rare outsized wins.

Some traders use weeklies for income. They sell deep out-of-the-money weekly calls against a stock they own, collecting $0.10–$0.30 per share per week. Over 52 weeks, this can add up to 5–10% of annual yield if the calls never get assigned. The risk is that the stock rallies sharply and the shares are called away; the trade then becomes a forced short sale.

## The psychology trap: overconfidence and assignment risk

Weekly [options](/derivatives/option-basics/) are seductive because they make trading feel urgent and actionable. A monthly [option](/derivatives/option-basics/) is abstract; the stock might move. A weekly is concrete; the move has to happen this week or the [option](/derivatives/option-basics/) dies. This creates artificial urgency that often leads to poor decisions.

Traders oversize positions because the [premium](/option-premium/) is cheap. A trader tells herself, "I can only lose $0.20 per share." But she buys 100 contracts (10,000 shares notionally), and her total loss is $2,000 if the [option](/derivatives/option-basics/) expires worthless. This is why weekly traders burn through capital so quickly.

[Assignment risk](/exercise-price/) is another hidden trap. If you sell deep out-of-the-money weekly calls and the stock rallies past the strike on Thursday, you will be assigned early—forced to sell your shares at the strike price on Friday morning, just as the stock is moving higher. You locked in a loss you did not want. Buying weekly calls on a stock about to pay a dividend also carries [assignment risk](/exercise-price/) if the call goes deep in-the-money; the call buyer may exercise early to capture the dividend, leaving you with cash instead of the stock position you wanted.

## When weeklies make sense and when they do not

**Good use cases**:
- Hedging a specific catalyst (earnings, Fed decision) over the next few days.
- Ultra-short-term directional bets by traders comfortable with [gamma](/gamma/) and [theta](/theta/) dynamics.
- Collecting premium by selling far out-of-the-money calls against a position you own, if you accept [assignment risk](/exercise-price/).
- Scalping [bid-ask](/bid-ask-spread/) spreads as a market maker in high-volume tickers.

**Bad use cases**:
- Position holding: if you do not plan to act daily, a monthly [option](/derivatives/option-basics/) or stock ownership is simpler.
- Low-capital traders: the [spread](/bid-ask-spread/) and [theta](/theta/) burn make small positions uneconomic.
- Stocks with low weekly volume: the cost of illiquidity outweighs the leverage benefit.
- Traders who cannot afford to lose: weeklies magnify both gains and losses; only risk capital you can afford to lose.

## The advantage of monthly options over weeklies for most traders

Most traders are better off ignoring weeklies and using standard monthly [options](/derivatives/option-basics/). Monthlies have lower [theta](/theta/) per day, giving your thesis time to unfold. They have tighter [spreads](/bid-ask-spread/) on a wider range of stocks. The leverage is real but sustainable. And emotionally, a monthly [option](/derivatives/option-basics/) does not feel like a lottery ticket; it feels like a genuine bet.

The traders who profit from weeklies are those who treat them as a business—scalping [spreads](/bid-ask-spread/) as a market maker, or selling premium systematically and taking assignment when it comes. Retail traders buying weeklies in hopes of a big score are usually wrong about the timing and pay the price in [gamma](/gamma/) losses and [spread](/bid-ask-spread/) friction.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/derivatives/option-basics/) — core mechanics and contract structures
- [Theta](/theta/) — daily time decay and the relentless bleeding of near-term value
- [Gamma](/gamma/) — explosive delta changes and volatility of weekly P&L
- [Delta](/delta/) — directional sensitivity and how it accelerates in weeklies
- [Expiration date](/expiration-date/) — the Friday cycle and how it differs from monthly expirations
- [Bid-ask spread](/bid-ask-spread/) — the hidden cost of entry and exit in illiquid series
- [Deep out-of-the-money option](/deep-out-of-the-money-option/) — where most weekly speculative buying happens
- [Call option](/call-option/) — bullish weekly structures
- [Put option](/put-option/) — bearish and hedging weekly structures

### Wider context

- [Implied volatility](/volatility-smile/) — shorter dated = more vulnerable to volatility shifts
- [Option premium](/option-premium/) — why weeklies are cheap compared to monthlies
- [Market maker](/market-maker-trading/) — the other side of weekly option spreads
- [Time value](/time-value/) — the entire premium of a weekly is time value, and it evaporates fast
- [Stock](/stock/) — the underlying asset; often simpler for most traders
- [Over-the-counter market](/over-the-counter-market/) — where institutional weeklies trade

</div>
