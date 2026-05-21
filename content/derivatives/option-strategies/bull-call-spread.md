---
title: "Bull Call Spread"
description: "A two-leg option strategy that caps both risk and profit by buying and selling calls at different strikes, typically used when expecting modest upside."
---

*A bull call spread reduces the cost of bullish exposure by offsetting a long call with a higher-strike short call. It turns unlimited upside into a defined profit window, making it attractive when capital is limited or conviction is moderate.*

## What a bull call spread is

A bull call spread pairs a long [call option](/wiki/call-option/) at a lower strike with a short call at a higher strike, both expiring the same week or month. You buy the cheaper (more in-the-money or less out-of-the-money) call and sell the more expensive one, netting a debit. If the stock rises above your long call's strike, you profit; if it stays below, you lose your initial debit. Profit caps at the difference between the two strikes minus what you paid.

The strategy is neither fully bullish nor fully neutral—it's optimism with guardrails. You're betting on upside without betting the farm.

## Why to use a bull call spread

The primary reason is **cost reduction**. A naked long call can be expensive; selling a call against it recovers 30–60% of that cost in premium, lowering your break-even. For traders with limited capital, spreads are essential.

A second reason is **risk definition**. Losses never exceed your initial debit. You can calculate exact worst-case scenarios before entering, which appeals to risk-conscious traders and portfolio managers.

Third, spreads work well in **mildly bullish markets**. If you're confident in a directional move but unsure of magnitude, a spread beats a naked call—you don't oversell volatility, and your payoff matches your conviction level.

## When a bull call spread wins

Bull call spreads shine when implied [volatility](/wiki/implied-volatility/) is elevated. Selling the higher strike call generates fat premium, which offsets the long call's cost. If volatility then contracts post-entry, both legs decline in value, but the short call's decay works in your favor.

The strategy also wins in **consolidation after a spike**. If the stock jumps into earnings, then trades sideways, the spread's built-in short call bleeds time decay while your long call has already captured the intended move.

Spreads suit defined-return profiles: if your thesis is "stock rallies 10%, not 50%," a spread frames that boundary.

## When a bull call spread misfires

If the stock tanks hard, your long call expires worthless and you keep nothing; you've lost the full debit paid upfront. The short call provides no safety net in sharp declines—it only limits upside.

Spreads also lose money if the stock consolidates just below your long strike. You've paid to be directionally right, but timing matters; being early by one week means full loss.

Implied volatility spikes harm spreads asymmetrically. If IV jumps after you enter, your short call gains value faster than your long call, widening the loss. You're short volatility without meaning to be.

## Mechanics and adjustment

Entry cost is `long call premium – short call premium`, typically $100–$400 on standard contracts. Maximum profit is `(difference between strikes) – (net debit)`. Maximum loss is the net debit paid.

Many traders adjust bull call spreads by **rolling up** the short call if the stock rallies hard. You buy back the short call at profit, sell an even higher strike, and extend the expiration. This locks in some gains while keeping upside alive. Rolling is optional and riskier than holding to expiration.

## Bull call spread vs. outright call purchase

An outright long call offers unlimited upside and requires no secondary management. A bull call spread caps profit but cuts your cost in half and defines risk on day one. Choose spreads when capital is scarce or conviction is moderate; choose naked calls when you're deeply bullish and can afford the premium.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/bear-call-spread/">Bear Call Spread</a> — short-biased analog using two calls at different strikes.</li>
<li><a href="/wiki/call-option/">Call Option</a> — the long-call leg of a bull call spread.</li>
<li><a href="/wiki/bull-put-spread/">Bull Put Spread</a> — similar strategy using puts instead of calls.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — affects spread premiums and entry costs.</li>
<li><a href="/wiki/strike-price/">Strike Price</a> — defines the two levels in a bull call spread.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — the contract type underlying all spreads.</li>
<li><a href="/wiki/derivatives/">Derivatives</a> — broader asset class.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring spread sensitivity.</li>
</ul>
</div>
