# Foreguild v1 → v2: gap analysis and recommendation

**Prepared:** 11 November 2026. **Scope:** the existing claim 9502 (`Foreguild: Sell Verified Outcomes`, wallet `0xa15c…b93c`) and the 73 claims on POIDH #1531. **Purpose:** decide whether a v2 is worth submitting, and if so, what must change.

## 1. What v1 does well

v1 is a credible, honest operator plan. Its strengths are real and should be preserved:

- **Authentic supply-side evidence.** It uses the author's own 28 Oct–8 Nov 2026 ledger: ~140 supply actions across eleven agent marketplaces produced about $2.08. That is more concrete than most of the field's invented traction.
- **A clear demand-first thesis.** “Buyers buy outcomes, not agents” is correct, and the three surfaces (Guild Delivery, Board, Verify API) follow from it.
- **A coherent unit economics story.** The $150 board task is traced through the 8% fee, $2.10 verification and $0.90 payment cost to a $9.00 contribution; the plan explicitly says settlement alone is thin and Guild Delivery carries the margin.
- **Honest assumptions and kill criteria.** The 90-day plan has measurable gates, a $6.4k budget, and a published “what would make this wrong” section.
- **Good writing and design.** It is readable, compact (12 pages, ~3.5k words), and free of token/VC filler.

## 2. What the strongest competitors do better

The bar moved after 8 November. The strongest entries are not better written; they are **better evidenced and more ambitiously modelled**.

| Competitor | What it does better | Why it matters |
|---|---|---|
| **9531 — “the operating plan that already runs”** | Deployed escrow and futarchy contracts on testnet, a settled payout (0.1 → 0.098 NEAR, 2% fee), TEE-signed verdicts, a PayPal payout batch, and live `/api/markets`, `/api/futarchy`, `/api/feed`, `/api/poidh` endpoints. | It converts “proposed” into “verifiable today.” v1 has no live contract or endpoint. |
| **9513 — “the receipt, not the review”** | A measured Seer census (3,051 markets, 1,153 conditional, 125 funded, median $25.91, $13,446 total), a buyer-base analysis, the $37.50 minimum-ticket argument, a runnable `model.py --check`, and two live Base markets. | It is rigorous about the two things v1 asserts: verification cost and governance depth. |
| **9477 — “Buyers Are the Bottleneck”** | 394 Verdikta bounties, 525 AI-jury verdicts, 61 external buyers, 50 of 61 buyers also workers, a $1,360 outside market in eight weeks, rubric-defect back-testing, and ten day-90 predictions. | It has the best demand-side dataset in the field, and it uses it to attack recycled volume. |
| **9480 — “The Verification Guild”** | A 27-page plan with 48 pinned figures, a verification P&L, a sensitivity grid, a harness demo, measured market depth, and an explicit “where others are stronger” section. | It sets the standard for reproducibility and verification depth. |
| **9457 — “The Empirical Guild”** | Enumerates Poidh, Cantina (52 live, $58.9M pool), Immunefi (155 programs), Superteam (1 of 10 agent-allowed), and the Algora/Polar collapse; anchors a 90-day NSR ramp. | It measures the addressable supply rather than asserting a TAM. |
| **9524 — “The Franchise FAO”** | A franchise model with 55 guilds, $681k/month federation revenue by month 12, cross-guild verification, and three fully specified governance markets. | It has a larger, more scalable revenue story than v1's agency model. |

The common pattern: the top entries have **one proprietary dataset or live artifact**, and they push the revenue model beyond a single small agency. v1 has a proprietary operator ledger, but it is small ($2.08) and it is not connected to a loss/risk model.

## 3. The five gaps in v1

1. **Revenue ambition and structure.** v1's base case is $147k revenue and +$22k net in Year 1, with a $2.8k monthly fixed base. There is no 3-year P&L, no cohort model, no bull/bear scenario, and no path to a venture-scale business. It reads as a two-person agency with a board attached, not an FAO that can compound.
2. **Verification is asserted, not costed.** v1 says “verification is the moat” and uses a 10% human sample, but it does not give cost per check by tier, false-accept/false-reject targets, appeal rates, calibration methods, or a verification P&L. The $2.10 per board task is a single blended number.
3. **Futarchy is standard and not operational.** v1's NVR90, five decision classes and $1,000 liquidity floor are sensible, but they are the field's default. The markets decide fees/categories/spend; they do not price the work. There is no loss-ratio market, no reserve policy, no underwriting committee, and no measured Seer depth.
4. **No risk P&L.** v1 sells verified outcomes but treats failure as a dispute, not as a cost of goods sold. There is no loss ratio, claims reserve, combined ratio, or capital charge. This is the field-wide gap: in the 73 claim summaries, **42 mention verification, 13 mention risk-transfer insurance/assurance, and 0 mention loss ratio or combined ratio** (our census; see `data/claim_census.py`).
5. **Evidence gap.** v1 has no measured Seer depth, no claim census, no live market, and no data appendix. Competitors 9513, 9477, 9480 and 9457 all have at least one of those.

## 4. The five highest-leverage changes in v2

1. **Make the guarantee the product, not an upsell.** v2 reframes Foreguild as a completion underwriter: fixed price + date + remedy, with the board as distribution. This raises the ticket, makes the buyer's downside the pricing anchor, and creates a defensible margin that a 6–10% take cannot.
2. **Add a loss-ratio market and a RAC90 constitution.** Seer conditional scalar markets forecast the pure premium by class; the forecast is an input to every quote. RAC90 (risk-adjusted contribution) plus a 1.5× claims reserve and a 120% circuit breaker prevents revenue being bought by underpricing risk. This is futarchy doing real work, not ratifying fees.
3. **Build a 3-year, three-scenario P&L with cohorts.** Base case: $196k → $827k → $2.17M net revenue; EBITDA −$104k → +$177k → +$820k; break-even month 11; max cash trough −$117k. Bear case: 108% loss ratio, −$81k Y3 EBITDA, −$420k cumulative trough. The model is in `model.csv`, generated by `model.py`.
4. **Cost verification like COGS.** A T0–T4 stack with cost per check, false-accept/false-reject targets, appeal bonds, a 200-task quarterly calibration set, κ ≥ 0.7, and a verification P&L with a 1.5% of GWV stop rule. This turns “verification is the moat” into an operating budget.
5. **Measure the governance constraint.** v2 re-measures Seer's board (3,056 markets, 1,154 conditional, 127 funded, median $25.92, $13,600 total; all four Foreguild-specific Base conditional markets unfunded) and designs around it: $5k liquidity floor, 20 traders, $50k binding cap, decision bond, red team. It does not pretend a $25 market can bind a $50k decision.

## 5. Recommendation

**v2 is clearly different and materially stronger. It is worth putting in front of the judges — but as an addendum to claim 9502, not a silent replacement.**

Why:
- v2 is not a rehash. It changes the business model (underwriting vs take rate), the governance metric (RAC90 vs NVR90), the core market (loss ratio vs fee), and the evidence base (measured Seer depth + claim census + 3-year model). A judge who reads both sees a v1 that found the demand problem and a v2 that prices the risk.
- The regulatory/legal wrapper is the main new risk. v2 handles it explicitly (business-only contracts, no consumer sales, legal opinion per jurisdiction, licensed carrier if needed, stop-sell trigger), but a judge may still see “guarantee” as “insurance.” The plan says this out loud rather than hiding it.
- A second claim has a cost: the bounty already has 73 claims, and duplicate-looking submissions can split attention or look like spam. The safest path is a **comment/addendum on claim 9502** with the v2 URL and a one-line framing (“v1 proved demand is scarce; v2 prices the risk that verification fails”). If the parent wants two shots and the platform allows it, a separate claim is defensible — but the v1 site should not be overwritten.

**Recommendation:** submit v2 as an addendum first; file a second claim only if the parent is comfortable with the duplicate risk and the rules allow it. Do not replace the live v1 plan.

## 6. What would make v2 not worth submitting

- If the parent judges the regulatory burden of a completion guarantee to be disqualifying, v1's “verified outcomes” agency is the safer business; v2's underwriting thesis is the thing that makes it different, so without it there is no reason to submit.
- If the judges reward live artifacts above all else, 9531 and 9513 will beat both v1 and v2; v2's counter is the measured depth/census and the 3-year model, not a deployed contract.
- If the bounty rules treat multiple claims from the same wallet as one entry or penalize duplicates, an addendum is the only sensible route.

## 7. Comparison at a glance

| | v1 (claim 9502) | v2 |
|---|---|---|
| Thesis | Sell verified outcomes; demand-first | Underwrite the outcome; sell completion guarantees |
| Revenue model | 8% board fee + fixed-fee contracts + Verify API | Principal contracts + 9% board + 6% guarantee + Verify API |
| Y1 / Y3 net revenue | $147k / not modelled | $196k / $2.17M |
| Futarchy metric | NVR90 (net verified revenue) | RAC90 (risk-adjusted contribution) with reserve guardrails |
| Core governance market | Fee, categories, spend | Loss ratio by class; premium, reserve, verification budget |
| Verification | T0 + 10% human sample, blended $2.10 | T0–T4 with cost/error targets, appeals, calibration, P&L |
| Evidence | Operator ledger (~140 actions, $2.08) | Operator ledger + Seer depth + claim census + 3-year model |
| Length | 12 pages, ~3.5k words | 30 pages, ~13.2k words |
