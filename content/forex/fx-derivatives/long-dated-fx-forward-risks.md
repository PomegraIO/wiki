---
title: "Long-Dated FX Forward Risks and Pricing"
description: "Why multi-year currency forwards carry higher credit risk, basis risk, and pricing premiums than short-dated contracts."
keywords:
  - long dated fx forward risks
  - currency forward pricing
  - counterparty credit risk
  - fx basis risk
  - illiquid forward markets
---

*A **long-dated FX forward** is a contract to exchange currencies at a fixed rate years into the future, but the longer the maturity, the higher the credit risk, basis volatility, and pricing friction. Traders pay measurably more to lock in rates far ahead because uncertainties compound, counterparties become less trustworthy over extended periods, and the market for unwinding or hedging those contracts thins out.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Long-Dated FX Forwards — Key Facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for currency derivatives." />

<div class="wiki-infobox-caption">Multi-year currency forwards cost more and carry outsized risks that short-dated deals don't.</div>

|   |   |
|---|---|
| **Typical maturity range** | 1–10 years; anything beyond 5 years is illiquid |
| **Main cost drivers** | Counterparty credit risk, [basis risk](/basis-risk/), [interest-rate risk](/interest-rate-risk/) |
| **Pricing spread vs. short-dated** | 50–200+ basis points wider, depending on [credit rating](/credit-rating/) |
| **Unwinding friction** | Difficult; most banks avoid marking-to-market on 5+ year forwards |
| **Typical users** | Large corporates with long-term FX exposure, [hedge funds](/hedge-fund/) managing [carry trades](/carry-trade/) |
| **Settlement risk** | Counterparty may default before delivery; [credit-default-swap](/credit-default-swap/) pricing reflects this |

</aside>

## Why Long-Dated Forwards Cost More

The price of a currency forward is anchored in [interest-rate differentials](/interest-rate/) between the two currencies — a simple arbitrage idea called [interest-rate parity](/interest-rate-parity/). In theory, the forward rate should equal the spot rate adjusted for the yield curve gap. In practice, the longer the forward, the wider the bid-ask spread and the steeper the discount demanded by the dealer.

That wedge emerges because holding a 10-year FX forward obligates the bank to maintain [counterparty credit risk](/counterparty-risk/) exposure for a decade. If you lock in a USD/JPY forward at 2.5% over par for five years, and your counterparty's [credit spread](/credit-spread/) widens from 50 to 200 basis points in year two, the forward is now worth less to you (the counterparty is riskier). The bank that sold you the forward must either hold that deteriorating credit exposure or pay to hedge it — and neither is free.

Corporate treasurers often accept these premiums because the alternative — rolling short-dated forwards repeatedly — exposes them to [basis risk](/basis-risk/): the forwards reset at unknown rates every 3–6 months, and unexpected moves in the spot-forward differential can blow holes in budgets. A 10-year lock-in eliminates that rolling uncertainty.

## Basis Risk in Multi-Year Contracts

**Basis** in FX markets is the spread between the current [spot rate](/spot-rate/) and the forward rate implied by [interest-rate](/interest-rate/) differentials. Over short horizons (days to weeks), basis is stable and predictable. Over years, it drifts.

When you transact a 5-year USD/EUR forward, you are implicitly betting on a specific path of [USD](/us-dollar/) and [EUR](/european-central-bank/) [interest rates](/interest-rate/) and their cross-currency basis. If [the Federal Reserve](/federal-reserve/) cuts rates unexpectedly or European [credit spreads](/credit-spread/) blow out, the basis can shift by 200+ basis points. A treasurer who hedged 5-year currency exposure last year at an agreed rate may find that equivalent exposure is now cheaper or more expensive to forward-hedge today — but they are already locked in.

This gap between where you locked in and where rates move is basis risk, and it accumulates over time. Long-dated forwards crystallize a single path; short-dated forwards are repriced continuously but expose you to rollover costs and rates moving against you at each renewal.

## Counterparty Credit Risk and Concentration

A 10-year FX forward with a bank is a [credit exposure](/credit-risk/). The mark-to-market value of the contract (what it would cost to unwind) can swing by tens of millions of dollars if spot rates or [interest rates](/interest-rate/) move. The longer the maturity, the more that exposure can grow.

Banks manage this by demanding higher [credit spreads](/credit-spread/) (wider bid-ask) and by limiting the total notional amount any single counterparty can transact in long-dated forwards. A highly-rated multinational company might transact a $100 million 10-year forward; a smaller firm or a weaker credit would be quoted much wider margins or refused entirely.

Regulators reinforced this constraint after 2008. [Basel III](/capital-adequacy/) [capital](/capital-adequacy/) rules require banks to hold equity against potential future credit losses on long-dated derivatives. A 10-year forward that could move $50 million in value is far more capital-intensive than a 3-month forward that can move only $5 million. That cost is passed to the client as a wider spread.

## Illiquidity and Unwinding Costs

Most long-dated FX forwards are bespoke contracts between a bank and a client. There is no exchange, no standardized contract, no secondary market. If you need to exit or adjust your 6-year forward midway, the bank will unwind it by:

1. Calculating the mark-to-market cost (what it would cost the bank to lay off the contract to another counterparty, or to reverse the trade).
2. Adding a unilateral bid-ask spread to compensate for the hassle and credit risk of binding the bank into a new, opposite forward with a different partner.

A 10-year forward might have a $5 million mark-to-market loss due to spot and [interest-rate](/interest-rate/) moves, plus another $2–5 million in unwinding friction. You lose the contract *and* pay to get out of it.

This illiquidity is why treasurers often endure [basis risk](/basis-risk/) by rolling short-dated forwards instead. A 3-month forward is actively quoted by dozens of banks, can be unwound almost instantly at a tight spread, and resets regularly to market reality. A 5-year forward is a phone call to one or two banks, a long negotiation, and a much wider exit cost.

## Pricing Mechanics and the Forward Curve

The [interest-rate](/interest-rate/) differential between currencies determines the theoretical forward premium or discount. The [USD](/us-dollar/) typically offers lower rates than emerging-market currencies; a 10-year USD/BRL forward will be quoted at a steep premium (fewer Brazilian reais per dollar) to compensate for the [interest-rate](/interest-rate/) gap.

But dealers don't quote at the "true" theoretical rate. They quote a bid and ask that widens with maturity:

- **1-month forward**: bid-ask of 0.2–0.5 pips (for major pairs like USD/EUR)
- **1-year forward**: 2–5 pips
- **5-year forward**: 10–30 pips
- **10-year forward**: 30–100+ pips

For a $100 million notional, a 10-pip spread is $10,000; for a $1 billion transaction, it is $100,000. Illiquid currencies and weaker credits can see spreads double or triple.

## When Long-Dated Forwards Make Sense

They are appropriate when:

- A company has *known, multi-year operating cash flows* in a foreign currency and wants certainty on conversion costs. A US exporter with a 5-year contract to deliver goods and collect EUR in tranches every quarter might hedge the stream with forwards, locking in USD equivalents now.
- A [private-equity fund](/private-equity-fund/) or [hedge fund](/hedge-fund/) is running a [carry trade](/carry-trade/) where the upside comes from *interest-rate differentials*, not spot appreciation. A 5-year AUD/JPY carry (buy AUD, fund in JPY) is profitable if the [interest-rate](/interest-rate/) gap persists; the fund locks in that gap via a long-dated forward.
- [Basis risk](/basis-risk/) would be materially worse than [credit risk](/credit-risk/). A multinationals hedging a 10-year pension obligation in EUR may prefer a 10-year forward (fixed [credit risk](/credit-risk/)) to rolling 1-year forwards and re-pricing every 12 months.

## Practical Example: Corporate Hedge

Imagine a US manufacturer with a $50 million, 4-year contract to sell machinery to a German customer, payable in EUR in equal quarterly installments.

**Option 1: Roll 3-month forwards**
- Lock in today's spot + forward spread for the first quarter.
- Every 3 months, roll the remaining notional at whatever spot + spread the market quotes.
- Pros: Tight spreads, no credit concentration.
- Cons: If EUR weakens or [USD interest rates](/interest-rate/) rise, rolling costs could jump 5–10% over 4 years.

**Option 2: Lock a 4-year forward**
- Quote: 1.0800 USD/EUR (vs. spot of 1.0900).
- Pros: Certainty; no rollover risk; one transaction.
- Cons: Dealer adds 30+ pips to the "fair" rate to cover [credit risk](/credit-risk/), basis volatility, and illiquidity. Over $50 million, that's $150,000–$250,000 upfront.

The treasurer weighs: is the certainty worth the $200,000 cost? If budget visibility is critical and EUR is volatile, yes. If the company can tolerate quarterly repricing, rolling is cheaper on average.

## See also

<div class="wiki-seealso">

### Closely related

- [Interest-rate risk](/interest-rate-risk/) — How currency forwards are sensitive to diverging central-bank policy
- [Basis risk](/basis-risk/) — Why forwards and spot don't move in lockstep
- [Counterparty risk](/counterparty-risk/) — The credit exposure embedded in every derivative trade
- [Carry trade](/carry-trade/) — Using interest-rate differentials to profit with leveraged forwards
- [Credit-default swap](/credit-default-swap/) — How markets price the risk of dealer default
- [Forward contract](/forward-contract/) — The mechanics of binding, over-the-counter FX contracts

### Wider context

- [Currency risk](/currency-risk/) — The broad category of FX exposure management
- [Currency volatility](/currency-volatility/) — Why spot rates move, and how forwards are priced
- [Over-the-counter market](/over-the-counter-market/) — Where long-dated forwards trade, unseen
- [Dealer capital requirements](/capital-adequacy/) — Why banks charge more for longer-dated risk

</div>
