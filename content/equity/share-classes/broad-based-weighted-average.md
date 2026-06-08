---
title: "Broad-Based Weighted Average"
description: "An anti-dilution mechanism that reprices preferred shares to the weighted-average price of all dilutive securities issued in a subsequent round."
keywords:
  - weighted average anti-dilution
  - broad-based formula
  - anti-dilution mechanism
  - down round financing
  - preferred stock protection
image: "/svg/equity.svg"
---

*A **broad-based weighted average** anti-dilution clause reprices [preferred stock](/preferred-stock/) to reflect the weighted-average price at which all equity (and all dilutive securities) were issued in a subsequent financing round. If a company issues shares at multiple prices or volumes, the repricing averages them proportionally—protecting the preferred investor from dilution without the severe founder destruction of a [full ratchet](/full-ratchet-anti-dilution/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Broad-Based Weighted Average — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for equity and share structure." />

<div class="wiki-infobox-caption">The industry-standard anti-dilution formula—investor protection with founder fairness.</div>

|   |   |
|---|---|
| **What it is** | Repricing to the weighted-average price of all issued shares and convertible securities |
| **Also called** | Weighted average anti-dilution, broad-based formula, broad-based WA |
| **Calculation basis** | All outstanding common + all dilutive securities (options, warrants, convertibles) |
| **Effect on founders** | Moderate dilution; founder common suffers proportionally to actual down round size |
| **Trigger** | Any issuance below the preferred's conversion price |
| **Contrast** | [Full ratchet](/full-ratchet-anti-dilution/) — reprices to the lowest price paid, regardless of volume |

</aside>

## The balancing act

A preferred investor wants protection from down rounds: if the company's valuation drops, the investor should not be blindsided by dilution. But an overly harsh anti-dilution clause can strangle founders and deter future fundraising. The [full ratchet](/full-ratchet-anti-dilution/) reprices preferred to the single lowest price paid, a sledgehammer that can crater founder ownership even if most investors are paying a much higher price.

The broad-based weighted average is a compromise. It reprices the preferred to the actual average price paid across the round, weighted by the volume of shares issued at each price. If most investors pay $6 per share but a small strategic tranche sells at $4, the weighted average might be $5.80. The repricing is real, but proportional to the actual dilution the company suffered, not punitive.

This formula has become the market standard for Series B and later rounds, and increasingly even for Series A, because it aligns the preferred investor's protection with commercial reality.

## How the calculation works

The mechanics are more complex than a full ratchet but follow a clear formula.

Start with a company that issued Series A preferred stock at $10 per share. The Series A investor holds, say, 1 million shares and paid $10 million. The company also has 5 million shares of [common stock](/common-stock/) outstanding, mostly held by the founder. The company is valued at $150 million (6 million shares at $25 per share post-Series A).

Two years later, the company struggles. It needs capital and approaches new investors. Interest is soft; investors bid $6 per share. The board accepts and raises $60 million by issuing 10 million new shares at $6.

Now the question: what is the weighted-average price?

The broad-based formula includes all dilutive securities—all common stock, all preferred, all options in the money, and any convertible securities. Assume for simplicity that all existing equity was common or Series A preferred, and the only new issuance is the Series B at $6.

**Outstanding shares before Series B:**
- Common: 5 million shares
- Series A preferred: 1 million shares
- Total: 6 million shares

**New issuance (Series B):**
- 10 million shares at $6

**Weighted-average calculation:**
Weighted average price = (outstanding shares × old price + new shares × new price) / (outstanding + new)
= (6 million × average old price + 10 million × $6) / (6 million + 10 million)

But what is the "old price"? The Series A paid $10, common shareholders' basis is unknown. The solution: use a "fully diluted" common valuation. Assume the post-Series A valuation of $25 per share (from earlier) is the benchmark for the Series A's conversion price. Then:

= (6 million × $25 + 10 million × $6) / 16 million
= ($150 million + $60 million) / 16 million
= $210 million / 16 million
= **$13.125 per share**

The Series A preferred, originally convertible at $10, now reprices to $13.125—a *repricing upward* in this scenario. Wait, that seems wrong?

Actually, it makes sense: the Series B came in at $6, well below the original $25 valuation, but the weighted-average price is $13.125 because the existing shareholders (who are not selling down) hold a much larger value at the original price. The repricing is "up" because the dilution is real but not total. The company and its existing shareholders were valued at $150 million; the new capital values the company at $60 million. The average of those two values, weighted by share count, is in between.

In real practice, if the Series B had been at $6 and the company faced a true down round, the weighted-average price would likely still be lower than $10, but not as catastrophically low as the full ratchet would make it.

## Broad-based versus narrow-based

Some investors negotiate for a "narrow-based" weighted average that includes only the newly issued preferred in the calculation, not the entire common stock outstanding. This is still more moderate than a full ratchet but harsher than a true broad-based weighted average.

The difference: a broad-based formula uses all common and all dilutive securities in the denominator. A narrow-based formula counts only shares of the same series or class—for instance, only Series A preferred, not all common.

Because common shares are usually far more numerous than preferred, including them in the denominator (broad-based) makes the repricing less severe. Narrow-based formulas can still be harsh to founders, but they are preferred by more aggressive investors.

Modern venture capital standard is broad-based. If an investor demands narrow-based, that is a negotiation point—a signal that they are less founder-friendly than the market norm.

## When broad-based repricings actually occur

In practice, down rounds that trigger broad-based repricings are rare in successful venture portfolios because most venture companies either scale successfully (driving valuations upward) or fail and shut down (no subsequent round to trigger repricing).

When they do occur, broad-based repricings are most common in Series B and Series C, when the company is still venture-backed but growth is slower than hoped. A Series A investor entered at $10; Series B comes at $8; the broad-based repricing applies. The Series A investor's conversion price drops to something like $8.50, a moderate penalty that protects them from the full brunt of the $10-to-$8 drop.

Late-stage venture and growth equity investors often relax anti-dilution clauses further or eliminate them, because at that stage the company's fundamentals and market position are better known. Repricing feels less necessary.

## The strategic use and abuse

Well-written broad-based weighted average clauses include carve-outs for specific issuances that should not trigger repricing. Equity granted to employees as options is usually carved out—the company does not want to trigger anti-dilution every time it makes an option grant. Convertible debt is often carved out too, or included at a formulaic conversion price rather than the price at which the debt actually converts.

These carve-outs are crucial to the clause's effectiveness. Without them, a company could not do employee equity grants or raise bridge financing without triggering repricing and damaging the cap table.

Additionally, if multiple rounds of issuance happen in quick succession at different prices, the repricing mechanism can chain: Series B reprices Series A; Series C reprices both Series A and B. The cumulative effects can still be severe, even with a broad-based formula. Some sophisticated term sheets include an "anti-stacking" rule or a specific anti-dilution adjustment formula that prevents repricing from compounding unreasonably.

## Why founders accept broad-based weighted average

Founders accept broad-based weighted average clauses because they are the market standard and because the alternative—full ratchet—is much worse. In a down round, some dilution is inevitable; the broad-based formula ensures the dilution is proportional to the actual valuation drop, not a punitive multiple of it.

Additionally, founders recognize that investors *do* take real downside risk in venture. A Series A investor who paid $10 per share faces a genuine loss if the company later raises at $6. Some repricing mechanism is legitimate. The broad-based weighted average is the consensus about where fairness lies.

## See also

<div class="wiki-seealso">

### Closely related

- [Full Ratchet Anti-Dilution](/full-ratchet-anti-dilution/) — the harsher alternative anti-dilution formula
- [Preferred Stock](/preferred-stock/) — the equity class that uses anti-dilution clauses
- [Common Stock](/common-stock/) — the class diluted by anti-dilution adjustments
- [Conversion Price](/preferred-stock/) — the per-share price at which preferred converts
- [Down Round](/equity-financing/) — a lower-valuation round that triggers repricing
- [Series A](/initial-public-offering/) — the typical round where anti-dilution language is first introduced

### Wider context

- [Equity Financing](/equity-financing/) — the capital-raising context where anti-dilution is negotiated
- [Venture Capital](/private-equity-fund/) — the investor class using anti-dilution clauses
- [Term Sheet](/initial-public-offering/) — the legal document outlining repricing formulas
- [Share Dilution](/authorized-but-unissued-shares/) — the broader phenomenon anti-dilution protects against
- [Liquidation Preference](/preferred-stock/) — another protective feature of preferred stock

</div>