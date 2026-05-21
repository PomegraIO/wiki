---
title: "Anti-Dilution Provisions"
description: "Contractual protections that adjust an investor's conversion price or share count downward if the company issues shares at a lower price, preserving the investor's ownership or economic value."
---

*Anti-dilution provisions are clauses in preferred stock agreements that protect investors from dilution—the reduction in ownership percentage or economic value—when a company issues new shares at a price lower than the investor's original purchase price. Upon a down round (a fundraising at a lower valuation), anti-dilution provisions adjust the investor's conversion price or share count downward, maintaining their economic interest or voting power. These are standard in venture capital and private equity investing.*

## Types of anti-dilution

**Weighted-average anti-dilution**: The conversion price is adjusted based on a weighted-average calculation considering the old price, new price, and share quantities. Less protective to the investor than full ratchet.

**Full ratchet anti-dilution**: The conversion price is reduced to the lowest price paid by any investor in a later round. The most protective (and most punitive to common shareholders).

**Broad-based weighted-average**: Uses all outstanding shares (including options and warrants) in the weighted-average calculation. More protective than narrow-based.

**Narrow-based weighted-average**: Uses only preferred shares in the weighted-average calculation. Less protective than broad-based.

**No anti-dilution**: Some investors accept no protection, allowing their conversion price to remain fixed even in down rounds.

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Anti-Dilution Provisions — key facts</div>
  <table>
    <tr><th>Purpose</th><td>Protect investor from down-round dilution</td></tr>
    <tr><th>Mechanism</th><td>Adjust conversion price or share count downward</td></tr>
    <tr><th>Types</th><td>Full ratchet, weighted-average (broad or narrow), none</td></tr>
    <tr><th>Impact</th><td>Increases investor's pro-rata ownership; dilutes common shareholders</td></tr>
  </table>
</aside>

## Full ratchet example

A Series A investor buys 1M preferred shares at $10/share, investing $10M.

**Conversion**: 1M preferred = 1M common (1:1 conversion ratio).

**Series B down round**: Company issues new Series B preferred at $5/share.

**Full ratchet adjustment**: The Series A investor's conversion price is reduced to $5/share. The conversion ratio is now 1M preferred → 2M common (the investor can now convert to 2x as many common shares).

**Effect**: The Series A investor's pro-rata ownership increased (from 1M / existing common to 2M / existing common). The pre-existing common shareholders (founders, employees with common stock) are diluted—the investor now has a larger claim on the company.

## Weighted-average example

Same scenario, but with weighted-average anti-dilution:

**Weighted-average formula**:
New conversion price = Old conversion price × (Old shares outstanding + New shares issued) / (Old shares outstanding + New shares issued at new price)

Simplified: New CP = $10 × (Old cap + New money at new price) / (Old cap + New money at old price)

**Calculation** (assuming simple case):
- Old price: $10, old shares: 1M = $10M
- New price: $5, new shares: 2M = $10M (Series B raises same amount at lower price)
- New conversion price: $10 × (10M + 10M) / (10M + 20M) = $10 × 20M / 30M = $6.67

The Series A investor's conversion ratio is now $10 / $6.67 = 1.5M common shares (from 1M). Still dilution protection, but less extreme than full ratchet (2M).

## Why companies grant anti-dilution

**Investor requirement**: Venture investors almost always demand anti-dilution protection. It's a core term in preferred stock.

**Risk mitigation**: Startups are risky; down rounds are not uncommon. Anti-dilution protects the investor's economic interest if the company stumbles.

**Fundraising facilitation**: Anti-dilution makes preferred stock more attractive and easier to sell. Investors are willing to invest at lower discount rates if they have downside protection.

## Impact on founders and common shareholders

Full ratchet anti-dilution is punitive to common shareholders (founders, employees with common stock). In a down round:

- Preferred investors' conversion ratios expand.
- Common shareholders' ownership percentage shrinks.
- In extreme cases, a founder holding common stock might see their ownership diluted so severely that they are nearly wiped out, even though preferred investors are protected.

This is why founders often negotiate for weighted-average anti-dilution, which softens the blow. Full ratchet is more common in highly aggressive investor situations or when the founders are desperate.

## Exclusive vs. standard anti-dilution

**Exclusive anti-dilution**: Only preferred shareholders have protection. Common shareholders bear the full dilution of down rounds.

**Standard (broad-based)**: Anti-dilution is calculated using all shares, including common, options, and warrants. More equitable but less protective to preferred holders.

## Scope and carve-outs

Anti-dilution provisions typically carve out certain issuances that don't trigger adjustment:

- **Stock splits and consolidations**: These are cosmetic; no anti-dilution trigger.
- **Employee equity grants**: Up to a specified pool (e.g., 10% of shares for employee equity). No trigger unless exceeded.
- **Equipment financing**: Shares issued in equipment-backed financing are often exempt.
- **Strategic issuances**: Shares issued for partnerships, strategic investments, or acquisitions may be exempt if approved by the board or preferred holders.

Example carve-out language: "Anti-dilution provisions do not apply to (a) stock splits, (b) shares issued under an approved employee equity plan up to 15% of outstanding shares, or (c) shares issued for bona fide acquisitions approved by holders of a majority of preferred shares."

## Pricing mechanics: what triggers anti-dilution

Anti-dilution is triggered by issuances at a **below-investment-price** (below the investor's original purchase price). Example:

- Series A investor bought at $10/share.
- Series B issued at $8/share → triggers anti-dilution.
- Series B issued at $12/share → no trigger (not a down round for Series A).

If Series B is above Series A's price, the Series A investor does not trigger anti-dilution (they're not diluted). Series B is the one potentially at risk if there's a Series C down round.

## Mathematical impact of full ratchet

Full ratchet can be harsh. If a company raises at lower and lower prices across multiple rounds:

- Series A: $10/share
- Series B: $5/share (full ratchet, Series A → $5 conversion price)
- Series C: $2/share (full ratchet, Series A and B both → $2 conversion price)

By Series C, the Series A investor (who invested $10/share) is converting at 1/5th the original price. The conversion ratio expanded 5x. If there are 10M common shares and the Series A investor has 1M preferred, their conversion from 1M to 5M common is massive dilution to founders.

## Negotiated alternatives

Rather than accepting mechanical full ratchet, investors and founders sometimes negotiate:

- **Weighted-average with caps**: "Weighted-average, but conversion price cannot go below X."
- **Tiered anti-dilution**: "Full ratchet if down round is >20% below Series A; weighted-average if <20%."
- **Conditional carve-outs**: "Anti-dilution applies unless the company raises at Series C price with VC approval."

These nuanced provisions are common in Series B and later rounds, where founders have more negotiating power.

## Real-world example: Down round scenario

**Series A** (Year 1): Startup raises $10M at $10/share valuation ($100M post-money). Series A investor owns 10% (10M shares / 100M total).

**Series B** (Year 3): Company has grown but markets are weak. Series B investor invests $5M at $5/share valuation ($50M post-money). Company issues 1M new Series B shares.

**Full ratchet impact on Series A**:
- Old conversion ratio: 1M Series A → 1M common
- New conversion ratio: 1M Series A → 2M common (1:2)
- New pro-rata ownership: 2M common / (existing common + existing preferred + 1M Series B) = roughly 20% (up from 10%)

Series A investor's ownership doubled at the expense of founders and common shareholders.

**Weighted-average impact on Series A**:
- New conversion ratio: ~1.33M common (1:1.33)
- New pro-rata ownership: ~13%

Series A investor gains protection but not full doubling.

## Legislative and regulatory context

Anti-dilution provisions are negotiated and customized per deal—there is no standard form. However:

- **SEC** does not regulate anti-dilution directly (these are private contract terms).
- **State corporate law** allows broad freedom to customize share terms, including anti-dilution.
- **NVCA model documents** (National Venture Capital Association) provide templates with weighted-average anti-dilution as a default.

## Derivative impact: earnings per share (EPS)

When anti-dilution triggers, the investor's conversion share count increases. For accounting purposes, this is often reflected in "diluted EPS" calculations (which assume all convertible securities are exercised). Large anti-dilution adjustments can have large impacts on reported diluted EPS.

## Covenant vs. anti-dilution

Anti-dilution provisions are sometimes conflated with covenants:

- **Anti-dilution**: Automatic adjustment to conversion price/ratio upon a triggering event (down round).
- **Covenant**: A contractual obligation or restriction on the company (e.g., "the company shall not issue shares below $X without prior preferred holder approval").

A company might covenant not to issue below a certain price, eliminating the anti-dilution trigger. Or it might allow dilution but not trigger anti-dilution if approved by preferred holders.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/preferred-stock/">Preferred Stock</a> — the typical holder of anti-dilution rights.</li>
  <li><a href="/wiki/common-stock/">Common Stock</a> — diluted by anti-dilution triggered on preferred.</li>
  <li><a href="/wiki/share-issuance/">Share Issuance</a> — the triggering event (down-round issuance) that activates anti-dilution.</li>
  <li><a href="/wiki/junior-preferred/">Junior Preferred Stock</a> — may have different anti-dilution terms than senior preferred.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/venture-capital-fund/">Venture Capital Fund</a> — primary negotiator of anti-dilution terms.</li>
  <li><a href="/wiki/capital-structure-arbitrage/">Capital Structure Arbitrage</a> — sometimes exploits asymmetric anti-dilution protections.</li>
  <li><a href="/wiki/dilution/">Dilution</a> — the phenomenon that anti-dilution provisions address.</li>
</ul>
</div>
