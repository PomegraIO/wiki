---
title: "Deal Market"
description: "Market where bilateral transactions are negotiated directly between parties rather than executed through exchanges or auctions."
keywords:
  - bilateral negotiation
  - over-the-counter dealing
  - principal trading
  - market microstructure
---

*A **deal market** is a forum where buyers and sellers negotiate transactions directly with each other, settling terms bilaterally rather than through a standardized exchange or auction mechanism. Price, timing, and counterparty risk are all contractual variables between the two parties.*

<aside class="wiki-infobox">

| Characteristic | Detail |
|---|---|
| **Price setting** | Bilateral negotiation, no central limit order book |
| **Counterparty** | Direct exposure; often mitigated by clearing or collateral |
| **Speed** | Minutes to hours (human-driven) |
| **Transparency** | Limited; no continuous real-time publically posted quotes |
| **Typical asset** | Bonds, FX forwards, [interest-rate swaps](/wiki/interest-rate-swap/), large equity blocks |
| **Participants** | Banks, institutional investors, corporations |

</aside>

## Why negotiated transactions persist despite electronic exchanges

Deal markets exist precisely because many financial contracts resist standardization. A [foreign exchange forward](/wiki/fx-forward/) tailored to a corporation's exact cash flow date, or a [credit derivative](/wiki/credit-derivative/) referencing a specific loan, cannot be executed against a [centralized exchange](/wiki/centralized-exchange/). Bilateral dealing lets parties customize strike dates, notional amounts, credit terms, and settlement procedures. The cost is opacity and longer execution; the benefit is flexibility.

Banks and hedge funds maintain dealing desks for this reason. A dealer quotes a [bid-ask spread](/wiki/bid-ask-spread/) to a client, absorbs [counterparty risk](/wiki/counterparty-risk/), and either warehouses the position or lays it off with another dealer downstream. This chain of bilateral relationships is the backbone of the global [fixed-income](/wiki/bond/) and [derivatives](/wiki/derivatives-exchange-crypto/) markets.

## Price discovery in deal markets vs. lit venues

An exchange publishes an [order book](/wiki/order-book-depth/) and a last-trade print every second. A deal market has neither. Instead, price discovery happens through inquiry — a buyer phones a dealer asking "where is X?" The dealer quotes a two-way price (bid and offer), and the buyer either deals or calls another dealer. This process is slower and requires market participants to know whom to call, but it produces a fair price because information spreads through the dealer network.

In [credit derivatives](/wiki/credit-default-swap/), the most liquid instruments may trade 5–10 times per day; less liquid names may trade weekly. The absence of a public order book does not mean the price is arbitrary; it means liquidity is conditional on knowing a counterparty willing to deal.

## Settlement and counterparty considerations

Bilateral transactions settle between the two principals, often using a [clearinghouse](/wiki/central-counterparty-clearing/) as an intermediary. [DTCC](/wiki/dtcc/) clears most [bond](/wiki/corporate-bond/) trades; [LCH](/wiki/lch-clearnet/) clears [interest-rate swaps](/wiki/interest-rate-swap/). Clearing insulates each party from the other's credit risk; without it, a deal market participant faces direct [default risk](/wiki/counterparty-credit-risk/).

For instruments that do not clear (bespoke [currency options](/wiki/currency-option/) or [commodity swaps](/wiki/commodity-swap/)), counterparty risk is managed via [collateral](/wiki/credit-support/) agreements, netting clauses, and [haircuts](/wiki/haircut-agreement/). These negotiations add friction to bilateral dealing.

## Deal markets vs. electronic platforms

A [crossing network](/wiki/crossing-network/) and a [single-dealer platform](/wiki/single-dealer-platform/) are hybrids that blend deal-market features (negotiation, flexibility) with electronic speed. But pure deal markets remain human-centric. Dealers still use phones and Bloomberg terminals because the relationship matters; a client knows her dealer's credit quality, and the dealer has decades of relationship capital at stake.

This is why [alternative trading systems](/wiki/alternative-trading-system/) have not entirely replaced dealer networks. Dealer inventory (willingness to buy) and dealer relationships (trust, credit quality, knowledge of client flows) cannot yet be fully automated.

<div class="wiki-seealso">

### Closely related
- [Over-the-counter market](/wiki/over-the-counter-market/) — The broader umbrella for off-exchange bilateral transactions
- [Centralized exchange](/wiki/centralized-exchange/) — The alternative: standardized, limit-order-book driven
- [Principal trading](/wiki/principal-trading/) — Dealer takes the other side
- [Block trade mechanics](/wiki/block-trade-mechanics/) — Large bilateral equity trades

### Wider context
- [Market microstructure](/wiki/price-discovery/) — How prices form across venues
- [Counterparty credit risk](/wiki/counterparty-credit-risk/) — The risk of dealing bilaterally
- [Interest-rate swap](/wiki/interest-rate-swap/) — A canonical deal-market instrument
- [Credit default swap](/wiki/credit-default-swap/) — Another core bilateral derivative

</div>
