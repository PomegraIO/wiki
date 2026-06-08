---
title: "Overnight Margin in Futures Trading: What Happens After the Close"
description: "How initial margin in futures differs from intraday maintenance margin, why brokers demand higher overnight coverage, and the gap-risk exposure traders face."
keywords:
  - futures trader overnight margin risk
  - initial margin vs maintenance margin
  - overnight margin requirements
  - gap risk in futures
  - futures margin call mechanics
---

*In futures trading, overnight margin represents the capital a broker requires you to hold from market close to market open—typically much higher than the intraday maintenance margin. This stricter standard exists because overnight, your position cannot be monitored continuously, and price gaps from overnight news can instantly wipe out your cushion. Understanding the difference between initial and maintenance margin, and the timing of margin calls after the close, is critical to avoiding forced liquidation.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Overnight Margin — key facts</div>

<img src="/svg/people.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Overnight margin is stricter than intraday to protect brokers from gap risk.</div>

|   |   |
|---|---|
| **Initial margin** | 50–100% of maintenance; locked in at trade entry; nonrefundable per round turn |
| **Maintenance margin** | Intraday threshold; if you fall below, you receive a margin call |
| **Overnight margin** | Often 120–150% of maintenance; applies from close to open next day |
| **Gap risk** | Overnight news (earnings, geopolitical events, macro data) can create unfillable overnight gaps |
| **Liquidation timing** | Brokers may auto-liquidate at open if you're below overnight requirement |

</aside>

## Initial margin versus maintenance margin

To open a futures position, you must deposit **initial margin**—a lump sum that clears once per contract entry. This is nonrefundable per round-turn (entry and exit). Brokers set initial margin to cushion against typical intraday volatility plus a buffer. For a standard [E-mini S&P 500 futures contract](/sp-500-index/), initial margin is roughly $10,000–$12,000 in normal conditions.

**Maintenance margin** is lower—typically 70–75% of initial—and represents the minimum balance you need to maintain in your account while the position is open during market hours. If your account equity falls below maintenance margin because of intraday losses, the broker issues a margin call. You have until close of business to deposit cash; if you don't, the broker liquidates enough contracts to restore you to maintenance level.

Overnight, however, the rules tighten. Many brokers impose an **overnight margin requirement** that is higher than maintenance—sometimes 100–150% of the day's maintenance threshold. The reason: between close and open, no continuous monitoring is possible, and [credit risk](/credit-risk/) spikes.

## Why overnight margins are stricter

During market hours, your broker can monitor your P&L in real time and liquidate positions in seconds if you approach the maintenance margin floor. This continuous surveillance allows brokers to keep intraday margin thresholds relatively tight. Once the market closes, that safety valve disappears. A position that was safely above maintenance margin at 4:00 PM could gap against you overnight if a major news event breaks—Fed announcement, earnings surprise, geopolitical shock, natural disaster—and when markets reopen, you may be deeply underwater before you can trade.

A simple example illustrates the danger. Suppose you are **long** 10 E-mini S&P 500 contracts with initial margin of $10,000 per contract (=$100,000 total), and your maintenance margin requirement is $7,000 per contract. The market closes. Overnight, a central bank surprises markets with a dovish pivot, and futures rally 100 basis points, adding $5,000 per contract to your position, pushing you comfortably above maintenance. You wake up relieved.

But reverse the scenario: overnight, a major company announces an accounting fraud, and equities gap down 100 basis points. Your 10 contracts lose $5,000 per contract (=$50,000 total). Your equity in those contracts is now $100,000 – $50,000 = $50,000, or $5,000 per contract—below the maintenance margin of $7,000. You are in a margin call. When the market opens, you cannot trade until you deposit another $20,000 ($2,000 per contract × 10) to restore maintenance, or the broker auto-liquidates your position.

Overnight margin requirements exist precisely to create a buffer for this scenario. If the overnight margin standard had been set at, say, 150% of maintenance (=$10,500 per contract), you would have needed $105,000 total to hold the position overnight. The overnight gap loss of $5,000 would have left you at $100,000 equity, still above the overnight minimum. You would not face a forced liquidation.

## Gap risk and liquidity

**Gap risk** is the core hazard overnight margin is designed to address. A gap is a price jump from one level to another with no trading in between. In stock futures or currency futures, overnight gaps are common. Between the US close and Asia open, or between Asia close and European open, substantial news breaks. If you are on the wrong side, you may face liquidation at an unfavorable price the next morning.

This risk compounds if the underlying contract becomes illiquid during the gap. Consider a [crude-oil](/crude-oil/) futures contract during heightened geopolitical tension. You close out your position at 4:00 PM. Overnight, a Middle East conflict escalates, and oil is bid hard at the Asian open. But volume is light—if you need to unwind 100 contracts, the bid-ask spread may be wide, and you'll take a worse fill than if you'd exited before the close. The overnight margin requirement is the broker's way of saying: "You are taking this gap risk; we need more collateral to remain on the hook for you."

## How overnight margin calls work

When markets close, your broker assesses your position against the overnight margin requirement. In most cases, this happens automatically after the regular close. If your equity is below the overnight standard, you receive notification—typically by email, phone, or trading platform alert.

The response timeline varies by broker and contract type, but typically you have until a specified time the next morning (often 8:00 AM or 9:00 AM) to deposit funds. Some brokers allow you to trade during pre-market hours to exit positions without meeting the overnight requirement first; others require the cash deposit before any trading resumes.

If you do not meet the requirement by the deadline, the broker liquidates your position at the market open, often at a disadvantageous fill because they are a forced seller (or buyer, if you were short). This automatic liquidation protects the broker from holding your credit risk overnight, but it locks in your loss and may trigger tax consequences ([wash-sale](/wash-sale/) rules) if you repurchase the same contract quickly.

## Variation margin and interest costs

Beyond the initial and overnight margin requirement, many brokers charge **interest on margin balances**—essentially a short-term loan. The rate varies by broker and collateral quality, but overnight margin balances are often charged at prime + 1–3%. Over months or years, this compounds. A trader carrying $50,000 in margin overnight at 5% annual interest incurs approximately $6.85 per trading day in financing costs. For active, leveraged traders, this is not trivial.

Additionally, [futures contracts](/futures-contract/) are marked-to-market daily. Variation margin—the daily P&L settlement—is transferred in or out of your account at the end of each trading session. If you are underwater, cash leaves your account immediately. This daily settlement is distinct from initial and overnight margin, but it further constrains liquidity for undercapitalized traders.

## Practical strategies for managing overnight margin

Experienced traders often reduce or exit positions ahead of the close to minimize overnight exposure. A day trader who can flatten out by 3:55 PM faces no overnight margin requirement and no gap risk. Swing traders and longer-term futures speculators, by contrast, must plan to hold positions overnight and budget for the extra margin cost.

Some traders use [protective-put](/protective-put/) or [stop-loss](/fx-stop-loss-order-mechanics/) orders to limit downside overnight, though gaps can blow through stops. Others diversify across contracts with lower correlation, reducing the chance that a single overnight shock wipes out multiple positions.

Institutional traders often use prime brokerage relationships, which offer lower margin rates and more negotiated overnight requirements in exchange for larger notional volumes. Retail traders lack this leverage and pay standard, higher rates.

## Brokers and margin flexibility

Different brokers set different overnight margin standards, and those standards vary by contract, volatility regime, and collateral type. A quiet, liquid contract like the S&P 500 E-mini may have tight overnight margins; an illiquid, thinly capitalized emerging-market currency future may demand much higher coverage. During stress periods—financial crises, circuit breakers, illiquidity spikes—brokers often raise overnight requirements across the board as a protective measure.

This tightening can be sudden and painful. Retail traders waking up to a 50% increase in overnight margin requirements have sometimes been force-liquidated before they even knew what happened. Reading your broker's terms carefully, understanding their margin policies, and maintaining a safety cushion above minimums are essential.

## See also

<div class="wiki-seealso">

### Closely related

- [Margin-call-forex](/margin-call-forex/) — how margin calls work in currency trading
- [Leverage-ratio-forex](/leverage-ratio-forex/) — the math of borrowed capital in leveraged trades
- [Futures-contract](/futures-contract/) — mechanics of futures clearing and settlement
- [Protective-put](/protective-put/) — hedging overnight risk with options
- [Stress-testing](/stress-testing/) — assessing portfolio resilience to overnight gaps

### Wider context

- [Counterparty-risk](/counterparty-risk/) — why brokers demand margin to cover default risk
- [Interest-rate](/interest-rate/) — how financing costs affect leverage profitability
- [Volatility-smile](/volatility-smile/) — how implied volatility shapes risk premiums
- [Value-at-risk](/value-at-risk/) — estimating potential losses over a holding period
- [Systematic-risk](/systemic-risk/) — how market-wide shocks force correlated liquidations

</div>
