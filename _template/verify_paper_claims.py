#!/usr/bin/env python3
"""
Generic freeze checker for arXiv paper packages.

Reads FREEZE.yaml next to this script and validates a source checkout.

Usage:
  python verify_paper_claims.py --fsot-root /path/to/clone --strict-hash
  set FSOT_ROOT=...  # also accepted as --fsot-root default

Customize FREEZE.yaml keys for each paper. Extend checks below as needed.
"""

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
    import yaml  # type: ignore
except ImportError:
    yaml = None


def load_freeze() -> dict:
    text = FREEZE_PATH.read_text(encoding="utf-8")
    if yaml is not None:
        return yaml.safe_load(text) or {}
    # minimal fallback: only top-level string keys "key: value"
    out: dict = {}
    for line in text.splitlines():
        line = line.split("#", 1)[0].rstrip()
        if not line.strip() or line.strip().startswith("-"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--fsot-root",
        "--repo-root",
        dest="root",
        type=Path,
        default=os.environ.get("FSOT_ROOT") or os.environ.get("PAPER_REPO_ROOT"),
        help="Path to source repo clone",
    )
    ap.add_argument("--strict-hash", action="store_true")
    ap.add_argument("--require-cross-proof", action="store_true")
    args = ap.parse_args()

    if not FREEZE_PATH.is_file():
        print(f"ERROR: missing {FREEZE_PATH}", file=sys.stderr)
        return 2
    if not args.root:
        print("ERROR: pass --fsot-root / --repo-root or set FSOT_ROOT", file=sys.stderr)
        return 2

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2

    freeze = load_freeze()
    hard: list[str] = []
    soft: list[str] = []
    ok: list[str] = []

    print(f"Repo root: {root}")
    print(f"Freeze:    {FREEZE_PATH}")
    print(f"Edition:   {freeze.get('edition_id')}")
    print()

    # Oracle hash (optional)
    oracle = freeze.get("oracle") or {}
    if isinstance(oracle, dict):
        opath = oracle.get("path")
        exp = str(oracle.get("sha256") or "").upper()
        if opath and exp and exp not in ("REPLACE_OR_N_A", "REPLACE", ""):
            p = root / opath
            if p.is_file():
                got = sha256_file(p)
                if got == exp:
                    ok.append(f"oracle hash match: {got[:12]}…")
                else:
                    msg = f"oracle hash mismatch: {got} != {exp}"
                    (hard if args.strict_hash else soft).append(msg)
            else:
                (hard if args.strict_hash else soft).append(f"missing oracle file: {opath}")

    # Required artifacts
    arts = freeze.get("artifacts_required_after_bundle") or []
    if isinstance(arts, list):
        for rel in arts:
            if not isinstance(rel, str) or rel.startswith("REPLACE"):
                soft.append(f"skip placeholder artifact: {rel}")
                continue
            if (root / rel).is_file():
                ok.append(f"artifact present: {rel}")
            else:
                hard.append(f"missing artifact: {rel}")

    # Formal JSON (optional common path)
    formal = freeze.get("formal") or {}
    for cand in (
        "data/cross_proof_verification_report.json",
        "data/certificate.json",
        "data/publication_claims_manifest.json",
    ):
        p = root / cand
        if not p.is_file():
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            soft.append(f"could not parse {cand}: {e}")
            continue
        if "overall_ok" in data:
            if data["overall_ok"] is True:
                ok.append(f"{cand}: overall_ok true")
            else:
                (hard if args.require_cross_proof else soft).append(
                    f"{cand}: overall_ok={data.get('overall_ok')}"
                )
        if cand.endswith("certificate.json") and data.get("sorry_count_formal") == 0:
            ok.append("sorry_count_formal: 0")
        # nested formal spine
        spine = data.get("full_formal_spine") or {}
        atomic = spine.get("atomic_provable_count") or data.get("atomic_obligations")
        min_a = None
        if isinstance(formal, dict):
            min_a = formal.get("atomic_obligations_min")
        if atomic is not None and min_a is not None and int(min_a) > 0:
            if int(atomic) >= int(min_a):
                ok.append(f"atomic {atomic} >= {min_a}")
            else:
                hard.append(f"atomic {atomic} < {min_a}")

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

    print("\nRESULT: PASS — available freeze checks satisfied")
    print("Customize this script per paper for domain-specific metrics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
