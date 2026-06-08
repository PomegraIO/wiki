---
title: "Short Sale Locate Requirements and Execution Delay"
description: "Brokers must locate and reserve borrowable shares before executing a short sale, or the order is rejected or delayed, creating execution risk and friction."
keywords:
  - short sale locate requirement
  - short sale execution delay
  - borrow shares short selling
  - hard to borrow stocks
  - short sale settlement risk
image: /svg/trading.svg
---

*A **short sale locate requirement** means your broker must identify and reserve available shares to borrow before your sale order executes. If no shares are available or the locate fails, the order gets rejected, cancelled, or delayed—sometimes minutes, sometimes days. This regulatory guardrail, called Regulation SHO, prevents "naked" short selling and creates execution risk that doesn't exist on the buy side.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Locate Requirements — key facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for trading." />

<div class="wiki-infobox-caption">Borrowing shares for short sales creates friction that buys don't face.</div>

|   |   |
|---|---|
| **What triggers a locate** | Any short sale order; rule applies to all stocks on US exchanges |
| **Who must locate** | The broker or its lending agent; settles shares by T+2 |
| **Locate window** | Must be in place at market open or by order entry, depending on broker |
| **Failure outcome** | Order rejected, delayed, or converted to a buy-in |
| **Hard-to-borrow stocks** | Highly shorted or low-float names; locates may be impossible |
| **Cost implication** | Borrow fees (0.5%–20%+ annually) passed to the short seller |

</aside>

## What "locate" means in practice

When you place a short sale order, your broker's back office or a lending agent must confirm that shares exist in a lending pool—typically shares held by other institutional clients, pension funds, or the broker's own inventory. The locate is a reservation: "We have identified 10,000 shares of XYZ available for borrow, and we are committing to lend them to you on settlement (T+2 or T+3, depending on your market)."

Without a locate, the order cannot legally execute under Regulation SHO. The broker must have the locate in place before the order hits the exchange—or at latest by the time the order opens the next trading day (for end-of-day orders in some jurisdictions).

## Execution delays and rejections

When shares are unavailable for borrow, the order either:
- **Is rejected immediately** — The broker cancels the order and notifies you the locate failed. You have no position.
- **Sits in a pending state** — The order rests while the broker searches for shares, hoping to locate them before market open or within a few hours.
- **Is executed as a "buy-in"** — In rare cases, the broker executes the order anyway and then attempts to locate shares after the sale, accepting the risk of a forced buy-in if shares cannot be secured by T+3.

The second scenario is the source of execution delays. Highly shorted stocks, SPACs shortly after merger announcements, or micro-cap stocks with few shares outstanding often have shallow lending pools. Locates may take hours or may never happen.

For day traders, a failed locate on a short sale can wipe out the intended trade entirely. For swing traders holding positions across multiple days, a delayed locate means you miss the entry price or miss the trade window entirely.

## Why regulation mandates the locate

Before Regulation SHO (adopted in 2005), brokers and traders could execute short sales without actually borrowing shares, a practice called "naked shorting." The seller would simply agree to deliver shares at settlement (T+2), betting that shares would be available by then. If they were not available, the trade would fail to settle, creating a "fail-to-deliver" that could pile up over weeks—artificially suppressing the stock price and frustrating legitimate shareholders.

The locate requirement forces brokers to confirm upfront that shares exist and are obtainable. It reduces fails-to-deliver and prevents the worst abuses of naked shorting. The downside is friction: it adds operational complexity and creates execution risk that buy-side orders do not have.

## Hard-to-borrow stocks

Stocks with a small float or high existing short interest often lack available borrow. Examples include:
- **Low-float stocks** — Heavily held by founders or insiders; few shares trade freely
- **Highly shorted names** — So many traders are short that lending pools are depleted
- **Biotech or micro-caps** — Limited institutional holders, so sparse lending inventory
- **Recently halted stocks** — Lending may pause until trading resumes

Brokers signal hard-to-borrow status by charging borrow fees—sometimes 0.5% annually on a mega-cap, but 5%, 10%, or even 20%+ annually on a micro-cap or heavily shorted stock. At extreme borrow fees, short selling is economically pointless for anything but a conviction multi-month thesis. A fee of 20% annually—even if the stock falls 30%—wipes out most of your gain.

## The locate vs. the borrow

Locate and borrow are related but distinct. A locate is the broker's confirmation that shares exist and are available. A borrow is the actual loan—initiated at trade execution and settled at T+2. You do not pay borrow fees until the borrow is activated; the locate is free (from the broker's perspective; they absorb the cost as a service).

If a locate fails, no borrow happens, and you have no position. If a locate succeeds but the actual borrow is unavailable at settlement, a "buy-in" may be forced—the broker buys shares in the market to settle your short, charging you the difference if the price has moved against you.

## Execution timing and order types

Different order types interact with locate rules:
- **Market orders** — Must have a locate by the time the order executes; rejected if unavailable
- **Limit orders** — Can rest overnight pending a locate; may execute the next day if shares become available
- **Short-exempt orders** — Used by market makers and certain institutions; subject to different locate timing
- **After-hours orders** — Locate windows are typically tied to market open, so orders placed after-hours may execute the next day once a locate is confirmed

If you place an end-of-day short sale order, your broker typically has until market open the next day to locate shares. If they cannot, the order cancels or you receive a notification that you must resubmit.

## Strategic implications

For traders, the locate requirement is a hidden cost of short selling. In fast-moving markets or on hard-to-borrow stocks, you may not be able to execute at the price you want—or at all. This asymmetry between long and short orders is structural; there is no equivalent friction on the buy side.

Institutional traders managing large short positions often pre-arrange borrow commitments with their prime broker or lending agents, guaranteeing locate availability for key positions. Retail traders relying on a single broker may face delays or rejections on volatile stocks.

The locate requirement also supports [bid-ask spreads](/bid-ask-spread/) by making short sales operationally expensive on hard-to-borrow names, which can widen spreads and reduce liquidity.

## See also

<div class="wiki-seealso">

### Closely related

- [Short selling](/short-selling/) — The mechanics of borrowing and selling shares you do not own
- [Borrow shares short selling](/short-selling/) — How lenders profit from share loans
- [Execution risk](/execution-risk/) — Broader category of risks that orders may not fill as intended
- [Bid-ask spread](/bid-ask-spread/) — How execution friction is reflected in pricing
- [Market maker (trading)](/market-maker-trading/) — Entities that provide liquidity and hedge using borrows

### Wider context

- [Securities and Exchange Commission](/securities-and-exchange-commission/) — The regulator behind Regulation SHO
- Settlement clearing — Why T+2 settlement creates time for locates to be executed
- [Counterparty risk](/counterparty-risk/) — The risk that a borrow counterparty defaults before settlement
- [Regulatory risk](/market-risk/) — How regulatory changes reshape trading behavior

</div>
