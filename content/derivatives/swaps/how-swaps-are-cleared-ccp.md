---
title: "How Swaps Are Cleared Through a Central Counterparty"
description: "How interest rate swaps are cleared through a CCP: the lifecycle from trade execution through counterparty substitution, daily margining, and default-fund contributions that mutualize risk."
keywords:
  - how interest rate swaps are cleared ccp
  - central counterparty clearing
  - swap clearing process
  - initial margin
  - variation margin
image: "/svg/derivatives.svg"
---

*When two parties trade an [interest-rate-swap](/interest-rate-swap/), clearing through a **central counterparty (CCP)** transforms the transaction from a bilateral agreement into two offsetting contracts: one between each party and the CCP. The CCP becomes the middleman, guaranteeing performance by both sides through daily margining, initial capital requirements, and a shared default fund—converting individual [counterparty-risk](/counterparty-risk/) into systemic mutualization.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">How Swaps Are Cleared — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">A CCP inserts itself as intermediary, eliminating bilateral credit risk through daily settlement and pooled guarantees.</div>

|   |   |
|---|---|
| **Key players** | Original swap counterparties, CCP (e.g., LCH, CME), clearing members |
| **CCP role** | Becomes buyer to every seller, seller to every buyer; guarantees settlement |
| **Initial margin** | Upfront capital per trade; varies by notional, tenor, and risk model |
| **Variation margin** | Daily cash flow reflecting swap mark-to-market changes |
| **Default fund** | Shared mutualized guarantee; all clearing members contribute |
| **Settlement cycle** | Daily; T+0 or T+1 depending on CCP and instrument |

</aside>

## The Bilateral Swap vs. the Cleared Swap

Before clearing, two parties negotiated a swap directly. Party A (a bank) agrees to pay a fixed rate to Party B (a corporation) in exchange for receiving floating-rate coupons. The contract specifies notional amount, tenor, fixed and floating legs, payment dates, and termination rights. The two parties face each other's credit risk: if Party B defaults, Party A loses the net present value of the remaining swap cash flows. If Party A fails, Party B absorbs the loss.

This bilateral structure worked for decades but concentrated risk in the largest banks and made the derivatives market opaque. When Lehman Brothers collapsed in 2008, thousands of bilateral swaps went into default simultaneously, triggering cascading losses and uncertainty about who owed what to whom. The 2009 Dodd-Frank regulations and European equivalents then mandated that most standardized swaps clear through a CCP.

Clearing does not eliminate the swap—the economic terms remain identical. Instead, it inserts a guarantor between the two parties, transforming credit risk into operational and liquidity risk managed on a daily basis.

## How the CCP Steps In: Substitution

When a swap is submitted to a CCP for clearing, the CCP becomes the legal counterparty to both parties. The bilateral swap is "novated"—legally extinguished—and replaced with two separate cleared swaps: Party A versus CCP, and CCP versus Party B. Neither Party A nor Party B owes the other anything; they each owe the CCP.

This substitution happens in seconds via electronic instruction. The original trade details (notional, rate, tenor) are identical in both cleared contracts. From Party A's perspective, they are now long the floating leg and short the fixed rate, with the CCP as their counterparty. From Party B's perspective, they are short the floating leg and long the fixed rate, again with the CCP.

The CCP's guarantee is underpinned by three mechanisms: initial margin, variation margin, and the default fund.

## Initial Margin: Upfront Capital to Cover One-Day Risk

When a swap is cleared, both parties immediately deposit **initial margin** with the CCP. This is a cash or security transfer into a segregated account held in the clearer's name on behalf of each clearing member (and ultimately the end-user).

Initial margin is sized to cover potential price movement over a one-day period in a stressed market scenario. A longer-dated swap (e.g., 10-year tenor) with higher interest-rate sensitivity requires larger initial margin than a short-dated swap. A CCP uses a standardized risk model (Value-at-Risk, historical simulation, or similar) to set initial margins daily, adjusting for realized volatility and market conditions.

For a $100 million notional 5-year interest-rate swap, initial margin might range from $500,000 to $2 million, depending on the CCP's methodology and market volatility. Both the fixed-rate payer and fixed-rate receiver post initial margin; neither has priority in the event of default.

## Variation Margin: Daily Mark-to-Market Settlement

At the end of each trading day, the CCP marks all cleared swaps to market price. The change in value since the prior day—either positive or negative—is immediately settled in cash or securities. This is **variation margin**.

Suppose a 5-year interest-rate swap has a fixed rate of 4%, and market rates fall to 3.9% by end of day. The fixed-rate receiver now owns an in-the-money swap worth an estimated $300,000 (simplified). The CCP settles that gain: Party B's account is credited $300,000, and Party A's account is debited $300,000. Cash flows in and out daily, realizing gains and losses in real time.

Variation margin is the mechanism that keeps the CCP's exposure to either party small. Because mark-to-market is daily, the CCP's maximum loss on a defaulting party is limited to one day's price movement (plus any intraday moves during the default resolution window, typically a few hours). This is why initial margin is sized to cover one-day stress—it bridges the gap between daily settlement and the cost of exiting the defaulter's portfolio.

## The Default Fund and Mutualized Risk

Despite daily margining, a CCP cannot guarantee that variation margin will fully cover a sudden, catastrophic market move plus a concurrent clearing member default. To bridge this gap, the CCP maintains a **default fund** (or guarantee fund), which all clearing members contribute to proportionally.

When a CCP member defaults and their initial and variation margin are insufficient to cover losses on their portfolio, the CCP draws on the default fund. This spreads the loss across all other members. If the default fund is exhausted, the CCP's own capital is next. In the most extreme case, non-defaulting members may face "tear-up" assessments—additional capital calls to cover any remaining shortfall.

This mutualization is the tradeoff for the systemic stability that clearing provides. No single party bears the full risk of a counterparty default; all members share it. This incentivizes members to monitor each other's credit quality and operational integrity.

## The Clearing Member Layer

Not all market participants can clear directly. A CCP requires members to meet strict capital, operational, and governance standards. Most banks, hedge funds, and asset managers are not direct members; instead, they trade through a **clearing member** (typically a large bank) who submits their trades to the CCP on their behalf.

The clearing member collects initial and variation margin from the end-user and posts it to the CCP. The end-user faces the clearing member's credit risk (segregation rules limit this but do not eliminate it), while the clearing member faces the CCP. This tiered structure preserves the benefit of CCP clearing—systemic risk is concentrated at the CCP level—while allowing smaller firms to participate.

## Settlement and Operational Risk

Cleared swaps typically settle on a T+0 basis: margin due and settled the same day. Some CCPs offer T+1 settlement for certain instruments. The CCP also manages the mechanics of the accrued coupon exchange on reset dates. If a swap's floating leg resets on June 15, the CCP calculates the accrued coupon (e.g., the 3-month Libor equivalent since the last reset) and settles it between the parties.

This operational infrastructure is massive: the CCP must process millions of trades daily, maintain accurate pricing models, handle corporate actions (e.g., Libor changes), and manage defaults rapidly. Operational risk—system failures, settlement failures, cyber attacks—is now concentrated at a handful of major CCPs (LCH, CME Clearing, Eurex Clearing). Failures in one CCP could affect the entire financial system.

## Liquidity Implications and Market Depth

Clearing standardizes contracts (fixed notional amounts, standard tenors, defined reset dates), which deepens the pool of available counterparties and increases [price-discovery](/price-discovery/). A 5-year USD interest-rate swap traded through the same CCP by thousands of market participants creates tight bid-ask spreads and high liquidity.

However, clearing also imposes operational costs (CCP fees, margin management) and regulatory capital requirements (especially for banks under Basel III rules). These costs are passed to end-users through wider spreads than might exist in a bilateral market with a trusted counterparty. The tradeoff—lower [credit-risk](/credit-risk/) and higher liquidity vs. higher operational costs—is generally accepted as net positive post-2008.

## See also

<div class="wiki-seealso">

### Closely related

- [Counterparty Risk](/counterparty-risk/) — credit risk that clearing eliminates through mutualization
- [Interest Rate Swap](/interest-rate-swap/) — the primary instrument cleared; structure and use cases
- [Repurchase Agreement](/repurchase-agreement/) — another bilateral market subject to central clearing post-Dodd-Frank
- [Swap](/swap/) — generic derivative swap class; mechanics and variations
- [Credit Default Swap](/credit-default-swap/) — swap type with similar clearing infrastructure

### Wider context

- [Derivatives Hedging](/derivatives-hedging/) — use cases for swaps and other cleared derivatives
- [Dodd-Frank Act](/dodd-frank-act/) — regulation mandating clearing for standardized swaps
- [Systemic Risk](/systemic-risk/) — the concentration risk of clearing houses in the financial system
- [Liquidity Risk](/liquidity-risk/) — operational risk of margin and default-fund liquidity
- [Price Discovery](/price-discovery/) — how clearing standardization improves market pricing

</div>
