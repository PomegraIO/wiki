---
title: "Stablecoin"
description: "A cryptocurrency designed to maintain a stable value, typically pegged to a reference asset like the US dollar or gold."
---

*A stablecoin is a cryptocurrency explicitly designed to minimize price volatility. Unlike [bitcoin](/wiki/bitcoin/), which fluctuates based on supply and demand, a stablecoin maintains a stable value—usually $1 USD or 1 gram of gold—through one of several mechanisms: backing by reserves, algorithmic adjustment of supply, or collateralization. Stablecoins are the bridge between the volatile crypto markets and the traditional financial system.*

## Why stablecoins matter

Cryptocurrencies are unsuitable as media of exchange because their values swing 10–30% in a day. If you pay for a coffee with Bitcoin today, it might be worth 20% more or less tomorrow. Stablecoins solve this by anchoring value. A merchant accepting a stablecoin knows the payment's value will not change overnight. Users can hold stablecoins as a store of value without currency risk while maintaining exposure to crypto infrastructure.

Stablecoins also unlock financial services. Decentralized-lending protocols—where users deposit stablecoins to earn interest or borrow stablecoins—have grown to tens of billions of dollars in volume precisely because users are comfortable borrowing or depositing a coin that will not collapse in value. Without stablecoins, crypto finance would be a niche speculation market, not a functional alternative to traditional banking.

## Three design approaches

**Reserve-backed stablecoins** hold an equal amount of some reference asset (dollars, euros, gold, or other cryptocurrencies) to back each coin in circulation. USDC, operated by Circle, maintains dollar reserves in regulated US banks. When you send $1 to Circle, you receive 1 USDC. When you redeem 1 USDC, you receive $1. The issuer must be trusted to hold the reserves and redeem on demand. This model is simple and has proven most robust, but it requires centralized custody and regulatory compliance from the issuer.

**Algorithmic stablecoins** use smart contracts to adjust supply in response to price. If the price of the coin falls below $1, the protocol burns tokens to reduce supply, pushing the price back up. If it rises above $1, the protocol mints new tokens, increasing supply to push the price down. Terra's Luna stablecoin (before its 2022 collapse) was algorithmic, as is Ampleforth. The advantage is decentralization—no central bank or custodian is needed. The disadvantage is fragility: if faith in the mechanism breaks, there is no reserve to restore confidence, and the coin can spiral to zero. Most algorithmic stablecoins have failed or nearly failed.

**Overcollateralized stablecoins** are created by depositing an amount of crypto assets greater than the face value of the stablecoin issued. If you deposit $2 of Ethereum to [Maker](/wiki/ethereum/), you might receive $1 in DAI, a stablecoin. If Ethereum's price falls, you must deposit more collateral or your position is liquidated. This model maintains stability through collateral rather than reserves or algorithms, and it works reasonably well. The downside is efficiency: if you must deposit $2 to create $1 in spending power, the system wastes capital.

## Reserve-backed dominance

Tether (USDT), USDC, and True USD dominate the stablecoin market because they are reserve-backed and issued by entities with strong reputational incentives to maintain the peg. USDT has a checkered history of reserve transparency, and regulatory scrutiny has increased since 2021. USDC is backed by regulated banks and regular attestations. Both trade in trillions of dollars worth annually and are essential to the functioning of crypto markets.

Most reserve-backed stablecoins are issued by centralized entities and require custody in the traditional financial system. This introduces counterparty risk: if the issuer is hacked or the custodian fails, the stablecoin could lose value. Several proposals for "decentralized" stablecoin systems (e.g., central-bank digital currencies on public blockchains) attempt to mitigate this by having governments or central banks issue tokens directly, though technical and political obstacles remain substantial.

## Price stability mechanisms in practice

Reserve-backed stablecoins maintain the peg through arbitrage. If 1 USDC trades below $1 on a [cryptocurrency-exchange](/wiki/cryptocurrency-exchange/), an arbitrageur can buy it cheaply, redeem it from Circle for $1, and pocket the difference. If it trades above $1, an arbitrageur can buy $1 from a bank, deposit it to Circle for 1 USDC, and sell the USDC at a premium. These arbitrage loops keep the price tight to $1.

Overcollateralized stablecoins maintain the peg through a mix of arbitrage and liquidation incentives. If DAI falls below $1, liquidators have an incentive to [credit-default-swap](/wiki/credit-default-swap/) the collateral of debtors, capturing the spread. This mechanism works until a black-swan crash occurs so fast that liquidators cannot act.

## The regulatory frontier

Central banks and regulators are increasingly skeptical of private stablecoins. If a stablecoin is widely used as a medium of exchange, it is, in effect, a private currency competing with the national currency. Regulators worry about monetary-policy control, sanctions evasion, and systemic risk if a large stablecoin fails. Many countries now require stablecoin issuers to be licensed and regulated like banks. Others are considering banning non-government stablecoins entirely.

<div class="wiki-seealso">
<h2>See also</h2>
<h3>Closely related</h3>
<ul>
<li><a href="/wiki/utility-token/">Utility Token</a> — tokens with functional purpose within protocols.</li>
<li><a href="/wiki/wrapped-token/">Wrapped Token</a> — tokens representing assets on other blockchains.</li>
<li><a href="/wiki/algorithmic-trading/">Algorithmic Trading</a> — market mechanisms that help maintain stablecoin pegs.</li>
</ul>
<h3>Wider context</h3>
<ul>
<li><a href="/wiki/decentralized-exchange/">Decentralized Exchange</a> — platforms where stablecoins are heavily traded.</li>
<li><a href="/wiki/cryptocurrency-exchange/">Cryptocurrency Exchange</a> — centralized exchanges that also trade stablecoins.</li>
<li><a href="/wiki/ethereum/">Ethereum</a> — blockchain hosting most major stablecoins.</li>
</ul>
</div>
