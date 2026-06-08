---
title: "Intraday Liquidity in Real-Time Gross Settlement Systems"
description: "Intraday liquidity in RTGS systems allows banks to fund continuous payment queues using daylight overdrafts and repos rather than idle cash. Learn how central banks provide this critical infrastructure."
keywords:
  - intraday liquidity real time gross settlement
  - RTGS daylight overdraft
  - settlement liquidity central bank
  - payment system risk management
image: /svg/trading.svg
---

*In **real-time gross settlement** (RTGS) systems, financial institutions must settle securities and cash trades individually and immediately—not batched at day-end. This creates a continuous demand for liquidity throughout the day: banks need funds to pay for incoming securities and to cover outflows without interruption. Central banks provide **intraday liquidity** through daylight overdraft facilities and [repurchase agreements](/repurchase-agreement/) so that participants can fund this queue without holding enormous idle cash balances overnight or halting payment activity when temporary mismatches occur. Without this infrastructure, RTGS settlement would bottleneck, forcing institutions to queue trades or accumulate costly overnight reserves.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Intraday Liquidity in RTGS — Infrastructure Basics</div>

<img src="/svg/trading.svg" alt="An abstract editorial mark for payment settlement and central banking." />

<div class="wiki-infobox-caption">The plumbing that allows trillions in daily settlements to flow without gridlock.</div>

|   |   |
|---|---|
| **What it is** | Short-term credit supplied by central banks to fund payment queues during the settlement day |
| **Sources** | Daylight overdrafts; intraday repo; standing credit facilities; collateral-based liquidity windows |
| **Why needed** | RTGS settles trades individually and immediately; payments do not batch, so timing mismatches are constant |
| **Key metric** | Intraday peak liquidity demand (often 2–5× daily average settlement value) |
| **Central bank role** | Lender of last resort for same-day liquidity; sets rates and collateral rules |
| **Risk angle** | Participants might overdraft excessively; central bank monitors and enforces credit discipline |

</aside>

## How RTGS Demands Intraday Liquidity

In a traditional batch settlement system (rare now in major markets), trades accumulate during the day and settle at a fixed window—typically 2:00 p.m. or 4:00 p.m. A bank can predict its net position at settlement time, hold cash to cover it, and settle all trades at once. Simple, but slow: a trade agreed at 10:00 a.m. settles 4 hours later, carrying overnight [counterparty risk](/counterparty-risk/).

RTGS inverts this model: every trade settles the instant it is matched, and each party must have available funds or credit in its [central bank](/central-bank/) account. A bank that has sold securities and received cash can deploy that cash immediately to buy other securities. But if a bank needs to buy before it has sold—a common intraday pattern—it must either hold idle cash or borrow from the central bank.

The problem is magnitude. A large bank might settle $500 billion in trades on a typical day, but that settlement is not evenly distributed. Early in the session, the bank may be a net buyer (paying for securities it has purchased) even though it will be a net seller (receiving cash from earlier sales) by day-end. Peak intraday liquidity demand—the maximum cumulative outflow a bank must cover—often reaches 2 to 5 times its daily average settlement value. Requiring a bank to hold $2 trillion in idle cash to cover this peak would be economically wasteful and would drain liquidity from the rest of the economy.

Central banks solve this by offering intraday credit. A bank can overdraft its account (go negative in its central bank balance) during the day and repay the overdraft by day-end, paying a small intraday interest rate (often very low, sometimes zero) as the price of this convenience.

## Daylight Overdraft Facilities

The most straightforward form of intraday liquidity is the **daylight overdraft** or **daytime credit line**. The [Federal Reserve](/federal-reserve/), the [European Central Bank](/european-central-bank/), and other major central banks allow banks participating in their RTGS systems to carry negative balances during business hours, provided they return to a positive balance by the end of the day. The rules typically specify:

- A maximum overdraft limit (often based on the institution's capital, payment activity, or risk profile)
- An intraday interest rate (often 25–50 basis points, or zero for emergency facility use)
- A requirement to return to zero or positive balance by day-end (usually 4:30 p.m. or 5:00 p.m. in the U.S.)
- A ban on overdrafting overnight (the Fed charges much higher rates, effectively prohibiting overnight deficit balances)

Banks monitor their intraday position continuously and manage the overdraft like a working-capital line: they draw when payments are due, repay when incoming cash arrives. The central bank monitors aggregate overdraft usage and individual bank limits to ensure no participant is carrying excessive risk.

## Intraday Repo and Collateralized Borrowing

For banks that want to avoid overdraft limits or prefer collateralized borrowing, central banks also operate **intraday repurchase** (repo) facilities. A bank can post eligible securities (Treasury bonds, high-grade corporates, etc.) and borrow cash for a few hours, repaying the loan plus interest by day-end. The collateral provides the central bank with recourse if the borrower fails to repay.

During normal times, intraday repo is not heavily used because daylight overdrafts are cheaper and simpler. But if a bank has large trading losses or a sudden funding shock, repo provides a backstop: it can monetize securities without selling them (avoiding market disruption) and repay at day-end. Central banks typically price intraday repo at a penalty rate (higher than the overnight rate) to discourage overuse but still offer it to prevent payment gridlock.

The [European Central Bank](/european-central-bank/), [Bank of England](/central-bank/), and other central banks have expanded intraday repo programs in recent years, particularly during stress episodes (market dislocations, fund redemptions, geopolitical shocks) when normal intraday funding dries up.

## Peak Liquidity Demand and Network Effects

The total intraday liquidity need across the entire system depends on how payment flows concentrate. On a day when equity markets are volatile, many traders are unwinding positions simultaneously, and incoming and outgoing trades are highly correlated, peak demand can spike well above normal levels. Central banks monitor this and sometimes adjust facility rates or collateral terms to manage demand.

Importantly, intraday liquidity is not equally distributed. Large money-center banks and dealers participate heavily in payment flows; small regional banks may only send or receive payments episodically. The central bank's intraday credit facility must be sufficient to let the high-velocity institutions operate without interruption, even as smaller participants queue trades.

Network effects matter too: if a key payment hub (a major dealer) runs out of intraday liquidity and cannot overdraft further, it may be forced to delay payments, which backs up other banks in the settlement system. This cascade can freeze an otherwise liquid market. Central banks prevent this by:

- Offering ample intraday credit limits to critical institutions
- Actively monitoring payment queues and clearing logjams
- Standing ready to lend at penalty rates rather than allow gridlock
- Coordinating across central banks in crisis moments (so that cross-currency settlements do not stall due to USD or EUR liquidity scarcity)

## Risk and Moral Hazard

The downside of generous intraday credit is moral hazard: if central bank funds are too cheap and readily available, banks might be tempted to take excessive intraday positions, knowing they can always overdraft. To manage this, central banks impose limits (a bank cannot overdraft more than X basis points of its capital) and charge rates that rise steeply beyond prudent levels (a penalty rate structure). Some central banks also impose caps on system-wide intraday overdraft, forcing banks to compete for scarce intraday credit when demand is extreme.

This discipline has been tested during financial crises. In 2008–2009, intraday demand for [Federal Reserve](/federal-reserve/) overdraft capacity surged as banks hoarded cash and delayed payments to preserve liquidity. The Fed responded by expanding facilities and keeping rates low, recognizing that tight intraday credit would have amplified the liquidity crisis.

## Global Coordination

RTGS systems are national or regional (the Fed's Fedwire in the U.S., TARGET2 in the eurozone), but **cross-currency settlement** occurs globally at every moment. A U.S. bank buying yen settlement needs dollars; a Japanese bank buying euros needs yen. If the Fed's intraday facility is exhausted or rates spike, it impairs yen settlement even in Japan's system. Central banks have therefore established **standing swap lines** (the Fed-ECB swap line, the Fed-BOJ swap line) to supply foreign currency liquidity at the intraday level, ensuring that one central bank's policy does not create artificial scarcity in another region.

## See also

<div class="wiki-seealso">

### Closely related

- [Central bank](/central-bank/) — Operator and lender of last resort for settlement systems
- [Repurchase agreement](/repurchase-agreement/) — Collateralized borrowing used for intraday funding
- [Counterparty risk](/counterparty-risk/) — What RTGS settlement minimizes by settling immediately
- [Liquidity risk](/liquidity-risk/) — The specific risk of temporary funding gaps during the settlement day
- [Monetary policy](/monetary-policy/) — Central bank setting that influences intraday credit costs
- [Federal Reserve](/federal-reserve/) — Operates the U.S. RTGS (Fedwire) and daylight overdraft facility

### Wider context

- [Stock exchange](/stock-exchange/) — Origin of trades that require intraday settlement
- [Broker](/broker/) — Institution using intraday credit to settle customer trades
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — Regulator of settlement system design
- [Over-the-counter market](/over-the-counter-market/) — Trades that also require timely settlement through RTGS
- [Systemic risk](/systemic-risk/) — Why central banks ensure RTGS never gridlocks

</div>
