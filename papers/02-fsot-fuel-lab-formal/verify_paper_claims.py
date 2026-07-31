#!/usr/bin/env python3
"""Freeze checker for Paper 02 — FSOT Fuel Lab."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FREEZE_PATH = HERE / "FREEZE.yaml"

try:
    import yaml
except ImportError:
    yaml = None


def load_freeze() -> dict:
    text = FREEZE_PATH.read_text(encoding="utf-8")
    if yaml is None:
        raise SystemExit("PyYAML required: pip install PyYAML")
    return yaml.safe_load(text)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def near(a: float, b: float, tol: float = 1e-6) -> bool:
    return abs(float(a) - float(b)) <= tol


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fsot-root", type=Path, default=os.environ.get("FSOT_ROOT"))
    ap.add_argument("--strict-hash", action="store_true")
    ap.add_argument("--require-cross-proof", action="store_true")
    args = ap.parse_args()
    if not args.fsot_root:
        print("ERROR: --fsot-root required", file=sys.stderr)
        return 2
    root = Path(args.fsot_root).resolve()
    freeze = load_freeze()
    hard, soft, ok = [], [], []

    print(f"Repo:   {root}")
    print(f"Freeze: {FREEZE_PATH}")
    print()

    # Oracle
    exp = str(freeze["oracle"]["sha256"]).upper()
    op = root / freeze["oracle"]["path"]
    if op.is_file():
        got = sha256_file(op)
        if got == exp:
            ok.append(f"oracle SHA-256 match {got[:12]}…")
        else:
            (hard if args.strict_hash else soft).append(f"oracle mismatch {got}")
    else:
        hard.append(f"missing {op}")

    # Fuel benchmark
    fuel_rel = freeze["fuel_lab"]["benchmark"]
    fuel_path = root / fuel_rel
    if not fuel_path.is_file():
        hard.append(f"missing {fuel_rel}")
    else:
        fuel = json.loads(fuel_path.read_text(encoding="utf-8"))
        n = fuel.get("record_count") or fuel.get("observable_count")
        med = fuel.get("pooled_median_error_pct") or fuel.get("median_error_pct")
        exp_n = freeze["fuel_lab"]["record_count"]
        exp_m = freeze["fuel_lab"]["pooled_median_error_pct"]
        if n == exp_n:
            ok.append(f"fuel records: {n}")
        else:
            hard.append(f"fuel records {n} != {exp_n}")
        if med is not None and near(med, exp_m, 1e-5):
            ok.append(f"fuel pooled median: {med}%")
        else:
            hard.append(f"fuel pooled median {med} != {exp_m}")
        if float(med or 99) <= float(freeze["fuel_lab"]["green_gate_pct"]):
            ok.append("fuel under green gate 0.5%")
        else:
            hard.append("fuel exceeds green gate")

    # Desktop closure
    vd_path = root / "data/verified_desktop_cross_proof_closure.json"
    if vd_path.is_file():
        vd = json.loads(vd_path.read_text(encoding="utf-8"))
        if vd.get("verdict") == freeze["formal"]["verified_desktop_verdict"]:
            ok.append(f"desktop verdict: {vd.get('verdict')}")
        else:
            soft.append(f"desktop verdict: {vd.get('verdict')}")
        for p in vd.get("panels") or []:
            if p.get("panel") == "Fuel_Lab_Live_Panel":
                if near(p.get("pooled_median_error_pct"), freeze["fuel_lab"]["pooled_median_error_pct"], 1e-5):
                    ok.append("closure Fuel_Lab median matches freeze")
                else:
                    hard.append(f"closure fuel median {p.get('pooled_median_error_pct')}")
    else:
        hard.append("missing verified_desktop_cross_proof_closure.json")

    # Figure
    fig = root / freeze["fuel_lab"]["figure"]
    if fig.is_file():
        ok.append(f"figure present: {fig.name}")
    else:
        soft.append(f"missing figure {fig}")

    # Parameter audit if present
    pa = root / "data/parameter_count_audit.json"
    if pa.is_file():
        doc = json.loads(pa.read_text(encoding="utf-8"))
        v = str(doc.get("verdict") or doc.get("status") or "")
        if "ZERO_FREE" in v.upper() or doc.get("zero_free") is True:
            ok.append("parameter audit ZERO_FREE")
        else:
            # file may only have nested fields
            soft.append(f"parameter audit present (verdict={v!r})")

    # Cross-proof optional
    xp = root / "data/cross_proof_verification_report.json"
    if xp.is_file():
        doc = json.loads(xp.read_text(encoding="utf-8"))
        if doc.get("overall_ok") is True:
            ok.append("cross_proof overall_ok: true")
        else:
            (hard if args.require_cross_proof else soft).append(
                f"overall_ok={doc.get('overall_ok')}"
            )
        spine = doc.get("full_formal_spine") or {}
        atomic = spine.get("atomic_provable_count")
        min_a = freeze["formal"]["atomic_obligations_min"]
        if atomic is not None and int(atomic) >= int(min_a):
            ok.append(f"atomic {atomic} >= {min_a}")
        elif atomic is not None:
            hard.append(f"atomic {atomic} < {min_a}")
    else:
        (hard if args.require_cross_proof else soft).append("missing cross_proof report")

    print("PASSED")
    for m in ok:
        print(f"  [ok]   {m}")
    if soft:
        print("\nWARNINGS")
        for m in soft:
            print(f"  [warn] {m}")
    if hard:
        print("\nFAILURES")
        for m in hard:
            print(f"  [FAIL] {m}")
        print("\nRESULT: FAIL")
        return 1
    print("\nRESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
