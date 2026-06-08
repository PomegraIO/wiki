---
title: "Trading Options on ADRs"
description: "Learn how options on ADRs work, which depositary receipts have listed options, and how depositary ratios affect contract specifications."
keywords:
  - adr options trading how it works
  - american depositary receipt options
  - listed options contracts ADR
  - depositary ratio settlement
image: /svg/equity.svg
---

*Options on American Depositary Receipts ([ADRs](/adr/)) offer traders direct hedging and directional exposure to foreign stocks traded in dollars on U.S. exchanges. These **ADR options** are standard listed contracts, but their structure depends critically on the depositary ratio — how many foreign shares each ADR represents — which can make contract specifications non-standard and settlement mechanics non-obvious.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">ADR Options — Contract Essentials</div>

<img src="/svg/equity.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">Foreign stock hedging in dollars: the depositary ratio is your contract decoder.</div>

|   |   |
|---|---|
| **Underlying** | The ADR itself (one contract = 100 ADRs by default) |
| **Strike and expiration** | Same as standard options (monthly, quarterly, LEAP) |
| **Ratio variants** | 1:1, 2:1, 5:1 (ADR to foreign shares) — changes contract size |
| **Settlement type** | Cash or physical delivery of ADRs, depending on the option |
| **Key risk** | Depositary ratio changes or delisting can alter terms mid-contract |
| **Listing exchanges** | CBOE, NASDAQ, NYSE Arca for major ADRs; not all ADRs have listed options |

</aside>

## Which ADRs Have Listed Options

Not every ADR has listed options. The market has consolidated on major, high-volume ADRs: Alibaba (BABA), Samsung (SSNLF), Toyota (TM), ASML (ASML), SAP (SAP), and Novo Nordisk (NVO) all have deep option markets. Dozens of others — smaller-cap or less liquid foreign names — have limited or no options.

The key driver is volume and spreads. A market maker will list options only if they can generate tight bid-ask spreads and reliable volume. This favors large-cap, frequently-traded ADRs whose underlying stock is itself liquid in its home market. A small-cap Mexican bank's ADR, even if it trades, may have no options at all.

Before assuming an ADR has options, traders should check the Chicago Board Options Exchange (CBOE) or NASDAQ OMX options chain databases. The absence of options often means that a levered exposure to the foreign stock requires buying the ADR itself and using [margin](/leverage-ratio-forex/) or buying a direct foreign-listed option (more complex, less convenient, often more expensive).

## The Depositary Ratio and Contract Specification

This is where many traders stumble. A standard options contract controls 100 shares of stock. An ADR options contract also controls 100 ADRs — but how many foreign shares that represents depends on the depositary ratio.

If Samsung's ADR has a 1:1 ratio (one ADR = one share), then one call option on Samsung ADR gives the right to buy 100 ADRs = 100 shares. The contract works exactly like owning 100 Samsung shares on the Korean exchange.

But some ADRs have ratios of 2:1, 5:1, or even higher. For example:

- **ASML (one of the largest ADRs)** trades at a 1:1 ratio: one ADR = one Dutch share.
- **Airbus (EADSY)** was historically at a 1:10 ratio: one ADR = 10 Airbus shares. One call option controls 1,000 Airbus shares notionally.
- **Novo Nordisk (NVO)** trades at 1:1.

When the ratio is not 1:1, the contract size published by the exchange is already adjusted. You do not have to manually multiply. One call still controls "100 shares of stock equivalent" after the ratio adjustment. But this means that different ADRs have different contract sizes measured in notional foreign share equivalents, and an amateur trader can easily miscalculate exposure or hedge ratios.

## Settlement Mechanics and Physical Delivery

Most equity options in the U.S. settle in cash: you exercise, and the exchange moves money into your account. ADR options can settle differently depending on the contract terms.

If an ADR option is **cash-settled**, you exercise a call, the option is worth the intrinsic value at expiration, and you receive cash. Your position closes automatically.

If an ADR option is **physically settled**, you exercise a call, and you receive 100 ADRs (adjusted for the depositary ratio) at the strike price. This is common for many major ADRs. You then own the ADRs and can hold them, sell them, or redeem them for foreign shares with the depositary bank.

This matters for margin and cost basis. If you exercise a deep in-the-money call 100 times to accumulate ADRs, you now hold a large stock position with full margin requirements. If the option is cash-settled, your option profit is realized in cash and you have flexibility.

Conversely, some sophisticated traders intentionally exercise into ADRs to acquire a position at a set price, then hold or divest the ADRs in the secondary market. The optionality of physical delivery makes ADR options valuable for international rebalancing strategies.

## How to Hedge an ADR Position with Options

A U.S.-based investor who owns Samsung ADRs (SSNLF) and worries about downside can buy a put option. A put's strike and expiration determine the insured floor.

But the calculation is straightforward only at 1:1 ratios. If the investor owns 10,000 ADRs and Samsung's ADR is 1:1, buying 100 put contracts (each controlling 100 shares) hedges the entire position. If the depositary ratio were 5:1, owning 10,000 ADRs would control 50,000 foreign shares, so the hedge would require 500 put contracts to match.

The depositary bank's public disclosure of the ratio is the starting point. Most ADRs also specify the ratio in their ticker symbol or the options exchange listing. Missing this step is a common source of under-hedged or over-hedged positions.

## Why ADR Options Matter for Foreign Exposure

U.S. investors often face two paths to foreign stock exposure: buy the ADR in dollars, or open a foreign brokerage account and trade the stock in its native currency and exchange. ADR options bridge a gap.

If a trader believes Toyota will fall, they can buy a put on Toyota's ADR (TM) on the NASDAQ without opening a Japanese brokerage account or dealing with yen volatility. The contract is denominated in dollars, settles in U.S. markets, and is regulated by the SEC. This simplicity is worth the small premium over cheaper Japanese options markets.

Conversely, for an options trader familiar with foreign markets, the ADR option may be more expensive than buying a contract on the foreign exchange directly. This arbitrage (buying cheap foreign options, selling rich ADR options) is exploited by market makers and professional traders, which tends to keep ADR option prices competitive.

## Non-Standard Events and Contract Adjustments

A complication unique to ADRs is that the depositary bank can change the ratio, consolidate, or split the ADR if the foreign company undergoes capital actions.

If Samsung were to do a 2-for-1 stock split in Korea, the bank might adjust the ADR ratio from 1:1 to 2:1 (each ADR now represents 2 Korean shares). The SEC and the depositary bank have rules for how this adjusts outstanding option contracts, but the mechanics can be opaque to retail traders.

Example: You own an in-the-money call option on Samsung at a 1:1 ratio. If the bank changes the ratio to 2:1, the option contract size adjusts, your strike adjusts, and the intrinsic value is preserved — but your contract now controls 100 × 2 = 200 Korean shares notionally instead of 100. The economic value is the same, but the mechanics changed without your action.

Similarly, if a foreign company delists from its home exchange or the ADR facility is terminated, the options may be settled or converted to cash based on a final determination by the depositary bank. These are rare but known events (e.g., BHP Billiton, ABB) and can trigger forced liquidation.

## Liquidity and Bid-Ask Spreads

Liquidity in ADR options varies enormously. The largest ADRs (BABA, TM, ASML, NVO, SAP) have multi-dollar notional bid-ask spreads measured in cents, often tighter than the underlying foreign options on home exchanges. Smaller ADRs have spreads of 10–50 cents or wider, making options impractical for small accounts.

Check the options chain's open interest and volume before entering an ADR options trade. An option with zero open interest and minimal daily volume might not be tradeable on the exit, leaving you forced to hold to expiration or abandon the position.

## See also

<div class="wiki-seealso">

### Closely related

- [American Depositary Receipt](/adr/) — The underlying: foreign stock wrapped in a dollar-denominated U.S. security.
- [Option](/option/) — Basics of calls, puts, strikes, and expiration.
- [Derivatives Hedging](/derivatives-hedging/) — Why and how to use options to hedge stock positions.
- [Options vs. Forwards](/forward-contract-vs-futures-contract-differences/) — Comparing optionality with locked-in forward price exposures.
- [Currency Risk](/currency-risk/) — ADRs eliminate currency translation, but expose you to the foreign company's risk.

### Wider context

- [Stock Exchange](/stock-exchange/) — Where ADRs trade (NASDAQ, NYSE); where options are listed (CBOE, NASDAQ OMX, NYSE Arca).
- [Equity Financing](/equity-financing/) — Foreign companies use ADRs to tap U.S. capital and broaden shareholder bases.
- [Volatility Smile](/volatility-smile/) — Advanced option pricing concepts that apply equally to ADR options.
- [Basis Risk](/basis-risk/) — The gap between ADR option prices and foreign options on home exchanges.

</div>
