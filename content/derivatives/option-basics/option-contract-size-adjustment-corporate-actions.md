---
title: "How Option Contract Size Changes After Stock Splits and Mergers"
description: "Learn how option contracts adjust for stock splits, reverse splits, and mergers—what changes in strike price, deliverable shares, and contract multipliers."
keywords:
  - how option contracts adjust for stock splits
  - option adjustment stock split
  - options expiration merger
  - contract adjustment corporate actions
  - stock split options multiplier
image: /svg/derivatives.svg
---

*When a company splits its stock or merges with another, the [options](/option/) trading on it don't simply vanish—the exchange's clearinghouse adjusts the contract terms to prevent windfall gains or losses. Understanding these adjustments matters for anyone holding long or short options through a corporate action.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Option Contract Adjustments — key facts</div>

<img src="/svg/derivatives.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Corporate actions trigger mechanical resets to option multipliers, strike prices, and sometimes deliverable share counts.</div>

|   |   |
|---|---|
| **Stock split (2:1)** | Deliverable shares double; strike price halves |
| **Reverse split (1:2)** | Deliverable shares halve; strike price doubles |
| **Cash dividend** | No adjustment (ordinary); options trade ex-dividend |
| **Merger (fixed ratio)** | Option converts to equivalent position in acquirer stock |
| **Spin-off** | New contract(s) covering both parent and spun-off entity |
| **Who decides** | FINRA, OCC, or exchange rulebook for that market |

</aside>

## Why adjustments exist

Before any automatic adjustment, imagine a 2:1 stock split. A call option to buy 100 shares at $50 stays on the books unchanged—but the underlying stock just halved in price per share, and there are twice as many shares now. A holder would get a windfall: they'd buy shares at artificially cheap strike, or a seller would face an outsized loss. The clearinghouse standardizes the adjustment so that option holders and sellers face the same economic outcome *after* the corporate action as they faced *before*.

This neutrality principle governs every adjustment. The exchange's rule committee publishes adjustment bulletins before the event, specifying exactly what changes. In the U.S., the [Options Clearing Corporation (OCC)](/option/) issues these rulings; other markets have equivalent bodies.

## Stock splits and reverse splits

A **stock split** divides each share into multiple shares at a proportionally lower price. In a 2:1 split, one share becomes two; the price drops roughly in half. For options:

- **Multiplier increases**: A contract representing 100 shares (the standard U.S. multiplier) becomes one representing 200 shares.
- **Strike price halves**: A $50 strike becomes $25.
- **Number of contracts unchanged**: You still own one contract, but it now covers twice as many shares.

A **reverse split** (or stock consolidation) combines shares. In a 1:2 reverse split, two shares merge into one. The price roughly doubles:

- **Multiplier decreases**: A 100-share contract becomes 50 shares.
- **Strike price doubles**: $50 becomes $100.
- **Fractional shares handled**: If you hold an odd number of contracts, settlement may involve a cash adjustment instead of fractional shares.

The ratio always scales inversely: if shares multiply by a factor, the strike divides by that factor, and vice versa. The net effect is that an option's intrinsic and time value remain economically neutral—you have the same claim on the same economic stake, just expressed differently.

## Cash and stock dividends

**Cash dividends** do not trigger adjustments under standard U.S. rules. Instead, option contract holders do not receive the dividend; the option trades ex-dividend, and the stock price drops by roughly the dividend amount on the ex-date. This protects sellers from paying out cash they never contracted for. A holder of calls is indirectly penalized (lower stock price eats into call value), but the contract terms stay fixed.

**Stock dividends**—when a company distributes additional shares as a dividend rather than cash—do trigger adjustments. A 5% stock dividend (0.05 shares per existing share) increases the multiplier and adjusts the strike proportionally, similar to a stock split.

## Mergers, acquisitions, and reorganizations

When two companies merge under a fixed exchange ratio—say, Company B acquires Company A at a ratio of 1.5 shares of B for each share of A—options on Company A must be adjusted or converted:

- **Survivor stock substitution**: Each option on Company A converts to an option on Company B's stock, with the multiplier and strike adjusted by the exchange ratio.
- **Cash merger**: If the deal is all-cash, the option may become a cash-settled contract that pays out the difference between the acquisition price and strike.
- **Mixed deals**: Stock-and-cash mergers may result in a split adjustment or a cash settlement component.

The OCC publishes a "notification" well before the merger closing, specifying the exact adjustment. Traders should monitor corporate action calendars closely, as the window between announcement and final terms can create uncertainty—some options may trade on multiple valuation assumptions until the deal closes.

## Spin-offs and special dividends

A **spin-off** creates a new independent company from a division of the original. The original shareholders receive shares in the new entity. Options on the original stock must be adjusted:

- Both the original and new company become deliverable, or
- New option contracts are created to cover the spun-off entity, with original contracts adjusted to exclude the spun-off value.

The OCC typically creates two separate contracts, each covering one entity, and resets the original multiplier to reflect the reduced claim. A holder of one original call now holds economically equivalent calls on both entities—a position that can be worth more, less, or the same depending on how the market values the newly independent companies.

## Fractional shares and settlement

When an adjustment would create fractional contract multipliers—say, a 3:2 split on an option contract—the OCC has standardized rules:

- **Rounding to whole shares**: Multipliers round to the nearest whole share to maintain clarity.
- **Cash in lieu**: If rounding cannot work (odd number of shares), the contract may settle in cash equal to the fractional share value.
- **No fractional contracts in the U.S.**: Standard U.S. equity options always represent whole-number multipliers, so cash adjustments are common in odd-ratio splits or spinoffs.

A holder discovering fractional entitlements should expect a small cash adjustment at settlement, separate from the normal option cash flow.

## Practical impact on open positions

For a **call holder**, a stock split is neutral: you can still buy shares at the original economic strike, just twice as many of them (at half the per-share price). The [delta](/delta/), [gamma](/gamma/), and [theta](/theta/) of the position remain numerically identical. The option remains valuable if the stock rises above the adjusted strike.

For a **put holder**, the same neutrality applies: you can sell at the adjusted strike. However, a reverse split *increases* the strike price in dollar terms, which can shift whether the option ends up in-the-money, and liquidity may dry up on contracts with unusual multipliers.

**Short option sellers** face the mirror image: they benefit from neutral adjustments too, since they collected [premium](/option-premium/) based on the original economic stakes.

**Practical warning**: Liquidity sometimes concentrates on the original, unadjusted contracts during the adjustment window. After the corporate action closes, only the adjusted contracts trade actively. This can create a forced squeeze for holders trying to liquidate odd or unusual positions—timing the exit before the event is often wise.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — fundamental concepts, buyer and seller roles, premium and [intrinsic value](/intrinsic-value/)
- [Delta](/delta/) — measures sensitivity to stock price moves; unchanged by pure splits
- [Expiration date](/expiration-date/) — standard settlement dates; extended or moved during certain corporate actions
- [Stock split](/stock-split/) — the underlying corporate action from an equity perspective
- [In-the-money](/in-the-money/) — strike, current price, and whether an option will be exercised

### Wider context

- [Derivatives hedging](/derivatives-hedging/) — how options are used to protect positions
- [Merger](/merger/) — corporate acquisition mechanics and deal closure
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — oversees U.S. option market rules and clearinghouse standards

</div>
