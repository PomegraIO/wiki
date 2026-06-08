---
title: "Carry Trade Strategy Explained"
description: "How carry trade strategies use interest-rate differentials between currencies to generate profit, and why rapid reversals and crowding can amplify losses."
keywords:
  - carry trade strategy explained
  - interest rate currency trading
  - uncovered interest rate parity
  - carry trade unwind
  - fx leverage strategy
image: /svg/strategies.svg
---

*A **carry trade strategy** borrows in a low-interest-rate currency (say the yen at 0.5%) and invests the proceeds in a higher-yielding currency or asset (say Australian dollars earning 4%), pocketing the interest differential of 3.5% per year—assuming exchange rates stay put. But carry trades amplify losses when the funding currency unexpectedly appreciates, squeezing positions and forcing liquidations. Crowded, high-leverage carries are prone to sudden unwinding, making them profitable in calm markets and catastrophic in shocks.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Carry Trade — key facts</div>

<img src="/svg/strategies.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">An asymmetric bet: collect interest in stability, lose it all in a reversal.</div>

|   |   |
|---|---|
| **Core mechanism** | Borrow low, invest high; pocket the spread |
| **Funding currency** | Low-rate (yen, franc, euro) |
| **Investment currency** | High-rate (emerging-market currencies, high-yield bonds) |
| **Profit source** | Interest-rate differential, if FX flat |
| **Key risk** | Funding currency appreciation; forces liquidation |
| **Leverage** | Often 5–20x; amplifies gains and losses |
| **Typical horizon** | Months to years (longer than day trading) |
| **Crowding risk** | Correlated, forced selling can cascade |

</aside>

## The Core Mechanic: Borrowing and Lending at Different Rates

A carry trade is a **spread trade**. The trader (or hedge fund) borrows money in a currency where [interest rates](/interest-rate/) are low—historically Japan (yen near 0%), Switzerland (franc often <1%), or the euro (sub-1% during certain cycles). The borrowing cost is the short-term funding rate: repo rate, overnight index swap ([SOFR](/sofr/)), or the central bank's policy rate plus a small spread.

With that borrowed cash, the trader invests it in a higher-yielding asset: bonds or currencies of countries with elevated [interest rates](/interest-rate/). Emerging-market governments (Turkey, Mexico, Brazil) often offer 5–10% yields. Or the trader buys high-yield corporate bonds. Or simply deposits the money in a high-rate currency's money market. The investment yield is 4–6%.

The **profit is the spread**: 5% investment yield minus 1% funding cost = 4% annual carry. On $1 billion borrowed and deployed, that's $40 million per year if the spot [exchange rate](/spot-exchange-rate/) never moves.

## Why Carry Works in Calm Markets

Carry trades are profitable during periods of:

**Low volatility.** When [currency volatility](/currency-volatility/) is subdued, the odds that the funding currency suddenly appreciates shrink. If a trader borrows yen and buys Turkish lira bonds, and the yen/lira [exchange rate](/spot-exchange-rate/) is stable, the carry accrues without disruption. The VIX is low, risk appetite is high, and investors are comfortable holding foreign assets.

**Stable central-bank policy.** If the interest-rate differential is entrenched (Japan's rates locked at near-zero while Turkey's are 20%), the carry persists. Central banks are predictable, and traders can deploy capital with confidence.

**Low [counterparty risk](/counterparty-risk/):** Emerging-market assets are liquid and creditworthy (or perceived so). Funding markets are deep—borrowing yen in the repo market is straightforward.

These conditions held in much of the 2010s, especially after the 2008 crisis. The yen was cheap, funding easy, and emerging-market yields enticing. Billions flowed into carry trades.

## The Reversal Scenario: Why Unwinds Are Violent

A carry trade unwind occurs when **the funding currency appreciates**—the opposite of what the trader needs. Suppose a hedge fund borrowed $100 million yen at 0.5%, converted to Turkish lira, and bought lira bonds yielding 15%. The profit was 14.5% annually on notional $100 million—$14.5 million per year.

Then a shock hits: the Turkish central bank surprises markets by tightening policy, or geopolitical risk rises, or a global "risk-off" event (recession, bank crisis, deflation panic) triggers. Investors who hold risky emerging-market assets get spooked. They sell en masse. The lira crashes. A trader who borrowed yen and bought lira is now underwater on the currency move alone.

But worse: the shock that weakened the lira also *strengthened the yen*. Why? During global risk-off events, investors flee to safe havens—the yen (a low-rate, stable currency with deep markets) and U.S. Treasuries are destinations. Demand for yen soars, pushing its [exchange rate](/spot-exchange-rate/) sharply higher. A trader holding yen debt now faces a twofold loss:
1. The lira investment has crashed (EM assets sold off).
2. The yen funding currency has *appreciated* against all other currencies (the debt is harder to repay).

## Leverage Amplifies the Unwind

Most carry trades are leveraged 5–20x. A fund with $1 billion of capital might borrow $10 billion in low-rate currency. The leverage magnifies carry accrual: on $10 billion deployed at 4% carry, the fund makes $400 million per year. But it also magnifies losses. A 10% move against the trade—yen appreciates 10% and lira falls 5%—can wipe out the fund's entire capital.

When losses mount, the leveraged fund faces a margin call: it must post more collateral to cover unrealised losses. If the fund can't raise cash, it must liquidate positions. Liquidating a large foreign asset position requires selling in the market. If many funds are liquidating simultaneously—which they are, because they're all reacting to the same shock—the selling cascades. Asset prices fall further, forcing more liquidations. The market becomes disorderly.

## The Mechanics of Unwind Cascades

Carry trades are often crowd-like. If the yen-carry is profitable, hundreds of hedge funds, proprietary trading desks, and retail traders pile in. They borrow yen in the same repo markets, buy the same emerging-market bonds. When the shock hits and one fund liquidates, it doesn't just trigger its own losses—it impacts the market for lira, causing the lira to fall further and forcing other funds to liquidate.

In August 2024 and September 2023, when Bank of Japan hints about tightening surfaced, yen-funded carry trades unwound. The yen surged 10% in weeks. Funds that were short yen and long risky assets faced savage losses. Stock markets globally fell 5–10% in correlation. The carry unwind is not just a forex event—it propagates through equity and credit markets, tightening financial conditions and reducing appetite for risk assets overall.

## Interest-Rate Parity and the Rationalisation

Economic theory, called uncovered [interest-rate parity](/interest-rate/) (or "UIP"), says that if a high-rate currency offers a 4% advantage over a low-rate currency, the low-rate currency should appreciate by roughly 4% per year, erasing the carry. In a frictionless, perfectly-efficient market, no one can earn a free 4% return indefinitely.

But UIP fails systematically. Emerging-market currencies and weak currencies *don't* appreciate to offset their yield disadvantage. Instead, they *depreciate* over time, making the carry even worse for survivors. This is the "forward-premium puzzle": high-yield currencies have historically been bad bets on a forward-looking basis, yet the carry was positive in real time.

The reason carry persists is **risk premium**. Traders accept lower long-term returns in exchange for carry accrual in the near term. They are compensated for the tail risk of an unwind. Some carry-trade researchers argue that the strategy has been a chronic loser over decades—you accumulate carry steadily but face rare, severe drawdowns that overwhelm the small annual gains. The 2024 unwind was a vivid reminder.

## Positioning and Crowding: The Canary in the Mine

Market participants monitor carry positioning closely for early signals. If hedge-fund positioning in a carry trade is at extremes (leveraged at the limit, concentration high), the stage is set for an unwind. A small shock—a Fed speaker's comment, a surprising inflation print, a geopolitical flare-up—can tip the market from carry accumulation to liquidation.

Data on [futures](/futures-contract/) positioning, cross-currency basis swaps, and repo specialness (yen repo rates turning deeply negative) give signals that carry is crowded. Sophisticated traders use these signals to de-risk ahead of shocks.

## Variations and Hedging

Some traders run "pair trades" that reduce the unwind risk. Instead of going long a high-yield currency and short a safe-haven currency outright, they run a carry trade between two non-reserve currencies—borrowing Polish zloty to buy Brazilian real, for example. The shock dependence is lower because neither is a canonical "safe haven." But the carry is smaller too.

Others hedge the currency risk with [options](/option/) or [forwards](/forward-contract/), locking in the [interest-rate](/interest-rate/) spread. This eliminates the unwind risk but costs money (the option premium, the forward bid-ask), eating into the carry. Most carry traders *don't* hedge, because the hedge cost exceeds the carry itself in calm markets, and they're confident (incorrectly) that they can exit before a shock.

## Systemic Implications

Carry trades matter for financial stability because they are systemic. When they unwind, asset prices fall sharply, funding markets tighten (repo rates spike), and [counterparty risk](/counterparty-risk/) fears rise. Central banks watch carry exposure as an early-warning indicator of financial stress. The 2024 yen unwind, modest by historical standards, still triggered 3–4% stock-market declines in the US and Japan—a reminder that carry unwinds propagate.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest Rate](/interest-rate/) — the differential that funds the trade
- [Currency Volatility](/currency-volatility/) — spikes during carry unwinds and create losses
- [Leverage Ratio (Forex)](/leverage-ratio-forex/) — the amplification of carry trades
- [Spot Exchange Rate](/spot-exchange-rate/) — the rate at which the carry is booked; appreciation triggers losses
- [Forward Contract](/forward-contract/) — can hedge currency risk but costs money
- [Uncovered Interest Rate Parity](/uncovered-interest-rate-parity/) — the theory predicting carry trades should earn zero; empirically false
- [Counterparty Risk](/counterparty-risk/) — risk that the lending or borrowing entity fails

### Wider context

- [Momentum Investing](/momentum-investing/) — carry trades are a form of momentum in FX and fixed income
- [Basis Risk](/basis-risk/) — mismatch between the rate paid and the rate earned
- [Systemic Risk](/systemic-risk/) — carry unwinding can trigger broad-market stress
- [Hedge Fund](/hedge-fund/) — the investor type most active in carry trading
- VIX Index — when the VIX spikes, carry unwinds accelerate

</div>
