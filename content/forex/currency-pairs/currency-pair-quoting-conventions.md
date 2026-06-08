---
title: "Currency Pair Quoting Conventions"
description: "The market conventions that determine which currency appears first in a forex pair notation and the logic behind non-standard inversions."
keywords:
  - currency pair notation
  - forex pair convention
  - base currency quote currency
  - currency pair ordering
  - inverted pairs
image: "/svg/forex.svg"
---

*In forex notation, a **currency pair** is written as two three-letter codes separated by a slash—for example, EUR/USD. The first currency (base) is the unit being quoted; the second currency (quote) is the value in which it is priced. The order is not arbitrary: market convention sets it, and traders must respect the standard or risk confusion and botched trades. Some pairs, however, are traded inverted by historical convention, testing even experienced traders.*

## Base and quote: the fundamental structure

When you see EUR/USD at 1.0850, you are reading: one euro costs 1.0850 US dollars. The euro is the base; the dollar is the quote currency. If the rate moves to 1.0900, the euro has strengthened (it now costs more dollars).

Conversely, if you see GBP/USD at 1.2650, one British pound costs 1.2650 dollars. If the rate rises to 1.2700, sterling has strengthened.

The base/quote structure has a mathematical consequence: if you know EUR/USD (1.0850) and USD/GBP (0.7900), you can calculate EUR/GBP by dividing: 1.0850 ÷ 0.7900 = 1.3734. This is why the base/quote order matters—it determines whether you divide or multiply when chaining conversions.

## The hierarchy of conventions

The forex market has developed a de facto hierarchy for which currency comes first. It is not written down in law but is observed nearly universally because trading on the wrong convention leads to instant confusion and losses.

**The US dollar comes second (except for a few exceptions).** EUR/USD, GBP/USD, AUD/USD, NZD/USD, CAD/USD are the standard major pairs. The dollar is always quoted, never the base.

**Among non-dollar pairs, the euro typically comes first.** EUR/GBP, EUR/JPY, EUR/CHF are standard. If someone mentions a pound-yen cross, the market interprets it as GBP/JPY, but in most contexts, traders would express it as EUR/JPY first.

**Commodity currencies (CAD, AUD, NZD) usually come after the dollar.** You say USD/CAD (Canadian dollar per US dollar), not CAD/USD, because the Canadian dollar is historically quoted against the US dollar in commodity markets, not the reverse.

**The Japanese yen comes last in most pairs.** USD/JPY, EUR/JPY, GBP/JPY—the yen is the quote, not the base. This is a historical convention rooted in the yen's historical role and [central bank](/central-bank/) policy.

## The exceptional inversions

Some pairs are traded inverted by convention, even though this violates the hierarchy above. This creates a trap for newcomers.

**USD/CHF (Swiss franc).** The franc is a major currency, often traded against the dollar. But the market standard is USD/CHF—not CHF/USD—making the franc the quote. There is no deep reason; it is simply how the market evolved.

**GBP/USD (British pound).** You might expect pounds to come second, like other non-dollar currencies. But historically, sterling was the dominant global currency, and the convention locked in as GBP/USD, making pounds the base. The pound was first, the dollar followed.

**XAU/USD (gold in US dollars).** Gold is quoted in dollars, making USD the quote—but the convention is XAU/USD (gold/dollar), not the other way around. Traders speak of "dollar weakness pushing gold up" because gold is in the numerator.

**GBP/JPY, AUD/JPY, EUR/JPY, GBP/CHF.** These crosses follow the convention that the yen and franc come last, even though there is no overriding global hierarchy. GBP/JPY is standard; you would not say JPY/GBP.

These inversions are second nature to professional traders but catch newcomers off guard. If you confuse GBP/USD and USD/GBP—thinking they are the same pair inverted—you will place trades in the opposite direction and suffer losses.

## Bid, ask, and directional clarity

The [bid-ask spread](/bid-ask-spread/) reinforces the base/quote structure. When a dealer quotes EUR/USD at 1.0850/1.0851, that is shorthand:

- **Bid (1.0850):** The dealer will buy euros from you at 1.0850 dollars per euro.
- **Ask (1.0851):** The dealer will sell euros to you at 1.0851 dollars per euro.

If the pair moves to 1.0900/1.0901, the euro has strengthened and the spread (1 pip) is unchanged. If you had shorted EUR/USD at 1.0850, you now have a loss because euros are more expensive.

Inverting the pair—quoting as USD/EUR (0.9215/0.9216)—inverts the bid-ask too. The bid and ask flip roles, and a trader who does not adjust direction will hedge the wrong way.

## Conventions in corporate and payment systems

In corporate finance, [accounts payable](/accounts-payable/) and [accounts receivable](/accounts-receivable/) often use different conventions. An American importer buying goods from Japan might see the invoice in JPY, but internally track it as USD/JPY. A European exporter selling to Canada might invoice in CAD and track it as CAD/EUR (inverted from the major pair convention USD/CAD).

The underlying economic exposure is the same, but notation confusion can creep in. Best practice is to always specify clearly: "we are short 1 million euros" or "we are long yen" rather than relying on the pair notation alone.

## Why these conventions matter for traders

For a [trader](/algorithmic-trading/) or [broker](/broker/), pair notation errors are costly. A trader intending to buy EUR/USD might accidentally short it if they misread the order. A [market maker](/market-maker-trading/) who quotes the wrong pair to a client faces an arbitrage loss.

Algorithmic trading systems must encode the right conventions; a bot trading GBP/USD but receiving a quote for USD/GBP will immediately lose money. Exchanges and trading platforms are built around these conventions; every [order](/market-order/) routing system depends on them.

## Modern consensus and technological encoding

Today, most trading systems and data feeds use the ISO 4217 currency code standard (three-letter codes: EUR, USD, GBP, JPY, etc.) and encode the pair conventionally in the code. A data feed that broadcasts "EURUSD" or "EUR/USD" means the pair in the standard order. Platforms, APIs, and real-time pricing services all follow this.

Still, confusion arises when traders from different markets or systems communicate verbally. A conversation between a Tokyo desk and a London desk about "dollar-yen" can be ambiguous—does one mean USD/JPY or JPY/USD? The safer phrasing is "dollar per yen" or "yen per dollar," which specifies direction unambiguously.

## See also

<div class="wiki-seealso">

### Closely related

- [Exotic Currency Pairs](/exotic-currency-pairs/) — specialized non-standard pairs with their own quoting rules
- [Minor Currency Pairs](/minor-currency-pairs/) — crosses between major currencies
- [Pip and Pipette](/pip-and-pipette/) — the unit of price movement in a quoted pair
- [Bid-Ask Spread](/bid-ask-spread/) — the cost difference between buying and selling
- [Market Order](/market-order/) — executing a trade in a specific pair direction
- [Over-the-Counter Market](/over-the-counter-market/) — where forex pairs are traded decentrally
- [Spot Exchange Rate](/spot-exchange-rate/) — the immediate exchange rate for a pair

### Wider context

- [Currency Risk](/currency-risk/) — why traders and businesses care about pair directions
- [Interest Rate](/interest-rate/) — influences which pairs are quoted and traded
- [Central Bank](/central-bank/) — policy shapes pair liquidity and convention
- [Broker](/broker/) — intermediaries who quote and execute in standard pair notation

</div>
