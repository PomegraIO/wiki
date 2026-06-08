---
title: "Front-Running Prohibition"
description: "Rules barring broker-dealers and advisers from trading ahead of their clients' large pending orders to capture the anticipated price move."
keywords:
  - front running
  - broker-dealer conflict
  - fiduciary duty
  - order flow
  - market manipulation
image: "/svg/regulation.svg"
---

*A broker or adviser **front-runs** when they trade for their own account ahead of executing a client's large order, capturing the price movement their own client's order will generate. If a client asks a broker to buy 100,000 shares at market, and the broker buys 10,000 for themselves first, they pocket the spread between the cheap price they get and the slightly higher price the client's order will push the [stock](/stock/) to. Front-running is illegal because the broker owes a fiduciary duty to the client; self-dealing at the client's expense is a breach of trust.*

<aside class="wiki-infobox">

<div class="wiki-infobox-title">Front-Running — key facts</div>

<img src="/svg/regulation.svg" alt="An abstract editorial mark for the topic." />

<div class="wiki-infobox-caption">A fiduciary violation and form of market abuse that exploits the broker's privileged knowledge of client orders.</div>

|   |   |
|---|---|
| **What it is** | Trading ahead of a client's large order using knowledge of that order |
| **Also called** | Trading ahead; prior-to-disclosure abuse; confidentiality violation |
| **Governed by** | Securities Exchange Act Section 10(b); [SEC](/securities-and-exchange-commission/) Rule 10b-5; FINRA rules; common law fiduciary duty |
| **Key players** | [Broker-dealers](/broker/), investment advisers, traders within broker firms |
| **Prohibited conduct** | Using nonpublic client order information to trade ahead |
| **Enforcement** | SEC, FINRA, state securities regulators, civil lawsuits |
| **Remedy** | Restitution to client; disgorgement of profits; suspension or bar from industry |

</aside>

## The core conflict and why it matters

A large institutional client — say, a pension fund — calls their broker with an order: "Buy me 500,000 shares of Company X at the market." This is not a secret, but it is information. The broker's traders know it. If they are on a busy trading day, that order might take 20 or 30 minutes to execute; the broker's algorithm will break it into smaller chunks and feed it to the market gradually to avoid shocking the [price](/stock-market/).

Here is the problem: the broker's traders also know that when a 500,000-share buy order hits the market in small pieces, the stock's [price](/stock-market/) will likely drift upward. There is inelastic demand. Smart traders will anticipate it. So the broker's proprietary trading desk asks the simple question: why don't we buy 50,000 shares for ourselves right now, before we execute the client's order? When the client's order hits and the price rises, we sell our 50,000 shares into that higher price and pocket the difference.

The client loses. They buy at a higher average price than if the broker had executed them first. The broker gains. The broker's personal trading profits at the direct expense of the client they are supposed to serve.

This is front-running. It is illegal precisely because the broker is a fiduciary — they owe the client a duty of loyalty, meaning they must put the client's interests first, not second to their own.

## Legal frameworks

Front-running violations can be prosecuted under multiple statutes. The most powerful is Securities Exchange Act Section 10(b), which makes it illegal to use a deceptive practice in connection with the purchase or sale of securities. The [SEC](/securities-and-exchange-commission/) interprets this to include trading on nonpublic information obtained in a fiduciary capacity.

The [SEC](/securities-and-exchange-commission/) also enforces Rule 10b-5, which applies the antifraud statute more broadly: a [broker-dealer](/broker/) who trades ahead of a client order using material nonpublic information (the client's order itself) and fails to disclose this conflict of interest has made an untrue statement of fact or omitted a material fact necessary to make a statement not misleading. The information is material because it affects the price the client will pay.

Beyond federal securities law, FINRA — the self-regulatory organization for broker-dealers — has explicit rules. FINRA Rule 5210 requires [brokers](/broker/) to place client orders ahead of their own. FINRA Rule 5310 requires disclosure of material conflicts of interest. A broker that trades ahead without clear, advance disclosure violates these rules and faces suspension, fines, or permanent bar.

Finally, the common law of fiduciary duty applies. A client can sue a broker civilly for breach of fiduciary duty, claiming unjust enrichment. Even if the client cannot prove the securities fraud cleanly, they can recover the profits the broker made from the front-run as damages.

## How it differs from other trading abuses

Front-running is often confused with other forms of trading manipulation, but the distinction matters. Insider trading involves trading on material nonpublic information about the *company* (earnings, a merger, a lawsuit). Front-running involves trading on material nonpublic information about a *client's order*. The economic harm is the same — the client loses — but the confidential information and the breach differ.

[Spoofing](/spoofing-layering-prohibition/) is placing fake orders to move prices. Front-running is placing *real* orders ahead of a client's, using legitimate market access but improper knowledge. A [market maker](/market-maker-trading/) who [quotes](/bid-ask-spread/) tight spreads is doing their job; a broker who widens the spread after noticing a large client order, then executes the client at the wider spread, is front-running if they do this for themselves.

## Detection and enforcement

Detecting front-running requires examining order timing and fills. Regulators and compliance teams look for patterns: Does the broker consistently buy or sell their own account just before executing large client orders in the same direction? Are the fills on the client orders markedly worse than benchmark prices? Did the broker's proprietary trading profit correlate with client order flow?

Modern systems use surveillance algorithms to flag suspicious timing. A broker's compliance officer will be required to review a large trade if the [broker's](/broker/) own order immediately precedes the client's by more than a few seconds. The [SEC](/securities-and-exchange-commission/) and FINRA also conduct examinations and bring enforcement actions.

In one notable case, the SEC settled with a major [broker-dealer](/broker/) that had allowed its proprietary traders to see the firm's client orders in real time. The traders systematically front-ran large orders, generating millions in profits. The firm paid tens of millions in restitution and fines.

## Modern safeguards and Chinese walls

Most large [broker-dealers](/broker/) now implement strict order handling procedures. Client orders are routed through compliance systems before hitting the market. The [broker's](/broker/) proprietary traders are segregated (a "Chinese wall") and do not have real-time access to client order information. Compliance must timestamp and log all trades. Large client orders are disclosed to the client at execution, with precise fills, so the client can verify they received fair treatment.

Technology has helped. Algorithmic execution systems can split large orders and route them so quickly that a rogue trader has no time to front-run. Some brokers have moved to agency models where they do not execute proprietary trades at all, eliminating the conflict.

But the temptation remains real. Any broker with access to large client orders and a profit motive faces the same conflict. Enforcement, along with the fiduciary duty framework and the risk of civil litigation, keeps the incentive suppressed — but not eliminated.

## See also

<div class="wiki-seealso">

### Closely related

- [Broker-Dealer](/broker/) — the entity that owes the fiduciary duty
- Fiduciary Duty — the legal obligation the broker breaches
- [Market Maker](/market-maker-trading/) — traders who execute orders and might be involved in front-running
- [Bid-Ask Spread](/bid-ask-spread/) — the venue where front-runners exploit client orders
- [Spoofing and Layering Prohibition](/spoofing-layering-prohibition/) — another market manipulation tactic
- Insider Trading — related abuse involving nonpublic information

### Wider context

- [Stock](/stock/) — the securities being traded when front-running occurs
- [Securities and Exchange Commission](/securities-and-exchange-commission/) — primary regulator
- FINRA — self-regulatory organization with front-running rules
- Securities Exchange Act — foundational statute that prohibits front-running

</div>
