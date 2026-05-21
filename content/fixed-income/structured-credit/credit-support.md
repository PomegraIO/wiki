---
title: "Credit Support"
description: "The structural mechanisms—tranching, overcollateralization, reserves, triggers—that protect investors from credit losses in securitized credit structures."
---

*Credit support is the collective set of tools used to make securitized debt safe for investors. A tranche structure with subordination is credit support. Overcollateralization is credit support. Cash reserves held in escrow are credit support. Interest-rate hedges that protect against cash-flow disruption are credit support. A strong securitization layers multiple forms of credit support, with each mechanism backstopping the others. Weak support leaves investors exposed.*

## The layered protection model

Credit support in securitizations is typically layered:

**Layer 1: Subordination (Tranching)**
- Mezzanine and equity tranches absorb losses before senior tranches.
- Equity tranche might absorb 5% of collateral value in losses.
- Mezzanine absorbs another 10%.
- Only after both are exhausted (15% losses) do senior investors suffer.

**Layer 2: Overcollateralization**
- Issued bonds = $85M; collateral = $100M.
- The $15M excess provides an additional buffer.
- Overcollateralization ratio is typically 5–20%.

**Layer 3: Reserve Accounts**
- Cash is set aside and held in escrow.
- Used to cover interest shortfalls if collateral cash flows decline.
- Typically funded from excess spread.

**Layer 4: Triggers and Dynamic Structures**
- If delinquencies exceed a threshold, cash diversion occurs (senior bonds get paid faster).
- If overcollateralization falls below a target, excess spread is retained to rebuild it.
- These triggers automatically protect investors if deterioration is detected.

**Layer 5: Originator Retention**
- The originator retains the equity tranche or some portion of credit risk.
- Creates skin-in-the-game incentive to maintain quality.

## Subordination and seniority

Subordination is the primary credit support. In a 4-tranche securitization:

- **Senior A tranche**: Gets paid before all others; suffers losses only after junior tranches are wiped out.
- **Senior B tranche**: Gets paid after Senior A but before junior tranches.
- **Mezzanine tranche**: Gets paid after both senior tranches.
- **Equity**: Gets paid last; absorbs first losses.

The subordination ratio specifies how much junior protection sits below each tranche. A Senior A tranche might have 30% subordination (30% junior collateral sits below it). A Senior B might have 20%.

This structure is formalized in the transaction's "pro-rata waterfall": the monthly order in which cash is distributed.

## Sizing tranches: the modeling exercise

Securitization structurers use credit loss models to size tranches. The process:

1. **Model expected losses** under base-case assumptions (e.g., 1% default rate, 50% severity).
2. **Model stress scenarios** (unemployment spikes, home prices fall, etc.), predicting losses in 95th and 99th percentile scenarios.
3. **Size the equity** to absorb expected losses plus a buffer.
4. **Size mezzanine** to absorb 95th percentile losses.
5. **Size senior** to absorb 99th percentile losses and remain investment grade.

A securitizer might model: expected loss is 0.6%, 95th percentile is 2%, 99th percentile is 3.5%. Thus:

- Equity: 1.5% subordination (covers expected loss + buffer)
- Mezzanine: 2.5% subordination (covers 95th percentile)
- Senior: 3.5% subordination (covers 99th percentile)
- Or equivalently, 3.5% total subordination to senior; 2.5% to mezzanine; 1.5% to equity.

## Overcollateralization: the static cushion

Overcollateralization (OC) is set at issuance as a percentage of bond face:

- Collateral value: $100M
- Bonds issued: $90M
- OC ratio: 11% (i.e., 11% of bond face is excess collateral)

This cushion absorbs losses. If collateral depreciates by $2M (due to defaults or market repricing), OC shrinks from 11% to 9.8%. The bond principal is unaffected (still $90M) but the excess cushion has shrunk.

OC is dynamic. As collateral amortizes (principal is repaid), OC shrinks. As defaults accumulate, OC shrinks faster. Some deals include OC maintenance triggers: if OC falls below a target (say, 5%), excess cash is diverted to pay down bonds (rebuild OC) rather than going to equity.

## Reserve accounts and excess spread

Reserve accounts are cash held in escrow. A typical structure:

- **Interest reserve account**: Holds cash equal to 1–2 months of interest on the bonds.
- **Principal reserve account**: Holds cash equal to 1–2 months of expected principal.

These reserves are funded from excess spread: the difference between collateral yield and bondholder yield. If mortgages yield 4% and senior bonds pay 2.5%, the 1.5% excess funds subordinate bonds (0.8%) and reserve accounts (0.7%).

In a stress scenario where collateral cash flows decline (defaults spike), the reserve account covers interest shortfalls, preventing a missed payment to bondholders.

## Triggers and protective actions

Modern securitizations include triggers tied to collateral performance:

**OC trigger**: If OC falls below a threshold (e.g., 5% for senior tranches), excess cash is diverted to pay down senior bonds, rebuilding OC.

**Delinquency trigger**: If 30+ day delinquencies exceed a percentage (e.g., 3%), a "delinquency cascade" begins: excess cash is diverted to pay down bonds faster.

**Default trigger**: If cumulative defaults exceed a percentage, certain actions occur (e.g., servicer replacement, shift to more conservative loan-loss assumptions).

**Prepayment trigger**: If prepayments exceed a certain speed, excess cash allocation changes.

Triggers are backstops. They protect investors by automatically shifting priorities if collateral deteriorates, without requiring anyone to make a judgment call.

## Originator retention and alignment

Dodd-Frank requires originators to retain at least 5% of credit risk in each securitization. Most retain the equity tranche. This "skin in the game" aligns incentives: if the originator retains equity, it has a direct financial interest in loan quality.

An originator cannot off-load all credit risk and rely on investors to bear losses. Some portion of risk stays with the creator. This should theoretically incentivize careful underwriting.

In practice, originator retention varies. Some originators hold much more than 5%, retaining significant mezzanine tranches. Others hold exactly 5% and sell the rest. The amount and type of retention signal confidence (high retention = confident; low retention = skeptical).

## Support for different asset classes

Credit support structures vary by asset class:

**Mortgages**: Typically 15–25% total subordination, 5–15% OC, interest reserves 2–3 months.

**Auto loans**: 10–15% subordination, 3–8% OC, smaller reserves (auto defaults are faster and more predictable).

**Credit cards**: 20–35% subordination, 10–15% OC, larger reserves (credit card defaults are volatile and recovery is low).

**Corporate loans**: 15–25% subordination, 2–5% OC, special provisions (revolving commitments, floating-rate risks).

The structure is calibrated to the asset class's credit characteristics. High-volatility assets need more support.

## Support adequacy and investor confidence

A securitization with substantial support (high subordination, high OC, large reserves, tight triggers) is safer and trades at tighter spreads. A securitization with minimal support (just enough to achieve its rating) is riskier and trades at wider spreads.

During normal times, minimal support might be acceptable (spreads are tight). During crisis or stress, investors flee to maximum-support deals, creating spread volatility.

Post-2008, investor demand for support increased. Many investors will not buy subordinate or mezzanine tranches in deals with less than historical norms for subordination and OC. This has pushed structures to be more conservative than pre-crisis norms.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/tranche/">Tranche</a> — subordination is the primary form of credit support.</li>
<li><a href="/wiki/overcollateralization/">Overcollateralization</a> — OC provides additional cushioning.</li>
<li><a href="/wiki/securitization/">Securitization</a> — credit support structures securitizations.</li>
<li><a href="/wiki/credit-loss-model/">Credit Loss Model</a> — models determine appropriate support levels.</li>
<li><a href="/wiki/credit-rating/">Credit Rating</a> — ratings depend on the adequacy of credit support.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/structured-finance/">Structured Finance</a> — credit support is a fundamental tool.</li>
<li><a href="/wiki/asset-backed-security/">Asset-Backed Security</a> — all ABS rely on credit support.</li>
<li><a href="/wiki/credit-risk/">Credit Risk</a> — credit support mitigates credit risk.</li>
</ul>
</div>
