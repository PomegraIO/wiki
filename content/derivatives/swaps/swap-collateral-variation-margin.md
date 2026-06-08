---
title: "Variation Margin and Collateral in Cleared Swaps"
description: "Variation margin and collateral in cleared swaps are daily margin calls that adjust for mark-to-market changes, plus initial margin to cover future credit exposure over the closeout period."
keywords:
  - variation margin collateral cleared swaps
  - daily margin calls swaps
  - initial margin cleared swaps
  - swap collateral requirements
---

*In centrally cleared swaps, **variation margin** is posted daily to reflect the mark-to-market profit or loss on the position, while **initial margin** is held upfront to protect against potential future exposure during the closeout period. Together, these collateral mechanisms ensure that counterparty credit risk is minimal and that the central clearing counterparty (CCP) can cover losses even if a participant defaults. Understanding how and why these margins work is essential to grasping modern swap risk management.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Variation Margin & Collateral — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for derivatives." />

<div class="wiki-infobox-caption">Daily margin calls and upfront collateral protect cleared swaps against counterparty default.</div>

|   |   |
|---|---|
| **Variation margin** | Daily cash adjustment for realized mark-to-market gains and losses |
| **Initial margin** | Upfront collateral to cover potential future exposure during closeout |
| **Frequency** | Variation margin typically daily; initial margin calculated at trade inception and adjusted periodically |
| **Amount** | Variation margin equals daily P&L; initial margin scales with notional, tenor, and volatility |
| **Collateral forms** | Cash, government bonds, or other high-quality liquid assets |
| **Enforceability** | Mandatory for centrally cleared swaps; bilateral OTC swaps increasingly use similar terms |
| **Impact on counterparty risk** | Dramatically reduces credit exposure versus uncleared swaps |

</aside>

## The Two Layers of Margin Protection

Cleared swap participants post two types of collateral:

1. **Variation margin**: Adjusted daily based on the mark-to-market value of the position.
2. **Initial margin**: A fixed amount posted at inception, held as a buffer against potential future losses.

Together, they eliminate the need for daily credit assessment of the trading counterparty. If a participant's position deteriorates, variation margin is posted before the loss becomes large. If the participant defaults, initial margin provides a cushion for the central clearing counterparty (CCP) to manage and close out the position.

## Variation Margin: Daily Mark-to-Market

Every business day, the clearing house marks every swap position to the current market price. If a participant has a $2 million gain on a swap, the other side has a $2 million loss. The losing side pays the winning side the $2 million in variation margin.

### Example

Party A enters a 5-year pay-fixed [interest-rate swap](/interest-rate-swap/) on $100 million notional:
- **Swap rate agreed**: 4.0% fixed.
- **Notional**: $100 million.

Three months later, market swap rates fall to 3.5%. Party A's position—paying 4.0% when the market is 3.5%—is now underwater. The value of that swap has declined, reflecting the loss in fair value.

The clearing house calculates the mark-to-market loss on Party A's position (say, $1.2 million) and requires Party A to post $1.2 million in variation margin cash by end of business. If rates subsequently rise back to 4.2%, Party A's swap is now in-the-money by approximately $1 million, so the clearing house pays Party A $1 million variation margin.

This daily exchange ensures that neither party builds up large unrealized losses. It is the economic equivalent of marking bonds to market in a bond portfolio every day and requiring the losing side to settle the change immediately.

### Settlement timing

Most CCPs settle variation margin on a T+0 basis (same day) or T+1 (next business day), depending on the currency and market convention. Intraday variation margin calls can occur during extreme market moves.

## Initial Margin: Protecting Against Future Exposure

While variation margin covers realized losses, swaps carry credit risk even when they are currently in-the-money. If a clearinghouse participant defaults, the CCP must close out that participant's positions in the market. The closing process takes time (typically 1–5 business days), and market prices can move unfavorably during that window.

Initial margin is sized to cover the potential future exposure (PFE) of the position during this closeout period. It answers the question: *If my counterparty defaults tomorrow and I must close out their swap at market prices, how much could I lose before I'm done closing?*

Initial margin is calculated using:
- **Notional**: Larger notional = larger margin.
- **Tenor**: Longer-dated swaps (5–10 years) have greater PFE than short-dated swaps.
- **Volatility**: Higher volatility (interest rate, FX) = higher margin.
- **Correlation**: Across a portfolio, diversification reduces margin if exposures offset.

### Initial margin calculation (simplified)

For a single interest-rate swap, a rough rule of thumb is:

**Initial Margin ≈ Notional × Tenor (years) × Interest-Rate Volatility × 1–2%**

A $100 million, 10-year swap in a 1% interest-rate volatility environment might require $10–20 million in initial margin. The exact amount depends on the CCP's margin model (often SPAN, CBOT's Standard Portfolio Analysis of Risk, or the CCP's proprietary model).

### Portfolio margining

If a participant has both long and short swaps, the CCP calculates margin on a net portfolio basis. A participant with $100 million long in 3-year swaps and $80 million short in 3-year swaps does not post margin on $180 million; instead, margin is calculated on the net $20 million exposure plus a credit-spread and volatility buffer.

## Collateral Eligibility

Not all assets count as posted collateral. Most CCPs accept:

- **Cash** (in the relevant currency).
- **Government securities** (Treasuries, Gilts, Bunds, etc.), typically at a haircut of 0–2%.
- **Agency debt** (e.g., Fannie Mae, Freddie Mac), with a small haircut.
- **Investment-grade corporate bonds**, with a higher haircut (5–15%).
- **Equities**, rarely and only high-liquidity blue chips, with large haircuts (10–30%).

The haircut reflects liquidity and credit risk. A $100 million Treasury posted at a 0.5% haircut counts as $99.5 million collateral; a corporate bond posted at a 10% haircut counts as $90 million.

This structure incentivizes participants to post high-quality, liquid collateral. It also ensures that if a participant defaults and the CCP must liquidate collateral, it can do so quickly without severe loss.

## How Variation Margin and Initial Margin Interact

Variation margin reduces the amount of initial margin required. If a swap moves against a participant:

1. **Daily variation margin** is posted, so the loss is crystallized and the CCP's exposure shrinks.
2. **Initial margin** is then required only on the remaining mark-to-market position, not the original position.

In stressed markets, when prices move by 5–10% daily:
- Variation margin calls explode.
- Initial margin may be recalculated and increased (a "margin call" in the traditional sense).

This can create a feedback loop during financial crises: large losses trigger variation margin calls, which drain liquidity, forcing participants to raise cash by selling other assets, which drives prices down further and increases margin requirements.

## The 2020 Dash for Cash and Margin

During the March 2020 COVID-19 crisis, volatility spiked across all asset classes. Variation margin calls on cleared swaps and other derivatives surged. Some participants faced $10–20 billion in daily margin calls, forcing them into fire-sales of bonds and equities. This contagion effect—margin calls driving broader market stress—is now a focus of regulatory stress testing.

In response, CCPs introduced margin buffer policies and regulatory agencies encouraged central banks to provide liquidity. The lesson: variation margin is a powerful stabilizer in normal times but can amplify stress in extremis.

## Bilateral OTC Swaps and Collateral Agreements

Not all swaps are centrally cleared. Many institutional-grade OTC swaps remain bilateral, governed by ISDA master agreements with [netting](/swap-netting-agreement/) provisions. For these swaps:

- Collateral agreements are negotiated bilaterally, not imposed by a CCP.
- Variation margin is typically exchanged less frequently (weekly or monthly) than in cleared markets.
- Initial margin (called "independent amount" or "threshold") is agreed between the two parties or may not be required at all if both are highly rated.

Post-2008, however, industry practice has moved toward daily margining even in bilateral swaps, especially for non-investment-grade counterparties.

## Margin and Leverage

For hedge funds, proprietary traders, and leveraged participants, margin requirements are a critical constraint. A $100 million hedge fund with a $1 billion notional [interest-rate swap](/interest-rate-swap/) position might need to post $50–100 million in initial margin plus variation margin buffers. This eats into their trading capital.

Conversely, large dealers and highly rated financial institutions may negotiate lower margin requirements (or so-called "threshold" amounts) because their credit quality is high. This structural advantage allows large institutions to hold more leveraged positions, a feature that has drawn regulatory criticism as a source of systemic vulnerability.

---

## See also

<div class="wiki-seealso">

### Closely related

- [Swap netting agreements](/swap-netting-agreement/) — how collateral interacts with legal netting
- [Notional principal in swaps](/notional-principal-swap/) — the underlying amount on which margin is sized
- [Counterparty risk](/counterparty-risk/) — the credit risk that margin mitigates
- [Interest-rate swap](/interest-rate-swap/) — the most common swap type subject to margin
- Mark-to-market accounting — how variation margin gain/loss is realized
- [Central clearing](/swap/) — the infrastructure that enforces margin requirements

### Wider context

- [Systemic risk](/systemic-risk/) — how margin calls can amplify market stress
- [Liquidity risk](/liquidity-risk/) — the operational challenge of posting variation margin
- [Leverage](/leverage-ratio-forex/) — how margin constrains leveraged trading

</div>
