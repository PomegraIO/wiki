---
title: "Non-Participating vs Participating Preferred at Exit"
description: "Non-participating preferred returns capital first then exits; participating preferred gets capital back plus a share of profits, potentially worth much more at sale."
keywords:
  - non-participating preferred
  - participating preferred
  - preferred stock exit
  - liquidation preference
  - startup acquisition
---

*In a startup exit, the choice between **non-participating preferred** and **participating preferred** can be worth tens of millions of dollars to founders and early investors. Non-participating preferred investors get their money back first, then exit; participating preferred investors recoup their stake *and* then share in profits alongside common shareholders. A single worked example shows why venture investors now demand participation, and why founders must understand this before signing term sheets.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Preferred Share Structures at Exit — Key Facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">How liquidation preferences reshape who gets paid at a sale.</div>

|   |   |
|---|---|
| **Non-participating** | Returns capital first; investor exits after preference is satisfied |
| **Participating** | Returns capital first; then shares in remaining proceeds like common stock |
| **Payoff difference** | Dramatic for exits where sale price is 5–20x the preferred investment |
| **Market trend** | Participating is now standard in Series A and later rounds |
| **Impact on founders** | Participating preferred can reduce founder proceeds by 30–50% in large exits |

</aside>

## The Setup: A Numerical Example

Imagine a startup is acquired for $100 million. Here's the capital structure at the time of sale:

| Class | Shares | Price per share | Value |
|-------|--------|-----------------|-------|
| **Common (Founders)** | 10,000,000 | — | — |
| **Series A Preferred (VC)** | 2,000,000 | $10 | $20M preference |
| **Series B Preferred (VC)** | 1,000,000 | $25 | $25M preference |
| **Total accrued preferences** | — | — | **$45M** |
| **Remaining for common** | — | — | **$55M** |

The VC holds $45 million in total liquidation preferences. The founders hold common stock. Now the question: how are proceeds divided under each structure?

## Non-Participating Preferred: The Waterfall

Under a **non-participating** structure, the waterfall is simple:
1. Pay Series A investors their $20M preference.
2. Pay Series B investors their $25M preference.
3. Distribute *all remaining proceeds* ($55M) pro-rata to *common shareholders only*.

The Series A and Series B investors get their money back and nothing more—they "exit" after their preference is satisfied. In this scenario, the VCs together receive $45M. The $55M remainder goes to common holders (founders, employees, early backers) *pro-rata by share count*.

If founders own 80% of common shares, they receive 80% of $55M = $44M. The other 20% goes to other common holders.

**VC proceeds: $45M. Founder proceeds: $44M.**

This is rare today, but it was common in earlier rounds (Angels, Series A) ten years ago.

## Participating Preferred: The Double Dip

Under a **participating** structure, the same $100M sale is divided differently:

1. Pay Series A investors their $20M preference.
2. Pay Series B investors their $25M preference.
3. Take the remaining $55M and distribute it *pro-rata to all shareholders* (common *and* preferred) **based on fully-diluted share count**.

This means the Series A and Series B investors get their preference *and then participate in the leftovers as if they were common shareholders*.

The fully-diluted share count is:
- Founders (common): 10,000,000 shares
- Series A: 2,000,000 shares
- Series B: 1,000,000 shares
- **Total: 13,000,000 shares**

The $55M is split pro-rata: Series A gets (2M / 13M) × $55M = $8.5M extra. Series B gets (1M / 13M) × $55M = $4.2M extra.

**Series A total: $20M + $8.5M = $28.5M.**
**Series B total: $25M + $4.2M = $29.2M.**
**VC total: $57.7M.**

Founders get only the common holders' slice: (10M / 13M) × $55M = $42.3M.

**VC proceeds: $57.7M. Founder proceeds: $42.3M.**

The difference: **Founders lose $1.7M in this scenario.** But the gap widens dramatically in larger exits.

## A Larger Exit: The Multiplier Effect

Now imagine the startup sells for $200 million instead.

**Remaining after preferences: $200M - $45M = $155M.**

Under **non-participating**: Founders keep $155M (pro-rata 80% = $124M).

Under **participating**: $155M is split fully-diluted. Founders keep only (10M / 13M) × $155M = $119.2M.

**Founders lose $4.8M.**

But the difference is even more acute when exits are *smaller than the total preferences*.

## A Down Exit: When Preferences Bite Hardest

Suppose the startup sells for only $50 million—a down round from the $45M in accumulated preferences.

**Non-participating: Waterfall**
1. Series A gets $20M (their full preference).
2. Series B gets $25M (their full preference).
3. Nothing remains. Founders get $0.

**Participating: Still a waterfall**
1. Series A and Series B together get their $45M preference.
2. Remaining $5M is split fully-diluted: Founders get (10M / 13M) × $5M = $3.85M.

In a down exit, both structures hurt founders equally—preferences are paid in full, and common shareholders eat losses. But at small exits, the gap between participating and non-participating is minimal because there's little juice left after preferences anyway.

The real divergence shows up in large exits where the company dramatically outperforms the VC's $45M bet.

## Why Participating Is Now Standard

Modern investors (especially Series A and beyond) demand participating preferred because:

1. **Upside capture.** If the company becomes a multi-billion dollar exit, the VC wants to participate in the outsized returns, not cap their upside at the preference.
2. **Market standard.** After 2000 and the post-2008 risk-averse environment, terms hardened. Most LPs now expect their GPs to negotiate participation.
3. **Risk compensation.** Early VC is risky (90% of startups fail). Those who write large checks want participation to make the winners cover the losses from losers and failures.

**Non-participating** is now relegated to:
- Angel and early seed rounds (smaller money, less sophisticated terms).
- Rare, well-connected founders who negotiate hard.
- Some convertible notes or SAFEs (which avoid preference structure altogether).

## Cap on Participation: A Founder's Defense

Smart founders negotiate a **cap** on participation: the preferred investor receives their preference plus participation *up to a maximum multiple* (typically 3–5x their invested amount). Beyond that cap, they're treated like common shareholders.

Example: Series A invests $20M at $10 per share, so they own 2M shares. They negotiate a 3x cap. They get their $20M preference plus participation, but their total proceeds cannot exceed $60M. If the exit is $300M, their 3x cap kicks in at $60M, and the remaining proceeds split pro-rata to all shareholders—including the preference.

This structure rewards investors generously while capping their total take, leaving more for founders in mega-exits.

## See also

<div class="wiki-seealso">

### Closely related

- [Preferred stock](/preferred-stock/) — The security class whose structure we're unpacking
- [Liquidation preference](/liquidation-preference/) — The priority order that defines who gets paid first
- [Common stock](/common-stock/) — The opposite class, subordinate to preferred
- [Equity financing](/equity-financing/) — How startups raise rounds and grant preferences
- [Share buyback](/share-buyback/) — An alternative exit mechanism (though less common in VC exits)

### Wider context

- [Acquisition](/acquisition/) — The event triggering liquidation preference calculations
- [Valuation](/discounted-cash-flow-valuation/) — Underlying value that determines exit price
- [Merger](/merger/) — A variant of exit with similar waterfall mechanics
- [Initial public offering](/initial-public-offering/) — Another exit route where preferences matter

</div>
