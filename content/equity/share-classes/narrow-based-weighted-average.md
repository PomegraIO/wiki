---
title: "Narrow-Based Weighted Average"
description: "An anti-dilution formula that resets preferred shares' conversion price using only issued preferred stock, delivering a sharper adjustment than broad-based methods."
keywords:
  - anti-dilution protection
  - weighted-average formula
  - preferred shares
  - down round
  - conversion price
image: "/svg/equity.svg"
---

*A **narrow-based weighted average** is an anti-dilution protection formula that recalculates the conversion price of [preferred stock](/preferred-stock/) based on the number of previously issued preferred shares, ignoring common stock and options. It produces a steeper reset in a down-round scenario, protecting venture investors more aggressively than broad-based alternatives.*

## The mechanics: preferred shares only

When a company issues new equity at a lower valuation than a previous round—known colloquially as a down round—earlier [preferred stock](/preferred-stock/) investors face dilution of their ownership. The narrow-based weighted-average formula recalculates their conversion price by weighting the new issue against *issued preferred stock only*. Common stock, employee options, and other securities are excluded.

The formula is:

```
New Conversion Price = Old Conversion Price × 
                      (Issued Preferred Before Down Round) / 
                      (Issued Preferred Before + New Preferred Issued)
```

Consider a concrete example. An investor purchased [preferred stock](/preferred-stock/) at $10 per share when 1 million preferred shares were outstanding. The company then issues a new round of preferred at $6 per share, raising capital by issuing 500,000 new preferred shares. The narrow-based calculation:

```
New Price = $10 × 1,000,000 / (1,000,000 + 500,000)
          = $10 × 0.667 = $6.67
```

The conversion price drops from $10 to $6.67. When the [preferred stock](/preferred-stock/) holder eventually converts to [common stock](/common-stock/), they receive proportionally more common shares, cushioning their economic loss from the lower-priced round.

## Narrow-based versus broad-based

The critical distinction lies in the denominator. Broad-based weighted-average includes all outstanding equity in the calculation: [common stock](/common-stock/), all [preferred stock](/preferred-stock/) series, employee [options](/option/), warrants, and other convertible securities. This produces a milder adjustment.

Using the same scenario but assuming 5 million [common stock](/common-stock/) shares existed:

- **Narrow-based**: $10 × 1,000,000 / 1,500,000 = $6.67 (33% reduction in conversion price)
- **Broad-based**: $10 × 6,000,000 / 6,500,000 = $9.23 (8% reduction)

The narrow formula creates a far steeper adjustment. From a [preferred stock](/preferred-stock/) investor's perspective, this is protective; from a founder and [common stock](/common-stock/) holder's perspective, it is punitive. The gap between equity ownership and voting control (via conversion) widens dramatically in a down round with narrow-based anti-dilution.

## Standard practice in venture capital

Narrow-based weighted-average protection is market-standard in US venture capital [preferred stock](/preferred-stock/) term sheets, particularly in Series A and later rounds. Large venture firms include it as routine boilerplate—investors assume they will receive it unless they negotiate otherwise. Founders typically accept it as the cost of raising venture capital; however, they often negotiate for modifications:

- A **price cap** (e.g., "conversion price cannot go below 80% of the down-round price")
- A **carve-out** (e.g., "anti-dilution applies to Series A only, not Series B")
- **Broad-based** anti-dilution instead of narrow-based

Some venture funds in overheated markets have dropped anti-dilution entirely, betting that liquidity events will make the protection moot.

## Why venture investors demand it

Venture capitalists justify narrow-based anti-dilution clauses as compensation for risk:

1. **Asymmetric risk.** Venture investors bear the bulk of [business cycle](/business-cycle/) and [market risk](/market-risk/) during the company's early years. [Preferred stock](/preferred-stock/) carries downside protection (via [liquidation preferences](/liquidation-preference/)) and upside participation. Anti-dilution protects the downside cushion.

2. **Negotiating leverage.** Large venture firms have sufficient reputation and follow-on capital that founders accept whatever anti-dilution terms they offer. Market power, not economic principle, drives the use of narrow-based formulas.

3. **Path dependency.** Venture contracts are templated and precedent-driven. If Series A used narrow-based, Series B also does. Founders rarely muster the negotiating power to shift to broad-based after the first round.

## Impact on founder and employee wealth

The practical effect emerges in exit scenarios. Suppose a company:

- Raises Series A at $10 per share (1 million shares issued, $10 million capital raised)
- Does a down round at $6 per share (500,000 shares issued, $3 million capital raised)
- Exits five years later at $8 per share (implying an $80 million valuation)

Under narrow-based anti-dilution, Series A holders' conversion price resets to $6.67, so they convert into significantly more [common stock](/common-stock/) at exit. The [common stock](/common-stock/) pool—owned by founders and employees—is compressed because so much equity went to the preferred class before conversion. In a middle-range exit like this, narrow-based anti-dilution can transfer $5–15 million of founder and employee wealth to venture investors.

If the company had negotiated broad-based or no anti-dilution, the [common stock](/common-stock/) pool would be larger at exit, benefiting the team. This dynamic is one reason sophisticated founders and their lawyers scrutinize term sheets: the anti-dilution language can swing $millions in outcomes.

## Investor protection and moral hazard

One unintended consequence of narrow-based anti-dilution: it can weaken investor discipline. If Series A investors know their conversion price has a floor (via anti-dilution), they may accept down-round pricing more readily than they otherwise would. The anti-dilution clause becomes a crutch, reducing the sting of a failed investment thesis.

Some argue that removing or limiting anti-dilution would force venture investors to be more selective and patient, improving capital allocation. Conversely, anti-dilution advocates contend that down rounds are inevitable in venture and that investors deserve a baseline protection.

## International practice

Broad-based weighted-average is more common in European and Australian venture markets, where anti-dilution overall is less aggressive. Full-ratchet anti-dilution (resetting the conversion price to the down-round price, with no weighting) is rare in modern venture but occasionally appears in restructurings or in deals where one investor dominates.

## See also

<div class="wiki-seealso">

### Closely related

- [Preferred Stock](/preferred-stock/) — the security carrying anti-dilution protection
- Conversion Price — the metric being recalculated
- [Common Stock](/common-stock/) — the residual equity class affected by conversion
- [Liquidation Preference](/liquidation-preference/) — companion preferred-shareholder protection
- [Option](/option/) — employee equity often excluded from anti-dilution denominator

### Wider context

- Dilution — the underlying ownership impact
- [Stock](/stock/) — all equity classes
- [Market Capitalization](/market-capitalization/) — valuation frame for exits
- [Business Cycle](/business-cycle/) — venture risk context
- [Market Risk](/market-risk/) — systematic risk preferred investors hedge against

</div>
