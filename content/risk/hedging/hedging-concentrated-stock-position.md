---
title: "Hedging a Concentrated Stock Position"
description: "Techniques to hedge concentrated stock exposure—collars, prepaid forwards, exchange funds, protective puts—without triggering immediate tax on unrealized gains."
keywords:
  - hedging concentrated stock position
  - collar hedge strategy
  - prepaid variable forward
  - exchange fund hedge
  - protective put concentrated position
  - tax-efficient hedge
---

*Holding a **concentrated stock position**—a large stake in a single company—creates both opportunity and risk. A **hedging a concentrated stock position** refers to techniques like collars, protective puts, prepaid variable forwards, and exchange funds that let you reduce downside exposure and diversify without immediately selling and triggering capital gains tax.*

## Why Concentration Matters

A single stock can represent 30%, 50%, or even 80% of a portfolio—common when an employee has vested equity, inherited shares, or founded a company. The position may be deeply profitable, with a very low [cost basis](/cost-basis/). Selling immediately to diversify incurs a large [capital gains tax](/capital-gains-tax-investor/) bill, often 20%–37% federal plus state tax, depending on holding period and income.

Yet holding on creates idiosyncratic risk. If that company stumbles—regulatory setback, management failure, industry disruption—the entire portfolio suffers. The optimal strategy for many investors is to keep the position but reduce its downside exposure and gradually diversify into other assets.

## Protective Put: Simple But Expensive

The most straightforward approach is to buy a [protective put](/protective-put/)—an out-of-the-money put option on the stock. If the stock falls below the strike price, the put gains value, offsetting losses.

Example: You own 1,000 shares of a $150 stock, position value $150,000, with a $30 cost basis. You buy a 1-year put with a $130 strike. If the stock drops to $100, the put is worth roughly $30,000, offsetting most of the portfolio's loss. If the stock rises to $200, you let the put expire worthless and capture the full upside.

The tradeoff is [option premium](/option-premium/). A deep out-of-the-money put (far below the current stock price) is cheap but offers little protection. An at-the-money or near-the-money put is expensive—often 3–7% of position value per year. Over a 5-year horizon, that's a 15–35% drag on returns, a meaningful cost.

Protective puts also don't solve concentration; they only cushion the fall. Your portfolio is still 80% or 90% in one stock. Other hedges actively reduce exposure.

## The Collar: Zero or Near-Zero Cost

A collar is a **protective put** combined with a **covered call**. You buy a put at a lower strike and sell a call at a higher strike. The call premium partially or fully offsets the put cost, creating a hedge that costs little or nothing.

Example: Stock at $150, cost basis $30.
- Buy a 1-year $130 put (cost: $6,000).
- Sell a 1-year $180 call (receive: $6,000).
- Net cost: $0.

The payoff is capped. If the stock rises to $250, you are forced to sell at $180 due to the call assignment. You forfeit the $50–$70 per share above $180. If it falls to $100, the put protects you at $130.

This trade-off—protection down, upside capped—appeals to investors who have already made substantial gains and want to lock them in while preserving most downside safety. It is also tax-efficient: the collar itself is usually a non-event for tax purposes, though the eventual sale of the stock (whether by call assignment or voluntary) triggers gains.

Collars are widely used by executives with concentrated founder stock or employee equity. They are easy to enter and exit, liquid in the options market, and flexible. The main drawback is surrendering outsized upside if the stock rallies past the call strike.

## Prepaid Variable Forward (PVF)

A **prepaid variable forward** is a more sophisticated financial structure. In a PVF, you enter a forward contract with a bank: you agree to sell shares in the future (typically 1–3 years) at a price to be determined within a range at that time. In exchange, the bank pays you cash now—often 80–95% of the current market value.

Example: Stock at $150. The bank pays $135 cash today. In 2 years, you deliver shares worth anywhere from $120 to $180 (a typical range). If the stock is at $150, you deliver at $150. If it has soared to $200, you deliver at the $180 floor. If it has crashed to $100, you deliver at the $120 floor (but you have already received $135 cash, so your net loss is small).

The PVF defers taxation. The forward contract itself is not a taxable event. You recognize the gain when you finally deliver shares in 2–3 years, giving you deferral benefit and time to plan.

The structure is complex and involves counterparty risk (the bank must pay and accept the shares). It typically requires working with a financial advisor or investment bank and is most practical for very large concentrated positions ($1 million+). Costs and structuring are not transparent and can add up.

## Exchange Funds

An **exchange fund** (or swap fund) is a partnership into which multiple investors contribute appreciated securities. Each investor receives fund shares, and the fund manager diversifies the pool into many holdings. The exchange itself is usually a non-taxable event under Section 1031 principles (or closely modeled on it), though the IRS has scrutinized these more carefully in recent years.

Once the shares are exchanged for fund interests, your single-stock concentration is gone. The fund acts like a mutual fund or ETF holding dozens of stocks. You have diversified without a taxable sale.

The catch: You are locked into the fund for typically 7–10 years. The fund is illiquid. Fees are higher than a standard index fund. Diversification happens at entry; no ongoing rebalancing occurs from your perspective. If the market collapses shortly after you join, you are stuck waiting out the holding period.

Exchange funds made more sense before low-cost [ETFs](/etf/) and index funds existed. Today, they are less common but still available for very large (>$5 million) concentrated positions in situations where deferral is critical.

## Share Lending and Buying to Close

For very large, well-known stocks, you can lend shares to short-sellers and collect a borrowing fee. Lending doesn't change your tax status (you still own the shares), but it generates income. The fee may be 0.05–2% per year, depending on how scarce the shares are.

Some investors combine lending with buying a call option, creating a synthetic structure. You lend shares, collect the fee, use part of the fee to buy a call that limits downside, and maintain tax deferral. This is more technical and requires careful execution, but it can work on large, liquid positions.

## Tax Considerations and Timing

The key to any concentrated-position hedge is understanding the tax timeline. A protective put or collar does not trigger a gain immediately. You recognize gains only when you sell or the stock is called away. If you hold for more than one year, any gain is long-term [capital gains tax](/capital-gains-tax-investor/) (preferential rates).

A Section 1045 or Section 1244 rollover, if available, can defer gains. Many founders who sell a concentrated position and reinvest the proceeds in new startup equity can defer tax under Sec. 1045, provided strict timing rules are met.

Timing a hedge is also tax-relevant. If you buy a protective put before the stock has risen further, you lock in a baseline. If you wait for the stock to double, the put is more expensive. The calculus shifts based on when you plan to eventually exit.

## See also

<div class="wiki-seealso">

### Closely related

- [Using Futures to Hedge a Small Portfolio](/futures-hedge-for-small-portfolio/) — Futures-based hedges for smaller, diversified portfolios
- [Protective Put](/protective-put/) — Core mechanics of buying downside protection
- [Covered Call](/covered-call/) — Selling call options against a stock position
- [Derivatives Hedging](/derivatives-hedging/) — Broad principles of hedging with options and forwards
- [Cost Basis](/cost-basis/) — How your entry price affects gain or loss calculations
- [Capital Gains Tax (Investor)](/capital-gains-tax-investor/) — Tax rates and timing rules for stock sales

### Wider context

- [Concentration Risk](/concentration-risk/) — Why concentrated positions are risky
- [Diversification](/diversification/) — The case for spreading investments
- [Options](/option/) — How option contracts work
- [Forwards and Futures](/forward-contract/) — Fixed future delivery and pricing
- [Tax Loss Harvesting](/tax-loss-harvesting/) — Other tax-aware strategies for managing positions

</div>
