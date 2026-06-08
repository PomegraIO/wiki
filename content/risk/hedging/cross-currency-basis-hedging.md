---
title: "Cross-Currency Basis Hedging"
description: "Protecting against basis risk when funding in a foreign currency through cross-currency basis swaps."
keywords:
  - cross-currency basis swap
  - funding hedging
  - currency basis risk
  - offshore funding
  - basis spread
image: "/svg/risk.svg"
---

*A **cross-currency basis hedge** is a strategy that protects a borrower or investor against changes in the basis spread embedded in [cross-currency swaps](/cross-currency-swap/)—the premium or discount that emerges when exchanging cash flows in two currencies at a different rate than the spot market implies. When a company funds itself in foreign currency rather than its home currency, that basis spread is real money, and it moves unpredictably.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Cross-Currency Basis Hedging — key facts</div>

<img src="/svg/risk.svg" alt="An abstract editorial mark denoting risk and hedging strategies." />

<div class="wiki-infobox-caption">Basis swaps protect borrowers against the cost of funding mismatches between currencies.</div>

|   |   |
|---|---|
| **What it is** | A derivative strategy that locks in (or neutralises) the spread between spot forex rates and the [interest-rate](/interest-rate/) parity implied rate |
| **Also called** | Basis spread hedging, cross-currency swap hedge |
| **Key driver** | Supply and demand for [offshore funding](/capital-flows/), [central bank](/central-bank/) policy, and [credit-risk](/credit-risk/) premia |
| **Measured in** | Basis points (0.01%) above or below [covered interest-rate parity](/interest-rate-risk/) |
| **Used by** | Multinational corporates, [banks](/bank-of-america/), [hedge funds](/hedge-fund/), and [private-equity](/private-equity-fund/) firms |
| **Related instrument** | [Cross-currency swap](/cross-currency-swap/), [forward contract](/forward-contract/) |

</aside>

## Why the basis exists in the first place

Textbooks teach covered interest-rate parity: if you can borrow dollars at 5 per cent, lend yen at 3 per cent, and the forward forex rate is set to equilibrate the returns, both currencies should cost the same. In reality, they rarely do. When hundreds of billions of dollars flood into Japanese yen to finance cheap carry trades, or when banking regulations make yen funding scarce, the basis spread—the gap between what parity predicts and what the market actually prices—widens. A US firm funding itself in yen might find it pays an extra 20 basis points beyond the theoretical rate. That is basis risk, and it is distinct from ordinary [currency-risk](/currency-risk/).

## The mechanics of hedging the basis

To hedge this mismatch, a borrower enters a basis swap. In its simplest form, the borrower agrees to pay a floating rate in the foreign currency (say, yen LIBOR) and receives a floating rate plus a basis spread in its home currency (say, dollar SOFR plus 20 bps). The spread is now fixed. If the basis widens to 30 bps, the borrower is protected; if it narrows to 10 bps, the borrower pays that protection. The swap essentially converts uncertainty about the basis into a known, predictable cost. For a company that has real operating cash flows in both currencies, this lock-in is valuable insurance.

A related but distinct approach is to buy a [cross-currency swap](/cross-currency-swap/) outright—paying in one currency, receiving in another—and simultaneously trade the FX basis through the money market. This requires active management and access to offshore funding markets, and it is more common among [banks](/bank-of-america/) and large [asset managers](/asset-allocation/) than corporates.

## When the basis widens: funding stress and banks

The basis spread is not random. It balloons during financial stress, when [risk-aversion](/market-risk/) spikes and [counterparty-risk](/counterparty-risk/) suddenly matters. In the 2008 financial crisis, the dollar-yen basis blew out to –200 bps or worse; Japanese banks that had funding gaps found it ruinously expensive to raise dollars. The [Federal Reserve](/federal-reserve/) eventually opened swap lines with the Bank of Japan to restore stability. This teaches a hard lesson: basis risk is partly a [liquidity-risk](/liquidity-risk/) and [systemic-risk](/systemic-risk/) phenomenon, not just a textbook pricing anomaly.

Hedging the basis, therefore, is really a proxy for hedging funding stability. A bank that relies on offshore deposits or money-market funding is implicitly short the basis; when the basis widens, its funding costs spike. [Central banks](/central-bank/) manage this by intervening in basis swap markets or by opening swap lines with peers.

## Cost and trade-offs

Hedging the basis is not free. The basis swap spread itself—the fee you pay to transfer the risk—reflects the market's opinion of how likely the basis is to widen, and who is willing to take the opposite bet. In a benign environment, the basis is stable, and paying to hedge it is a pure cost. In a stressed environment, the basis can move sharply, and the hedge is priceless.

For a borrower, the decision hinges on its operational footprint and balance-sheet flexibility. A multinational with substantial foreign-currency revenues may accept basis risk because it expects its earnings to absorb the cost. A financial institution, which must fund itself at market rates, often cannot afford the luxury; hedging becomes mandatory. The [cost-of-debt](/cost-of-debt/) rises by the basis swap spread, but [default-risk](/credit-risk/) drops because funding is more predictable.

## Basis swaps vs. plain forwards

A [forward contract](/forward-contract/) locks in an exchange rate; a basis swap locks in the *spread above* parity. The two work in tandem. If you know you owe yen in six months, you can sell yen forward to lock in the dollar amount. But if you are *funding* in yen—rolling over a series of yen loans—you face a stream of basis payments over time, not a single FX rate. A basis swap, which is typically quarterly-reset, mirrors that cashflow profile more closely than a vanilla forward.

## When basis hedges backfire

Basis swaps, like all derivatives, carry [operational-risk](/operational-risk/) and [counterparty-risk](/counterparty-risk/). A borrower that hedges the basis but misjudges its future currency needs may find itself paying basis premiums on swaps that no longer protect its actual funding. If the currency mismatch resolves—say, the subsidiary is sold—the swap remains a liability. Accounting treatment under IFRS and GAAP also affects whether the hedge qualifies for special treatment, which can create profit-and-loss (P&L) volatility.

Worse, basis risk is correlated with broader financial stress. A borrower that needs the hedge most—during a crisis when the basis is widening—may find that the cost of entering new hedges is prohibitive, or that banks are unwilling to post the required collateral. This is why dynamic basis hedging, in which borrowers adjust their hedge ratio based on available funding, is more realistic than a static, eternal hedge.

## See also

<div class="wiki-seealso">

### Closely related

- [Cross-currency swap](/cross-currency-swap/) — the derivative instrument used to execute a basis hedge
- [Correlation hedging](/correlation-hedging/) — protecting against changes in the statistical relationships between assets
- [Quanto hedging](/quanto-hedging/) — hedging FX-asset correlation in multi-currency positions
- [Covered interest-rate parity](/interest-rate-risk/) — the theoretical relationship that basis swaps protect against
- [Currency risk](/currency-risk/) — the broader category of FX exposure that basis hedges address
- [Forward contract](/forward-contract/) — a simpler instrument for locking in exchange rates
- [Interest-rate swap](/interest-rate/) — the domestic equivalent; basis swaps are the cross-currency version
- [Counterparty risk](/counterparty-risk/) — the risk that the swap counterparty defaults

### Wider context

- [Hedge fund](/hedge-fund/) — major users of basis trades
- [Central bank](/central-bank/) — interventions that suppress or amplify basis spreads
- [Capital flows](/capital-flows/) — the macroeconomic driver of basis dynamics
- [Systemic risk](/systemic-risk/) — basis blowouts during financial crises
- [Liquidity risk](/liquidity-risk/) — closely tied to basis risk during stress

</div>
