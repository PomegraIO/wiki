---
title: "Basis Trade Hedging Risk"
description: "A basis trade—long a cash bond and short futures—hedges spread risk but exposes traders to repo-rate, margin-call, and funding stress during market crises."
keywords:
  - basis trade hedging risk
  - bond futures basis trade
  - cash-and-carry basis
  - repo rate risk basis trade
  - basis trade margin call
image: /svg/risk.svg
---

*A **basis trade** is a classic fixed-income arbitrage: buy a bond outright (the cash position) and simultaneously short an equivalent futures contract (the derivative position). The strategy is designed to capture the difference—the basis—between the bond's spot price and the futures price, which should theoretically converge at contract expiration. The beauty is that the strategy appears to hedge away market risk: if rates rise, both positions lose equally, leaving the trader with just the basis spread profit. The trap is that basis trades introduce three hidden risks—repo funding, margin calls, and funding stress—that can blow up the trade during exactly the times it is supposed to protect.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Basis trade risk — The mechanical reality</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A seemingly safe arbitrage becomes dangerous when funding markets freeze and margin requirements spike.</div>

|   |   |
|---|---|
| **Position structure** | Long bond + short futures = spread capture |
| **Intended hedge** | Rate risk cancels; trader captures basis |
| **Hidden risk 1** | Repo-funding cost during stress rises sharply |
| **Hidden risk 2** | Futures margin call forces early exit at loss |
| **Hidden risk 3** | Leverage amplifies losses if basis widens |
| **Stress event trigger** | Credit event, financial stress, liquidity crunch |

</aside>

## The basic structure and rationale

A trader enters a basis trade by:
1. Buying a bond (e.g., a 10-year Treasury) at its spot price
2. Simultaneously selling (shorting) a Treasury futures contract at its futures price
3. Holding both positions to maturity or until convergence

**The theory is sound.** At futures expiration, the futures price *must* converge to the cash bond price (otherwise arbitrage would explode the difference). The gap between the two—the basis—represents a "free" profit once rate risk is hedged away. If the basis is 2 basis points wide, a trader locking in that spread captures 2 bps risk-free.

This simple arbitrage has been profitable for decades and remains a staple of fixed-income desks. But the trade has costs and risks that are not obvious in calm markets.

## The funding cost: Repo rates and the carry

To finance the long bond position, a trader typically borrows via [repurchase agreement (repo)](/repurchase-agreement/). The trader sells the bond to a lender with a commitment to repurchase it at a slightly higher price. The rate difference—the repo rate—is the funding cost.

The basis profit is only real if the basis spread exceeds the financing cost. A basis of 2 bps is worthless if repo financing costs 5 bps. A trader thus relies on **repo rates staying low and stable**.

This assumption fails during stress. When credit tightens, **repo rates spike**. The 2008 financial crisis saw repo rates on certain securities jump from 2–3% to 10%+ literally overnight. During the March 2020 COVID panic, Treasury repo rates spiked to levels not seen since 2008. In 2023, the regional banking crisis briefly spiked repo rates again.

When repo rates spike above the basis width, the trade flips from profitable to loss-making. A trader holding the position now loses money on the daily financing. The longer the trade is held, the larger the loss.

## Margin calls and forced liquidation

The short futures position is marked-to-market daily. If rates rise and the futures price falls, the trader receives a margin credit. But if rates fall and the futures price rises, the trader faces a **margin call**—a demand for cash to cover the loss on the short position.

If the trader does not have enough cash on hand or cannot borrow it at reasonable cost, the trader must liquidate the short futures position early. But here is the trap: **when a trader is forced to cover a short futures position at an inopportune time, it locks in a loss**. The basis trade only profits if the trader can hold both legs to convergence.

During the 2008 crisis, many basis traders faced exactly this situation. The short futures position moved against them; margin calls came due; and they were forced to exit the short, closing out the hedge. The long bond position remained, now entirely unhedged, in a market where bonds were selling off.

## The leverage amplifier

Most basis traders use leverage to amplify returns. If a basis of 2 bps is worth 2 bps on $1 million notional, it is worth 20 bps on $10 million notional. A typical leveraged basis trade might deploy 5–10x notional leverage, financed through repo.

Leverage is neutral if the bet works perfectly: the trader captures the basis on a larger balance sheet and earns proportionally more. But leverage is pernicious if anything goes wrong. A margin call that is 5% of notional is manageable; a margin call that is 5% of 10x leveraged notional is a catastrophe.

When repo funding becomes scarce or expensive, a leveraged basis trader often has no choice but to deleverage. This means selling the long bond position into a market that may be illiquid, taking a loss on the exit price. The trader wanted to hold to maturity; the funding market forced an early exit.

## The 2019 Treasury market episode

A dramatic real-world example occurred in September 2019, when Treasury repo rates spiked to 10% overnight. The spike was triggered by a combination of corporate tax payments, quarter-end demand for dollars, and a surprise withdrawal of reserve balances from the Federal Reserve. But the immediate effect was brutal for basis traders.

Traders who had funded long Treasury positions overnight saw their financing costs jump 500+ basis points in a single day. Those who had shorted futures to hedge found themselves facing pressure on both fronts: the repo funding became expensive, and the margin calls mounted as the short futures positions deteriorated. The result was a disorderly unwind: basis traders dumped long positions, which forced yields higher, which forced more margin calls.

The Federal Reserve had to intervene with billions of dollars of reverse-repo operations to stabilize funding. Without that intervention, some estimates suggest the spiral could have cascaded into a credit event.

## Why the basis trade is still popular despite the risks

Despite these hazards, basis traders remain active because:

1. **The returns are real in normal times.** A basis of 2–3 bps, financed at 1.5 bps, nets a genuine arbitrage profit.

2. **The risks are invisible during calm markets.** A trader can run the strategy for years without facing a margin call or a repo funding crisis.

3. **Competition keeps the basis tight.** If the basis gets too wide, more traders pile in, compressing it back down. The need to capture a narrowing basis incentivizes leverage.

4. **Short-term performance pressure drives risk-taking.** A basis trader measured on monthly or quarterly returns has an incentive to employ leverage. A brief funding crisis is an acceptable tail risk if it improves expected returns in most scenarios.

## Risk management and mitigations

Sophisticated basis traders manage these risks through:

- **Maintaining a cash buffer.** Holding enough unencumbered liquidity to cover potential margin calls without forced liquidation.
- **Diversifying funding sources.** Using both overnight and term repo, and spreading exposures across multiple lenders to reduce the risk that a single funding source dries up.
- **Monitoring repo rates and basis spreads in real time.** A trader who watches repo rates carefully can exit early if funding costs begin to rise unsustainably.
- **Stress testing leverage.** Running scenarios where repo rates spike 500 basis points and asking: "Can I survive this?"
- **Maintaining lines of credit.** Securing backup financing from central banks or other sources that remain available during stress.

Even with these precautions, **the fundamental fragility remains**. During a true systemic crisis—a financial panic, a major credit event, a sudden policy shock—basis traders are vulnerable.

## The systemic dimension

Basis trading is not just an individual trader's problem. Aggregate basis trades represent a significant portion of the balance sheets at major fixed-income dealers and hedge funds. When funding markets freeze, the entire basis-trading community can face forced liquidation simultaneously. This can trigger a vicious cycle: forced selling pushes yields higher and widens credit spreads, which creates more margin calls, which forces more selling.

The 2008 crisis and the 2019 repo spike both illustrated how individual basis trades, when aggregated across the market, can become a systemic risk. Central banks now monitor basis trading activity specifically for this reason.

## See also

<div class="wiki-seealso">

### Closely related

- [Basis](/basis/) — The foundation concept of basis trading
- [Futures contract](/futures-contract/) — The derivative used to short the hedge
- [Repurchase agreement](/repurchase-agreement/) — The repo financing mechanism
- Arbitrage — The core strategy and its mechanics
- [Margin call](/margin-call-forex/) — The forced-liquidation trigger
- [Hedge fund](/hedge-fund/) — Common executor of basis trades

### Wider context

- Fixed-income trading — Broader context for bond trading strategies
- Leverage — Amplification of returns and risks
- [Liquidity risk](/liquidity-risk/) — Inability to exit positions at fair prices
- [Systemic risk](/systemic-risk/) — How individual trades become market-wide risks
- [Stress testing](/stress-testing/) — Risk management approach for tail scenarios

</div>
