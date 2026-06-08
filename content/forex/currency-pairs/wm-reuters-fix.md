---
title: "WM/Reuters Fix"
description: "The daily 4 pm London benchmark rate for currency pairs, its calculation methodology, and the LIBOR-scale manipulation scandal that exposed its vulnerability."
keywords:
  - forex benchmark
  - currency fixing
  - wm/reuters fix
  - benchmark manipulation
  - fx market microstructure
image: "/svg/forex.svg"
---

*The **WM/Reuters Fix** is a daily currency benchmark set at 4 pm London time, calculated from a sample of the largest FX transactions and indicative quotes during a 60-second window. For three decades it anchored billions in currency transactions and benchmarks before becoming the epicentre of a manipulation scandal that reshaped regulation of financial benchmarks globally.*

## The 4 pm London snapshot

The WM/Reuters Fix gets its name from the partnership between Thomson Reuters (the data and calculation agent) and State Street's Foreign Exchange Division (WM), formed in 1994. At precisely 4 pm London time each business day, Thomson Reuters samples the spot FX market—collecting prices from the largest e-brokers, banks, and market makers. For the 60 seconds around that timestamp, it captures executed trades and streaming quotes, then calculates a volume-weighted midpoint for each major currency pair.

This single number became the day's "official" exchange rate for an enormous range of financial contracts: pension funds settling their currency exposure at month-end, corporations closing the books on overseas revenue, index providers rebalancing funds, and custodians settling billions in FX transactions on behalf of clients. A bank or hedge fund that traded EUR/USD during the day but wanted to lock in a known settlement price would reference the WM/Reuters Fix as objective, transparent, and (supposedly) resistant to manipulation.

The 4 pm London slot was not arbitrary. It sat at the midpoint of the overlap between US and European trading sessions, when trading volume in major pairs was heaviest and the price discovery most efficient. By publishing the day's fix at this moment, it created a quasi-official closing price for global FX.

## Methodology: transparency that hid vulnerability

Thomson Reuters collected its data from multiple sources: electronic communication networks (ECNs), streaming brokers, and requests for indicative prices sent directly to major banks. For each currency pair, it would rank the contributions by volume, then weight them accordingly. Outlier prices were flagged and sometimes excluded. The entire process was published in detailed methodology documents.

Yet this very transparency masked a structural weakness: the 60-second window was narrow, and the number of true wholesale transactions during that window was finite. If a bank or consortium of banks wanted to move the fix in their favour, they could—in theory—time large trades or indicative quotes to flood the window with one-directional pressure. Because the fix was used to settle trillions of dollars in actual contracts, even a move of a few pips in their desired direction would yield enormous profits on those underlying positions.

The WM/Reuters Fix sat on the surface of the market, visible to all. What lay beneath was a smaller, more manipulable pool of quotes than most market participants realised.

## The manipulation scandal and fallout

In 2013, investigations by UK and US authorities uncovered systematic manipulation of the WM/Reuters Fix by major banks, particularly around month-end and quarter-end when fixing-based settlement volumes spiked. Traders at institutions including Barclays, UBS, RBS, Citi, and JPMorgan would coordinate trades and indicative quotes to push the fix in a direction that benefited their client-facing business or their own proprietary positions.

The scale was staggering. One trader at UBS admitted to moving the dollar/yen fix by as much as 0.3 per cent in a single day—a move that appears small in percentage terms but that, applied to positions worth billions, amounted to tens of millions in profit. Unlike the simultaneous LIBOR scandal, which involved individual banks submitting false rates, WM/Reuters manipulation often entailed trading *around* the window or flooding it with strategic quotes—technically not submitting false data, but using real trading activity to distort price discovery at a crucial moment.

Regulators from the Financial Conduct Authority in London to the Commodity Futures Trading Commission in the US fined the involved institutions more than $2 billion in aggregate. The reputational damage extended beyond the fined banks: the WM/Reuters Fix's credibility, already under pressure from the LIBOR revelations, suffered a blow from which it would never fully recover.

## Transition and legacy

By 2015, the FCA had declared the WM/Reuters Fix the subject of official "determination" as a critical benchmark. New rules required more rigorous input validation, oversight by compliance teams, and firewalls between trading desks and the contributors feeding data into the calculation. Thomson Reuters and WM implemented stricter sampling windows, anonymisation of contributors, and real-time monitoring for anomalous activity.

But institutional memory had shifted. Pension funds and asset managers began diversifying their fixing references, using multiple benchmarks or moving settlement windows to earlier times of day when the likelihood of concentrated manipulation was lower. Some large custodians shifted away from the 4 pm London fix entirely, instead settling FX transactions using earlier snapshots or real-time net settlement.

The WM/Reuters Fix persists today, still widely used in structured products, bonds, and corporate accounting. Yet it is no longer the unremarkable standard it once was. It serves as a historical marker of an era in which global benchmarks sat atop little visible scrutiny—and a warning that price discovery in even the largest markets can be compromised when incentives align and enforcement lags.

## See also

<div class="wiki-seealso">

### Closely related

- [LIBOR](/libor/) — the interbank interest rate benchmark that revealed systematic manipulation
- Benchmark manipulation — regulatory definition and enforcement
- [Price discovery](/price-discovery/) — the mechanism by which spot FX rates emerge from trading activity
- [Spot exchange rate](/spot-exchange-rate/) — the rate implied by contemporary transactions

### Wider context

- Forex market microstructure — how bid-ask spreads and order flow shape FX pricing
- [Market maker trading](/market-maker-trading/) — the role of liquidity providers in FX benchmarks
- [Regulatory overreach](/dodd-frank-act/) — how post-2008 regulation reshaped benchmark governance
- [Over-the-counter market](/over-the-counter-market/) — the decentralised structure that enabled fixing manipulation

</div>
