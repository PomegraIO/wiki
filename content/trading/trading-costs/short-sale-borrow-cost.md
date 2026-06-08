---
title: "Short Sale Borrow Cost"
description: "The stock-borrow fee paid by short sellers, how rates vary from easy-to-borrow to hard-to-borrow securities, and impact on trade profitability."
keywords:
  - short sale borrow cost
  - stock borrow fee
  - short seller borrow cost
  - hard-to-borrow securities
  - borrow rate short selling
image: /svg/trading.svg
---

*A **short sale borrow cost** is the fee a [short-selling](/short-selling/) trader pays to borrow stock from a broker or lender. The rate varies dramatically by security: easy-to-borrow stocks (like mega-cap indices) might cost just 5–10 basis points per year, while hard-to-borrow microcaps can cost 10–50% per year or more. High borrow costs can turn a promising short thesis into an underwater trade.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Short Sale Borrow Cost — Key Facts</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A daily fee accrued proportionally to the value and duration of a short position; set by supply and demand for borrowed shares.</div>

|   |   |
|---|---|
| **What it is** | Fee to borrow stock for short selling; paid daily to the lender |
| **Quoted as** | Annual percentage rate (e.g., "3% borrow rate"); charged daily based on days held |
| **Who sets the rate** | Broker or stock-lending desk; varies by supply/demand for that specific stock |
| **Easy-to-borrow** | Mega-cap, high-volume stocks; rates 0.05–0.25% per year |
| **Hard-to-borrow** | Microcaps, recently shorted, low float; rates 2–50%+ per year |
| **Paid by** | Short seller directly (reduces profit) or embedded in short fee at closeout |
| **Impact** | Larger on longer-duration shorts; can exceed expected profit |

</aside>

## Why short sellers must borrow

When you short a stock, you sell something you don't own. The buyer expects to receive actual shares at settlement (usually T+2, two business days later). Where do those shares come from? You must borrow them from someone who owns them: a long-term investor, a mutual fund, or an ETF. The lender agrees to lend the shares and expects to be compensated.

The borrowing cost is passed to the short seller. A trader shorting 10,000 shares of a stock quoted at 3% borrow rate is liable for annual interest of: 10,000 × current price × 0.03. If the stock trades at $100, that's $30,000 per year, or roughly $82 per day. Over a week-long short, you'll pay about $570 in borrow costs before you account for the profit or loss from the stock price move.

## How borrow rates are set

Borrow rates are determined by **supply and demand** for loanable shares, managed through a stock-lending market.

**Abundant shares:** If many investors own the stock and are willing to lend it out (often passively through their brokers' securities lending programs), supply is ample. Borrowing is cheap: 0.05–0.25% per year.

**Scarce shares:** If few shares are available (small float, concentrated ownership, or high short interest already exhausting available lendable shares), borrow rates spike. A heavily shorted microcap might quote 5–50% per year.

Most large brokers have a "stock-borrow desk" that negotiates rates and manages inventory. They balance:
- **Lender demand:** Funds want lending yield; if rates are too low, they don't participate.
- **Borrower demand:** Short sellers compare the borrow cost to their profit opportunity; if costs are too high, they don't short.
- **Inventory:** If the borrow desk has many shares available, it lowers rates to move inventory. If shares are scarce, it raises rates to conserve inventory.

Real-time borrow-rate quotes are available through major brokers and stock-lending platforms. Rates update as supply and demand shift, sometimes intraday.

## Easy-to-borrow vs. hard-to-borrow

**Easy-to-Borrow (ETB) stocks:**

These are mega-cap, highly liquid securities like the components of the [sp-500-index](/sp-500-index/). Examples: Apple, Microsoft, Amazon. Borrow rates are typically 0.05–0.50% per year. Many ETFs are ETB as well.

A short seller is unlikely to face borrow restrictions on these; the broker can almost always locate shares from its lending pool.

**Hard-to-Borrow (HTB) stocks:**

These are lower-liquidity, lower-float securities, or stocks already heavily shorted. A recently IPO'd stock, a distressed company, or a microcap with few outstanding shares might have HTB status.

Borrow costs climb. Rates of 5–20% per year are common; in extremes, rates have hit 100%+ (quoted as "borrow rate unavailable" or the broker simply refuses to lend). On a $50 stock with 10% borrow cost, a short seller pays $5 per share per year.

Example: A short seller bets a microcap stock will fall from $50. The borrow rate is 8%. If the stock takes 6 months to fall as expected, the short seller pays:
- Borrow cost: $50 × 0.08 × (6/12) = $2 per share
- If the stock falls 20%, the short profits $10 per share
- Net profit: $10 – $2 = $8 per share (still profitable, but reduced)

If borrow cost were 30% and the trade takes 12 months:
- Borrow cost: $50 × 0.30 × 1 = $15 per share
- Stock falls 20%: $10 per share profit
- Net loss: –$5 per share (unprofitable, despite being right on direction)

## Borrow cost compounds over time

Like [overnight-financing-cost-cfd](/overnight-financing-cost-cfd/) on leveraged positions, short-sale borrow costs accrue daily. They're quoted as annual rates but charged proportionally to the number of days held.

**Daily charge = (Position value) × (Annual borrow rate) / 365**

On a $100,000 short position with 8% annual borrow rate:
- Daily cost: $100,000 × 0.08 / 365 = $21.92 per day
- Monthly cost: ~$657
- Annual cost: $8,000

A short seller expecting a stock to fall 15% but who must hold for 18 months faces 18 months of compounding borrow costs. If borrow rates rise (because more shorts pile in), the cost compounds faster.

## Factors affecting borrow availability and rates

**Float size:** Stocks with small floats (few shares outstanding) are harder to borrow. A microcap with 1 million shares outstanding but 50 million shorted shares in short interest is in severe borrow squeeze. Brokers may not allow new shorts, or rates spike to 50%+.

**Short interest:** When many traders are already shorting a stock, lendable inventory becomes scarce. New short sellers face higher rates or inability to borrow at all.

**Recent offerings:** After a company announces a secondary offering, shares flood the market (assuming successful underwriting), driving borrow rates down as supply soars.

**Forced recalls:** If a large lender (e.g., a fund) decides to sell all shares and needs them back immediately, it can "recall" borrowed shares. Short sellers are forced to buy back and cover at inopportune prices. This is rare but has forced short-squeeze situations.

**Corporate actions:** Stock splits, reverse splits, or special distributions can temporarily disrupt borrow markets as shares change form.

## Estimating impact on short profitability

A short seller should calculate borrow cost upfront and factor it into the profit threshold. If you believe a stock will fall 10% and borrow costs are 5% annually, and you're planning a 6-month hold:

- Expected profit from price: 10%
- Borrow cost (6 months): 5% × 0.5 = 2.5%
- Net expected return: 10% – 2.5% = 7.5%

If borrow cost is 15% (hard-to-borrow stock):
- Net expected return: 10% – 7.5% = 2.5% (much tighter margin of safety)

Many short sellers abandon positions if borrow cost spirals above 10–15% annualized, because the risk-reward deteriorates: they need outsized stock declines to overcome borrowing costs.

## Borrow cost and market efficiency

Short-sale borrow costs are a form of market friction. High borrow costs on distressed or heavily-shorted stocks make short selling expensive and reduce the supply of short capital. This can allow mispriced securities to persist longer than fundamental analysis would suggest.

Conversely, abundant cheap borrow supply on mega-cap ETFs and blue-chips enables active short-sellers to constantly test valuations, contributing to [price-discovery](/price-discovery/).

## Managing borrow cost in a short trade

- **Locate shares early:** Some brokers allow you to "locate" shares before entering the short, locking in a borrow rate. Delaying location can result in higher rates later if inventory tightens.
- **Hedge with options:** A short seller might buy a [call-option](/call-option/) to cap upside risk, rather than hold an expensive short outright.
- **Use stock-lending revenue:** Some brokers pass stock-lending revenue back to short sellers if they lend out their positions. This can offset or exceed borrow costs.
- **Pair trades:** A short seller might simultaneously long a related stock (e.g., short a competitor) to benefit from relative value, offsetting borrow costs via the relative move.
- **Exit early if rates soar:** If borrow rates spike due to unexpected short interest or supply tightness, exit the short position rather than fight rising costs.

## See also

<div class="wiki-seealso">

### Closely related

- [Short Selling](/short-selling/) — The mechanics and risks of betting on stock declines
- [Overnight Financing Cost in CFD and Margin Trading](/overnight-financing-cost-cfd/) — Similar daily-compounding costs on leveraged positions
- [Market Impact of a Large Order](/market-impact-large-order/) — Execution costs that apply to short entry and exit
- [VWAP as an Execution Cost Benchmark](/vwap-execution-cost-benchmark/) — Evaluating the quality of short execution
- [Call Option](/call-option/) — Used to hedge short positions and cap upside risk
- [Put Option](/put-option/) — Alternative synthetic short using options
- [Bid-Ask Spread](/bid-ask-spread/) — The cost of immediacy on short entry and exit

### Wider context

- [Squeeze](/short-selling/) — Price surge driven by short covering when borrow availability tightens
- [Short Interest](/short-selling/) — Market gauge of betting against a company
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulator of short-selling and stock-borrow disclosure
- [Price Discovery](/price-discovery/) — Role of shorting in testing and establishing fair values
- [Leverage Ratio](/leverage-ratio-forex/) — Shorting is leveraged in that small moves have outsized impact
- [Counterparty Risk](/counterparty-risk/) — Risk the broker or lender fails during a short position

</div>
