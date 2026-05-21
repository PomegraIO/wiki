---
title: "Basis Swap"
description: "A swap that exchanges cash flows tied to two different floating-rate indices to profit from or neutralize differences in their rates."
---

*A basis swap is an agreement to exchange interest payments on two different floating-rate indices, with no fixed rate. Both legs float, but each is pegged to a different reference—typically SOFR versus LIBOR, or two different tenor versions of the same index.*

<div class="wiki-hatnote">Do not confuse the basis swap (a derivative contract) with the <a href="/wiki/basis/">basis</a> (the difference between a futures price and spot price).</div>

## Why basis swaps exist

When two floating-rate indices trade at different yields—either because they reference different markets or different tenors—there is a spread between them called the basis. A basis swap lets a borrower or investor exploit, neutralize, or hedge that spread.

The most common type: someone borrows at SOFR + 2%, but their natural source of returns is tied to LIBOR. If LIBOR-SOFR spread widens, they lose money even though they correctly anticipated the level of rates. A basis swap lets them exchange SOFR payments for LIBOR payments (or vice versa) to align their funding and earning streams.

## Structure

A basis swap has two floating-rate legs:
- **Leg A**: pays Floating Index A (e.g., 3-month SOFR) + spread A.
- **Leg B**: pays Floating Index B (e.g., 3-month LIBOR) + spread B.

The spread (or basis) is set at inception and is fixed; it is the only fixed quantity in the contract. The difference between the two floating rates floats for the life of the swap, and that is exactly the point: the swap holder is betting on the basis spreading or tightening.

Example: a swap where Party A pays SOFR flat and receives LIBOR + 10 basis points. If LIBOR and SOFR are currently equal, Party A is receiving 10 bps. If SOFR jumps 20 bps but LIBOR stays flat, Party A is now receiving -10 bps (paying). The swap isolates exposure to the LIBOR–SOFR spread, not to the absolute level of rates.

## Key variations

**SOFR-LIBOR basis swap**: Exchanges floating payments on SOFR (the new risk-free rate) for LIBOR (the older, panel-bank-based rate). This is heavily used as the financial industry transitions away from LIBOR. A borrower with a LIBOR-linked loan uses a SOFR-LIBOR basis swap to lock in the expected spread.

**Tenor basis swap**: Both legs reference the same underlying index (e.g., SOFR) but with different tenors. For example, 3-month SOFR versus 6-month SOFR. Banks use these to manage mismatches between their funding and lending tenors.

**Cross-currency basis swap**: A hybrid that combines basis-swap and [currency-swap](/wiki/fx-swap/) features, exchanging LIBOR in one currency for a different floating index in another currency.

## Valuation and pricing

A basis swap is valued as the difference between the present values of the two floating legs. Because both legs are floating, the notional principal can be recovered at par at inception (both legs are worth the notional). The "swap rate" is the fixed basis (spread) that makes the two legs equal in value.

Dealers price basis swaps by:
1. Projecting each floating index forward using appropriate [forward curves](/wiki/forward-exchange-rate/).
2. Discounting the projected cash flows to present value.
3. Solving for the basis that equates the two legs.

When a borrower enters a basis swap, they are saying: "I am willing to pay the mid-market basis in order to neutralize the spread risk between these two indices." The bid-ask spread on a basis swap is usually wider than on a vanilla [interest-rate swap](/wiki/interest-rate-swap/) because the basis is less liquid and harder to hedge.

## Uses

**Liability hedging**: A borrower with SOFR-based debt that earns LIBOR-based returns uses a basis swap to convert LIBOR income into SOFR, matching the liability.

**LIBOR transition**: As LIBOR phase-out proceeded, borrowers and lenders used SOFR-LIBOR basis swaps to lock in the spread they would pay or receive if they switched benchmarks.

**Tenor management**: A bank that borrows in 3-month tenors but lends in 6-month tenors can use a tenor basis swap to hedge the timing mismatch.

**Speculative positioning**: A trader who believes the LIBOR-SOFR spread will narrow (i.e., LIBOR will fall relative to SOFR) can go long LIBOR and short SOFR in a basis swap, pocketing the gains if they are right.

## Risks

**Basis risk**: The spread between the two indices can move unexpectedly, and a hedge might not work perfectly. A company hedging LIBOR exposure with SOFR is exposed to basis risk—the possibility that the spread widens despite rates moving as expected.

**Liquidity risk**: Basis swaps are less liquid than vanilla [interest-rate swaps](/wiki/interest-rate-swap/). If you need to exit early, you may face a wide bid-ask spread or difficulty finding a dealer willing to take the other side.

**Index discontinuation risk**: LIBOR is being phased out entirely in most tenors by 2025. A long-dated basis swap on LIBOR indices carries the risk that the index ceases to be published, and cash settlement mechanics take over.

**Counterparty risk**: Like all swaps, a basis swap exposes both parties to [counterparty risk](/wiki/counterparty-risk/)—the possibility that the other party defaults. However, because both legs are floating and typically close in value, the [replacement cost](/wiki/counterparty-risk/) is usually small.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the parent category of derivative contracts.</li>
<li><a href="/wiki/interest-rate-swap/">Interest-rate swap</a> — the most common swap; basis swaps are a variation with two floating legs.</li>
<li><a href="/wiki/fx-swap/">FX swap</a> — a cross-currency swap that combines basis-swap logic with currency conversion.</li>
<li><a href="/wiki/sofr/">SOFR</a> — the secure overnight financing rate, increasingly the reference for basis swaps.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/basis/">Basis</a> — the underlying spread concept that motivates basis swaps.</li>
<li><a href="/wiki/libor/">LIBOR</a> — the legacy floating rate being phased out.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the risk that the other party fails to pay.</li>
</ul>
</div>
