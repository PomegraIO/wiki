---
title: "Counterparty Risk"
description: "Counterparty risk is the probability that the other party in a financial transaction will fail to meet its obligations, leaving you holding a loss or unexecuted contract."
keywords:
  - counterparty risk
  - default risk
  - credit exposure
  - derivative risk
  - bilateral risk
image: "/svg/risk.svg"
---

*Counterparty risk is the risk that the other party to a financial contract — a borrower, broker, [bond](/bond/) issuer, or derivatives counterparty — will fail to deliver on its obligations. It is a form of [credit-risk](/credit-risk/) but extends beyond simple lending to include all financial contracts with future cash flows or settlements.*

<div class="wiki-hatnote">

This entry covers the risk that any counterparty fails to perform. For the specific case of a government failing to pay its debt, see [sovereign-risk](/sovereign-risk/); for the risk of failure during settlement, see [settlement-risk](/settlement-risk/).

</div>

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Counterparty Risk — key facts</div>

<img src="/svg/risk.svg" alt="Two hands reaching to shake, one suddenly disappearing, leaving a broken bridge" />

<div class="wiki-infobox-caption">Counterparty risk materializes when the other party fails to perform.</div>

|   |   |
|---|---|
| **What it is** | Risk that counterparty defaults or fails to perform |
| **Applies to** | [Bonds](/bond/), loans, derivatives, swaps, forwards, OTC transactions |
| **Measured by** | Probability of default; exposure at default; loss given default |
| **High in** | Uncleared OTC derivatives; bilateral swaps with weak counterparties |
| **Low in** | Cleared derivatives; government [bonds](/bond/); exchange-traded instruments |
| **Can be reduced by** | Central clearing; collateral agreements; netting; central counterparties |
| **Amplified by** | [Systemic risk](/systemic-risk/); contagion; interconnectedness |

</aside>

## Counterparty risk is everywhere in finance

Every financial contract has a counterparty. When you own a [bond](/bond/), the issuer is your counterparty — they must pay coupons and principal. When you buy a [stock](/stock/), your broker is a counterparty — they must deliver the shares or hold them safely. When you enter a derivative contract (a swap, forward, option), the dealer is a counterparty — they must pay you if the contract moves in your favour.

Counterparty risk is the risk that any of these parties fails. The issuer defaults on the [bond](/bond/). The broker goes bankrupt and your securities are lost. The dealer cannot pay on the swap.

The magnitude varies widely. US Treasury counterparty risk is near zero — the US government is unlikely to default on obligations to Americans. A small regional bank is a much riskier counterparty.

## The PD-EAD-LGD framework

Counterparty risk, like [credit-risk](/credit-risk/), is measured using:

1. **Probability of default (PD).** How likely is this counterparty to fail? Estimated from credit ratings, historical default rates, or market prices.

2. **Exposure at default (EAD).** How much do you have at risk if they fail? For a [bond](/bond/), it is the face value plus accrued interest. For a derivative, it is the current market value plus potential future exposure.

3. **Loss given default (LGD).** What portion of the exposure do you lose? If collateral backs the contract (a secured loan), recovery is higher. If it is unsecured (an OTC derivative), recovery is lower.

Expected loss = PD × EAD × LGD. A swap with a dealer carrying a 1% annual default probability, $10 million current exposure, and 50% loss rate generates an expected loss of $50,000 per year.

## Counterparty risk in derivatives and swaps

Counterparty risk is particularly acute in over-the-counter (OTC) derivatives like swaps, forwards, and options. These contracts are bilateral: the risk flows both ways. If interest rates move in your favour, your counterparty owes you; if rates move against you, you owe them.

Before the 2008 financial crisis, OTC derivatives were largely uncleared, meaning two parties dealt directly with each other. This created massive bilateral counterparty risk: if one party failed mid-contract, the other faced losses. Lehman Brothers' failure in 2008 left swap counterparties with billions in unexpected losses.

To reduce this risk, central clearing was introduced. Now, most OTC derivatives go through a central counterparty (CCP), like the Intercontinental Exchange (ICE) or the Clearing House. The CCP interposes itself between the two parties, reducing bilateral risk. But this shifts counterparty risk to the CCP itself — now you worry about whether the CCP will survive.

## Counterparty risk concentration

Many large institutions are highly interconnected. Bank A lends to Bank B, which lends to Bank C, which borrows from Bank A, and all three hold swaps with each other. If Bank B fails, the failure ripples through the network, threatening Banks A and C. This is [systemic-risk](/systemic-risk/) — counterparty risk that spreads.

During the 2008 crisis, counterparty risk concentration was extreme. Lehman Brothers was a counterparty to thousands of contracts with hundreds of firms. Its failure created a cascade of losses and threatened the entire financial system.

## Managing and mitigating counterparty risk

Financial institutions use several tools:

- **Collateral agreements.** A swap agreement includes a provision that the losing party must post collateral daily, reducing the EAD. If the counterparty fails, you hold collateral to cover losses.

- **Netting.** If you have multiple contracts with a counterparty, your exposure is the net of all contracts, not the sum. If you owe them $10M on one swap and they owe you $12M on another, your net exposure is $2M in your favour, not $22M.

- **Central clearing.** Using a CCP reduces bilateral counterparty risk, though it concentrates risk on the CCP.

- **Counterparty diversification.** Use many counterparties for derivatives rather than concentrating on one dealer.

- **Credit monitoring.** Track the credit quality of key counterparties; if it deteriorates, reduce exposure or request additional collateral.

For individual investors, counterparty risk is mainly with your broker (for stock and [bond](/bond/) holdings) and your bank (for deposits). Choose large, well-capitalized institutions; diversify across multiple institutions if your holdings are large.

## See also

<div class="wiki-seealso">

### Closely related

- [Credit risk](/credit-risk/) — counterparty risk is a form of credit risk
- [Settlement-risk](/settlement-risk/) — counterparty risk during settlement
- [Systemic risk](/systemic-risk/) — counterparty failures can trigger systemic crises
- [Bond](/bond/) — issuer is a counterparty
- [Derivative](/option/) — contract holder and dealer are counterparties

### Broader context

- [Central clearing](/central-bank/) — reduces bilateral counterparty risk
- [Collateral](/bond/) — mitigates counterparty risk
- [Too big to fail](/systemic-risk/) — large counterparties are systemic
- [Lehman Brothers](/credit-risk/) — 2008 example of counterparty risk crystallizing
- [Stress testing](/stress-testing/) — assess losses from counterparty default

</div>
