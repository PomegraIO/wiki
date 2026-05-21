---
title: "Iron Condor"
description: "A four-leg option strategy combining a bull put spread and bear call spread, designed to profit from stagnation and low volatility."
---

*An iron condor sells both a put spread and a call spread simultaneously, profiting when the stock stays between two strike bands. It's the canonical income strategy for traders betting on range-bound markets.*

## What an iron condor is

An iron condor stacks four options: (1) a short put at a lower strike, (2) a long put at an even lower strike, (3) a short call at an upper strike, and (4) a long call at an even higher strike. All four typically expire the same month.

You collect net credit at entry (short put premium + short call premium, minus the cost of both long options). Maximum profit is that credit, realized when the stock stays between the short put and short call strikes through expiration. Maximum loss occurs if the stock breaks either boundary—it's the width of whichever spread was breached, minus the credit received.

The strategy is neutral—you're indifferent to direction as long as the stock consolidates.

## Why to use an iron condor

The primary appeal is **premium collection from a sideways market**. After a volatile move, stocks often trade flat for weeks or months. An iron condor collects income on that stagnation without requiring directional conviction.

A second reason is **high probability**. If you sell put and call spreads far from the current price, the stock has a wide safety margin. Many traders target 70–80% win rates by selling iron condors where the market is pricing very low odds of breach.

Iron condors also suit **portfolio overlay strategies**. Fund managers deploy them to generate 1–3% monthly returns on top of equity holdings, effectively monetizing the market's fear premium.

## When an iron condor wins

Iron condors thrive in **elevated implied volatility**. Fat option premiums mean bigger credits; you're collecting fat income while the market's pricing in fear that doesn't materialize.

They also excel in **range-bound consolidation**. After a sharp move up or down, the stock often enters a tight trading range as uncertainty resolves. An iron condor placed at the edges of that range captures most of the move's aftermath.

The strategy is ideal when **implied volatility is expected to contract**. If you enter at high IV and IV drops, both spreads shrink in value. The short legs decay faster, and your max profit is locked in early.

## When an iron condor goes wrong

If the stock breaks through either the put or call side boundary, you're at max loss on that leg. The opposite spread becomes worthless, offering no offset. A gap move through one side can wipe out your entire month's profit in one day.

Iron condors also suffer if **implied volatility spikes unexpectedly**. Both spreads widen; the long puts and calls that cost you money gain value faster than the short legs. Your unrealized loss can swing dramatically.

Late in the month, if the stock approaches one of your strikes, [gamma](/wiki/gamma/) risk becomes severe. A 1% move in the stock can swing the position 20–30%—you can go from max profit to max loss in one session.

## Mechanics and adjustment

You receive a credit at entry—typically $300–$800 per condor (selling two spreads). Maximum profit is that credit. Maximum loss is the width of either spread minus the credit (often the put side is wider for deeper ITM protection).

**Adjustment** is essential. Most traders don't let iron condors run to expiration if threatened. Common moves:
- **Rolling the threatened spread**: Buy back the short put or call at a loss, sell a new one further away from the current price.
- **Closing one side early**: Exit the threatened spread at 50% max loss, keep the profitable side.
- **Converting to a butterfly**: Buy back one of the shorts and sell another option, restructuring into a tighter payoff.

Iron condor management is a constant job—profit depends on active monitoring and swift adjustment.

## Iron condor vs. individual spreads

You could deploy a [bull put spread](/wiki/bull-put-spread/) and a [bear call spread](/wiki/bear-call-spread/) separately, getting the same payoff. Many traders do. The iron condor bundles them, which can simplify execution and reporting, but doesn't fundamentally change the math. Choose a bundled iron condor for simplicity; choose separate spreads for flexibility.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/bull-put-spread/">Bull Put Spread</a> — the put side of an iron condor.</li>
<li><a href="/wiki/bear-call-spread/">Bear Call Spread</a> — the call side of an iron condor.</li>
<li><a href="/wiki/theta/">Theta</a> — time decay that profits this strategy.</li>
<li><a href="/wiki/gamma/">Gamma</a> — acceleration risk as expiration nears.</li>
<li><a href="/wiki/implied-volatility/">Implied Volatility</a> — central to iron condor credit and profitability.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/option/">Option</a> — the contract type underlying iron condors.</li>
<li><a href="/wiki/options-greeks/">Options Greeks</a> — tools for measuring condor risk.</li>
<li><a href="/wiki/volatility-smile/">Volatility Smile</a> — affects the pricing of far-OTM spreads.</li>
</ul>
</div>
