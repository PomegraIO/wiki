---
title: "Commodity-Linked Note"
description: "Structured debt instruments whose repayment or returns are tied to commodity prices, offering leverage, capital protection, or synthetic commodity exposure."
keywords:
  - commodity-linked note
  - structured note
  - commodity bond
  - capital-protected note
  - structured product
  - leverage note
image: "/svg/commodities.svg"
---

*A **commodity-linked note** is a bond issued by a bank that promises returns linked to commodity-price performance. The investor may receive capital protection (get their principal back even if the commodity falls) and a leveraged commodity-price payoff, or they may accept mark-to-market daily pricing in exchange for lower fees. These structures embed commodity exposure inside a debt instrument, typically sold to retail investors seeking commodity access without direct futures trading.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Commodity-Linked Note — key facts</div>

<img src="/svg/commodities.svg" alt="An abstract editorial mark for commodities and natural resources." />

<div class="wiki-infobox-caption">Leverage and optionality wrapped in a bond; issuer credit risk embedded in returns.</div>

|   |   |
|---|---|
| **What it is** | Structured debt whose maturity value or coupons depend on commodity prices |
| **Common structures** | Capital-protected, leveraged, barrier (knock-out), inverse |
| **Payoff** | Price appreciation, coupon income, or both, tied to commodity |
| **Leverage** | 2×, 3×, or higher multipliers on commodity moves common |
| **Term** | Typically 3–10 years; some embedded with early-call rights (issuer can redeem) |
| **Key appeal** | Leverage with partial capital protection; tax structuring; yield enhancement |
| **Main risk** | Issuer credit risk; embedded optionality is costly; illiquidity if issuer deteriorates |
| **Issued by** | Large banks (structuring teams) to retail and some institutional clients |

</aside>

## Structure and payoff profiles

A commodity-linked note is fundamentally a bond combined with an [option](/option/) on a commodity. When you buy a note, you lend money to the issuer (usually a bank) for a fixed term, say five years. At maturity, instead of receiving a fixed interest payment, you receive a payoff based on the commodity price.

The simplest version is a leveraged note. You invest $10,000, and the bank promises that at maturity, you receive $10,000 plus 2× the percentage gain in oil prices (or 2× the loss). If oil rises 20%, you get $12,000 (a 20% gain on principal). If oil falls 20%, you get $6,000 (a 20% loss on principal, plus repayment of the $10,000 principal = $8,000; wait, that is already reflected). The leverage multiplies both directions.

A capital-protected variant is more complex: the bank guarantees you receive at least your $10,000 back at maturity, no matter what the commodity does. But if oil rises 20%, you receive $10,000 plus, say, 80% of the gain (or perhaps 2× the gain, funded by insurance costs). The protection against downside comes at a cost: the upside is capped or reduced. The bank finances this protection using [options](/option/), buying a [put option](/put-option/) on the commodity index to cap the investor's losses. This insurance is expensive, so the upside participation is limited.

Other structures are barrier notes (they pay full leverage only if the commodity stays above or below a certain price), inverse notes (they profit if the commodity falls), or income notes (they pay a fixed coupon plus a leveraged kicker). The variety is limited only by the issuer's imagination and the investor's risk tolerance.

## Why banks sell these

Commodity-linked notes are immensely profitable for issuers. The bank embeds options and leverage into the structure, prices those options using quantitative models, and sells the note to retail investors at a markup. The investor overpays for the optionality, and the bank pockets the profit.

From the investor's perspective, a commodity-linked note is often a poor deal compared to buying a [commodity ETF](/etf/) and using a brokerage margin account to lever it. The optionality embedded in the note—the capital protection, the leverage formula, the barrier triggers—is priced assuming certain volatility and commodity-price behaviour. If the market behaves differently, the investor suffers. The bank, conversely, hedges its optionality exposure and locks in a profit regardless.

That said, there are genuine use cases. An investor who cannot access futures or derivatives directly (due to regulatory status or internal policy) can gain commodity exposure through a note. An investor in a high tax bracket might use a capital-protected structure to manage expected losses without triggering wash-sale issues. A retail investor intimidated by margin accounts and leverage can get a controlled, bounded exposure through a note with built-in stops.

## Capital protection comes with a cost

Capital-protected commodity notes sold well during the 2008 crisis and the 2020 pandemic when investors were terrified of losses. A note that promises "you keep your $10,000 even if oil crashes to zero" is reassuring. But the protection is not free.

The bank hedges this guarantee by buying a [put option](/put-option/) on the commodity, locking in a floor price. If the commodity is currently trading at $60 per barrel and the put strike is $50, the bank pays the option premium upfront. This cost is deducted from the investor's upside participation. If the put costs 10% of the notional value, the investor receives only 90% of any commodity-price gain. Over ten years, that 10% reduction in upside is material.

Moreover, the protection is only as good as the issuer's credit. If the bank fails or is downgraded, the capital protection may be worthless. During the 2008 crisis, investors holding capital-protected notes issued by failing banks discovered that the "guarantee" depended on the issuer's solvency. This is called ["going-concern" risk](/going-concern/): the structure assumes the issuer survives.

## Leverage and daily compounding

Commodity-linked notes often embed leverage, sometimes extreme. A 3× or 5× leveraged note amplifies commodity moves by that multiple. But there is a catch: if the note is not daily-rebalanced (and most structured notes are not), its leverage drifts over time.

Consider a 2× leveraged note on oil. On day one, oil is at $100. Your leverage is exactly 2×. On day two, oil rises to $105 (a 5% gain). Your note should be worth $110 (5% × 2 = 10% gain). On day three, oil falls to $100 (a 4.76% loss from $105). If daily rebalancing occurred, your note would fall 9.52% (4.76% × 2), landing at roughly $100.52. But if the note is not rebalanced, the leverage ratio has changed: the gain of $10 on $110 is not exactly 2× the 4.76% loss.

This compounding effect, called "volatility decay," is a quiet tax on leveraged notes held over months or years. In volatile commodities, the decay can be significant. An investor holding a leveraged note expecting a simple multiple of the commodity's total return can be surprised by underperformance caused by rebalancing friction.

## Credit risk and early redemption

A commodity-linked note is a liability of the issuing bank. If the note is sold by a bank rated BBB, the note is also credit-rated BBB (or the option's value is discounted for credit risk). A downgrade of the bank is a disaster: the note's secondary-market value collapses, and the investor may be forced to hold it until maturity.

Many notes include an embedded call option, allowing the issuer to redeem the note early. If the structure is performing well for the investor (the commodity has risen significantly), the bank may call the note early and pocket the difference. If the commodity has fallen, the bank lets the note run. This asymmetry favours the issuer.

## Comparison to other commodity vehicles

A commodity-linked note offers leverage and structured payoffs that a plain [ETF](/etf/) or [index fund](/index-fund/) does not. But it carries issuer credit risk, embedded leverage complications, and is often expensive relative to the underlying commodity exposure. An [exchange-traded commodity](/exchange-traded-commodity/) is a simpler debt instrument with transparent leverage and no embedded optionality. A [physically backed commodity ETF](/physically-backed-commodity-etf/) is transparent and cost-efficient. A [commodity total return swap](/commodity-total-return-swap/) offers institutional investors bespoke leverage and is priced more fairly.

A commodity-linked note is best suited for retail investors who want leverage or protection but cannot access derivatives directly. Sophisticated investors usually find better value elsewhere.

## See also

<div class="wiki-seealso">

### Closely related

- [Exchange-Traded Commodity](/exchange-traded-commodity/) — Debt-backed commodity exposure without embedded optionality
- [Physically Backed Commodity ETF](/physically-backed-commodity-etf/) — Direct commodity ownership via exchange-traded fund
- [Commodity Total Return Swap](/commodity-total-return-swap/) — Bespoke bilateral commodity returns transfer
- [Option](/option/) — Right (not obligation) to buy or sell at a fixed strike price
- [Put Option](/put-option/) — Protective downside insurance in structured products
- [Leveraged ETF](/leveraged-etf/) — Daily-rebalancing fund providing constant leverage multiples
- [Call Option](/option/) — Upside participation mechanism embedded in notes

### Wider context

- Commodity — Raw materials and energy traded globally
- [Derivative](/futures-contract/) — Synthetic financial instrument deriving value from an underlying
- [Bond](/bond/) — Fixed-income debt instrument
- [Credit Rating](/credit-rating/) — Issuer solvency assessment and risk quantification
- [Structured Product](/commodity-linked-note/) — Customised debt or investment combining bonds and derivatives

</div>
