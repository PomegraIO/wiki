---
title: "Overnight Indexed Swap"
description: "A swap that exchanges a fixed rate for the daily compounded return of an overnight rate, used for cash management and short-term hedging."
---

*An overnight indexed swap (OIS) is a contract where one party pays a fixed rate and the other pays the total return from compounding a daily overnight rate (such as SOFR or SONIA) over the life of the swap. It isolates exposure to short-term rate expectations and is heavily used by banks, central banks, and money market participants.*

## Structure and mechanics

An OIS links the floating leg to an overnight reference rate that resets daily:

**Fixed leg**: Party A pays a fixed rate (the "OIS rate") once at maturity.

**Floating leg**: Party B pays the cumulative return from daily compounding of SOFR (Secured Overnight Financing Rate) or another overnight index. Each day, the overnight rate compounds forward. At maturity, Party B's payment is:

$$ \text{Notional} \times \left[ \prod_{i=1}^{n} \left(1 + \frac{r_i \times d_i}{360}\right) - 1 \right] $$

where r_i is the overnight rate on day i and d_i is the number of calendar days in that period.

Settlement typically occurs once at maturity. No interim cash flows. Both legs are usually in the same currency.

## Why overnight swaps matter

**Separates Fed expectations from term premium**: An [interest-rate swap](/wiki/interest-rate-swap/) on 3-month SOFR includes both short-term rate expectations and a term premium (compensation for extending duration beyond one day). An OIS isolates pure short-term expectations. The overnight rate compounds so frequently that longer-term expectations matter less.

**Trading Fed policy**: Investors use OIS to bet on where the Fed will set short-term rates. If an OIS to a specific date is 5.1%, the market is pricing in an average Fed Funds target of ~5.1% to that date.

**Balance sheet relief**: Banks use OIS to hedge their overnight deposit funding. A bank that borrows nightly at SOFR + 10 bps can swap to fixed via an OIS, locking in a known cost.

## Uses and applications

**Fed policy pricing**: The Fed Funds Futures contract is the traditional tool for betting on Fed moves. But OIS are preferred by many because they:
- Are settled against the actual overnight rate, not a cash-settled futures index.
- Can be customized to any date.
- Are more liquid in certain maturities.

A trader expecting the Fed to cut by 25 bps within three months would buy an OIS (receive fixed) to profit if the OIS rate falls, reflecting expectations of lower overnight rates.

**Hedging overnight funding**: A bank with overnight liabilities (demand deposits, overnight borrowing) that reprices daily uses an OIS to convert floating overnight costs to fixed. This lowers funding uncertainty.

**Cross-currency OIS**: A bank that borrows overnight dollars but has euro liabilities uses a cross-currency OIS to swap the overnight dollar rates into overnight euro rates. Less common than vanilla OIS but useful for multicurrency treasuries.

**Repo curve hedging**: The [repo market](/wiki/repurchase-agreement/) is essentially an overnight lending market. A dealer that finances a securities portfolio in repo can hedge the cost with OIS.

## Valuation and pricing

An OIS is priced as the fixed rate that equates the present value of both legs:

1. **Floating leg PV**: Discount the expected cumulative overnight return using the [zero-coupon discount curve](/wiki/zero-coupon-bond/).

2. **Fixed leg PV**: Discount the fixed payment.

3. **Solve for the rate**: Find the fixed OIS rate that makes them equal.

The OIS rate is typically close to the market expectation of the average overnight rate over the period. For example, if the Fed Funds target is 5.0% to 5.25%, and a 3-month OIS is 5.1%, the market is pricing in an average Fed Funds rate near 5.1% over the next three months.

Dealers adjust for:
- **Credit spread**: Compensation for the risk the counterparty defaults.
- **Liquidity**: Less liquid OIS (longer tenors) have wider spreads.
- **Curve shape**: If the overnight curve is steep, forward rates are higher, affecting the OIS price.

## Common underlyings

**SOFR (U.S.)**: The primary OIS rate in dollars. Replaced [LIBOR](/wiki/libor/)-based OIS.

**SONIA (UK)**: The sterling overnight index average. The primary OIS rate in pounds.

**EURIBOR OIS (Eurozone)**: European version, though less common than SONIA or SOFR OIS.

**TONAR (Japan)**: Japanese overnight rate. OIS on TONAR is used for yen management.

## OIS spread and implied Fed expectations

The **OIS spread** (also called the Fed Funds target path) is the difference between the OIS rate and the current Fed Funds target midpoint. 

If the Fed Funds target is 5.0% - 5.25% (midpoint 5.125%) and a 1-month OIS is 5.0%, the OIS spread is approximately -12.5 bps, suggesting the market expects the Fed to cut rates during the month.

Traders closely monitor OIS curves to gauge Fed expectations. A flat or inverted OIS curve (longer-dated OIS lower than shorter-dated) signals expectations of rate cuts. A steep OIS curve (longer OIS higher) signals rate hike expectations.

## Risks

**Liquidity risk**: While common, OIS can be illiquid in certain tenors (e.g., very long-dated OIS beyond 5 years). Dealers may quote wide spreads or decline to trade.

**Basis risk**: The overnight rate you actually pay (due to credit or operational factors) may differ from the OIS rate you lock in.

**Model risk**: Pricing depends on assumptions about future overnight rates and discount factors. Different models can give different prices.

**Counterparty risk**: The dealer might default. Less of a concern for very short-dated OIS (1 month) but more relevant for longer dated OIS.

**Rate shock risk**: If the Fed moves unexpectedly, OIS rates can move sharply. The longer the OIS term, the larger the potential move.

## Market conventions

- **Tenors**: Most liquid are 1, 3, 6, and 12 months. OIS also trade out to 30 years (for pension and insurance hedging) but with wider spreads.
- **Maturities**: Often on fixed dates (e.g., 1 month from now, next Fed meeting date, next quarter-end).
- **Notional**: Can be very large (hundreds of millions) for bank treasury operations.
- **Settlement**: Typically once at maturity (final settlement).
- **Daycount**: Usually 360-day year (money market convention).

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/swap/">Swap</a> — the foundational derivative structure.</li>
<li><a href="/wiki/interest-rate-swap/">Interest-rate swap</a> — the longer-dated cousin of OIS.</li>
<li><a href="/wiki/sofr/">SOFR</a> — the primary overnight rate referenced in OIS.</li>
<li><a href="/wiki/sonia/">SONIA</a> — the UK overnight index.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/federal-funds-rate-target/">Federal Funds Rate Target</a> — what OIS pricing reflects.</li>
<li><a href="/wiki/repurchase-agreement/">Repurchase agreement</a> — the overnight lending market that OIS helps manage.</li>
<li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the primary risk in OTC swaps.</li>
<li><a href="/wiki/zero-coupon-bond/">Zero-coupon bond</a> — used to discount OIS cash flows.</li>
</ul>
</div>
