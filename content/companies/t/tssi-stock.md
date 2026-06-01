---
title: "TSS, Inc. (TSSI)"
description: "TSS, Inc. provides software tools and services that help semiconductor companies convert chip design simulation data into test code for manufacturing equipment—a specialized but essential part of the chip production pipeline."
keywords:
  - semiconductor testing
  - EDA tools
  - automatic test equipment
  - chip design
  - test automation
handwritten: true
---

TSS, Inc. (ticker: TSSI) is a small software company that solves a specific but critical problem in semiconductor manufacturing: taking the design data and simulation files that chip engineers create and translating them into the test code that manufacturing equipment needs to verify whether chips actually work. This is not glamorous work, but it is indispensable. Every chip that ships has been run through test equipment controlled by software—and that software often comes from or is enabled by tools that TSS provides.

<aside class="wiki-infobox">
<table>
<tr><th>Ticker</th><td>TSSI (OTC Markets)</td></tr>
<tr><th>Founded</th><td>1979</td></tr>
<tr><th>Headquarters</th><td>Pacific Northwest, USA</td></tr>
<tr><th>Core service</th><td>Design-to-test software translation</td></tr>
<tr><th>Main customers</th><td>Semiconductor manufacturers and design companies</td></tr>
<tr><th>Sector</th><td>Electronic design automation (EDA)</td></tr>
<tr><th>SEC CIK</th><td>0001320760</td></tr>
</table>
</aside>

## Why chip testing matters

When a semiconductor company designs a new chip, engineers simulate its behavior in software first. They run thousands of test cases to check whether the design does what they want: Does the memory work? Can the processor handle the clock speed? Will the power consumption stay reasonable? These simulations use specialized languages and tools to describe what should happen.

But simulation is not the same as reality. Once chips are actually manufactured, they need to be tested on real equipment—machines called automatic test equipment, or ATE. This equipment has thousands of pins that connect to the chip, apply signals, and measure the responses. The test equipment is controlled by test programs. Someone has to write or generate those test programs, and that is where the gap appears.

TSS exists in that gap. The design simulation data is in one format. The test equipment expects programs in a different format. Getting from here to there is not straightforward. TSS specializes in bridging that translation.

## The product and the competitive moat

TSS's flagship product is a suite of software tools that reads simulation data—usually in formats like STIL (Standardized Test Interface Language), WGL (Waveform Generation Language), or other industry standards—and converts it into test patterns that can be fed directly into ATE. The software also validates those patterns, checks for errors, and optimizes them for the specific test equipment in use.

TSS invented WGL in the 1980s. Over decades, WGL became the de facto standard in the industry for describing test patterns. That history gives TSS a distinctive position: its tools are built around the standards it helped create, and many semiconductor companies have embedded WGL and TSS-compatible workflows into their design and manufacturing processes. Switching away from tools that speak the language your engineers know well is not costless.

The company has expanded its services beyond just software. TSS also provides consulting, training, and technical support—helping customers implement the translation tools, troubleshooting problems, and working with specific ATE vendors to ensure compatibility. For a semiconductor manufacturer running a fab with expensive equipment and tight testing schedules, having reliable technical support matters.

## The business model and the customer base

TSS operates on a software licensing and services revenue model. Large semiconductor manufacturers pay for licenses to use the company's translation tools. Sometimes that is an upfront perpetual license; sometimes it is a subscription or maintenance contract. Service revenue comes from consulting engagements, custom development, and support contracts.

The customer base includes established semiconductor companies, fabless chip designers, and test and measurement equipment suppliers. These are generally not price-sensitive customers: if a translation tool saves your fab one percent of downtime or reduces defect escape—chips that make it past your testing but fail in the field—that is worth far more than the software license cost. When yield or speed-to-market is at stake, customers buy the solution that works.

That said, the market is not infinite. The number of serious semiconductor manufacturers is limited. And over the decades, larger EDA companies like Synopsys and Cadence have built test translation capabilities into their broader design platforms. Those big players have different distribution channels and deeper pockets. TSS survives by being specialized and reliable in exactly the segment it serves, not by trying to out-invest Synopsys.

## Challenges and the shifting landscape

TSS faces headwinds from industry consolidation. As the semiconductor design tool business has consolidated around a few major vendors, those vendors have incentive to fold more test functions into their own tools, reducing the need for standalone tools like TSS's. Some of TSS's value proposition is also vulnerable to automation and machine learning: as design simulation becomes faster and more accurate, some of the manual translation and validation work that TSS performs might be automated or built into the upstream design flow.

The company also operates in a niche market. While every chip needs testing, the number of organizations that care deeply about test code translation tools is much smaller than the number of chip designers or manufacturers. That narrows the addressable market and limits how much the company can grow without expanding into adjacent areas.

## How to research TSS

Anyone evaluating TSSI should start with the company's annual 10-K filing (SEC CIK 0001320760), which describes the customer base, the products, and revenue trends. TSS's investor relations site and quarterly earnings reports show whether revenue is stable or growing and whether the company is investing in new product development. The key question is whether the company is winning or losing market share in its niche, and whether test automation tools are becoming more or less important to semiconductor manufacturers as chip design tools evolve.

Watch for developments in the EDA market broadly: if Synopsys or Cadence acquire capabilities or companies that compete with TSS, that is a signal. Also pay attention to whether major customers are renewing their contracts and whether TSS is winning new customers or being displaced. In a specialized software business like this, recurring contract renewals and net new customer wins are the two indicators that matter most.
