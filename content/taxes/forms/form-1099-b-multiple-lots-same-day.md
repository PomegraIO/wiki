---
title: "Form 1099-B: Reporting Multiple Lots Sold on the Same Day"
description: "How brokers aggregate or itemize same-day sales of different lots on Form 1099-B and how you reconcile those with Form 8949."
keywords:
  - 1099-b multiple lots same day
  - form 1099-b same-day sales
  - form 8949 sales reconciliation
  - tax lot sales reporting
image: /svg/taxes.svg
---

*When you sell multiple tax lots of the same security on the same day, your broker must report those sales on Form 1099-B. The challenge is that the form may aggregate sales or list them separately, and you must reconcile each line against your own [cost basis](/cost-basis/) records on Form 8949. Knowing how your broker aggregates—and how to map that back to your actual lots—keeps your tax return accurate.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Form 1099-B Same-Day Sales — key facts</div>

<img src="/svg/taxes.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Broker aggregation rules vary; your Form 8949 must detail each lot separately.</div>

|   |   |
|---|---|
| **1099-B consolidation** | Broker may list one line (total) or multiple lines (per lot), same day |
| **Cost basis included** | If broker knows your cost basis (same account), reported on 1099-B |
| **Your matching task** | Map 1099-B lines to individual tax lots sold |
| **Form 8949 requirement** | List each lot separately with quantity, date acquired, date sold, basis, proceeds |
| **Aggregate vs. itemize** | Broker choice; neither is "wrong," but impacts reconciliation difficulty |
| **IRS matching** | IRS receives 1099-B; your 8949 must foot to the aggregate |

</aside>

## How Brokers Report Same-Day Sales

Securities brokers report stock sales on **Form 1099-B** (Proceeds from Broker and Barter Transactions). The form lists proceeds, dates, and (if known) [cost basis](/cost-basis/). When you sell 100 shares of ABC stock on a single day, the broker sends you one Form 1099-B line. But if you sell 50 shares at 10:00 a.m. and another 50 at 2:00 p.m.—or if you hold multiple lots with different acquisition dates and you sell portions of several—the broker faces a choice: consolidate into one line or break out separate lines.

**Aggregation** (one line for all same-day sales of one security):
- Broker reports total proceeds, total shares sold, average [cost basis](/cost-basis/) (if applicable)
- Simpler for the broker; cleaner form appearance
- Requires you to hand-match the aggregate to your underlying lot sales

**Itemization** (one line per tax lot sold):
- Broker reports each lot separately: 50 shares from Lot A, 50 from Lot B, with each lot's basis and proceeds
- More transparent but clutters the form
- Easier for you to reconcile if lots are clearly labeled

There is no uniform IRS mandate on aggregation vs. itemization. Broker practices vary. Some firms (like Fidelity and Vanguard) itemize by default. Others aggregate same-day sales into a single line per security. You should check your broker's policy and request itemization if clarity is important to you.

## Cost Basis Tracking and Reporting

If the broker has access to your cost basis (typically, when you purchased the shares in the same account at that broker), they include it on Form 1099-B. The IRS introduced **[basis reporting](/cost-basis/) requirements** in 2011, and coverage has expanded. For stocks, most brokers now report basis. For mutual funds and other assets, coverage is less complete.

When you hold multiple lots of a single security, the broker's cost basis figure on 1099-B reflects the lot(s) actually sold. If you sold 50 shares from a lot purchased at $50 and 50 shares from a lot purchased at $55, the form should report the weighted average ($52.50) or—if itemized—show $50 basis for the first line and $55 for the second.

**The catch:** If the broker does not itemize and you use a specific identification strategy (e.g., [FIFO](/fifo/), [LIFO](/lifo/), or average cost), the weighted average on 1099-B may not match your actual tax lot basis. This mismatch creates a reconciliation headache on your [Form 8949](/form-8949/).

## Reconciling 1099-B to Form 8949

**Form 8949** is where you list capital gains and losses in detail, lot by lot. The [Schedule D](/schedule-d/) then rolls up 8949 totals into your overall capital gain or loss figure. Here is how the reconciliation works:

1. **List each tax lot you sold**, even if 1099-B aggregates them. If you sold 50 shares from Lot A (bought $50, sold $60) and 50 from Lot B (bought $55, sold $60), Form 8949 has two lines.

2. **Proceed and basis columns** on 8949 must foot to the 1099-B total. If 1099-B shows $6,000 proceeds and you list two 8949 lines totaling $6,000, you are aligned.

3. **Basis reporting code** (Column b) on 8949 lets you indicate whether basis was reported to IRS. If 1099-B included basis, you check "Yes" for those lines. If you had to research basis yourself (e.g., for older stocks or holdings with missing records), you check "No."

4. **Adjustments and reconciliation box** at the bottom of 8949: If 1099-B shows an aggregate but you have itemized lots, make sure your separate lot gains/losses sum to the net gain/loss on 1099-B. If they do not, the form has a reconciliation problem you must explain.

## Same-Day Sales with Different Cost Methods

The complexity deepens if you use different [cost basis](/cost-basis/) methods for different lots. U.S. tax law allows several approaches:

- **[FIFO](/fifo/)** (first in, first out): Sales pull from oldest lots first
- **[LIFO](/lifo/)** (last in, first out): Sales pull from newest lots first
- **Average cost**: All lots blended at average price
- **Specific identification**: You choose which lots to sell

If you specify particular lots to your broker ("sell Lot C and Lot D today"), the broker should honor that and report accordingly. But if you did not specify, many brokers default to [FIFO](/fifo/). This matters for same-day sales because your tax filing assumes a particular method.

**Example**: You own ABC stock in three lots:
- Lot A: 100 shares, purchased 2015 at $20/share (basis $2,000)
- Lot B: 100 shares, purchased 2019 at $40/share (basis $4,000)
- Lot C: 100 shares, purchased 2024 at $50/share (basis $5,000)

On June 1, 2025, you sell 150 shares at $60/share ($9,000 proceeds). You intended to sell Lots A and C (oldest and newest for preferential tax treatment). But your broker defaults to [FIFO](/fifo/) and sells Lots A and B. The 1099-B reports:
- 150 shares sold
- Proceeds: $9,000
- Cost basis: $3,000 (average of $2,000 and $4,000)

Your Form 8949 must detail:
- Lot A: 100 shares, basis $2,000, proceeds $6,000, gain $4,000
- Lot B: 50 shares, basis $2,000, proceeds $3,000, gain $1,000
- Total: basis $4,000 (not the $3,000 average shown on 1099-B)

You note the difference and explain: "Per broker statement, basis method was [FIFO](/fifo/); actual identified lots per Form 8949 detail above." This is a disclosure, not an error, as long as your 8949 totals are transparent.

## When You Must Supply Your Own Basis

If the broker does not report basis (old stocks, securities purchased outside the current broker, inherited shares, etc.), you must research your cost basis and enter it on Form 8949. The IRS allows this; you sign a statement confirming the figures. This is laborious but necessary for accuracy.

For inherited securities, [stepped-up basis](/cost-basis/) rules typically set your basis at fair market value on the decedent's death date, not the original cost. You document this separately (from the estate tax return or appraisal) and reference it on 8949.

## Practical Tips for Same-Day Sales

- **Specify lots in writing** when you sell. Tell your broker exactly which lots you want to sell and keep a copy of the instruction.
- **Reconcile 1099-B to your trades** as soon as you receive it (typically February–March after year-end). Verify that the proceeds match your sell orders and that cost basis (if included) makes sense.
- **Create a spreadsheet** mapping each 1099-B line to your underlying tax lots. This becomes your Form 8949 template.
- **Keep all broker statements** and confirmations for at least three years (six if underreporting income > 25%). If the IRS challenges your basis claim, you need evidence.
- **Use basis-tracking software** if your brokerage offers it. Many firms provide tools to help you reconcile basis and generate 8949 entries.

## See also

<div class="wiki-seealso">

### Closely related

- [Form 8949](/form-8949/) — capital gains and losses detail; where 1099-B reconciles
- [Cost Basis](/cost-basis/) — basis determination and reporting to IRS
- [FIFO](/fifo/) — first-in, first-out cost method
- [LIFO](/lifo/) — last-in, first-out cost method
- [Schedule D](/schedule-d/) — summary of capital gains and losses
- [Tax Lot](/tax-lot/) — individual parcel of a security purchase

### Wider context

- Long-Term Capital Gain Tax — preferential tax rate for holding period >1 year
- [Capital Gains Tax](/capital-gains-tax-investor/) — overall framework for investment income taxation
- [Wash Sale](/wash-sale/) — rule preventing loss carryforward after repurchase
- [Tax Loss Harvesting](/tax-loss-harvesting/) — strategy using realized losses for deductions

</div>
