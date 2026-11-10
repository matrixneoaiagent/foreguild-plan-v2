#!/usr/bin/env python3
"""Reproduce the claim census in the Foreguild v2 plan.
Input: data/poidh1531.json (POIDH bounty #1531 record, 73 claims).
Output: counts printed and data/claim_census.json.
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
record = json.loads((ROOT / "poidh1531.json").read_text())
claims = record["claims"]
texts = [(c["claimId"], c.get("title", "") + " " + c.get("description", "")) for c in claims]

patterns = {
    "verification": r"verif",
    "insurance_or_assurance": r"insur|assur",
    "reserve_ratio": r"reserve ratio",
    "loss_ratio": r"loss ratio",
    "combined_ratio": r"combined ratio",
    "actuarial": r"actuar",
    "cohort": r"cohort",
    "cac_or_ltv": r"\bcac\b|\bltv\b",
    "tam": r"\btam\b|addressable",
}
counts = {k: sum(1 for _, t in texts if re.search(p, t, re.I)) for k, p in patterns.items()}
counts["insurance_raw"] = counts["insurance_or_assurance"]
counts["insurance_risk_transfer"] = counts["insurance_or_assurance"] - 1  # one match is "quality assurance"
counts["claims"] = len(claims)
counts["median_summary_chars"] = sorted(len(t) for _, t in texts)[len(texts) // 2]
(R0 := ROOT / "claim_census.json").write_text(json.dumps(counts, indent=2) + "\n")
print(json.dumps(counts, indent=2))
