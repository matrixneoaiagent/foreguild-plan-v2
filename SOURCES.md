# Sources — Foreguild v2: Underwrite the Outcome

Every non-obvious factual claim in `index.html` is footnoted to one of the numbered sources below. Access date: 11 November 2026 unless stated. Financial figures, loss ratios, verification error rates and conversion rates are **planning assumptions**, not observed Foreguild results; they are labelled in the plan and reproduced in `model.csv`.

## Primary evidence produced for this plan

- **Seer market-depth measurement (11 Nov 2026).** Public endpoint `POST https://app.seer.pm/.netlify/functions/markets-search`, paginated to the full board. Result: 3,056 markets; 1,154 conditional; 127 funded; median funded liquidity $25.92; total conditional liquidity $13,599.57; 398 Futarchy markets; 165 on Base, of which 4 conditional and 0 funded. Raw JSON: `data/seer_markets.json`, `data/seer_root.json`, `data/seer_base.json`, `data/seer_futarchy.json`; script: `data/seer_depth.py`; summary: `data/seer_depth.json`. Prior independent measurement (9 Nov 2026): 3,051 / 1,153 / 125 / $13,446, published in POIDH claim 9513.
- **Claim census (11 Nov 2026).** 73 claim summaries from the POIDH #1531 record (`data/poidh1531.json`). Counts: verification 42; insurance/assurance raw 14 (13 risk-transfer + 1 quality-assurance); reserve ratio 2; loss ratio 0; combined ratio 0; actuarial 0; cohort 1; CAC/LTV 2; TAM 0. Script: `data/claim_census.py`; output: `data/claim_census.json`.
- **Financial model.** `model.py` generates `model.csv` (36 monthly rows). Base case: Y1 net revenue $196,297, EBITDA −$103,703; Y2 $827,292 / +$177,288; Y3 $2,170,036 / +$820,036. Bear and bull scenarios are functions in `model.py`. All inputs are assumptions.

## Numbered sources (matching the footnotes)

1. **Seer documentation — What is Seer; conditional markets; futarchy.** https://docs.seer.pm/documentation/what-is-seer · https://docs.seer.pm/app/conditional-markets · https://docs.seer.pm/whitepaper/applications/futarchy
2. **Seer deployed contracts — FutarchyFactory on Gnosis; Base deployment.** https://docs.seer.pm/developers/contracts/deployed-contracts
3. **Seer Risk Pricing — DeFi default-probability markets.** https://risk.seer.pm
4. **Seer depth measurement (this plan) + prior measurement in POIDH claim 9513.** https://app.seer.pm/.netlify/functions/markets-search · https://poidh.xyz/base/bounty/1531
5. **Claim census (this plan) + POIDH #1531 record.** https://poidh.xyz/base/bounty/1531
6. **Upwork, Inc., Form 10-K for FY2025 (filed 13 Feb 2026).** GSV $4.0B; revenue $787.8M; FY2023 GSV $4.1B. https://www.sec.gov/Archives/edgar/data/1627475/000162747526000012/upwk-20251231.htm
7. **Fiverr International Ltd., Form 20-F for FY2025 (filed 12 Mar 2026).** Marketplace GMV $1.073B, −2.2%; marketplace revenue $297.5M; take rate 27.7%; active buyers −13.6%; spend per buyer +13.3%. https://www.sec.gov/Archives/edgar/data/1762301/000117891326000858/zk2634486.htm
8. **Cantina — opportunities.** 52 live opportunities; $58.9M payouts available; $56.8M paid; 8,450 vulnerabilities found; 25,136 researchers. https://cantina.xyz/competitions
9. **DefiLlama — chains and protocols.** Base TVL $5.75B; 927 protocols on Base; 257 >$1M; 146 >$10M; 1,258 protocols globally >$1M TVL; 8,983 total protocols. https://api.llama.fi/v2/chains · https://api.llama.fi/protocols
10. **SWE-bench — Verified and leaderboards.** 500 human-filtered tasks; mini-SWE-agent 65% on Verified (2025); SWE-agent 12.47% on the original benchmark (March 2024). https://www.swebench.com/ · https://openai.com/index/introducing-swe-bench-verified/
11. **Zheng et al., “Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena,” NeurIPS 2023.** Strong LLM judges reach >80% agreement with humans, with position, verbosity and self-enhancement biases. https://arxiv.org/abs/2306.05685
12. **UMA — optimistic oracle.** 99.8% of requests resolve without dispute; 65% DVM majority; 24-hour commit/reveal; one-week unstaking. https://docs.uma.xyz/protocol-overview/how-does-umas-oracle-work
13. **Kleros — decentralized arbitration court.** https://kleros.io/
14. **MetaDAO — decision markets.** 96 proposals for 14 organizations since November 2023. https://docs.metadao.fi/governance/overview
15. **Robin Hanson, “Futarchy: Vote Values, But Bet Beliefs.”** https://mason.gmu.edu/~rhanson/futarchy.html
16. **Rethink Priorities, “Issues with Futarchy.”** Thin markets, risk premia, manipulation, non-myopic incentive compatibility. https://rethinkpriorities.org/research-area/issues-with-futarchy/
17. **Frontier Research, “Decision Markets in Governance.”** Fail-conditional market thinness in MetaDAO; manipulation evidence; wealth weighting. https://instituteforexoticscience.ca/content/frontier/fr-decision-markets-in-governance.html
18. **Robin Hanson, “Futarchy’s Minor Flaw.”** Decision selection bias. https://www.overcomingbias.com/p/futarchys-minor-flaw
19. **Dynomight, “Futarchy’s fundamental flaw.”** Selection bias in decision markets. https://dynomight.net/futarchy-market/
20. **x402 — open internet-native payment standard.** Production-ready; millions of transactions; zero protocol fees. https://x402.org
21. **Model Context Protocol (MCP).** Open standard for connecting AI applications to tools and data. https://modelcontextprotocol.io/docs/getting-started/intro
22. **Agent Payments Protocol (AP2).** Payment authorization and accountability for agents; does not verify delivery. https://ap2-protocol.org/
23. **Circle — USDC.** Native USDC on Base. https://www.circle.com/en/usdc
24. **Stripe pricing.** 2.9% + 30¢ domestic cards; 1.5% stablecoin payments; $15 dispute fee. https://stripe.com/pricing
25. **Insurance Business, “Unlock emerging specialty lines.”** Specialty combined ratios 32.1%–57.1% (2014–2024). https://www.insurancebusinessmag.com/us/news/excess-surplus/unlock-emerging-specialty-lines-a-growth-playbook-for-mgas-and-wholesale-brokers-549688.aspx
26. **Gallagher Re, 2026 MGA market report.** $125B+ MGA premium in 2025; program-carrier net combined ratio in the low 90s. https://www.ajg.com/gallagherre/-/media/files/gallagher/gallagherre/news-and-insights/2026/june/mga-market-report-2026-reinsurance-capital-north-america.pdf
27. **Aon, 2025 MGA Market and Outlook.** MGA loss ratios and growth. https://www.aon.com/getmedia/9bcce983-f8ba-4aa3-8e51-f70b1f9d1cf1/2025-MGA-Market-and-Outlook.pdf
28. **POIDH bounty #1531, “FAO Operating Plan Contest.”** 0.5 ETH; 73 claims; deadline 12 Nov 2026 AoE. https://poidh.xyz/base/bounty/1531
29. **POIDH documentation and API.** https://docs.poidh.xyz/
30. **Seer, “AI Markets.”** Prediction markets consumed by algorithms at machine speed. https://docs.seer.pm/whitepaper/applications/ai-markets
31. **Seer, “Conditional Markets for Futarchy, Decision Markets & Info Finance.”** https://seer-pm.medium.com/conditional-markets-for-futarchy-decision-markets-info-finance-b1b317df7705
32. **Base documentation.** USDC, gas, ecosystem. https://docs.base.org/
33. **Circle Nanopayments.** Gas-free USDC payments down to $0.000001 for agents. https://www.circle.com/nanopayments
34. **Seer futarchy whitepaper.** https://docs.seer.pm/whitepaper/applications/futarchy
35. **The 8 November 2026 Foreguild plan (v1), companion to this document.** https://matrixneoaiagent.github.io/foreguild-plan/

## Notes on use

- The SEC filings are the primary source for Upwork and Fiverr figures; the take rates are computed as revenue ÷ GSV (Upwork) or reported (Fiverr).
- The Cantina and DefiLlama figures are live-page/API reads on 11 November 2026 and will change.
- The MGA and specialty-insurance benchmarks are used only as an order-of-magnitude check on the underwriting margin; Foreguild is not an insurer and does not have a carrier’s capital structure.
- No source is used to imply a partnership, endorsement, live Foreguild contract or observed Foreguild revenue.
