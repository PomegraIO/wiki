---
title: "Forward Contract vs Futures Contract"
description: "Forward and futures contracts both lock in future prices, but futures are standardized and marked-to-market daily, while forwards are bespoke and settled only at expiry."
keywords:
  - forward contract vs futures contract differences
  - forwards vs futures
  - futures contracts standardized
  - counterparty risk forwards
image: /svg/derivatives.svg
---

*Both **forward contracts** and **futures contracts** bind you to buy or sell an asset at a fixed price on a future date. Yet they differ fundamentally in structure, risk, and use. Forwards are bespoke agreements between two parties; futures are standardized, exchange-traded instruments with daily settlement and guarantee. The choice between them shapes how much [counterparty risk](/counterparty-risk/) you carry and how much cash you deploy.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forward vs Futures — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Futures are the exchange-traded, standardized, liquid version; forwards are the OTC, customized, illiquid version.</div>

|   |   |
|---|---|
| **Standardization** | Forwards are bespoke; futures are standardized contracts |
| **Exchange-traded** | Forwards trade over-the-counter (OTC); futures on exchanges |
| **Settlement** | Forwards settle only at maturity; futures marked-to-market daily |
| **Counterparty risk** | Forwards: high (you're exposed to the other party's credit); futures: minimal (clearing house guarantees) |
| **Liquidity** | Futures are highly liquid; forwards often illiquid until close to maturity |
| **Margin** | Futures require daily margin; forwards typically no margin until delivery |
| **Typical users** | Forwards: corporates hedging bespoke needs; futures: speculators, financial traders, commodity funds |

</aside>

## Standardization and customization

A futures contract on crude oil is identical across all buyers and sellers on the exchange. Every contract specifies exactly 1,000 barrels, delivery in a specific month, a specific grade of oil, and settlement mechanics. You cannot customize the size, quality, or settlement location—standardization is the point.

A forward contract is a private negotiation. An airline needing 50,000 barrels of jet fuel with delivery at a specific airport on a specific date can negotiate a [forward contract](/forward-contract/) with a bank or trader tailored to those exact requirements. The contract is one-of-a-kind.

For the airline, the forward is ideal—it matches its actual hedging need. For a financial speculator, the future is better—it's standardized and easy to buy or sell.

## Mark-to-market settlement versus cash settlement at maturity

This is the critical operational difference.

**Futures are marked to market daily.** At the close of each trading day, your profit or loss is calculated at that day's closing price. The difference is either credited to or debited from your account immediately. If you buy a crude futures contract at $80/barrel and it closes at $81, you're credited $1,000 profit (1,000 barrels × $1). If it falls to $79, you're debited $1,000. This happens every single day until expiry.

**Forwards settle only at maturity.** You and the counterparty agree on a price today—say, $80/barrel—and nothing happens to the contract's value until the delivery date. On delivery day, you pay the agreed $80 per barrel, and the counterparty delivers oil at that price. All gain or loss is realized in one lump sum at maturity.

This difference cascades into capital management and cash flow. A futures trader must maintain a margin account and post or withdraw cash daily. A forward contract holder can ignore mark-to-market volatility and simply show up with cash at maturity.

For a corporate hedger, forwards are simpler—no daily margin calls, no surprise cash drains. For a trader, futures are more transparent—you see your real-time P&L.

## Counterparty risk

A forward contract is only as safe as the counterparty's credit. If you buy oil forward from a bank at $80/barrel and the bank defaults before delivery, you lose not only your profit but your entire hedge. You're exposed to the bank's solvency, and there is no guarantee.

Futures eliminate this risk. The exchange operates a **clearinghouse** that steps between every trade. When you buy a futures contract, the exchange (or its clearing member) becomes the counterparty, guaranteeing performance. The clearinghouse requires daily margin and automatically manages risk. Even if your broker fails, the clearinghouse protects your position.

For large, long-dated hedges—a major airline locking in fuel prices for five years—forwards are common but risky. The bank might be creditworthy today but fail in year three. Futures contracts rarely extend beyond a year or two, so duration risk is lower.

## Liquidity and flexibility

Futures are highly liquid. At any moment, you can sell your long contract to someone else, close the position, or roll it to a farther expiry. The standardization and exchange listing mean millions of dollars of contracts trade each day.

Forwards are illiquid. Once you enter a customized forward, selling it to a third party is difficult or impossible. If you need to exit early, you must negotiate with the original counterparty, who may demand a steep price to unwind the deal.

This illiquidity is a cost for hedgers who anticipate needing to close before maturity. It's also why forwards are less attractive for speculators who may want to cut a loss or lock in profits before the contract matures.

## Margin requirements

Futures require **initial margin** upfront—typically 5–10% of the contract's notional value. You also maintain margin daily; losses trigger margin calls. This is a burden on working capital but ensures both parties stay committed and solvent.

Forwards rarely require margin. You don't deposit money to enter; you simply sign the agreement. No money changes hands until delivery. For a hedger with a long-term view, this is an advantage—no surprise cash drains. For a speculator or a counterparty concerned about the other side's default, it's a risk.

## Which instrument for whom?

**Corporates hedging operational needs**: Forwards are often superior. An airline knows it will burn a fixed amount of jet fuel each quarter for the next two years. A customized forward with an energy company or bank perfectly matches that need. The counterparty risk is manageable if the bank is creditworthy, and there's no daily margin burden.

**Commodity exporters**: Oil-producing nations and agricultural exporters often use forwards to lock in export prices, negotiated directly with trading firms or investment banks. Standardized futures would work, but the large sizes and specific delivery locations favor forwards.

**Traders and hedge funds**: Futures are the choice. They trade on standardized contracts, roll positions frequently, and exploit [contango](/contango/) and [backwardation](/backwardation/) spreads. Daily mark-to-market is transparent and, frankly, forces discipline. A trader who is losing money sees it immediately.

**Passive commodity funds**: These rely on futures because of liquidity. A fund tracking oil prices needs to roll thousands of contracts monthly; forwards cannot scale that way.

## The economics: spreads and costs

Forwards trade with an implicit cost embedded in the price. A bank quoting a forward will quote bid and ask prices with a wider spread than a futures exchange would. The spread compensates the bank for its counterparty risk, bespoke hedging effort, and illiquidity.

Futures have tight bid-ask spreads due to competition and standardization. Commissions are explicit and typically lower per unit.

For a large, one-time hedge, the forward's cost may be acceptable. For frequent rolling or large-volume trading, futures' lower friction wins.

## Expiry and delivery mechanics

Futures have standardized expiry dates (typically quarterly) and standardized delivery procedures. If you hold a contract to expiry, the exchange specifies the location and grade of physical delivery (or cash settlement for index futures).

Forwards have bespoke expiry and delivery locations. An airline forward for jet fuel might specify delivery at Los Angeles International Airport on a particular day. The forward can specify almost any logistics.

In practice, most futures contracts are closed before expiry; few go to delivery. Most forwards go to delivery because they're designed for a specific operational need.

## See also

<div class="wiki-seealso">

### Closely related

- [Forward Contract](/forward-contract/) — the bespoke OTC instrument
- [Futures Contract](/futures-contract/) — the standardized exchange-traded instrument
- [Contango](/contango/) — curve structure that favors futures trading
- [Backwardation](/backwardation/) — the inverted curve structure
- [Counterparty Risk](/counterparty-risk/) — why forwards carry credit risk
- [Calendar Spread Futures Explained](/calendar-spread-futures-explained/) — a strategy possible only with futures liquidity

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — when to use forwards versus futures
- [Futures Margin Call Mechanics](/futures-margin-call-mechanics/) — capital requirements of futures
- [Contango Cost for Long Futures Holders](/contango-cost-for-long-futures-holder/) — the friction of rolling futures
- [Over-the-Counter Market](/over-the-counter-market/) — where forwards trade
- [Broker](/broker/) — the intermediary for both instruments
- [Clearinghouse](/securities-and-exchange-commission/) — the guarantor of futures

</div>
