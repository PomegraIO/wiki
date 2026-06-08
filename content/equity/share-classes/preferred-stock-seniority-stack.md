---
title: "Preferred Stock Seniority Stack in a Startup Cap Table"
description: "Preferred stock seniority stack determines payout order in a startup cap table: Series A sits above B, B above C, and all sit above common stock."
keywords:
  - preferred stock seniority
  - startup cap table
  - series a b c preferred
  - liquidation preference
  - waterfall payout
  - common stock junior
---

*A **preferred stock seniority stack** is the layered hierarchy of claim rights on a startup's assets and cash. Series A preferred sits in one layer, Series B in another above it, Series C above that, and common stock at the bottom. When the company is acquired or liquidated, cash flows up through these layers: the most senior preferred gets paid first, then the next tier, and so on until the money runs out. Common shareholders—founders and early employees—often get nothing when proceeds fall short of the stack's total preferences, even if the company was nominally worth billions.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Preferred Stock Seniority Stack — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for equity and ownership." />

<div class="wiki-infobox-caption">Each funding round creates a new tier; earlier investors sit above later ones.</div>

|   |   |
|---|---|
| **Typical order** | Series A → B → C → common stock (most to least senior) |
| **Triggers** | Liquidation, acquisition, or forced dividend; rarely in normal operations |
| **Payout** | Senior holders usually get their full preference; juniors get leftovers |
| **Multiple** | 1.0x (non-participating) means preference equals investment; more means upside too |
| **Scenario** | $100m exit, $10m Series A pref, $6m Series B → A gets full $10m, B gets remaining $90m |
| **Common stock** | Often worthless if preferred preferences exceed exit value |

</aside>

## Why the stack exists: protecting investors

A startup is high-risk. Most fail or return modest multiples. Venture investors and later-stage preferred shareholders need protection. They negotiate liquidation preferences—contractual promises that if the company is sold, liquidated, or wound down, their shares get paid in a specific order before junior shares.

This is not greed. It's risk-adjusted return. A Series A investor putting $5 million into a seed-stage company with a $20 million post-money valuation owns 20%. If the company is sold two years later for $40 million, a simple pro-rata split would give them $8 million—a 60% return. But if the company is sold for $10 million, they'd get $2 million, a 60% loss. A liquidation preference of 1.0x non-participating says: "If this exit is less than $5 million, I get back my $5 million first; anything left goes to common." The preference protects against the downside.

Later rounds—Series B, C—negotiate their own preferences. Series B might insist on a 1.0x non-participating preference for their $15 million check. So the seniority stack is: Series A ($5m preference) sits above Series B ($15m preference) sits above common stock.

This is where the term "preferred" comes from: these shareholders have preferred claims, not because they are favored by the company, but because they have contractual rights over junior claims.

## Waterfall mechanics: how proceeds flow

An acquisition or liquidation triggers a waterfall. Proceeds flow through the seniority stack in order:

1. Holders of the most senior class get paid to their preference
2. Any remaining cash flows to the next tier down
3. The process repeats until cash runs out

**Example:**

- Series A: 1,000 shares, $1 preference per share → **$1,000 total preference**
- Series B: 2,000 shares, $0.75 preference per share → **$1,500 total preference**
- Common: 3,000 shares, no preference
- **Sale price: $2,000 total**

Waterfall:
- Series A: Gets paid first. They want $1,000. Remaining: $2,000 − $1,000 = $1,000
- Series B: Gets paid next. They want $1,500, but only $1,000 remains. They get $1,000
- Common: Gets $0

Series A holders walk away with $1 per share, a breakeven or modest loss. Series B holders get $0.50 per share, a loss. Common shareholders get nothing—they now own shares in a company that sold for less than the preferred preferences, a phenomenon called being "underwater" or "out of the money."

Change the sale price to $3,000:
- Series A: Paid $1,000 in full. Remaining: $2,000
- Series B: Gets $1,500 in full. Remaining: $500
- Common: Gets $500 total, $0.17 per share

## The founder experience: common stock in the stack

This is where founders and early employees often suffer. They typically hold common stock. If they did not negotiate for a board seat or information rights, they may not even know the exact liquidation preferences. A founder who bootstrapped the company, hired the first team, and grew it from idea to $500 million "valuation" may wake up after an acquisition to learn that Series D preferred had a 2.0x participating preference, Series C had 1.0x non-participating, and Series B and A had the same. The founder's common stock is worthless.

This is not fraud; it is contractual terms agreed to at each fundraising. But it is common for founders to be surprised or embittered when they understand, retroactively, that they needed to have fought harder for board seats, anti-dilution protection (e.g., a lower preference for later rounds), or conversion rights into preferred stock as the company grew.

## Non-participating vs. participating preferences

The examples above assume **non-participating** preferences: once you're paid your preference, you're done, and the remaining proceeds go to the next tier. But many Series B and later prefer **participating** or **double-dip** preferences: you get your preference, and then you also participate pro-rata in the remaining cash.

Example (continuing the $2,000 sale):

- Series A: 1,000 shares, 1.0x non-participating pref of $1,000. Remaining: $1,000.
- Series B: 2,000 shares, 1.0x **participating** pref of $1,500.

Now Series B gets their full $1,500 preference, and then also participates pro-rata in the remaining $500 (using their 2,000 shares out of 5,000 total non-Series-A shares). They get an extra $500 × (2,000 / 5,000) = $200. Series B receives $1,700 total.

Common and Series A get the remaining $300, split pro-rata: $300 × (3,000 / 3,000) = $300 to common, $0 to Series A (they already had their preference).

Participating preferences inflate the seniority advantage and further squeeze junior holders. Founders and employees often lose out completely when Series C or D negotiations include heavy participating preferences.

## Drag-along and call mechanics

Seniority doesn't stop at waterfall mechanics. Many preferred-stock agreements include **drag-along rights**: if holders of a super-majority (often two-thirds or three-quarters) of preferred stock approve a sale, they can force common shareholders and junior preferred to sell too, at the same price per share. This prevents a dissident founder with common stock from blocking a sale that the VCs want, or from negotiating a better deal. It is a powerful tool for investors and has closed companies against founder resistance.

Conversely, some preferred stock includes **call rights**: the company can buy back shares at par (the original investment price) under certain conditions, effectively canceling shares if a later-stage investor objects to their terms.

## Building with this in mind

Founders who understand the seniority stack can negotiate better terms:

- Push for common-stock conversion rights: as the company raises Series B and beyond, set terms that let founders convert their common to preferred shares to protect themselves.
- Seek information rights and board seats: even with common stock, a seat at the table gives you early warning of preference terms.
- Negotiate for pari-passu or non-participating preferences in later rounds: if you're raising Series B, resist Series B investors' demands for 2.0x participating preferences; try for 1.0x non-participating, which limits the squeeze.
- Consider anti-dilution: carve-outs for employee options (ESOP pools) protect the option pool from dilution and align incentives.

Understanding the seniority stack also helps when choosing between job offers at startups. If you're an early employee weighing equity compensation, ask about the cap table, the series of preferred stock, and their preferences. Equity in a company with $10 million raised at a $50 million post-money valuation is very different from equity in a company with $100 million raised at a $500 million valuation—the latter faces a much higher bar before common stock is worth anything.

## See also

<div class="wiki-seealso">

### Closely related

- [Preferred stock](/preferred-stock/) — the instrument itself and its general structure
- Liquidation preferences — the contractual engine of the waterfall
- [Common stock](/common-stock/) — the junior class in the stack
- [Acquisition](/acquisition/) — the most common trigger for waterfall payouts
- [Share buyback](/share-buyback/) — an alternative to acquisition or liquidation, with its own payout rules
- [Board of directors](/board-of-directors/) — entity that often approves seniority terms

### Wider context

- [Initial public offering](/initial-public-offering/) — rarely affected by seniority because all preferred typically converts to common at IPO
- Valuation — the headline number that masks the seniority complexity
- [Due diligence](/due-diligence/) — the process of uncovering cap tables and preferences during a transaction
- Venture capital — the ecosystem that invented and propagates seniority stacks
- [Merger](/merger/) — another form of transaction triggering waterfall mechanics

</div>
