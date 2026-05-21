---
title: "Dividend Adjustment (Options)"
description: "Modifications made to option terms when the underlying stock pays a dividend, preserving the option holder's economic interest."
---

*When a stock pays a [dividend](/wiki/dividend/), its price typically drops by the dividend amount on the ex-dividend date. Options are adjusted to account for this price drop to prevent economically unfair outcomes. For [call options](/wiki/call-option/), the [strike price](/wiki/strike-price/) is reduced by the dividend amount; for [put options](/wiki/put-option/), the strike is increased. These adjustments, called dividend adjustments or dividend protection, ensure option contracts remain economically equivalent despite the corporate action.*

## Why dividends matter to options

An option's value depends on the underlying stock's price. If a $100 stock pays a $2 dividend and the stock drops to $98 on the ex-dividend date, a call owner who was in-the-money is now less in-the-money—their [intrinsic value](/wiki/intrinsic-value/) has shrunk, even though the fundamental business is unchanged. Without adjustment, dividend payments would unfairly penalize call buyers and benefit call sellers. Adjustments restore fairness.

## Mechanics of call and put adjustments

For a $100 call option on a stock paying a $2 dividend: the strike is reduced to $98. This means the call holder's break-even is lower and they get the economic benefit of the dividend drop they couldn't capture (since options don't receive dividends). For a put option at $100, the strike rises to $102, increasing the put's value since the underlying has fallen and the put is now more in-the-money. The adjustments are mechanical and automatic.

## Only ordinary dividends trigger adjustments

Not all corporate actions trigger adjustments. Ordinary [dividends](/wiki/dividend/) do. Special dividends (one-time, unusually large payments) also trigger adjustments and are sometimes contractually handled differently—some contracts may specify that special dividends above a threshold receive a pro-rata adjustment of the strike. Stock splits, mergers, and other events have their own adjustment rules.

## Early exercise risk with upcoming dividends

An [American call option](/wiki/american-option/) holder facing a large [dividend](/wiki/dividend/) payment may choose to [exercise](/wiki/exercise/) early to capture the dividend—something a [protective put](/wiki/protective-put/) holder can't do. The strike adjustment is meant to compensate the call owner for not being able to capture the dividend, but it's not a perfect substitute. Some traders prefer to exercise early and hold the stock through the ex-date to pocket the full dividend.

## Implications for covered calls and puts

A [covered call](/wiki/covered-call/) writer who owns shares collects the dividend regardless of the option; the dividend adjustment has no impact on them. However, if the short call is exercised before the ex-dividend date (early assignment on an American option), the writer loses the upcoming dividend. This is why call writers monitor ex-dividend dates—assignment before the date costs them the dividend. Put sellers are unaffected by dividend adjustments in most cases unless their put is assigned.

## Interaction with strikes and moneyness

Dividend adjustments can shift the [moneyness](/wiki/moneyness/) of options. A call that was barely out-of-the-money might become in-the-money after a strike reduction due to dividend. This affects [delta](/wiki/delta/), [gamma](/wiki/gamma/), and the probability of profit at expiration. Traders need to understand whether they're looking at a pre-adjustment or post-adjustment strike when evaluating a position.

## Non-U.S. markets and less-predictable dividends

Dividend adjustments are standardized and mechanical in the U.S. equity options market because dividends are announced far in advance. In some international markets where special or extraordinary dividends are less predictable, option adjustments can surprise holders. Currency options and commodity options typically don't have dividend adjustments because their underlying assets don't pay dividends.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/dividend/">Dividend</a> — the corporate action triggering the adjustment.</li>
<li><a href="/wiki/strike-price/">Strike price</a> — what gets adjusted mechanically.</li>
<li><a href="/wiki/early-exercise/">Early exercise</a> — often motivated by upcoming dividends.</li>
<li><a href="/wiki/expiration-date/">Expiration date</a> — dividend dates and exercise windows are coordinated.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/call-option/">Call option</a> — affected by dividend adjustments.</li>
<li><a href="/wiki/put-option/">Put option</a> — also affected by dividend adjustments.</li>
<li><a href="/wiki/american-option/">American option</a> — early exercise risk due to dividends.</li>
</ul>
</div>
