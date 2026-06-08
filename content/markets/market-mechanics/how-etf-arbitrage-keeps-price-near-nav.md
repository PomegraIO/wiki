---
title: "How ETF Arbitrage Keeps Price Near NAV"
description: "Authorized participants use creation and redemption to exploit ETF price premiums and discounts, keeping market prices aligned with net asset value."
keywords:
  - how etf arbitrage keeps price near nav
  - etf premium discount
  - authorized participant
  - etf creation redemption mechanism
  - nat asset value etf
image: "/svg/markets.svg"
---

***ETF arbitrage** is the mechanism that keeps an exchange-traded fund's market price close to its underlying net asset value. When an ETF's share price drifts above or below the value of its holdings, [authorized participants](/authorized-participant/)—large financial institutions—exploit the gap by creating or redeeming shares, capturing the spread and simultaneously pushing price back toward fair value.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ETF Arbitrage — Key facts</div>

<img src="/svg/markets.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Creation and redemption keep quoted prices aligned with holdings.</div>

|   |   |
|---|---|
| **Core mechanism** | Authorized participants buy/sell basket and create/redeem shares to capture price gaps |
| **Who profits** | Market makers and large institutional traders |
| **Who benefits** | All ETF holders (via price efficiency) |
| **Typical discount/premium** | Under 0.5% for liquid ETFs; wider for illiquid or stressed markets |
| **Speed** | Executes in seconds to minutes when profitable |

</aside>

## The Creation-Redemption Plumbing

An ETF is not simply a mutual fund that trades on an exchange. It has two markets operating in parallel: the secondary market (where you and I trade shares on the stock exchange) and the primary market (where authorized participants can create and redeem shares directly with the fund issuer).

Imagine an [ETF](/etf/) tracking the S&P 500. The fund holds 500 stocks in proportion to their index weight. The **net asset value (NAV)** is calculated once per day at market close, reflecting the closing prices of all holdings. But the ETF's share price is quoted throughout the trading day on the stock exchange, moving second by second as supply and demand shift.

When the secondary market price rises above the NAV, an authorized participant sees profit. They assemble a basket of the 500 stocks exactly matching the fund's composition, deliver it to the fund sponsor, and receive a large block of new ETF shares. The participant then sells those shares on the stock exchange at the higher quoted price. Profit = the spread between NAV and the price they sold at. The creation of new shares increases supply, which pushes price down; equilibrium is restored.

Conversely, when the secondary market price falls below NAV, the reverse arbitrage triggers. The participant buys shares on the stock exchange at the depressed price and redeems them directly with the fund in exchange for the underlying basket of securities. They sell the securities at their current market value, which exceeds what they paid for the ETF shares. Again, supply and demand self-correct—redemption removes shares from circulation, tightening supply and lifting price back up.

## Why This Matters for the Price

The existence of this arbitrage mechanism is why ETFs rarely trade far from NAV. Unlike a closed-end fund, which can trade at a large discount or premium because there is no mechanism to create or redeem shares, an ETF's price is tethered to reality.

For highly liquid ETFs—those with large trading volumes and tight [bid-ask spreads](/bid-ask-spread/)—the secondary market price typically stays within 0.1% of NAV. During normal market conditions, [arbitrage](/algorithmic-trading/) is so efficient that the profit window closes almost instantly.

For less liquid ETFs, or during market stress, the discount or premium can widen. A bond ETF trading when credit markets are frozen, or a small-cap regional fund during a sector selloff, might drift 0.5% to 1% away from NAV before the arbitrage becomes attractive enough to execute. But even then, the mechanism exists and will eventually pull price back in line.

## The Role of Authorized Participants

Only certain large financial institutions—authorized participants—have the legal right and operational capability to create and redeem shares. These are typically investment banks, broker-dealers, and other market makers with the scale to:

- Assemble or disassemble securities baskets matching the fund's exact holdings
- Execute large block trades efficiently
- Absorb the operational costs of creation/redemption
- Take on temporary inventory risk

Retail investors cannot create or redeem directly with the fund. We buy and sell on the stock exchange, which is where authorized participants compete for our business and where arbitrage keeps prices honest.

## Costs That Limit Arbitrage

The arbitrage is not free. Creating or redeeming a large ETF share block incurs:

- **Bid-ask spreads** on the component securities
- **Commissions** (often waived for authorized participants, but implicit in spreads)
- **Timing risk** (markets move between execution legs)
- **Opportunity cost** of capital and inventory

When these costs are large, the arbitrage window widens. A large, illiquid underlying basket—say, an emerging-market equity ETF holding 800+ stocks with thin trading—might only trigger arbitrage when the premium or discount exceeds 0.5%. Smaller or more exotic funds may see wider windows.

This is why [active ETFs](/active-etf/) with non-transparent holdings, or funds tracking hard-to-assemble baskets, can drift further from NAV than a [passive index fund](/index-fund/) tracking the S&P 500.

## Secondary Market Price vs NAV

A common misconception is that an ETF's price and its NAV are the same. They are not—they update at different times.

NAV is calculated once per trading day after market close, using the closing prices of all underlying securities. It is what you see published the next morning. The secondary market price, by contrast, is live throughout the trading day, moving with every share trade.

If you buy or sell an ETF during the trading day, you get the market price—which may be higher or lower than the previous day's NAV. Authorized participants ensure that the trading-day price stays close to the intraday value of the basket (or the expected value of the next day's NAV), not the stale published NAV from yesterday.

## When Arbitrage Breaks Down

Arbitrage can fail during genuine market dislocations. If one of the underlying securities becomes illiquid or halts trading—or if credit markets freeze and [counterparty risk](/counterparty-risk/) spikes—authorized participants may pull back. In March 2020, for example, some bond ETFs suffered wider-than-normal discounts because assembling the underlying baskets became difficult and costly. Once markets stabilized and creation resumed, prices snapped back.

This is a feature, not a bug. The arbitrage mechanism reveals when underlying markets are stressed; the widening discount is honest pricing.

## See also

<div class="wiki-seealso">

### Closely related

- [Authorized Participant](/authorized-participant/) — the market maker that executes creation and redemption
- [ETF](/etf/) — structure and mechanics of exchange-traded funds
- [Net Asset Value](/net-asset-value/) — the calculation and use of fund NAV
- [Bid-Ask Spread](/bid-ask-spread/) — the cost of trading and its effect on arbitrage windows
- [Index Fund](/index-fund/) — passive tracking and why ETFs keep tight margins
- [Closed-End Fund](/closed-end-fund/) — contrast: no creation/redemption, wider premiums/discounts

### Wider context

- [Market Maker Trading](/market-maker-trading/) — how dealers profit and improve liquidity
- [Price Discovery](/price-discovery/) — how markets converge on fair value
- [Algorithmic Trading](/algorithmic-trading/) — the technology behind arbitrage execution
- [ETF Premium Discount](/etf-premium-discount/) — detailed treatment of when and why gaps occur

</div>
