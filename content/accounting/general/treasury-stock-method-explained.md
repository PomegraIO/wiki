---
title: "Treasury Stock Method Explained"
description: "How the treasury stock method calculates dilution from in-the-money options and warrants in diluted EPS calculations."
keywords:
  - treasury stock method
  - diluted earnings per share
  - in-the-money options
  - option dilution
  - treasury shares
---

*The **treasury stock method** is the standard formula used to calculate dilutive share count from in-the-money employee stock options, warrants, and convertible securities when computing [diluted earnings per share](/earnings-per-share/). It answers a simple question: if all these options were exercised today, how many shares would remain outstanding after the company repurchased shares at current market price with the exercise proceeds?*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Treasury Stock Method — dilution formula</div>

<img src="/svg/accounting.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Converts option exercise value into net new share count for EPS dilution.</div>

|   |   |
|---|---|
| **Basic formula** | (shares if exercised − shares repurchased) = incremental dilution |
| **Shares if exercised** | number of [in-the-money](/in-the-money/) options outstanding |
| **Exercise proceeds** | (shares × [exercise price](/exercise-price/)) |
| **Shares repurchased** | proceeds ÷ [current stock price](/stock/) |
| **When applies** | Diluted EPS, convertible securities, warrant valuation |
| **No dilution if** | options are out-of-the-money or proceeds exceed repurchase capacity |

</aside>

## Why the Method Exists

Under [GAAP](/generally-accepted-accounting-principles/) (ASC 260) and [IFRS](/international-financial-reporting-standards/) (IAS 33), companies must report two earnings-per-share numbers: basic (actual shares outstanding) and diluted (assuming all [in-the-money](/in-the-money/) securities are converted to shares).

The challenge: a company with 100 million shares and 10 million [in-the-money](/in-the-money/) options could simply count all 110 million shares in the denominator. But that ignores the fact that exercising options generates cash — proceeds the company could use to repurchase and retire some of those new shares. If the option is substantially in the money, the repurchase might cancel out most or all of the dilution.

The treasury stock method models this logic: assume the company gets the exercise cash and buys back shares at the current price. The *net* new shares represent true dilution.

## The Calculation, Step by Step

Suppose a company has:
- Stock price: $50
- 10 million [in-the-money](/in-the-money/) options with [exercise price](/exercise-price/) of $30
- Current [shares outstanding](/stock/): 100 million

**Step 1: Shares from exercise.**
If all 10 million options are exercised, 10 million new shares appear: 100 + 10 = 110 million.

**Step 2: Exercise proceeds.**
Exercise price × number of options = $30 × 10 million = $300 million.

**Step 3: Shares repurchased.**
The company uses $300 million to buy back shares at $50 each: $300M ÷ $50 = 6 million shares retired.

**Step 4: Net dilution.**
110 million (post-exercise) − 6 million (repurchased) = **104 million shares** for diluted EPS.

The diluted [earnings per share](/earnings-per-share/) uses 104 million in the denominator instead of 100 million. If net income is $400 million, diluted EPS is $400M ÷ 104M = **$3.85**, versus basic EPS of $400M ÷ 100M = **$4.00**.

## When Options Don't Dilute

If options are deeply out of the money, they simply don't enter the diluted count. If the stock price drops to $25 and all options have a $30 [exercise price](/exercise-price/), exercising them would be irrational — no one exercises a call option below its [strike price](/strike-price/). The treasury stock method assumes zero shares issued, zero proceeds, zero repurchase, zero dilution.

Even if slightly in the money, some options may contribute negligible dilution. If the stock trades at $31 and 1 million options have a $30 [strike price](/strike-price/), exercise proceeds are $30 million. At $31 per share, that buys 0.97 million shares — nearly offsetting the 1 million issued. Net dilution: only ~30,000 shares.

## Warrants and Other Securities

The same method applies to [warrants](/exercise-price/) (long-dated call options often issued in financing rounds) and to conversion features embedded in convertible bonds or [preferred stock](/preferred-stock/). For a [convertible bond](/convertible-bond/), the question is: if converted into common stock, what is the dilution?

A 4% coupon bond convertible into 25 shares trades at $1,000 par. Stock price is $35. If converted:
- 25 new shares are issued.
- The company avoids $40 annual coupon (4% of $1,000) — an after-tax savings depending on the [tax rate](/marginal-tax-rate-investor/).
- Simplified: the company could use the coupon savings to repurchase shares at $35. At $40 annual coupon, it buys ~1.14 shares per year, which over the bond's life reduces net dilution.

Under [ASC 260](/generally-accepted-accounting-principles/), the treasury stock method assumes the company uses the after-tax value of foregone coupon payments to repurchase shares. Dividends on the converted shares are not subtracted — the company receives no "proceeds" from dividends; they simply transfer cash to shareholders.

## Weighted Average: Timing and Contingencies

Diluted [earnings per share](/earnings-per-share/) uses a **weighted average** share count over the reporting period. If options are exercised partway through the year, the treasury stock method calculates dilution as if exercised at the beginning, weighted by the months outstanding.

Similarly, if options vest in tranches or are conditional on performance, diluted EPS includes only the shares that are *probable* to vest under the contingency rules.

## If Exercise Proceeds Exceed Repurchase Capacity

The treasury stock method has a ceiling: a company can't repurchase more shares than the exercise proceeds allow. However, there's also a floor: if the company has excess cash and the option is deeply in the money, some companies argue they could repurchase *more* than the exercise proceeds (using other cash). 

Under strict [GAAP](/generally-accepted-accounting-principles/), the treasury stock method uses only the option proceeds — not other available cash. This prevents distortions from variations in cash balance or [dividend](/dividend/) policy. The exception: if a company has announced plans to use other cash for a share repurchase program, that repurchase activity enters the calculation.

## Sector Nuance: Technology Stock Options

Tech companies with large employee-option programs often have 15–25 million options outstanding in a company of 400 million shares. When deep in the money (stock up 5–10x from grant), the dilution can be substantial even after the treasury stock repurchase.

Conversely, during downturns, many options move out of the money and contribute zero dilution. This creates a paradoxical "beating the street" dynamic: a company might see its diluted share count *decline* if options go underwater, even as it repurchases fewer shares. For investors comparing year-over-year [earnings per share](/earnings-per-share/), this volatility is a red flag — it indicates EPS growth may partly reflect option expiration rather than business performance.

## Practical Impact on Valuation

Analysts often use diluted share count (post-treasury stock method) as the denominator for [price-to-earnings-ratio](/price-to-earnings-ratio/) and other per-share metrics. A stock trading at $100 with diluted EPS of $5 trades at a 20x [P/E](/price-to-earnings-ratio/). But if treasury stock dilution is understated (because the model assumes shares are repurchased at current price, not below), true dilution may be larger and the multiple higher.

The treasury stock method does *not* account for future option grants. Each year, companies award new options, which will eventually dilute shareholders. The method captures only *existing* in-the-money options. Investors scrutinizing long-term [return on equity](/return-on-equity/) and competitive advantage must weigh annual option grants alongside reported dilution.

## See also

<div class="wiki-seealso">

### Closely related

- [Earnings Per Share](/earnings-per-share/) — the per-share metric diluted EPS serves
- [In-the-Money](/in-the-money/) — the condition triggering treasury stock method inclusion
- [Exercise Price](/exercise-price/) — the hurdle rate determining dilution magnitude
- [Convertible Bond](/convertible-bond/) — securities using the same treasury stock approach
- [Share Buyback](/share-buyback/) — the repurchase mechanism offsetting dilution

### Wider context

- [Generally Accepted Accounting Principles](/generally-accepted-accounting-principles/) — ASC 260 governs diluted EPS rules
- [Employee Stock Options](/exercise-price/) — the primary driver of tech-company dilution
- [Option Premium](/option-premium/) — the value investors pay for in-the-money leverage
- [Price-to-Earnings Ratio](/price-to-earnings-ratio/) — valuation metric affected by diluted share counts
- [Return on Equity](/return-on-equity/) — long-term metric distorted by unaccounted future option grants

</div>
