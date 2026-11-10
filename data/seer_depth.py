#!/usr/bin/env python3
"""Measure Seer's market board for the Foreguild v2 plan.
Public endpoint documented at https://docs.seer.pm/developers/api
Writes data/seer_depth.json. Run on 2026-11-11 produced:
3,056 markets; 1,154 conditional; 127 funded; median $25.918; total $13,599.56;
398 Futarchy; 165 on Base (4 conditional, 0 funded).
"""
import json, statistics as st, time, urllib.request, pathlib

URL = "https://app.seer.pm/.netlify/functions/markets-search"
ROOT = pathlib.Path(__file__).resolve().parent

def post(payload):
    req = urllib.request.Request(URL, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)

def all_markets(extra=None):
    out, page = [], 1
    while True:
        p = {"limit": 1000, "page": page}
        if extra: p.update(extra)
        d = post(p)
        ms = d.get("markets", [])
        out += ms
        if not ms or page >= d.get("pages", 1) or len(out) >= d.get("count", 0):
            break
        page += 1
        time.sleep(0.4)
    return out

root = all_markets()
cond = all_markets({"showConditionalMarkets": True})
fut = all_markets({"type": "Futarchy"})
base = all_markets({"chainsList": ["8453"]})

def is_cond(m):
    return m.get("parentMarket", {}).get("id", "0x" + "0" * 40) != "0x" + "0" * 40

def is_funded(m):
    return bool(m.get("hasLiquidity")) or (m.get("liquidityUSD") or 0) > 0

liq = [m.get("liquidityUSD") or 0 for m in cond]
pos = [x for x in liq if x > 0]
out = {
    "measured_at": "2026-11-11",
    "markets": len(root),
    "conditional": sum(1 for m in cond if is_cond(m)),
    "funded_conditional": sum(1 for m in cond if is_funded(m)),
    "median_funded_liquidity_usd": round(st.median(pos), 2) if pos else 0,
    "total_conditional_liquidity_usd": round(sum(liq), 2),
    "futarchy": len(fut),
    "base_markets": len(base),
    "base_conditional": sum(1 for m in base if is_cond(m)),
    "base_funded": sum(1 for m in base if is_funded(m)),
    "base_conditional_funded": sum(1 for m in base if is_cond(m) and is_funded(m)),
    "by_chain": {str(ch): sum(1 for m in root if m.get("chainId") == ch) for ch in sorted({m.get("chainId") for m in root})},
}
(ROOT / "seer_depth.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
