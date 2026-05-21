---
title: "Forward Contract"
description: "A forward contract is a customizable bilateral agreement to exchange an asset for cash at a fixed price on a future date, settled at maturity (not daily)."
keywords:
  - forward contract
  - forward
  - otc derivative
  - bilateral
  - customizable
image: "/svg/derivatives.svg"
---

*A **forward contract** is a private agreement between two parties (typically facilitated by a bank) to buy or sell an underlying asset at a fixed price on a specified future date. Unlike standardized [futures contract](/futures-contract/)s, forwards are customizable (any quantity, date, asset). They are settled only at maturity (no daily [mark-to-market](/mark-to-market/)) and carry counterparty risk. Forwards are used extensively in currency and commodity markets by companies hedging operational exposure.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Forward Contract — key facts</div>

<img src="/svg/derivatives.svg" alt="Two-party bilateral agreement diagram" />

<div class="wiki-infobox-caption">Forwards are customizable OTC derivatives.</div>

|   |   |
|---|---|
| **Traded** | Over-the-counter (OTC), not exchange |
| **Customization** | Fully customizable (amount, date, terms) |
| **Standardization** | None; each contract is unique |
| **Settlement** | At maturity only (no daily mark) |
| **Margin** | None (may require collateral for credit risk) |
| **Liquidity** | Low; must hold to maturity or find counterparty |
| **Counterparty risk** | High; one party defaults at maturity |
| **Pricing** | Cost of carry: Forward price = Spot × e^(r×T) |
| **Typical use** | Currency hedging, commodity locks |
| **Regulation** | Minimal historically; increasing post-2008 |

</aside>

## How forwards work

You and a bank agree: "On June 30 (T), I will pay you $1.20 per EUR and receive €1 million in exchange." This is a forward contract.

The forward price ($1.20) is fixed today, based on the [spot price](/strike-price/) (current EUR/USD rate) and the [cost-of-carry](/cost-of-carry/) (interest rates). The contract obligates both parties; neither has the option to walk away.

At maturity, you settle. If EUR/USD has risen to $1.25, the bank gained $50,000 (you pay $1.20 but the bank could have sold at $1.25). If EUR/USD fell to $1.15, you gained $50,000 and the bank lost. **One party wins; the other loses.**

## Forwards vs. [futures](/futures-contract/)

| Aspect | Forward | Futures |
|--------|---------|---------|
| **Traded** | OTC | Exchange |
| **Customization** | Full | Standardized |
| **Settlement** | At maturity | Daily |
| **Margin** | None typically | Required |
| **Counterparty risk** | High | Low |
| **Liquidity** | Low | High |

Futures are the exchange-traded standardized version of forwards. Forwards are the bespoke bilateral version.

## Pricing: cost-of-carry

The forward price is:

Forward Price = Spot Price × e^(r×T)

For a currency forward with spot EUR/USD = 1.10, US rate = 2%, euro rate = 3%, and T = 1 year:

Forward = 1.10 × e^((0.02-0.03)×1) = 1.10 × e^(−0.01) ≈ 1.089

The forward adjusts for interest-rate differentials, storing the [cost-of-carry](/cost-of-carry/) between the two currencies.

For commodities, [cost-of-carry](/cost-of-carry/) includes storage, insurance, and convenience yield.

## Uses and examples

**Currency hedges:** An exporter earning €1M in 6 months locks in the exchange rate using a 6-month EUR/USD forward, eliminating currency risk.

**Commodity locks:** A utility fixes the price of heating oil for winter, avoiding price spikes.

**Interest-rate forwards:** A borrower locks in a future borrowing rate using a forward-rate agreement (FRA).

## Counterparty risk

The major risk in forwards is **counterparty risk**: if the market moves far against the counterparty, they may default rather than settle. After the 2008 crisis, standardized contracts and clearing houses were mandated for many derivatives to reduce this risk.

## No mark-to-market

Unlike [futures](/futures-contract/), forwards do not settle daily. Profits and losses are deferred to maturity. This can be good (no forced margin calls) or bad (uncertainty accumulates).

An exporter with a short forward (locked in a sale price) does not receive daily payments if the currency rises; they wait until maturity and settle.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — standardized, exchange-traded version
- [Swap](/swap/) — series of forwards at different dates
- [Cost of carry](/cost-of-carry/) — drives forward pricing
- [Basis](/basis/) — spot vs. forward price
- [Counterparty risk](/bond/) — default risk

### Applications

- [Hedging](/hedge-fund/) — locking in future prices
- Commodity forward — locks commodity prices
- [Currency forward](/currency-option/) — locks exchange rates
- [Interest-rate forward](/interest-rate-swap/) — locks borrowing rates

### Pricing and valuation

- [Mark-to-market](/mark-to-market/) — not done daily for forwards
- [Spot price](/strike-price/) — starting point for pricing
- [Interest rates](/interest-rate/) — affect forward price
- [Discount factor](/compound-interest/) — in forward valuation

### Deeper context

- [Derivative](/option/) — the family of instruments
- [OTC market](/stock-exchange/) — where forwards trade
- [Risk management](/hedge-fund/) — forwards in hedging

</div>
