---
title: "Market Maker Quoting Obligations"
description: "Regulatory requirements for designated market makers to maintain continuous two-sided quotes with minimum size and price standards."
keywords:
  - market maker quoting obligations
  - continuous quote requirements
  - market maker rules
  - two-sided quotes
  - designated market makers
image: /svg/regulation.svg
---

*Designated market makers on major U.S. exchanges are not passive participants—they must actively maintain a continuous presence by posting two-sided quotes (a bid and an ask) during trading hours. **Market maker quoting obligations** impose minimum size and price standards on these quotes, ensuring that investors can reliably find liquidity and that spreads remain tight. Failure to maintain the required quotes results in fines, trading restrictions, or loss of market maker status.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Market Maker Quoting — Key Facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A market maker must quote, continuously, or face sanctions.</div>

|   |   |
|---|---|
| **Who must quote** | Designated market makers (DMMs) on NYSE; market makers on Nasdaq |
| **Obligation start** | Market open (9:30 a.m. ET); continuous through close (4:00 p.m. ET) |
| **Minimum size** | Typically 100–1,000 shares depending on security price and volatility |
| **Price standard** | Bid-ask spread capped; quotes must be within NBBO or near-NBBO |
| **Exceptions** | No quoting during halts, extreme volatility, or order-processing delays |
| **Sanctions** | Fines, execution-quality demerits, loss of market maker appointment |
| **Monitoring** | Exchange surveillance and FINRA audit trails |

</aside>

## The Purpose of Quoting Obligations

Market makers serve as the liquidity providers of last resort. On any given security, if buyers and sellers do not naturally meet, a market maker steps in—buying when others are selling, selling when others are buying—to prevent the price from gapping or the stock from becoming untradeable.

Without a quoting obligation, a market maker could cherry-pick: actively trading in liquid, high-profit securities while ignoring less-active stocks. This would hollow out liquidity in secondary stocks, making them illiquid or expensive to trade. By mandating continuous quotes, exchanges ensure that even micro-cap or distressed securities maintain a minimum viable bid-ask spread and trading opportunity.

A two-sided quote (a simultaneous bid to buy and offer to sell) also signals confidence in fair value. If a market maker believes the stock is worth $50, it will quote $49.99 bid and $50.01 offer. Traders seeing this know they can buy or sell near fair value. If market makers were allowed to quote only one side or to withdraw quotes opportunistically, price discovery would suffer.

## Size Requirements

Quoting obligation rules specify a **minimum order size** that a market maker must be willing to execute at its quoted price.

On the **NYSE**, designated market makers typically must maintain a two-sided quote of:

- **At least 500–1,000 shares** for stocks trading below $100.
- **Scaled by price**: lower-priced stocks might require 1,000–2,000 shares; higher-priced stocks 100–500 shares.
- **Wider spreads for lower-volume securities**: a small-cap stock might allow 5–10 cent spreads, whereas a mega-cap requires penny spreads.

On **Nasdaq**, market makers must maintain quotes in all Nasdaq-listed securities they are assigned to, with typical minimums of:

- **1,000 shares** (or 1 contract for options) at the inside bid and offer.
- **Subject to a "quotation size" rule**: the size should reflect the stock's normal trading volume and volatility.

These minimums are not aspirational; they are enforceable. If a market maker quotes 100 shares at $50 when it is obligated to quote 1,000, the exchange can fine or suspend the market maker.

## Spread and Price Standards

Market makers must quote at or near the **National Best Bid and Offer (NBBO)**. The rules differ slightly by exchange:

**NYSE DMM obligations:**

- Quote the best bid and offer on the exchange, or within a narrow band of the NBBO.
- For highly liquid stocks (e.g., mega-caps), the spread is typically capped at one penny.
- For less liquid stocks, spreads may be wider, but still subject to "reasonable" constraints.
- Quote updates must reflect material changes in the market within seconds.

**Nasdaq market maker rules:**

- Maintain a quote within the best bid and offer (NBBO) or no more than ½ of a penny away.
- Size must be honored: quoted 1,000 shares at the price; executing more is a violation.
- Quotes must be firm (not subject to withdrawal) during trading hours.

## The Quoting Obligation and Trading Volatility

Market makers do not have an absolute duty to quote during extreme market dislocations:

- **Trading halts**: when the SEC halts trading in a security, quoting obligations are suspended.
- **Extraordinary volatility**: if a stock gaps 20% in one minute, a market maker may be relieved from its quoting duty temporarily while it reassesses fair value.
- **Regulatory events**: during SEC investigations, exchange-ordered position checks, or risk management freezes, quoting can be suspended.
- **System outages**: if the market maker's order-management system goes down, temporary relief may be granted.

However, these exceptions are narrow. Claiming "volatility" as a pretext to avoid quoting during a normal market correction does not fly.

## Enforcement and Penalties

Exchanges monitor quoting compliance through automated surveillance:

1. **Real-time tracking**: algorithms flag instances where a market maker fails to post a required quote.
2. **Spread monitoring**: if a quote is wider than permitted or stale (not updated), it is flagged.
3. **Fill tests**: if a customer could not execute at the market maker's quoted price because it was too small, that is recorded.

**Sanctions:**

- **Fine**: $500–$50,000+ per violation, depending on severity and frequency.
- **Trading restrictions**: suspension from quoting in the affected security or even market maker status.
- **Execution quality demerits**: exchanges publish market maker quality metrics; violations harm a firm's reputation.
- **Deregistration**: repeated violations can result in loss of market maker appointment.

Large market makers have been fined millions of dollars for systematic quoting violations. In 2018, Citadel Securities agreed to pay $272.5 million to the SEC and FINRA for violations including failure to maintain required quotes and reporting inaccurate quotes. In 2019, Virtu Financial paid $10.3 million for quoting failures on Nasdaq.

## The Business Model Behind Quoting

Market makers accept quoting obligations in exchange for **priority access** and **preferential pricing**:

- They can trade before other dealers, capturing early information.
- They can post their bids and offers first and adjust them as the market moves.
- They earn the [bid-ask spread](/bid-ask-spread/) on every trade, plus rebates from exchanges for providing liquidity.

On profitable, liquid securities, the spread and rebate income cover the costs of quoting. On less-liquid securities, quoting at a wider spread may still be profitable. But if a stock's volatility spikes or volume dries up, a market maker can face losses—which is why they lobby for exceptions to quoting rules during stress events.

## Relationship to [Clearly Erroneous Trade Cancellation](/clearly-erroneous-trade-cancellation/) and Other Rules

Market maker quotes feed into broader market integrity mechanisms:

- **NBBO calculation**: the best bid and offer across venues is derived from all market maker quotes; sloppy quoting undermines the NBBO.
- **Erroneous trade detection**: if a trade executes far outside the market maker's quotes, the exchange uses quote timestamps to determine whether it was a true error or a market maker's failure to update.
- **Reg SHO compliance**: market makers have certain exemptions from short-sale restrictions, but only if they are actively quoting; otherwise they lose the exemption.

## High-Frequency Quoting and the Paradox

In modern markets, most quoting is done by automated algorithms operated by high-frequency trading firms. These algorithms post and cancel millions of quotes per day, adjusting to market conditions in milliseconds. This is fully legal as long as the quotes meet size and spread minimums and are firm (not frivolous or meant to mislead).

However, this creates a paradox: quoting is supposed to signal confidence in fair value, but if a market maker posts a quote and cancels it 10 milliseconds later without trading, what does that quote actually mean? Regulators have grappled with this, resulting in rules on "quotation stuffing" (posting and canceling quotes to clog the market) and "layering" (posting fake quotes to create false impressions of liquidity).

## See also

<div class="wiki-seealso">

### Closely related

- [Bid-Ask Spread](/bid-ask-spread/) — the profit margin within which market makers operate
- [Clearly Erroneous Trade Cancellation](/clearly-erroneous-trade-cancellation/) — uses quote data to detect erroneous trades
- [Consolidated Audit Trail (CAT) Reporting](/consolidated-audit-trail-cat-reporting/) — CAT monitors continuous quoting compliance
- [Reg SHO Locate Requirement](/reg-sho-locate-requirement/) — market makers have locate exemptions conditioned on active quoting
- [Price Discovery](/price-discovery/) — quoting obligations support fair value formation

### Wider context

- Market Maker — the role and economics of market making
- [Stock Exchange](/stock-exchange/) — venues that enforce quoting rules
- National Best Bid and Offer (NBBO) — the standard that market maker quotes must meet
- Liquidity — the core benefit quoting obligations provide
- [High-Frequency Trading](/high-frequency-trading/) — modern market makers rely on algorithmic quoting

</div>
