---
title: "Mark-to-Market"
description: "Mark-to-market is the daily revaluation of futures and other derivatives to current market prices, settling gains and losses immediately rather than deferring to maturity."
keywords:
  - mark-to-market
  - mtm
  - daily settlement
  - derivatives accounting
  - futures settlement
image: "/svg/derivatives.svg"
---

*The **mark-to-market (MTM)** process revalues [futures contract](/futures-contract)s and other derivatives to current market prices at the end of each trading day. Gains and losses are calculated and immediately credited or debited to the trader's account. This daily settlement—unique to futures and some exchange-traded options—differs from [forward contract](/forward-contract)s, which settle only at [expiration date](/expiration-date). Mark-to-market reduces counterparty risk and forces traders to post [margin](/initial-margin) to maintain positions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Mark-to-Market — key facts</div>

<img src="/svg/derivatives.svg" alt="Daily settlement of gains and losses" />

<div class="wiki-infobox-caption">MTM settles positions daily at market prices.</div>

|   |   |
|---|---|
| **Timing** | End of each trading day |
| **Reference price** | Settlement price set by exchange |
| **Settlement** | Gain/loss deposited/withdrawn immediately |
| **Account impact** | Daily update to equity |
| **Margin calls** | If equity falls below maintenance |
| **Accounting** | Reported as realized gains/losses (not deferred) |
| **Advantage** | Reduces counterparty risk |
| **Disadvantage** | Forces daily cash movements |
| **Applies to** | Futures, exchange-traded options |
| **Does not apply** | Forward contracts, OTC swaps (typically) |

</aside>

## Daily settlement mechanism

At the end of each trading day, the exchange sets a **settlement price**—the official close or a volume-weighted average.

For a trader long a December crude oil contract:
- Bought at $70/barrel, December contract
- Today's settlement price: $71/barrel
- Gain: +$1/barrel × contract size = $1,000 (for a 1,000-barrel contract)
- This $1,000 is credited to the trader's account immediately

Next day, if the settlement price falls to $69:
- Loss: −$2/barrel × 1,000 = −$2,000
- The $2,000 is debited from the account

The trader's account balance moves daily with the contract's value.

## Margin and forced liquidation

If daily losses drain the account below [maintenance margin](/maintenance-margin), the trader faces a **margin call**: deposit more funds or close the position. This forces risk management and prevents traders from accumulating unlimited losses.

A trader with $5,000 [initial margin](/initial-margin) might have $3,500 [maintenance margin](/maintenance-margin). If losses reach $1,500, the trader is below maintenance and must deposit cash or sell the contract.

## Accounting implications

In regular investing, you do not realize a gain until you sell. A stock bought at $100 and now at $110 has an unrealized $10 gain.

In futures, MTM forces **realization**. The daily gain is treated as realized income for tax and accounting purposes, even if the position remains open. This creates tax complications for some strategies.

## Counterparty risk reduction

The fundamental purpose of MTM is to reduce counterparty risk. With [forward contract](/forward-contract)s, losses accumulate over time and are settled at maturity. If the counterparty defaults before maturity, you lose everything.

With futures and MTM, losses are settled daily. If the counterparty defaults tomorrow, you lose only today's loss, not weeks or months of accumulated exposure.

## Comparison with forwards

| Aspect | Futures (MTM) | Forwards (No MTM) |
|--------|---------------|-------------------|
| **Settlement** | Daily | At maturity |
| **Counterparty risk** | Low; settled daily | High; deferred |
| **Margin** | Required | Rare |
| **Liquidity** | High; exit anytime | Low; hold to maturity |
| **Accounting** | Realized daily | Deferred |

## OTC swaps and MTM

[Swap](/swap) contracts traded OTC typically do **not** have daily MTM. They settle at maturity (for fixed-term swaps) or on termination. Some swap dealers offer MTM settlements for special arrangements.

The lack of daily settlement is why [swap](/swap) credit risk is higher than futures.

## See also

<div class="wiki-seealso">

### Closely related

- [Futures contract](/futures-contract/) — uses MTM settlement
- [Margin](/initial-margin/) — MTM enables margin requirements
- [Maintenance margin](/maintenance-margin/) — enforced via MTM
- [Settlement price](/mark-to-market/) — daily reference level
- [Forward contract](/forward-contract/) — no MTM; deferred settlement

### Risk management

- [Counterparty risk](/bond/) — reduced by MTM
- [Liquidity risk](/stock-market/) — MTM enables exits
- Margin calls — triggered by MTM losses
- [Forced liquidation](/stock-market) — result of margin call

### Accounting

- Realized vs. unrealized — MTM realizes gains
- Tax implications — daily realization affects taxes
- Reporting — MTM shown daily

### Deeper context

- [Derivative](/option/) — the family of instruments
- [Clearing house](/stock-exchange/) — enforces MTM
- [Exchange-traded](/stock-exchange/) — standardized MTM

</div>
