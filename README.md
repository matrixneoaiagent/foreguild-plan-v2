# Foreguild v2 — Underwrite the Outcome

A revenue-first operating plan for Foreguild, the proposed futarchy-governed AI job board. The thesis: the field has 73 entries on verifying agent work, but almost none price the risk that verification fails. Foreguild should sell a **completion guarantee** — a fixed price and date for a verified outcome — price the loss ratio with Seer conditional markets, verify with a T0–T4 stack, and govern on **RAC90** (risk-adjusted contribution) with hard solvency guardrails. Base case: $2.17M net revenue and $820k EBITDA in Year 3, break-even in month 11, on a $250k seed plus the contest prize. Every financial figure is a labelled assumption, not an observed result.

## Files

| File | What it is |
|---|---|
| `index.html` | Self-contained plan: inline CSS, inline SVG charts, inline JS calculator; no external fonts or assets. Mobile-readable and printable. |
| `plan.pdf` | A4 rendering of `index.html` (30 pages, ~13.2k words). |
| `cover.png` | 1200×630 title card for the POIDH claim proof image. |
| `model.csv` | 36 monthly rows: contracts, GCV, board GMV, guaranteed value, revenue lines, costs, EBITDA, cumulative cash, reserve, headcount, loss ratio. |
| `model.py` | The model that generates `model.csv`; includes bull/bear scenario functions. |
| `SOURCES.md` | Every source URL, numbered to match the footnotes. |
| `GAP_ANALYSIS.md` | What v1 did well, what the strongest competitors do better, the five highest-leverage changes, and the recommendation on submitting v2. |
| `data/poidh1531.json` | Raw POIDH #1531 record used for the claim census. |
| `data/seer_*.json` | Raw Seer market dumps used for the depth measurement. |
| `data/claim_census.py` | Reproduces the 73-claim census. |
| `data/seer_depth.py` | Reproduces the Seer depth measurement. |

## Reproduce

```bash
python3 model.py                      # writes model.csv
python3 data/claim_census.py          # writes data/claim_census.json
python3 data/seer_depth.py            # fetches Seer and writes data/seer_depth.json
chromium --headless --no-sandbox --disable-gpu --virtual-time-budget=4000 \
  --no-pdf-header-footer --print-to-pdf=plan.pdf index.html
```

The PDF in this folder was produced with Chromium from the local `index.html`. The HTML is the source of truth; the PDF is a print rendering.

## Status

Independent non-internal entry for Seer's FAO Operating Plan Contest (POIDH #1531, on-chain id 545). Companion to the 8 November 2026 claim 9502, not a replacement. Prepared with AI assistance. No affiliation with Seer, Foreguild or POIDH. Nothing here is an offer of insurance, securities or investment advice.
