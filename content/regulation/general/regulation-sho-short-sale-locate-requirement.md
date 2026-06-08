---
title: "Regulation SHO and the Short-Sale Locate Requirement"
description: "How SEC Regulation SHO requires brokers to locate shares and enforce close-out obligations before executing short sales, preventing naked shorting and market manipulation."
keywords:
  - regulation sho
  - short-sale locate requirement
  - locate requirement short selling
  - naked short selling
  - sec regulation sho
  - short sale rules
image: /svg/regulation.svg
---

*Regulation SHO is the SEC's framework for controlling abuses in [short-selling](/short-selling/), with the **locate requirement** as its centerpiece: before executing a short sale, a broker must reasonably locate (or have reasonable grounds to borrow) the shares the customer intends to deliver. This rule prevents "naked" short sales—sales executed without any arrangement to borrow shares—which can artificially inflate supply and distort prices. Combined with mandatory close-out rules, the locate requirement is the primary regulatory circuit-breaker on manipulative shorting.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Regulation SHO — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for regulation." />

<div class="wiki-infobox-caption">SEC rules that require pre-execution share location and same-settlement close-outs.</div>

|   |   |
|---|---|
| **Locate requirement** | Broker must locate or have reasonable grounds to borrow before short sale executes |
| **Timing** | Locate occurs before order execution (not after) |
| **Close-out** | Short seller must deliver shares by settlement date or face forced buy-in |
| **Naked shorting** | Illegal on equity securities; limited exceptions for market-makers |
| **Regulation** | [Securities-and-exchange-commission](/securities-and-exchange-commission/) (SEC); enforced with [FINRA](/finra/) rules |
| **Key dates** | Rule 10a-1 (short-sale uptick rule), Rule 10b-21 (locate rule) adopted 2005, tightened 2007 |
| **Penalty** | Forced buy-in, fines, trading halts, sanctions |

</aside>

## What Regulation SHO Is

**Regulation SHO**, adopted by the SEC in 2005 and refined in 2007, is a comprehensive set of rules designed to prevent fraud and manipulation in [short-selling](/short-selling/). The regulation addresses three core abuses: naked short sales (sales without borrowing arrangements in place), failure to deliver (FTD), and manipulation via short squeezes. The locate requirement is the primary mechanism that prevents naked shorting before it happens.

The rule applies to all equity securities traded in U.S. markets—stocks listed on NYSE, NASDAQ, and OTC markets. It does not typically apply to options, bonds, or most commodities, though similar locate rules exist in other regulatory schemes.

## The Locate Requirement: How It Works

Before a broker accepts a short-sale order from a customer, the broker must (or the customer must, depending on the broker's agreement) **reasonably locate** shares that can be borrowed. "Locate" means the broker has identified a specific source—often another brokerage, a [custodian](/custodian/), or a securities lending desk—that has agreed (or is likely to agree, contractually) to lend the shares.

The locate must happen *before* the order is executed, not after. This is the critical preventative step: it stops the trader from going short without any borrowing backstop.

### Three Levels of Locate

The SEC rule distinguishes three standards:

1. **Reasonable Grounds to Borrow** — The broker has reasonable assurance that it can borrow the shares by settlement date. This is the minimum standard for most institutions and is widely interpreted to mean the broker has checked an internal lending pool or signed a standby agreement with a lender.

2. **Actual Locate** — The broker has confirmed availability with a specific lender. For highly restricted or hard-to-borrow stock, this is the more stringent requirement, especially if the customer has a history of failing to deliver.

3. **Executed Locate (Market-Maker Exception)** — Market-makers have a narrow exemption: they may execute a short sale *without* a pre-execution locate, but must close-out their position by the end of the trading day (intraday locate). This exemption is designed to let market-makers provide liquidity without requiring pre-trade share checks.

## Why Locate Requirements Matter

Without locate requirements, a short-seller could execute a sale even if no shares were available to borrow. This is called a "naked short sale" or "naked short." The seller promises to deliver shares at settlement (typically two business days out, or T+2) but has made no arrangement to actually obtain those shares. Instead, the seller is betting that the price will fall, allowing them to buy back shares at a lower price before settlement date and pocket the difference.

In aggregate, naked shorts inflate the apparent supply of shares. If many traders are simultaneously executing naked shorts in a thinly traded stock, the price can be artificially depressed by phantom shares flooding the market. Early versions of this abuse (pre-2005) contributed to market bubbles and failures, including the collapse of small-cap stocks where naked shorting ran rampant.

The locate requirement directly blocks this by forcing the broker to verify, upfront, that shares can be sourced. If they can't be, the order is rejected or goes on a list pending availability.

## Failure to Deliver and Close-Out Rules

Even with a locate in place, things can go wrong. The stock is borrowed, the sale is executed, but by settlement date the shares haven't actually arrived from the lender. This creates a "failure to deliver" (FTD). Regulation SHO mandates close-out rules:

- **T+4 Rule:** If shares are not delivered by the fourth business day after the trade, the broker must close out the position (buy shares to return to the lender) by the end of T+4.
- **Continuous Close-Out:** For certain liquid securities on the [SEC](/securities-and-exchange-commission/)'s list, failure to deliver across two settlement cycles (T+5) must trigger a buy-in the very next business day.

These close-out rules ensure that shorts don't become chronic failures-to-deliver, which would replicate the naked short effect over time.

## Regulation SHO and Market-Makers

Market-makers (traders who stand ready to buy and sell for their own account to provide liquidity) were given a partial exemption in Regulation SHO. They may execute short sales without a pre-trade locate, relying instead on an intraday locate by end of trading. The logic is that market-makers must react quickly to order flow, and requiring a locate before each small trade would cripple their ability to quote two-sided markets.

However, this exemption comes with strict close-out obligations. A market-maker who executes a naked short at 10 a.m. must close out that position—buy shares or return borrowed shares—by end of day. The SEC and [FINRA](/finra/) monitor market-maker close-out rates carefully; persistent failure by a market-maker to close out naked shorts can result in enforcement action.

## The Rule in Practice: Mechanics and Enforcement

When a retail trader places a short-sale order with a broker, the broker's back-office system checks its locate inventory or calls a securities-lending desk to see if shares are available. If yes, the trade executes and a borrow agreement is typically established immediately (often intraday). If no, the trade is rejected or placed on a "locate list," pending availability.

Most brokers simply reject orders on stocks with no locate available. Some offer delayed execution, waiting for shares to become available.

If the broker improperly executes a short sale without a locate, the [SEC](/securities-and-exchange-commission/) and [FINRA](/finra/) can:

- Issue a warning
- Impose trading halts or suspensions for the violating broker
- Fine the broker (often six-figure sums for egregious conduct)
- Mandate mandatory close-out and restitution to customers

For customers who knowingly participate in a naked short, the SEC can also pursue civil-litigation or, in fraud cases, criminal referrals.

## Hard-to-Borrow Stocks and the Realities

In practice, large-cap, liquid stocks have abundant shares in the borrowing market. A locate is trivial. But for small-cap, thinly traded, or newly volatile stocks—especially those subject to short-squeeze scenarios—shares can be hard or impossible to borrow. A trader may intend to short a stock but discover that no shares are available to locate.

In such cases, the trader must either:
- Wait and try again later when shares come available
- Trade a different security
- Accept that the short is not feasible

This friction is by design. Regulation SHO makes [short-selling](/short-selling/) more difficult when supply is constrained, which is the intended antidote to naked shorting.

## Relationship to Circuit Breakers and Trading Halts

Regulation SHO works alongside other SEC circuit-breaker rules. The **SEC short-sale circuit-breaker rule** (Rule 10a-2) requires a trading halt whenever a stock falls 10% in a single day due to short-selling pressure. The **uptick rule** (Rule 10a-1) restricts short sales on a downtick in certain conditions. Together with the locate requirement, these rules aim to prevent panic-driven short squeezes and cascading sell-offs fueled by unrestricted naked shorts.

## See also

<div class="wiki-seealso">

### Closely related

- [Short-selling](/short-selling/) — The trading practice that Regulation SHO governs
- [Securities-and-exchange-commission](/securities-and-exchange-commission/) — Primary regulator issuing Regulation SHO
- [FINRA](/finra/) — Broker regulator that enforces locate requirements through rule 4560
- Failure to deliver — The enforcement outcome when shorts aren't closed out
- Naked short selling — The abuse the locate requirement prevents

### Wider context

- Market-manipulation — The class of conduct Regulation SHO targets
- [Price-discovery](/price-discovery/) — Why preventing naked shorts supports fair markets
- [Systemic-risk](/systemic-risk/) — How naked shorting can threaten financial stability
- [Broker](/broker/) — Intermediary responsible for enforce locate before executing shorts

</div>
