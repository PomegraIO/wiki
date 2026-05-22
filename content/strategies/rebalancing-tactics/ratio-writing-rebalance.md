---
title: "Ratio Writing Rebalance"
description: "Selling more call options than shares held to raise capital while maintaining an equity position."
keywords:
  - covered call
  - ratio writing
  - call selling
  - capital raising
  - rebalancing
---

*In **ratio writing**, an investor sells more [call options](/wiki/call-option/) than the number of shares they own, using the premium income to fund capital needs while keeping the underlying stock. A naked or partially covered position, this tactic is riskier than [covered calls](/wiki/covered-call/) but less capital-intensive when raising cash.*

<div class="wiki-hatnote">
Closely related to <a href="/wiki/covered-call/">/covered-call/</a> (same number of calls as shares). For the mechanics of call selling and assignment, see <a href="/wiki/call-option-equity/">/call-option-equity/</a>.
</div>

<aside class="wiki-infobox">

| Aspect | Detail |
|---|---|
| **Position structure** | Long shares + short calls (calls exceed shares) |
| **Capital raised** | Premium from call sales |
| **Maximum profit if uncalled** | Capped by call strike |
| **Unlimited loss if shares drop** | Below the call strike minus premium collected |
| **Assignment risk** | Partial if only some calls are in-the-money |
| **Suitable for** | Bullish outlook with capital needs |

</aside>

## How ratio writing differs from covered calls

A covered call writer owns 100 shares and sells 1 call, capping upside at the strike while keeping downside risk. A ratio writer might own 100 shares but sell 2 or 3 calls, generating larger premium income. The benefit is obvious: more cash up front. The risk is equally clear: if the stock rises sharply above the call strike, the writer is forced to deliver shares on one call but does not own enough shares to cover the others. They must buy back the naked calls at a loss or sell shares at below the market value to cover assignment.

The position is a form of [naked call writing](/wiki/naked-short-selling-ban/), though "naked" calls are the portion unhedged by stock. Because assignment exposes the writer to theoretically unlimited loss if the stock rallies, ratio writing is not suitable for all accounts. Some brokers prohibit it entirely or restrict it to experienced traders; others require additional margin.

## A concrete example

An investor owns 100 shares of a stock trading at $50. Rather than sell 1 call at $52 strike for $2.00 premium ($200 total), they sell 2 calls at the same strike for $1.90 each ($380 total). The extra $180 cash comes from the extra call sold.

- If stock stays below $52, both calls expire worthless. The investor keeps all $380 premium and retains the 100 shares.
- If stock rises to $55, both calls are exercised. The investor delivers 100 shares against one call at $52 (locked in price). The second call requires buying 100 shares in the market at $55 to cover—a loss of 3 points per share, or $300. Net: +$380 premium, −$300 loss on the short delivery = +$80.
- If stock rises to $60, the naked call loss widens to $800 (buying at $60 to deliver at $52). Net: +$380 premium, −$800 loss = −$420 total.

## When ratio writing makes sense

Ratio writing is suitable when:

1. **Capital need is acute and near-term.** You need cash in the next 30–60 days but are willing to risk the shares.
2. **Stock outlook is neutral to mildly bullish.** You expect the stock to stay below the call strike, or you're comfortable allowing it to be called away.
3. **Premium difference is substantial.** Selling 2 calls instead of 1 must meaningfully increase cash flow to justify the naked-call risk.
4. **Account size can absorb loss.** The margin requirement for the naked portion (typically 20% of strike value) and the theoretical loss must fit within portfolio risk tolerance.

It's a tactic more commonly seen in hedging operational risks. For instance, a corporate executive with concentrated [restricted stock](/wiki/restricted-stock/) might use ratio writing to fund tax payments due on [vesting](/wiki/vesting-restricted-stock/) without selling shares outright. Or a mutual fund rebalancing away from equities might use ratio writing on stocks they're trimming to raise the capital faster.

## Risk management and alternatives

Ratio writers must monitor the underlying stock closely. If it rallies toward the strike, the writer faces a decision: hold and accept the risk of naked-call loss, or buy back the extra calls (closing the naked position) and pocket a smaller profit. Many ratio writers set standing buy-back orders at 50% of the call premium to lock in gains early.

A less risky alternative is **call-ratio spread**: sell 2 (or more) calls at a higher strike and buy 1 call at a lower strike, financing the naked portion. This caps maximum loss but also reduces net premium collected.

Another alternative is [ratio put spreading](/wiki/put-ratio-spread/), where the writer sells more puts than covered by cash, to raise capital while waiting for a stock to decline. This shifts the risk profile.

## Tax implications

[Call option](/wiki/call-option/) assignment triggers a capital gain or loss on the delivered shares. If the writer has held the stock long-term, the gain is long-term [capital gain](/wiki/capital-gains-tax-investor/). The call premium is taxed as ordinary income in the year received (not as a capital gain), though assignment results in a wash for gains/losses on the underlying.

The holding period of the original shares is disrupted by assignment; shares delivered are treated as sold on assignment date, and the tax lot must be tracked carefully for purposes of [basis](/wiki/cost-basis/) and [wash sale](/wiki/wash-sale/) rules.

## When ratio writing goes wrong

The most common failure is when the stock gaps higher on an earnings surprise or sector rotation. A ratio writer caught unaware can see the naked call position swing from a "free money" trade to an emergency margin call in hours. Several well-publicized blowups in retail trading (2021–2023) involved ratio call writers who were forced to buy back at market close, suffering 5–7 figure losses.

The position is also subject to [assignment](/wiki/assignment/) risk on the short side. If early assignment occurs (usually only on dividend ex-date or in the final days before expiration), the writer must be prepared to cover the naked calls immediately.

<div class="wiki-seealso">

### Closely related

- [Covered call](/wiki/covered-call/) — The safer baseline: sell 1 call per 100 shares held
- [Call option](/wiki/call-option-equity/) — Mechanics of call buying and selling
- [Call ratio spread](/wiki/call-ratio-spread/) — Hedged version using both long and short calls
- [Naked call](/wiki/naked-short-selling-ban/) — The regulatory framework for naked options

### Wider context

- [Options Greeks](/wiki/options-greeks/) — Delta, gamma, theta used to manage ratio positions
- [Assignment](/wiki/assignment/) — Mechanics of call exercise and share delivery
- [Capital gains tax](/wiki/capital-gains-tax-investor/) — Tax consequence of assignment
- [Margin trading](/wiki/forex-margin/) — Financing the naked portion of the position

</div>