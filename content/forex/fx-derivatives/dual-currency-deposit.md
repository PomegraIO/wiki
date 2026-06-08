---
title: "Dual Currency Deposit"
description: "A yield-enhanced savings product where the bank holds a call option on an alternative currency and may repay principal in that weaker currency."
keywords:
  - dual currency deposit
  - structured deposit
  - fx option
  - savings product
  - currency exposure
image: /svg/forex.svg
---

*A **dual currency deposit** is a fixed-term savings product that promises an above-market interest rate in exchange for giving the bank an embedded [call option](/call-option/): at maturity, the bank may elect to repay principal in a designated alternative currency rather than the deposit currency. If the alternative currency has weakened relative to the deposit currency, the depositor suffers a loss on principal. The higher yield compensates the depositor for accepting this [currency risk](/currency-risk/).*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Dual Currency Deposit — key facts</div>

<img src="/svg/forex.svg" alt="An abstract editorial mark for FX instruments." />

<div class="wiki-infobox-caption">Above-market interest rate offset by embedded FX downside for the depositor.</div>

|   |   |
|---|---|
| **What it is** | Structured deposit combining interest + embedded FX option |
| **Issuer** | Banks; offered to retail and institutional depositors |
| **Interest rate** | Above standard market rates (compensation for option risk) |
| **Optionality** | Bank holds the right to repay in alternative currency |
| **Strike** | Spot rate at inception (par forward) |
| **Principal risk** | Depositor bears loss if alternative currency weakens |
| **Duration** | Typically 3 months to 2 years |
| **Leverage** | None (principal protected at strike, not leveraged) |

</aside>

## Structure and payoff

A depositor places, say, USD 1 million for 12 months at an agreed rate—typically 5–6 per cent if market rates are at 2 per cent. At inception, the bank fixes a strike rate: for example, USD/CHF at 0.92 (meaning 1 USD = 0.92 CHF). At maturity:

- **If the bank does not exercise its option**: the depositor receives USD 1 million principal plus 12 months of accrued interest in USD.
- **If the bank exercises its option**: the depositor receives principal in CHF at the strike rate. If USD/CHF has risen to 0.95, the bank pays back 920,000 CHF (the original strike amount), which now buys only USD 973,684 at spot—a loss of USD 26,316 on the depositor's principal.

The premium embedded in the deposit is the interest-rate differential. The bank shorts a currency call (has the right to deliver an alternative currency) and finances the short call premium by offering above-market interest.

## Why banks offer them and depositors buy them

For the **bank**, a dual currency deposit is a liability that they can convert into a cheaper currency if it weakens during the tenor. If a bank collects USD deposits at 5.5 per cent but market rates are 2 per cent, the bank captures 3.5 per cent in embedded profit. The bank then hedges the [currency risk](/currency-risk/) (or leaves it as a trading position if the treasury believes the alternative currency will strengthen).

For the **depositor**, dual currency deposits appeal in low-interest environments. If markets offer only 2 per cent on safe USD deposits, the dual currency version at 5.5 per cent is tempting. Retail investors often fail to fully appreciate the embedded FX downside, viewing the deposit as a savings account rather than a leveraged currency bet. Institutional depositors—hedge funds, international insurance companies—use them as a deliberate [currency volatility](/currency-volatility/) trade.

## Risk profile for the depositor

The depositor has sold a [call option](/call-option/) on the alternative currency (or equivalently, sold a put on the deposit currency). The payoff at maturity is:

**Principal (in deposit currency) = Notional + max(0, Spot − Strike) × Notional / Strike**

If spot moves against the depositor (the strike currency weakens), the bank exercises and the depositor's principal shrinks. There is no floor other than the strike rate itself; if the currency crashes, the depositor receives only the strike amount—a total loss of principal converted to the alternative currency.

However, the principal is *not* leveraged or marked-to-market during the tenor. Unlike margin accounts or forwards, the depositor does not face variation margin calls if the currency moves sharply. They simply wait until maturity to discover whether the bank exercised.

## Comparison to other instruments

A dual currency deposit differs from an [FX Forward Extra](/fx-forward-extra/) in that the payoff is asymmetric: the bank chooses whether to exercise, not the depositor. It differs from a [variance swap](/fx-variance-swap/) in that it has a single binary event (exercise or not), not a continuous settlement on realised volatility.

It is similar in spirit to a **covered call**: the bank is long the deposit (owes interest and principal) and short a currency call. The interest rate compensates the depositor for being short the call.

A depositor concerned about [currency risk](/currency-risk/) should compare the dual currency deposit to simply holding a CD at market rates and buying a [put option](/put-option/) on the strike currency—the "protected deposit" approach. The protected deposit costs upfront; the dual currency deposit costs in the form of foregone principal if the bank exercises.

## Real-world pricing and variants

The interest rate on a dual currency deposit is set by the dealer using [Black-Scholes](/black-scholes-model/) or [vanna-volga](/vanna-volga-pricing/) pricing models. If the alternative currency is illiquid or the tenor is long, the [volatility smile](/equity-etf/) and [interest rate risk](/interest-rate-risk/) both matter.

A bank might offer a **dual currency deposit with a knock-out**: the option cancels if spot reaches a barrier level during the tenor, protecting the depositor from catastrophic principal loss but reducing the interest rate.

Alternatively, a **quanto dual currency deposit** (rare) fixes the FX conversion rate at inception, eliminating spot risk but not interest-rate risk. This variant is less common because it removes the reason the bank wanted to fund the deposit cheaply.

## Regulatory and credit concerns

Dual currency deposits are treated as structured products and often fall under retail conduct rules. In some jurisdictions (EU, for instance), they carry mandatory warnings about principal loss. Regulators frown on retail sales without explicit FX risk disclosure.

[Counterparty risk](/counterparty-risk/) is high: the depositor is not only a creditor of the bank but also assumes an FX bet against the bank's treasury. If the bank fails mid-tenor, the depositor loses both the principal guarantee and the option. Deposit insurance schemes typically cover the nominal principal amount but may not cover the missed interest if the bank defaults.

## Market dynamics and interest rates

When central banks raise rates, dual currency deposits become more attractive to banks (wider funding cost differentials) and less attractive to depositors (because market rates rise and the deposit looks less special). Conversely, in low-rate environments, depositors desperate for yield often accept the FX risk.

Currency volatility also drives the economics. If [implied volatility](/equity-etf/) is very high, the embedded call option is expensive, and banks must offer very high interest to compensate. This creates a self-reinforcing dynamic: high volatility → attractive dual currency deposits → depositors take FX risk → spot can move sharply → original depositor losses realized.

## See also

<div class="wiki-seealso">

### Closely related

- [Option](/option/) — derivative contract granting the right to buy or sell
- [Call Option](/call-option/) — option to buy at a fixed strike
- [Put Option](/put-option/) — option to sell at a fixed strike
- [FX Forward Extra](/fx-forward-extra/) — structured product combining forward with optionality
- [FX Variance Swap](/fx-variance-swap/) — pure volatility exposure traded in OTC markets
- [Vanna-Volga Pricing](/vanna-volga-pricing/) — smile-adjusted FX options valuation
- [Black-Scholes Model](/black-scholes-model/) — foundational option pricing framework
- [Counterparty Risk](/counterparty-risk/) — risk that the bank issuing the deposit defaults

### Wider context

- [Currency Risk](/currency-risk/) — exposure to adverse FX movements
- [Currency Volatility](/currency-volatility/) — fluctuations in FX spot rates
- [Interest Rate Risk](/interest-rate-risk/) — exposure to changes in discount rates
- [Over-the-Counter Market](/over-the-counter-market/) — decentralised trading of structured products
- [Bid-Ask Spread](/bid-ask-spread/) — cost of unwinding a position before maturity
- [Central Bank](/central-bank/) — institution setting official interest rates and monetary policy

</div>
