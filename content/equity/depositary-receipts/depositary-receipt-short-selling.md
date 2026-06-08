---
title: "Short Selling Depositary Receipts"
description: "The mechanics and constraints of borrowing and short-selling ADRs and GDRs versus the underlying ordinary shares."
keywords:
  - can you short sell adr depositary receipt
  - short selling adr
  - gdr short selling mechanics
  - depositary receipt borrowing
image: "/svg/equity.svg"
---

*Yes, you can short-sell [ADRs](/adr/) and [GDRs](/adr/), but the mechanics differ slightly from shorting ordinary shares. A short seller borrows an ADR from a lender, sells it on a U.S. exchange, and must later buy it back to return it. The custodian bank holds the underlying ordinary shares; movements between ADR and ordinary markets, settlement rules, and availability of borrows all introduce friction. Shorting depositary receipts is feasible but often less liquid and more costly than shorting the home-market ordinary shares, especially for volatile or thin-volume receipts.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ADR Short Selling — key facts</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Shorting depositary receipts is possible but subject to borrow availability and custodian settlement rules.</div>

|   |   |
|---|---|
| **Borrowing mechanism** | Short seller borrows ADR from prime broker or lender; ADR is loaned just like ordinary stock |
| **Borrow availability** | Often tighter for ADRs than home-market ordinary shares; lower float and fewer shares outstanding |
| **Borrow costs** | Lending fees (short borrow fee) typically higher for ADRs, especially if supply is thin |
| **Settlement and custody** | ADR custodian controls underlying shares; settlement timing between ADR and home market can lag |
| **Arbitrage friction** | Price gaps between ADR and ordinary market create short-covering risk for the arbitrage trader |
| **Regulatory restrictions** | Home country may restrict or prohibit short selling of local shares; ADR shorting may sidestep local bans |

</aside>

## How ADR Short Selling Works

A **short seller** wants to profit from a falling ADR price. The mechanics mirror ordinary stock shorting but with added layers.

1. **Borrow the ADR:** The short seller contacts a prime broker or securities lender and borrows ADR shares. The lender typically holds the ADR in a margin account or securities lending account. The short seller receives the ADR and a borrow fee (often 0.5–3% annualized, but can spike to 10%+ for hard-to-borrow receipts).

2. **Sell on the U.S. exchange:** The short seller sells the borrowed ADR on NASDAQ, NYSE, or another U.S. exchange, receiving cash.

3. **Wait for the price to fall:** The short seller hopes the ADR price declines.

4. **Buy back and return:** The short seller buys the ADR at a lower price, returns it to the lender, and keeps the difference (minus borrow fees and transaction costs).

For example, a short seller borrows 1,000 Samsung ADRs at $70/share, receiving $70,000. Samsung weakens, and the ADRs fall to $65/share. The short seller buys back 1,000 at $65,000, returns them, and nets $5,000 profit before fees.

## Why ADR Shorting Is More Difficult Than Ordinary Stock

ADRs are typically far less liquid than the home-market ordinary shares. Samsung has a massive float and very high daily volume on the Korean Stock Exchange; Samsung ADRs on NYSE, by contrast, are lower-volume. Fewer ADRs exist because each ADR represents a ratio (e.g., one ADR = 1/4 ordinary share) and the custodian bank only deposits ordinary shares when there is demand for ADRs.

**Borrow availability is constrained.** If few ADRs are in circulation, there are fewer shares available to borrow. A short seller may find borrowing 100,000 ADRs is not feasible; the lender simply does not have that many to loan. By contrast, borrowing 100,000 ordinary Samsung shares is trivial given the massive home-market float.

**Borrow costs spike.** Scarce inventory commands a premium borrow fee. A short seller might expect to pay 0.5% annualized to short ordinary Samsung shares in Korea; the ADR borrow might cost 5–15% annualized if it is hard to find.

**Settlement and arbitrage risk.** The custodian bank (usually a large international bank like Citibank or JP Morgan) holds the underlying ordinary shares and issues ADRs in response to deposit requests. If the ADR price diverges from the ordinary share price (adjusted for the ratio), arbitrageurs capitalize by buying cheap ordinary shares, depositing them for ADRs, and selling the ADRs—or vice versa. But this arbitrage is not instantaneous. Settlement delays between the home market and the U.S. market, currency conversion time, and custodian processing create windows of price friction.

A short seller who is also long ordinary shares (or vice versa) as a hedge faces this timing mismatch: buying back the ADR and selling ordinary shares to lock in profit may not settle simultaneously, leaving the position exposed.

## ADR Shorting When Home-Country Restrictions Exist

In some countries, regulators restrict or ban short-selling of ordinary shares to stabilize markets. France and Italy have periodically imposed short-sale bans on financial stocks. During such bans, short selling is illegal in the home market.

But shorting the ADR on a U.S. exchange is typically not prohibited by the home country—it occurs in U.S. jurisdiction under U.S. law. A trader who cannot short a stock in Paris may be able to short the ADR on NYSE.

However, regulators and the custodian bank are aware of this gap. The custodian may tighten ADR issuance during a local short-sale ban to prevent large discrepancies between ADR and ordinary prices, reducing the short-seller's ability to borrow. And some banks have policies restricting ADR shorting when the underlying shares are banned from shorting domestically, to avoid facilitating circumvention.

## Comparing ADR Shorting to Ordinary-Share Shorting

| Dimension | ADR Shorting | Ordinary-Share Shorting |
|---|---|---|
| **Liquidity** | Lower volume, wider spreads | Typically tighter, deeper |
| **Borrow cost** | Often 2–10%+ annualized | Often 0–2% annualized |
| **Borrow availability** | May be scarce, especially for non-U.S. companies | Usually abundant for major stocks |
| **Currency exposure** | ADR price is in USD; ordinary shares in home currency | Home-currency risk for ADR short sellers |
| **Settlement** | U.S. T+2 settlement plus custodian delays | Home-market settlement rules |
| **Arbitrage risk** | Price gaps between ADR and ordinary; arbitrage lag | Minimal; single market |
| **Regulatory gaps** | Can short when home-market bans exist | Subject to home-country restrictions |

## Practical Constraints

**Liquidity constraints:** A trader wanting to short millions of dollars of ADRs may find the market too thin. If ADR volume is 100,000 shares per day and the trader wants to short 500,000 shares, it will take 5+ days to accumulate the short, during which the price may move.

**Borrow squeezes:** If a large holder of an ADR decides to recall lent shares or reduce lending supply (e.g., to vote at a shareholder meeting or to exit a position), the short squeeze can be severe. The borrow fee can spike from 2% to 20% in days, eating into profits.

**Dividend and corporate-action timing:** When a company pays a dividend on ordinary shares, the custodian bank adjusts the ADR ratio or distributes a cash dividend to ADR holders. A short seller owes the dividend to the lender. Timing mismatches and currency conversion can create unexpected costs.

**Holding period and carry:** For a long-duration short (holding the position for months or years), the cumulative borrow fee and dividend liability can dwarf the gain from a modest price decline. A 15% decline over 2 years sounds attractive until you subtract 30% in accumulated borrow costs.

## Margin and Regulatory Requirements

ADR shorts are subject to the same U.S. margin rules as ordinary stock shorts (Regulation T requires 150% of proceeds in a margin account). Some brokers treat ADRs as higher-risk and impose stricter margin requirements (200–250%).

The short seller must also comply with SEC Rule 10a-1 (the uptick rule) if applicable, and position limits if trading on behalf of a hedge fund or other regulated entity.

## See also

<div class="wiki-seealso">

### Closely related

- [ADR](/adr/) — Overview of American depositary receipts and their creation
- [Depositary Receipt Short Selling](/depositary-receipt-short-selling/) — This article's core topic
- [Short Selling](/short-selling/) — General mechanics of selling borrowed securities
- [Borrow and Lending Markets](/depositary-receipt-short-selling/) — How securities lending works
- [GDR](/adr/) — Global depositary receipts and shorting considerations

### Wider context

- [Arbitrage](/depositary-receipt-short-selling/) — ADR-ordinary share arbitrage strategies
- [Market Maker](/market-maker-trading/) — How dealers provide ADR liquidity
- [Liquidity Risk](/liquidity-risk/) — Thinness and spreads in secondary markets
- [Currency Risk](/currency-risk/) — USD exposure for cross-border short sellers
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — U.S. regulatory framework

</div>
