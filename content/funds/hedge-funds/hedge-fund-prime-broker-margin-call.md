---
title: "Prime Broker Margin Calls and Forced Liquidation in Hedge Funds"
description: "How prime broker margin calls trigger forced liquidation in hedge funds, cascade effects, and systemic contagion explained."
keywords:
  - hedge fund margin call
  - prime broker margin call forced liquidation
  - hedge fund leverage management
  - forced selling cascade
  - prime broker counterparty risk
image: /svg/funds.svg
---

*A **prime broker margin call** is both a routine protective mechanism and a potential trigger for financial catastrophe. When a hedge fund's collateralized positions lose value, the prime broker demands additional cash to cover losses. If the fund can't pay, the broker seizes and liquidates positions—often at the worst possible time and prices. Understanding the chain of events is critical for any investor in hedge fund strategies.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Prime Broker Margin Calls — Key Facts</div>

<img src="/svg/funds.svg" alt="An abstract editorial mark for funds." />

<div class="wiki-infobox-caption">Daily repricing and leverage create acute solvency crises in leveraged funds.</div>

|   |   |
|---|---|
| **Typical Fund Leverage** | 2:1 to 5:1; some funds run 10:1+ |
| **Haircut on Collateral** | 2–10% depending on asset liquidity and volatility |
| **Margin Call Trigger** | Position loss of 5–10%; can be daily repricing |
| **Response Time** | 24–48 hours typically; urgent calls can be hours |
| **Forced Sale Slippage** | 2–15% below market price; worse in stressed conditions |
| **Prime Broker Costs** | 10–50 basis points on borrowed funds |
| **Multi-Prime Broker Spread** | Allows some flexibility; single-broker funds are at risk |
| **Cascade Effect** | One fund's forced selling triggers peer margin calls |
| **Historical Example** | LTCM, 1998; Archegos, 2021; various quant blowups |
| **Systemic Amplifier** | Margin call cascades can freeze credit markets |

</aside>

## How Prime Brokers Work

A prime broker is a bank or investment firm that provides leverage and clearing services to hedge funds. The fund deposits capital with the prime broker; the broker then lends additional cash or securities, allowing the fund to amplify positions. In exchange, the prime broker charges fees, earns spreads, and holds collateral.

A fund with $100 million in capital might borrow $200–300 million from the prime broker, creating $300–400 million in buying power. This leverage magnifies gains (good years produce outsized returns) and magnifies losses. The prime broker manages this risk through daily repricing and margin maintenance requirements. Every day, the broker marks all positions to market and calculates the fund's net equity. If equity falls below a minimum (often called the maintenance margin), the broker issues a margin call.

## The Margin Call Process

The mechanics are straightforward in principle but catastrophic in practice. Here's the sequence:

**Day 1**: A hedge fund has $100 million in equity and has borrowed $250 million. Positions are marked to market at market close. A major market move or news event causes the fund's core holdings to lose $20 million overnight.

**Day 2, Morning**: The prime broker reprices. The fund now has $80 million in equity against $250 million in borrowings—a [leverage ratio](/leverage-ratio-forex/) of 3.1:1. The broker's requirement is 2:1; the fund is out of compliance. The broker issues a margin call: deposit $50 million or sell down positions to restore the 2:1 ratio.

**The Fund's Dilemma**: The fund doesn't have $50 million in spare cash (most of its capital is deployed). It must sell positions. But which ones? If it sells its smallest or most liquid holdings, it realizes losses and weakens its investment thesis. If it holds, it risks forced liquidation at even worse prices.

## Forced Liquidation Mechanics

If a hedge fund fails to meet a margin call within 24–48 hours, the prime broker has contractual authority to liquidate positions unilaterally. This is where prime broker leverage becomes dangerous.

The broker doesn't care about the fund's investment thesis or market timing. It cares only about recovering its loan. So it sells the most liquid positions first—the same stocks or bonds every hedge fund holds. This creates a wall of forced selling at the exact moment price discovery is worst.

A $50 million equity position that would trade normally at a 0.5% bid-ask spread becomes a $50 million forced sale in a thin market. The fund gets filled at 2–5% below the last "normal" trade price, or worse. If multiple prime brokers are liquidating hedge fund positions simultaneously—a systemic event—the slippage can reach 10–20% or more.

## The Cascade Effect

Prime broker margin calls become systemic when many funds face them simultaneously. Here's why:

**Shared Positions**: If multiple hedge funds own the same stock or bond (a [crowded trade](/hedge-fund-crowding-risk/)), margin calls affecting one fund trigger forced selling that moves prices against other funds holding the same position. Those other funds then face margin calls too.

**Shared Prime Broker**: If multiple funds borrow from the same prime broker, the broker may intentionally stagger liquidations to limit market impact. But in a crisis, the broker prioritizes its own balance sheet. A broker in financial stress may liquidate accounts aggressively, feeding the cascade.

**Interconnected Counterparties**: A hedge fund borrows from a prime broker and trades derivatives with investment banks. If forced liquidation forces the fund to unwind swaps or options, it imposes losses on the dealer counterparties. Those losses can spread to other banks and funds.

**Contagion Through Leverage**: Leverage magnifies the cascade. If a fund uses 3:1 leverage and its portfolio drops 15%, the fund is wiped out. Its creditors (prime broker, counterparties, lenders) incur losses. Those lenders then tighten credit for other funds, forcing them to deleverage, which drives prices lower, which triggers more margin calls.

## Historical Examples of Prime Broker Blowups

**Long-Term Capital Management (1998)**: LTCM had $4.7 billion in equity but controlled $125 billion in positions—27:1 leverage. When a Russian default caused market dislocation, LTCM's convergence trades moved against it sharply. Prime brokers realized LTCM was insolvent and began margin calls. LTCM couldn't liquidate its positions without moving markets catastrophically, so the Fed orchestrated a $3.6 billion consortium bailout instead.

**Archegos Capital (2021)**: Archegos had $10 billion in equity but controlled $160 billion in positions via total return swaps—a form of leverage that many investors overlooked. When key holdings like ViacomCBS crashed 40%, Archegos faced margin calls it couldn't meet. Its prime brokers (Credit Suisse, Nomura, and others) were forced to liquidate $30+ billion in positions in days. The cascade wiped out $100 billion in value and exposed how opaque leverage in derivatives markets had become.

**2008 Bear Stearns**: Bear Stearns was a major prime broker itself. As mortgage-backed securities lost value, prime brokers and counterparties lost confidence. Funding dried up. Bear couldn't meet margin calls to its own lenders, triggering a run. JPMorgan was forced to acquire it at a distressed price within days.

## Mitigation and Risk Management

Sophisticated hedge funds and their prime brokers work to prevent margin-call cascades:

**Conservative Leverage Policies**: Funds with 2:1 leverage have more cushion before forced liquidation than 4:1 funds. Some regulations now cap prime broker leverage, though enforcement varies.

**Multi-Prime Broker Approach**: A fund that uses three different prime brokers can negotiate more favorable terms and isn't entirely at the mercy of any single broker. If one broker becomes unstable, the fund can move positions to others.

**Diversified Collateral**: Rather than concentrating borrowed capital in one position, funds spread leverage across many uncorrelated positions. This reduces the risk that a single market move triggers a proportional margin call.

**Liquidity Buffers**: Holding 10–20% of assets in cash or very liquid securities means the fund can meet margin calls without forced selling. It's an insurance premium on stability.

**Stress Testing**: Funds model daily scenarios: "What if my leveraged positions decline 10% overnight?" or "What if my primary prime broker becomes insolvent?" Stress testing reveals when leverage is too high.

**Counterparty Due Diligence**: Evaluating prime broker creditworthiness and capital adequacy is now standard. Funds avoid brokers with weak capital ratios or high [concentrated credit risk](/concentration-risk/).

## Regulatory Oversight

After 2008, regulators tightened rules on prime brokers and leverage. The Dodd-Frank Act mandated clearing of most derivatives through central counterparties, reducing bilateral counterparty risk. Basel III capital requirements forced prime brokers to hold more capital against their leverage exposure to hedge funds.

However, regulatory gaps persist. Leverage through total return swaps (the Archegos vector) remains less transparent than traditional margin lending. Offshore funds face looser oversight. The SEC and CFTC continue expanding surveillance of leverage concentrations, but systematic monitoring of hedge fund aggregate positions remains incomplete.

## See also

<div class="wiki-seealso">

### Closely related

- [Hedge Fund vs Private Equity](/hedge-fund-vs-private-equity-differences/) — Why structural leverage makes hedge funds vulnerable to margin calls
- [Hedge Fund Crowding Risk](/hedge-fund-crowding-risk/) — How concentrated positions amplify margin-call cascades
- [Hedge Fund for Family Offices](/hedge-fund-for-family-offices/) — Due diligence questions institutional allocators ask about leverage
- [Leverage Ratio](/leverage-ratio-forex/) — Measuring debt vs. equity and margin coverage
- [Counterparty Risk](/counterparty-risk/) — Credit exposure to prime brokers and derivatives dealers
- [Liquidity Risk](/liquidity-risk/) — The cost of forced selling in thin markets

### Wider context

- [Credit Risk](/credit-risk/) — Broader framework for understanding broker insolvency and contagion
- [Systemic Risk](/systemic-risk/) — How individual margin calls can freeze credit markets
- [Dodd-Frank Act](/dodd-frank-act/) — Post-2008 regulatory constraints on prime brokers and leverage
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulator overseeing prime broker capital and leverage limits

</div>
