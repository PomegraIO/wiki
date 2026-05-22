---
title: "Butterfly Shift"
description: "A yield curve movement where short and long-term rates change more than medium-term rates, creating a concave dip or bulge in the curve."
keywords:
  - butterfly shift yield curve
  - yield curve shape
  - steepening flattening
  - intermediate rates
---

*A **butterfly shift** in the [yield curve](/wiki/yield-curve/) occurs when short and long-term [interest rates](/wiki/interest-rate/) move upward or downward more than intermediate (5–10 year) rates, causing the curve to twist into a concave shape—either a dip (if short and long rates fall relative to medium) or a bulge (if short and long rates rise relative to medium).*

The term "butterfly" comes from the shape the curve resembles: a dip in the middle resembles butterfly wings spreading outward, or a bulge in the middle resembles wings folding together. This is distinct from a [steepening](/wiki/curve-steepening-commodity/) (long rates rise faster than short) or [flattening](/wiki/curve-flattening/) (long rates fall faster than short) move. A butterfly describes the relative movement of three points on the curve: short, intermediate, and long.

<aside class="wiki-infobox">

| Scenario | Short 2Y | Medium 5Y | Long 10Y | Curve shape | Typical driver |
|---|---|---|---|---|---|
| **Positive butterfly** | ↓ | ↑ | ↓ | Concave dip | Flight-to-quality into safety |
| **Negative butterfly** | ↑ | ↓ | ↑ | Concave bulge | Demand for medium-term bonds |
| **Parallel shift** | ↑ | ↑ | ↑ | Unchanged shape | Inflation shock, rate hike cycle |
| **Steepening** | ↓ | ↔ | ↑ | Slope increases | Growth recovery, short rates capped |

</aside>

## Positive butterfly: the concave dip

A **positive butterfly** (also called a bullet) occurs when short and long rates fall and intermediate rates rise—or, more commonly, when the 10-year and 2-year rates move down while the 5-year rate stays firm or rises.

**Example during market stress** (e.g., March 2020, COVID panic):
- 2-year yield falls from 1.5% to 0.3% (investors fleeing to safety, expecting the Fed to cut rates).
- 5-year yield stays around 0.5% (middling demand, mixed outlook).
- 10-year yield falls from 1.9% to 0.6% (flight-to-quality, long-term bonds seen as ultimate safe havens).

The result: the curve dips between 2 and 10 years, with 5-year rates higher than both 2-year and 10-year rates. This creates a concave (upward-bowed) shape at the intermediate end.

**Why it happens**: In a crisis, investors flee to the longest-duration bonds (10-year Treasurys) for maximum safety. Simultaneously, the [Federal Reserve](/wiki/federal-reserve/) signals emergency rate cuts, pushing 2-year expectations sharply lower. The 5-year sits awkwardly between the two dynamics, pulled neither fully downward (like the 2-year) nor fully downward (like the 10-year's flight-to-quality).

## Negative butterfly: the concave bulge

A **negative butterfly** occurs when short and long rates rise and intermediate rates fall—or when the 5-year rate rises relative to both 2-year and 10-year rates.

**Example during a mid-cycle slowdown**:
- 2-year yield rises from 0.5% to 0.8% (market expects the Fed to keep rates higher for longer).
- 5-year yield falls from 1.2% to 1.0% (recession fears dampening medium-term growth expectations).
- 10-year yield rises from 1.5% to 1.7% (inflation expectations support long-term rates).

The result: the curve bulges upward at the 5-year point, with 5-year rates highest and 2-year and 10-year rates lower. This creates a concave (downward-bowed) shape.

**Why it happens**: The 5-year occupies an awkward zone—long enough that some investors see recession risk and demand yield concessions, but short enough that it is sensitive to near-term [Federal Reserve](/wiki/federal-reserve/) policy. If the Fed is holding rates steady (short rates firm) and long-term growth is still positive (long rates supported), the 5-year rate can be caught in a squeeze, moving lower than both.

## Trading the butterfly

Butterfly moves create **butterfly spreads**—a term structure trade that profits from changes in the curve's shape.

A **butterfly spread** typically involves:
- **Long** 2-year and 10-year bonds (short the curve at the extremes).
- **Short** 5-year bonds (short the middle).

If a positive butterfly occurs (5-year yield falls relative to 2-year and 10-year), the trader profits because they are short the 5-year (benefit from yield rise) and long the 2-year and 10-year (benefit from yield fall).

The Greeks of a butterfly trade:
- **Gain from a positive butterfly**: If 5-year yields rise 20 bps while 2-year and 10-year yields fall 10 bps, the trade profits.
- **Loss from a steepening**: If the curve steepens uniformly (all yields rise, but long more than short), the trade loses because the long 10-year position suffers.
- **Duration hedge**: Because the trade is duration-neutral (long 2 and 10, short 5), it profits from shape changes without directional [interest rate risk](/wiki/interest-rate-risk/).

## Why butterflies happen: structural and cyclical drivers

**Structural**: The Treasury market is segmented. [Pension funds](/wiki/pension-obligation/) and insurers demand long-dated bonds for liability matching. [Banks](/wiki/central-bank/) focus on shorter maturities. Foreign central banks (China, Japan) buy long bonds. [Money market](/wiki/money-market-fund/) funds stay in short-maturity instruments. These preferences create natural imbalances. If foreign demand for long bonds surges, long yields fall and a positive butterfly develops.

**Cyclical**: During a recession, investors fear both very short-term rollover (hence short rates fall as the Fed cuts) and medium-term growth (hence 5-year rates are squeezed), while long-term Treasury bonds benefit from a "safe haven" bid. This classic recession pattern produces a positive butterfly.

During late-cycle inflation (e.g., 2021–2022), the [Federal Reserve](/wiki/federal-reserve/) hiked aggressively, but long-dated bonds held value because inflation was expected to cool. Short rates rose sharply (early hikes), 10-year rates rose moderately (some inflation expectations priced in), and 5-year rates were caught in the middle—a mixed dynamic creating butterfly-like distortions.

## Historical examples

**March 2020 (COVID crash)**: The classic positive butterfly. 2-year yields fell >120 bps, 10-year yields fell ~60 bps, and the 5-year actually rose initially before crashing. The curve dipped sharply at the intermediate end.

**2019 (US-China trade war, Fed cuts cycle)**:  The Fed began cutting rates unexpectedly in July. Short rates fell sharply; long rates fell modestly (term premium evaporated, but growth concerns were moderate). A positive butterfly formed as the 5-year was caught between declining short rates and anchored long rates.

**2022 (Fed hiking cycle, rising-rate environment)**: Short rates rose +425 bps, intermediate rates rose +250 bps, long rates rose +150 bps. This was less a butterfly and more a parallel shift with a steepening gradient, but there were moments when the 5-year lagged both extremes, creating brief negative butterflies.

## Implications for bond portfolio managers

A portfolio manager holding intermediate-maturity bonds (5–7 year range) faces butterfly risk. If market conditions create a negative butterfly, intermediate yields rise relative to long yields, harming the manager's position.

Hedges:
- **Buy long bonds, sell short bonds**: Flattens the portfolio's duration exposure to butterfly risk.
- **Monitor [carry](/wiki/carry-cost-forex/) vs. [roll-down](/wiki/roll-down-return/) returns**: In a positive butterfly environment, short and long bonds carry negative [roll-down](/wiki/roll-down-return/) (yields rising as the bonds mature), while intermediate bonds may experience positive [roll-down](/wiki/roll-down-return/), creating asymmetric losses.

## Why economists care about butterflies

The [yield curve](/wiki/yield-curve/) shape is a signal of economic expectations. A positive butterfly suggests fear of near-term recession (short rates down) with eventual stability (long rates down but less than short). A negative butterfly can signal a mid-cycle slowdown with eventual recovery (short rates up, long rates up, intermediate rates uncertain).

Understanding butterfly moves helps [central banks](/wiki/central-bank-policy-tools/) fine-tune [policy](/wiki/monetary-policy/). If the [Federal Reserve](/wiki/federal-reserve/) wants to steepen the curve but the market is generating a butterfly instead, it suggests market participants see a different rate path than the Fed projects.

## Quantifying butterflies: the butterfly index

Traders use a **butterfly index** to quantify the shape:

Butterfly = (2-year yield + 10-year yield) / 2 − 5-year yield

A positive butterfly index means the 5-year is below the midpoint of the 2-year and 10-year. A large negative value means the 5-year is above the midpoint.

Values greater than ±15 bps are considered extreme and often mean-revert, presenting trading opportunities.

<div class="wiki-seealso">

### Closely related
- [Yield Curve](/wiki/yield-curve/) — Relationship between bond yields and maturity
- [Curve Flattening](/wiki/curve-flattening/) — Long yields fall faster than short yields
- [Curve Steepening Commodity](/wiki/curve-steepening-commodity/) — Long yields rise faster than short yields
- [Butterfly Spread](/wiki/butterfly-spread/) — Options or futures trade exploiting curve shape changes

### Wider context
- [Interest Rate](/wiki/interest-rate/) — Price of borrowing; drives bond yields
- [Term Premium](/wiki/term-premium/) — Extra yield demanded for longer-duration bonds
- [Yield Curve Inversion](/wiki/yield-curve-inversion/) — When short yields exceed long yields, often precedes recession
- [Central Bank Policy](/wiki/central-bank-policy-tools/) — Fed interest rate decisions that anchor curve levels

</div>
