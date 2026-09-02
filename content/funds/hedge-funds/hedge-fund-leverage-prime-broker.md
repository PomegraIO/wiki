---
title: "Hedge fund leverage and prime broker"
description: "The financing and operational infrastructure that hedge funds use to access leverage, borrow securities, and execute trades through prime brokers."
---

*Hedge funds obtain leverage through prime brokers—financial institutions that provide financing, securities lending, clearing, and operational services—enabling funds to amplify returns but also magnifying losses and creating counterparty risk.*

<aside class="wiki-infobox">
  <div class="wiki-infobox-title">Hedge Fund Leverage and Prime Broker — key facts</div>
  <table>
    <tr><th>Prime broker role</th><td>Financing, securities lending, clearing, operations</td></tr>
    <tr><th>Leverage typical</th><td>2-to-1 to 5-to-1 for long-short funds; up to 10-to-1 for arbitrage</td></tr>
    <tr><th>Financing costs</th><td>Repo rate (overnight repo, term repo) plus haircut</td></tr>
    <tr><th>Key risk</th><td>Prime broker failure; collateral rehypothecation</td></tr>
  </table>
</aside>

A hedge fund cannot operate without leverage, and leverage requires a prime broker. A prime broker is a bank or securities firm that provides financing, securities lending, clearing, settlement, and a suite of operational services. Goldman Sachs, Morgan Stanley, JPMorgan, and Citadel Securities are among the largest prime brokers. Without a prime broker, a hedge fund is limited to investing its own capital; with one, it can amplify that capital by 2x, 3x, or more.

## The prime broker's role

**Financing and margin**: The prime broker lends cash to the hedge fund, secured by the fund's portfolio. If a fund has $100 million in capital and borrows $200 million, it can deploy $300 million in assets. The financing is typically done via [repurchase agreements](/wiki/repurchase-agreement/) (repos), where the fund sells securities to the prime broker and agrees to buy them back later at a slightly higher price, with the difference representing interest.

**Securities lending**: The fund may want to short-sell a stock (betting it will fall). To do so, the fund must borrow the stock from the prime broker, who borrows it from their clients (other institutional investors with custodial accounts). The fund pays a borrow fee (typically 0.1 to 1 percent annually, but sometimes much higher for hard-to-borrow stocks) and returns the stock later.

**Clearing and settlement**: The prime broker executes trades on behalf of the fund, clears them through clearinghouses, and settles (exchanges cash and securities). This is behind-the-scenes plumbing that is essential but often invisible to the investor.

**Operational services**: Prime brokers provide technology, reporting, and administrative support. The fund can access real-time data on its positions, cash flows, and risk metrics through the prime broker's platform. They handle reconciliation, compliance reporting, and custody of assets.

## The cost and structure of leverage

Leverage has a cost. If a prime broker finances a position via repos at 2 percent per year, and the underlying asset yields 4 percent, the fund nets 2 percent (4% yield minus 2% financing cost). If the fund can do this at 3x leverage with $3 million deployed on $1 million of capital, the gross return is 6 percent ($3M * 2%) on $1M, or 6 percent. But after paying the prime broker's fees for financing, services, and clearing (another 0.5 to 1 percent), the fund nets 4 to 5 percent—a respectable return on capital if returns are compared to Treasuries (3 to 4 percent), but modest relative to the leverage and risk taken.

The cost of leverage varies with market conditions. In normal times, repo rates are tight and financing is cheap. In stressed periods (like September 2019 or March 2020), repo rates spike and financing becomes expensive. A fund that budgeted for 2 percent financing costs might face 5 percent costs unexpectedly, wiping out profits. This is why hedges funds monitor repo rates obsessively and diversify their prime broker relationships to ensure financing access if one prime broker tightens credit.

## Haircuts and margin calls

When a hedge fund borrows via repo, the prime broker takes a haircut—it lends less than the market value of the securities pledged as collateral. If the fund pledges $100 million in Treasury bonds, the prime broker might lend $98 million (a 2 percent haircut). This protects the prime broker: if the bond value falls and the fund defaults on the repo, the prime broker owns bonds worth $98 million against a $98 million loan.

Haircuts vary with asset class and market conditions. Government bonds have low haircuts (0.5 to 1 percent); corporate bonds have higher haircuts (2 to 5 percent); equities have even higher haircuts (5 to 15 percent); and illiquid or complex securities might have haircuts of 30 percent or more. In a crisis, haircuts can spike overnight. A security that had a 5 percent haircut might suddenly have a 20 percent haircut if credit spreads widen sharply. This forces the fund to post additional collateral or reduce its leverage.

A margin call is when the prime broker demands the fund post additional cash or securities to maintain collateral coverage. If a fund has positions that fall sharply in value, the collateral is insufficient, and the prime broker issues a margin call. The fund must either meet the call immediately or face forced liquidation of its portfolio at bad prices.

## Prime broker relationships and counterparty risk

Most hedge funds use multiple prime brokers (typically 2 to 5) to diversify counterparty risk. If one prime broker fails (as Lehman Brothers did in 2008), the fund's assets with that broker are at risk. During a multi-broker failure, the fund could face cascading losses.

The relationship between a hedge fund and its prime brokers is also negotiated. Larger funds with more assets can demand better rates and more lenient terms. A $1 billion fund might get 10 basis points on repo financing, while a $100 million fund might pay 15 basis points. This creates an economy of scale: larger funds can afford leverage more cheaply.

Prime brokers also provide credit lines independent of collateralized repos. A hedge fund might maintain a $50 million unsecured credit line with a prime broker, usable for short-term financing or operating expenses. These credit lines are vital during periods when collateral haircuts are rising and repo financing is tight.

## Leverage and systemic risk

The interconnectedness of hedge funds and prime brokers creates systemic risk. When many hedge funds are leveraged and markets move adversely, margin calls cascade across the financial system. Prime brokers face simultaneous demands to liquidate collateral across many funds, flooding markets with selling. This can trigger a liquidity crisis.

The 2008 financial crisis illustrated this. When Lehman Brothers failed, hundreds of hedge funds with prime brokerage relationships at Lehman lost access to their accounts, were forced into unfavorable positions, and suffered massive losses. Other prime brokers, facing margin calls from Lehman's failure, tightened financing to all their hedge fund clients, forcing deleveraging across the industry. The deleveraging created a vicious cycle: forced selling depressed asset prices, which triggered more margin calls, forcing more selling.

To address this systemic risk, regulators now require prime brokers to maintain higher capital reserves and to stress-test their ability to absorb a large client failure. Prime brokers are also required to segregate customer assets, preventing the commingling of customer and proprietary assets that occurred before 2008.

## Rehypothecation and concentration risk

Prime brokers earn fees not only from the hedge funds they finance but also from the use of hedge-fund collateral. When a prime broker receives securities as collateral, it rehypothecates—relends those securities to other counterparties, earning a fee or financing benefit. This amplifies the prime broker's profit but creates concentration risk. If many hedge funds pledge the same security as collateral and the prime broker rehypothecates all of it, the prime broker has created a liability it might not be able to cover if markets move sharply.

Regulations have tightened rehypothecation rules to reduce this risk, but the practice remains common. Hedge funds that want to restrict rehypothecation must negotiate for it, typically paying higher financing costs in exchange.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
  <li><a href="/wiki/hedge-fund/">Hedge fund</a> — the primary user of leverage via prime brokers.</li>
  <li>Leverage — the debt amplification strategy.</li>
  <li><a href="/wiki/repurchase-agreement/">Repurchase agreement</a> — the primary financing mechanism.</li>
  <li><a href="/wiki/prime-broker/">Prime broker</a> — the financial institution providing services.</li>
</ul>
<h3>Wider context</h3>
<ul>
  <li><a href="/wiki/counterparty-risk/">Counterparty risk</a> — the risk that a prime broker fails.</li>
  <li><a href="/wiki/lehman-brothers-collapse/">Lehman Brothers collapse</a> — a cautionary tale of prime broker interdependence.</li>
  <li>Margin — how leverage is implemented operationally.</li>
</ul>
</div>
